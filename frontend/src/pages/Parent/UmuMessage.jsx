import React from 'react'
import { FaBell, FaCalendar, FaRocketchat, FaUserAlt } from 'react-icons/fa';
import { Link } from 'react-router-dom'
import Header from '../../components/Header'
import Footer from '../../components/Footer'
import prof from '../../img/profile.png'

const UmuMessage = () => {
    return (
        <div>
            <Header />
            <body className='flex gap-3 bg-white'>
                <aside className='w-1/5 mx-20 mb-8 umubyeyidash mt-4 rounded-3xl'>
                    <div className='flex justify-center '><img src={prof} alt='profile' className='w-12 h-12 rounded-full' />
                    </div>
                    <content className="">
                        <p className='justify-center font-bold text-lg flex'>UMUBYEYI Mother</p>
                        <p className='text-md  justify-center flex'>groupe7@gmail.com</p>
                        <span className='gap-2 pt-4 flex justify-center font-bold text-green-600 '><FaRocketchat /> Messages </span>
                        <p className='gap-2 flex justify-center font-bold pt-8'><FaBell /> Notification</p>
                        <Link to="/UmuSchedule"><p className='gap-2 flex justify-center font-bold pt-8'><FaCalendar />Schedule </p></Link>
                        <p className='gap-2 flex justify-center font-bold pt-8'><FaUserAlt /> Semester </p>
                         <Link to="#" className='gap-2 flex justify-center font-bold pt-8 pb-12 underline'>LogOut</Link>
                    </content>
                </aside>
                <div className='flex  w-screen justify-center'>
                    <p className='text-3xl underline font-bold pt-4'>New Messages</p>
                </div>

            </body>
            <Footer />
        </div>
    )
}

export default UmuMessage
