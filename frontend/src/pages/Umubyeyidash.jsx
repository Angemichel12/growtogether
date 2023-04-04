import React from 'react'
import Header from '../components/Header'
import Footer from '../components/Footer'
import im1 from '../img/welcome1.png'
import im2 from '../img/welcome2.png'
import im3 from '../img/welcome3.png'
import im4 from '../img/welcome4.png'
import prof from '../img/profile.png'
import { FaRocketchat} from 'react-icons/fa';

const Umubyeyidash = () => {
    return (
        <div>
            <Header />
            <body className='flex gap-3 umubyeyi'>
                <aside className='w-2/6  mx-20 mb-8 umubyeyidash mt-4 rounded-3xl'>
                    <div className='flex justify-center '><img src={prof} alt='profile' className='w-12 h-12 rounded-full' />
                    </div>
                    <p className='text-center font-bold text-lg'>UMUBYEYI Mother</p>
                    <p className='text-center text-md'>groupe7@gmail.com</p>
                    <span className='gap-2 pt-4 flex justify-center font-bold'><FaRocketchat /> Messages </span>
                </aside>
                <div className='gird grid-cols-2 text-white'>
                    <div className='flex gap-52 justify-center pt-12'>
                        <div ><img src={im1} alt='image1' />
                            <p className='text-lg text-center font-bold'>Pregnance Service</p></div>
                        <div ><img src={im3} alt='image1' />
                            <p className='text-lg text-center font-bold'>Pediatric Service</p></div>
                    </div>

                    <div className='flex gap-52 justify-center pt-12 pb-9'>
                        <div ><img src={im2} alt='image1' />
                            <p className='text-lg text-center font-bold'>Health Adivisor</p></div>
                        <div ><img src={im4} alt='image1' />
                            <p className='text-lg text-center font-bold'>Other Services</p></div>
                    </div>
                </div>

            </body>
            <Footer />
        </div>
    )
}

export default Umubyeyidash
