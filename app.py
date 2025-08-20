import os
import gdown
import torch
from flask import Flask, jsonify

app = Flask(__name__)

MODEL_PATH = "model.pth"

# Download model if not exists
if not os.path.exists(MODEL_PATH):
    url = https://drive.google.com/file/d/1yjjovIojwU4UihaPKtv695W6cjQzoxYn  # ✅ your link
    gdown.download(url, MODEL_PATH, quiet=False)

# Load model
model = torch.load(MODEL_PATH, map_location="cpu")
model.eval()

@app.route("/")
def home():
    return "✅ Car Damage Detection App is running on Render!"

@app.route("/predict", methods=["GET"])
def predict():
    # Dummy response for now (replace later with real inference)
    return jsonify({"status": "success", "message": "Prediction endpoint works!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render requires this
    app.run(host="0.0.0.0", port=port)
