# Smart Dustbin with AI-Powered Waste Segregation  

This project implements an **AI-based Smart Dustbin** that uses a trained deep learning model to classify waste (e.g., Plastic, Metal, Paper, Organic, etc.) in real-time using a camera. Once detected, the system sends the container number to a **motor controller (ESP32)**, which directs the waste to the correct bin.  
Used to won inter
---

## ✨ Features  
- Real-time waste detection using a webcam.  
- Pre-trained CNN model for classification.  
- ESP32 microcontroller for motor and container control.  
- Modular design: training, prediction, and deployment scripts separated.  
- Easily extendable with new classes and datasets.  

---

## 📂 Project Structure  
├── dataset/ # Training dataset (images organized by class)

├── models/ # Saved models (.h5 files)

├── train_model.py # Script to train the model

├── camera_predict.py # Run real-time camera predictions

├── requirements.txt # Python dependencies

├── README.md # Project documentation

└── .gitignore # Ignore unnecessary files in git

---

## ⚙️ Installation  

### 1. Clone the repository  
```bash
git clone https://github.com/your-username/smart-dustbin.git
cd smart-dustbin
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

### 3. Activate:

Windows:
```bash
env\Scripts\activate
```

Linux/Mac:
Windows:
```bash
source env/bin/activate
```
### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 🏋️ Training the Model

Add your dataset in the dataset/ folder (organized by subfolders per class).
Example:
```bash
dataset/
├── plastic/
├── metal/
├── paper/
└── organic/
```

### Train the model:
```bash
python train_model.py
```

This will generate a trained .h5 model in the models/ folder.

### 📷 Running Real-Time Predictions

Connect your camera.

Run:
``` bash
python camera_predict.py
```

The system will show real-time classification with predicted container numbers.

### 🔗 Hardware Integration (ESP32 + Motors)

The AI model runs on a PC/Raspberry Pi for high computation.

Once a prediction is confident, it sends the container number to ESP32 (via serial/WiFi).

ESP32 interprets this and activates the correct motor to open the bin.

### 🛠️ Requirements

Python 3.9 or 3.10 (recommended)

TensorFlow

Keras

OpenCV

NumPy

Install via:
```bash
pip install -r requirements.txt
```

### 🚀 Future Improvements

- [ ] Optimize model for TensorFlow Lite to run directly on edge devices.

- [ ] Add IoT features (cloud logging, mobile notifications).

- [ ] Improve accuracy with larger datasets.

### 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss.
