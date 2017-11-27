<template>
<div>
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
          <b-dropdown id="ddown1" text="BLOG " size="sm">
            <div class="dd-wrapper">
              <b-dropdown-item>GEEKY</b-dropdown-item>
            </div>
            <div class="dd-wrapper">
              <b-dropdown-item>SOME RANDOM SHIT</b-dropdown-item>
            </div>
          </b-dropdown>
        </div>
        <div><a>US</a></div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import bDropdown from 'bootstrap-vue/es/components/dropdown/dropdown'

export default {
  name: 'blog-header',
  data () {
    return {
    }
  },
  computed: {
    hasCover () {
      if (this.$route.meta.hasCover) {
        return true
      } else {
        return false
      }
    }
  },
  components: {
    bDropdown
  }
}
</script>

<style scoped>
.header-wrapper{
  background:#0288d1;
  top: 0;
  width: 100%;
  z-index: 999;
  position: fixed;
  left:0;  
  height: 11rem;
}
.blog-header{
  width: 100%;
  height: 7rem;
  flex-basis: auto;
  align-items: flex-end;
  display: flex;
  justify-content: space-between;
  color: white;
  z-index: 99999;
  font-weight: 600;
}
.logo{
  display: flex;
  font-size: 3rem;
  z-index: 99999;
}
.links{
  display: flex;
  justify-content: space-around;
  flex-direction: row;
  text-align: center;
  z-index: 99999;
  margin-bottom: 0.2rem;
  align-items: center;
}
.links>div{
  padding-right: 20px;
  height: 100%;
}
.links div a{
  font-size: 1.2rem;
}
.dd-wrapper{
  height: 100%;
  width: 100%;
}
.back-cover{
  width: 100%;
  background: #0288d1;
}
</style>
