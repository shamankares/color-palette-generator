# Color Palette Generator

This application generates a color palette based on the image using K-Means Clustering algorithm. This application only process the image in memory and does not store the uploaded image.

## Usage

    flask --app palettegen run

## Configurations

- MAX_CONTENT_LENGTH: Maximum file size allowed to be processed.

- MAX_NUM_OF_COLORS: Maximum number of colors palette allowed to be processed.

- CORS: Allowed origin of the request. It should be filled as JSON array string.
