import React from "react";
import "./Header.css";

const Header = () => {
  return (
    <nav className="fixed items-center">
      <div className="flex items-center my-5 ">
        <div className="flex-grow text-center w-full" id="nav-title">
          Prime Bites
        </div>
        <div className="relative right-10 hover:text-m-gray" id="nav-items">
          <button type="button">Menu</button>
        </div>
      </div>
    </nav>
  );
};

export default Header;
