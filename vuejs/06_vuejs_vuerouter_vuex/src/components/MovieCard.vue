<template>
  <div>
    <h2>{{ movieCard.title }}</h2>
    <img :src="posterUrl" alt="">
    <hr>
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movieCard: Object,
  },
  computed: {
    posterUrl: function () {
      const imgUrl = `https://image.tmdb.org/t/p/w500/${this.movieCard.poster_path}`
      return imgUrl
    }
  }
}
</script>

<style>

</style>