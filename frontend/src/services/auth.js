import axios from 'axios';

const apiUrl = 'http://localhost:8000/api/users/';

export const authService = {
    register(userData) {
        return axios.post(`${apiUrl}register/`, userData);
    },
    login(userData) {
        return axios.post(`${apiUrl}login/`, userData);
    },
};