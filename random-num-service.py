import asyncio
import aiohttp
import time
import random

headers = {
    "Synx-Cat": "1",
    "Content-Type": "application/x-www-form-urlencoded",
}


# async await for response
async def output(number: int):
    data = {
        "token": "aToken_36d8715e3531fd8e8c01fcbfd26bf5af1908e14f15014d2d14817b568bc0bb0e",
        "objectID": "1",
        "txt": number,
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://randoms-squad.cioty.com/hytte-sensor-test-first",
            headers=headers,
            data=data,
        ) as response:
            print(await response.text())


def main():
    while True:
        num = random.randint(1, 100)
        asyncio.run(output(num))
        print(f"Sent: {num}")
        time.sleep(10)


if __name__ == "__main__":
    main()
