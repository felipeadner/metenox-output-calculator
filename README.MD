Metenox Output Calculator

This project calculates the monthly output of minerals based on data provided in a CSV file. It includes a Python script for the calculation logic and a web interface built with Flask to interact with the script.

## Project Structure

- **`app.py`**: Contains the main logic for processing the CSV file and calculating the output based on the data.
- **`templates/index.html`**: A simple HTML form that allows the user to upload a CSV file.
- **`requirements.txt`**: Lists the required Python packages for the project.

---

## Features

- **CSV File Upload**: Upload a CSV file containing the required data.
- **Mineral Calculation**: Calculates the number of units of different minerals based on their proportions.
- **Downloadable Results**: Processed data is returned in the form of a downloadable CSV file.

---

## Required Libraries

To run the project, you will need to install the necessary dependencies. The required libraries are listed in the `requirements.txt` file:

1. Flask
2. pandas

Install them with:

pip install -r requirements.txt

---

## Code Overview

### Main Calculation Code

The main logic of the project calculates the number of mineral units based on the given proportions and utilization rate.

```python
import pandas as pd

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

```

### Flask Web Application Code

This is the code for the Flask web application that allows the user to upload a CSV file and receive a processed CSV file as the result.

from flask import Flask, request, render_template, send_file
import pandas as pd
from io import StringIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_file():
    file = request.files['file']
    df = pd.read_csv(file)
    # Processing logic as in the main code
    result = df.to_csv(index=False)
    return send_file(StringIO(result), attachment_filename="result.csv", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

HTML Form (index.html)

### The HTML form allows users to upload the CSV file:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload CSV File</title>
</head>
<body>
    <h1>Upload CSV File</h1>
    <form action="/process" method="post" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>


---

## How to Run

### 1. Install Dependencies

Make sure to install the required dependencies first:

pip install -r requirements.txt

### 2. Start the Flask Application

Run the Flask application with the following command:

python app.py

This will start the web application on http://127.0.0.1:5000/.

### 3. Upload the CSV File

Go to the application in your browser and upload the CSV file. The file should have the following columns:

System: The name of the system.

Planet: The name of the planet.

Moon: The name of the moon.

Utilization Rate: The percentage of the moon's volume used for mining.

Mineral Name1-4: The names of the minerals.

Mineral Proportion1-4: The proportions of each mineral.


### 4. Download the Result

Once the file is uploaded, the system will process it, calculate the output, and return the result as a downloadable CSV file.


---

## CSV File Format

The CSV file should have the following columns:

System: Name of the system.

Planet: Name of the planet.

Moon: Name of the moon.

Utilization Rate: Percentage of the moon's total volume used.

Mineral Name1-4: Names of the minerals.

Mineral Proportion1-4: Proportions of each mineral.
