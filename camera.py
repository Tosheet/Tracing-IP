import cv2
from exif import Image
from PIL import Image as PillowImage
from PIL import ExifTags
import socket
import socket
import re, uuid


#Camera capture
cam_port = 0
cam = cv2.VideoCapture(cam_port)

result, image = cam.read()

if result:

	cv2.imwrite("cam2.jpg", image)





