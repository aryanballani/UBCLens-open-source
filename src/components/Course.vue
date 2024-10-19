<!-- components/Course.vue -->

  
 <template>
  <v-btn @click="$emit('back')">Back to Courses</v-btn>
  <h2>{{ courseId }}</h2>
  <LineChart 
    v-if="postDates.length > 0" 
    :x-axis-data="postDates" 
    :y-axis-data="postCounts" 
  />
</template>

<script setup>
import { ref, watch } from 'vue'
import LineChart from './LineChart.vue'
import Papa from 'papaparse' // Make sure to install this library using npm install papaparse
import { format, parseISO } from 'date-fns' // Library to handle dates. Install with npm install date-fns


const props = defineProps(['courseId', 'file'])
const emits = defineEmits(['back'])

const postDates = ref([])
const postCounts = ref([])

const fetchData = () => {
  // Use FileReader to read the CSV file from the local directory
  fetch(props.file)
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
watch(() => props.file, fetchData, { immediate: true })
</script>
  
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