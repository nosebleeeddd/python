# Asynchronous programming is when
# a function runs while another is
# sleeping or being 'unproductive' by using await

import asyncio

async def main():
    # this will make an async task that called other_function()
    task = asyncio.create_task(other_function())
    print("a")
    await asyncio.sleep(1)
    print("b")
    await task


async def other_function():
    print("1")
    await asyncio.sleep(2)
    print("2")

asyncio.run(main())
