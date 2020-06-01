<template>
  <div>
    <a-input v-model="inputValue" />
    {{inputValue}}
  </div>
</template>
<script>
import AInput from '_c/AInput.vue'
export default {
  name: 'store',
  data () {
    return {
      inputValue: ''
    }
  },
  comments: {
    AInput: AInput
  }
}
</script>
