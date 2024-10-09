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
`git clone https://github.com/yashwantpradhan/Vox-Quiz.git`

Navigate to the project directory:
`cd Vox-Quiz`

Create and activate a virtual environment (optional but recommended):
`python3 -m venv venv source venv/bin/activate`

Install the required dependencies:
`pip install -r requirements.txt`

Run the application:
`streamlit run app.py`

Open your browser and navigate to:
`http://localhost:8501`



🎮 How to Play

Choose a category from the options: Animals 🐯, Birds 🦅, or Insects 🐜.

Click Start 🟢 to generate an image from the selected category.

The image will be displayed, and you’ll be prompted to say your answer aloud 🎙️.

The app will use speech recognition to process your answer.

If your answer is correct ✅, you'll get immediate feedback!

If the answer is incorrect ❌ or if time runs out ⏳, the correct answer will be displayed.

📋 Dependencies

Ensure you have the following dependencies installed:

`requests`

`Pillow`

`streamlit`

`random`

`speech_recognition`

`pyaudio`


🤝 Contributing


If you'd like to contribute to the project, follow these steps:

Fork the repository 🍴.

Create a new branch (git checkout -b feature-branch).

Make your changes.

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature-branch).

Open a pull request 🔄.

📜 License

This project is licensed under the MIT License.

🎉 Acknowledgments

Hugging Face API for image generation.

Google Speech Recognition API for voice input.

Streamlit for the user interface.

