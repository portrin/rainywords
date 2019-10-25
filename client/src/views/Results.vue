<template>
    <div class="results">
        <div class="title-results">Results:</div>

        <div v-for="result in results" :key="result.id">
         <p>
            <span><b>{{ result.username }}</b></span><br />
            <span>{{ result.score }}</span>
        </p>
    </div>
    </div>
</template>

<script>
import Service from '../services/Service';

export default {
  name: 'Results',
  data () {
    return {
        results: []
    }
  },
  mounted() {
      this.getResults()
  },
  methods: {
    async getResults () {
      const response = await Service.fetchResults()
      this.results = response.data
    }
  }
}
</script>

<style lang="scss" scoped>
@import "../sass/_variables.scss";

.title-results {
    font-size: 1.625rem;
    color: $theme-blue-color;
    font-weight: $font-weight-bold;
}
</style>