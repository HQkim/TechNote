<template>
  <div>
    <button @click="pickMovie">PICK</button>
    <h2>{{ movieTitle }}</h2>
    <img :src="movieUrl" alt="">
  </div>
</template>

<script>
import { mapState } from 'vuex'
import _ from 'lodash'

export default {
  name: 'Random',
  data: function () {
    return {
      movieTitle: '',
      movieUrl: '',    
    }
  },
  computed: {
    ...mapState(['movieCards'])
  },
  methods: {
    pickMovie: function () {
      const selectedMovie = _.sampleSize(this.movieCards, 1)[0]
      this.movieTitle = selectedMovie.title
      this.movieUrl = `https://image.tmdb.org/t/p/w500/${selectedMovie.poster_path}`
      // console.log(selectedMovie)
      // console.log(this.movieUrl)
      // console.log(this.movieUrl)
      
    }
  }
}
</script>

<style>

</style>