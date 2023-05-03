// import React, { useEffect, useState } from "react";
// import { Switch, Route } from "react-router-dom";
// import Home from "./Home";



// function App() {
//   const [songs, setSongs] = useState([])
//   const [artists, setArtists] = useState([])
//   const [albums, setAlbums] = useState([])
//   const [playlists, setPlaylists] = useState([])
//   const [users, setUsers] = useState([])
  


  

//   useEffect(() => {
//     fetch('/songs')
//       .then((r) => r.json())
//       .then(setSongs)
//   }, [])

//   useEffect(() => {
//     fetch('/artists')
//       .then((r) => r.json())
//       .then(setArtists)
//   }, [])

//   useEffect(() => {
//     fetch('/albums')
//       .then((r) => r.json())
//       .then(setAlbums)
//   }, [])

//   useEffect(() => {
//     fetch('/playlists')
//       .then((r) => r.json())
//       .then(setPlaylists)
//   }, [])

//   useEffect(() => {
//     fetch('/users')
//       .then((r) => r.json())
//       .then(setUsers)
//   }, [])



//   // const addUserState = (newUserObj) => {
//   //   setUsers([newUserObj, ...users])
//   // }

//   // const addPlaylistState = (newPlaylistObj) => {
//   //   setPlaylists([newPlaylistObj, ...playlists])
//   // }

//   return (
//     <div>
//      <Home></Home>
//     </div>
//   );
// }




// export default App;


import React, { useEffect, useState } from "react";

import Login from "./Login";
import { getTokenFromUrl } from "./Spotify";
import SpotifyWebApi from "spotify-web-api-js";
import SidebarOption from "./sidebarOption";
import Sidebar from "./Sidebar";

const spotify = new SpotifyWebApi();

function App() {
  const [token, setToken] = useState();

  useEffect(() => {
    const hash = getTokenFromUrl();
    window.location.hash = "";
    const _token = hash.access_token;

    if (_token) {
      setToken(_token);
      spotify.setAccessToken(_token);
    }

    console.log("token", token);
  }, []);

  return <div>
    <Sidebar></Sidebar>
    <SidebarOption></SidebarOption>
  </div>;
}

export default App;
