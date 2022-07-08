#!/usr/bin/env python3
# Distributed under CC0 1.0 Universal (CC0 1.0) Public Domain Dedication.

"""
This application simulates the plant controlled by the thermostat node: it takes a voltage command,
runs a crude thermodynamics simulation, and publishes the temperature (i.e., one subscription, one publication).
"""

import time
import asyncio
import uavcan.si.unit.voltage
import uavcan.si.sample.temperature
import uavcan.time
import pycyphal
from pycyphal.application.heartbeat_publisher import Health
from pycyphal.application import make_node, NodeInfo, register
from pycyphal.application.plug_and_play import CentralizedAllocator
from pycyphal.application.node_tracker import  NodeTracker
from uavcan.register import Access_1, Name_1
from pycyphal.application.register import ValueProxy, Value
from pycyphal.application.register import Natural16
import logging

logging.basicConfig(level=logging.WARNING)

UPDATE_PERIOD = 2.0

def tracker(nodeID, old_entry, new_entry):
    print("TRACKER INFO", nodeID, old_entry, new_entry)
          
          
async def main() -> None:

    with make_node(NodeInfo(name="org.opencyphal.pycyphal.demo.master"), "master.db") as node:

        ca=CentralizedAllocator(node)
        nt=NodeTracker(node)
        nt.add_update_handler(tracker)
        
        # Run the main loop forever.
        next_update_at = asyncio.get_running_loop().time()
        while True:
            # Sleep until the next iteration.
            next_update_at += UPDATE_PERIOD
            await asyncio.sleep(next_update_at - asyncio.get_running_loop().time())


            remote_node_id=125

            reg_value=Value(natural16=Natural16(100))
            reg_name="reg.rmap.module.TH.1.0.id"
            
            acc_th = node.make_client(Access_1, remote_node_id)              # Create a client
            request_th = Access_1.Request(name=Name_1(reg_name), value=reg_value)  # Create request object

            response = await acc_th(request_th)                                 # Send request, wait for response
            if response is None:
                raise RuntimeError("Oops, request has timed out")
            print("The register value is:", response)



            reg_value=Value(natural16=Natural16(150))
            reg_name="reg.rmap.service.module.TH.GetDataAndMetadata.1.0.id"
            
            acc_get = node.make_client(Access_1, remote_node_id)              # Create a client
            request_get = Access_1.Request(name=Name_1(reg_name), value=reg_value)  # Create request object

            response = await acc_get(request_get)                                 # Send request, wait for response
            if response is None:
                raise RuntimeError("Oops, request has timed out")
            print("The register value is:", response)


            
if __name__ == "__main__":

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
