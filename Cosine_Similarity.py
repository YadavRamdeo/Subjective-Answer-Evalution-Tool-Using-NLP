import os
import numpy as np
from tkinter import Tk, filedialog
from sklearn.feature_extraction.text import TfidfVectorizer
from colorama import Fore, Style, init

init(autoreset=True)

def get_terminal_width():
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 80  

def center_align(text):
    width = get_terminal_width()
    return text.center(width)

def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    return dot_product / (norm_vec1 * norm_vec2)

def evaluate_grade(percentage):
    if percentage >= 90:
        return Fore.GREEN + "A+" + Style.RESET_ALL
    elif percentage >= 80:
        return Fore.GREEN + "A" + Style.RESET_ALL
    elif percentage >= 70:
        return Fore.BLUE + "B+" + Style.RESET_ALL
    elif percentage >= 60:
        return Fore.BLUE + "B" + Style.RESET_ALL
    elif percentage >= 50:
        return Fore.YELLOW + "Pass" + Style.RESET_ALL
    else:
        return Fore.RED + "Fail" + Style.RESET_ALL

def calculate_marks(model_answer, student_answer, total_marks=100):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([model_answer, student_answer])
    
    vec1 = tfidf_matrix[0].toarray()[0]
    vec2 = tfidf_matrix[1].toarray()[0]
    
    similarity = cosine_similarity(vec1, vec2)
    percentage = similarity * total_marks  
    
    grade = evaluate_grade(percentage)
    
    return percentage, grade

def display_result(model_answer, student_answer, percentage, grade):
    print(Fore.BLUE + center_align("=" * 50))
    print(Fore.MAGENTA + center_align("COSINE SIMILARITY EVALUATION"))
    print(Fore.BLUE + center_align("=" * 50))
    
    print(Fore.LIGHTYELLOW_EX + "\n" + center_align("📘 MODEL ANSWER:"))
    print(center_align("-" * 50))
    for line in model_answer.splitlines():
        print(center_align(line))
    print(center_align("-" * 50))
    
    print(Fore.LIGHTCYAN_EX + "\n" + center_align("✏️ STUDENT ANSWER:"))
    print(center_align("-" * 50))
    for line in student_answer.splitlines():
        print(center_align(line))
    print(center_align("-" * 50))
    
    print(Fore.LIGHTGREEN_EX + "\n" + center_align("📊 Evaluation Result:"))
    print(center_align("-" * 50))
    print(center_align(f"Result in Percentage: {percentage:.2f}%"))
    print(center_align(f"Final Result: - Grade: {grade}"))
    print(Fore.BLUE + center_align("=" * 50))

def upload_file(prompt):
    Tk().withdraw()  
    file_path = filedialog.askopenfilename(title=prompt, filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if not file_path:
        raise FileNotFoundError("No file was selected!")
    return file_path

if __name__ == "__main__":
    print(Fore.CYAN + center_align("=" * 50))
    print(Fore.GREEN + center_align("COSINE SIMILARITY EVALUATION TOOL USING NATURAL LANGUAGE PROCESSING (NLP)"))
    print(Fore.CYAN + center_align("=" * 50))
    
    print(center_align("Please upload the files for evaluation."))
    
    try:
        model_file = upload_file("Select the Model Answer File")
        student_file = upload_file("Select the Student Answer File")
        
        print(Fore.WHITE + "\n" + center_align(f"Model file selected: {model_file}"))
        print(Fore.WHITE + center_align(f"Student file selected: {student_file}"))
        
        with open(model_file, 'r') as mf:
            model_answer = mf.read()
        with open(student_file, 'r') as sf:
            student_answer = sf.read()
        
        percentage, grade = calculate_marks(model_answer, student_answer)
        
        display_result(model_answer, student_answer, percentage, grade)
    
    except FileNotFoundError as e:
        print(Fore.RED + "\n" + center_align(f"❌ Error: {e}"))
    except Exception as e:
        print(Fore.RED + "\n" + center_align(f"❌ Unexpected error: {e}"))