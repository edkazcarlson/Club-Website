import React from 'react'
import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'

export default class Calendar extends React.Component {
  render() {
    return (
      <FullCalendar
        plugins={[ dayGridPlugin ]}
        initialView="dayGridMonth"
        events = {[
            { title: 'event 1', timeText : '0:0:00', date: '2021-01-01' },
            { title: 'event 2', date: '2021-01-02' }
        ]}
        eventContent={this.renderEventContent}
      />
    )
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