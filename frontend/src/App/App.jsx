import React, { useEffect } from 'react';
import { Router, Route, Switch, Redirect } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';

import { history } from '../_helpers';
import { alertActions } from '../_actions';
import { PrivateRoute } from '../_components';
import { HomePage } from '../Pages/HomePage';
import { LoginPage } from '../Pages/LoginPage';
import { RegisterPage } from '../Pages/RegisterPage';
import {NavBar} from '../_components/NavBar'
import { PersonalInfoPage } from '../Pages/PersonalInfoPage';


function App() {
    const alert = useSelector(state => state.alert);
    const dispatch = useDispatch();
    const userToken = localStorage.getItem('token')
    console.log(userToken)
    useEffect(() => {
        history.listen((location, action) => {
            // clear alert on location change
            dispatch(alertActions.clear());
        });
    }, []);

    const nav = <NavBar userToken = {userToken}/>


    return (
        <div >
            {/* {alert.message &&
                <div className={`alert ${alert.type}`}>{alert.message}</div>
            } */}
            <Router history={history}>
                <Route exact path="/" >
                    {nav}
                    <HomePage/>
                </Route>
                <PrivateRoute exact path="/settings" >
                    {nav}
                    <PersonalInfoPage/>
                </PrivateRoute>
                <Route path="/login" component={LoginPage} />
                <Route path="/register" component={RegisterPage} />
                {/* <Redirect from="*" to="/" /> */}
            </Router>
        </div>
    );
}

export { App };