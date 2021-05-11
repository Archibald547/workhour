import axios from '../service/http'
// import QS from 'qs'

// export function userRejister(data) {
//     return axios({
//         url: `${base.url}/users/register`,
//         method: 'post',
//         data: QS.stringify(data)
//     })
// }

// export function userInfo() {
//     return axios({
//         url: `${base.url}/profile/all`,
//         method: 'get'
//     })
// }

export function userLogIn(data){
    var url = "/user/login"
    var method = 'post'
        // await axios.post(api, model).then(function (response) {
        //     console.log(api, response.status)
        //     if(response.status == 200){
        //         // console.log("success",response)
        //         commit("setToken", response.data)
        //         console.log("logged in")
        //     }
        // })
    return axios({
        url: url,
        method: method,
        data: data
    })
}