import React from 'react';
import './Footer.css';

const Footer = () => {
    let footerText = "All rights reserved. NFT 2022";
    footerText = footerText.replace("NFT", "Independent Game");

    return (
        <footer className="footer">
            <p>{footerText}</p>
        </footer>
    );
}

export default Footer;