import React from 'react'
import SigninPage from '../../components/SigninPage'
import Logo from '../../assets/img/Logo.png'
import Button from '../../components/Button'
import FormField from '../../components/FormField'
import { Link, Navigate, redirect } from 'react-router-dom'
import useForm from '../../hooks/useForm'
import userRepo from '../../repositories/users'

const Signin = () => {
  const {handleChange, values } = useForm({
    username: '',
    password: '',
    email: '',
    first_name: '',
    last_name: '',
    is_active: true
  })

  let handleSubmit = (e) => {
    e.preventDefault()
    userRepo.createUsers({
      username: values.username,
      password: values.password,
      email: values.email,
      first_name: values.first_name,
      last_name: values.last_name,
      is_active: values.is_active
    })
    .then(() => {
      console.log('User created !')
      redirect('/login')
    })
    .catch((e) => {
      console.log(e.message)
    })
  }
  return (
    <SigninPage>
      <div id='wrapper'>
        <img className="login-logo" src={Logo} alt="AluraFlix logo" />
        <form onSubmit={handleSubmit}>
        <FormField
          label={'First Name'}
          type={'text'}
          name={'f_name'}
          value={values.first_name}
          onChange={handleChange}
          /> 
        <FormField
          label={'Last Name'}
          type={'text'}
          name={'l_name'}
          value={values.last_name}
          onChange={handleChange}
          />
        <FormField
          label={'Email'}
          type={'email'}
          name={'email'}
          value={values.email}
          onChange={handleChange}
          /> 
        <FormField
          label={'Username'}
          type={'text'}
          name={'user'}
          value={values.username}
          onChange={handleChange}
          /> 
          <FormField
          label={'Password'}
          type={'password'}
          name={'pass'}
          value={values.password}
          onChange={handleChange}
          /> 
        <Button type="submit" id='btn-submit'>
          Sign In
        </Button>
        </form>
        <h2>Have an account ? <Link to="/login">Log In !</Link></h2>
      </div>
    </SigninPage>
    
  )
}

export default Signin