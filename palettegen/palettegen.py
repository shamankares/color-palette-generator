from . import utils

import numpy as np
from sklearn.cluster import KMeans
from PIL import Image

def generate_palette(image_stream, num_of_colors):
  image_file = utils.create_file(image_stream)
  img = Image.open(image_file).convert('RGB')

  width, height = img.size
  img = img.resize((int(width / 2), int(height / 2))) # Kecilkan gambar untuk mempercepat komputasi

  img_px = np.reshape(img, (-1, 3))

  k_means = KMeans(n_clusters=num_of_colors, n_init='auto', random_state=0).fit(img_px)
  palette = k_means.cluster_centers_.astype(np.uint8)
  palette_sorted = utils.sort_by_hue(palette)

  img.close()

  return { 'palette': utils.parse_palette(palette_sorted) }
