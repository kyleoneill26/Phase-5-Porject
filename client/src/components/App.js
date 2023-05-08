import React, { useEffect, useState } from "react";
import { Switch, Route, NavLink, useHistory } from "react-router-dom";
import Login from "./Login";
import Header from "./Header";
import NavBar from "./NavBar";
import AccountPage from "./AccountPage";
import CreateAccount from "./CreateAccount";
import UpdateAccount from "./UpdateAccount";








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

// function onDeleteAccount() {
//     const requestOptions = {
//         method: 'DELETE',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify({id: currentUser.id})
//     };
//     fetch(`/playlists/${currentUser.id}`, requestOptions)
//         .then(setCurrentUser(null))
//         .then(history.push('/'))
// }

  
useEffect(() => {
  fetch("/check_session").then((response) => {
      if (response.ok) {
          response.json().then((user) => setCurrentUser(user));
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

  // useEffect(() => {
  //   fetch('/users')
  //     .then((r) => r.json())
  //     .then(setUsers)
  // }, [])



  // const addUserState = (newUserObj) => {
  //   setUsers([newUserObj, ...users])
  // }

  // const addPlaylistState = (newPlaylistObj) => {
  //   setPlaylists([newPlaylistObj, ...playlists])
  // }

  return (
    <div className='App'>
    <header>
        { currentUser ? (<div>Welcome, {currentUser.fname} {currentUser.lname}!</div>) : <div><NavLink className='NavLink' exact to = '/login'>Login</NavLink></div>}
        <NavBar className="App-header"/>
        <Switch>
       
            <Route path='/login'>
                <Login className="App-header" currentUser={currentUser} onLogin={onLogin} onLogout={onLogout} />
            </Route>
            <Route path='/login'>
                <Login className="App-header" currentUser={currentUser} onLogin={onLogin} onLogout={onLogout} />
            </Route>
            <Route path='/register'>
                  <CreateAccount className="App-header" currentUser={currentUser} onLogout={onLogout} onCreateAccount={onCreateAccount} />
            </Route>
            <Route path='/update_account'>
                  <UpdateAccount className="App-header" currentUser={currentUser} setCurrentUser={setCurrentUser} onLogout={onLogout}  />
            </Route>
         
            <Route path='/'>
                <AccountPage className="App-header"/>
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




