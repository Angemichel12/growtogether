import React from 'react'
import Header from '../components/Header';
import Footer from '../components/Footer';

const Login = () => {
    return (
        <div>
            <div>
            <Header/>
            </div>
            <div className="login h-full py-12">
            <form className=" rounded-md justify-center content-center mx-60 w-48 p-8 ">
                <h1>WELCOME</h1><br/>
                <label>UserName</label><br/>
                <input type="text" required className="rounded-md w-32"/><br/>
                <label>Password</label><br/>
                <input type="password" required  className=" rounded-md w-32"/><br/>

                <button className="bg-green-900 rounded-md">Login</button>
            </form>
            </div>
            <div>
            <Footer/>
            </div>
        </div>
    )
}

export default Login
