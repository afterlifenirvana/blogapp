import Vue from 'vue'
import Router from 'vue-router'
import IndexView from '../components/Index'
import SearchView from '../components/Search'
import PostView from '../components/Post'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'IndexView',
      component: IndexView,
      meta: {
        hasCover: true
      }
    },
    {
      path: '/field/searchby/',
      name: 'SearchView',
      component: SearchView,
      meta: {
        hasCover: false
      }
    },
    {
      path: '/post/',
      name: 'Post',
      component: PostView,
      meta: {
        hasCover: true
      }
    }
  ]
})
