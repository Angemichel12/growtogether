import React from 'react'
import bgim from '../img/welcome.png'
import im1 from '../img/welcome1.png'
import im2 from '../img/welcome2.png'
import im3 from '../img/welcome3.png'
import im4 from '../img/welcome4.png'
import { Link } from 'react-router-dom'
import { FaAngleRight} from 'react-icons/fa';
const Body = () => {
    return (
        <div className='bg-gray-300'>
            <body style={{
                backgroundImage: `url(${bgim})`,
                backgroundSize: 'cover',
                backgroundRepeat: 'no-repeat',
                backgroundPosition: 'center',
                opacity: ''
            }} className='h-screen opacity-95'>
                <content className='flex justify-center flex-col pt-36'>
                    <p className='text-center text-4xl text-gray-700'>Welcome to our <span className='font-bold'>GROW TOGETHER</span> team !!</p>
                    <p className='text-center pt-8 text-2xl text-gray-700'>You Will Meet Health Professionals Who Will Help You</p>
                </content>

                <div class="dropdown flex  justify-end lg:mr-32 md:mr-20 sm:mr16 lg:mt-64 sm:mt-52 md:mt-44">
                    <button className="dropbtn px-6 py-2 font-bold text-3xl  flex gap-2 rounded-3xl text-white shadow-xl shadow-black border-b border-white">Continue <FaAngleRight/> </button>
                    <div className="dropdown-content">
                        <Link to="/HealthLogin">As a Health Care</Link>
                        <Link to="/login">As a Parent</Link>
                    </div>
                </div>

            </body>
            <div className='bg-white pb-1'>
                <p className='text-center p-8 text-4xl font-bold pb-32'>What We Offer</p>
                <section className='flex justify-around mb-20 flex-wrap'>
                    <div ><img src={im1} alt='image1' />
                        <p className='text-sm font-bold'>We provide consultancy on pregnant women</p></div>
                    <div ><img src={im2} alt='image1' />
                        <p className='text-sm text-center font-bold'>Contact with health professionals</p></div>
                    <div ><img src={im3} alt='image1' />
                        <p className='text-sm text-center font-bold'>Pediatric Consultion and advsing</p></div>
                    <div ><img src={im4} alt='image1' /></div>
                </section>
            </div>
        </div>
    )
}

export default Body
