import face_recognition
import numpy as np
import os

known_faces = []
enc_directory = './Encodings'
test_directory = './Test'


print("Testing {} images from test directory".format(len(os.listdir(test_directory))))
for filename in os.listdir(enc_directory):
    known_face = np.load(os.path.join(enc_directory, filename))
    known_faces = [
        known_face
    ]
    print("Testing encoding of {}".format(filename))
    found_images = 0
    for test_file in os.listdir(os.path.join(test_directory, filename)):
        test_dir_spe = os.path.join(test_directory, filename)
        test_image = face_recognition.load_image_file(os.path.join(test_dir_spe, test_file))
        test_face_encoding = face_recognition.face_encodings(test_image)[0]
        result = face_recognition.compare_faces(known_faces, test_face_encoding)
        if result[0]:
            found_images += 1
            print("Picture of {} was found in file {}".format(filename, test_file))
    print("Found {} in {} images out of {} test images".format(filename, found_images, len(os.listdir(test_dir_spe))))
