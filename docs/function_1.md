# Function 1

## Original Code
```python
def fetch_air_quality(zip_code="20002"):
    """Fetches air quality data for a given ZIP code using AirNow API."""
    try:
        api_request = requests.get(
            f"http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip_code}&distance=10&API_KEY=YOUR_API_KEY"
        )
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
        return city, quality, category
    except Exception as e:
        return "Error", "N/A", "N/A"
```

## Generated Documentation
```python
Here is the comprehensive documentation for the `fetch_air_quality` function:

**Purpose Summary**: The `fetch_air_quality` function fetches air quality data for a given ZIP code using the AirNow API. It returns the city, current AQI, and category of air quality for the specified ZIP code.

**Parameter Explanations**:

* `zip_code`: The ZIP code for which to fetch air quality data. If left blank, it will use the default value of "20002".

**Return Value**: A tuple containing the city, current AQI, and category of air quality for the specified ZIP code. The return values are:

* `city`: The name of the city where the ZIP code is located.
* `quality`: The current Air Quality Index (AQI) for the city. This value ranges from 0 to 500, with higher values indicating poorer air quality.
* `category`: The category of air quality for the city, which can be either "Good", "Moderate", "Unhealthy for Sensitive Groups", or "Unhealthy".

**Example**: To fetch air quality data for a specific ZIP code, you can use the following code:
```python
city, quality, category = fetch_air_quality("21301")
print(f"The current air quality in Baltimore is {quality}.")
```
This will fetch the air quality data for the ZIP code "21301" and print a message indicating the current AQI.

**Output as a Docstring in Python Format**:
```python
def fetch_air_quality(zip_code="20002"):
    """Fetches air quality data for a given ZIP code using AirNow API.

    :param zip_code: The ZIP code for which to fetch air quality data. If left blank, it will use the default value of "20002".
    :return: A tuple containing the city, current AQI, and category of air quality for the specified ZIP code.
    """
    try:
        api_request = requests.get(
            f"http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip_code}&distance=10&API_KEY=YOUR_API_KEY"
        )
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
        return city, quality, category
    except Exception as e:
        return "Error", "N/A", "N/A"
```
```

## Prompt Used
```
System: You are an expert Python developer specializing in generating clean, clear, and helpful documentation.
User: 
Please generate comprehensive documentation for the following Python function. Include:

- A brief purpose summary
- Parameter explanations
- Return value
- An example if possible
- Output as a docstring in Python format

Code:
def fetch_air_quality(zip_code="20002"):
    """Fetches air quality data for a given ZIP code using AirNow API."""
    try:
        api_request = requests.get(
            f"http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip_code}&distance=10&API_KEY=YOUR_API_KEY"
        )
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
        return city, quality, category
    except Exception as e:
        return "Error", "N/A", "N/A"

Assistant:
```