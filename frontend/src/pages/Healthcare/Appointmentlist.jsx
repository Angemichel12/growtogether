import React from 'react'

const Appointmentlist = () => {
    return (
        <div>
            <div className="flex justify-center pt-8 h-screen healthbg">
                <content className="flex flex-col gap-8 bg-white h-auto w-11/12 mb-8 p-12">
                    <div className='w-full flex flex-col items-center justify-center'>
                        <h1 className='text-green-500 text-4xl font-bold '>Today</h1>
                        <content className='flex gap-32 mt-4'>
                            <h1 className='text-xl font-bold'>Reg Number</h1>
                            <h1 className='text-xl font-bold'>Full Name</h1>
                            <h1 className='text-xl font-bold'>Telphone</h1>
                            <h1 className='text-xl font-bold'>Email</h1>
                        </content>
                    </div>

                    <div className='w-full flex flex-col items-center justify-center mt-4'>
                        <h1 className='text-green-500 text-4xl font-bold '>Tomorrow</h1>
                        <content className='flex gap-32 mt-4'>
                            <h1 className='text-xl font-bold'>Reg Number</h1>
                            <h1 className='text-xl font-bold'>Full Name</h1>
                            <h1 className='text-xl font-bold'>Telphone</h1>
                            <h1 className='text-xl font-bold'>Email</h1>
                        </content>
                    </div>
                </content>
            </div>

        </div>
    )
}

export default Appointmentlist