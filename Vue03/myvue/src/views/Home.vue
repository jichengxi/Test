<template>
  <div class="home">
    <p>{{food}}</p>
    <button @click="handClick('back')">返回上一页</button>
    <button @click="handClick('push')">跳转到parent</button>
    <button @click="handClick('replace')">替换到parent</button>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    // HelloWorld
  },
  props: {
    food: {
      type: String,
      default: 'apple'
    }
  },
  beforeRouteEnter (to, from, next) {
    console.log(to.name, from.name)
    next(vm => {
      console.log(vm)
    })
  },
  beforeRouteLeave (to, from, next) {
    const leave = confirm('您确定要离开吗？')
    if (leave) next()
    else next(false)
  },
  methods: {
    handClick: function (type) {
      if (type === 'back') this.$router.back()
      else if (type === 'push') {
        const name = 'lison'
        this.$router.push({
          path: `/argu/${name}`
          // name: 'argu',
          // params: {
          //   name: 'lison'
          // }
          // query: {
          //   name: 'lison'
          // }
        })
      } else if (type === 'replace') {
        this.$router.replace({
          name: 'parent'
        })
      }
    }
  }
}
</script>
