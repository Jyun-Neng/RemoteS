import asyncio
import websockets
import cv2
import numpy as np

async def server(websocket, path):
    image_bytes = await websocket.recv()
    size = 720, 1280
    image = np.fromstring(image_bytes, np.uint8).reshape(size)
    cv2.imwrite('img.png', image)
    
    greeting = "Received!!"
    send = "Done!"
    await websocket.send(send)
    print("> {}".format(greeting))

start_server = websockets.serve(server, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
