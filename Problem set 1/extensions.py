extension = input("File name: ").strip().lower()#.endswith((".gif",".jpg",".jpeg",".png",".pdf",".txt",".zip"))

# it works but could be shorter
if extension.endswith(".gif"):
    print("image/gif")
elif extension.endswith(".jpg") or extension.endswith(".jpeg"):
    print("image/jpeg")
elif extension.endswith(".png"):
    print("image/png")
elif extension.endswith(".pdf"):
    print("application/pdf")
elif extension.endswith(".txt"):
    print("text/plain")
elif extension.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
"""
# second try, didn't work
match extension:
    case ".gif":
        print("image/gif")
    case ".jpg" | ".jpeg":
        print("image/jpeg")
    case ".png":
        print("image/png")
    case ".pdf":
        print("application/pdf")
    case ".txt":
        print("text/plain")
    case ".zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
"""