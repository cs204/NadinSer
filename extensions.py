name = input("File name: ")
ext = name.split('.')[-1]
match ext:
    case "jpg":
        print("image/jpeg")
    case "pdf":
        print("application/pdf")
    case "gif":
        print("image/gif")
    case "jpeg":
        print("image/png")
    case "png" :
        print("image/png")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")