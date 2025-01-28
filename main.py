# main.py
from model import Band, Venue, Concert, initialize_db, conn

def main():
    # Initialize the database
    print("Initializing the database...")
    initialize_db()
    print("Database created and initialized successfully!\n")

    # Test Band methods
    band1 = Band.find_by_id(1)
    if band1:
        print(f" Band: {band1.name} (Hometown: {band1.hometown})")
        print(" Concerts:")
        for concert in band1.concerts():
            print(f"  -  Concert ID: {concert.id}, Date: {concert.date}, Venue: {concert.venue().title}")
        print(" Venues:")
        for venue in band1.venues():
            print(f"  -  Venue: {venue.title}, City: {venue.city}")
        print(" Introductions:")
        for intro in band1.all_introductions():
            print(f"  -  {intro}")
        print()

    # Test Venue methods
    venue1 = Venue.find_by_title('The Blue Room')
    if venue1:
        print(f" Venue: {venue1.title} (City: {venue1.city})")
        print(" Concerts:")
        for concert in venue1.concerts():
            print(f"  -  Concert ID: {concert.id}, Date: {concert.date}, Band: {concert.band().name}")
        print(" Bands:")
        for band in venue1.bands():
            print(f"  -  Band: {band.name}, Hometown: {band.hometown}")
        most_frequent_band = venue1.most_frequent_band()
        print(f" Most Frequent Band: {most_frequent_band.name if most_frequent_band else 'None'}")
        print()

    # Test Concert methods
    concert1 = Concert.find_by_id(1) 
    if concert1:
        print(f" Concert Details:")
        print(f"  -  Date: {concert1.date}")
        print(f"  -  Band: {concert1.band().name}")
        print(f"  -  Venue: {concert1.venue().title}, City: {concert1.venue().city}")
        print(f"  -  Hometown Show: {'Yes' if concert1.hometown_show() else 'No'}")
        print(f"  -  Introduction: {concert1.introduction()}")
        print()

    # Close the database connection
    conn.close()
    print("Database connection closed. Goodbye!")

if __name__ == '__main__':
    main()  