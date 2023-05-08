import React, { useEffect, useState } from "react";
import { NavLink, useHistory } from "react-router-dom";
import { Form, InputGroup, Row, Button } from 'react-bootstrap';

function UpdateAccount({currentUser, setCurrentUser, onLogout, onDeleteAccount}) {

    const [newFirstName, setNewFirstName] = useState('')
    const [newLastName, setNewLastName] = useState('')
    const [newEmail, setNewEmail] = useState('')
    const [newPassword, setNewPassword] = useState('')

    const handleFirstName = e => setNewFirstName(e.target.value)
    const handleLastName = e => setNewLastName(e.target.value)
    const handleEmail = e => setNewEmail(e.target.value)
    const handlePassword = e => setNewPassword(e.target.value)
    const history = useHistory();

	function handleUpdateAccountSubmit(e) {
        e.preventDefault();

        const updatedCustomer = {
            fname: newFirstName,
            lname: newLastName,
            email: newEmail,
            password: newPassword
        }

        const requestOptions = {
            method: 'PATCH',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                fname: newFirstName,
                lname: newLastName,
                email: newEmail,
                password: newPassword
            })
        };
        fetch(`/users/${currentUser.id}`, requestOptions)
            .then(setCurrentUser(updatedCustomer))
            .then(history.push('/account'))
    }

    function handleLogout() {
        fetch("/logout", {
            method: "DELETE",
        }).then(() => onLogout());
    }

    return (
        <div>
            { currentUser ? (
                <div>
                    <div className="container mt-3 mb-3"><h1>Update your account information:</h1></div>
                    <form className="container mt-3 mb-3" onSubmit={handleUpdateAccountSubmit}>
                        <Row className="mb-3">
                            <Form.Group controlId="formGridText" className="col col-sm-3">
                                <Form.Label>First Name</Form.Label>
                                <Form.Control className="form-control"type="name" name="fname" placeholder="First Name" onChange={handleFirstName} />
                            </Form.Group>
                            <Form.Group controlId="formGridText" className="col col-sm-3">
                                <Form.Label>Last Name</Form.Label>
                                <Form.Control className="form-control" type="name" name="lname" placeholder="Last Name" onChange={handleLastName} />
                            </Form.Group>
                        </Row>
                        <Row className="mb-3">
                            <Form.Group controlId="formGridEmail" className="col col-sm-3">
                                <Form.Label>Email Address</Form.Label>
                                <Form.Control className="form-control" type="text" name="email" placeholder="Email Address" onChange={handleEmail} />
                            </Form.Group>
                        </Row>
                       
                        <Row className="mb-3">
                            <Form.Group controlId="formGridPassword" className="col col-sm-3">
                                <Form.Label>New Password</Form.Label>
                                <Form.Control className="form-control" type="text" name="password" placeholder="New Password" onChange={handlePassword} />
                            </Form.Group>
                            <Form.Group controlId="formGridConfirmPassword" className="col col-sm-3">
                                <Form.Label>Confirm Password</Form.Label>
                                <Form.Control className="form-control" type="text" name="confirmpassword" placeholder="Confirm Password" />
                            </Form.Group>
                        </Row>
                        <Row className="mb-3">
                            <Form.Group controlId="formGridSubmit" className="col col-sm-3">
                                <input type="submit" value="Update Account" className="me-4 btn btn-success btn-md btn-block" />
                            </Form.Group>
                        </Row>
                    </form>
                    <div className="container mt-2 mb-2"><button onClick={handleLogout} className="me-4 btn btn-danger btn-md btn-block">Logout</button></div>
                    <div className="container mt-2 mb-2"><button onClick={onDeleteAccount} className="me-4 btn btn-danger btn-md btn-block">Delete My Account</button></div>
                </div>) : (
                    <div>
                        <br />
                        <div>Please <NavLink className='NavLink' exact to = '/login'>Login</NavLink> to update your account</div>
                    </div>
                )}
        </div>
	)
}

export default UpdateAccount;