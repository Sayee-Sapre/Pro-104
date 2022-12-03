import cv2

img = cv2.imread("solar-system.jpg")

cv2.imshow("output",img)

cv2.waitKey(0)

cv2.putText(
    img,
    "Sun",
    (80,100),
    cv2.FONT_HERSHEY_COMPLEX,
    2,
    (255,250,250)
)

cv2.putText(
    img,
    "Mercury",
    (110,250),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,250,250)
)

cv2.putText(
    img,
    "Venus",
    (200,255),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,250,250)
)

cv2.putText(
    img,
    "Earth",
    (290,260),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,250,250)
)

cv2.putText(
    img,
    "Mars",
    (385,260),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,250,250)
)

cv2.putText(
    img,
    "Jupiter",
    (485,100),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,250,250)
)

cv2.putText(
    img,
    "Saturn",
    (685,120),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,250,250)
)

cv2.putText(
    img,
    "Uranus",
    (910,150),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,250,250)
)

cv2.putText(
    img,
    "Neptune",
    (1048,150),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,250,250)
)



cv2.imwrite("Solar_systemwithname.jpg",img)
