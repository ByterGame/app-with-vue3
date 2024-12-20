import axios from 'axios';

const apiUrl = 'http://localhost:8000/api/users/';

export const authService = {
    register(userData) {
        return axios.post(`${apiUrl}register/`, userData);
    },
    login(userData) {
        return axios.post(`${apiUrl}login/`, userData);
    },
    // updateMoney(userData) {
    //     return axios.post(`${apiUrl}updateMoney/`, userData);
    // },
    // updateHero(userData) {
    //     return axios.post(`${apiUrl}updateHero/`, userData);
    // },
    getData(username) {
        return axios.get(`${apiUrl}getData/`, {params : {username : username}});
    },
    updateData(userData) {
        return axios.post(`${apiUrl}updateData/`, userData);
    },
    getUsersStats(username){
        return axios.get(`${apiUrl}getStats/`, {params : {username : username}});
    }
};
