<template>
  <div id="app">
    <h1>My First Youtube Project</h1>
    <SearchBar @input-search="onInputSearch" />
    <VideoDetail :video="selectedVideo" />
    <br />
    <VideoList :videos="videos" @select-video="onSelectVideo" />
  </div>
</template>

<script>
import axios from "axios";
import SearchBar from "@/components/SearchBar";
import VideoList from "@/components/VideoList";
import VideoDetail from "@/components/VideoDetail";

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY;
const API_URL = "https://www.googleapis.com/youtube/v3/search";

export default {
  name: "App",
  data: function () {
    return {
      inputValue: "",
      videos: [],
      selectedVideo: "",
    };
  },
  methods: {
    onInputSearch: function (inputText) {
      // console.log("데이터가 SearchBar로부터 올라옴");
      // console.log(inputText);
      this.inputValue = inputText;

      const params = {
        key: API_KEY,
        part: "snippet",
        type: "video",
        q: this.inputValue,
      };

      axios
        .get(API_URL, {
          params,
        })
        .then((res) => {
          // console.log(res.data.items);
          this.videos = res.data.items;
          if (!this.selectedVideo) {
            this.selectedVideo = this.videos[0];
            console.log(this.selectedVideo);
          }
          // console.log(this.videos);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    onSelectVideo: function (video) {
      this.selectedVideo = video;
    },
  },
  components: {
    SearchBar, // ES6 전에는 SearchBar: SearchBar, 로 썼어야함.
    VideoList,
    VideoDetail,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
