import asyncio
import aiohttp
import time

headers = {
    "Synx-Cat": "4",
    "Content-Type": "application/x-www-form-urlencoded",
}

data = {
    "token": "aToken_36d8715e3531fd8e8c01fcbfd26bf5af1908e14f15014d2d14817b568bc0bb0e",
    "objectID": "1",
}

# async await for response
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://randoms-squad.cioty.com/hytte-sensor-test-first",  # URL TO LISTEN TO
            headers=headers,
            data=data,
        ) as response:
            print(await response.text())


if __name__ == "__main__":
    asyncio.run(main())
    time.sleep(10)
    print("end")
