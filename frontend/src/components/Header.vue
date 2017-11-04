<template>
  <div class="blog-header">
    <div class="logo">Big 8</div>
    <div class="links">
      <div><a>The Blog.</a></div>
      <div><a>Us.</a></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'blog-header'
}
</script>

<style scoped>
.blog-header{
  width: 100%;
  height: 4em;
  font-size: 1em;
  flex-basis: auto;
  box-shadow: 0px 3px 15px rgba(0,0,0,0.3);
  background: #4f8ef2; 
  align-items: center;
  border-bottom:1px solid black;
  display: flex;
}
.logo{
  
}
.links{
  display: flex;
  justify-content: space-around;
  flex-direction: row;
  text-align: center;
}
.links div{
  font-size: 2em; 
  height: 100%;
}


</style>


