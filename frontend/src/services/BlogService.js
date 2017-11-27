import http from '@/helpers/http-common'

export default class BlogApi {
  static getPosts (SearchDict) {
    return http.get('/api/posts/', { params: SearchDict })
  }
}
