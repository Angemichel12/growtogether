import React from 'react'
import DoctorNav from '../components/DoctorNav'
import { Link } from 'react-router-dom'

const HealthRegist = () => {
  return (
    <div>
      <DoctorNav />
      <body className=''>
        <div className="flex justify-center bg-black pt-8 h-screen">
        <content className="flex  flex-col items-center bg-white healthlog rounded-3xl h-4/5 p-8">
            <p className='text-4xl mb-16 font-bold py-4'>REGISTER A PARENT</p>
            <form className=''>
                <label className='font-bold text-lg'>Names</label>
                <input type='text' className='border-black border p-2  mb-4 mx-16'></input><br/>
                <label className='font-bold text-lg'>Birth Year</label>
                <input type='text' className='border-black border p-2  mb-4 mx-10'></input><br/>
                <label className='font-bold text-lg'>Email</label>
                <input type='text' className='border-black border p-2 mb-4 mx-20'></input><br/>
                <label className='font-bold text-lg'>Telephone</label>
                <input type='text' className='border-black border p-2 w-52 mb-4 font-bold mx-10 mr-4'></input><br/>
                <Link to=""><button className='healbtn my-12 mx-24 rounded-md text-lg border border-black text-white px-5 py-2 '>Register</button></Link> 
            </form>
        </content>
        </div>
      </body>
    </div>
  )
}

export default HealthRegist
