import asyncio
import aiohttp
import time
import re

headers = {
    "Synx-Cat": "4",
    "Content-Type": "application/x-www-form-urlencoded",
}

data = {
    "token": "aToken_36d8715e3531fd8e8c01fcbfd26bf5af1908e14f15014d2d14817b568bc0bb0e",
    "objectID": "1",
}

# async await for response
async def getter():
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://randoms-squad.cioty.com/patient-arrival",  # URL TO LISTEN TO
            headers=headers,
            data=data,
        ) as response:
            return await response.text()


def main():
    while True:
        response = asyncio.run(getter())
        # scrape data from response
        print(response)
        # response = re.findall(r"sample=(\d+)", response)
        time.sleep(10)


if __name__ == "__main__":
    main()
