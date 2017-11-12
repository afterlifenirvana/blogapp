<template>
  <div class="header-wrapper">
    <div class="container blog-header">
      <div class="logo">
        <span>
          big
        </span>
         <span> 
           8
         </span>
      </div>
      <div class="links">
        <div>
          <b-dropdown id="ddown1" text="BLOG" class="m-md-2">
            <b-dropdown-item>GEEKY</b-dropdown-item>
            <b-dropdown-item>SOME RANDOM SHIT</b-dropdown-item>
          </b-dropdown>
        </div>
        <div><a>US</a></div>
      </div>
    </div>
  </div>
</template>

<script>
import bDropdown from 'bootstrap-vue/es/components/dropdown/dropdown'

export default {
  name: 'blog-header',
  components: {
    bDropdown
  }
}
</script>

<style scoped>
.header-wrapper{
  background:#0288d1;
}
.blog-header{
  width: 100%;
  height: 7rem;
  flex-basis: auto;
  align-items: flex-end;
  display: flex;
  justify-content: space-between;
  color: white;
  z-index: 1;
  font-weight: 600;
}
.logo{
  display: flex;
  font-size: 3rem;
}
.links{
  display: flex;
  justify-content: space-around;
  flex-direction: row;
  text-align: center;
}
.links div{
  padding-right: 20px; 
  height: 100%;
}
.links div a{
  font-size: 1.1rem;
}
</style>


