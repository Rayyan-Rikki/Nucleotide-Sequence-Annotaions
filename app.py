from flask import Flask, request, render_template_string, send_file
from flask_frozen import Freezer
import os

app = Flask(__name__)
freezer = Freezer(app)

def reverse_complement(sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(sequence))

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        sequence = request.form['sequence']
        result = reverse_complement(sequence)
    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Reverse Complement</title>
            <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
            <div class="container mt-5">
                <h1 class="text-center">Reverse Complement Tool</h1>
                <form method="post" class="mt-4">
                    <div class="form-group">
                        <label for="sequence">Enter DNA Sequence</label>
                        <textarea class="form-control" id="sequence" name="sequence" rows="10" maxlength="5000"></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary">Reverse</button>
                </form>
                <div class="mt-4">
                    <h2>Reverse Complement:</h2>
                    <textarea class="form-control" rows="10" readonly>{{ result }}</textarea>
                </div>
                <form method="post" action="/download" class="mt-3">
                    <input type="hidden" name="sequence" value="{{ request.form.sequence }}">
                    <button type="submit" class="btn btn-secondary">Download Result</button>
                </form>
                <div class="mt-3">
                    <a href="/about" class="btn btn-info">About</a>
                </div>
            </div>
            <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
        </body>
        </html>
    ''', result=result)

@app.route('/download', methods=['POST'])
def download():
    sequence = request.form['sequence']
    result = reverse_complement(sequence)
    filename = 'reverse_complement.txt'
    with open(filename, 'w') as file:
        file.write(result)
    return send_file(filename, as_attachment=True)

@app.route('/about')
def about():
    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>About</title>
            <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
            <div class="container mt-5">
                <h1>About This Application</h1>
                <p>This application takes a DNA sequence and returns its reverse complement.</p>
                <a href="/" class="btn btn-primary">Go back to the main page</a>
            </div>
            <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    freezer.freeze()
    app.run(debug=True)