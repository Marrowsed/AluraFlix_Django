import config from '../config';

const URL_CATEGORIES = `${config.URL}categories/`;
const URL_PLAYLIST = `${config.URL}playlist/`;

const getAllCategories = async (token, page) => {
    return fetch(`${URL_CATEGORIES}?page=${page}`,
    {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    })
    .then(async (response) => {
        if(response.ok) {
            let data = await response.json()
            return data
        }})
    .catch((e) => {
        console.log("ERROR", e)
    })
    
}

const postCategories = async (token, newCategory) => {
    return fetch(`${URL_CATEGORIES}`,
    {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(newCategory)
    })
    .then(async (response) => {
        if(response.ok) {
            let res = await response.json()
            console.log('Category Posted !')
            return res
        }
    })
    .catch((e) => {
        console.log("ERROR", e)
    })
}

const getCategoriesId = async (token, id) => {
    let response = await fetch(`${URL_CATEGORIES}/${id}/`,
    {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    })
    let data = await response.json()
    return data.results
}

const getVideoByCategoryId = async (token, id) => {
    let response = await fetch(`${URL_CATEGORIES}/${id}/videos/`,
    {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    })
    let data = await response.json()
    return data.results
}
  
const getPlaylist = async (token) => {
    let response = await fetch(`${URL_PLAYLIST}`,
        {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            }
        })
    let data = await response.json()
    return data
  }

export default {
  getPlaylist,
  getCategoriesId,
  getVideoByCategoryId,
  getAllCategories,
  postCategories
};
