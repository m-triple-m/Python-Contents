import os

path = "d:/video_thumbnails"

ext = []

for f in os.listdir(path):
    print(f)
    if os.path.isfile(os.path.join(path, f)):
        ext.append(f.split('.')[-1])

ext = set(ext)

try:
    for e in ext:
        os.mkdir(os.path.join( path, e.upper() ))
except Exception as e:
    print(e)

for f in os.listdir(path):
    if os.path.isfile(os.path.join(path, f)):
        old_path = os.path.join(path, f)
        new_path = os.path.join(path, f.split('.')[-1].upper(), f )
        os.rename( old_path, new_path )