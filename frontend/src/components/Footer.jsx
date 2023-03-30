import React from 'react'
import { FaFacebook, FaInstagram, FaTwitter } from 'react-icons/fa';
const Footer = () => {
  return (
    <div>
      <footer className='flex justify-around p-10 footer'>
        <div>
            <h3 className='text-3xl'>Quick links</h3>
            <ul className='text-xl '>
                <li className=' social '>Home</li>
                <li className=' social'>About Us</li>
                <li className=' social'>Contact Us</li>
            </ul>
        </div>
        <div>
        <h3 className='text-3xl'>Services</h3>
            <ul className='text-xl '>
                <li className=' social'>Termes & Condition</li>
                <li className=' social'>Privacy Policy</li>
                <li className=' social'>Help</li>
            </ul>
        </div>
        <div>
        <h3  className='text-3xl'>Social Media</h3>
            <ul className='text-xl '>
                <li className=' social '><FaInstagram className='icons' />Instagram</li>
                <li className=' social'><FaTwitter className='icons' />Twitter</li>
                <li className=' social'><FaFacebook className='icons' />FaceBook</li>
            </ul>
        </div>
        <div>
        <h3 className='text-3xl'>Contacts</h3>
            <ul className='text-xl '>
                <li className=' social'>Tel: 078800000</li>
                <li className=' social'>Email: group@gmail.com</li>
            </ul>
        </div>
      </footer>
    </div>
  )
}

export default Footer
