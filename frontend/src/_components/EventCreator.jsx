import React, { useState } from 'react'
import Popup from 'reactjs-popup';
import 'reactjs-popup/dist/index.css';
//https://fullcalendar.io/docs/date-clicking-selecting


export default function EventCreator(props) {
    let openState = props.open;
    let opener = props.opener;
    console.log(openState)
    return(
        <Popup open={openState} closeOnDocumentClick onClose={opener(false)}>
        <div className="modal">
          <a className="close" onClick={opener(false)}>
            &times;
          </a>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Beatae magni
          omnis delectus nemo, maxime molestiae dolorem numquam mollitia, voluptate
          ea, accusamus excepturi deleniti ratione sapiente! Laudantium, aperiam
          doloribus. Odit, aut.
        </div>
      </Popup>
    );
}


