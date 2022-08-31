file = input("Enter the Filename: ")
f = file.split(".")
ext=f[-1]
if ext=="py":
    print("The Extension is 'Python File'")
elif ext=="cpp":
    print("The Extension is 'C++ File'")
elif ext=="java":
    print("The Extension is 'Java File'")
elif ext=="c":
    print("The Extension is 'C File'")
elif ext=="js":
    print("The Extension is 'Javascript File'")
elif ext=="doc" or ext=="docx":
    print("The Extension is 'Document File'")
elif ext=="mp3" or ext=="mpa":
    print("The Extension is 'Audio File'")
elif ext=="rar" or ext=="tar":
    print("The Extension is 'Compressed File'")
elif ext=="iso" or ext=="bin":
    print("The Extension is 'Disc File'")
elif ext=="exe" or ext=="msi":
    print("The Extension is 'Executable File'")
elif ext=="jpg" or ext=="png":
    print("The Extension is 'Image File'")
elif ext=="mp4" or ext=="mkv":
    print("The Extension is 'Video File'")
else:
    print("Please Check The Filetype Entered")