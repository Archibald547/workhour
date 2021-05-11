//store/modules/auth.js

import { userLogIn} from "../../service/apis.js";

const state = {
    token: "",
    expiration: Date.now(),
    username: null
};  
const getters = {
    getToken: (state) => state.token,
    // isAuthenticated: (state) => state.token.length > 0 && state.expiration > Date.now()
    isAuthenticated: () => localStorage.token > 0 && Date.parse(localStorage.expiration) > Date.now()
};
const actions = {
    async LogIn({commit}, model) {
        console.log("logging in")
         await userLogIn(model).then(function (response) {
                if(response.status == 200){
                    // console.log("success",response)
                    commit("setToken", response.data)
                    
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
        state.token = model.token
        state.expiration = new Date(model.expiration)
        localStorage.setItem( 'token', model.token)
        localStorage.setItem( 'expiration', new Date(model.expiration) )
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
