import config from "../config";

const URL_USERS = `${config.URL}users/`;

const createUsers = (newUser) => {
    let response = fetch(`${URL_USERS}register/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(newUser)
    })
    let data = response.json()
    return data
}


export default createUsers;
