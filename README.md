# Race Condition Script

This script simulates a basic race condition scenario using Python's asyncio library and the httpx library. Race conditions occur when the outcome of a program depends on the relative timing of events that are not properly synchronized. In this script, multiple asynchronous HTTP requests are sent to a specified URL concurrently, potentially leading to unpredictable behavior due to the interleaving of their execution.

## Usage

1. **Install Dependencies:**
   ```bash
   pip install httpx

## Requirements

- Python 3.7+
- [httpx](https://github.com/encode/httpx)

## Configuration

- **URL (`url`):**
  Modify the `url` variable to specify the target URL where the requests will be sent.

- **HTTP Method (`method`):**
  Set the `method` variable to either `"post"` or `"get"` to determine the type of HTTP request to be sent.

- **Request Count (`count`):**
  Adjust the `count` variable to specify the number of concurrent requests to be sent.

- **Headers (`headers`):**
  Customize the `headers` dictionary to include any additional headers required for your requests.

- **Request Body (`body`):**
  Modify the `body` list to include different request bodies. Currently, it contains an empty string, but you can add more bodies if needed.

## Usage

1. **Dependencies Installation:**
   Ensure you have the `httpx` library installed. If not, you can install it using pip:
   ```bash
   pip install httpx
