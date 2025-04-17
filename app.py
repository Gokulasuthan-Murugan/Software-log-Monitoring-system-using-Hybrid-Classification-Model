from flask import Flask, request, jsonify, render_template
from src.pipeline.Predict_Pipeline import PredictionPipeline

app = Flask(__name__)

# Load your model once when the app starts
predictor = PredictionPipeline()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    message = data.get("message")

    if not message:
        return jsonify({"error": "No message provided"}), 400

    try:
        prediction = predictor.prediction_pipeline(message)
        return jsonify({"message": message, "prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
