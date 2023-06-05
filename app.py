from flask import Flask, render_template, request
import random
import string

app = Flask(__name__, static_folder='static')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/generate-password', methods=['POST'])
def generate_password():
    length = int(request.form.get('length', 16))  # Default length is 16
    use_letters = request.form.get('letters') == 'on'
    use_digits = request.form.get('digits') == 'on'
    use_symbols = request.form.get('symbols') == 'on'

    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not (use_letters or use_digits or use_symbols):
        return render_template('index.html', password='')

    password = ''
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if (use_letters and any(c.isupper() for c in password)) or not use_letters:
            if (use_symbols and any(c in string.punctuation for c in password)) or not use_symbols:
                if (use_digits and any(c.isdigit() for c in password)) or not use_digits:
                    break

    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run()



