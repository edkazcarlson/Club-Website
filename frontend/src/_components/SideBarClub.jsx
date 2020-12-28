import React from 'react'
import PropTypes from 'prop-types'

function SideBarClub(props) {
    const text = props.text;
    const imgSrc = props.imgSrc
    return (
        <ListItem button key={text}>
            <img src = {imgSrc}></img>
            <ListItemText primary={text} />
        </ListItem>
    )
}


export default SideBarClub

