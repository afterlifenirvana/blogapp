<template>
  <div class="post-card"> 
    <header class="post-header">
      <div class="header-title">
        <h2>
          <a>
            {{ item.title }}
          </a>
        </h2>
      </div>
      <div>
        <h3 class="post-tags">
          By <a>{{ item.author.user.first_name + ' ' + item.author.user.last_name }}</a> / In <a>{{ item.category }}</a>
        </h3>
      </div>
      <span class="big-letter">
        {{ item.title[0] }}
      </span>
    </header>
    <div class="summary">
      <p>
        {{ item.short_summary }}
      </p>
    </div>
    <span class="read-more">
      <a>Read on</a>
    </span>
  </div>
</template>

<script>
export default {
  name: 'post-card',
  data: function () {
    return {
    }
  },
  beforeMount () {
    // console.log(this.item)
  },
  props: {
    item: {
      type: Object,
      required: true
    }
  }
}
</script>

<style scoped>
.post-card{
  margin-bottom: 9rem;
  padding-bottom: 10rem;
}
.post-card::after{
  content: "";
  background: rgba(51,51,51,0.2);
  height: 1px;
  width: 50px;
  position: absolute;
  margin-top: 14rem;
  left: 50%;
  margin-left: -25px;
}
.post-header{
  position: relative;
}
.big-letter{
  font-size: 26rem;
  line-height: 1.2;
  color: rgba(0,0,0,.07);
  z-index: 1;
  position: absolute;
  left: -7rem;
  top: 50%;
  -webkit-transform: translate(0,-50%);
  -ms-transform: translate(0,-50%);
  transform: translate(0,-50%);
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  pointer-events: none;
  text-transform: uppercase;
}
.header-title{
  padding-bottom: 2rem;
}
.header-title h2{
  text-transform: uppercase;
  font-size: 4rem;
  word-wrap: break-word;
  touch-action: manipulation;
  font-weight: 600;
}
.header-title h2 a{
  cursor: pointer;
}

.post-tags{
  font-size:1.5rem;
  color: #888888 !important;
  padding-bottom: 2rem;
}
.post-tags a{
  border-bottom: 1px solid transparent;
  padding-bottom: 3px;
  transition: border-bottom .1s ease-in-out;
  text-decoration: none;
}
.post-tags a:hover{
  border-bottom: 1px solid;
  color: black;
}
.summary{
  font-size: 2rem;
  font-family: 'Josefin Slab', sans-serif;
  overflow: hidden;
  text-overflow: ellipsis;
  padding-bottom: 4rem;
}
.summary p{
  height: 13.5rem;
  font-weight: 600;
  line-height: 1.4;
  display: -webkit-box;
  /* Fallback for non-webkit */
  margin: 0 auto;
  -webkit-line-clamp: 5;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}
.read-more{
  color: white;
  font-size: 1.1rem;
  text-transform: uppercase;
  padding: 12px 4.5rem 12px 4.5rem;
  background: #039be5;
  border: 1px solid #039be5;
}
.read-more:hover{
  box-shadow: 0 10px 20px 0 rgba(1,1,1,.15);
}
</style>
