import React from 'react';
import { Link } from 'react-router-dom';

const Sidebar = () => {
  const menuItems = [
    { name: 'Home', path: '/' },
    { name: 'About', path: '/about' },
    { name: 'Contact', path: '/contact' },
    { name: 'Services', path: '/services' },
  ];

  const replaceNFT = (text) => {
    return text.replace(/NFT/g, 'Independent Game');
  };

  return (
    <div className="sidebar">
      <ul>
        {menuItems.map((item, index) => (
          <li key={index}>
            <Link to={item.path}>{replaceNFT(item.name)}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Sidebar;