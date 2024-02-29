# API

HTTP POST /generate

### Request Body

To send the request, you must use `multipart/form-data` as the `Content-Type` header.

| Name          | Type                  | Description |
| ------------- | --------------------- | ----------- |
| `numOfColors` | `number` or `string`  | Specify the number of colors needed for generating a palette |
| `image`       | `file`                | Upload an image for which the color palette needed to be generated. This paramater should be an image file and less than 2MB. |

### JSON Response

| Name         | Description |
| ------------ | ----------- |
| `statusCode` | Response code. |
| `status`     | Status of the response. |
| `message`    | Response message. This property may be absent if succeeded. |
| `data`       | Data returned from server if succeeded. This property may be absent if server returned the error instead. |

#### Success 200

The following properties are contained inside `data` property.

| Name      | Description |
| --------- | ----------- |
| `palette` | An array of colors palette. The length of the palette depends on requested number of colors. |

#### Error 4xx

| Error Code       | Description |
| ---------------- | ----------- |
| `400`            | Returned if the payload does not contains the needed properties, the property has invalid type, or the file is not an image file. |
| `413`            | Returned if the image file larger than 2MB. |
