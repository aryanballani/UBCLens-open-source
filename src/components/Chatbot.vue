<script setup>
import { ref } from 'vue';

// Reactive variables to store user input and responses
const userInput = ref('');
const responses = ref([
  { type: 'bot', message: 'Hello! How can I assist you today?' }
]);

// Loading state to indicate when a response is being fetched
const loading = ref(false);

// Function to handle user input submission
const submitInput = async () => {
  if (userInput.value.trim()) {
    // Add the user input to the responses
    responses.value.push({ type: 'user', message: userInput.value });

    // Store user's message
    const prompt = userInput.value.trim();
    

    userInput.value = ''; // Clear the input field

    // Set the role description for the chatbot
    const introductoryContext = `You are a custom chatbot for a user looking at course information such as sentiments, responses from students each day. Now this is the user's prompt:`;
    // Set loading state to true
    loading.value = true;

    try {
      // Make an API call to get the chatbot response
      const response = await fetch("http://localhost:11434/api/generate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          model: "llama3.2", // Replace with your model name if different
          prompt: prompt // Send user's prompt to the backend
        })
      });

      // Check if the response is not ok (e.g., 404 or 500 errors)
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      // Read the entire response as text (since it might not be a single JSON object)
      const text = await response.text();
      let parsedData;

      // Attempt to parse the text as JSON
      try {
        parsedData = JSON.parse(`[${text.replace(/}\s*{/g, '},{')}]`); // Converting the separate JSONs into an array
      } catch (jsonError) {
        console.error("Error parsing JSON:", jsonError, "Response Text:", text);
        throw new Error("Invalid JSON received from the server.");
      }

      // Combine all segments of the 'response' fields into a single message
      const combinedMessage = parsedData.map(item => item.response).join(' ');

      // Add the bot's response to the responses array
      responses.value.push({
        type: 'bot',
        message: combinedMessage || "Sorry, I couldn't understand that."
      });
    } catch (error) {
      console.error('Error fetching bot response:', error);
      responses.value.push({
        type: 'bot',
        message: "There was an error processing your request. Please try again."
      });
    } finally {
      // Set loading state to false
      loading.value = false;
    }
  }
};
</script>

<template>
  <v-card class="pa-4 mt-4">
    <v-card-title class="text-green">Ask Me Anything!</v-card-title>
    <v-card-text>
      <!-- Chat display area -->
      <div class="chat-container">
        <div v-for="(response, index) in responses" :key="index" :class="response.type">
          <strong v-if="response.type === 'user'">You:</strong>
          <strong v-else>Bot:</strong>
          {{ response.message }}
        </div>

        <!-- Loading indicator -->
        <div v-if="loading" class="loading-indicator">
          <em>Loading response...</em>
        </div>
      </div>

      <!-- Input area -->
      <v-text-field
        v-model="userInput"
        label="Type your question here..."
        variant="outlined"
        color="green"
        @keyup.enter="submitInput"
      ></v-text-field>
      
      <!-- Submit button -->
      <v-btn color="green" @click="submitInput">Submit</v-btn>
    </v-card-text>
  </v-card>
</template>

<style scoped>
.chat-container {
  max-height: 200px;
  overflow-y: auto;
  margin-bottom: 1rem;
}

.user {
  text-align: right;
  margin-bottom: 0.5rem;
}

.bot {
  text-align: left;
  margin-bottom: 0.5rem;
}

.loading-indicator {
  text-align: center;
  margin: 1rem 0;
  color: gray;
}
</style>
