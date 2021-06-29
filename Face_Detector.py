import cv2
from random import randrange
#Load some pre-trained data on face frontal from opencv (haar cascade algo)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#choose an image to detect faces in
#img = cv2.imread('RDJ.jpg')
# Capture video from webcam
webcam = cv2.VideoCapture(0) #captures video, if 0 is put in bracket it accesses the webcam. to capture a video put video file name

# Iterate forever over frames
while True:

    # Read the current frame
    successful_frame_read, frame = webcam.read()
    # Must convert to Grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect Faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # Drraw rectangle around face (1-coordinates of top left vertex, 2-(x+w, y+h), 3-for color(B, G, R), 4- Border thickness of the rectangle)
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 5)

    # Display image with face spotted 
    cv2.imshow('Lucifer Face Detector', frame)

    # Wait here in the code and listen fora key press (pauses execution of code, in this case it closess the image as soon as any key is pressed)
    key = cv2.waitKey(1)  #if bracket left blank, waitkey will only  capture one frame at a time, so we give it "1" now it will automstically hit a key after 1 milisecond.
    # Stop if Q key is pressed
    if key==81 or key==113: #81-113 ASCII code
        break

    
#Release the videoCapture object
webcam.release()

"""
# Must convert to Grayscale
#grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect Faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# Drraw rectangle around face (1-coordinates of top left vertex, 2-(x+w, y+h), 3-for color(B, G, R), 4- Border thickness of the rectangle)
#(x, y, w, h) = face_coordinates[0]
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 5)

print(face_coordinates)

# Display image with face spotted 
#cv2.imshow('Lucifer Face Detector', img)

# Wait here in the code and listen fora key press (pauses execution of code, in this case it closess the image as soon as any key is pressed)
#cv2.waitKey()



print("Code Completed")
"""