import pandas as pd
df=pd.read_csv("Arivals.csv")

class Flight:
    def __init__(self, flight_num, delay_time):
        self.flight_num = flight_num
        self.delay_time = float(delay_time)

    def check_severity(self):
        if 30 <= self.delay_time <= 60:
            print(f"STANDARD WARNING: Flight {self.flight_num} is delayed by {self.delay_time} mins.")
        elif self.delay_time > 60:
            print(f"SERVER WARNING: Flight {self.flight_num} is delayed by {self.delay_time} mins!")
        else:
            print(f"Flight {self.flight_num} is on time or has a minor delay.")


df = pd.DataFrame(arrivals_data)
df["Minutes_Delayed"] = df["Minutes_Delayed"].fillna(0)

delayed_flights = df[df["Minutes_Delayed"] > 30]

if not delayed_flights.empty:
    most_delayed_row = delayed_flights.loc[delayed_flights["Minutes_Delayed"].idxmax()]


    severe_flight = Flight(most_delayed_row["Flight_Number"], most_delayed_row["Minutes_Delayed"])
    severe_flight.check_severity()

    # 5. APPENDING (Pandas): Create a single-row DataFrame for logging
    log_entry = pd.DataFrame([most_delayed_row])
    log_filename = "severe_delays_log.csv"

    # Check if log file exists to decide on reading/concatenating
    if os.path.exists(log_filename):
        existing_log = pd.read_csv(log_filename)
        updated_log = pd.concat([existing_log, log_entry], ignore_index=True)
    else:
        updated_log = log_entry

    # Save the updated log
    updated_log.to_csv(log_filename, index=False)
    print(f"\nLogged {severe_flight.flight_num} to '{log_filename}'.")
else:
    print("No severe delays found today.")

print("\n--- Final Arrivals Table ---")
print(df)
