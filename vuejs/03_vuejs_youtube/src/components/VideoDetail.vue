<template>
  <div v-if="video">
    <iframe :src="videoURL" frameborder="0" width="480" height="270"></iframe>
    <h4>{{ videoTitle | stringUnescape }}</h4>
    <p>{{ videoDescription | stringUnescape }}</p>
  </div>
</template>

<script>
import _ from "lodash";

export default {
  name: "VideoDetail",
  props: {
    video: {
      type: [String, Object], // 처음에 아무것도 클릭안했을시 스트링
    },
  },
  computed: {
    videoURL: function () {
      const videoId = this.video.id.videoId;
      return `https://www.youtube.com/embed/${videoId}`;
    },
    videoTitle: function () {
      return `${this.video.snippet.title}`;
    },
    videoDescription: function () {
      return `${this.video.snippet.description}`;
    },
  },
  filters: {
    stringUnescape: function (rawText) {
      return _.unescape(rawText);
    },
  },
};
</script>

<style>
</style>