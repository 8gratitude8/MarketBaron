import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  const navItems = ['Home', 'About', 'Contact', 'Services'];

  const replaceNFT = (text) => {
    return text.replace(/NFT/g, 'Independent Game');
  };

  return (
    <nav>
      <ul>
        {navItems.map((item, index) => (
          <li key={index}>
            <Link to={`/${item.toLowerCase()}`}>{replaceNFT(item)}</Link>
          </li>
        ))}
      </ul>
    </nav>
  );
};

export default Navbar;