from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import pandas as pd

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            extension = filename.rsplit('.', 1)[1].lower()
            if extension not in ['csv', 'xlsx']:
                return "Invalid file type! Go back to upload again"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect('/upload')
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    file_info = []
    for file_name in files:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
        size = os.path.getsize(file_path)
        extension = file_name.rsplit('.', 1)[1]
        if extension not in ['csv', 'xlsx']:
            continue
        file_info.append({'name': file_name, 'size': size, 'extension': extension})
    return render_template('upload_view.html', files=file_info)

# @app.route('/remove_file', methods=['POST'])
# def remove_file():
#     filename = request.form['filename']
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#     os.remove(file_path)
#     return redirect('/upload')

@app.route('/remove_file', methods=['GET'])
def remove_file():
    filename = request.args.get('filename')
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    os.remove(file_path)
    return redirect('/upload')



@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/open/<filename>')
def open_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    extension = filename.rsplit('.', 1)[1]
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            if extension == 'csv':
                df = pd.read_csv(f)
            elif extension in ['xls', 'xlsx']:
                df = pd.read_excel(f)
            else:
                return 'Invalid file type'
    except UnicodeDecodeError:
        try:
            with open(file_path, 'r', encoding='iso-8859-1') as f:
                if extension == 'csv':
                    df = pd.read_csv(f)
                elif extension in ['xls', 'xlsx']:
                    df = pd.read_excel(f)
                else:
                    return 'Invalid file type'
        except:
            with open(file_path, 'rb') as f:
                if extension == 'csv':
                    df = pd.read_csv(f)
                elif extension in ['xls', 'xlsx']:
                    df = pd.read_excel(f)
                else:
                    return 'Invalid file type'
    return render_template('open.html', table=df.to_html(), filename=filename)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            return redirect('/upload')
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
