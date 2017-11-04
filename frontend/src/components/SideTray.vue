<template>
  <div class="well">
    <div class="search">
      search bar 
    </div>
    <post-card></post-card>
    <post-card></post-card>
    <post-card></post-card>
    <post-card></post-card>
    <post-card></post-card>
    <post-card></post-card>
    <post-card></post-card>
    <post-card></post-card>
    <post-card></post-card>
  </div>
</template>

<script>
import Card from './PostCard.vue'
export default {
  name: 'side-tray',
  components: {
    'post-card': Card
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.well{
  display: flex;
  flex-direction: column;
  overflow: auto;
  flex-basis: 33%;
  background: #4f8ef2; 
}
::-webkit-scrollbar {
  width: 0px;
  background: transparent;
}
.search{
  width: 100%;
  height: 10%;
  text-align: center;
  color: white;
}
</style>
