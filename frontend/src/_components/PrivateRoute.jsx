import React from 'react';
import { Route, Redirect } from 'react-router-dom';

function PrivateRoute({ component: Component, roles, ...rest }) {
    return (
        <Route {...rest} render={props => {
            if (localStorage.getItem('user') === null) {
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