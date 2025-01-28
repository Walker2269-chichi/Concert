# Concert Management System

This project implements a concert management system using Python. The domain includes three main entities: `Band`, `Venue`, and `Concert`. The application uses object-oriented programming to model the relationships and interactions between these entities.

---

## Features

### Band
- Represents a musical band.
- Attributes:
  - `name`: The name of the band.
  - `hometown`: The hometown of the band.
- Methods:
  - `play_in_venue(venue, date)`: Schedules a new concert for the band at the specified venue on the given date.
  - `all_introductions()`: Returns all concert introductions for the band.

### Venue
- Represents a concert venue.
- Attributes:
  - `name`: The name of the venue.
  - `city`: The city where the venue is located.
- Methods:
  - `add_concert(concert)`: Associates a concert with the venue.
  - `concert_on(date)`: Finds the first concert at the venue on the given date.
  - `most_frequent_band()`: Returns the band that has performed the most at this venue.

### Concert
- Represents a concert event.
- Attributes:
  - `date`: The date of the concert.
  - `band`: The band performing at the concert.
  - `venue`: The venue where the concert is held.
- Methods:
  - `introduction()`: Returns the band's introduction for the concert.
  - `hometown_show()`: Checks if the concert is in the band's hometown.






