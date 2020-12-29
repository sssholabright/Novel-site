import React from 'react';
import "./Header.css";


function Header() {

    
    return (
        <div className="header">
            <div className="nav_search">
                <input className="search" 
                        type="text"
                        placeholder="Search this site...." />
                <input  className="search_button"
                        type="button"
                        value="GO!"     />
            </div>

            </div>
    )
}

export default Header 
