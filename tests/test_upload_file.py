from pathlib import Path

resource = Path(__file__).parent / "resources"

def test_upload_invalid_property(client):
  response_no_image = client.post("/generate", data={
    "numOfColors": 3
  })
  response_no_num_of_colors = client.post("/generate", data={
    "image": (resource/"tepi_pantai.jpg").open("rb")
  })

  res_no_image_json = response_no_image.get_json()
  res_no_num_of_colors_json = response_no_num_of_colors.get_json()

  assert res_no_image_json['statusCode'] == 400
  assert res_no_image_json['status'] == 'failed'
  assert res_no_image_json['message'] == "Missing 'image' property"

  assert res_no_num_of_colors_json['statusCode'] == 400
  assert res_no_num_of_colors_json['status'] == 'failed'
  assert res_no_num_of_colors_json['message'] == "Missing 'numOfColors' property"

def test_upload_invalid_num_of_colors(client):
  response = client.post("/generate", data={
    "image": (resource/"tepi_pantai.jpg").open("rb"),
    "numOfColors": "abcd"
  })

  res_json = response.get_json()

  assert res_json['statusCode'] == 400
  assert res_json['status'] == 'failed'
  assert res_json['message'] == 'numOfColors must be a numeric string or number'

def test_upload_invalid_image_file(client):
  response = client.post("/generate", data={
    "image": (resource/"test.txt").open("rb"),
    "numOfColors": 6
  })

  res_json = response.get_json()

  assert res_json['statusCode'] == 400
  assert res_json['status'] == 'failed'
  assert res_json['message'] == 'The file must be an image file'

def test_upload_too_large_image_file(client):
  response = client.post("/generate", data={
    "image": (resource/"cumi_naik_mouse.png").open("rb"),
    "numOfColors": 6
  })

  res_json = response.get_json()

  assert res_json['statusCode'] == 413
  assert res_json['status'] == 'failed'
  assert res_json['message']

def test_upload_image_file(client):
  num_of_colors = 6
  response = client.post("/generate", data={
    "image": (resource/"tepi_pantai.jpg").open("rb"),
    "numOfColors": num_of_colors
  })
  res_json = response.get_json()
  data = res_json['data']

  assert res_json['statusCode'] == 200
  assert res_json['status'] == 'success'
  assert len(data["palette"]) == num_of_colors
  for color in data["palette"]:
    assert type(color) == dict
    assert 'R' in color
    assert 'G' in color
    assert 'B' in color
