import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
//import './App.css';
import Home from './pages/Home'
import Videos from './pages/Videos'
import Categories from './pages/Categories'
import RegisterVideos from './pages/Register/Videos';
import RegisterCategories from './pages/Register/Categories';
import Login from './pages/Login';
import { useState } from 'react';
import Signin from './pages/Signin';

function App() {
  const [token, setToken] = useState()
  let getToken = () => {
    setToken(localStorage.getItem("token"))
  }
  const ProtectedRoute = ({children }) => {
    if (!token) {
      return <Navigate to="/login" replace />;
    }
    return children;
  };

  const InitialRoute = ({children }) => {
    getToken()
    if (token) {
      return <Navigate to="/" replace />;
    }
    return children;
  };
  const Page404 = () => (<div><h1>Page Not Found !</h1></div>)
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path='/' 
          element={
          <ProtectedRoute>
            <Home />
          </ProtectedRoute>} exact/>
          <Route path='/login' element={
            <InitialRoute>
              <Login />
            </InitialRoute>
          } />
          <Route path='/signin' element={
            <InitialRoute>
              <Signin/>
            </InitialRoute>
          } />
          <Route path='/videos' 
          element={
          <ProtectedRoute>
            <Videos/>
          </ProtectedRoute>} />
          <Route path='/categories' 
          element={
          <ProtectedRoute>
            <Categories/>
          </ProtectedRoute>}/>
          <Route path='/register/videos' 
          element={
          <ProtectedRoute>
            <RegisterVideos/>
          </ProtectedRoute>} />
          <Route path='/register/categories' 
          element={
          <ProtectedRoute>
            <RegisterCategories/>
          </ProtectedRoute>} />
          <Route path="*" element={<Page404/>}/>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
