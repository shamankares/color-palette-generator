import numpy as np
import io

def parse_palette(palette):
  return list(map(
    lambda x: { 'R': x[0], 'G': x[1], 'B': x[2] },
    palette
  ))

def create_file(file_stream):
  file = io.BytesIO(file_stream)
  return file

def sort_by_hue(colors):
  hues = []
  c = colors.astype(np.float64) / 255
  c_maxs = np.max(c, axis=1)
  c_mins = np.min(c, axis=1)
  delta = c_maxs - c_mins

  for i in range(colors.shape[0]):
    idx_max = np.argmax(colors[i])

    if delta[i] == 0:
      hues.append(0)
    elif idx_max == 0:
      hues.append(60 * ((c[i, 1] - c[i, 2])/delta[i] % 6))
    elif idx_max == 1:
      hues.append(60 * ((c[i, 2] - c[i, 1])/delta[i] + 2))
    elif idx_max == 2:
      hues.append(60 * ((c[i, 0] - c[i, 1])/delta[i] + 4))
  
  conv = list(zip(hues, colors.tolist()))
  conv.sort(key=(lambda x: x[0]))
  
  return list(zip(*conv))[1]
