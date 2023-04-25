import cv2

# Загрузка модуля
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Считывание входящего видео
cap = cv2.VideoCapture('data\media.mp4')

while cap.isOpened():
    
    # Считывание видеопотока
    ret, frame = cap.read()

    if not ret:
        break

    # Конвертация видеопотока в оттенки серого
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Распознование лиц на видеопотоке
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.4, minNeighbors=5)

    # Прорисовка прямоугольников вокруг лиц
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Вывод результата
    cv2.imshow('frame', frame)

    # Остановка программы нажатием на кнопку "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Остановка программы нажатием на крестик
    if cv2.getWindowProperty('frame', cv2.WND_PROP_VISIBLE) < 1:
        break

# Закрытие активного окна
cap.release()
cv2.destroyAllWindows()
