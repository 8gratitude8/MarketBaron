import React from 'react';
import './Header.css';

const Header = () => {
  const siteTitle = "NFT Marketplace";
  const newTitle = siteTitle.replace("NFT", "Independent Game");

  return (
    <header className="header">
      <h1>{newTitle}</h1>
    </header>
  );
};

export default Header;