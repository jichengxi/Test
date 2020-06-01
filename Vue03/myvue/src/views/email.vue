<template>
  <div class="email">
    <p>email: 948788684@qq.com</p>
    <button @click="handleClick">按我</button>
  </div>
</template>
<script>
export default {
  methods: {
    handleClick () {
      this.$bus.$emit('on-click', 'hello')
    }
  },
  mounted () {
    console.log(this.$bus)
  }
}
</script>
<style>
  .email{
    border: 1px solid green;
  }
</style>
