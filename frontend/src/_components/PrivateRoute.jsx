import React from 'react';
import { Route, Redirect } from 'react-router-dom';

function PrivateRoute({ component: Component, roles, ...rest }) {
    console.log(`localStorage.getItem('user'): ${localStorage.getItem('user')}`)
    if (localStorage.getItem('user') === null) {
        console.log('couldnt get user')
    } else {
        console.log('could get user')
        console.log(localStorage.getItem('user'))
    }
    return (
        <Route {...rest} render={props => {
            if (localStorage.getItem('user') === null) {
                console.log('got into the failed to get user ')
                console.log(localStorage.getItem('user'))
                // not logged in so redirect to login page with the return url
                return <Redirect to={{ pathname: '/login', state: { from: props.location } }} />
            } else {
                console.log(`found user: ${localStorage.getItem('user')}`)
            }

            // logged in so return component
            return <Component {...props} />
        }} />
    );
}

export { PrivateRoute };