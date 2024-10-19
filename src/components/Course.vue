<script setup>
  import Chatbot from './Chatbot.vue';
  import { useRouter } from 'vue-router'
  import { reactive , ref, onMounted} from 'vue'
  import { watch } from 'vue'
  import LineChart from './LineChart.vue'
  import Papa from 'papaparse' // Make sure to install this library using npm install papaparse
  import { format, parseISO } from 'date-fns' // Library to handle dates. Install with npm install date-fns


  const postDates = ref([])
  const postCounts = ref([])

  const fetchData = () => {
    // Use FileReader to read the CSV file from the local directory
    fetch(`../../data/discussion_data/${props.courseId}.csv`)
      .then((response) => response.text())
      .then((csvData) => {
        processCsv(csvData)
      })
      .catch((error) => {
        console.error('Error fetching course data:', error)
      })
  }

  const processCsv = (csvData) => {
    Papa.parse(csvData, {
      header: true,
      skipEmptyLines: true,
      complete: (results) => {
        const dateCountMap = new Map()

        // Iterate over each row in the CSV
        results.data.forEach((row, index) => {
          // Check if the 'post_timestamp' field exists and is not empty
          if (!row['post_timestamp']) {
            console.warn(`Skipping row ${index} with missing or undefined post_timestamp:`, row);
            return;
          }

          // Log the keys of each row for debugging
          if (index === 0) {
            console.log("Row keys:", Object.keys(row)); // Log the keys of the first row to confirm column names
          }

          // Parse the timestamp using JavaScript's Date object after removing timezone
          try {
            // Remove the timezone abbreviation (e.g., "PDT") using a regex
            const cleanedTimestamp = row["post_timestamp"].replace(/\s[A-Z]+$/, "");

            // Create a new Date object and extract only the date (ignoring the time)
            const fullDate = new Date(cleanedTimestamp);
            const dateOnly = fullDate.toISOString().split("T")[0]; // Format as 'YYYY-MM-DD'

            // Update the count for each date
            if (dateCountMap.has(dateOnly)) {
              dateCountMap.set(dateOnly, dateCountMap.get(dateOnly) + 1);
            } else {
              dateCountMap.set(dateOnly, 1);
            }
          } catch (error) {
            console.error(`Error parsing date in row ${index}:`, row["post_timestamp"], error);
          }
        });

        // Extract dates and counts into arrays
        postDates.value = Array.from(dateCountMap.keys());
        postCounts.value = Array.from(dateCountMap.values());

        // Debugging: Log the parsed data
        console.log("Parsed Dates:", postDates.value);
        console.log("Parsed Counts:", postCounts.value);
      }
    })
  }
  
  // Defining props
  const props = defineProps({
      courseId: {
        type: String,
        required: true
      }
    })

  watch(() => `../../data/discussion_data/${props.courseId}.csv`, fetchData, { immediate: true })
  
  // Using router to navigate back
  const router = useRouter()
  
  const goBack = () => {
    router.push('/')
  }


  // Reactive object for sentiment percentages
  var sentimentPercentages = reactive({
    veryPositive: 50,
    positive: 0,
    neutral: 0,
    negative: 0,
    veryNegative: 0
  })

  const isLoading = ref(true); // New loading state


  onMounted(async () => {
  try {
    const sentimentData = await import(`../../data/sentiment_analysis/${props.courseId}.json`);
    sentimentPercentages = {
      veryPositive: sentimentData.veryPositive,
      positive: sentimentData.positive,
      neutral: sentimentData.neutral,
      negative: sentimentData.negative,
      veryNegative: sentimentData.veryNegative,
    };
  } catch (error) {
    console.error("Failed to load sentiment data:", error);
  } finally {
    isLoading.value = false;
  }
});
</script>



<template>
  <v-container fluid class="pa-0">
    <v-row>
      <!-- Back Button -->
      <v-col cols="12" class="pa-4">
        <v-btn
          prepend-icon="mdi-arrow-left"
          variant="text"
          color="green"
          @click="goBack"
        >
          Back to Courses
        </v-btn>
      </v-col>
    </v-row>

    <v-row class="fill-height">
      <!-- Graph Section (Left side) -->
      <v-col cols="12" md="7" class="pa-6">
        <v-card class="h-100">
          <v-card-title class="text-green pb-4">Grade Distribution - {{ courseId }}</v-card-title>
          <div class="graph-container pa-4" style="height: 400px">
            <v-card-text>
              <div style="width: 100%; height: 400px;">
                <LineChart
                  v-if="postDates.length > 0"
                  :x-axis-data="postDates"
                  :y-axis-data="postCounts"
                />
              </div>
            </v-card-text>
          </div>
        </v-card>
      </v-col>

      <!-- Right Side Panels -->
      <v-col cols="12" md="5" class="pa-6">
        <!-- Top Panel -->
        <v-card class="mb-6">
          <v-card-title class="text-green">Course Sentiment Summary</v-card-title>
          <v-card-text>
            <!-- Conditional Rendering -->
            <div v-if="isLoading">Loading sentiment data...</div>
            <div v-else>
              <div class="sentiment-row mb-2">
                <span>Very Positive comments</span>
                <v-progress-linear
                  :model-value="sentimentPercentages.veryPositive"
                  color="yellow"
                  height="10"
                  class="progress-bar"
                ></v-progress-linear>
              </div>

              <div class="sentiment-row mb-2">
                <span>Positive comments</span>
                <v-progress-linear
                  :model-value="sentimentPercentages.positive"
                  color="yellow"
                  height="10"
                  class="progress-bar"
                ></v-progress-linear>
              </div>

              <div class="sentiment-row mb-2">
                <span>Neutral comments</span>
                <v-progress-linear
                  :model-value="sentimentPercentages.neutral"
                  color="yellow"
                  height="10"
                  class="progress-bar"
                ></v-progress-linear>
              </div>

              <div class="sentiment-row mb-2">
                <span>Negative comments</span>
                <v-progress-linear
                  :model-value="sentimentPercentages.negative"
                  color="yellow"
                  height="10"
                  class="progress-bar"
                ></v-progress-linear>
              </div>

              <div class="sentiment-row mb-2">
                <span>Very Negative comments</span>
                <v-progress-linear
                  :model-value="sentimentPercentages.veryNegative"
                  color="yellow"
                  height="10"
                  class="progress-bar"
                ></v-progress-linear>
              </div>
            </div>
          </v-card-text>
        </v-card>

        <!-- Bottom Panel -->
        <v-card>
          <v-card-title class="text-green">Course Information</v-card-title>
          <v-card-text>
            <div class="text-body-1 mb-2">
              <strong>Professor:</strong> Dr. Smith
            </div>
            <div class="text-body-1 mb-2">
              <strong>Term:</strong> 2024W
            </div>
            <div class="text-body-1">
              <strong>Description:</strong> Introduction to Software Engineering. 
              Learn about software development lifecycle, testing, and project management.
            </div>
          </v-card-text>
        </v-card>
        <chatbot />
      </v-col>
    </v-row>
  </v-container>
</template>


<style scoped>
  .text-green {
    color: #42b883 !important;
  }
  
  .graph-container {
    width: 100%;
    height: 100%;
    min-height: 400px;
  }
  
  :deep(.v-card) {
    border-color: #42b883;
  }
  </style>