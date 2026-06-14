# PhishGuard-AI

PhishGuard AI is a machine learning-based phishing and spam detection system developed using Python, Natural Language Processing (NLP), and Streamlit. The application analyzes the content of emails or messages and classifies them as either legitimate or phishing/spam.

# Objectives

Detect phishing and spam messages automatically.

Apply NLP techniques for text preprocessing.

Classify messages using machine learning.

Identify suspicious phishing-related keywords.

Provide a simple and interactive user interface for real-time analysis.

# Key Concepts Used

Natural Language Processing (NLP): Used to preprocess and clean email text before machine learning analysis.

TF-IDF Vectorization: Converts email text into numerical feature vectors by measuring the importance of words within messages.

Linear Support Vector Machine (Linear SVM): A supervised machine learning algorithm used to classify messages as legitimate or phishing/spam.

Phishing Keyword Analysis: Identifies suspicious keywords commonly associated with phishing attempts to improve detection reliability.

# Tools & Technologies

Language: Python

Libraries: Pandas, NumPy, Scikit-learn, NLTK.

Frontend: Streamlit

Data Source: Ham & Spam Collection Dataset


# How to Run locally

1. Clone this repository.
2. Create a virtual environment with `python -m venv venv`.
3. Activate the environment with `.\venv\Scripts\activate`.
4. Install the required libraries using `pip install -r requirements.txt`.
5. Train the machine learning model with `python src/train.py`.
6. Run the Streamlit app with `streamlit run src/app.py`.

# Project Structure

```
phishguard-ai/
│
├── data/
│   └── spam.csv                 # SMS Spam Collection dataset used for training
│
├── src/
│   ├── preprocess.py            # Email text preprocessing and cleaning module
│   ├── train.py                 # Trains and evaluates the Linear SVM model
│   └── app.py                   # Streamlit-based phishing detection interface
│
├── requirements.txt            # List of Python package dependencies
├── README.md                   # Project documentation
└── .gitignore                  
