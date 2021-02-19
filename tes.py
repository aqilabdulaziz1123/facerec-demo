import face_recognition
import numpy as np
import os
from time import time
import sys

knownface = []
name = []

x = 1
dur = 0

if len(sys.argv) > 1:
    x = int(sys.argv[1])

for files in os.listdir('./db'):
    image = face_recognition.load_image_file('./db/' + files)
    knownface.append(face_recognition.face_encodings(image)[0])
    name.append(files.split('.')[0])

for i in range(x):
    for files in os.listdir('./tes'):
        start = time()
        image = face_recognition.load_image_file(f"./tes/{files}")
        encodes = face_recognition.face_encodings(image)
        for encode in encodes:
            matches = face_recognition.compare_faces(knownface, encode)
            for i in range(len(name)):
                if matches[i]:
                    # print(name[i])
                    pass
        dur += time() - start

num = len(os.listdir('./tes'))*x
print(f"photos processed : {num}")
print(f"time taken : {dur} seconds")
print(f"average time per photo processed : {dur/num} seconds")
