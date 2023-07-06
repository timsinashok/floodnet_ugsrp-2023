## This file has different libraries and procedures I used to establish connection with Disto for data retrival. 


## Device Name: DISTO 24856152
## Device Address: 01B6DE0A-06C3-F92B-DF68-1B203C22AF69


import asyncio
from bleak import BleakScanner, BleakClient

device_address = '906E4045-4BAE-0493-E9ED-15F2397BD4CB'  # Replace with the Bluetooth device address of your sensor

async def discover_services():
    async with BleakScanner() as scanner:
        devices = await scanner.discover()
        for device in devices:
            if device.address == device_address:
                async with BleakClient(device) as client:
                    services = await client.get_services()
                    for service in services:
                        print(f'Service: {service}')
                        for characteristic in service.characteristics:
                            print(f'    Characteristic: {characteristic}')
                break

asyncio.run(discover_services())


import asyncio
from bleak import BleakScanner, BleakClient

device_address = '906E4045-4BAE-0493-E9ED-15F2397BD4CB'  # Replace with the Bluetooth device address of your Disto D1 sensor

distance_characteristic_uuid = '3ab10101-f831-4395-b29d-570977d5bf94'  # Replace with the actual UUID for distance measurement characteristic

async def read_distance():
    async with BleakClient(device_address) as client:
        print("device found")
        distance_characteristic = await client.read_gatt_char(distance_characteristic_uuid)
        print(distance_characteristic)
        # value = await distance_characteristic.read()
        distance = distance_characteristic.decode("utf-8")
        return distance

distance = asyncio.run(read_distance())
print('Distance:', distance, 'mm')


import asyncio
from bleak import BleakClient

address = "01B6DE0A-06C3-F92B-DF68-1B203C22AF69"
MODEL_NBR_UUID = "3ab10101-f831-4395-b29d-570977d5bf94"

async def main(address):
    client = BleakClient(address)
    try:
        await client.connect()
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))
    except Exception as e:
        print(e)
    finally:
        await client.disconnect()

asyncio.run(main(address))



import asyncio
from bleak import BleakScanner, BleakClient

device_address = '01B6DE0A-06C3-F92B-DF68-1B203C22AF69'  # Replace with the Bluetooth device address of your sensor
distance_characteristic_uuid = '00002902-0000-1000-8000-00805f9b34fb'  # Replace with the UUID for the distance characteristic

async def get_distance():
    async with BleakScanner() as scanner:
        devices = await scanner.discover()
        for device in devices:
            if device.address == device_address:
                async with BleakClient(device) as client:
                    services = await client.get_services()
                    for service in services:
                        for characteristic in service.characteristics:
                            if characteristic.uuid == distance_characteristic_uuid:
                                distance_value = await client.read_gatt_char(characteristic)
                                print(f"Distance: {distance_value}")
                                return
                break

asyncio.run(get_distance())





#################### searching devices #######################
import asyncio
from bleak import BleakScanner

async def discover_devices():
    scanner = BleakScanner()
    devices = await scanner.discover()
    for device in devices:
    
        print(f"Device Name: {device.name}")
        print(f"Device Address: {device.address}")
        print("")

asyncio.run(discover_devices())