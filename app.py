import os
from flask import Flask, render_template, request, jsonify, redirect
import logging
import csv

app = Flask(__name__)



from flask import Flask, render_template
import csv

app = Flask(__name__)

# def read_csv(file_path):
#     print(file_path)
#     data = []
#     with open(file_path, 'r') as file:
#         csv_reader = csv.DictReader(file)
#         for row in csv_reader:
#             data.append(row)
#     return data

@app.route('/')
def dashboard():
    # Ganti 'dataset_anomali.csv' dengan nama file CSV Anda
    file_path = 'dataset_anomali.csv'
    # data = read_csv(file_path)
    return render_template('dashboard.html')

# @app.route('/index')
# def index():
#     # Ganti 'dataset_anomali.csv' dengan nama file CSV Anda
#     file_path = 'dataset_anomali.csv'
#     data = read_csv(file_path)
#     return render_template('dashboard.html', data = data)


@app.route('/index', methods=['POST', 'GET'])
def index():
    data = [] 
 # Initialize data as an empty list
    if request.method == 'POST':
        if request.files:
            uploaded_file = request.files['filename']
            uploaded_file.save(os.path.join(app.config['FILE_UPLOADS'], uploaded_file.filename))
            with open(os.path.join(app.config['FILE_UPLOADS'], uploaded_file.filename)) as file:
                csv_file = csv.reader(file)
                # csv_file = csv.DictReader(file)
                 
                # for row in csv_file:
                #     data.append(row)
                

                for idx, x in enumerate(csv_file):
                    x[0] = idx + 1
                    data.append(x)                    

    return render_template('index.html', data=data)

@app.route('/index')
def processed_data():
    data = request.args.get('data')  # Retrieve data from URL parameter
    # Process data here
    return render_template('index.html', data=data)

app.config['FILE_UPLOADS'] = "C:\\Users\\rifqi\\Documents\\TA1\\Program\\static\\file\\upload"

@app.route('/index')
def home(): 
    return redirect('/index')



if __name__ == '__main__':
    app.run(debug=True)


