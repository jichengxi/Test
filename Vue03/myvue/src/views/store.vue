<template>
  <div>
    <a-input v-model="inputValue" />
    <p>AInput: {{inputValue}}</p>
    <a-show :content="inputValue" />
<!--    <p>appName: {{appName}}</p>-->
    <p>userName: {{userName}}</p>
  </div>
</template>
<script>
import AInput from '_c/AInput.vue'
import AShow from '_c/AShow.vue'
// import vuex from 'vuex'
// const mapState = vuex.mapState
import { mapState } from 'vuex'
export default {
  name: 'store',
  data () {
    return {
      inputValue: ''
    }
  },
  components: {
    AInput: AInput,
    AShow: AShow
  },
  computed: {
    // appName () {
    //   return this.$store.state.appName
    // },
    // userName () {
    //   return this.$store.state.user.userName
    // }
    // ...mapState([
    //   'appName'
    // ])
    // ...mapState({
    //   appName: state => state.appName,
    // }),
    ...mapState('user', {
      userName: state => state.userName
    })
  }
}
</script>`
