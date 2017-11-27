<template>
  <div class="slide">
    <div class="big-letter">
      W
    </div>
    <div class="post">
      <h2 class="title">
        <a>
          a very good post to read about something new to clear your mind
        </a>
      </h2>
      <div class="meta-data">
        By <a class="author">Rishi Sarswat</a>&emsp;/&emsp;In&emsp;<a class="category">Technology</a>
      </div>
      <div class="button">
        <span>
          <a>Read on</a>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
export default{
  data () {
    return {

    }
  }
}
</script>

<style scoped>
.slide{
  max-width: 1240px;
  height: calc(100% - 200px);
  width: 100%;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: flex-end;
}
.big-letter{
  font-size: 64rem;
  text-transform: uppercase;
  font-weight: 600;
  line-height: 1.2;
  color: rgba(0,0,0,.1);
  z-index: 1;
  position: absolute;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  pointer-events: none;
  text-transform: uppercase;
  padding-top: 100px;
  bottom: -50%;
  left: 50%;
  transform: translate(-50%,-10%);
}
.post{
  z-index: 9999;
  width: 100%;
  height: 100%;
  display: flex;
  flex-wrap: wrap;
  align-content: center;
  padding-top: 7%;
}
.title{
  color:white;
  touch-action: manipulation;
  width: 100%;
  font-size: 6.4rem;
  line-height: 1.1;
  transition: all .2s ease-in-out;
  text-shadow: 0 0 0 transparent;
  text-align: center;
  padding-bottom: 2rem;
  font-weight: 600;
}
.title>a{
  color: #ffffff;
  text-decoration: none;
  opacity: 1;
  word-wrap: break-word;
  text-transform: uppercase;
}
.title:hover>a{
  text-shadow: 0 5px 10px rgba(0,0,0,.3);
}
.meta-data{
  width: 100%;
  text-align: center;
  font-size: 1.5rem;
  color: white;
  padding-bottom: 4rem;
}
.author, .category{
  border-bottom: 1px solid transparent;
  padding-bottom: 3px;
  transition: border-bottom .1s ease-in-out;
  text-decoration: none;
}
.author:hover{
  border-bottom: 1px solid;
}
.category:hover{
  border-bottom: 1px solid;
}
.button{
  text-transform: uppercase;
  width: 100%;
  padding-bottom: 4rem;
  display: flex;
  justify-content: center;
}
.button>span{
  height: 40px;
  display: inline-block;
  text-align: center;
  text-decoration: none;
  padding: 0 20px;
  line-height: 40px;
  min-width: 160px;
  font-size: 1.1rem;
  border: 1px solid;
  outline: 0;
  transition: all .1s ease-in-out;
  touch-action: manipulation;
  background: white;
  color: #0288d1;
}
.button>span:hover{
  box-shadow: 0 10px 20px 0 rgba(1,1,1,.15);
}
</style>
