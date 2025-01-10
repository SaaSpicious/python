
try:
    file = open("file_not_exists.txt")
    file.read()
except FileNotFoundError as filename:
    file = open("file_not_exists.txt","w")
    print(f"File {filename} doesn't exist!")
except:
    print("Whooopsie, das ging schief!")
else:
    print("Yeah, we're good!")
finally:
    file.close()
    print("File was closed!")
    raise TypeError("I just made this error up out of thin air...")