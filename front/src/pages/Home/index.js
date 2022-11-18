import React, {useState, useEffect} from 'react'
import config from '../../config'
import categoriesRepo from '../../repositories/categories.js'
import HomePage from '../../components/HomePage'
import Banner from '../../components/HomePage/Banner'
import Carousel from '../../components/HomePage/Carousel'

const Home = () => {
  const [token, setToken] = useState(localStorage.getItem("token"))
  const [initialData, setInitialData] = useState([])
  useEffect( () => {
    token ?
    validateToken()
    : window.location.reload(true)
  }, [token])

  useEffect(() => {
    initialData.length === 0 ?
    getVideos()
    : console.log("Playlist Loaded")
  }, [initialData])

  let validateToken = async () => {
    let data = await config.validateToken(localStorage.getItem("token"))
    data.code === "token_not_valid" ? setToken(await config.refreshToken(localStorage.getItem("refresh"))) && window.location.reload(true) : console.log("Valid Token")
  }

  let getVideos = async () => {
    validateToken()
    let data = await categoriesRepo.getPlaylist(localStorage.getItem('token'))
    setInitialData(data)
  }

  return (
    <>
    <HomePage paddingAll={0}>
      {initialData.length === 0 && (<div>Loading...</div>)}
      {initialData.map((v, index) => {
        if (index === 0) {
          return (
            <div key={v.id}>
              <Banner
                videoTitle={initialData[0].videos[0].title}
                url={initialData[0].videos[0].url}
                videoDescription={initialData[0].videos[0].description}
              />
              <Carousel
                ignoreFirstVideo
                data={v}
              />
            </div>
          );
        } 
        return (
          <Carousel
            data={v}
          />
        )  
      })}
    </HomePage>
    </>
  )
}

export default Home