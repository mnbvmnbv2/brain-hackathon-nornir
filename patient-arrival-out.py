import asyncio
import aiohttp
import time
import numpy as np

headers = {
    "Synx-Cat": "1",
    "Content-Type": "application/x-www-form-urlencoded",
}


# async await for response
async def to_hive(number: int):
    data = {
        "token": "aToken_36d8715e3531fd8e8c01fcbfd26bf5af1908e14f15014d2d14817b568bc0bb0e",
        "objectID": "1",
        "sample": number,
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://randoms-squad.cioty.com/patient-arrival",
            headers=headers,
            data=data,
            # verify=False,
        ) as response:
            print(await response.text())


def main():
    while True:
        # weekdays with arrival coefficient
        # weekdays = [
        #     ("Monday", 1),
        #     ("Tuesday", 1),
        #     ("Wednesday", 1),
        #     ("Thursday", 1),
        #     ("Friday", 1),
        #     ("Saturday", 1),
        #     ("Sunday", 1),
        # ]
        weekdays = [
            (0, 1),
            (1, 1),
            (2, 1),
            (3, 1),
            (4, 2),
            (5, 2),
            (6, 1),
        ]
        # month with arrival coefficient
        # months = [
        #     ("January", 1),
        #     ("February", 1),
        #     ("March", 1),
        #     ("April", 1),
        #     ("May", 1),
        #     ("June", 1),
        #     ("July", 1),
        #     ("August", 1),
        #     ("September", 1),
        #     ("October", 1),
        #     ("November", 1),
        #     ("December", 1),
        # ]
        months = [
            (0, 1),
            (1, 1),
            (2, 1),
            (3, 1),
            (4, 1),
            (5, 1),
            (6, 1),
            (7, 1),
            (8, 1),
            (9, 1),
            (10, 1),
            (11, 1),
        ]

        # times with arrival coefficient
        times = [
            (3600 * 0, 2),
            (3600 * 1, 3),
            (3600 * 2, 1),
            (3600 * 3, 1),
            (3600 * 4, 1),
            (3600 * 5, 1),
            (3600 * 6, 1),
            (3600 * 7, 1),
            (3600 * 8, 1),
            (3600 * 9, 1),
            (3600 * 10, 1),
            (3600 * 11, 1),
            (3600 * 12, 1),
            (3600 * 13, 1),
            (3600 * 14, 1),
            (3600 * 15, 1),
            (3600 * 16, 1),
            (3600 * 17, 1),
            (3600 * 18, 1),
            (3600 * 19, 1),
            (3600 * 20, 1),
            (3600 * 21, 1),
            (3600 * 22, 1),
            (3600 * 23, 1),
        ]
        weekday_idx = np.random.randint(0, len(weekdays))
        weekday = weekdays[weekday_idx]
        month_idx = np.random.randint(0, len(months))
        month = months[month_idx]
        time_idx = np.random.randint(0, len(times))
        _time = times[time_idx]

        arrival_rate_lam = 1 * weekday[1] * month[1] * _time[1]
        arrival_rate = np.random.poisson(lam=arrival_rate_lam)

        output = {
            "weekday": weekday[0],
            "month": month[0],
            "time": _time[0],
            "arrivalrate": arrival_rate,
        }

        asyncio.run(to_hive(str(output)))
        print(f"Sent: {output}")
        time.sleep(5)


if __name__ == "__main__":
    main()
