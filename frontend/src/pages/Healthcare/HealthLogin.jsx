import React from 'react'
import DoctorNav from '../../components/DoctorNav'
import { Link } from 'react-router-dom'
const HealthLogin = () => {
  return (
    <div>
      <DoctorNav />
      <body className=''>
        <div className="healthbg flex justify-center  pt-8 h-screen">
        <content className="flex justify-center flex-col items-center bg-white healthlog rounded-3xl h-4/5">
            <p className='text-4xl mb-6 font-bold'>Welcome</p>
            <form className='flex flex-col '>
                <label className='font-bold text-lg'>Enter Your Employment Id</label>
                <input type='text' className='border-black border p-2 rounded-xl mb-4'></input>
                <label className='font-bold text-lg'>Password</label>
                <input type='text' className='border-black border p-2 rounded-xl mb-4 font-bold'></input>
                <span className='underline'>Forget Password? <span className='setone'>Set One</span></span>
                <Link to="/HealthHome"><button className='healbtn my-8 mx-16 rounded-2xl text-lg text-white px-5 py-2'>LOGIN</button></Link> 
                <p className='font-bold'>Don't have account? <span className='text-green-700 underline'>SIGN UP</span></p>
            </form>
        </content>
        </div>
      </body>
    </div>
  )
}

export default HealthLogin
