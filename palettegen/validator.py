from werkzeug.exceptions import BadRequest

def validate_request_properties(req):
  if 'numOfColors' not in req.form:
    raise BadRequest(description="Missing 'numOfColors' property")
  
  if 'image' not in req.files:
    raise BadRequest(description="Missing 'image' property")

def validate_num_of_colors(num_of_colors):
  if type(num_of_colors) == str:
    if not num_of_colors.isnumeric():
      raise BadRequest(description='numOfColors must be a numeric string or number')
  elif type(num_of_colors) != int:
    raise BadRequest(description='numOfColors must be a numeric string or number')

def validate_image(image):
  content_type = image.content_type

  if 'image' not in content_type:
    raise BadRequest(description='The file must be an image file')

def validate_requested_num_of_colors(num_of_colors, limit):
  if num_of_colors > limit:
    raise BadRequest(description=f"The requested 'numOfColors' exceeds the specified limit (Max: {limit})")