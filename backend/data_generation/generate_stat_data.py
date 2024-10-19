import pandas as pd
import random
from datetime import datetime, timedelta

# Define the key dates and parameters
start_date_stats = datetime(2024, 9, 1)
midterm_date_stats = datetime(2024, 10, 20)
final_date_stats = datetime(2024, 12, 22)
num_rows_stats = 3000  # Reduced the number of rows to 3000

# Topics from the STAT 200 slides
stats_topics = [
    "Confidence Intervals", "Hypothesis Testing", "Comparing Means", "ANOVA",
    "Probability Concepts", "Sampling Distributions", "Paired and Independent Samples",
    "Comparing Counts", "Testing Independence", "Association and Causality"
]

# Helper function to generate unique names
def generate_name():
    first_names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jenna", "Kevin", "Laura", "Mike", "Nina", "Oscar", "Paula", "Quinn", "Rachel", "Steve", "Tina", "Uma", "Victor", "Wendy", "Xander", "Yara", "Zach"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Helper function to generate STAT 200 questions based on topics
def generate_stats_question(topic):
    questions_stats = {
        "Confidence Intervals": [
            "How do we interpret a 95% confidence interval?", 
            "What is the difference between a confidence interval for a mean and a proportion?",
            "Why is the critical value different for 90% and 95% confidence intervals?"
        ],
        "Hypothesis Testing": [
            "What is the significance level in hypothesis testing?", 
            "How do we decide whether to reject the null hypothesis?", 
            "Can someone explain the concept of Type I and Type II errors?"
        ],
        # Add more questions for each topic similarly...
    }
    return random.choice(questions_stats.get(topic, ["What are your thoughts on this topic?"]))

# Helper function to generate unique answers based on topics for STAT 200
def generate_stats_answer(topic):
    answers_stats = {
        "Confidence Intervals": [
            "A 95% confidence interval suggests we are fairly sure that the interval contains the true population parameter.",
            "In confidence intervals, the margin of error is influenced by the chosen confidence level.",
            "When calculating confidence intervals, we rely on the central limit theorem for large samples.",
            "A wider confidence interval indicates greater uncertainty about the population parameter."
        ],
        "Hypothesis Testing": [
            "The significance level determines the threshold for deciding whether to reject the null hypothesis.",
            "In hypothesis testing, a p-value lower than 0.05 often leads to rejecting the null hypothesis.",
            "Type I error happens when we mistakenly reject a true null hypothesis, while Type II error occurs when we fail to reject a false one.",
            "The power of a hypothesis test is the probability of correctly rejecting a false null hypothesis."
        ],
        # Add more answers for each topic similarly...
        "Comparing Means": [
            "When comparing means, we often assume that the samples are independent and normally distributed.",
            "A paired t-test is useful when the samples are dependent, like measurements taken before and after treatment.",
            "The pooled standard deviation is an average of variances from both groups being compared."
        ],
        "ANOVA": [
            "In ANOVA, the null hypothesis states that all group means are equal.",
            "We use the F-ratio to compare the variability between groups to the variability within groups.",
            "A significant F-test indicates that there is at least one group mean that differs from the others."
        ],
        # Adding default answers for other topics
        "Probability Concepts": [
            "The probability of independent events occurring together is the product of their individual probabilities.",
            "Bayes' theorem helps in updating the probability of an event based on new evidence."
        ],
        "Sampling Distributions": [
            "A sampling distribution represents the distribution of a statistic over many samples drawn from the same population.",
            "The standard error measures the variability of a sampling distribution."
        ],
        "Paired and Independent Samples": [
            "Paired samples share a connection or dependency, such as repeated measures from the same subjects.",
            "Independent samples do not have any inherent relationship between the observations."
        ],
        "Comparing Counts": [
            "We use a chi-square test to compare observed and expected frequencies in categorical data.",
            "A chi-square statistic helps assess if there is a significant difference in categorical distributions."
        ],
        "Testing Independence": [
            "Two variables are independent if the occurrence of one event does not influence the probability of the other.",
            "Independence can be assessed using conditional probabilities."
        ],
        "Association and Causality": [
            "Correlation does not imply causation; other factors could be influencing both variables.",
            "Establishing causality requires ruling out confounding variables and showing a consistent, logical relationship."
        ]
    }
    
    # Randomly combine phrases to generate a unique answer
    base_answer = random.choice(answers_stats.get(topic, ["This is a default answer for this topic."]))
    additional_info = random.choice([
        " This concept is fundamental to statistical inference.", 
        " It is essential to validate assumptions before drawing conclusions.", 
        " Keep in mind the sample size and variability.", 
        " This is a crucial topic for understanding real-world data analysis."
    ])
    
    return base_answer + additional_info

# Helper function to generate date with realistic timestamp
def generate_date():
    base_date = start_date_stats + timedelta(days=random.randint(0, (final_date_stats - start_date_stats).days))
    random_time = timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59), seconds=random.randint(0, 59))
    return base_date + random_time

# Generate the dataset for STAT 200
data_stats = []
negative_comments = ["I don't think you're correct.", "That's wrong.", "I disagree with your point.", 
                     "That doesn't seem accurate.", "I'm not convinced by this explanation.", 
                     "This is not convincing at all."]

negative_comment_count_stats = 0

for _ in range(num_rows_stats):
    topic = random.choices(stats_topics, weights=[1 if t not in ["Hypothesis Testing", "Comparing Means", "ANOVA"] else 3 for t in stats_topics])[0]
    is_negative = negative_comment_count_stats < 50 and random.random() < 0.01
    if is_negative:
        negative_comment_count_stats += 1
    
    entry = {
        "topic_id": random.randint(1000000, 9999999),
        "topic_title": f"STAT 200: {topic}",
        "topic_message": generate_stats_question(topic),  # Topic message is the question
        "topic_author_id": random.randint(100000, 200000),
        "topic_author_name": generate_name(),
        "topic_created_at": generate_date().strftime("%Y-%m-%d %H:%M:%S PDT"),
        "topic_posted_at": generate_date().strftime("%Y-%m-%d %H:%M:%S PDT"),
        "post_author_id": random.randint(100000, 200000),
        "post_author_name": generate_name(),
        "post_id": random.randint(1000000, 9999999),
        "post_parent_id": None if random.random() > 0.6 else random.randint(1000000, 9999999),
        "post_message": generate_stats_answer(topic) if not is_negative else random.choice(negative_comments),  # Unique post message or negative comment
        "post_likes": random.randint(0, 15),
        "post_timestamp": generate_date().strftime("%Y-%m-%d %H:%M:%S PDT")
    }
    data_stats.append(entry)

# Convert the generated data into a DataFrame
df_stats_200_final = pd.DataFrame(data_stats)

# Save the final dataset to a CSV file
output_file_stats_final = "STAT_200_Discussion_Data.csv"
df_stats_200_final.to_csv(output_file_stats_final, index=False)

print(f"Dataset generated and saved as {output_file_stats_final}")
