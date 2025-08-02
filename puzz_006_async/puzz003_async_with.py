"""
Оператор async with в Python предназначен для работы с асинхронными контекстными менеджерами. Он позволяет выполнять
асинхронные операции входа и выхода из контекста, аналогично тому, как with работает с синхронными контекстными
менеджерами.
"""
import asyncio

"""
В данном случае, выводит сообщение и имитирует небольшую задержку с помощью asyncio.sleep.
__aexit__ - асинхронная версия метода __exit__, выполняется при выходе из контекста. Также выводит сообщение, имитирует 
задержку и обрабатывает возможные исключения.
async with AsyncContextManager() as cm: - использование async with. При этом сначала вызывается __aenter__, затем 
выполняется код внутри блока with, и в конце вызывается __aexit__.
"""


class AsyncContextManager:
    async def __aenter__(self):
        print("Start async context... ")
        await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Finished async context...")
        await asyncio.sleep(1)
        if exc_type:
            print(f"Error: {exc_type}, {exc_val}, {exc_tb}")
        return False


async def main():
    async with AsyncContextManager() as cm:
        print("Process async context... ")
        await asyncio.sleep(1)
    print("After async context")


if __name__ == "__main__":
    asyncio.run(main())
