import os
import face_recognition
import numpy as np

img_directory = './Images'
enc_directory = './Encodings'
for filename in os.listdir(img_directory):
    image_array = face_recognition.load_image_file(os.path.join(img_directory, filename))
    image_encoding = face_recognition.face_encodings(image_array)[0]
    print(image_encoding)
    enc_file_name = os.path.splitext(filename)[0]
    encode_file = open(os.path.join(enc_directory, enc_file_name), "wb")
    np.save(encode_file, image_encoding)
    print("Saved encoding File {} to {}".format(enc_file_name, encode_file.name))
    encode_file.close()

    # encoding = np.load(os.path.join(img_directory, filename))
    # print(os.path.join(directory, filename))
    # known_encodings.append(encoding)
    # known_faces.append(filename)
    # print(known_faces)
