🎉 Vox Quiz 🎉

Vox Quiz is an interactive game application built with Python and Streamlit. The game challenges users to identify 🐾 animals, 🦜 birds, or 🦋 insects based on AI-generated images. Users provide their answers via voice input 🎙️, and the app checks the correctness of their response in real-time.

🚀 Features

🎨 AI-generated Images: The application generates images using the Hugging Face API with Stable Diffusion models.
🎤 Voice Input: Users answer by speaking into their microphone, and the app recognizes the speech using the Google Speech Recognition API.
🖥️ Interactive UI: The interface is built using Streamlit, offering a clean and responsive layout.
🎮 Game Modes: Three different game categories (Animals, Birds, Insects) for users to choose from.
⚡ Real-time Feedback: The app provides immediate feedback on whether the answer is correct or not.

🛠️ Technologies Used

Streamlit: For building the web-based user interface.
Hugging Face API: For generating images using the Stable Diffusion model.
PIL (Pillow): For handling image data and manipulation.
SpeechRecognition: For capturing and processing user speech input.
pyaudio: For interacting with the system's microphone.
Random: For random selection of animals, birds, or insects.
Python: Core language used for the entire project.

📦 Installation

Clone the repository:
git clone https://github.com/yashwantpradhan/Vox-Quiz.git

Navigate to the project directory:
cd Vox-Quiz

Create and activate a virtual environment (optional but recommended):
python3 -m venv venv source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required dependencies:
pip install -r requirements.txt

Run the application:
streamlit run app.py

Open your browser and navigate to:
http://localhost:8501
