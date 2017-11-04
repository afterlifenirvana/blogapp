<template>
  <div id="app">
    <blog-header></blog-header>
    <div class="bottom">
      <side-tray></side-tray>
      <!-- <blog-header></blog-header> -->
    </div>
  </div>
</template>

<script>
import Blogheader from './components/Header'
import SideTray from './components/SideTray'
export default {
  name: 'app',
  components: {
    'blog-header': Blogheader,
    'side-tray': SideTray
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Roboto+Condensed|Yanone+Kaffeesatz:300,400');
#app{
  font-family: 'Roboto Condensed', Helvetica, sans-serif;
  display: flex;
  flex-direction: column;
  height: 100%;
  overflow-y: hidden;
}
.bottom{
  font-family: 'Roboto Condensed', Helvetica, sans-serif;
  display: flex;
  flex-direction: row;
  height: 100%;
  overflow-y: hidden;
}
</style>
