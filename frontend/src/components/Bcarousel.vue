<template>
  <div  class="carousel-wrapper">
    <carousel class="carousel" :perPage="1" paginationColor="#ffffff" :autoplayTimeout="3000" paginationActiveColor="#ffffff" :autoplay="true" :autoplayHoverPause="true" :loop="true">
      <slide class="slide-wrapper">
          <cover-post></cover-post>
      </slide>
      <slide class="slide-wrapper">
          <cover-post></cover-post>
      </slide>
    </carousel>
  </div>
</template>

<script>
import { Carousel, Slide } from 'vue-carousel'
import CoverPost from './CoverPost'
export default {
  data () {
    return {
      slide: 0,
      sliding: null
    }
  },
  methods: {
    onSlideStart (slide) {
      this.sliding = true
    },
    onSlideEnd (slide) {
      this.sliding = false
    }
  },
  components: {
    Carousel,
    Slide,
    CoverPost
  }
}
</script>
<style scoped>
.carousel-wrapper{
  height: 92%;
  background: #0288d1;
  padding-top: 15rem;
}
.carousel{
  width: 100%;
  background: #0288d1;
  height:100%;
}
.slide-wrapper{
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
}
</style>
