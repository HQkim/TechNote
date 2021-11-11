<template>
  <div>
    <h2>로또 번호</h2>
    <button @click="getLuckyNums">로또번호나와!</button>  
    <h2>오늘의 로또 번호 {{ $route.params.lottoNum }}개</h2>
    <!-- <p>{{ $route.params }}</p> -->
    <ul>
      <li v-for="(num, idx) in selectedLuckyNums" :key="idx">{{ num }}</li>
    </ul>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'TheLotto',
  data: function () {
    return {
      selectedLuckyNums: [],
    }
  },
  methods: {
    getLuckyNums: function () {
      const numbers = _.range(1, 46)
      this.sampleNums = _.sampleSize(numbers, this.$route.params.lottoNum)  // 임시 변수 이렇게 사용가능
      this.selectedLuckyNums = _.sortBy(this.sampleNums)
    }
  }
}
</script>

<style>

</style>