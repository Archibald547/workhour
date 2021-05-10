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
        console.log("logging in")
        var api = "/user/login"
        await axios.post(api, model).then(function (response) {
            console.log(api, response.status)
            if(response.status == 200){
                // console.log("success",response)
                commit("setToken", response.data)
                console.log("logged in")
            }
        })
        // await commit('setToken', model.get('username'))
        // if (result.data.success) {
        //     commit("setToken", result.data);
        //     // router.push("/");
        //     console.log("logged in")
        //   }
    },
    async LogOut({commit}){
        console.log("logging out")
        let token = null
        commit('logout', token)
        console.log("logged out")
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
        console.log(state.token)
        console.log(state.expiration)
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
