# Asynchronous programming is when
# a function runs while another is
# sleeping or being 'unproductive' by using await

import asyncio

async def main():
    # this will make an async task that called other_function()
    task = asyncio.create_task(other_function())
    print("a")
    await asyncio.sleep(5)
    print("b")
    # in order to get any return value you need to await the task
    return_value = await task
    print(f"return value was {return_value}")



async def other_function():
    print("1")
    await asyncio.sleep(2)
    print("2")
    return 10


asyncio.run(main())
