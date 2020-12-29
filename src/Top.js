import React from 'react';
import "./Top.css";
import MenuBookIcon from '@material-ui/icons/MenuBook';

function Top() {
    return (
        <div className="top">
            <div className="img">
                <div className="top_left">
                    <p>Home</p>
                    <p>Stories</p>
                    <p>Blog</p>
                </div>

                <div className="top_center">
                    <MenuBookIcon />
                    <h2>Kings Stories & Series</h2>
                    <p>Because Everybody Love Reading Stories</p>
                </div>

                <div className="top_right">
                    <p>Info</p>
                    <p>Contact Us</p>
                    <p>Sitemap</p>
                </div>

                <div className="top_info">
                    <p>-The best stories on the web-</p>
                    <p>Read or link to over 1000 stories listed under Stories to the left.</p>
                    <p>Submit your short stories for review as a Word document attached to an</p>
                    <p>email to: Read@Short-Story.Me</p>
                </div>
            </div>
        </div>
    )
}

export default Top
