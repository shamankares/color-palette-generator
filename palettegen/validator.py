def validate_num_of_colors(num_of_colors):
  if type(num_of_colors) == str:
    if not num_of_colors.isnumeric():
      raise 'ValidationError'
  elif type(num_of_colors) != int:
    raise 'ValidationError'

def validate_image(image):
  content_type = image.content_type

  if 'image' not in content_type:
    raise 'ValidationError'
