import cv2
import pandas
from datetime import datetime

first_frame = None
new_object_list = [None, None]
new_object_times = []

df = pandas.DataFrame(columns=["Start", "End"])

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    new_object = False

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (_, cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:  # if object is less than 100x100 size ignore it
            continue

        new_object = True
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0))

    new_object_list.append(new_object)
    new_object_list = new_object_list[-2:]

    if new_object_list[-1] is True and new_object_list[-2] is False:
        new_object_times.append(datetime.now())
    if new_object_list[-1] is False and new_object_list[-2] is True:
        new_object_times.append(datetime.now())

    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        if new_object is True:
            new_object_times.append(datetime.now())
        break


print(new_object_times)

for i in range(0, len(new_object_times), 2):
    df = df.append({"Start": new_object_times[i], "End": new_object_times[i + 1]}, ignore_index=True)

df.to_csv("New_object_times.csv")

video.release()
cv2.destroyAllWindows()
