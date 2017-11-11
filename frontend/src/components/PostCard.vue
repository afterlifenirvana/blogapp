<template>
  <div class="post-card"> 
    <header class="post-header">
      <div class="header-title">
        <h2>
          <a>
            {{ title }} {{ title }}
          </a>
        </h2>
      </div>
      <div>
        <h3 class="post-tags">
          By <a>Rishi Sarswat</a> / In <a>Python</a>
        </h3>
      </div>
      <span class="big-letter">
        {{ big }}
      </span>
    </header>
    <div class="summary">
      <p>
      {{ summary }} {{ summary }} {{ summary }} {{ summary }} {{ summary }}
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
      title: 'Some article you should read',
      big: 'S',
      summary: 'This is something you shoudl read cause i have written and it will be good so you should pay attention to this and see whats this all about',
      author: 'Rishi Sarswat'
    }
  }
}
</script>

<style>
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
  text-decoration: none;
  padding-bottom: 3px;
  border-bottom: 1px solid transparent;
  -webkit-transition: border-bottom .1s ease-in-out;
  transition: border-bottom .1s ease-in-out;
  cursor: pointer;
}
.post-tags a:hover{
  color: #333333 !important;
}
.summary{
  font-size: 1.8rem;
  font-family: 'Josefin Slab', sans-serif;
  overflow: hidden;
  text-overflow: ellipsis;
  padding-bottom: 4rem;
}
.summary p{
  height: 13rem;
  display: -webkit-box;
  /* Fallback for non-webkit */
  margin: 0 auto;
  -webkit-line-clamp: 5;
  -webkit-box-orient: vertical;
  overflow: hidden;
  font-weight: 400;
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
