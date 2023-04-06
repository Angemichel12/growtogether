import React from 'react'
import DoctorNav from '../components/DoctorNav'
import TypeWriterEffect from 'react-typewriter-effect';
const HealthHome = () => {
    return (
        <div>
            <div >
                <DoctorNav />
                <div className='healthbg'>
                    <span className='flex justify-center pt-60 '>

                        <TypeWriterEffect
                            textStyle={{
                                color: 'white',
                                fontWeight: 700,
                                fontSize: '8rem',
                            }}
                            cursorColor="gray"
                            cursorSize="0.1px"
                            multiText={['GROW2GETHER']}
                            typeSpeed={300}
                            multiTextDelay={1000}
                            multiTextLoop
                        />
                    </span>
                </div>
            </div>
        </div>
    )
}

export default HealthHome