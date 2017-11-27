<template>
<div class="bottom">
  <carousel></carousel>
</div>
</template>

<script>
import Bcarousel from './Bcarousel'

export default {
  name: 'post',
  data () {
    return {

    }
  },
  components: {
    'carousel': Bcarousel
  }
}
</script>

<style scoped>
.bottom{
  font-family: 'Josefin Sans', sans-serif;
  height: 100%;
}
</style>
