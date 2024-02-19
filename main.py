from flask import Flask, render_template, request, send_file
from gtts import gTTS


app = Flask(__name__)

def text_to_speech(text, filename='output.mp3'):
    tts = gTTS(text=text, lang='ko')
    tts.save(filename)
    return filename

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        audio_file = text_to_speech(input_text)
        return render_template('index.html', input_text=input_text, audio_file=audio_file)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
