import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import Home from "./Home";



function App() {
  const [songs, setSongs] = useState([])
  const [artists, setArtists] = useState([])
  const [albums, setAlbums] = useState([])
  const [playlists, setPlaylists] = useState([])
  const [users, setUsers] = useState([])
  


  

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
    <div>
        <UserProvider>
            <Header />
            <Route exact path='/users/:id'>
                <ViewProfile />
            </Route>
            <Switch>
                <Route exact path="/">
                    <Home/>
                </Route>
                <Route exact path="/songs">
                    <Songs addReviewToState={addReviewToState}/>
                </Route>
                <Route exact path="/albums">
                    <Reviews reviews={displayReviews}/>
                </Route>
                <Route exact path="/users">
                    <Users/>
                </Route>
                <Route path="/profile">
                    <Profile removeReviewFromState={removeReviewFromState}/>
                </Route>
            </Switch>
        </UserProvider>
    </div>
  );
}




export default App;




