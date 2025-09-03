# Watch on YouTube

This project implements a Python program to extract YouTube URLs from HTML `<iframe>` elements and convert them to the shorter, shareable `youtu.be` format.

## Description

The program `watch.py`:

- Implements a function `parse(s)` that:
  - Takes a string of HTML as input.
  - Searches for an `<iframe>` element with a `src` attribute pointing to a YouTube video.
  - Converts the YouTube `embed` URL to a `youtu.be` URL.
  - Returns the converted URL as a string, or `None` if no YouTube URL is found.

- Supported input formats for YouTube URLs in `src`:
  - `http://youtube.com/embed/VIDEO_ID`
  - `https://youtube.com/embed/VIDEO_ID`
  - `https://www.youtube.com/embed/VIDEO_ID`
  - `http://www.youtube.com/embed/VIDEO_ID`
