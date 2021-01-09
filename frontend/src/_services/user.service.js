import config from 'config';
import { authHeader } from '../_helpers';
import axios from 'axios'

export const userService = {
    login,
    logout,
    register,
    getAll,
    getById,
    update,
    delete: _delete
};

function login(username, password) {
    // const requestOptions = {
    //     method: 'POST',
    //     headers: { 'Content-Type': 'application/json' },
    //     body: JSON.stringify({ username: username,
    //          password: password })
    // };
    const params = new URLSearchParams();
    params.append("username", username);
    params.append("password", password);

    return axios.post(`${config.apiUrl}/login/access-token`, params)
        .then(handleResponse)
        .then(response => {
            console.log(`response:`)
            console.log(response)
            // store user details and jwt token in local storage to keep user logged in between page refreshes
            const token = response.data.access_token;
            localStorage.setItem('token', token);

            return response;
        });
}

function logout() {
    // remove user from local storage to log user out
    localStorage.removeItem('user');
}

function getAll() {
    const requestOptions = {
        method: 'GET',
        headers: authHeader()
    };

    return fetch(`${config.apiUrl}/users`, requestOptions).then(handleResponse);
}

function getById(id) {
    const requestOptions = {
        method: 'GET',
        headers: authHeader()
    };

    return fetch(`${config.apiUrl}/users/${id}`, requestOptions).then(handleResponse);
}

function register(user) {
    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(user)
    };
    console.log(user)
    console.log(`${config.apiUrl}`)
    return fetch(`${config.apiUrl}/users`, requestOptions).then(handleResponse);
}

function update(user) {
    const requestOptions = {
        method: 'PUT',
        headers: { ...authHeader(), 'Content-Type': 'application/json' },
        body: JSON.stringify(user)
    };

    return fetch(`${config.apiUrl}/users/${user.id}`, requestOptions).then(handleResponse);;
}

// prefixed function name with underscore because delete is a reserved word in javascript
function _delete(id) {
    const requestOptions = {
        method: 'DELETE',
        headers: authHeader()
    };

    return fetch(`${config.apiUrl}/users/${id}`, requestOptions).then(handleResponse);
}

function handleResponse(response) {
    // console.log(response)
    // return response.text().then(text => {
    //     const data = text && JSON.parse(text);
    //     if (!response.ok) {
    //         if (response.status === 401) {
    //             // auto logout if 401 response returned from api
    //             logout();
    //             location.reload(true);
    //         }
    //         const error = (data && data.message) || response.statusText;
    //         console.log(`Error in user.service: ${error}`)
    //         return Promise.reject(error);
    //     }

    //     return data;
    // });
    console.log('user.service1')
    console.log(response)
    if (response.status === 400) {
            console.log('user.service')
            console.log(resposne)
            return Promise.reject(response.data.detail);
    } else if (response.status === 200) {
        return response
    } else {
        return Promise.reject(response);
    }
}