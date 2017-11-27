<template>
  <div class="bottom">
    <carousel></carousel>
    <bot-tray :data="data"></bot-tray>
  </div>
</template>

<script>
import BottomTray from './BottomTray'
import Bcarousel from './Bcarousel'
import BlogService from '../services/BlogService'

export default {
  name: 'Index',
  components: {
    'carousel': Bcarousel,
    'bot-tray': BottomTray
  },
  data () {
    return {
      data: []
    }
  },
  created () {
    BlogService.getPosts({action: 'recents'}).then((response) => {
      this.data = response.data.data
    })
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
