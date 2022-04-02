import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import SignInPage from './pages/SignInPage';
import RegistrationPage from './pages/RegistrationPage';
import HomePage from  './pages/HomePage';
// import Home from './pages/home/Home';

  
  // ========================================
  
  ReactDOM.render(
    <BrowserRouter>
       <Routes>
        <Route exact path="/" element={<HomePage/>} />
        <Route path="/signin" element={<SignInPage/>} />
        <Route path="/register" element={<RegistrationPage/>} />
      </Routes>
      </BrowserRouter>,
    document.getElementById('root')
  );
  