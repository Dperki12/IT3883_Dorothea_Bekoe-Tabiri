import sqlite3

# Step 1: Create a SQLite database and connect to it
conn = sqlite3.connect("dvdrental.db")
cursor = conn.cursor()

# Step 2: Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Temperature (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Day_Of_Week TEXT,
        Temperature_Value REAL
    )
""")

# Step 3: Read data from input file and insert into table
with open("Assignment5input.txt", "r") as file:
    for line in file:
        day,temperature = line.strip().split()
        cursor.execute("INSERT INTO Temperature (Day_Of_Week, Temperature_Value) VALUES (?, ?)", (day, float(temperature)))

conn.commit()

# Step 4: Get average temperature for Sunday and Thursday
cursor.execute("""
    SELECT Day_Of_Week, AVG(Temperature_Value) AS Avg_Temp
    FROM Temperature
    WHERE Day_Of_Week IN ('Sunday', 'Thursday')
    GROUP BY Day_Of_Week
""")

results = cursor.fetchall()
for day, avg_temp in results:
    print(f"The average temperature for {day}: {avg_temp:.2f}°F")

# Clean up
cursor.close()
conn.close()
