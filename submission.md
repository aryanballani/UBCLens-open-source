# I Hacked-LA-2024
- "submit" your work by forking the repo (see README), and make a pull request with your final submission including an update of this submission.md file. 

List your group members:
> Divyansh Sharma
> Aryan Ballani
> Kanish Khanna
> Yiquan Liu
> Ankur Bhardwaj

# This Project
> Link to presentation: https://docs.google.com/presentation/d/1YN8AtAZXZ0r3MUmAFQZXwMceFUEDUzPNdY-BK6KyXN8/edit#slide=id.g30cac874191_0_13 



> Give a brief description of the final product:

Choosing the right course at UBC can feel overwhelming. You check UBC Grades for averages and RateMyProf for reviews, but there’s still something missing: what’s the actual environment inside the course? Are discussions lively or disengaged? Until now, there hasn’t been an easy way to find out.

Introducing UBC Lens – a web app that gives students a real insider’s perspective on courses. Using data from Canvas, UBC Lens goes beyond grades and ratings. It employs sentiment analysis to capture the mood in discussions, count vectorization to highlight key topics and trends, and frequency metrics to measure student engagement levels.

UBC Lens offers more than just surface-level information. By analyzing real interactions, it helps students choose courses where they can thrive and truly connect with their learning experience.

# Reflection
## Approach
> What was your approach to the dataset? What problem did you want to solve? What technology did you decide to use? How did your team split the work?


Since all of us are not taking any courses that use the canvas discussions, we decided to create mock data by replicating how the actual data would look like if we retrive it using canvas API, we also used the the hack-la data from the hackathon canvas course and could find key insights. 

The problem we are solving is to give students a platform where they can view the keywords, how people respond to queries, and also a chat bot using meta llama 3.2, which can answer any questions that the user has.

We used vue.js and vite for the frontend. In addition to that we also use Ollama for the chatbot.
The team was split into 3 parts: 3 people for the frontend, 1 for sentiment analysis and frontend, 1 for implementing the chatbot and creating the mock data.
# Wins / Challenges
> Describe some wins / challenges. What did you learn? What would you do differently next time?

Through this project we were able to grasp the concept of using the canvas API and vue.js to create a web app. We also learned how to host a chatbot using Ollama LLM and conducting sentiment analysis using a pre-trained model. Since, we were a team of 5 people, we faced challenges with merging and pull requests. One thing we would do differently next time is to use the github actions to automate the process of merging and pull requests.


