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

export function postUserLogInAPI(data){
        // await axios.post(api, model).then(function (response) {
        //     console.log(api, response.status)
        //     if(response.status == 200){
        //         // console.log("success",response)
        //         commit("setToken", response.data)
        //         console.log("logged in")
        //     }
        // })
    return axios({
        url: "/user/login",
        method: 'post',
        data: data
    })
}

export function getUserAPI(){
    return axios({
        url: "/user/",
        method: 'get'
    })
}

export function getUserIdAPI(user_id){
    return axios({
        url: "/user/" + user_id,
        method: 'get'
    })
}

export function getUserMyAPI(){
    return axios({
        url: "/user/my",
        method: 'get'
    })
}

export function postUserAPI(data){
    return axios({
        url: "/user/",
        method: 'post',
        data: data
    })
}

export function getTaskAPI(){
    return axios({
        url: "/task/",
        method: 'get'
    })
}

export function getTaskIdAPI(task_id){
    return axios({
        url: "/task/" + task_id,
        method: 'get'
    })
}

export function postTaskAPI(data){
    return axios({
        url: "/task/",
        method: 'post',
        data: data
    })
}

export function getWorkhourAPI(){
    return axios({
        url: "/workhour/",
        method: 'get'
    })
}

export function getWorkhourIdAPI(workhour_id){
    return axios({
        url: "/workhour/" + workhour_id,
        method: 'get'
    })
}

export function getWorkhourMyPI(){
    return axios({
        url: "/workhour/my",
        method: 'get'
    })
}

export function postWorkhourAPI(data){
    return axios({
        url: "/workhour/",
        method: 'post',
        data: data
    })
}