import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import RegisterPage from '../../../components/RegisterPage';
import useForm from '../../../hooks/useForm';
import FormField from '../../../components/FormField';
import Button from '../../../components/Button';
import categoriesRepo from '../../../repositories/categories';
import videosRepo from '../../../repositories/videos';
import config from '../../../config';

const RegisterVideos = () => {
  const [categories, setCategories] = useState([]);
  const categoryTitles = categories.map(c => c.title);
  const { handleChange, values } = useForm({
    title: '',
    description: '',
    url: 'https://www.youtube.com/',
    category_name: '',
  });
  const [token, setToken] = useState(localStorage.getItem('token'))

  useEffect(() => {
    validateToken()
    getAllCategories(token)
  }, []);

  let getAllCategories = (token, page=1, final=[]) => {
    categoriesRepo
      .getAllCategories(token, page)
      .then((data) => {
        let results = data.results
        final = results.concat(final)
        if(data.next != null){
          page++
          getAllCategories(token, page, final)
        }
        setCategories(final.concat(categories))
      })
      .catch((e) => {
        console.log(e)
        })
      }
  console.log(categories)

  let validateToken = async () => {
    let data = await config.validateToken(localStorage.getItem("token"))
    if(data.code === "token_not_valid") setToken(await config.refreshToken(localStorage.getItem("refresh"))) && window.location.reload(true)
  }

  return (
    <RegisterPage>
      <h1>New Video</h1>


      <form onSubmit={(e) => {
        e.preventDefault();

        const chosenCategory = categories.find((c) => {
          return c.title === values.category_name;
        });


        videosRepo.postVideo(token, {
            title: values.title,
            description: values.description,
            url: values.url,
            category_name: chosenCategory.title,
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
          label="Video Title"
          name="title"
          value={values.title}
          onChange={handleChange}
        />

        <FormField
        label="Video Description"
        name="description"
        value={values.description}
        onChange={handleChange}
        />


        <FormField
          label="URL"
          name="url"
          value={values.url}
          onChange={handleChange}
        />

        <FormField
          label="Category"
          name="category_name"
          value={values.category_name}
          onChange={handleChange}
          suggestions={categoryTitles}
        />

        <Button type="submit">
          Register
        </Button>
      </form>

      <br />
      <br />

      <Link to="/register/categories">
        New Category
      </Link>
      <br/>
      <hr/>
      <Link to="/">
        Back to Home
      </Link>
    </RegisterPage>
  );
}

export default RegisterVideos;
