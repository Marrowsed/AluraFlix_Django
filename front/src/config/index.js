const URL = "http://127.0.0.1:8000/api/"

const generateToken = async (user, pass) => {
    let response = await fetch(`${URL}token/`,
     { 
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "username": user,
            "password": pass
        })
    })
    let data = await response.json()
    localStorage.setItem("token", data.access)
    localStorage.setItem("refresh", data.refresh)
    return await data.access
}

const refreshToken = async () => {
    let response = await fetch(`${URL}token/refresh/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "refresh": `${localStorage.getItem("refresh")}`
        })
    })
    let data = await response.json()
    localStorage.setItem("refresh", data.refresh)
    localStorage.setItem("token", data.access)
    data.detail !== "Token is invalid or expired" ? console.log("Refreshed") : console.log("Couldn't refresh")
    return await data.access
}

const validateToken = async (token)  => {
    let response = await fetch(`${URL}validate/`,
     { 
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    })
    let data = await response.json()
    response.status === 200 ? console.log("Valid Token") : console.log("Invalid Token, refresh it")
    return await data
}



export default {
    URL,
    generateToken,
    validateToken,
    refreshToken
}