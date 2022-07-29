import cv2
import numpy as np
import time
import PoseModule as pm



#Track Pushups
def track_push(cap, detector):
    # direction : 0 -> up : 1 -> down
    count = 0
    dir = 0
    pTime = 0

    while True:
        success, img = cap.read()
        #resuze and fit the video to frame
        # img = cv2.resize(img, (1280, 720))

        # img = cv2.imread("videos/images/push-angle.jpeg")
        img = detector.findPose(img, False)

        lmList = detector.findPosition(img, False)
        if len(lmList) != 0:

            ## --- Get tracking for right and left arm --
            #Right Arm
            detector.findAngle(img, 12, 14, 16)

            #Left Arm
            angle = detector.findAngle(img, 11, 13, 15)

            # set up range for pushup
            low = 70
            high = 150
            per = np.interp(angle, (low, high), (0, 100))

            # print( angle ,"->" , per)
            # calculate the number of pushups
            if per == 100:
                if dir == 0:
                    count += 0.5
                    dir = 1
            if per == 0:
                if dir == 1:
                    count += 0.5
                    dir = 0

            # dislpay count
            cv2.putText(img, str(int(count)), (50, 50),
                        cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
            print(count)

            #Display FPS
            cTime = time.time()
            fps = 1/(cTime - pTime)
            pTime = cTime
            cv2.putText(img, str(int(fps)), (50, 100),
                        cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)

            # get a loading bar
            bar = np.interp(angle, (low, high), (650, 100))
            #Draw bar
            cv2.rectangle(img, (1100, 100), (1175, 650), (0, 255, 0), 3)
            cv2.rectangle(img, (1100, int(bar)), (1175, 650),
                          (0, 255, 0), cv2.FILLED)
            #show percentage
            cv2.putText(img, str(int(per)), (1100, 75),
                        cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)



#Track Squat
def track_squat(cap, detector):
    # direction : 0 -> up : 1 -> down
    count = 0
    dir = 0
    pTime = 0

    while True:
        success, img = cap.read()
        #resuze and fit the video to frame
        # img = cv2.resize(img, (1280, 720))

        # img = cv2.imread("videos/images/push-angle.jpeg")
        img = detector.findPose(img, False)

        lmList = detector.findPosition(img, False)
        if len(lmList) != 0:

            ## --- Get tracking for right and left arm --
            #Right Leg
            detector.findAngle(img, 24, 26, 28)

            #Left Leg
            angle = detector.findAngle(img, 23, 25, 27)

            # set up range for pushup
            low = 70
            high = 150
            per = np.interp(angle, (low, high), (0, 100))

            # print( angle ,"->" , per)
            # calculate the number of pushups
            if per == 100:
                if dir == 0:
                    count += 0.5
                    dir = 1
            if per == 0:
                if dir == 1:
                    count += 0.5
                    dir = 0

            # dislpay count
            cv2.putText(img, str(int(count)), (50, 50),
                        cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
            print(count)

            #Display FPS
            cTime = time.time()
            fps = 1/(cTime - pTime)
            pTime = cTime
            cv2.putText(img, str(int(fps)), (50, 100),
                        cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)

            # get a loading bar
            bar = np.interp(angle, (low, high), (650, 100))
            #Draw bar
            cv2.rectangle(img, (1100, 100), (1175, 650), (0, 255, 0), 3)
            cv2.rectangle(img, (1100, int(bar)), (1175, 650),
                          (0, 255, 0), cv2.FILLED)
            #show percentage
            cv2.putText(img, str(int(per)), (1100, 75),
                        cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


# Open webcam
cap = cv2.VideoCapture('videos/pushup6.mp4')

# Mediapipe Pose model instance
while cap.isOpened():
    user_choice = int(
            input(
                'Which exercise would you like to do? Please enter 1, 2 or 3.\n1. Squat \n2. Pushup \n3. SuryaNamaskar\n'))

    detector = pm.poseDetector()

    # Recognise particular exercise based on user input
    if user_choice == 1:
        print('1')
        track_squat(cap, detector)
    elif user_choice == 2:
        print('2')
        track_push(cap, detector)
    else:
        print('123')

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break




