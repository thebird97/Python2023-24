import random
import sys
from enum import Enum
import time
import datetime
import unittest
import unittest


#PART 1
class DeviceStatus(Enum):
    ON = 1
    OFF = 0


class SecurityStatus(Enum):
    NORMAL = "NORMAL"
    EMERGENCY = "EMERGENCY"


DEFAULT_TEMPERATURE = 20


class SmartLight:
    """
    Represents a smart light device with capabilities to turn on, turn off,
    set brightness, and dim light.

    Attributes:
        device_id (str): Identifier for the smart light.
        status (DeviceStatus): The current status of the light (ON or OFF).
        brightness (int): The brightness level of the light.
    """
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = DeviceStatus.OFF
        self.brightness = 0
        self.last_updated = datetime.datetime.now()

    def turn_on(self):
        self.status = DeviceStatus.ON
        self.brightness = 100
        self.last_updated = datetime.datetime.now()

    def turn_off(self):
        self.status = DeviceStatus.OFF
        self.brightness = 0
        self.last_updated = datetime.datetime.now()

    def set_brightness(self, level):
        if self.status == DeviceStatus.OFF:
            self.turn_on()
        self.brightness = level
        self.last_updated = datetime.datetime.now()

    def dim_light(self, steps=5):
        if self.status == DeviceStatus.ON and self.brightness > 0:
            self.brightness = max(self.brightness - steps, 0)
            self.last_updated = datetime.datetime.now()


class Thermostat:
    """
    Represents a thermostat device with capabilities to turn on, turn off,
    and set temperature.

    Attributes:
        device_id (str): Identifier for the thermostat.
        status (DeviceStatus): The current status of the thermostat (ON or OFF).
        temperature (int): The current temperature setting.
    """
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = DeviceStatus.OFF
        self.temperature = DEFAULT_TEMPERATURE  # Default
        self.last_updated = datetime.datetime.now()

    def turn_on(self):
        self.status = DeviceStatus.ON
        self.last_updated = datetime.datetime.now()

    def turn_off(self):
        self.status = DeviceStatus.OFF
        self.last_updated = datetime.datetime.now()

    def set_temperature(self, temp):
        if temp > self.temperature:
            self.turn_on()
        self.temperature = temp
        self.last_updated = datetime.datetime.now()


class SecurityCamera:
    """
    Represents a security camera with capabilities to turn on, turn off,
    trigger alarm, and reset alarm.

    Attributes:
        device_id (str): Identifier for the security camera.
        status (DeviceStatus): The current status of the camera (ON or OFF).
        security_status (SecurityStatus): The current security status (NORMAL or EMERGENCY).
    """
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = DeviceStatus.ON #Camera is working by default
        self.security_status = SecurityStatus.NORMAL
        self.last_updated = datetime.datetime.now()

    def turn_on(self):
        self.status = DeviceStatus.ON
        self.last_updated = datetime.datetime.now()

    def turn_off(self):
        self.status = DeviceStatus.OFF
        self.last_updated = datetime.datetime.now()

    def trigger_alarm(self):
        if self.status == DeviceStatus.ON:
            self.security_status = SecurityStatus.EMERGENCY
            self.last_updated = datetime.datetime.now()

    def reset_alarm(self):
        if self.status == DeviceStatus.ON:
            self.security_status = SecurityStatus.NORMAL
            self.last_updated = datetime.datetime.now()

#PART 2

