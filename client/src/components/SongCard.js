import React, {useState} from 'react'


function SongCard() {

    // const handleClick = () => {
    //     setCreateForm(!createForm)
    // }

    return (
        <div className="songCard">
            <h1>Title: {song.title}</h1>
            <h1>Artist: {song.artist}</h1>
            {createForm && user ? <songs user={user} song={song} /> : <div></div>}
        </div>
    )
}

export default SongCard