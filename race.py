import httpx
import asyncio
import random


method="post"
count=10


url = 'https://www..com/redeem'

headers = {
    "Host": "www.test.com",
    "Connection": "keep-alive",
    "Content-Length": "110",
    "Cache-Control": "max-age=0",
    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "Origin": "https://www..com",
    "DNT": "1",
    "Upgrade-Insecure-Requests": "1",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://www..com/redeem",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en",
    "Cookie": ''
}



body = [
''
]


request_count = 0


async def send_request(client, method):
    global request_count
    try:
        random_index = random.randint(0, len(body) - 1)
        chosen_body = body[random_index]

        if method.lower() == "post":
            response = await client.post(url,  headers=headers, data=chosen_body)
        elif method.lower() == "get":
            response = await client.get(url, headers=headers)
        else:
            raise ValueError("Invalid HTTP method specified")

        response.raise_for_status()

        request_count += 1
        print("==================================")
        print(f"[*] Request #{request_count} - Method: {method.upper()}")
        print("[*] Chosen Body:", random_index)
        print(response.text)
        print("==================================")
    except Exception as e:
        print(f"[!] Request failed: {e}")


async def main():
    async with httpx.AsyncClient() as client:
        tasks = [asyncio.create_task(send_request(client, method=method)) for i in range(count)]
        await asyncio.gather(*tasks)



if __name__ == "__main__":
    asyncio.run(main())
