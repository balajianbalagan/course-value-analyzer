import pandas as pd

# Load the job dataset
job_data = pd.read_csv('job_data.csv')

# Handle missing salary values (e.g., fill with median, mean, or a placeholder)
job_data['salary'] = job_data['salary'].fillna(job_data['salary'].median())

# Standardize skills/tags (convert to lowercase, remove duplicates, etc.)
job_data['skills'] = job_data['skills'].str.lower().str.split(',')

# Example function to preprocess and clean job data
def preprocess_job_data(df):
    df['skills'] = df['skills'].apply(lambda x: [skill.strip() for skill in x])
    return df

job_data = preprocess_job_data(job_data)
