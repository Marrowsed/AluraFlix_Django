import React, { useEffect, useState } from 'react'
import VideoPage from '../../components/VideoPage'
import config from '../../config'
import FormField from '../../components/VideoPage/FormField'
import Carousel from '../../components/VideoPage/Carousel'

const Videos = () => {

  const [token, setToken] = useState(localStorage.getItem("token"))
  const [videos, setVideos] = useState([])
  const [search, setSearch] = useState('')
  const [suggestions, setSuggestions] = useState([])
  
  useEffect(() => {
    getAllQueryVideos()
  }, [search])

  let validateToken = async () => {
    let data = await config.validateToken(localStorage.getItem("token"))
    if(data.code === "token_not_valid") setToken(await config.refreshToken(localStorage.getItem("refresh"))) && window.location.reload(true)
  }

   let getAllQueryVideos = async (page=1, videos=[]) => {
    validateToken()
    if (search) {
      let response = await fetch(`${config.URL}videos/?search=${search}&page=${page}`,{
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
      }
      })
      let data = await response.json()
      let results = data.results
      videos = results.concat(videos)
      if (data.next !== null) {
        page++
        getAllQueryVideos(page, videos)
      }
      setSuggestions(videos)
      return setVideos(videos)
    } else {
      setVideos([])
    }}

  return (
   <VideoPage>
    <FormField
      label={"Search for videos"}
      type={"input"}
      name={"search"}
      value={search}
      onChange={e => setSearch(e.target.value)}
      suggestions={suggestions}
    />
    {search.length === 0 && (<h1>Search for an awesome video !</h1>)}
      {videos && 
        (
           <Carousel
            data={videos}
            />   
        )
      }
   </VideoPage>
  )
}

export default Videos