import axios from 'axios'

const BASE_URL = '//localhost:8000/'

const HTTP = axios.create({
  baseURL: BASE_URL
})

export default HTTP
