<template>
  <div class="bottom">
    <bot-tray></bot-tray>
  </div>
</template>

<script>
import BottomTray from './BottomTray'
export default {
  data () {
    return {
    }
  },
  components: {
    'bot-tray': BottomTray
  }
}
</script>

<style scoped>
.bottom{
  font-family: 'Josefin Sans', sans-serif;
  height: 100%;
}
</style>
