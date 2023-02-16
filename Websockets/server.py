#!/usr/bin/env python3
import asyncio
import websockets
import json


async def websocket_callback(websocket,path):
    """the callback function for 
    the websocket service"""
    message = await websocket.recv()                            #wait for the service to recieve a command
    message = json.loads(message)                          #take the message from json to a string
    await websocket.send("response message")                        #send a response to the client
    print("Command ",message["command"], " has been published")
    return "Done"
    


def main(args=None):
    """main function that will run on terminal"""
    asyncio.get_event_loop().run_until_complete(server_)
    asyncio.get_event_loop().run_forever()



if __name__ == "__main__":
    server_ = websockets.serve(
    websocket_callback, "127.0.0.1",8000)
    main()