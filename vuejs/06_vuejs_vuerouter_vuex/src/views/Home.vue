<template>
  <div>
    <MovieCard 
      v-for="movieCard in movieCards"
      :key="movieCard.id"
      :movieCard="movieCard"  
    />
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
import { mapState } from 'vuex'

export default {
  name: 'Home',
  components: {
    MovieCard,
  },
  created: function () {
    this.$store.dispatch('LoadMovieCards')
  },
  computed: {
    ...mapState(['movieCards'])
  }
}
</script>

<style>

</style>