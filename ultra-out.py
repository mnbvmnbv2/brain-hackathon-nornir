import asyncio
import aiohttp
import time
import serial

ser = serial.Serial("COM3", 9600, timeout=1)

headers = {
    "Synx-Cat": "1",
    "Content-Type": "application/x-www-form-urlencoded",
}


# async await for response
async def to_hive(number: int):
    data = {
        "token": "aToken_36d8715e3531fd8e8c01fcbfd26bf5af1908e14f15014d2d14817b568bc0bb0e",
        "objectID": "1",
        "dist": number,
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://randoms-squad.cioty.com/ultra-sound-sensor",
            headers=headers,
            data=data,
            # verify=False,
        ) as response:
            print(await response.text())


def main():
    while True:
        # weekdays with arrival coefficient
        s = ser.read(1000)

        asyncio.run(to_hive(str(s)))
        print(f"Sent: {s}")
        time.sleep(5)


if __name__ == "__main__":
    main()
