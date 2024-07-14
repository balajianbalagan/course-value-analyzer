from flask import Flask, request, render_template, jsonify
import pandas as pd
from utils.analysis import analyze_course
from utils.job_scraper import getAndSaveJobData
import csv
import json
import os



app = Flask(__name__)
# Load and preprocess job dataset


@app.route('/')
def index():
    return render_template('job_search.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    course_topics = request.json.get('course_topics')
    job_name = request.json.get('job_name')
    job_data = pd.read_csv("scraped_jobs/"+job_name+".csv")
   
    analysis_result = analyze_course(course_topics, job_data)
    return jsonify(analysis_result)


@app.route('/job_search')
def job_search_page():
    return render_template('job_search.html')

@app.route('/job_search', methods=['POST'])
def job_search():
    data = request.get_json()
    job_name = data.get('job_name')
    job_keywords = data.get('job_keywords').split(',')

    # Scrape job data and save to CSV
    csv_file = "scraped_jobs/"+job_name + ".csv"
    getAndSaveJobData(job_name, job_keywords)

    # Read the CSV data
    job_data = []
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            job_data.append(row)

    # Convert CSV data to JSON and return as response
    return jsonify({'results': job_data})

@app.route('/course_analysis')
def course_analysis():
    return render_template('index.html')

@app.route('/job_names', methods=['GET'])
def get_job_names():
    job_names = []
    directory = 'scraped_jobs/'
    if os.path.exists(directory):
        job_names = [filename.split('.')[0] for filename in os.listdir(directory) if filename.endswith('.csv')]
    return jsonify(job_names)

if __name__ == '__main__':
    app.run(debug=True)
