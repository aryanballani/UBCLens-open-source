import pandas as pd
import random
from datetime import datetime, timedelta

# Define the key dates and parameters
start_date_cpsc320 = datetime(2024, 9, 1)
midterm_date_cpsc320 = datetime(2024, 10, 20)
final_date_cpsc320 = datetime(2024, 12, 22)
num_rows_cpsc320 = 3000  # Adjusted for a realistic dataset size

# Topics from the CPSC 320 course based on the Algorithm Design book
cpsc320_topics = [
    "Greedy Algorithms", "Divide and Conquer", "Dynamic Programming", "Network Flow",
    "Graph Algorithms", "NP-Completeness", "Approximation Algorithms", "Randomized Algorithms",
    "Data Structures", "Sorting and Searching"
]

# Helper function to generate unique names
def generate_name():
    first_names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jenna", "Kevin", "Laura", "Mike", "Nina", "Oscar", "Paula", "Quinn", "Rachel", "Steve", "Tina", "Uma", "Victor", "Wendy", "Xander", "Yara", "Zach"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Helper function to generate CPSC 320 questions based on topics
def generate_cpsc320_question(topic):
    questions_cpsc320 = {
        "Greedy Algorithms": [
            "Can someone explain why the greedy algorithm works for interval scheduling?",
            "How do we prove that the greedy choice yields an optimal solution?",
            "Why can't a greedy approach work for all optimization problems?"
        ],
        "Divide and Conquer": [
            "What are the common divide and conquer techniques?",
            "How does divide and conquer relate to recursion?",
            "Can someone explain the steps in the merge sort algorithm?"
        ],
        # Add more questions for each topic similarly...
    }
    return random.choice(questions_cpsc320.get(topic, ["What are your thoughts on this topic?"]))

# Helper function to generate unique answers based on topics for CPSC 320
def generate_cpsc320_answer(topic):
    answers_cpsc320 = {
        "Greedy Algorithms": [
            "The greedy algorithm works when the problem has optimal substructure and the greedy choice property.",
            "For interval scheduling, choosing the interval that ends earliest maximizes the number of non-overlapping intervals.",
            "Not all problems allow a greedy approach because some require considering future choices."
        ],
        "Divide and Conquer": [
            "Divide and conquer breaks a problem into smaller subproblems, solves each recursively, and combines their results.",
            "Merge sort uses divide and conquer by recursively dividing the array and merging sorted halves.",
            "Divide and conquer approaches are often implemented using recursion to handle smaller problem instances."
        ],
        # Add more answers for each topic similarly...
    }
    
    # Create a dynamic combination of phrases for unique answers
    additional_phrases = [
        " This is essential for achieving efficient algorithms.",
        " It is crucial to understand the assumptions underlying this approach.",
        " This strategy can be adapted to a wide range of problems.",
        " This method offers a straightforward solution for many optimization issues."
    ]
    
    base_answer = random.choice(answers_cpsc320.get(topic, [
        "This topic is complex and requires careful analysis.",
        "Understanding this concept is crucial for mastering algorithm design."
    ]))
    
    # Combine base answer with additional unique phrases
    return f"{base_answer}{random.choice(additional_phrases)}"

# Helper function to generate date with realistic timestamp
def generate_date():
    base_date = start_date_cpsc320 + timedelta(days=random.randint(0, (final_date_cpsc320 - start_date_cpsc320).days))
    random_time = timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59), seconds=random.randint(0, 59))
    return base_date + random_time

# Generate the dataset for CPSC 320
data_cpsc320 = []
negative_comments = ["I don't think you're correct.", "That's wrong.", "I disagree with your point.", 
                     "That doesn't seem accurate.", "I'm not convinced by this explanation.", 
                     "This is not convincing at all."]

negative_comment_count_cpsc320 = 0

for _ in range(num_rows_cpsc320):
    topic = random.choices(cpsc320_topics, weights=[1 if t not in ["Divide and Conquer", "Greedy Algorithms", "Dynamic Programming"] else 3 for t in cpsc320_topics])[0]
    is_negative = negative_comment_count_cpsc320 < 50 and random.random() < 0.01
    if is_negative:
        negative_comment_count_cpsc320 += 1
    
    entry = {
        "topic_id": random.randint(1000000, 9999999),
        "topic_title": f"CPSC 320: {topic}",
        "topic_message": generate_cpsc320_question(topic),  # Topic message is the question
        "topic_author_id": random.randint(100000, 200000),
        "topic_author_name": generate_name(),
        "topic_created_at": generate_date().strftime("%Y-%m-%d %H:%M:%S PDT"),
        "topic_posted_at": generate_date().strftime("%Y-%m-%d %H:%M:%S PDT"),
        "post_author_id": random.randint(100000, 200000),
        "post_author_name": generate_name(),
        "post_id": random.randint(1000000, 9999999),
        "post_parent_id": None if random.random() > 0.6 else random.randint(1000000, 9999999),
        "post_message": generate_cpsc320_answer(topic) if not is_negative else random.choice(negative_comments),  # Unique post message or negative comment
        "post_likes": random.randint(0, 15),
        "post_timestamp": generate_date().strftime("%Y-%m-%d %H:%M:%S PDT")
    }
    data_cpsc320.append(entry)

# Convert the generated data into a DataFrame
df_cpsc320_final = pd.DataFrame(data_cpsc320)

# Save the final dataset to a CSV file
output_file_cpsc320_final = "CPSC_320_Discussion_Data.csv"
df_cpsc320_final.to_csv(output_file_cpsc320_final, index=False)

print(f"Dataset generated and saved as {output_file_cpsc320_final}")
