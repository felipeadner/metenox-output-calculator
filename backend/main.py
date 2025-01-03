import pandas as pd

# Function to calculate the number of units of each type
def calculate_units(moon_utilization_rate_percent, mineral1_proportion, mineral2_proportion, mineral3_proportion, mineral4_proportion):
    total_volume = (moon_utilization_rate_percent / 100) * 30000
    mineral1_volume = (mineral1_proportion / 100) * total_volume
    mineral2_volume = (mineral2_proportion / 100) * total_volume
    mineral3_volume = (mineral3_proportion / 100) * total_volume
    mineral4_volume = (mineral4_proportion / 100) * total_volume
    mineral1_units = mineral1_volume / 10
    mineral2_units = mineral2_volume / 10
    mineral3_units = mineral3_volume / 10
    mineral4_units = mineral4_volume / 10
    return {
        "Mineral #1": int(mineral1_units),
        "Mineral #2": int(mineral2_units),
        "Mineral #3": int(mineral3_units),
        "Mineral #4": int(mineral4_units)
    }

# Function to calculate the number of units in a month
def calculate_monthly_units(moon_utilization_rate_percent, mineral1_proportion, mineral2_proportion, mineral3_proportion, mineral4_proportion):
    units_per_rate = calculate_units(moon_utilization_rate_percent, mineral1_proportion, mineral2_proportion, mineral3_proportion, mineral4_proportion)
    hours_per_month = 24 * 30
    monthly_units = {type: quantity * hours_per_month for type, quantity in units_per_rate.items()}
    return monthly_units

# Function to validate inputs
def validate_input(value, allow_zero=False, integer=False):
    try:
        if pd.isna(value):
            if allow_zero:
                return 0 if integer else 0.0
            raise ValueError("Missing value")
        value = str(value).replace(",", ".")
        value_float = float(value)
        if integer:
            value_int = int(value_float)
            if value_int <= 0:
                raise ValueError
            return value_int
        else:
            value_float = round(value_float, 2)
            if value_float < 0 or (value_float == 0 and not allow_zero):
                raise ValueError
            return value_float
    except ValueError:
        raise ValueError(f"Invalid input: '{value}'. Please enter a valid number.")

if __name__ == "__main__":
    file_path = input("Enter the path of the spreadsheet (CSV): ")
    try:
        df = pd.read_csv(file_path)

        expected_columns = [
            "System", "Planet", "Moon", "Utilization Rate", "Mineral Name1", "Mineral Proportion1",
            "Mineral Name2", "Mineral Proportion2", "Mineral Name3", "Mineral Proportion3",
            "Mineral Name4", "Mineral Proportion4"
        ]

        if not all(col in df.columns for col in expected_columns):
            raise ValueError("The spreadsheet must contain the following columns: " + ", ".join(expected_columns))

        results = []

        for index, row in df.iterrows():
            try:
                system = str(row["System"]).strip()
                planet = validate_input(row["Planet"], integer=True)
                moon = validate_input(row["Moon"], integer=True)
                utilization_rate = validate_input(row["Utilization Rate"])
                mineral1_proportion = validate_input(row["Mineral Proportion1"])
                mineral2_proportion = validate_input(row["Mineral Proportion2"])
                mineral3_proportion = validate_input(row["Mineral Proportion3"])
                mineral4_proportion = validate_input(row["Mineral Proportion4"], allow_zero=True)

                mineral1_name = row["Mineral Name1"]
                mineral2_name = row["Mineral Name2"]
                mineral3_name = row["Mineral Name3"]
                mineral4_name = row["Mineral Name4"]

                monthly_result = calculate_monthly_units(
                    utilization_rate, mineral1_proportion, mineral2_proportion, mineral3_proportion, mineral4_proportion
                )

                results.append({
                    "System": system,
                    "Planet": planet,
                    "Moon": moon,
                    "Mineral Name1": mineral1_name,
                    "Monthly Result Mineral1": monthly_result["Mineral #1"],
                    "Mineral Name2": mineral2_name,
                    "Monthly Result Mineral2": monthly_result["Mineral #2"],
                    "Mineral Name3": mineral3_name,
                    "Monthly Result Mineral3": monthly_result["Mineral #3"],
                    "Mineral Name4": mineral4_name,
                    "Monthly Result Mineral4": monthly_result["Mineral #4"]
                })

            except ValueError as e:
                print(f"Error in row {index + 1}: {e}")

        df_results = pd.DataFrame(results)
        output_path = "results.csv"
        df_results.to_csv(output_path, index=False)
        print(f"Results saved in the file: {output_path}")

    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
    except ValueError as e:
        print(e)