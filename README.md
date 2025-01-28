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



## Getting Started

### Prerequisites

- Python 3.8 

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate  # For Linux/Mac
   env\Scripts\activate    # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---


## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---


