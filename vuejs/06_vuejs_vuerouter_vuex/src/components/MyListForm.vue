<template>
  <div>
    <input type="text" v-model.trim="movieTitle" @keyup.enter="createMovieList" />
    <button @click="createMovieList">Add</button>
  </div>
</template>

<script>
export default {
  name: 'MyListForm',
  data: function () {
    return {
      movieTitle: null,
    }
  },
  methods: {
    createMovieList: function () {
      const movie = {
        title: this.movieTitle,
      }
      if (movie.title) {
        this.$store.dispatch("createMovieList", movie); // actions 호출
      }
      this.movieTitle = null;
      // console.log(this.$store.state.movieList)
    },
  }
}
</script>

<style>

</style>