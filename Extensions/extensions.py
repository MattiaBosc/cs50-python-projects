name = input("File name: ")
name = name.lower().strip()

extension = name.split(".")[-1]

match extension:
    case "gif" | "jpg" | "jpeg" | "png":
        if extension == "jpg":
            extension = "jpeg"
        print(f"image/{extension}")
    case "pdf" | "zip":
        print(f"application/{extension}")
    case "txt":
        print(f"text/plain")
    case _:
        print("application/octet-stream")
