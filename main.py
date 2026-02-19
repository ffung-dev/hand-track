import cv2
import mediapipe as mp

mpHands = mp.solutions.hands # detect hands
mpDraw = mp.solutions.drawing_utils # draw landmarks
capture = cv2.VideoCapture(0) 
print(capture.isOpened())

capture.set(3, 1280) # width
capture.set(4, 720) # height
def main():
    print('0')
    with mpHands.Hands(
        max_num_hands = 2,
        min_detection_confidence = 0.8,
        min_tracking_confidence = 0.8,
    ) as hands: 
        while True:
            success,img = capture.read()    
            if not success:
                print('fail')
                break

            img = cv2.flip(img, 1) # mirror
            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # cv2 default is bgr, mp requires rgb
            
            result = hands.process(rgb) # get data
            if result.multi_hand_landmarks: # hand detected or nah
                for hand_lms in result.multi_hand_landmarks:
                    mpDraw.draw_landmarks(
                        img,
                        hand_lms,
                        mpHands.HAND_CONNECTIONS,
                    )
                    # drawing_spec.color = (242, 84, 142)

                    fingertips = {
                        "thumb": hand_lms.landmark[4],
                        "index" : hand_lms.landmark[8],
                        "middle" : hand_lms.landmark[12],
                        "ring" : hand_lms.landmark[16],
                        "pinky" : hand_lms.landmark[20],
                    }
            cv2.imshow("hand tracker", img)
            if cv2.waitKey(1) & 0xFF == ord('x'): # check every ms if x key pressed; exit
                break

    
    capture.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__" :
    main()