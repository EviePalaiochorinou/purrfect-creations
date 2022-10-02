
# Purrfect Creations

A fullstack metrics dashboard that displays key figures of a small business's order data.  

This project is made with:  
- Python3
- FastAPI
- React
- Airtable API data

This project features:
- Testing with Pytest

### Specifications  

Key figures on dashboard:  

- Total Orders

- Total Orders this month

- Number of orders in progress

- Revenue

- A list of the most recent few orders

- A list of all placed orders

## Running The Project Locally

### Installation

1. Clone this repository  
    ```sh
   git clone https://github.com/EviePalaiochorinou/purrfect-creations.git
   ```

2. Activate your virtual environment

3. Install the requirements
   ```sh
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```  
    
### Usage

In the main directory:  
- Start the back-end server
  ```sh
  uvicorn main:app --reload
  ```  
- View the endpoint results
  ```sh
  http://127.0.0.1:8000/dashboard
  ``` 
- View your Swagger UI and test the endpoints manually
  ```sh
  http://127.0.0.1:8000/docs
  ``` 
In the dashboard directory:
- Go into the dashboard directory
  ```sh
  cd dashboard/
  ```
- Start the front-end server
  ```sh
  npm start
  ```
- View the dashboard
  ```sh
  http://localhost:3000
  ```
### Testing

You can run the tests using:
```shell script
pytest -s -v
```  

## Implementation  

The following endpoints were built:  

GET /dashboard  

The endpoint gets data from the Airtable API ("https://api.airtable.com/v0/...").  
It returns all data from one endpoint in an aggregated form.  
This is so that we only make one call to the external API, to make our app faster. When the dashboard in the front-end refreshes, our back-end needs to make only one call to the extrernal API. It is faster to transform the data in memory than over the network.

### Error Handling

- An exception is raised (at the handler level) when the external API is unreachable. 

### Testing  

- In order to test my application, for every API endpoint, I first write a simple handler test with the expectation of successful HTTP response.  
- I chose to go with integration tests over unit tests, so requests tests were the best kind to go forward with.   
- Ideally, here I would mock the Airtable Api Client in order to write more tests that do not make real calls to the external api. This way I can test if I get the responses I am expecting.
- Future work includes to aim for 100% test coverage and include tests for all edge cases.  

