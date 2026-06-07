from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ==========================================
# COURSE DATABASE
# ==========================================

courses = {
    "Python for Beginners":
        "python programming coding automation",

    "Machine Learning Fundamentals":
        "python machine learning data science",

    "Deep Learning with TensorFlow":
        "python deep learning neural networks tensorflow",

    "Web Development Bootcamp":
        "html css javascript frontend web design",

    "Cloud Computing Essentials":
        "aws cloud devops infrastructure",

    "Data Structures and Algorithms":
        "algorithms data structures problem solving coding",

    "Cyber Security Basics":
        "security networking ethical hacking cyber",

    "Data Analytics with Python":
        "python pandas numpy analytics visualization"
}

# ==========================================
# USER INPUT
# ==========================================

print("=" * 60)
print("AI COURSE RECOMMENDATION ENGINE")
print("=" * 60)

user_interest = input(
    "\nEnter your interests (comma separated): "
)

# ==========================================
# DATA PREPARATION
# ==========================================

course_names = list(courses.keys())
course_descriptions = list(courses.values())

documents = [user_interest] + course_descriptions

# ==========================================
# TF-IDF VECTORIZATION
# ==========================================

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

# User Vector
user_vector = tfidf_matrix[0]

# Course Vectors
course_vectors = tfidf_matrix[1:]

# ==========================================
# COSINE SIMILARITY
# ==========================================

similarity_scores = cosine_similarity(
    user_vector,
    course_vectors
)

# ==========================================
# RANK COURSES
# ==========================================

scores = similarity_scores.flatten()

recommendations = list(
    zip(course_names, scores)
)

recommendations.sort(
    key=lambda x: x[1],
    reverse=True
)

# ==========================================
# OUTPUT
# ==========================================

print("\nTop Recommendations")
print("-" * 60)

for rank, (course, score) in enumerate(
        recommendations[:5],
        start=1):

    print(
        f"{rank}. {course}"
        f"  | Similarity Score: {score:.3f}"
    )

print("-" * 60)