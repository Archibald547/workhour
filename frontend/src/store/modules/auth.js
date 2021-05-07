//store/modules/auth.js

import axios from 'axios';
const state = {
    token: "",
    expiration: Date.now(),
    username: null
};  
const getters = {
    isAuthenticated: (state) => state.token.length > 0 && state.expiration > Date.now()
};
const actions = {
    async LogIn({commit}, model) {
        const result = await axios.post("/api/auth", model)
        await commit('setToken', model.get('username'))
        if (result.data.success) {
            commit("setToken", result.data);
            // router.push("/");
          }
    },
    async LogOut({commit}){
    let token = null
    commit('logout', token)
    }
};
const mutations = {
    setUser(state, username){
        state.username = username
    },
    LogOut(state){
        state.username = null
        state.token = ""
    },
    setToken: (state, model) => {
        state.token = model.token;
        state.expiration = new Date(model.expiration)
      },
    clearToken: (state) => {
    state.token = "";
    state.expiration = Date.now();
    }
};
export default {
  state,
  getters,
  actions,
  mutations
};
