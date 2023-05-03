import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import Home from "./Home";



function App() {
  const [songs, setSongs] = useState([])
  const [artists, setArtists] = useState([])
  const [albums, setAlbums] = useState([])
  const [playlists, setPlaylists] = useState([])
  const [users, setUsers] = useState([])
  
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
        <header>
         
            <NavBar className="App-header"/>
            <Switch>
                <Route path='/songs'>
                    <MoviePage changeSearch={changeSearch} addSong={addSongs} movies={searchedSongs} className="App-header"/>
                </Route>
                <Route path='/account'>
                    <AccountPage className="App-header" currentUser={currentUser} onLogout={onLogout} />
                </Route>
                <Route path='/playlists'>
                    <AboutMe className="App-header"/>
                </Route>
                <Route path='/login'>
                    <LoginPage className="App-header" currentUser={currentUser} onLogin={onLogin} onLogout={onLogout} />
                </Route>
               
                <Route path='/update_account'>
                    <UpdateAccount className="App-header" currentUser={currentUser} setCurrentUser={setCurrentUser} onLogout={onLogout} onDeleteAccount={onDeleteAccount} />
                </Route>
               
                <Route path='/'>
                    <Home className="App-header"/>
                </Route>
                <Route path='*'>
                    <h1>404 not found</h1>
                </Route>
            </Switch>
        </header>
    </div>
  );
}




export default App;




