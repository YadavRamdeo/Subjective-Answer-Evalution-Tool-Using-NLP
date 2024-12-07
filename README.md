Subjective Answer Evaluation Tool
An NLP-powered tool designed to automate the evaluation of subjective answers by comparing them with model answers, providing accurate and unbiased grading.

Features
Cosine Similarity-Based Evaluation:
Measures the similarity between student answers and model answers, generating a match percentage score.

Customizable Scoring:
Configurable parameters to prioritize keywords or phrases and handle diverse answer variations.

NLP-Powered:
Uses techniques like tokenization, lemmatization, and stopword removal to focus on meaningful content.

Interactive UI:
Upload student and model answers for instant scoring and detailed feedback.

Scalability:
Supports bulk evaluation and multilingual capabilities.

Technologies
Language: Python
NLP Libraries: NLTK, SpaCy
Backend: Flask or Django Rest Framework
Frontend: React.js (optional for UI)
Algorithm: Cosine similarity for text comparison
Use Cases
Automating grading for exams, assignments, and assessments.
E-learning platforms for real-time feedback.
Educational institutions aiming to reduce manual grading effort.
Setup
Clone the repository:
bash
Copy code
git clone https://github.com/YadavRamdeo/subjective-answer-evaluation-tool.git
cd subjective-answer-evaluation-tool
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Run the application:
bash
Copy code
python app.py
License
This project is licensed under the MIT License. See the LICENSE file for details.


