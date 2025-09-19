import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model
import os

# --------------------
# Dataset Preparation
# --------------------
dataset_path = "D:\Code-Base\SIH Krishna\dataset"   # Replace with your dataset folder path
# Your dataset structure should be:
# dataset/
#     plastic/
#     paper/
#     glass/
#     organic/
#     metal/

datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

train_data = datagen.flow_from_directory(
    dataset_path,
    target_size=(224,224),
    batch_size=32,
    class_mode="categorical",
    subset="training"
)

val_data = datagen.flow_from_directory(
    dataset_path,
    target_size=(224,224),
    batch_size=32,
    class_mode="categorical",
    subset="validation"
)

# --------------------
# Build Model
# --------------------
base_model = MobileNetV2(weights="imagenet", include_top=False, input_shape=(224,224,3))
base_model.trainable = False  # Freeze base model

x = GlobalAveragePooling2D()(base_model.output)
x = Dense(128, activation="relu")(x)
x = Dropout(0.3)(x)
output = Dense(train_data.num_classes, activation="softmax")(x)

model = Model(inputs=base_model.input, outputs=output)

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# --------------------
# Train
# --------------------
history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=10
)

# --------------------
# Save Model
# --------------------
os.makedirs("models", exist_ok=True)
model.save("models/waste_classifier.h5")
print("✅ Model saved at models/waste_classifier.h5")
