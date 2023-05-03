import React, { useState, useEffect, useContext } from "react";
import SongCard from "./SongCard"
import { UserContext } from "../context/user";

function Songs({songs}) {
    
    const { user, setUser } = useContext(UserContext);
    const [songs, setSongs] = useState([]);

    useEffect(() => {
        fetch("/songs")
        .then((r) => r.json())
        .then(setSongs);
    }, []);

    console.log(user)

   

    let songCards = songs.map((song) => <SongCard key={song.id} user={user} song={song} />);

    return (
        <div className='profile'>
            <h1>Your Songs</h1>
            <div className="songList">
                {songCards}
            </div>
        </div>
    )
}

export default Songs