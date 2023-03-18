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
        weekdays = [
            ("Monday", 1),
            ("Tuesday", 1),
            ("Wednesday", 1),
            ("Thursday", 1),
            ("Friday", 1),
            ("Saturday", 1),
            ("Sunday", 1),
        ]
        # month with arrival coefficient
        months = [
            ("January", 1),
            ("February", 1),
            ("March", 1),
            ("April", 1),
            ("May", 1),
            ("June", 1),
            ("July", 1),
            ("August", 1),
            ("September", 1),
            ("October", 1),
            ("November", 1),
            ("December", 1),
        ]

        # times with arrival coefficient
        times = [
            ("00:00", 1),
            ("01:00", 1),
            ("02:00", 1),
            ("03:00", 1),
            ("04:00", 1),
            ("05:00", 1),
            ("06:00", 1),
            ("07:00", 1),
            ("08:00", 1),
            ("09:00", 1),
            ("10:00", 1),
            ("11:00", 1),
            ("12:00", 1),
            ("13:00", 1),
            ("14:00", 1),
            ("15:00", 1),
            ("16:00", 1),
            ("17:00", 1),
            ("18:00", 1),
            ("19:00", 1),
            ("20:00", 1),
            ("21:00", 1),
            ("22:00", 1),
            ("23:00", 1),
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
        time.sleep(10)


if __name__ == "__main__":
    main()
