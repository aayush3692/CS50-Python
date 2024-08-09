word = input("File name: ")

answer = word.lower()

if '.gif' in answer:
    print("image/gif")
elif '.png' in answer:
    print("image/png")
elif '.jpg' in answer:
    print("image/jpeg")
elif '.jpeg' in answer:
    print("image/jpeg")
elif '.pdf' in answer:
    print("application/pdf")
elif '.zip' in answer:
    print("application/zip")
elif '.txt' in answer:
    print("text/plain")

else:
    print("application/octet-stream")


