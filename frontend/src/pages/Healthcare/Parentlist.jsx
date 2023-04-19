import React from 'react'
import DoctorNav from '../../components/DoctorNav'
const Parentlist = () => {
    return (
        <div>
            <DoctorNav />
            <body className=''>
                <div className="flex justify-center pt-8 h-screen healthbg">
                    <content className="flex  flex-col items-center bg-white h-auto w-11/12 mb-8 p-12">
                        <p className='text-4xl mb-16 font-bold py-4 underline'>Parent List</p>

                    </content>
                </div>
            </body>
        </div>
    )
}

export default Parentlist