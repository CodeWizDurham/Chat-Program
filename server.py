# server.py

import asyncio
import websockets

async def handle_websocket(websocket, path):
    print("Client connected")
    try:
        # Keep the connection open to handle incoming messages
        async for message in websocket:
            print(f"Received message: {message}")

            # Echo the received message back to the client
            await websocket.send(f"Echo: {message}")
    except websockets.exceptions.ConnectionClosedError:
        pass
    finally:
        print("Client disconnected")

# Create a WebSocket server
start_server = websockets.serve(handle_websocket, "localhost", 8765)

# Run the server indefinitely
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
