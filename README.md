# Agricultural Commodities API

This project provides an API that serves data related to agricultural commodities. Built with Flask and backed by a Postgres database, this API offers endpoints that enable users to query data based on various parameters like variable codes, product codes, year, and municipality codes.

## Features

- Retrieve agricultural commodity data based on:
  - Variable codes
  - Temporary crop product codes
  - Year
  - Municipality codes
- Powered by Flask for the API and SQLAlchemy for database interactions.
- Swagger documentation for endpoint details.

## Installation & Usage

- This API is defined for use in the cloud and therefore requires data available in a database. Below are the instructions for running the local API, but without the availability of data.

1. **Clone the Repository**
   ```
   git clone https://github.com/SamuelOliveirads/agricultural_production_analysis.git
   ```

2. **Navigate to the Directory**
   ```
   cd agricultural_commodities_api
   ```

3. **Install Dependencies**
   Make sure you have Python and pip installed.
   ```
   pip install -r requirements.txt
   ```

4. **Set Up the Database**
   Ensure you have Postgres set up and a database ready for the project. Update the database connection string accordingly.

5. **Run the API**
   ```
   waitress-serve --listen=0.0.0.0:5000 api:app
   ```

6. **Access the API**
   By default, the API will be accessible at `http://127.0.0.1:5000/`.

7. **Swagger UI**
   You can view the interactive API documentation by navigating to `http://127.0.0.1:5000/apidocs`.

## API Endpoints

- **Get Commodities Data**
  - **URL:** `/api/commodities`
  - **Method:** `GET`
  - **Query Parameters:** 
    - `cod_variavel`
    - `cod_produto_lavouras_temporarias`
    - `cod_ano`
    - `cod_municipio`
  - **Response:** Returns a JSON array with the filtered commodities data based on the query parameters.
