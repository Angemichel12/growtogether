import React from 'react'
import Header from '../../components/Header'
import { FaEnvelope, FaPhone, } from 'react-icons/fa'

const Contactus = () => {
  return (
    <div>
      <Header />
      <body className='flex justify-center'>
        <div className='w-1/2  flex h-auto mt-16 bg-gray-300 py-8 px-16'>
            <aside className='w-1/2 flex flex-col gap-8'>
                <h1 className='text-2xl flex justify-center'>Leave us a Message</h1>
                <p className='flex text-center mr-8 text-lg'>Fill out this form we will reach out to you within 24 hours</p>
                <p className='flex gap-8 ml-10 mt-6'> <FaPhone /> +250788999999</p>
                <p className='flex gap-8 ml-10'> <FaEnvelope /> group7@gmail.com</p>
            </aside>
            <div className='w-1/2 bg-white h-auto border border-black'>
                <form className='py-12 px-8 flex flex-col gap-1'>
                    <label>Your Name</label>
                    <input type='text' className='bg-gray-300 h-8' />
                    <label className='mt-8'>Email</label>
                    <input type='text' className='bg-gray-300 h-8' />
                    <label className='mt-8'>Your Message</label>
                    <textarea className='bg-gray-300 h-1/4'></textarea>
                    <button className='mt-4 text-white content-end mx-20 bg-green-700 p-1 rounded-3xl'>Send Message</button>
                </form>
            </div>
        </div>
      </body>
    </div>
  )
}

export default Contactus
