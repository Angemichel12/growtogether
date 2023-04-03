import React from 'react'
import bgim from '../img/welcome.png'
import im1 from '../img/welcome1.png'
import im2 from '../img/welcome2.png'
import im3 from '../img/welcome3.png'
import im4 from '../img/welcome4.png'
import{Link} from 'react-router-dom'
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
                <content className='flex justify-center flex-col pt-32'>
                    <p className='text-center text-2xl'>Welcome to our <span className='font-bold'>GROW TOGETHER</span> team !!</p>
                    <p className='text-center pt-8 text-2xl'>You Will Meet Health Professionals Who Will Help You</p>
                </content>
                <div className='flex justify-center'>
                    <button className='btn '>Learn More</button>
                </div>

                <div className='flex justify-end font-bold  text-3xl'>
                   <Link to="/login"> <button className='btn2 px-8 py-0 mt-4 mr-2 flex gap-4 rounded-3xl text-white'>Continue
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-12 h-12">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                        </svg>

                    </button></Link>
                </div>
            </body>
            <div className='bg-white p-8'>
                <p className='text-center p-8 text-4xl font-bold pb-28'>What We Offer</p>
                <section className='flex justify-around mb-20 gap-4'>
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
