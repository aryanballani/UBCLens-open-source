<script setup>
  import { defineProps } from 'vue'
  import { useRouter } from 'vue-router'
  import { reactive } from 'vue'
  
  // Defining props
  const props = defineProps({
    courseId: {
      type: String,
      required: true
    }
  })
  
  // Using router to navigate back
  const router = useRouter()
  
  const goBack = () => {
    router.push('/')
  }

  // Reactive object for sentiment percentages
  const sentimentPercentages = reactive({
    veryPositive: 25,
    positive: 30,
    neutral: 20,
    negative: 15,
    veryNegative: 10
  })

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
                <line-chart />
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
              <span>Negative  comments</span>
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
      </v-col>
    </v-row>
  </v-container>
</template>

<!-- Styling -->
<style scoped>
.text-green {
  color: #42b883 !important;
}

.text-body-1 {
display: flex;
justify-content: space-between;
align-items: center;  
}

.sentiment-row {
display: flex;
justify-content: space-between;
align-items: center;
}

/* Progress bar styling to keep it smaller and aligned right */
.progress-bar {
  width: 50%; /* Adjust this width to control the size */
  margin-left: 20px; /* Adds space between the text and the bar */
}

/* Optional: Add padding or margin if needed for card text */
.v-card-text {
  padding-right: 10px;
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