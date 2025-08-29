# CS50 P-Shirt

This project allows you to virtually try on a CS50 T-shirt by overlaying the CS50 shirt image on any photo using Python and Pillow.

## Description

The program `shirt.py`:

- Accepts exactly two command-line arguments:
  1. Input image filename (`.jpg` or `.png`)
  2. Output image filename (`.jpg` or `.png`)
- Resizes and crops the input image to match the shirt image size.
- Overlays `shirt.png` (with transparent background) on the input photo.
- Saves the result as the output image.

The program will exit with an error if:

- There are not exactly two command-line arguments.
- The input or output file is not `.jpg`, `.jpeg`, or `.png`.
- The input and output file extensions differ.
- The specified input image does not exist.

## Requirements

- Python 3
- `Pillow` library (`pip install pillow`)

## Setup

1. Create a folder and navigate into it:

```bash
mkdir shirt
cd shirt
