import asyncio
import websockets
import json
import argparse

parser = argparse.ArgumentParser(description="Mavsim commands")
parser.add_argument('--command',type=str,help='either land or takeoff')
args = parser.parse_args()

async def send_message(message):
    async with websockets.connect(
        "ws://127.0.0.1:8000") as websocket:
        await websocket.send(message)
        print(f"> {message}")



commander = {"command": args.command}

asyncio.get_event_loop().run_until_complete(send_message(json.dumps(commander)))