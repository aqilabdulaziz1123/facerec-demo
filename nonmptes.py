import face_recognition
import multiprocessing
import numpy as np
import os
from time import time
import sys
from multiprocessing import Process, Pool, Manager, cpu_count, set_start_method, Queue
# set_start_method('spawn')


# Global = Manager().Namespace()

# Global.knownface = []
# Global.name = []
# Global.buff_num = 1
# Global.is_exit = False

knownface = []
name = []
# Global.buff_num = 1
# Global.is_exit = False

# q = Queue()

# p = []

x = 1
y = 1
dur = 0

def process(worker_id, filename, Global, worker_num):
    known = Global.knownface
    image = face_recognition.load_image_file('./db' + filename)
    encoded = face_recognition.face_encodings(image)
    for encode in encoded:
        matches = face_recognition.compare_faces(known, encode)
        if matches:
            # print(filename)
            pass
    # dur += time() - start

# def f(filename):
#     print(filename)
#     image = face_recognition.load_image_file('./tes/' + filename)
#     encoded = face_recognition.face_encodings(image)
#     for encode in encoded:
#         matches = face_recognition.compare_faces(knownface, encode)
#         if matches:
#             # print(filename)
#             pass

if len(sys.argv) > 1:
    x = int(sys.argv[1])//6

for files in os.listdir('./db'):
    image = face_recognition.load_image_file('./db/' + files)
    knownface.append(face_recognition.face_encodings(image)[0])
    name.append(files.split('.')[0])
filenames = []
for i in range(x):
    for filename in os.listdir('./tes'):
        filenames.append(filename)
for files in filenames:
    start = time()
    image = face_recognition.load_image_file(f"./tes/{files}")
    encodes = face_recognition.face_encodings(image)
    for encode in encodes:
        matches = face_recognition.compare_faces(knownface, encode)
        for i in range(len(name)):
            if matches[i]:
                print(name[i])
                pass
    dur += time() - start
print(f"photos processed : {len(filenames)}")
print(f"time taken : {dur} seconds")
print(f"average time per photo processed : {dur/len(filenames)} seconds")



# if __name__ == '__main__':
#     if len(sys.argv) <= 1:
#         print('usage = py tes.py [number of photo to process (multiple of 6)] [how many processor used]')
#         exit(0)
#     if len(sys.argv) > 1:
#         x = int(sys.argv[1])//6
#     if len(sys.argv) > 2:
#         y = int(sys.argv[2])
#     for files in os.listdir('./db'):
#         image = face_recognition.load_image_file('./db/' + files)
#         knownface.append(face_recognition.face_encodings(image)[0])
#         name.append(files.split('.')[0])
#     files = []
#     for i in range(x):
#         for filename in os.listdir('./tes'):
#             files.append(filename)
#     print(files)
#     start = time()
#     with Pool(processes=y) as pool:
#         pool.map(f, files)
#     dur = time() - start
#     num = len(files)
