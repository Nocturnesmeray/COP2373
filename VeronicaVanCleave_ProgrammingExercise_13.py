import sqlite3
import random
import matplotlib.pyplot as plt

def database():
    """
    Creates the database, builds the population table, and inputs the
    baseline population data for 10 different cities in 2025.

    Parameters:
        None

    Variables:
        conn (sqlite3.Connection): The connection object to the database
        cursor (sqlite3.Cursor): The cursor object used for the SQL queries
        fl_cities_2025 (list): The list of cities including city, year, and population

    Logic:
        1. Made the database.
        2. Created the population table.
        3. Delete existing information in order to prevent duplication.
        4. Made a list of 10 Florida cities and their population during 2025.
        5. Insert the list into the database.
        6. Commit the changes and close the connection.

    Return:
        None
    """
    sqliteConnection = sqlite3.connect('population_VVC.db')
    cursor = sqliteConnection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS population (
        city TEXT,
        year INTEGER,
        population INTEGER
        )
        ''')

    cursor.execute('DELETE FROM population')

    fl_cities_2025 = [
         ("Jacksonville", 2025, 1024310),
        ("Miami", 2025, 498060),
        ("Tampa", 2025, 421042),
        ("Orlando", 2025, 341600),
        ("Tallahassee", 2025, 206877),
        ("Palm Bay", 2025, 147486),
        ("Gainesville", 2025, 150331),
        ("Brandon", 2025, 118347),
        ("Clearwater", 2025, 116678),
        ("Fort Myers", 2025,103075)
    ]

    # Inserts the baseline data into the population table matplotlib line graph
    cursor.executemany('''
    INSERT INTO population (city, year, population)
    VALUES (?,?,?)
    ''', fl_cities_2025)

    sqliteConnection.commit()

    # Close the cursor after use
    cursor.close()
    sqliteConnection.close()

def simulation():
    """
    Simulates the population growth and decline for 20 years.

    Parameters:
        None

    Variables:
        conn (sqlite3.Connection): The connection object to the database
        cursor (sqlite3.Cursor): The cursor object used for the SQL queries
        base_data (list): The list of cities including city, year, and population
        simulated_data (list): The list of simulated data
        city (str): The name of the city being simulated
        base_pop (int): The starting population being simulated
        current_pop (int): The current population
        year (int): The specific year used
        rate (float): The random growth or decline reate

    Logic:
        1. Connect to the database retrieve the population table.
        2. Loop through each city for the next 20 years.
        3. Generate a random growth or decline rate between -3% and 5%.
        4. Calculate the new population for a city and append it to a list.
        5. Insert the simulated data into the database.
        6. Commit the changes and close the connection.

    Return:
        None
    """
    conn = sqlite3.connect('population_VVC.db')
    cursor = conn.cursor()

    cursor.execute('SELECT city, population FROM population WHERE year = 2025')
    base_data = cursor.fetchall()

    simulated_data = []

    for city, base_pop in base_data:
        current_pop = base_pop

        for year in range(2026, 2046,):
            rate = random.uniform(-0.03, 0.05)
            current_pop = current_pop * (1 + rate)
            simulated_data.append([city, year, current_pop])

    # Insert all the simulated data into the database at once
    cursor.executemany('''INSERT INTO population (city, year, population)
    VALUES (?,?,?)''', simulated_data)

    conn.commit()
    cursor.close()
    conn.close()

def main():
    """
    Prompts the user to select a city and uses matplotlib to display a line
    graph of the simulated population.

    Parameters:
        None

    Variables:
        conn (sqlite3.Connection): The connection object to the database
        cursor (sqlite3.Cursor): The cursor object used for the SQL queries
        cities (list): The list of cities including city, year, and population
        selected_city (str): The city being simulated.
        years (list): The years displayed on the X-axis.
        populations (list): The population displayed on the Y-axis.

    Logic:
        1. Connect to the database retrieve the cities names.
        2. Display the available cities to the user.
        3. Prompt the user to input a chosen city.
        4. Plot the data using matplotlib and display a visual graph.


    Return:
        None
    """
    conn = sqlite3.connect('population_VVC.db')
    cursor = conn.cursor()

    cursor.execute('SELECT DISTINCT city FROM population')
    cities = [row[0] for row in cursor.fetchall()]

    for city in cities:
        print(city)

    selected_city = ("")
    selected_city = input("Choose a city: ")
    cursor.execute('SELECT year, population FROM population WHERE city = ?', (selected_city,))

    city_data = cursor.fetchall()
    conn.close()

    # Separate the data into X and Y coordinate lists for
    years = [row[0] for row in city_data]
    populations = [row[1] for row in city_data]

    plt.plot(years, populations)
    plt.title(f"Population Growth Simulation for {selected_city}")
    plt.xlabel("Year")
    plt.xticks(range(2025, 2046, 2))
    plt.ylabel("Population")
    plt.show()

if __name__ == "__main__":
    database()
    simulation()
    main()
