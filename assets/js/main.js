import * as events from './events.js';

document.addEventListener('DOMContentLoaded', events.loadAdditionalConfig);

const input = document.getElementById('image');
const inputPreview = document.getElementById('preview');
input.addEventListener('change', () => events.updateImageDisplay(input, inputPreview));

const form = document.getElementById('uploadImage');
form.addEventListener('submit', events.processImages);
