import random
import sys
from enum import Enum
import time
import datetime
import unittest
import unittest
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#PART 1
class DeviceStatus(Enum):
    ON = "On"
    OFF = "Off"


class SecurityStatus(Enum):
    NORMAL = "Normal"
    MOTIONDETECTION = "Motion detection"
    


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
        security_status (SecurityStatus): The current security status (NORMAL or MOTIONDETECTION).
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
            self.security_status = SecurityStatus.MOTIONDETECTION
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
                if device.security_status == SecurityStatus.MOTIONDETECTION:
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


smart_light = SmartLight("Light_01")
thermostat = Thermostat("Thermostat_01")
security_camera = SecurityCamera("Camera_01")


simulate_device_behavior(smart_light, 3, 1)
simulate_device_behavior(thermostat, 3, 1)
simulate_device_behavior(security_camera, 3, 1)


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
            if device.security_status == SecurityStatus.MOTIONDETECTION:
                device.reset_alarm()






smart_light = SmartLight("Part 2 Light_02")
thermostat = Thermostat("Part 2 Thermo_2")
security_camera = SecurityCamera("Part 2 Camera_02")


home_automation = AutomationSystem()
home_automation.discover_devices([smart_light, thermostat, security_camera])
home_automation.simulate_automation_system(10, 1)

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
        self.assertEqual(security_camera.security_status, SecurityStatus.MOTIONDETECTION)

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

#PART 4 GUI

# Light control functions
def toggle_light_gui():
    if light_status_var.get() == "On":
        light_status_var.set("Off")
        smart_light.turn_off()
        brightness_scale.set(0)
    else:
        light_status_var.set("On")
        smart_light.turn_on()
        brightness_scale.set(100)


    update_light_label()
    update_status_label()

def update_light_label():
    light_brightness_var.set(f"{smart_light.device_id} : \n{int(brightness_scale.get())}")


# Thermostat control functions
def toggle_thermostat():
    if thermostat_status_var.get() == "On":
        thermostat_status_var.set("Off")
        thermostat.status = DeviceStatus.OFF

    else:
        thermostat_status_var.set("On")
        thermostat.status = DeviceStatus.ON
    update_thermostat_label()
    update_status_label()

def update_thermostat_label():
    thermostat_temp_var.set(f"Living Room Thermostat\n{round(float(temperature_scale.get()))} C")

# Camera control functions
def toggle_camera():
    if camera_status_var.get() == "No":
        camera_status_var.set("Yes")
    else:
        camera_status_var.set("No")

def camera_mode_button_text():
    if security_camera.security_status == SecurityStatus.NORMAL:
        return "Set mode: MOTIONDETECTION"
    else:
        return "Set mode: Normal"


def toggle_camera_mode():
    if security_camera.status == DeviceStatus.OFF:
        camera_mode_var.set(f"Camera turned {security_camera.status.name}")
    else:
        if security_camera.security_status == SecurityStatus.NORMAL:
            security_camera.security_status = SecurityStatus.MOTIONDETECTION
        else:
            security_camera.security_status = SecurityStatus.NORMAL
        camera_mode_var.set(f"Camera mode: {security_camera.security_status.value}")

    update_camera_mode_button()


def update_camera_mode_button():
    camera_mode_button.config(text=camera_mode_button_text())

def camera_mode_button_text():
    if security_camera.status.name == DeviceStatus.ON.name:
        if security_camera.security_status == SecurityStatus.NORMAL:
            return "Set mode: Normal"
        else:
            return "Set mode: MOTIONDETECTION"
    else:
        return f"Camera turned off!"


def toggle_cam_onoff():
    if security_camera.status == DeviceStatus.ON:
        camera_onoff_var.set(f"Camera: {DeviceStatus.OFF.value}")
        security_camera.status = DeviceStatus.OFF
    else:
        camera_onoff_var.set(f"Camera: {DeviceStatus.ON.value}")
        security_camera.status = DeviceStatus.ON
    update_camera_onoff_button()
    update_camera_mode_button()
    update_status_label()  # Update status label


def update_status_label():
    status_label.config(text=f"{smart_light.device_id} : {smart_light.status.value}\n"
                             f"{thermostat.device_id}: {thermostat.status.value}\n"
                             f"{security_camera.device_id}: {security_camera.status.value}")



def update_camera_onoff_button():
    camera_on_off_button.config(text=camera_onoff_button_text())
def camera_onoff_button_text():
    if security_camera.status.name == DeviceStatus.ON.name:
        return f"Turn {security_camera.device_id} Off"
    else:
        return f"Set mode: {security_camera.device_id} On"



