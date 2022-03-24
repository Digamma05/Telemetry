import asyncio
from websockets import serve


def start_server(PORT: int, get_v):
    async def echo(websocket):
        async for message in websocket:
            await websocket.send(get_v)

    async def main():
        async with serve(echo, "localhost", PORT):
            await asyncio.Future()

    asyncio.run(main())
