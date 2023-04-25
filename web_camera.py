import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Open the video capture device (0 is the default camera)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    if not ret:
        # If there is no frame, break out of the loop
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the output
    cv2.imshow('frame', frame)

    # Stop the loop if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Close the window if the user presses 'x'
    if cv2.getWindowProperty('frame', cv2.WND_PROP_VISIBLE) < 1:
        break

# Release the capture device and destroy all windows
cap.release()
cv2.destroyAllWindows()
