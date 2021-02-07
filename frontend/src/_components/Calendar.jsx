import React from 'react'
import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from '@fullcalendar/interaction';
import timeGridPlugin from '@fullcalendar/timegrid';
import EventCreator from './EventCreator'

export default class Calendar extends React.Component {
  constructor(props){
    super(props);
    this.state = {open: false};
  }

  opener(status){
    this.setState({open: status});
  }
  
  render() {
    console.log(`Open state: ${this.state.open}`)
    return (
      [
      <EventCreator
        open = {this.state.open}
        opener = {() => this.opener.bind(this)}
      />,
      <FullCalendar
        plugins={[ timeGridPlugin, interactionPlugin ]}
        initialView="timeGridWeek"
        events = {[
            { title: 'event 1', timeText : '0:0:00', date: '2021-02-01' },
            { title: 'event 2', date: '2021-02-02' }
        ]}
        eventContent={this.renderEventContent}
        dateClick = {this.dateClick.bind(this)}
      />]
    )
  }

  dateClick(e) {
    console.log(this)
    console.log('date clicked');
    console.log(e);
    this.opener(true);
  }

  renderEventContent(eventInfo) {
    console.log(eventInfo)
    return (
      <>
        <b>{eventInfo.timeText}</b>
        <i>{eventInfo.event.title}</i>
      </>
    )
  }
}