import sqlite3
from typing import List, Optional

# Database connection
conn = sqlite3.connect('DB/concerts.db')
cursor = conn.cursor()

# Helper function to execute SQL queries
def execute_query(query, params=None, fetch_one=False):
    cursor.execute(query, params or ())
    if fetch_one:
        return cursor.fetchone()
    return cursor.fetchall()

# Helper function to insert data into the database
def insert_data(table, data):
    columns = ', '.join(data.keys())
    placeholders = ', '.join(['?'] * len(data))
    query = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'
    cursor.execute(query, tuple(data.values()))
    conn.commit()

# Band class
class Band:
    def __init__(self, id: int, name: str, hometown: str):
        self.id = id
        self.name = name
        self.hometown = hometown

    def __repr__(self):
        return f"Band(id={self.id}, name='{self.name}', hometown='{self.hometown}')"

    @classmethod
    def create(cls, name: str, hometown: str) -> None:
        """Creates a new band in the database."""
        data = {'name': name, 'hometown': hometown}
        insert_data('bands', data)

    @classmethod
    def find_by_id(cls, id: int) -> Optional['Band']:
        """Finds a band by its ID."""
        query = 'SELECT * FROM bands WHERE id = ?'
        result = execute_query(query, (id,), fetch_one=True)
        if result:
            return cls(*result)
        return None

    def concerts(self) -> List['Concert']:
        """Returns all concerts for this band."""
        query = 'SELECT * FROM concerts WHERE band_id = ?'
        results = execute_query(query, (self.id,))
        return [Concert(*row) for row in results]

    def venues(self) -> List['Venue']:
        """Returns all venues where this band has performed."""
        query = '''
        SELECT DISTINCT venues.* FROM venues
        JOIN concerts ON venues.id = concerts.venue_id
        WHERE concerts.band_id = ?
        '''
        results = execute_query(query, (self.id,))
        return [Venue(*row) for row in results]

    def play_in_venue(self, venue_title: str, date: str) -> None:
        """Schedules a new concert for this band at the specified venue and date."""
        venue = Venue.find_by_title(venue_title)
        if venue:
            # Check if a concert already exists for this band, venue, and date
            query = '''
            SELECT id FROM concerts
            WHERE band_id = ? AND venue_id = ? AND date = ?
            '''
            result = execute_query(query, (self.id, venue.id, date), fetch_one=True)
            if not result:  # Only insert if no duplicate exists
                data = {'band_id': self.id, 'venue_id': venue.id, 'date': date}
                insert_data('concerts', data)

    def all_introductions(self) -> List[str]:
        """Returns a list of introductions for all concerts this band has performed."""
        query = '''
        SELECT DISTINCT venues.city FROM venues
        JOIN concerts ON venues.id = concerts.venue_id
        WHERE concerts.band_id = ?
        '''
        results = execute_query(query, (self.id,))
        return [f"Hello {row[0]}!!!!! We are {self.name} and we're from {self.hometown}" for row in results]

    @classmethod
    def most_performances(cls) -> Optional['Band']:
        """Returns the band with the most performances."""
        query = '''
        SELECT band_id, COUNT(*) AS performance_count
        FROM concerts
        GROUP BY band_id
        ORDER BY performance_count DESC
        LIMIT 1
        '''
        result = execute_query(query, fetch_one=True)
        if result:
            return cls.find_by_id(result[0])
        return None

# Venue class
class Venue:
    def __init__(self, id: int, title: str, city: str):
        self.id = id
        self.title = title
        self.city = city

    def __repr__(self):
        return f"Venue(id={self.id}, title='{self.title}', city='{self.city}')"

    @classmethod
    def create(cls, title: str, city: str) -> None:
        """Creates a new venue in the database."""
        data = {'title': title, 'city': city}
        insert_data('venues', data)

    @classmethod
    def find_by_title(cls, title: str) -> Optional['Venue']:
        """Finds a venue by its title."""
        query = 'SELECT * FROM venues WHERE title = ?'
        result = execute_query(query, (title,), fetch_one=True)
        if result:
            return cls(*result)
        return None

    @classmethod
    def find_by_id(cls, id: int) -> Optional['Venue']:
        """Finds a venue by its ID."""
        query = 'SELECT * FROM venues WHERE id = ?'
        result = execute_query(query, (id,), fetch_one=True)
        if result:
            return cls(*result)
        return None

    def concerts(self) -> List['Concert']:
        """Returns all concerts at this venue."""
        query = 'SELECT * FROM concerts WHERE venue_id = ?'
        results = execute_query(query, (self.id,))
        return [Concert(*row) for row in results]

    def bands(self) -> List['Band']:
        """Returns all bands that have performed at this venue."""
        query = '''
        SELECT DISTINCT bands.* FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        WHERE concerts.venue_id = ?
        '''
        results = execute_query(query, (self.id,))
        return [Band(*row) for row in results]

    def concert_on(self, date: str) -> Optional['Concert']:
        """Finds the first concert at this venue on the specified date."""
        query = 'SELECT * FROM concerts WHERE venue_id = ? AND date = ?'
        result = execute_query(query, (self.id, date), fetch_one=True)
        if result:
            return Concert(*result)
        return None

    def most_frequent_band(self) -> Optional['Band']:
        """Returns the band that has performed the most at this venue."""
        query = '''
        SELECT band_id, COUNT(*) AS performance_count
        FROM concerts
        WHERE venue_id = ?
        GROUP BY band_id
        ORDER BY performance_count DESC
        LIMIT 1
        '''
        result = execute_query(query, (self.id,), fetch_one=True)
        if result:
            return Band.find_by_id(result[0])
        return None

# Concert class
class Concert:
    def __init__(self, id: int, band_id: int, venue_id: int, date: str):
        self.id = id
        self.band_id = band_id
        self.venue_id = venue_id
        self.date = date

    def __repr__(self):
        return f"Concert(id={self.id}, band_id={self.band_id}, venue_id={self.venue_id}, date='{self.date}')"

    @classmethod
    def create(cls, band_id: int, venue_id: int, date: str) -> None:
        """Creates a new concert in the database."""
        data = {'band_id': band_id, 'venue_id': venue_id, 'date': date}
        insert_data('concerts', data)

    @classmethod
    def find_by_id(cls, id: int) -> Optional['Concert']:
        """Finds a concert by its ID."""
        query = 'SELECT * FROM concerts WHERE id = ?'
        result = execute_query(query, (id,), fetch_one=True)
        if result:
            return cls(*result)
        return None

    def band(self) -> Optional['Band']:
        """Returns the band for this concert."""
        return Band.find_by_id(self.band_id)

    def venue(self) -> Optional['Venue']:
        """Returns the venue for this concert."""
        return Venue.find_by_id(self.venue_id)

    def hometown_show(self) -> bool:
        """Checks if the concert is in the band's hometown."""
        band = self.band()
        venue = self.venue()
        if band and venue:
            return band.hometown == venue.city
        return False

    def introduction(self) -> str:
        """Returns the band's introduction for this concert."""
        band = self.band()
        venue = self.venue()
        if band and venue:
            return f"Hello {venue.city}!!!!! We are {band.name} and we're from {band.hometown}"
        return "Introduction not available."

# Initialize the database
def initialize_db():
    """Initializes the database by running the SQL scripts."""
    with open('scripts/tables.sql', 'r') as f:
        cursor.executescript(f.read())  