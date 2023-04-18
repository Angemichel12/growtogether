import Header from '../../components/Header';
import Footer from '../../components/Footer';

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
  const handleLoginClick = () => { };

  return (
    <div>
      <div>
        <Header />
      </div>
      <div className="login h-full py-4 text-xl font-normal">
        <form className=" rounded-3xl flex flex-col justify-center items-center  mx-auto h-5/6 p-4 bg-white w-4/12 " onSubmit={handleSubmit}>
          <h1 className="font-semibold text-3xl text-center justify-center text-black mb-4">WELCOME</h1>
          <label htmlFor="email">Email</label>
          <input
            type="email"
            className="border w-fit p-1 rounded-xl bg-gray-200"
            id="email"
            value={email}
            onChange={(event) => setEmail(event.target.value)}
            required
          /><br />

          <label htmlFor="password">Password</label>
          <div className=" flex relative">
            <input
              className="border w-fit p-1 rounded-xl bg-gray-200"
              type={showPassword ? "text" : "password"}
              id="password"
              value={password}
              onChange={(event) => setPassword(event.target.value)}
              required
            />
            <span
              className="password-icon absolute top-2 right-2 "
              onClick={handleShowPassword}
              aria-label="Toggle password visibility">
              {showPassword ? <FaEye /> : <FaEyeSlash />}
            </span>

          </div>
          <Link to="#" className="underline text-sm mt-4">Forget password?</Link><br />

          <div className='mb-8' >
            <input
              type="checkbox"
              id="terms-and-conditions"
              checked={isChecked}
              onChange={handleCheckboxChange} />
            <label for="terms" className=" text-xs "> I agree to Terms and contitions</label>
          </div>
          <div className=" mx-auto">
            <Link to="/Umubyeyidash" >  <button
              disabled={!isChecked}
              onClick={handleLoginClick}
              className="bg-green-800 rounded-3xl content-center px-4 w-28 text-white p-2">
              Login
            </button></Link>
          </div>
        </form>
      </div>
      <div>
        <Footer />
      </div>
    </div>
  )
}

export default Login
