import React from 'react'
import PropTypes from 'prop-types'
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';

function SideBarClub(props) {
    const text = props.text;
    const imgSrc = props.imgSrc
    const iconSize = props.iconSize
    return (
        <ListItem button key={text} style = {{paddingLeft: '0px'}}>
            <img src = {imgSrc} style = {{borderRadius: '50%'}} width = {iconSize}></img>
            <ListItemText primary={text} />
        </ListItem>
    )
}


export default SideBarClub

