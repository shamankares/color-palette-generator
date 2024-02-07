from . import validator, palettegen

from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

import os
import json

def create_app(config=None):
  app = Flask(__name__, instance_relative_config=True)
  app.config['MAX_CONTENT_LENGTH'] = 2 * 1000 * 1000 # default max file size

  if config is None:
    if not app.config.from_pyfile('config.py', silent=True):
      app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
      app.config['MAX_CONTENT_LENGTH'] = os.getenv('MAX_CONTENT_LENGTH')
  else:
    app.config.from_mapping(config)
  
  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  @app.errorhandler(HTTPException)
  def handle_exception(err):
    response = err.get_response()
    response.data = json.dumps({
        "statusCode": err.code,
        "status": 'failed',
        "message": err.description,
    })
    response.content_type = "application/json"
    return response

  @app.post('/generate')
  def generate_palette():
    num_of_colors = None
    image = None
    
    try:
      validator.validate_request_properties(request)

      num_of_colors = request.form['numOfColors']
      image = request.files['image']
      
      validator.validate_num_of_colors(num_of_colors)
      validator.validate_image(image)
    except HTTPException as err:
      raise err

    image_stream = image.stream.read()
    palette = palettegen.generate_palette(image_stream, int(num_of_colors))

    return jsonify({
      'statusCode': 200,
      'status': 'success',
      'data': palette
    })
  
  return app
