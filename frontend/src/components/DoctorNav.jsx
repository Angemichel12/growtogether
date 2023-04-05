import React from 'react'
import { Link } from 'react-router-dom'

const DoctorNav = () => {
  return (
    <div>
      <nav>
        <ul className='doctornav'>
            <li>Parent List</li>
            <Link to="/HealthRegist"> <li>Registering Parent</li></Link>
            <li>Messages</li>
            <li>Appointment list</li>
            <li>Schedule</li>
        </ul>
      </nav>
    </div>
  )
}

export default DoctorNav
