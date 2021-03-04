import React, {useState} from 'react'
import TextField from '@material-ui/core/TextField'

export default function LoginEntryField(props) {
    let [hasError, setError] = React.useState(false);
    let [helperText, setHelper] = React.useState('');
    function textChange(e){
        if (props.verification === undefined){
            props.changeUser(e.target.value, props.modelKey)
        } else {
            console.log(props.currentPassword)
            if (e.target.value != props.currentPassword){
                setError(true)
                setHelper('Passwords to not match')
            } else{
                setError(false)
                setHelper('')
            }
        }
    }

    return (
        <div style = {{padding: '10px'}}>
            <TextField style = {{maxWidth: '100%'}}
            id="outlined-basic" label={props.label} error = {hasError} variant="outlined" onChange = {textChange} helperText = {helperText}/>
        </div>
    )
}
