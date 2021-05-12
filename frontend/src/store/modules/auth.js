//store/modules/auth.js

import { postUserLogInAPI} from "../../service/apis.js";

const state = {
    token: "",
    expiration: Date.now(),
    username: null
};  
const getters = {
    getToken: (state) => state.token,
    getUsername: (state) => state.username,
    getFullname: (state) => state.fullname,
    isAuthenticated: (state) => state.token.length > 0 && state.expiration > Date.now()
    // isAuthenticated: () => localStorage.token != null && Date.parse(localStorage.expiration) > Date.now()
    // isAuthenticated: () => localStorage.token != null
    
};
const actions = {
    async LogIn({commit}, model) {
        console.log("logging in")
         await postUserLogInAPI(model).then(function (response) {
                if(response.status == 200){
                    commit("LogIn", response.data)
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
        commit('LogOut')
        console.log("logged out")
    }
};
const mutations = {
    LogIn(state,data){
        state.username = data.username
        state.fullname = data.fullname
        state.token = data.token
        state.expiration = new Date(data.expiration)
    },
    LogOut(state){
        state.username = null
        state.fullname = null
        state.token = ""
        state.expiration = Date.now();
    },
    // setToken: (state, model) => {
    //     state.token = model.token
    //     state.expiration = new Date(model.expiration)
    //   },
    // clearToken: (state) => {
    //     state.token = "";
        
    // }
};
export default {
  state,
  getters,
  actions,
  mutations
};
