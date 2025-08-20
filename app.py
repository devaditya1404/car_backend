from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load your ML model
model = joblib.load("/Users/adityabonde/Desktop/Car_frontend/model_final.pth")

@app.route("/")
def home():
    return {"message": "ML API is running!"}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    prediction = model.predict([data["features"]])
    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
