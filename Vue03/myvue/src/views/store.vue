<template>
  <div>
    <a-input v-model="inputValue" />
    <p>AInput: {{inputValue}} -> lastLetter is {{inputValueLastLetter}}</p>
    <a-show :content="inputValue" />
    <p>appName: {{appName}} appNameWithVersion: {{appNameWithVersion}}</p>
    <p>userName: {{userName}} firstLetter: {{firstLetter}}</p>
    <button @click="handleChangeAppName">修改appName</button>
    <p>{{appVersion}}</p>
  </div>
</template>
<script>
import AInput from '_c/AInput.vue'
import AShow from '_c/AShow.vue'
// import vuex from 'vuex'
// const mapState = vuex.mapState
import { mapState, mapGetters, mapMutations } from 'vuex'
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
    // appVersion () {
    //   return this.$store.state.appVersion
    // },
    // userName () {
    //   return this.$store.state.user.userName
    // }
    // ...mapState([
    //   'appName'
    // ])
    ...mapState({
      appName: state => state.appName,
      userName: state => state.userName,
      appVersion: state => state.appVersion
    }),
    // ...mapState('user', {
    //   userName: state => state.userName
    // }),
    inputValueLastLetter () {
      return this.inputValue.substr(-1, 1)
    },
    appNameWithVersion () {
      return this.$store.getters.appNameWithVersion
    },
    ...mapGetters([
      'firstLetter'
    ])
  },
  methods: {
    // handleChangeAppName () {
    //   return this.$store.commit('SET_APP_NAME', {
    //     appName: 'newAppName'
    //   })
    // }
    ...mapMutations([
      'SET_APP_NAME',
      'SET_USER_NAME'
    ]),
    handleChangeAppName () {
      // this.$store.commit({
      //   type: 'SET_APP_NAME',
      //   appName: 'newAppName'
      // })
      this.SET_APP_NAME({
        appName: 'newAppName'
      })
      // this.$store.commit('SET_APP_VERSION')
    }
  }
}
</script>`
