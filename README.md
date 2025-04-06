# Indian-cow-breed
#  Bovine Breed Classifier

Welcome to the Bovine Breed Classifier — a farmer-focused web app that lets you **upload a photo of a cow** and instantly identifies its **breed using AI**. It also gives you detailed, easy-to-understand info in your local language, and even shows **nearby veterinary doctors** on a map!

This project is built to empower farmers with modern tools in a simple, accessible way. 🌱

---

## What You Can Do With It

-  Upload an image of a cow and get its breed instantly.
-  Choose your preferred language — from Hindi to Marathi to Tamil (and more coming).
-  Learn about the breed — origin, traits, care, productivity — with AI-generated info powered by Gemini.
-  Find veterinary doctors near you using Google Maps.
-  Clean, mobile-friendly, farmer-oriented UI with local-friendly colors and icons.

---

## 🛠️ Tech Behind the Scenes

| Area | Stack |
|------|-------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| AI Model | Trained CNN (Keras, TensorFlow) deployed on **Vertex AI** |
| Language Intelligence | Gemini Pro (Generative AI) |
| Location | Google Maps + Places API |

---

## 🔧 Getting Started

1. **Clone this repo**  
   ```bash
   git clone https://github.com/your-username/bovine-breed-classifier.git
   cd bovine-breed-classifier
Set up your environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install the requirements

pip install -r requirements.txt

Add your API keys
Create a .env file in the root directory:
GEMINI_API_KEY=your_gemini_api_key
MAPS_API_KEY=your_google_maps_api_key_here

Run the app

    python app.py

Now open your browser and go to http://127.0.0.1:5000 — you're all set!
Ideas For What's Next

    🎤 Voice input for hands-free usage

    🐮 Farmer forum or chat feature

    🧑‍🌾 WhatsApp chatbot for rural outreach

    💾 Offline support using PWA

 Thanks To

    The open-source community

    Google Cloud (Vertex AI, Maps API)

    Gemini AI for breed info

    Every farmer and livestock caretaker who inspired this idea
Questions? Suggestions?

Feel free to open an issue or reach out
