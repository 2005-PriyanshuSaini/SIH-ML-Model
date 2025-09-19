import cv2
import numpy as np
import tensorflow as tf

# Load trained model
model = tf.keras.models.load_model("models/waste_classifier.h5")

# Class names (update with your dataset folders)
class_names = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]

# Open webcam
cap = cv2.VideoCapture(0)  # 0 = default camera

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess frame
    img = cv2.resize(frame, (224,224))
    img = img.astype("float32") / 255.0
    img = np.expand_dims(img, axis=0)

    # Predict
    preds = model.predict(img)
    class_id = np.argmax(preds)
    confidence = np.max(preds)

    # Display result
    label = f"{class_names[class_id]} ({confidence*100:.2f}%)"
    cv2.putText(frame, label, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("Smart Dustbin Classifier", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
