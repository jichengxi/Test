<template>
  <input @input="handleInput" />
</template>
<script>
export default {
  name: 'AInput',
  methods: {
    handleInput (event) {
      const value = event.target.value
      this.$emit('input', value)
    }
  }
}
</script>
<!--:value="value"-->
<!--props: {-->
<!--    value: {-->
<!--      type: [String, Number],-->
<!--      default: ''-->
<!--    }-->
<!--  },-->
