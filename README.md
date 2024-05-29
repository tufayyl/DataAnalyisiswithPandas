# Data Analysis and Visualization with Python

This repository contains a Python script for data analysis and visualization. The script connects to a MySQL database, reads data from an Excel file into Pandas, and conducts analysis using SQL queries. Interactive visualizations, including line and bar graphs, are generated using Plotly Express.

## Features

- **Database Interaction**: Connects to a MySQL database to store and retrieve data.
- **Data Handling**: Reads data from an Excel file into a Pandas DataFrame and creates a corresponding database table.
- **Data Analysis**: Executes SQL queries for data analysis, including aggregation and grouping.
- **Visualization**: Generates interactive visualizations using Plotly Express, including line and bar graphs.
- **Customization**: The script allows for customization of graph titles, axis labels, and more.

## Getting Started

1. Clone this repository to your local machine.
2. Ensure you have Python and the necessary libraries installed (`pandas`, `mysql-connector-python`, `plotly`, `openpyxl`, `sqlalchemy`).
3. Update the MySQL connection details in the script to match your database credentials.
4. Place your data file (in Excel format) in the specified directory or update the file path in the script.
5. Run the Python script (`main.py`) and observe the generated visualizations.

## Requirements

- Python 3.x
- Pandas
- MySQL Connector
- Plotly Express
- Openpyxl
- SQLAlchemy
