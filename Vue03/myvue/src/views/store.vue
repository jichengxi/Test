<template>
  <div>
    <a-input v-model="inputValue" />
    <p>AInput: {{inputValue}} -> lastLetter is {{inputValueLastLetter}}</p>
    <a-show :content="inputValue" />
    <p>appName: {{appName}} appNameWithVersion: {{appNameWithVersion}}</p>
    <p>userName: {{userName}} firstLetter: {{firstLetter}}</p>
    <button @click="handleChangeAppName">修改appName</button>
    <p>{{appVersion}}</p>
    <button @click="handleChangeUserName">修改userName</button>
    <button @click="registerModule">动态注册模块</button>
    <p v-for="(li, index) in todoList" :key="index">{{ li }}</p>
  </div>
</template>
<script>
import AInput from '_c/AInput.vue'
import AShow from '_c/AShow.vue'
// import vuex from 'vuex'
// const mapState = vuex.mapState
import { mapState, mapGetters, mapMutations, mapActions } from 'vuex'
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
      appVersion: state => state.appVersion,
      userName: state => state.user.userName,
      todoList: state => state.user.todo ? state.user.todo.todoList : ''
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
    ...mapActions([
      'updateAppName'
    ]),
    handleChangeAppName () {
      // this.$store.commit({
      //   type: 'SET_APP_NAME',
      //   appName: 'newAppName'
      // })
      // this.SET_APP_NAME({
      //   appName: 'newAppName'
      // })
      this.updateAppName()
      // this.$store.commit('SET_APP_VERSION')
    },
    handleChangeUserName () {
      this.SET_USER_NAME('vue-cource')
      // this.$store.dispatch('updateAppName', '123')
      // this.$store.state.user.userName = '1111' 错误方法
    },
    registerModule () {
      this.$store.registerModule(['user', 'todo'], {
        state: {
          todoList: [
            '学习mutations',
            '学习actions'
          ]
        }
      })
    }
  }
}
</script>`
