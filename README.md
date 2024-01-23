# Python Image Background Remover

## Overview

This Python script provides a simple and user-friendly interface to remove the background from images using the BytesIO, easygui, PIL (Pillow), and rembg libraries. The script allows users to select an image file, process it to remove the background, and save the result.

## Prerequisites

Ensure that you have the following libraries installed before running the script:

- BytesIO
- easygui
- Pillow (PIL)
- rembg

You can install these libraries using the following command:

```bash
pip install rembg easygui pillow
```

Make sure to have rembg's dependencies installed as well. Refer to the [rembg documentation](https://pypi.org/project/rembg/) for more information.

## How to Use

1. Run the script using a Python interpreter.

```bash
python main.py
```

2. The script will prompt you to select an image file. Use the file dialog that appears to navigate to and select the desired image.

3. The script will prompt you to save the image.

4. When you click save, the script will then process the image and remove the background.

5. After saving the image an easygui message dialogue box will appear with success message.

## Additional Notes

- The script uses the rembg library to perform background removal. Make sure to comply with the license and usage terms of the rembg library.

- Feel free to customize the script according to your needs, such as handling different file formats, adding error handling, or incorporating additional features.

- For more information on the libraries used, refer to the official documentation for [BytesIO](https://docs.python.org/3/library/io.html#io.BytesIO), [easygui](https://easygui.readthedocs.io/en/latest/), [Pillow](https://pillow.readthedocs.io/en/stable/), and [rembg](https://pypi.org/project/rembg/).

- This script is a basic implementation and may not cover all edge cases. Feel free to enhance it based on your requirements.
