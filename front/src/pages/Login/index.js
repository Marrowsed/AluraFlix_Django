import React, { useEffect, useState } from 'react'
import LoginPage from '../../components/LoginPage'
import Logo from '../../assets/img/Logo.png'
import Button from '../../components/Button'
import FormField from '../../components/FormField'
import config from '../../config'
import { Link } from 'react-router-dom'

const Login = () => {
    const [token, setToken] = useState()
    const [user, setUser] = useState()
    const [password, setPassword] = useState()
    
    let handleSubmit = (e) => {
      e.preventDefault()
      setToken(config.generateToken(user, password))
      token ? setUser('') && setPassword('') && window.location.replace('/'): console.log('User not found')
    }
    return (
      <LoginPage>
        <div id='wrapper'>
          <img className="login-logo" src={Logo} alt="AluraFlix logo" />
          {token &&
                <>
                    <h2>Welcome back, {user} !</h2>
                    <Link to="/">Enter</Link>
                </>
          }
          {!token &&
          <>
            <form onSubmit={handleSubmit}>
            <FormField
              label={'Username'}
              type={'text'}
              name={'user'}
              value={user}
              onChange={e => setUser(e.target.value)}
              /> 
              <FormField
              label={'Password'}
              type={'password'}
              name={'pass'}
              value={password}
              onChange={e => setPassword(e.target.value)}
              /> 
            <Button type="submit" id='btn-submit'>
              Log In
            </Button>
            </form>
            <h2>Doesn't have an account ? <Link to="/signin">Sign In  </Link></h2>
          </>
          }
        </div>
      </LoginPage>
      
    )
  }

export default Login