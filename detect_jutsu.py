import cv2
import mediapipe as mp
import pickle
import numpy as np
import pygame
import os

# --- ১. সেটিংস ও মডেল লোড ---
pygame.mixer.init()
if os.path.exists("jutsu_sound.mp3"):
    jutsu_sound = pygame.mixer.Sound("jutsu_sound.mp3")
else:
    jutsu_sound = None

with open('jutsu_model.pkl', 'rb') as f:
    model = pickle.load(f)

# মিডিয়াপাইপ সেটআপ
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=2, 
    min_detection_confidence=0.5, 
    min_tracking_confidence=0.8
)

mp_selfie = mp.solutions.selfie_segmentation
segmentation = mp_selfie.SelfieSegmentation(model_selection=1)

# ক্যামেরা ইনডেক্স ২
cap = cv2.VideoCapture(2, cv2.CAP_DSHOW)

effect_timer = 0
jutsu_active = False

print("--- শ্যাডো ক্লোন মোড (ক্লোজার ক্লোনস) চালু ---")

# ক্লোন বসানোর ফাংশন
def apply_clone(canvas, person_img, mask, scale, x_offset):
    h, w = canvas.shape[:2]
    nw, nh = int(w * scale), int(h * scale)
    small_person = cv2.resize(person_img, (nw, nh))
    small_mask = cv2.resize(mask.astype(np.uint8), (nw, nh))
    
    y_off = h - nh
    actual_x = int(w/2 + x_offset - nw/2)
    
    roi_x_start = max(0, actual_x)
    roi_x_end = min(w, actual_x + nw)
    roi_w = roi_x_end - roi_x_start
    
    if roi_w <= 0: return canvas

    small_x_start = max(0, -actual_x)
    small_x_end = small_x_start + roi_w

    roi = canvas[y_off:y_off+nh, roi_x_start:roi_x_end]
    small_mask_crop = small_mask[:, small_x_start:small_x_end]
    small_person_crop = small_person[:, small_x_start:small_x_end]

    mask_3d = np.stack((small_mask_crop,) * 3, axis=-1).astype(bool)
    roi[mask_3d] = small_person_crop[mask_3d]
    return canvas

while True:
    success, img = cap.read()
    if not success: break

    img = cv2.flip(img, 1)
    h, w, _ = img.shape
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    clean_frame = img.copy()
    display_frame = img.copy()
    
    results_hands = hands.process(img_rgb)
    current_jutsu = False

    if results_hands.multi_hand_landmarks:
        for hand_lms in results_hands.multi_hand_landmarks:
            mp_draw.draw_landmarks(display_frame, hand_lms, mp_hands.HAND_CONNECTIONS)
        
        if len(results_hands.multi_hand_landmarks) == 2:
            all_landmarks = []
            for hand_landmarks in results_hands.multi_hand_landmarks:
                for lm in hand_landmarks.landmark:
                    all_landmarks.extend([lm.x, lm.y, lm.z])
            
            prediction = model.predict([all_landmarks])[0]
            probability = model.predict_proba([all_landmarks])[0]

            if prediction == 1 and probability[1] > 0.85:
                current_jutsu = True

    if current_jutsu:
        if not jutsu_active:
            if jutsu_sound: jutsu_sound.play()
            jutsu_active = True
        effect_timer = 150
    elif effect_timer > 0:
        effect_timer -= 1
    else:
        jutsu_active = False

    if effect_timer > 0:
        results_seg = segmentation.process(clean_frame)
        mask = results_seg.segmentation_mask > 0.4
        
        person_only = np.zeros_like(clean_frame)
        person_only[mask] = clean_frame[mask]
        
        canvas = clean_frame.copy()

        # --- পজিশনিং পরিবর্তন (আরও কাছাকাছি) ---
        # আগের ভ্যালু ছিল 0.35 এবং 0.60, এখন কমানো হলো
        dist1 = int(w * 0.15) # ভেতরের ক্লোনগুলো খুব কাছে
        dist2 = int(w * 0.30) # বাইরের ক্লোনগুলোও কাছে
        offsets = [-dist2, -dist1, dist1, dist2] 
        
        for off in offsets:
            # স্কেল ০.৭০ (৭০%) রাখা হয়েছে
            canvas = apply_clone(canvas, person_only, mask, 0.70, off)

        mask_3d = np.stack((mask,) * 3, axis=-1)
        # তুমি সবার সামনে থাকবে, তাই ক্লোনগুলো তোমার পেছনে ঢাকা পড়বে
        final_output = np.where(mask_3d, display_frame, canvas)
        
        cv2.putText(final_output, "SHADOW CLONE JUTSU!", (50, 100), 
                    cv2.FONT_HERSHEY_DUPLEX, 1.2, (0, 0, 255), 3)
    else:
        final_output = display_frame

    cv2.imshow("Live Shadow Clone Jutsu", final_output)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()