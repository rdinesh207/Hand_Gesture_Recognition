import cv2 
import mediapipe as mp
import pyautogui
import vlc
import time

def count_fingers(lst):
    cnt = 0

    thresh = (lst.landmark[0].y*100 - lst.landmark[9].y*100)/2

    if (lst.landmark[5].y*100 - lst.landmark[8].y*100) > thresh:
        cnt += 1

    if (lst.landmark[9].y*100 - lst.landmark[12].y*100) > thresh:
        cnt += 1

    if (lst.landmark[13].y*100 - lst.landmark[16].y*100) > thresh:
        cnt += 1

    if (lst.landmark[17].y*100 - lst.landmark[20].y*100) > thresh:
        cnt += 1

    if (lst.landmark[5].x*100 - lst.landmark[4].x*100) > 6:
        cnt += 1

    return cnt 

cap = cv2.VideoCapture(0)

drawing = mp.solutions.drawing_utils
hands = mp.solutions.hands
hand_obj = hands.Hands(max_num_hands=1)
instance = vlc.Instance('--no-xlib')

COUNTER, FPS = 0, 0
START_TIME = time.time()
fps_avg_frame_count = 10
# Create a MediaPlayer object
player = instance.media_player_new()

# Create a Media object
media = instance.media_new('SPIDER-MAN_ INTO THE SPIDER-VERSE - Official Trailer (HD).mp4')  # replace with your media file path

# Set the media to the player
player.set_media(media)

duration=player.get_length()
total_duration=duration / 1000

start_init = False 

prev = -1

while True:
    end_time = time.time()
    _, frm = cap.read()
    frm = cv2.flip(frm, 1)

    res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

    if res.multi_hand_landmarks:

        hand_keyPoints = res.multi_hand_landmarks[0]

        cnt = count_fingers(hand_keyPoints)

        if not(prev==cnt):
            if not(start_init):
                start_time = time.time()
                start_init = True

            elif (end_time-start_time) > 0.2:
                if (cnt == 1):
                    pyautogui.press("right")
                    print('skip 10 secs')
                    current_time=player.get_time()
                    new_time=current_time+10000
                    if new_time > total_duration:
                        newtime=0
                    player.set_time(new_time)
                
                elif (cnt == 2):
                    pyautogui.press("left")
                    print('playback 10 secs')
                    current_time=player.get_time()
                    new_time=current_time-10000
                    if new_time <= 0:
                        newtime=0
                    player.set_time(new_time)

                elif (cnt == 3):
                    pyautogui.press("up")
                    print('volume up')
                    new_volume=player.audio_get_volume()+10
                    if new_volume >= 200:
                        new_volume=200
                    player.audio_set_volume(new_volume)

                elif (cnt == 4):
                    pyautogui.press("down")
                    print('volume down')
                    new_volume=player.audio_get_volume()-10
                    if new_volume <= 10:
                        new_volume=10
                    player.audio_set_volume(new_volume)
                    

                elif (cnt == 5):
                    pyautogui.press("space")
                    print('space')
                    player.pause()
                    
                else:
                    player.play()

                prev = cnt
                start_init = False


        drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)
    
    if COUNTER % fps_avg_frame_count == 0:
        FPS = fps_avg_frame_count / (time.time() - START_TIME)
        START_TIME = time.time()
    fps_text = 'FPS = {:.1f}'.format(FPS)
    text_location = (24, 50)
    cv2.putText(frm, fps_text, text_location, cv2.FONT_HERSHEY_DUPLEX,
                1, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.imshow("window", frm)

    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        cap.release()
        break