class AutomationSystem:
    """
        Represents an automation system that manages multiple devices.

        Attributes:
            devices (list): List of devices managed by the automation system.
        """
    def __init__(self):
        self.devices = []

    def discover_devices(self, device_list):
        for device in device_list:
            self.add_device(device)

    def add_device(self,device):
        if device not in self.devices:
            self.devices.append(device)
            print(f"Device {device.device_id} added.")
        else:
            print(f"fDevice: {device.device_id} already exists.")

    def remove_device(self, device):
        if device in self.devices:
            self.devices.remove(device)
            print(f"Device {device.device_id} removed.")
        else:
            print(f"Device {device.device_id} not exists.")
    def execute_automation_tasks(self):
        for device in self.devices:
            if isinstance(device, SmartLight):
                # automation for SmartLight
                if device.brightness > 50:
                    device.dim_light(steps=10)
            elif isinstance(device, Thermostat):
                # automation for Thermostat
                if device.temperature > 25:
                    device.set_temperature(22)
            elif isinstance(device, SecurityCamera):
                # task for SecurityCamera
                if device.security_status == SecurityStatus.EMERGENCY:
                    device.reset_alarm()
    def simulate_automation_system(self, duration=10, interval=1):
        """
        Simulates the automation system for a specified duration and interval.

        Args:
            duration (int): Duration of the simulation in seconds.
            interval (int): Interval for each simulation step in seconds.
        """
        print(f"Simulation Duration: {duration} seconds, Interval: {interval} second(s)\n")
        start_time = time.time()

        while time.time() - start_time < duration:
            current_time = time.time() - start_time
            print(f"\nSimulation Time: {current_time:.2f} seconds")

            # Trigger automation tasks
            self.execute_automation_tasks()

            # Update device states and simulate behaviors
            for device in self.devices:
                if isinstance(device, SmartLight):
                    # Simulate random brightness changes and print the status
                    new_brightness = random.randint(0, 100)
                    device.set_brightness(new_brightness)
                    print(f"SmartLight {device.device_id} - Status: {device.status.name}, Brightness: {device.brightness}, Last Updated: {device.last_updated}")


                elif isinstance(device, Thermostat):
                    # Simulate random temperature changes and print the status
                    new_temp = random.randint(15, 30)
                    device.set_temperature(new_temp)
                    print(f"Thermostat {device.device_id} - Status: {device.status.name}, Temperature: {device.temperature}, Last Updated: {device.last_updated}")


                elif isinstance(device, SecurityCamera):
                    # Simulate security status changes and print the status
                    if random.choice([True, False]):
                        device.trigger_alarm()
                        print(f"Security {device.device_id} - Status: {device.status.name}, Temperature: {device.security_status}, Last Updated: {device.last_updated}")

                    else:
                        device.reset_alarm()
                        print(
                            f"SecurityCamera {device.device_id} - Status: {device.status.name}, Security Status: {device.security_status.value}, Last Updated: {device.last_updated}")

            time.sleep(interval)


#PART 1
def simulate_device_behavior(device, duration=10, interval=1):
    print(f"Duration: {duration} Interval: {interval}\n")
    start_time = time.time()

    while time.time() - start_time < duration:
        current_time = time.time() - start_time
        print(f"Simulation Time: {current_time:.2f} seconds")

        if isinstance(device, SmartLight):
            if random.choice([True, False]):
                device.dim_light(steps=random.randint(1, 10))
            else:
                device.set_brightness(random.randint(0, 100))

            print(
                f"Device: {device.device_id}, Type: SmartLight, Status: {device.status.name}, Brightness: {device.brightness}")

        elif isinstance(device, Thermostat):
            device.set_temperature(random.randint(15, 30))
            print(
                f"Device: {device.device_id}, Type: Thermostat, Status: {device.status.name}, Temperature: {device.temperature}")

        elif isinstance(device, SecurityCamera):
            if random.choice([True, False]):
                device.trigger_alarm()
            else:
                device.reset_alarm()

            print(
                f"Device: {device.device_id}, Type: SecurityCamera, Status: {device.status.name}, Security Status: {device.security_status.name}")

        time.sleep(interval)

#PART 1
print("#PART 1")
'''

smart_light = SmartLight("Light_01")
thermostat = Thermostat("Thermo_01")
security_camera = SecurityCamera("Camera_01")

simulate_device_behavior(smart_light, 3, 1)
simulate_device_behavior(thermostat, 3, 1)
simulate_device_behavior(security_camera, 3, 1)
'''

#PART 2
print("#PART 2")
def execute_automation_tasks(self):
    for device in self.devices:
        if isinstance(device, SmartLight):
            # automation for SmartLight
            if device.brightness > 50:
                device.dim_light(steps=10)
        elif isinstance(device, Thermostat):
            # automation for Thermostat
            if device.temperature > 25:
                device.set_temperature(22)
        elif isinstance(device, SecurityCamera):
            #task for SecurityCamera
            if device.security_status == SecurityStatus.EMERGENCY:
                device.reset_alarm()





