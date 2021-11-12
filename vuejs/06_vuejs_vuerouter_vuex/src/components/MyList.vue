<template>
  <div>
    <h2>MyList</h2>
    <MyListItem v-for="(movie, index) in movieList" :key="index" :movie="movie"/>
  </div>
</template>

<script>
import { mapState } from "vuex";
import MyListItem from '@/components/MyListItem'

export default {
  name: 'MyList',
  components: {
    MyListItem,
  },
  computed: {
    ...mapState(["movieList"]),
  }
}
</script>

<style>

</style>