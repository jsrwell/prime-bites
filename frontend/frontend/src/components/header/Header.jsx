import React, { useState, useEffect } from "react";
import "./Header.css";

const Header = () => {
  const [headerOpacity, setHeaderOpacity] = useState(100);

  useEffect(() => {
    const handleScroll = () => {
      const scrollPosition = window.scrollY;
      const maxScroll =
        window.document.documentElement.scrollHeight - window.innerHeight;
      const opacity = 0.6 - scrollPosition / maxScroll;

      setHeaderOpacity(opacity > 0 ? opacity : 0);
    };

    window.addEventListener("scroll", handleScroll);
    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  return (
    <header
      className={""}
      style={{ backgroundColor: `rgba(222, 26, 26, ${headerOpacity})` }}
    >
      <div
        className="flex items-center my-5"
        style={{
          color: headerOpacity === 0 ? "#000000" : "#FFFFFC",
          transition: "color 0.3s ease in out",
        }}
      >
        <div className="flex-grow text-center w-full" id="header-title">
          Prime Bites
        </div>
        <div className="relative right-10 hover:text-m-gray" id="header-items">
          <button type="button">Menu</button>
        </div>
      </div>
    </header>
  );
};

export default Header;
