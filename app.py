from flask import Flask, render_template, request
import nltk
from nltk.tokenize import word_tokenize

app = Flask(__name__)

# Function nltk
def word_tokenization(text):
    # Tokenizing the text and converting to lowercase
    words = word_tokenize(text.lower())
    # Filter only words (ignoring punctuation)
    words = [word for word in words if word.isalnum()]
    return ', '.join(words)

@app.route('/', methods=['GET', 'POST'])
def index():
    tokenized_text = ""
    if request.method == 'POST':
        input_text = request.form['inputText']
        tokenized_text = word_tokenization(input_text)
    
    return render_template('index.html', tokenized_text=tokenized_text)

if __name__ == '__main__':
    app.run(debug=True)
