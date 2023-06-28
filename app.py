from flask import Flask, render_template, request
from gtts import gTTS
import os

# Create the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    output_exists = False
    save_as = None

    if request.method == 'POST':
        mytext = request.form['text']
        save_as = request.form['save_as']  # Get the custom save file name from the form
        language = 'en'
        save_path = os.path.join('static', save_as + '.mp3')  # Build the save file path
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save(save_path)
        output_exists = True
    
    return render_template('index.html', output_exists=output_exists, save_as=save_as)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)