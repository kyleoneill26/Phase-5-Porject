import React from "react";
import { Link } from "react-router-dom";

function Header() {
  return (
    <header>
      <h1>Music Streaming App</h1>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/playlists">Playlists</Link>
          </li>
          <li>
            <Link to="/artists">Artists</Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;