import time
import cv2
import mediapipe as mp

print('hi')
# mp_hands = mp.solutions.hands # detect hands
print('1)')
# mp_draw = mp.solutions.drawing_utils # draw landmarks
print ('2')
capture = cv2.VideoCapture(0) 
print(capture.isOpened())
capture.set(3, 1280) # width
capture.set(4, 720) # height

def main():
    while True:
        # camera takes too long to load
        attempt = 0
        success, img = capture.read()
        while not success and attempt < 3:
            time.sleep(0.2)
            success, img = capture.read()
            attempt += 1
        if not success:
            print("fail")
            break
        
        img = cv2.flip(img, 1) # mirror
        cv2.imshow("hand tracker", img)
        if cv2.waitKey(1) & 0xFF == ord('x'): # check every ms if x key pressed; exit
            break
    capture.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__" :
    main()