<template>
  <div>
    <span>{{ movie.title }}</span>
    <button @click="deleteMovieList(movie)">Delete</button>
  </div>
</template>

<script>
import { mapActions } from "vuex"

export default {
  name: 'MyListItem',
  props: {
    movie: {
      type: Object,
    }
  },
  methods: {
    ...mapActions(["deleteMovieList"]),
  }
}
</script>

<style>

</style>