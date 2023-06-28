# TextToSpeech-Converter
This is a simple text-to-speech converter web application. It allows users to enter text and convert it into speech output. The converted speech can be played directly or saved as an audio file.

## Features

- Convert text to speech
- Play the converted speech
- Save the speech as an audio file
- Download the saved speech file

## Technologies Used

- Python
- Flask (Python web framework)
- gTTS (Google Text-to-Speech library)
- HTML
- CSS

## Setup and Installation

1. Clone the repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd text-to-speech-converter`
3. Create a virtual environment (optional but recommended): `python -m venv env`
4. Activate the virtual environment: `source env/bin/activate` (for Unix/Mac) or `.\env\Scripts\activate` (for Windows)
5. Install the dependencies: `pip install -r requirements.txt`
6. Run the application: `python app.py`
7. Open your web browser and access the application at `http://localhost:5000`

## Usage

1. Enter the text you want to convert into the provided text area.
2. Optionally, enter a custom file name in the "Save As" field if you want to save the speech output with a specific name.
3. Click the "Convert to Speech" button to convert the text to speech. The converted speech will be played back.
4. To save the speech as an audio file, click the "Save As" button. If you provided a custom file name, the speech will be saved with that name; otherwise, a default name will be used.
5. To download the saved speech file, click the "Download" button.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

