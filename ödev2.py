import cv2
import numpy as np

# Kamera bağlantısını başlattım
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # RGB görüntüsünü HSV formatına dönüştürdüm
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Yeşil renge ait HSV aralığını belirledim
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])

    # Mavi renge ait HSV aralığını belirledim
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Belirlenen aralıktaki renkleri beyaz yapacak maskeleri oluşturdum
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    # Yeşil ve mavi renkte olan yerleri siyah yaptım
    mask_green_blue = cv2.bitwise_or(mask_green, mask_blue)
    mask_not_green_blue = cv2.bitwise_not(mask_green_blue)

    # Orijinal görüntüde belirtilen aralıktaki renkleri siyah yapın, diğer renkleri gösterdim
    result = cv2.bitwise_and(frame, frame, mask=mask_not_green_blue)

    # Görüntüleri gösterin
    cv2.imshow('Original', frame)
    cv2.imshow('Result', result)

    # 'q' tuşuna basılınca döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera bağlantısını serbest bıraktım
cap.release()
cv2.destroyAllWindows()