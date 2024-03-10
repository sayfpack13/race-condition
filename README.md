# Race Condition Script

This script sends parallel HTTP requests but does not specifically demonstrate a race condition scenario where the outcome depends on the timing of the requests, such as with the "last byte wins" scenario.


# **Caution:**
This script is provided for educational purposes only. Race conditions can lead to unpredictable behavior and should be handled with caution. It is important to understand the implications of race conditions in concurrent programming.

# **Note:**
Do not use this script on platforms like Twitter or Facebook, as it may violate their terms of service.

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
