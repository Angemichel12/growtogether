import React from 'react'
import Header from './Header'
import Body from './Body'
import Footer from './Footer'
function Home() {
  return (
    <div className='flex flex-col flex-wrap text-gray-700 '>
      <Header />
      <Body />
      <Footer />
    </div>
  )
}

export default Home
