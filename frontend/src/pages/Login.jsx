import Header from '../components/Header';
import Footer from '../components/Footer';

import React, { useState } from "react";
import { FaEye, FaEyeSlash } from "react-icons/fa";

import { Link } from 'react-router-dom';


const Login = () => {
    const [showPassword, setShowPassword] = useState(false);
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [isChecked, setIsChecked] = useState(false);

    const handleSubmit = (event) => {
        event.preventDefault();
    
    };

    const handleShowPassword = () => {
        setShowPassword(!showPassword);
      
    };
  const handleCheckboxChange = (event) => {
    setIsChecked(event.target.checked);
  };
  const handleLoginClick = () => {};

    return (
        <div>
            <div>
            <Header/>
            </div>
            <div className="login h-full py-4 text-xl font-normal">
            <form className=" rounded-3xl justify-center content-center max-w-xs mx-auto  p-4 bg-white  " onSubmit={handleSubmit}>
                <h1 className="font-semibold text-3xl text-center justify-center text-black ">WELCOME</h1><br/>
                <label htmlFor="email">Email</label><br></br>
      <input
        type="email"
        className="border w-full rounded-xl bg-gray-200"
        id="email"
        value={email}
        onChange={(event) => setEmail(event.target.value)}
        required
      /><br/>

      <label htmlFor="password">Password</label>
      <div className=" flex relative">
        <input
          className="border w-full rounded-xl bg-gray-200"
          type={showPassword ? "text" : "password"}
          id="password"
          value={password}
          onChange={(event) => setPassword(event.target.value)}
          required
        />
         <span
          className="password-icon absolute top-1 right-2 "
          onClick={handleShowPassword}
          aria-label="Toggle password visibility">
          {showPassword ?<FaEye />: <FaEyeSlash />}
        </span>
       
      </div>
      <a href="#" className="underline text-sm">Forget password?</a><br/>
    
        <input
         type="checkbox" 
         id="terms-and-conditions"
         checked={isChecked}
         onChange={handleCheckboxChange} />
         <label for="terms" className=" text-xs"> I agree to Terms and contitions</label><br/><br/>
         <div className="border w-28 mx-auto">
         <Link to="/Umubyeyidash" >  <button 
            disabled={!isChecked} 
            onClick={handleLoginClick} 
            className="bg-green-800 border-2 rounded-3xl content-center px-4 w-28">
                Login
            </button></Link>
        </div>
        </form>
            </div>
            <div>
            <Footer/>
            </div>
        </div>
    )
}

export default Login
