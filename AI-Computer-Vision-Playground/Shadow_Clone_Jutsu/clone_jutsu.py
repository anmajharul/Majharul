import cv2
import mediapipe as mp
import csv
import time


# 1. Camera scanner function
def get_available_cameras():
    print("\nScanning cameras... please wait.")
    available_indices = []
    for i in range(5):
        cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                available_indices.append(i)
                cv2.imshow(f"Camera Index: {i}", frame)
                cv2.waitKey(1000)
                cv2.destroyAllWindows()
            cap.release()
    return available_indices


found_cameras = get_available_cameras()
if not found_cameras:
    print("Error: no camera found.")
    exit()

print(f"\nAvailable camera indices: {found_cameras}")
chosen_index = int(input("Which camera index do you want to use? "))

# 2. MediaPipe and camera setup
cap = cv2.VideoCapture(chosen_index, cv2.CAP_DSHOW)
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5)

# 3. User mode selection
print("\n--- Auto Data Collection Mode ---")
mode = input("Which data will you capture? (jutsu='1', normal hands='0'): ")
label = int(mode)
target_samples = 100  # How many data points to capture

print("\nGet ready! Data capture starts in 5 seconds...")
for i in range(5, 0, -1):
    print(f"{i}...")
    time.sleep(1)

print("\nStarting! Hold your pose...")

count = 0
while count < target_samples:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        # Only collect when two hands are visible (126 points)
        if len(results.multi_hand_landmarks) == 2:
            all_landmarks = []
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                for lm in hand_landmarks.landmark:
                    all_landmarks.extend([lm.x, lm.y, lm.z])

            all_landmarks.append(label)  # Add label at the end (0 or 1)

            with open("jutsu_data.csv", mode="a", newline="") as f:
                csv.writer(f).writerow(all_landmarks)

            count += 1
            print(f"Collected data: {count}/{target_samples}", end="\r")

    cv2.imshow("Auto Data Collection", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

print(f"\n\nDone! Successfully saved {count} samples.")
cap.release()
cv2.destroyAllWindows()
