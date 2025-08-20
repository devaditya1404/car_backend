import os, gdown, torch

MODEL_PATH = "model.pth"

if not os.path.exists(MODEL_PATH):
    # Download from Google Drive
    url = "https://drive.google.com/uc?id=YOUR_FILE_ID"
    gdown.download(url, MODEL_PATH, quiet=False)

model = torch.load(MODEL_PATH, map_location="cpu")
model.eval()
