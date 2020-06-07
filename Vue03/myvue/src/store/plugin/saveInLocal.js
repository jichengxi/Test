export default store => {
  // 刷新浏览器后第一次定义的操作，可以写在这里
  // console.log('store初始化了')
  if (localStorage.state) store.replaceState(JSON.parse(localStorage.state))
  store.subscribe((mutations, state) => {
    // console.log('提交mutations')
    // console.log(mutations)
    // console.log(state)
    localStorage.state = JSON.stringify(state)
  })
}
