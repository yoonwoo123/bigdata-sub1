import axios from 'axios'

const apiUrl = '/api'

export default {
  searchMovies(params) {
    return axios.get(`${apiUrl}/movies/`, {
      params,
    })
  },
  getusers(params) {
    return axios.get(`${apiUrl}/profiles/`, {
      params,
    })
  }
}