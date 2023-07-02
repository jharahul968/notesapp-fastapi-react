import React from 'react'

const Layout = (props) => {
  return (
    <div className='container dark'>
        <div className='app'>
            <Header/>
            {props.children}
        </div>
    </div>
  )
}

export default Layout