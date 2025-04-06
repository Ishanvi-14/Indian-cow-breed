from flask import Flask, render_template, request
import os
from model_predict import predict_breed
from breed_info import get_breed_info_from_gemini
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['MAP_API_KEY'] = os.getenv("MAPS_API_KEY")
UPLOAD_FOLDER = "static/uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    breed_info = None
    breed = None
    error = None
    image_filename = None
    language_code = "en"

    if request.method == "POST":
        file = request.files.get("image")
        language_code = request.form.get("language", "en")

        if file and file.filename:
            image_filename = file.filename
            img_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
            file.save(img_path)

            try:
                breed = predict_breed(img_path)
                breed_info, _, _ = get_breed_info_from_gemini(breed, language_code)
            except Exception as e:
                error = f"Prediction or info generation failed: {e}"
        else:
            error = "Please upload a valid image file."

    return render_template(
        "index.html",
        breed=breed,
        image_filename=image_filename,
        breed_info=breed_info,
        error=error,
        language_code=language_code,
        map_api_key=app.config['MAP_API_KEY']
    )

if __name__ == "__main__":
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
