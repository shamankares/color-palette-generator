from . import validator, palettegen

from flask import Flask, request, jsonify, render_template
from werkzeug.exceptions import abort

import os

def create_app(config=None):
  app = Flask(__name__, instance_relative_config=True)

  if config is None:
    app.config.from_pyfile('config.py', silent=True)
  else:
    app.config.from_mapping(config)
  
  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  @app.post('/generate')
  def generate_palette():
    num_of_colors = request.form['numOfColors']
    image = request.files['image']
    
    try:
      validator.validate_num_of_colors(num_of_colors)
      validator.validate_image(image)
    except:
      abort(400)

    image_stream = image.stream.read()
    palette = palettegen.generate_palette(image_stream, int(num_of_colors))

    return jsonify(palette)
  
  return app
