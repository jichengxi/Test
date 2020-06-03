const state = {
  userName: 'jichengxi'
}
const getters = {
  firstLetter: (state) => {
    return state.userName.substr(0, 1)
  }
}
const mutations = {
  SET_USER_NAME (state, params) {
    // console.log(state)
    // console.log(params)
    state.userName = params
  }
}
const actions = {
  //
}

export default {
  // namespaced: true,
  state,
  getters,
  mutations,
  actions
}
