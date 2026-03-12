import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# ১. ডাটা লোড করা
data = pd.read_csv('jutsu_data.csv', header=None)

# ২. ফিচার (X) এবং লেবেল (y) আলাদা করা
# প্রথম ১২৬টি কলাম হলো হাতের পয়েন্ট (X), শেষ কলামটি লেবেল (y)
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# ৩. ডাটাকে ট্রেইনিং এবং টেস্টিং সেটে ভাগ করা (৮০% ট্রেনিং, ২০% টেস্ট)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ৪. এআই মডেল তৈরি (Random Forest ব্যবহার করছি কারণ এটি জুটসু ডিটেকশনে দ্রুত কাজ করে)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# ৫. নির্ভুলতা পরীক্ষা করা
y_pred = model.predict(X_test)
score = accuracy_score(y_test, y_pred)
print(f"মডেলের নির্ভুলতা (Accuracy): {score * 100:.2f}%")

# ৬. মডেলটি সেভ করা যাতে পরে ব্যবহার করা যায়
with open('jutsu_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("অভিনন্দন! তোমার এআই জুটসু চিনতে শিখে গেছে। 'jutsu_model.pkl' ফাইলটি তৈরি হয়েছে।")