"""
smart_light = SmartLight("Light_02")
thermostat = Thermostat("Thermo_2")
security_camera = SecurityCamera("Camera_02")


home_automation = AutomationSystem()
home_automation.discover_devices([smart_light, thermostat, security_camera])
home_automation.simulate_automation_system(10, 1)
"""
#PART 3
print("PART 3")


class TestSmartHomeDevices(unittest.TestCase):

    def test_smart_light(self):
        smart_light = SmartLight("Light_Test")
        self.assertEqual(smart_light.status, DeviceStatus.OFF)
        self.assertEqual(smart_light.brightness, 0)

        smart_light.turn_on()
        self.assertEqual(smart_light.status, DeviceStatus.ON)
        self.assertEqual(smart_light.brightness, 100)

        smart_light.set_brightness(50)
        self.assertEqual(smart_light.brightness, 50)

        smart_light.dim_light(steps=10)
        self.assertEqual(smart_light.brightness, 40)

        smart_light.turn_off()
        self.assertEqual(smart_light.status, DeviceStatus.OFF)
        self.assertEqual(smart_light.brightness, 0)

    def test_thermostat(self):
        thermostat = Thermostat("Thermo_Test")
        self.assertEqual(thermostat.status, DeviceStatus.OFF)
        self.assertEqual(thermostat.temperature, DEFAULT_TEMPERATURE)

        thermostat.turn_on()
        self.assertEqual(thermostat.status, DeviceStatus.ON)

        thermostat.set_temperature(25)
        self.assertEqual(thermostat.temperature, 25)

        thermostat.turn_off()
        self.assertEqual(thermostat.status, DeviceStatus.OFF)

    def test_security_camera(self):
        security_camera = SecurityCamera("Camera_Test")
        self.assertEqual(security_camera.status, DeviceStatus.ON)
        self.assertEqual(security_camera.security_status, SecurityStatus.NORMAL)

        security_camera.trigger_alarm()
        self.assertEqual(security_camera.security_status, SecurityStatus.EMERGENCY)

        security_camera.reset_alarm()
        self.assertEqual(security_camera.security_status, SecurityStatus.NORMAL)

        security_camera.turn_off()
        self.assertEqual(security_camera.status, DeviceStatus.OFF)

class TestAutomationSystem(unittest.TestCase):

    def test_automation_system(self):
        smart_light = SmartLight("Light_Test")
        thermostat = Thermostat("Thermo_Test")
        security_camera = SecurityCamera("Camera_Test")

        home_automation = AutomationSystem()
        home_automation.discover_devices([smart_light, thermostat, security_camera])

        self.assertIn(smart_light, home_automation.devices)
        self.assertIn(thermostat, home_automation.devices)
        self.assertIn(security_camera, home_automation.devices)

        home_automation.remove_device(security_camera)
        self.assertNotIn(security_camera, home_automation.devices)

        # Execute automation tasks and verify changes
        smart_light.set_brightness(60)
        thermostat.set_temperature(26)

        home_automation.execute_automation_tasks()

        self.assertEqual(smart_light.brightness, 50)  # Dimmed by 10
        self.assertEqual(thermostat.temperature, 22)  # Set to 22

class TestAutomationSystem(unittest.TestCase):

    def test_simulate_automation_system(self):
        smart_light = SmartLight("Light_Sim")
        thermostat = Thermostat("Thermo_Sim")
        security_camera = SecurityCamera("Camera_Sim")

        home_automation = AutomationSystem()
        home_automation.discover_devices([smart_light, thermostat, security_camera])

        # Simulate for a short duration
        home_automation.simulate_automation_system(duration=2, interval=1)

        # Check if the devices' last_updated time has changed
        current_time = datetime.datetime.now()

        self.assertLess((current_time - smart_light.last_updated).total_seconds(), 3)
        self.assertLess((current_time - thermostat.last_updated).total_seconds(), 3)
        self.assertLess((current_time - security_camera.last_updated).total_seconds(), 3)

        # Further checks can be added based on expected behavior


if __name__ == '__main__':
    unittest.main()