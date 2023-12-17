import asyncio
import time
import multiprocessing


def fibonacci(i):
    if i in [0, 1]:
        return i
    if i == 2:
        return 1
    return fibonacci(i - 1) + fibonacci(i - 2)


async def async_fibonacci(i):
    if i in [0, 1]:
        return i
    if i == 2:
        return 1
    return await async_fibonacci(i - 1) + await async_fibonacci(i - 2)


def factorial(num):
    if num in [0, 1]:
        return 1
    return num * factorial(num - 1)


async def async_factorial(num):
    if num == 0:
        return 1
    return num * await async_factorial(num - 1)


def square(num):
    return num**2


async def async_square(num):
    return num**2


def cube(num):
    return num**3


async def async_cube(num):
    return num**3


def multiprocessing_calc(max_num):
    start = time.time()
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        fibs = pool.map(fibonacci, range(1, max_num))
        facts = pool.map(factorial, range(1, max_num))
        squares = pool.map(square, range(1, max_num))
        cubes = pool.map(cube, range(1, max_num))
    print("fibs: ", fibs, "\nfacts:", facts, "\nsquares:", squares, "\ncubes:", cubes)
    print(
        f"Execution time multiprocessing_calc --> {round((time.time() - start), 5)}\n"
    )


async def async_calc(max_num):
    start = time.time()
    coroutines = {"fibs": [], "facts": [], "squares": [], "cubes": []}

    for num in range(1, max_num):
        coroutines["fibs"].append(asyncio.create_task(async_fibonacci(num)))
        coroutines["facts"].append(asyncio.create_task(async_factorial(num)))
        coroutines["squares"].append(asyncio.create_task(async_square(num)))
        coroutines["cubes"].append(asyncio.create_task(async_cube(num)))

    fibs = await asyncio.gather(*coroutines["fibs"])
    facts = await asyncio.gather(*coroutines["facts"])
    squares = await asyncio.gather(*coroutines["squares"])
    cubes = await asyncio.gather(*coroutines["cubes"])
    print("fibs: ", fibs, "\nfacts:", facts, "\nsquares:", squares, "\ncubes:", cubes)
    print(f"Execution time async_calc --> {round((time.time() - start), 5)}\n")


if __name__ == "__main__":
    max_count = 11
    multiprocessing_calc(max_count)
    asyncio.run(async_calc(max_count))