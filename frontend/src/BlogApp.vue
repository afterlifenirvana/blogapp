<template>
  <div id="app">
    <blog-header></blog-header>
    <router-view></router-view>
  </div>
</template>

<script>
import Blogheader from './components/Header'
export default {
  name: 'app',
  components: {
    'blog-header': Blogheader
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Josefin+Sans:400,600,700|Josefin+Slab:300,400,600,600i,700');
#app{
  font-family: 'Josefin Sans', sans-serif;
  height: 100%;
  font-weight: 600;
}
</style>