def monitor_data():
    # Create a new top-level window
    monitor_window = tk.Toplevel(app)
    monitor_window.title("Real-time Data Monitoring")

    # Create a figure for plotting
    fig = Figure(figsize=(10, 4), dpi=100)
    ax1 = fig.add_subplot(131)  # For thermostat
    ax2 = fig.add_subplot(132)  # For security camera
    ax3 = fig.add_subplot(133)  # For smart light

    # Draw the canvas
    canvas = FigureCanvasTkAgg(fig, master=monitor_window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    temperature_data = []
    brightness_data = []
    motion_data = []
    time_data = []

    def update_data():
        # Simulate real-time data
        current_time = time.time()
        temperature = round(float(temperature_scale.get())) + random.uniform(-1, 1)
        brightness = int(brightness_scale.get()) + random.randint(-5, 5)
        motion_detected = random.choice([True, False])

        # Append data to lists
        time_data.append(current_time)
        temperature_data.append(temperature)
        brightness_data.append(brightness)
        motion_data.append(motion_detected)

        # Update thermostat graph
        ax1.clear()
        ax1.plot(time_data, temperature_data, 'r-')
        ax1.set_title('Thermostat Temperature')
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Temperature (C)')

        # Update security camera status
        ax2.clear()
        ax2.plot(time_data, [1 if motion else 0 for motion in motion_data], 'b-')
        ax2.set_title('Security Camera Status')
        ax2.set_xlabel('Time')
        ax2.set_ylabel('Motion Detected')

        # Update smart light brightness
        ax3.clear()
        ax3.plot(time_data, brightness_data, 'g-')
        ax3.set_title('Smart Light Brightness')
        ax3.set_xlabel('Time')
        ax3.set_ylabel('Brightness')

        # Draw the updated plots
        canvas.draw()

        # Update data every second
        monitor_window.after(1000, update_data)

    update_data()



smart_light = SmartLight("Hall Smartlight 01")
thermostat = Thermostat("Dining Thermostat 01")
security_camera = SecurityCamera("Front Door Camera_01")

app = tk.Tk()
app.title("Smart Home IoT Simulator")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Device status labels
light_status_var = tk.StringVar(value=smart_light.status.value)
thermostat_status_var = tk.StringVar(value=thermostat.status.value)
camera_status_var = tk.StringVar(value=security_camera.status.value)
status_label = ttk.Label(frame)
status_label.grid(column=0, row=0, pady=10, padx=10, columnspan=2)
update_status_label()


# Light controls
light_brightness_var = tk.StringVar()
brightness_scale = ttk.Scale(frame, from_=0, to=100, command=lambda x: update_light_label())
brightness_scale.set(int(smart_light.brightness))
light_brightness_var.set(f"{smart_light.device_id}  Brightness\n{smart_light.brightness}")
ttk.Label(frame, textvariable=light_brightness_var).grid(column=0, row=1, pady=10, padx=10, sticky=tk.W)
brightness_scale.grid(column=0, row=2, pady=10, padx=10, sticky=tk.W)
ttk.Button(frame, text=f"Toggle {smart_light.device_id} ON/OFF", command=toggle_light_gui).grid(column=0, row=3, pady=10, padx=10)

# Thermostat controls
thermostat_temp_var = tk.StringVar()
temperature_scale = ttk.Scale(frame, from_=-10, to=30, command=lambda x: update_thermostat_label())
temperature_scale.set(17)
ttk.Label(frame, textvariable=thermostat_temp_var).grid(column=0, row=4, pady=10, padx=10, sticky=tk.W)
temperature_scale.grid(column=0, row=5, pady=10, padx=10, sticky=tk.W)
ttk.Button(frame, text=f"Toggle {thermostat.device_id} ON/OFF", command=toggle_thermostat).grid(column=0, row=6, pady=10, padx=10)

# Camera controls
camera_onoff_var = tk.StringVar(value=f"Camera : {security_camera.status.value}")
camera_mode_var = tk.StringVar(value=f"Camera mode: {security_camera.security_status.value}")

ttk.Label(frame, text=f"{security_camera.device_id}").grid(column=0, row=7, pady=10, padx=10, sticky=tk.W)
ttk.Label(frame, textvariable=camera_mode_var).grid(column=0, row=8, pady=10, padx=10, sticky=tk.W)
camera_on_off_button = ttk.Button(frame, text=camera_onoff_button_text(), command=toggle_cam_onoff)
camera_on_off_button.grid(column=0, row=9, pady=10, padx=10)
camera_mode_button = ttk.Button(frame, text=camera_mode_button_text(), command=toggle_camera_mode)
camera_mode_button.grid(column=0, row=10, pady=10, padx=10)

camera_mode_button = ttk.Button(frame, text=camera_mode_button_text(), command=toggle_camera_mode)
camera_mode_button.grid(column=0, row=11, pady=10, padx=10)

monitorButton = ttk.Button(frame, text="Monitor Real-time Data", command=monitor_data)
monitorButton.grid(column=0, row=11, pady=10, padx=10)

app.mainloop()

