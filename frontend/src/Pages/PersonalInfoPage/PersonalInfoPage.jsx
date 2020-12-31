import React, { useState, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import Typography from '@material-ui/core/Typography';

import { userActions } from '../../_actions';

function PersonalInfoPage() {
    const [inputs, setInputs] = useState({
        username: '',
        password: ''
    });
    const [submitted, setSubmitted] = useState(false);
    const { username, password } = inputs;
    const loggingIn = useSelector(state => state.authentication.loggingIn);
    const dispatch = useDispatch();
    const location = useLocation();

    // reset login status
    useEffect(() => { 
        dispatch(userActions.logout()); 
    }, []);

    function handleChange(e) {
        const { name, value } = e.target;
        setInputs(inputs => ({ ...inputs, [name]: value }));
    }

    function handleSubmit(e) {
        e.preventDefault();

        setSubmitted(true);
        if (username && password) {
            // get return url from location state or default to home page
            const { from } = location.state || { from: { pathname: "/" } };
            dispatch(userActions.login(username, password, from));
        }
    }

    return (
        <div className="col-lg-8 offset-lg-2">
            <div>
                <img src = "https://th.bing.com/th/id/OIP.e5q3Vs_qDs-pmOL_r6TIqwHaHm?pid=Api&rs=1" width = '20%'></img>
                <Typography>
                    <h2>
                        My Name
                    </h2>
                </Typography>
            </div>
        </div>
    );
}

export { PersonalInfoPage };