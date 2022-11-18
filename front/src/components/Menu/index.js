import React from 'react'
import { Link } from 'react-router-dom'
import Logo from '../../assets/img/Logo.png'
import './Menu.css'
import Button from '../Button'

const Menu = () => {
  let signOut = () => {
    localStorage.setItem('token', '')
  }
  return (
    <nav className="Menu">
      <Link to="/">
        <img className="Logo" src={Logo} alt="AluraFlix logo" />
      </Link>
      <Button as={Link} className="ButtonLink" to="/videos">
        Videos
      </Button>
      <Button as={Link} className="ButtonLink" to="/categories">
        Categories
      </Button>
      <Button as={Link} className="ButtonLink" to="/register/videos">
        New Video
      </Button>
      <Button as={Link} className="ButtonLink" to="/login" style={{color: 'red'}} onClick={signOut}>
        Sign Out
      </Button>
    </nav>
  );
}

export default Menu;