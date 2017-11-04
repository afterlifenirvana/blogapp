<template>
  <div class="container post-card" v-bind:style="{height: height+'px'}">
    <div class="blog-title">
      Title
      Title
      Title
      Title
      Title
      Title
      Title
    </div>
    <div class="category">
      #python
    </div>
    <div class="summary">
      <p>
      This is some random blog about random stuff in life.
      so dont be shitty be happy. we will talk about everything and anything. Maybe it will make sense maybe it won't who cares.
      the desing is pretty shitty I know right but this is what happens when i design it.
      </p>
    </div>  
    <div class="detail">
      <div>
        Rishi Sarswat<br>
        11/11/2017 
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'post-card',
  data: function () {
    return {
      height: 0,
      rotate: 0
    }
  },
  mounted () {
    this.$nextTick(function () {
      window.addEventListener('resize', this.getWindowWidth)
      this.getWindowWidth()
      this.rotate = this.randomNumber(-10, 10)
    })
  },
  methods: {
    getWindowWidth (event) {
      this.windowWidth = document.documentElement.clientWidth
      this.height = this.$el.clientWidth
    },
    randomNumber (max, min) {
      return Math.floor(Math.random() * (max - min + 1)) + min
    }
  },
  beforeDestroy () {
    window.removeEventListener('resize', this.getWindowWidth)
    window.removeEventListener('resize', this.getWindowHeight)
  }
}
</script>

<style>
.post-card{
  width: 100%;
  text-align: center;
  padding-top: 2em;
  min-height: 20vh;
  font-weight: 500;
  overflow: hidden; 
  color:white;
  font-family: "Yanone Kaffeesatz";
  font-weight: 500;
  border-bottom: 1px solid black;
  /* box-shadow: 0 3px 3px 0 rgba(0, 0, 0, 0.16), 0 3px 3px 0 rgba(0, 0, 0, 0.23); */
}

/* .post-card::before{
    content:'';
    float:left;
    padding-top:100%;
} */

.blog-title{
  text-align: left;
  font-size: 1.5em;
  padding: 0.5em 1em 0em 1em;
  font-size: 2.5vmin;
  font-family: "Julius Sans One", sans-serif;
  font-weight: 600;
}
.category{
  text-align: left;
  padding: 0em 1em 0em 2em;
  word-wrap: break-word;
  font-size: 1em;
}
.summary p{
  text-align: left;
  padding: 0em 1em 0em 1.5em;
  font-size: 1.8vmin;
}
.detail{
  text-align: left;
  display: flex;
  justify-content: space-between;
  font-size: 1.8vmin;
  padding: 0em 1em 0em 1.5em;
}
</style>
