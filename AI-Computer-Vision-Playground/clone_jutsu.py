import cv2
import mediapipe as mp
import csv
import time

# ১. ক্যামেরা স্ক্যানার ফাংশন
def get_available_cameras():
    print("\nক্যামেরা স্ক্যান করা হচ্ছে... দয়া করে অপেক্ষা করুন।")
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
    print("!!! এরর: কোনো ক্যামেরা পাওয়া যায়নি।")
    exit()

print(f"\nপাওয়া গেছে এমন ক্যামেরার তালিকা: {found_cameras}")
chosen_index = int(input("আপনি কত নম্বর ক্যামেরা ইনডেক্সটি ব্যবহার করতে চান? "))

# ২. মিডিয়াপাইপ ও ক্যামেরা সেটআপ
cap = cv2.VideoCapture(chosen_index, cv2.CAP_DSHOW)
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5)

# ৩. ইউজার মোড সিলেকশন
print("\n--- অটো ডাটা কালেকশন মোড ---")
mode = input("কোন ডাটা নিবেন? (জুটসুর জন্য '1', নরমাল হাতের জন্য '0'): ")
label = int(mode)
target_samples = 100 # কয়টি ডাটা পয়েন্ট নিবেন

print(f"\nপ্রস্তুত হন! ৫ সেকেন্ড পর ডাটা সেভ শুরু হবে...")
for i in range(5, 0, -1):
    print(f"{i}...")
    time.sleep(1)

print("\n!!! শুরু !!! পোজ ধরে রাখুন...")

count = 0
while count < target_samples:
    success, img = cap.read()
    if not success: break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        # শুধুমাত্র ২ হাত থাকলেই ১২৬টি পয়েন্ট পাওয়া যাবে
        if len(results.multi_hand_landmarks) == 2:
            all_landmarks = []
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                for lm in hand_landmarks.landmark:
                    all_landmarks.extend([lm.x, lm.y, lm.z])
            
            all_landmarks.append(label) # শেষে লেবেল যোগ করা হচ্ছে (০ বা ১)
            
            with open('jutsu_data.csv', mode='a', newline='') as f:
                csv.writer(f).writerow(all_landmarks)
            
            count += 1
            print(f"সংগৃহীত ডাটা: {count}/{target_samples}", end="\r")

    cv2.imshow("Auto Data Collection", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

print(f"\n\nঅভিনন্দন! সফলভাবে {count}টি ডাটা সেভ হয়েছে।")
cap.release()
cv2.destroyAllWindows()