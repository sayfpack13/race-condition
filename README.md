# Race Condition Script

This script simulates a basic race condition scenario using Python's asyncio library and the httpx library. Race conditions occur when the outcome of a program depends on the relative timing of events that are not properly synchronized. In this script, multiple asynchronous HTTP requests are sent to a specified URL concurrently, potentially leading to unpredictable behavior due to the interleaving of their execution.

## Usage

1. **Install Dependencies:**
   ```bash
   pip install httpx
