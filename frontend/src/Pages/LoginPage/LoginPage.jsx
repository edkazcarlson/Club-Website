import React, { useState, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { makeStyles } from '@material-ui/core/styles';

import { userActions } from '../../_actions';
import { Container, Paper, Typography} from '@material-ui/core';
import TextField from '@material-ui/core/TextField'
import LoginEntryField from './LoginEntryField'

const useStyles = makeStyles((theme) => ({
    root: {
      '& > *': {
        margin: theme.spacing(1),
        width: '25ch',
      },
    },
  }));



function LoginPage() {
    let [loginState, setLoginState] = React.useState(true);
    let [userEmail, setUserEmail] = React.useState('');
    let [userName, setUserName] = React.useState('');
    let [userPass, setUserPass] = React.useState('');
    let setters = {'Username': setUserName, 'Password': setUserPass, 'Email': setUserEmail}
    const dispatch = useDispatch();

    function changeUser(newVal, modelKey){
        const setter = setters[modelKey];
        setter(newVal);
    }

    let form = null;
    const classes = useStyles();
    if (loginState){
        form = [<LoginEntryField label = 'Username' changeUser = {changeUser} modelKey = 'Username'/>,
        <LoginEntryField label = 'Password' changeUser = {changeUser} modelKey = 'Password'/>]
    } else {
        form = [<LoginEntryField label = 'Username' changeUser = {changeUser} modelKey = 'Username'/>,
        <LoginEntryField label = 'Email' changeUser = {changeUser} modelKey = 'Email'/>,
        <LoginEntryField label = 'Password' changeUser = {changeUser} modelKey = 'Password'/>,
        <LoginEntryField label = 'Verify Password' 
        modelKey = '' currentPassword = {userPass} verification = {true}/>]
    }
    
    function submitData(){
        if (loginState){

        } else {

        }
    }

    return (
        <div style = {{backgroundColor: 'red', height: '100%', width: '100%'}}>
            <div 
            style = {{backgroundColor: '#F0FFFF', alignItems: 'center', borderRadius: '25px', maxWidth: '500px',  maxHeight: '600px', margin: '50px auto'}}>
                <div style = {{display: 'flex', justifyContent: 'space-around'}}>
                    <Typography variant = 'h3' onClick = {() => setLoginState(true)} style = {loginState ? {opacity: '1'} : {opacity: '0.5'}}>
                        Login
                    </Typography>
                    <Typography variant = 'h3' onClick = {() => setLoginState(false)} style = {loginState ? {opacity: '0.5'} : {opacity: '1'}}>
                        Register
                    </Typography>
                </div>
                <form noValidate autoComplete="off"
                 style = {{display: 'flex', justifyContent: 'center', alignItems: 'center', flexDirection: 'column'}}>
                    {form}
                </form>
                <Button onClick = {submitData}>
                    Submit
                </Button>
            </div>
        </div>

    );
}

export { LoginPage };