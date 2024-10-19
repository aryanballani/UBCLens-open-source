import pandas as pd
import random
from datetime import datetime, timedelta

# Define the key dates and parameters
start_date = datetime(2024, 9, 1)
midterm_date = datetime(2024, 10, 20)
final_date = datetime(2024, 12, 22)
num_rows = 12000

# Topics from the lecture slides
topics = [
    "Memory and Numbers", "Static Scalars and Arrays", "Dynamic Allocation", "Control Flow",
    "Procedures and Stack", "Virtual Processors", "I/O & Asynchrony", "Synchronization"
]

# Topics to prioritize with higher message counts
prioritized_topics = ["Dynamic Allocation", "Control Flow", "Virtual Processors"]

# Negative comments
negative_comments = [
    "I don't think you're correct.", "That's wrong.", "I disagree with your point.", 
    "That doesn't seem accurate.", "I'm not convinced by this explanation.", 
    "I don't find this convincing.", "That seems like a misunderstanding.", 
    "This doesn't align with the course material.", "Are you sure about that?", 
    "That seems incorrect to me."
]

# Helper function to generate names
def generate_name():
    first_names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jenna", "Kevin", "Laura", "Mike", "Nina", "Oscar", "Paula", "Quinn", "Rachel", "Steve", "Tina", "Uma", "Victor", "Wendy", "Xander", "Yara", "Zach"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Helper function to generate questions based on topics
def generate_question(topic):
    questions = {
        "Memory and Numbers": [
            "How do I convert large binary numbers to hexadecimal quickly?",
            "Can someone explain how memory alignment works?",
            "Why is sign extension necessary in Java?"
        ],
        "Static Scalars and Arrays": [
            "What’s the difference between static and dynamic arrays in C?",
            "How does the ALU process data efficiently between registers and memory?",
            "Can someone explain memory-mapped I/O in more detail?"
        ],
        "Dynamic Allocation": [
            "Why do we need structs in C when we have classes in Java?",
            "How do we prevent memory leaks when using dynamic allocation in C?",
            "What’s the most efficient way to dynamically allocate memory for large structures?"
        ],
        "Control Flow": [
            "How do we translate for loops from Java to assembly without branches?",
            "What’s the significance of program counter-relative addressing?",
            "How can we effectively unroll loops in assembly?"
        ],
        "Procedures and Stack": [
            "When should local variables be on the stack versus the heap?",
            "How do we return addresses in assembly without risking errors?",
            "What’s the best way to diagram a procedure call in assembly?"
        ],
        "Virtual Processors": [
            "How does round-robin scheduling work with multiple threads?",
            "What’s the difference between preemptive and non-preemptive scheduling?",
            "Can someone explain how threads transition between states?"
        ],
        "I/O & Asynchrony": [
            "What’s the difference between PIO and DMA, and when do we use each?",
            "How can I write a simple event-driven program using function pointers?",
            "Why is polling not the best idea for high-speed devices?"
        ],
        "Synchronization": [
            "Why do we use locks and semaphores in multi-threaded programs?",
            "How do we detect and prevent deadlocks in a shared data structure?",
            "What’s the difference between busy-waiting and blocking locks?"
        ]
    }
    return random.choice(questions.get(topic, ["What are your thoughts on this topic?"]))

# Helper function to generate unique answers based on topics
def generate_answer(topic):
    answers = {
        "Memory and Numbers": [
            "To convert large binary numbers, group them into sets of four digits.",
            "Memory alignment optimizes CPU performance and prevents access errors.",
            "Sign extension preserves the signed value when increasing bit width."
        ],
        "Static Scalars and Arrays": [
            "Static arrays are great for fixed-size requirements, while dynamic arrays adapt to runtime needs.",
            "The ALU operates on data between registers and memory efficiently to optimize processing time.",
            "Memory-mapped I/O provides direct hardware communication, improving efficiency."
        ],
        "Dynamic Allocation": [
            "Always deallocate memory dynamically allocated with free() in C to prevent leaks.",
            "Use calloc in C if you need zero-initialized memory for complex structures.",
            "Dynamic memory allocation allows us to allocate memory on-the-fly based on current needs."
        ],
        "Control Flow": [
            "When translating for loops to assembly, try minimizing the branch instructions.",
            "Using program counter-relative addressing shortens instruction sizes in assembly.",
            "Loop unrolling is an effective technique for small, predictable loop counts."
        ],
        "Procedures and Stack": [
            "Always use stack frames to handle procedure calls effectively.",
            "Local variables should be on the stack for short-term storage, with heap storage for longer-term needs.",
            "Drawing clear stack diagrams helps understand procedure calls and returns."
        ],
        "Virtual Processors": [
            "Round-robin scheduling allocates a fixed time slice to each thread to ensure fair time-sharing.",
            "Preemptive scheduling interrupts threads, allowing the system to allocate resources efficiently.",
            "Thread states transition dynamically based on resource availability and thread priority."
        ],
        "I/O & Asynchrony": [
            "PIO is simple but works best for low-bandwidth devices.",
            "Using function pointers in C enables efficient event-driven programming.",
            "Polling may seem straightforward but is inefficient for high-speed devices."
        ],
        "Synchronization": [
            "Locks prevent race conditions in multi-threaded programs by enforcing mutual exclusion.",
            "Detect deadlocks by analyzing the order in which threads acquire locks.",
            "Blocking locks save CPU cycles compared to busy-waiting."
        ]
    }
    return random.choice(answers.get(topic, ["This is a default answer for this topic."]))

# Helper function to generate date with higher density around midterms and finals
def generate_date():
    base_date = start_date + timedelta(days=random.randint(0, (final_date - start_date).days))
    random_time = timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59), seconds=random.randint(0, 59))
    return base_date + random_time

# Generate the dataset with questions as topic messages and answers as post messages
data = []
negative_comment_count = 0

# Create a realistic distribution with more entries for prioritized topics
for _ in range(num_rows):
    topic = random.choices(topics, weights=[1 if t not in prioritized_topics else 3 for t in topics])[0]
    is_negative = negative_comment_count < 50 and random.random() < 0.01
    if is_negative:
        negative_comment_count += 1
    
    entry = {
        "topic_id": random.randint(1000000, 9999999),
        "topic_title": f"CPSC 213: {topic}",
        "topic_message": generate_question(topic),  # Topic message is the question
        "topic_author_id": random.randint(100000, 200000),
        "topic_author_name": generate_name(),
        "topic_created_at": generate_date().strftime("%Y-%m-%d %H:%M:%S PDT"),
        "topic_posted_at": generate_date().strftime("%Y-%m-%d %H:%M:%S PDT"),
        "post_author_id": random.randint(100000, 200000),
        "post_author_name": generate_name(),
        "post_id": random.randint(1000000, 9999999),
        "post_parent_id": None if random.random() > 0.6 else random.randint(1000000, 9999999),
        "post_message": generate_answer(topic) if not is_negative else random.choice(negative_comments),  # Post message is the answer or negative comment
        "post_likes": random.randint(0, 15),
        "post_timestamp": generate_date().strftime("%Y-%m-%d %H:%M:%S PDT")
    }
    data.append(entry)

# Convert the generated data into a DataFrame
df_cpsc_213_final = pd.DataFrame(data)

# Save the final dataset to a CSV file for download
output_file_final = "CPSC_213_Data_5.csv"
df_cpsc_213_final.to_csv(output_file_final, index=False)

print(f"Dataset generated and saved as {output_file_final}")
