import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import RegisterPage from '../../../components/RegisterPage';
import useForm from '../../../hooks/useForm';
import FormField from '../../../components/FormField';
import Button from '../../../components/Button';
import categoriesRepo from '../../../repositories/categories';
import config from '../../../config';

const  RegisterCategories = () => {
  const { handleChange, values } = useForm({
    title: '',
    color: ''
  });
  const [token, setToken] = useState(localStorage.getItem('token'))

  useEffect(() => {
    validateToken()
  }, []);

  let validateToken = async () => {
    let data = await config.validateToken(localStorage.getItem("token"))
    if(data.code === "token_not_valid") setToken(await config.refreshToken(localStorage.getItem("refresh"))) && window.location.reload(true)
  }

  return (
    <RegisterPage>
      <h1>New Category</h1>

      <form onSubmit={(e) => {
        e.preventDefault();

        categoriesRepo.postCategories(token, {
            title: values.title,
            color: values.color
        })
        .then(() => {
          window.location.replace('/')
        })
        .catch((e) => {
          console.log("Error", e)
        })
      }}
      >
        <FormField
          label="Category Title"
          name="title"
          value={values.title}
          onChange={handleChange}
        />

        <FormField
        label="Category Color"
        name="color"
        value={values.color}
        onChange={handleChange}
        />

        <Button type="submit">
          Register
        </Button>
      </form>

      <br />
      <br />

      <Link to="/register/videos">
        New Video
      </Link>
      <br/>
      <hr/>
      <Link to="/">
        Back to Home
      </Link>
    </RegisterPage>
  );
}

export default RegisterCategories;
