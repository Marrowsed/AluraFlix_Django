import config from '../config';

const URL_VIDEOS = `${config.URL}videos/`;

const postVideo = async (token, newVideo) => {
    return fetch(`${URL_VIDEOS}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(newVideo)
    })
    .then(async (response) => {
        if(response.ok) {
            let res = await response.json()
            console.log('Video Posted !')
            return res
        }
    })
    .catch((e) => {
        console.log("ERROR", e)
    })
}


export default {
    postVideo
};
