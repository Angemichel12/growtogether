import React from 'react'
import { Link } from 'react-router-dom'

const DoctorNav = () => {
  return (
    <div>
      <nav>
        <ul className='doctornav'>
        <Link to="/Parentlist"><li>Parent List</li> </Link>
          <Link to="/HealthRegist">
          <li>Registering Parent</li></Link>
          <Link to="/Message"><li>Messages</li></Link>
          <Link to="/Appointmentlist"><li>Appointment list</li></Link>
          <li>Schedule</li>
        </ul>
      </nav>
    </div>
  )
}

export default DoctorNav
