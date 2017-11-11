<template>
  <div class="bottom">
    <b-carousel></b-carousel>
    <bot-tray></bot-tray>
  </div>
</template>

<script>
import BottomTray from './BottomTray'
import Bcarousel from './Bcarousel'

export default {
  name: 'Index',
  components: {
    'b-carousel': Bcarousel,
    'bot-tray': BottomTray
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
.bottom{
  font-family: 'Josefin Sans', sans-serif;
  height: 100%;
}
</style>
