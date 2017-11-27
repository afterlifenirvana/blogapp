<template>
  <div class="well">
    <div class="posts-block">
      <div class="posts-header">
        <h3 class="title-head">{{ header }}</h3>
      </div>
      <div class="content-section">
        <div class="post-section" >
          <post-card v-for="item in data" :item="item" :key="item.id" ></post-card>
        </div>
        <span class="load-more">
          load more
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import Card from './PostCard.vue'
export default {
  name: 'bot-tray',
  components: {
    'post-card': Card
  },
  data () {
    return {
      header: 'LATEST POSTS'
    }
  },
  props: {
    data: {
      type: Array,
      required: true
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.well{
  background: #f8f8f8;
  width: 100%;
  position: relative;
}
.posts-block{
  transform: translate(0px,-99px);
  background: white;
  box-shadow: 0 30px 50px 0 rgba(1,1,1,.15);
  padding: 16rem 0 15rem 0;
  max-width: 1240px;
  margin: 0 auto 10rem;
}
.posts-header{
  margin-top: -4rem;
  margin-bottom: 8rem;
}
.posts-header h3{
  font-size: 1.5rem;
  text-transform: uppercase;
  text-align: center;
  padding-bottom: 3rem;
  font-weight: 600;
}
.title-head::after{
  background: rgba(51,51,51,0.2);
  content: "";
  height: 1px;
  width: 50px;
  position: absolute;
  margin-top: 6rem;
  left: 50%;
  margin-left: -25px;
}
.content-section{
  width: 65%;
  margin: 0 auto;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
.post-section{
  display: flex;
  flex-wrap: wrap;
}
.load-more{
  text-transform: uppercase;
  font-size: 1.1rem;
  color: white;
  text-transform: uppercase;
  padding: 12px 4.5rem 12px 4.5rem;
  background: black;
  border: 1px solid black;
  cursor: pointer;
}
.load-more:hover{
  box-shadow: 0 10px 20px 0 rgba(1,1,1,.15);
}
</style>
