import React, { useEffect, useState } from 'react'
import config from '../../config'
import CategoriesPage from '../../components/CategoriesPage'
import categoriesRepo from '../../repositories/categories.js'
import Carousel from '../../components/CategoriesPage/Carousel'
import Button from '../../components/Button'
import { Link } from 'react-router-dom'

const Categories = () => {
  const [token, setToken] = useState(localStorage.getItem("token"))
  const [playlist, setPlaylist] = useState([])

  useEffect(() => {
    getPlaylist()
  }, [])

  let validateToken = async () => {
    let data = await config.validateToken(token)
    if(data.code === "token_not_valid") setToken(await config.refreshToken(localStorage.getItem("refresh"))) && window.location.reload(true)
  }

  let getPlaylist = async () => {
    validateToken()
    let data = await categoriesRepo.getPlaylist(localStorage.getItem('token'))
    setPlaylist(data)
  }

  return (
    <CategoriesPage>
    <h1>Categories</h1>
    <h2>Want to help with more Categories ? <Button as={Link} className="ButtonLink" to="/register/categories">
        New Category
      </Button></h2>
    {playlist.map(p => (
      <Carousel
      data={p}
      />
    )
    )}

    </CategoriesPage>
    
  )
}

export default Categories