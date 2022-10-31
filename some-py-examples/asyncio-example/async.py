import asyncio
import aiohttp
import requests
from time import time

def get_file_sync(url):
    r = requests.get(url, allow_redirects=True)
    return r

def write_file_sync(response):
    filename = response.url.split("/")[-1]
    with open(filename, "wb") as file:
        file.write(response.content)


def main_sync():
    url = "https://loremflickr.com/320/240"
    t0 = time()
    for i in range(10):
        write_file_sync(get_file_sync(url))

    print(f"TIME: {time()-t0} sec")
###############################################################

def write_image(data):
    filename = "file-{}.jpg".format(int(time()*1000))
    with open(filename, "wb") as file:
        file.write(data)
    # WTF почему ф-ия синхронная? asyncio не предоставляет возможности для асинхронной работы с файлами
    # такая возможность есть у библиотеки Curio, aiofiles (работает с потоками)
    # здесь поиспользуем синхронную ф-ию

async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data)  # обычно это плохая идея, т.к. синхронный код может заблокировать асинхронный поток

async def main():
    url = "https://loremflickr.com/320/240"
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    # main_sync()
    t0 = time()
    asyncio.run(main())
    print(f"TIME: {time()-t0} sec")
