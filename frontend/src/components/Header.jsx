import React from 'react'
import { Link} from 'react-router-dom'
function Header() {
    return (
        <div>
            <nav className=''>
                <div className='flex justify-between p-8 bg'>
                    <aside className='pr-3'>
                        <ul>
                        <Link to="/"> <li className='text-xl'>Home</li></Link>
                        </ul>
                    </aside>
                    <ul className='flex gap-12'>
                        <li className='text-xl'>About us</li>
                        <li className='text-xl'>Contact Us</li>
                        <li><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" className="w-6 h-6 text-xl">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M17.982 18.725A7.488 7.488 0 0012 15.75a7.488 7.488 0 00-5.982 2.975m11.963 0a9 9 0 10-11.963 0m11.963 0A8.966 8.966 0 0112 21a8.966 8.966 0 01-5.982-2.275M15 9.75a3 3 0 11-6 0 3 3 0 016 0z" />
                        </svg>
                        </li>
                    </ul>
                </div>
            </nav>
        </div>
    )
}

export default Header
