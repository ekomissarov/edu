# https://www.youtube.com/watch?v=LO61F07s7gw&list=PLlWXhlUMyooawilqK4lPXRvxtbYiw34S8&index=7

# важно понимание событийных циклов, это главный элемент любой асинхронной программы
# он менеджер/планировщик задач. Суть его работы заключается в реагировании на какие-то происходящие события
# (чтобы блокирующие вызовы перестали быть таковыми)
# Написание событийного цикла это в принципе повторяющаяся, но довольно не тривиальная задача
# Это та задача, которую было бы не плохо усовершенствовать => asyncio

# asyncio модуль который в большей степени (но не только) предназначен для создания событийных циклов
# список задач -> как-то обрабатывать в событийном цикле (в наших примеров событиями были изменения состояний сокетов)
# Во всех примерах мы каждый сокет связывали с некоторой функцией обработчиком и когда сокет менял свое состояния,
# становился доступен для чтения или записи, мы вызывали соответствующую ему функцию обработчик
# это был или callback или генераторная функция

# в модуле asyncio в событийном цикле крутятся экземпляры класса task, которые являются контейнерами для корутин
# Event Loop:
#       coroutine > Task(Future)
#       экземпляры класса Task описывают те дейстивя, которые должны выполнятся асинхронно

# python 3.6

import asyncio

async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)  # не блокирующая функция

async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print(f"{count} seconds have passed")
        count += 1
        await asyncio.sleep(1)  # не блокирующая функция

async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())
    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()