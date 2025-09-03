# File Extensions

**Description:**  
This project is a Python program called `extensions.py` that determines the media type (MIME type) of a file based on its extension. The program prompts the user for a file name and outputs its media type if the file ends with one of the following suffixes (case-insensitive):

- `.gif` → `image/gif`  
- `.jpg` or `.jpeg` → `image/jpeg`  
- `.png` → `image/png`  
- `.pdf` → `application/pdf`  
- `.txt` → `text/plain`  
- `.zip` → `application/zip`  

If the file has a different suffix or no suffix, the program outputs `application/octet-stream`, which is a common default.
