import React, { useEffect, useState } from "react";
import { NavLink, useHistory } from "react-router-dom";
import { Form, InputGroup, Row, Button } from 'react-bootstrap';


function Login({currentUser, onLogin, onLogout}) {

    const [newEmail, setNewEmail] = useState('')
    const [newPassword, setNewPassword] = useState('')

    const handleEmail = e => setNewEmail(e.target.value)
    const handlePassword = e => setNewPassword(e.target.value)

    const history = useHistory();

    function handleLogout() {
        fetch("/logout", {
            method: "DELETE",
        }).then(() => onLogout());
    }
    
    function handleLoginResult(user) {
        if (user.hasOwnProperty('id')) {
            onLogin(user);
        } else {
            history.push('/login');
        }
    }

	function handleLoginSubmit(e) {
        e.preventDefault();

        try {
            const requestOptions = {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    email: newEmail,
                    password: newPassword
                })
            };
            fetch('/login', requestOptions)
                .then((r) => r.json())
                .then((user) => {
                    handleLoginResult(user);
                })
        } catch (err) {
            console.log(err);
        }
    
    }
    
    return (
        <div>
            { currentUser ? (
                <div>
                    <br />
                    <div><h2>Logged in as:</h2></div>
                    <div>Name: {currentUser.fname} {currentUser.lname}</div>
                    <div>Email: {currentUser.email}</div>
               
                    <br />
                    <NavLink className='NavLink' exact to = '/account'>My Account</NavLink>
                    <br />
                    <NavLink className='NavLink' exact to = '/update_account'>Update My Account</NavLink>
                    <br />
                    <button onClick={handleLogout} className="me-4 btn btn-danger btn-md btn-block">Logout</button>
                </div>) : (
                    <div>
                        <br />
                        <div className="container mt-3 mb-3"><h1>Enter your login info:</h1></div>
                        <form className="container mt-3 mb-3" onSubmit={handleLoginSubmit}>
                        <Row className="mb-3">
                        <Form.Group controlId="formGridEmail" className="col col-sm-3">
                                <Form.Label>Email Address</Form.Label>
                                <Form.Control className="form-control" type="text" name="email" placeholder="Email Address" onChange={handleEmail} />
                            </Form.Group>
                            <Form.Group controlId="formGridPassword" className="col col-sm-3">
                                <Form.Label>Password</Form.Label>
                                <Form.Control className="form-control" type="text" name="password" placeholder="Password" onChange={handlePassword} />
                            </Form.Group>
                        </Row>
                        <Row className="mb-3">
                            <Form.Group controlId="formGridSubmit" className="col col-sm-3">
                                <input type="submit" value="login" className="me-4 btn btn-success btn-md btn-block" />
                            </Form.Group>
                        </Row>
                    </form>
                    </div>
                )}
        </div>
	)
}

export default Login;