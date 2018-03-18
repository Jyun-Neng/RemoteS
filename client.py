import asyncio
import websockets
import cv2
from camera import detect


async def images(frame, size):
    async with websockets.connect('ws://localhost:8765') as websocket:
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        image = cv2.resize(frame, size)
        image_bytes = image.tobytes()
        print('> Send!')
        await websocket.send(image_bytes)

        greeting = await websocket.recv()
        print("< {}".format(greeting))

frame = detect()
size = 1280, 720
asyncio.get_event_loop().run_until_complete(images(frame, size))
