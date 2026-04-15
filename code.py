# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset (make sure your file name matches)
dataset = pd.read_csv("spam.csv", encoding='latin-1')

# Keep only required columns
dataset = dataset[['v1', 'v2']]
dataset.columns = ['type', 'message']

# Convert labels (ham=0, spam=1)
dataset['type'] = dataset['type'].map({'ham': 0, 'spam': 1})

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    dataset['message'], dataset['type'], test_size=0.5, random_state=1
)

# Convert text to numbers
cv = CountVectorizer()
X_train_vec = cv.fit_transform(X_train)
X_test_vec = cv.transform(X_test)

# Train model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Predict
y_pred = model.predict(X_test_vec)

# Accuracy
acc = accuracy_score(y_test, y_pred)
print(" Model Accuracy is:", acc)

# Test with custom message

sample = ["Hurry! Claim your reward now!"]
sample_vec = cv.transform(sample)
prediction = model.predict(sample_vec)

if prediction[0] == 1:
    print("This is SPAM")
else:
    print("This is NOT SPAM")

    # Test with custom message
sample = ["Congratulations! You have won a free prize"]
sample_vec = cv.transform(sample)
prediction = model.predict(sample_vec)

if prediction[0] == 1:
    print("This is SPAM")
else:
    print("This is NOT SPAM")