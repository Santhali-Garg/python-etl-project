# Python ETL Project using Pandas

## Project Overview

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline developed using **Python and Pandas**.

The pipeline reads customer data from a CSV file, performs data cleaning and transformation, and generates a cleaned CSV output file.

## ETL Flow

**CSV Source → Pandas DataFrame → Data Cleaning → Data Transformation → CSV Output**

## Technologies Used

* Python
* Pandas
* CSV
* GitHub

## Source Data

The input file `customers.csv` contains customer information such as:

* Customer ID
* Name
* City
* Age
* Salary

## Transformations Performed

1. Read the source CSV using Pandas `read_csv()`.
2. Loaded the data into a Pandas DataFrame.
3. Removed leading/trailing spaces from customer names.
4. Standardized city names by removing spaces and converting them to uppercase.
5. Created a derived `salary_band` column using a Python lambda function.
6. Exported the transformed data to `customers_cleaned.csv`.

## Project Structure

```text
python-etl-project/
│
├── data/
│   ├── customers.csv
│   └── customers_cleaned.csv
│
├── src/
│   └── customers.py
│
└── README.md
```

## How to Run

Navigate to the `src` folder and run:

```bash
python customers.py
```

The transformed output will be generated as:

```text
data/customers_cleaned.csv
```

## Key Learning

This project demonstrates practical beginner-level Python ETL concepts including:

* Pandas DataFrames
* CSV file handling
* Data cleansing
* String transformations
* Derived columns
* Lambda functions
* Exporting transformed data

## Future Enhancements

The pipeline can be extended with:

* Null/duplicate validation
* Data quality checks
* Error handling
* Additional transformations
* Database loading
* Automated ETL scheduling
