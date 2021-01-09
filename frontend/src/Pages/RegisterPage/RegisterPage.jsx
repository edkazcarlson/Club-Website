import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';

import { userActions } from '../../_actions';

function RegisterPage() {
    const [user, setUser] = useState({
        email : '',
        password: '',
        full_name: ''
    });
    const prettyFields = ['Email', 'Password', 'Full Name']
    const [submitted, setSubmitted] = useState(false);
    const registering = useSelector(state => state.registration.registering);
    const dispatch = useDispatch();

    // reset login status
    useEffect(() => {
        dispatch(userActions.logout());
    }, []);

    function handleChange(e) {
        const { name, value } = e.target;
        setUser(user => ({ ...user, [name]: value }));
    }

    function handleSubmit(e) {
        e.preventDefault();

        setSubmitted(true);
        if (user.full_name && user.email && user.password) {
            dispatch(userActions.register(user));
        }
    }
    console.log(`user.keys: ${Object.keys(user)}`)
    const forms = Object.keys(user).map(function(x, idx) {
        return ( <div className="form-group" key = {x}>
        <label>{prettyFields[idx]}</label>
        <input type="text" name={x} value={user.x} onChange={handleChange} className={'form-control' + (submitted && !user.x ? ' is-invalid' : '')} />
        {submitted && !user.x &&
            <div className="invalid-feedback">{prettyFields[idx]} is required</div>
        }
    </div>)
    })

    return (
        <div className="col-lg-8 offset-lg-2">
            <h2>Register</h2>
            <form name="form" onSubmit={handleSubmit}>
                {forms}
                <div className="form-group">
                    <button className="btn btn-primary">
                        {registering && <span className="spinner-border spinner-border-sm mr-1"></span>}
                        Register
                    </button>
                    <Link to="/login" className="btn btn-link">Cancel</Link>
                </div>
            </form>
        </div>
    );
}

export { RegisterPage };