# Course Value Analyzer

The Course Value Analyzer is a web application designed to analyze the relevance of educational courses in today's job market using data-driven insights. Leveraging machine learning techniques, the application predicts the value of courses based on current job demands, providing actionable insights for educational institutions and learners.

## Features

- **Data Collection and Preprocessing:** Collects and preprocesses data from job postings and course descriptions, including data cleaning, normalization, and tokenization.
  
- **Machine Learning Model:** Trains and deploys a machine learning model using Scikit-learn to predict the relevance of courses based on job market data.
  
- **Visualization:** Visualizes insights using Highcharts, presenting charts and graphs that highlight the relevance of courses and job market trends.
  
- **Web Interface:** Provides a user-friendly web interface built with Flask, Bootstrap, and Highcharts for interactive analysis and visualization of course values.

## Technologies Used

- **Python:** Backend programming language for data processing and machine learning.
  
- **Flask:** Web framework used for building the web application and API endpoints.
  
- **Scikit-learn:** Machine learning library for training predictive models.
  
- **Pandas:** Data manipulation and analysis library.
  
- **SpaCy:** Natural language processing library used for text preprocessing and analysis.
  
- **Highcharts:** JavaScript library for interactive charts and data visualization.
  
- **Bootstrap:** Frontend framework for responsive and mobile-first design.

## Deployment

The application is deployed on Render and can be accessed at [Course Value Analyzer](https://course-value-analyzer.onrender.com/course_analysis).

## Usage

1. **Data Analysis:** Upload or input course topics and analyze job readiness metrics such as similarity scores and keyword matching.
  
2. **Visualization:** View interactive charts and graphs that visualize course relevance and job market demand.
  
3. **Insights and Recommendations:** Receive insights and recommendations based on the analysis to improve course offerings and alignment with job market needs.

## Installation

To run the Course Value Analyzer locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/course-value-analyzer.git
   cd course-value-analyzer
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables or configuration files as needed for API keys, database connections, etc.

4. Run the Flask application:

   ```bash
   flask run
   ```

5. Access the application at `http://localhost:5000` in your web browser.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any enhancements, bug fixes, or new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please contact [Balaji Anbalagan](mailto:vijibalaji2003@gmail.com).
