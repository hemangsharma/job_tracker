from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import csv
import os
import pandas as pd
import json

app = Flask(__name__)
CSV_FILE_PATH = 'data/applications.csv'

# Ensure the data directory exists
os.makedirs('data', exist_ok=True)

# Initialize CSV file if it doesn't exist
if not os.path.exists(CSV_FILE_PATH):
    with open(CSV_FILE_PATH, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Company', 'Position', 'Date Applied', 'Status', 'Interview Date'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_application():
    if request.method == 'POST':
        company = request.form['company']
        position = request.form['position']
        date_applied = request.form['date_applied']
        status = request.form['status']
        interview_date = request.form.get('interview_date', '')

        with open(CSV_FILE_PATH, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([company, position, date_applied, status, interview_date])

        return redirect(url_for('index'))
    return render_template('add_application.html')

@app.route('/view')
def view_applications():
    data = pd.read_csv(CSV_FILE_PATH).to_dict(orient='records')
    return render_template('view_applications.html', data=data)

@app.route('/edit/<company>', methods=['GET', 'POST'])
def edit_application(company):
    data = pd.read_csv(CSV_FILE_PATH)
    app_data = data[data['Company'] == company].iloc[0]

    if request.method == 'POST':
        data.loc[data['Company'] == company, 'Status'] = request.form['status']
        data.loc[data['Company'] == company, 'Interview Date'] = request.form['interview_date']
        data.to_csv(CSV_FILE_PATH, index=False)
        return redirect(url_for('view_applications'))

    return render_template('edit_application.html', app_data=app_data)

@app.route('/charts')
def charts():
    data = pd.read_csv(CSV_FILE_PATH)
    status_counts = data['Status'].value_counts().to_dict()
    status_counts_json = json.dumps(status_counts)
    return render_template('charts.html', status_counts=status_counts_json)

if __name__ == '__main__':
    app.run(debug=True)
