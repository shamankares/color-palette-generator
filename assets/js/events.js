export async function copyHexColor(event) {
  const colorHex = event.target.getAttribute('hex-color');
  await navigator.clipboard.writeText(colorHex)
    .then(() => alert('Hex color value has been copied.'))
    .catch((error) => console.error(error));
}

export function toHexColor({ R, G, B }) {
  return `${R.toString(16)}${G.toString(16)}${B.toString(16)}`;
}

export function updateImageDisplay(uploader, preview){
    while (preview.firstChild) {
        preview.removeChild(preview.firstChild);
    }

    const file = uploader.files[0];
    const image = document.createElement('img');
    image.src = URL.createObjectURL(file);
    preview.append(image);
}

export function renderPalette({ data: { palette } }) {
  const resultPreview = document.querySelector('#result .preview');
  while (resultPreview.firstChild) {
    resultPreview.removeChild(resultPreview.firstChild);
  }

  for (const color of palette) {
    const colorPalette = document.createElement('button');
    colorPalette.setAttribute('class', 'palette');
    colorPalette.setAttribute('hex-color', toHexColor(color));
    colorPalette.setAttribute('style', `background-color: rgb(${color.R}, ${color.G}, ${color.B});`);
    colorPalette.addEventListener('click', copyHexColor);
    resultPreview.append(colorPalette);
  }
}

export function renderError(errorMessage) {
  const message = document.querySelector('p.load-message');
  message.textContent = errorMessage;
}

export async function processImages(event) {
    event.preventDefault();

    const resultPreview = document.querySelector('#result .preview');
    resultPreview.replaceChildren(); // clear the result preview

    const message = document.createElement('p');
    message.className = 'load-message';
    message.textContent = 'Processing...';
    resultPreview.append(message);

    const form = document.getElementById('uploadImage');
    const url = form.getAttribute('action');
    const formData = new FormData(form);
    
    await fetch(url, {
        method: 'POST',
        body: formData,
    })
    .then((res) => {
      if (res.ok) return res.json();

      return res.json().then(({
        message: errorMessage,
        statusCode,
      }) => {
        if (statusCode === 500) {
          throw new Error('Something is wrong in server. Try again later.');
        }
        throw new Error(errorMessage);
      });        
    })
    .then(renderPalette)
    .catch(renderError);
}

export function loadAdditionalConfig() {
  const form = document.getElementById('uploadImage');
  form.setAttribute('action', `${process.env.BACKEND_PROTOCOL}://${process.env.BACKEND_DOMAIN}:${process.env.BACKEND_PORT}/generate`);
  
  const numOfColors = document.getElementById('numOfColors');
  numOfColors.setAttribute('max', 16);
}
