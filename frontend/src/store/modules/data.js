import api from '../../api'
import axios from 'axios'

// initial state
const state = {
  // shape: [{ id, title, genres, viewCnt, rating }]
  movieSearchList: [],
  userList: [],
}

// actions
const actions = {
  async searchMovies({ commit }, params) {
    const resp = await api.searchMovies(params)
    const movies = resp.data.map(d => ({
      id: d.id,
      title: d.title,
      genres: d.genres_array,
      viewCnt: d.view_cnt,
      rating: d.average_rating,
      view_users: d.view_users,
    }))
    console.log("movielist")
    if (params.genre) {
      var genre_movies = []
      console.log(params.genre)
      for (var [key, movie] of Object.entries(movies)) {
          if (movie.genres.includes(params.genre)) {
              console.log(movie)
              genre_movies.push(movie)
              commit('setMovieSearchList', genre_movies)
          }
      }

  } else if (params === 'rating') {
      axios.get(`/api/movies/rating`).then((res) => {
          movies = res.data.map(d =>
              ({
                  id: d.id,
                  title: d.title,
                  genres: d.genres_array,
                  view_cnt: d.view_cnt,
                  avg_rate: d.avg_rate,
                  view_users: d.view_users,
              })
          )
          commit('setMovieSearchList', movies)
      })
  } else if (params === 'views') {
      axios.get(`/api/movies/views`).then((res) => {
          movies = res.data.map(d =>
              ({
                  id: d.id,
                  title: d.title,
                  genres: d.genres_array,
                  view_cnt: d.view_cnt,
                  avg_rate: d.avg_rate,
                  view_users: d.view_users,
              })
          )
          commit('setMovieSearchList', movies)
      })
  } else {
    commit('setMovieSearchList', movies)
  }
  },
  async getusers({ commit }, params) {
    const resp = await api.getusers(params)
    const users = resp.data.map(d => ({
      username: d.username,
      gender: d.gender,
      age: d.age,
      occupation: d.occupation,
      view_users: d.user_views,
    }))
    console.log("userlist")
    
    commit('setUserList', users)
  }
}

// mutations
const mutations = {
  setMovieSearchList(state, movies) {
    state.movieSearchList = movies.map(m => m)
  },
  setUserList(state, users) {
    state.userList = users.map(m => m)
  }
}

export default {
  namespaced: true,
  state,
  actions,
  mutations
}