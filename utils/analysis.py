import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Ensure necessary NLTK data packages are downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    if pd.isna(text):
        return ""
    
    # Tokenize and remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    
    # Debug: Print tokens after stopwords removal
    # print("Tokens after stopwords removal:", tokens)
    
    # Lemmatization using SpaCy
    doc = nlp(" ".join(tokens))
    lemmatized_tokens = [token.lemma_ for token in doc]
    
    # Debug: Print lemmatized tokens
    # print("Lemmatized tokens:", lemmatized_tokens)
    
    return " ".join(lemmatized_tokens)


def analyze_course(course_topics, job_data):
    # Preprocess job skills and handle NaN values
    job_data['processed_skills'] = job_data['tagsAndSkills'].apply(preprocess_text)

    # Tokenize and vectorize the job skills and course topics
    vectorizer = TfidfVectorizer()
    # Iterate through job_data and print values that cannot be fit transformed
    # print(job_data['processed_skills'].to_dict())
    job_skills_matrix = vectorizer.fit_transform(job_data['processed_skills'])
    processed_course_topics = preprocess_text(course_topics)
    course_topics_vector = vectorizer.transform([processed_course_topics])

    # Calculate similarity scores
    similarity_scores = cosine_similarity(course_topics_vector, job_skills_matrix).flatten()

    # Get top matching jobs
    top_matches = job_data.iloc[similarity_scores.argsort()[-10:][::-1]]

    # Get least matching jobs (optional)
    least_matches = job_data.iloc[similarity_scores.argsort()[:10]]

    # Determine demand and job readiness
    demand_topics = top_matches['tagsAndSkills'].str.split(',').explode().value_counts().head(10)
    job_readiness_score = similarity_scores.mean()

    # Find additional keywords and their vectors that highly match with course topics
    additional_keywords = []
    additional_vectors = []

    # Identify top matching vectors
    top_matching_indices = similarity_scores.argsort()[-10:][::-1]
    top_matching_vectors = job_skills_matrix[top_matching_indices]

    most_keywords = []
    most_vectors = []

    for vector in top_matching_vectors:
        top_indices = vector.indices
        top_values = vector.data

        # Extract top keywords
        top_keywords = [vectorizer.get_feature_names_out()[idx] for idx in top_indices]

        # Append to additional keywords list
        additional_keywords.extend(top_keywords)
        
        # Append vectors for visualization or further analysis
        additional_vectors.append({
            'keywords': top_keywords,
            'values': top_values.tolist()
        })

        # Keep track of most keywords and their vectors
        most_keywords.extend(top_keywords)
        most_vectors.append(top_values.tolist())

    # Identify least matching vectors
    least_matching_indices = similarity_scores.argsort()[:10]
    least_matching_vectors = job_skills_matrix[least_matching_indices]

    least_keywords = []
    least_vectors = []

    for vector in least_matching_vectors:
        least_indices = vector.indices
        least_values = vector.data

        # Extract least keywords
        least_keywords = [vectorizer.get_feature_names_out()[idx] for idx in least_indices]

        # Append to additional keywords list
        additional_keywords.extend(least_keywords)

        # Append vectors for visualization or further analysis
        additional_vectors.append({
            'keywords': least_keywords,
            'values': least_values.tolist()
        })

        # Keep track of least keywords and their vectors
        least_keywords.extend(least_keywords)
        least_vectors.append(least_values.tolist())

    # Additional similarity metrics
    similarity_metrics = {
        'max_similarity': np.max(similarity_scores),
        'min_similarity': np.min(similarity_scores),
        'mean_similarity': np.mean(similarity_scores),
        'std_similarity': np.std(similarity_scores)
    }
    
    # Map job names to similarity scores for Highcharts
    # print(top_matches['title'])
    job_names = top_matches['title'].tolist()
    similarity_distribution = {
        'categories': job_names,
        'scores': top_matching_indices.tolist()
    }

    return {
        'top_matching_jobs': top_matches.drop(columns=['processed_skills']).to_dict(orient='records'),
        'least_matching_jobs': least_matches.drop(columns=['processed_skills']).to_dict(orient='records'),
        'demand_topics': demand_topics.to_dict(),
        'job_readiness_score': job_readiness_score,
        'most_keywords': {
            'keywords': most_keywords,
            'vectors': most_vectors
        },
        'least_keywords': {
            'keywords': least_keywords,
            'vectors': least_vectors
        },
        'additional_keywords': additional_keywords,
        'additional_vectors': additional_vectors,
        'similarity_metrics': similarity_metrics,
        'similarity_distribution': similarity_distribution
    }
