import React from 'react'
import PropTypes from 'prop-types'
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import circlePlus from '../icons/circle-plus.png'

function ClubFinder(props) {
    console.log(circlePlus)
    const iconSize = props.iconSize
    const text = 'Find a club';
    console.log(iconSize)
    return (
        <ListItem button key={text} style = {{paddingLeft: '0px'}}>
            <img src = {circlePlus}/>
            <ListItemText primary={text} />
        </ListItem>
    )
}


export default ClubFinder

