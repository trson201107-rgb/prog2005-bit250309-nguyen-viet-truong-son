def get_filename(path):
    return path.split("\\")[-1]

def get_songname(path):
    filename = path.split("\\")[-1]
    return filename.rsplit(".", 1)[0]

path = "d:\\music\\muabui.mp3"

print(get_filename(path))
print(get_songname(path))