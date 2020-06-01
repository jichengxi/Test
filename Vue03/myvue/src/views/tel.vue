<template>
  <div class="tel">
    <p>tel: 17768098793</p>
    <p>{{ message }}</p>
  </div>
</template>
<script>
export default {
  data () {
    return {
      message: ''
    }
  },
  mounted () {
    this.$bus.$on('on-click', (msg) => { this.message = msg })
  }
}
</script>
<style>
  .tel{
    border: 1px solid red;
  }
</style>
