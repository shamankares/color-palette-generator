from pathlib import Path

resource = Path(__file__).parent / "resources"

def test_upload_invalid_property(client):
  response_no_image = client.post("/generate", data={
    "numOfColors": 3
  })
  response_no_num_of_colors = client.post("/generate", data={
    "image": (resource/"tepi_pantai.jpg").open("rb")
  })

  assert response_no_image.status_code == 400
  assert response_no_num_of_colors.status_code == 400

def test_upload_invalid_num_of_colors(client):
  response = client.post("/generate", data={
    "image": (resource/"tepi_pantai.jpg").open("rb"),
    "numOfColors": "abcd"
  })
  assert response.status_code == 400

def test_upload_invalid_image_file(client):
  response = client.post("/generate", data={
    "image": (resource/"test.txt").open("rb"),
    "numOfColors": 6
  })
  assert response.status_code == 400

def test_upload_too_large_image_file(client):
  response = client.post("/generate", data={
    "image": (resource/"cumi_naik_mouse.png").open("rb"),
    "numOfColors": 6
  })
  assert response.status_code == 413

def test_upload_image_file(client):
  num_of_colors = 6
  response = client.post("/generate", data={
    "image": (resource/"tepi_pantai.jpg").open("rb"),
    "numOfColors": num_of_colors
  })
  assert response.status_code == 200

  data = response.get_json()
  assert len(data["palette"]) == num_of_colors
  for color in data["palette"]:
    assert type(color) == dict
    assert 'R' in color
    assert 'G' in color
    assert 'B' in color
