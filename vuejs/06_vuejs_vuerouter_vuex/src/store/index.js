import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

const API_KEY = process.env.VUE_APP_MOVIE_API_KEY
const API_URL = 'https://api.themoviedb.org/3/movie/popular/'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movieCards: [],
    movieList: [],
  },
  mutations: {
    LOAD_MOVIE_CARDS: function (state, results) {
      state.movieCards = results
    },
    CREATE_MOVIE_LIST: function (state, movie) {
      state.movieList.push(movie)
    },
    DELETE_MOVIE_LIST: function (state, movie) {
      const index = state.movieList.indexOf(movie)
      state.movieList.splice(index, 1)
    }
  },
  actions: {
    LoadMovieCards: function ({commit}) {
      // console.log(API_KEY)
      axios({
        method: 'get',
        url: API_URL,
        params: {
          api_key: API_KEY,
          language: 'ko-KR',
        }
      })
        .then((res) => {
          console.log(res)
          commit('LOAD_MOVIE_CARDS', res.data.results)
        })
    },
    createMovieList: function ({ commit }, movie) {
      commit('CREATE_MOVIE_LIST', movie)
    },
    deleteMovieList: function ({ commit }, movie) {
      commit('DELETE_MOVIE_LIST', movie)
    },
  },
  modules: {
  }
})
