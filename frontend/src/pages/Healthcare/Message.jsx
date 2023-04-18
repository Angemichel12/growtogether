import React from 'react'
import DoctorNav from '../../components/DoctorNav'
import prof from '../../img/profile.png'
const Message = () => {
    return (
        <div>
            <DoctorNav />
            <body className=''>
                <div className="flex justify-center pt-8 h-screen healthbg">
                    <content className="flex  bg-white h-auto w-11/12 mb-8 p-12">
                        <aside className='w-4/12'>
                            <div className='bg-gray-300 m-4 rounded-lg flex gap-4'>
                                <img src={prof} alt='profile' className='rounded-full w-20 h-20 p-4' />
                                <content className='pt-4 pb-6'>
                                    <h1 className='text-xl font-bold'>Parent 1</h1>
                                    <p className='text-lg pt-2'>Good Evening Doctor</p>
                                    <p className='pt-2'>I am 14 weeks pregnent </p>
                                </content>
                            </div>

                            <div className='bg-gray-300 m-4 rounded-lg flex gap-4'>
                                <img src={prof} alt='profile' className='rounded-full w-20 h-20 p-4' />
                                <content className='pt-4 pb-6'>
                                    <h1 className='text-xl font-bold'>Parent 2</h1>
                                    <p className='text-lg pt-2'>Good Evening Doctor</p>
                                    <p className='pt-2'>I am 14 weeks pregnent </p>
                                </content>
                            </div>
                        </aside>
                        <content></content>
                    </content>
                </div>
            </body>
        </div>
    )
}

export default Message