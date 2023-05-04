import React, { useEffect, useState } from "react";
import { Switch, Route, NavLink, useHistory } from "react-router-dom";
import Login from "./Login";
import Header from "./Header";




function App() {

  const API_KEY = `b"\x7f\x7f(\xe8\x0c('\xa8\xa5\x82pb\t\x1d>rZ\x8c^\x7f\xbb\xe2L|"`
  
  const [songs, setSongs] = useState([])
  const [artists, setArtists] = useState([])
  const [albums, setAlbums] = useState([])
  const [playlists, setPlaylists] = useState([])
  const [users, setUsers] = useState([])
  const [currentUser, setCurrentUser] = useState(null);
  const history = useHistory();
  
  function onLogout() {
    setCurrentUser(null);
    history.push('/')
}

const onCreateAccount = userObj => {
    setUsers( [ ...users, userObj ] )
}

function onLogin(user) {
    setCurrentUser(user);
    history.push('/account')
}

function onDeleteAccount() {
    const requestOptions = {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({id: currentUser.id})
    };
    fetch(`/playlists/${currentUser.id}`, requestOptions)
        .then(setCurrentUser(null))
        .then(history.push('/'))
}

  
useEffect(() => {
  fetch("/check_session").then((response) => {
      if (response.ok) {
          response.json().then((customer) => setCurrentUser(customer));
      }
  });
  }, []);





  useEffect(() => {
    fetch('/songs')
      .then((r) => r.json())
      .then(setSongs)
  }, [])

  useEffect(() => {
    fetch('/artists')
      .then((r) => r.json())
      .then(setArtists)
  }, [])

  useEffect(() => {
    fetch('/albums')
      .then((r) => r.json())
      .then(setAlbums)
  }, [])

  useEffect(() => {
    fetch('/playlists')
      .then((r) => r.json())
      .then(setPlaylists)
  }, [])

  useEffect(() => {
    fetch('/users')
      .then((r) => r.json())
      .then(setUsers)
  }, [])



  // const addUserState = (newUserObj) => {
  //   setUsers([newUserObj, ...users])
  // }

  // const addPlaylistState = (newPlaylistObj) => {
  //   setPlaylists([newPlaylistObj, ...playlists])
  // }

  return (
    <div className='App'>
        <Login></Login>
         
          
           
            
       
    </div>

);
}




export default App;




