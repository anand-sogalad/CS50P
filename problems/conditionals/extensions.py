def main():
    value = get_user_input()
    new_value = validate_input(value)
    print(new_value)


def get_user_input():
    return input("File name: ")


def validate_input(val):
    extension = val.split(".")[-1]
    match extension:
        case "gif":
            return "image/gif"
        case "jpg" | "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _:
            return "application/octet-stream"


if __name__ == "__main__":
    main()
