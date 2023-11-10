import random
import time
import tkinter as tk  # GUI
from threading import Thread

'''
    - Egészítsd ki az okos eszközök mûködését:
        - pl. Lámpa (SmartLight) esetén legyen beállítható a fényerõ (brightness)
        - Thermostat: pl(hõmérsékleti szélsõértékek +) egy aktuális mért érték
        - SecurityCamera:
            motion_detected: boolean érték: mely tartalmazza, hogy épp érzékel-e mozgást


    AutomationSystem:
        - felelõs az összes eszköz kezeléséért

    Dashboard:
        Interaktív GUI, amivel a felhasználó ki-be kapcsolhatja az eszközök automatizálását
        Ha az automation_on be van kapcsolva,
        akkor a randomize_device_states fügvény beállítja 2 másodpercenként az értékeket.
        (az átkapcsolást automatikus és manuális mód között nem szükséges megvalósítani,
        de kipróbálhatod, ha False-ra állítod az értéket a forráskódban.)

        kezdetben egy véletlen számot generál 42 és 42 között.
        Ez itt most nem a jó válasz. Írd át, hogy pl 0 és 100 vagy 1 és 100 között vehessen fel értéket a lámpa esetén
        A többi eszköz esetén is az azoknak megfelelõ értékeket.

'''

'''Part 1: IoT Device Emulation (25 %)'''
'''Device Classes: Create Python classes for each type of IoT device you 
want to simulate, such as SmartLight, Thermostat, and SecurityCamera. 
Each class should have attributes like device ID, status (on/off), and 
relevant properties (e.g., temperature for thermostats, brightness for 
lights, and security status for cameras).
 Device Behavior: Implement methods for each device class that allow 
for turning devices on/off and changing their properties. Simulate 
realistic behavior, such as gradual dimming for lights or setting 
temperature ranges for thermostats.
 Randomization: Include a randomization mechanism to simulate 
changing device states and properties over time.'''


class SmartDevice:
    def __init__(self, device_id):
        self.status = False
        self.device_id = device_id

    def get_status(self):
        if self.status:
            return 'ON'
        return 'OFF'

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

    def toggle_status(self):
        self.status = not self.status


'''TODO: Add the relevant attributes and initialize them in the constructor'''


class SmartLight(SmartDevice):
    # in the constructor, set brightness to 0
    def __init__(self, device_id):
        super().__init__(device_id)  # ha nem hívjuk meg, akkor nem lesz status, device_id
        self.brightness = 0

    def set_brightness(self, value):
        if not self.status:
            self.turn_on()
        elif value == 0:
            self.turn_off()
        self.brightness = value


class Thermostat(SmartDevice):
    pass


class SecurityCamera(SmartDevice):
    pass


'''Part 2: Central Automation System (25 %)
 Automation System Class: Create a central automation system class, 
e.g., AutomationSystem, responsible for managing and controlling all 
devices. It should provide methods for discovering devices, adding 
them to the system, and executing automation tasks.
 Simulation Loop: Implement a simulation loop that runs periodically 
(e.g., every few seconds) to trigger automation rules, update device 
states, and simulate device behaviors'''


class AutomationSystem:
    def __init__(self):
        self.devices = []
        self.rules = []

    def add_device(self, device):
        self.devices.append(device)


class Dashboard:
    def __init__(self, root, system):
        self.root = root
        self.system = system
        self.root.title("Smart Home IoT Simulator")
        self.labels = []

        # ha hamisra állítjuk, a csúszkákkal adhatunk értékeket.
        # egyébként random
        self.automation_on = True

        self.automation_text = tk.StringVar()

        self.device_listbox = tk.Listbox(root, width=50)
        self.device_listbox.pack()

        self.update_device_list()

        # TODO: hozzáadjuk a többi ablakelemet
        self.create_device_controls()

        self.update_device_list()

        # szál kezelése
        self.update_thread = Thread(target=self.simulation_loop)
        self.update_thread.daemon = True
        self.update_thread.start()

    def update_device_list(self):
        self.device_listbox.delete(0, tk.END)
        for device in self.system.devices:
            self.device_listbox.insert(tk.END,
                                       f"{device.device_id}: {type(device).__name__} Status: {'On' if device.status else 'Off'}")

    def create_device_controls(self):
        # TODO: minden eszközhöz legyenek GUI elemek
        for i, device in enumerate(self.system.devices):
            if isinstance(device, SmartLight):
                self.create_light_controls(device)
                var_str = tk.StringVar()
                var_str.set("{} - {}%".format(device.device_id, device.brightness))
                tmp_label = tk.Label(self.root, textvariable=var_str)
                self.labels.append({
                    'id': device.device_id,
                    'label': var_str,
                    'device': device
                })
                tk.Button(self.root, text="Toggle ON/OFF",
                          command=lambda device=device: self.toggle_helper(device)).pack()
                tmp_label.pack()

    def toggle_random(self):
        self.automation_on = not self.automation_on

    def create_light_controls(self, light):
        # Create controls for a smart light
        label = tk.Label(self.root, text=f"{light.device_id} Brightness")
        label.pack()
        brightness_slider = tk.Scale(self.root, from_=0, to=100, orient="horizontal",
                                     command=lambda value, light=light: self.set_brightness(light, value))
        brightness_slider.pack()

    def update_values(self):
        for tmp_label in self.labels:
            device = tmp_label['device']
            if isinstance(device, SmartLight):
                tmp_label['label'].set(
                    "{} - {}".format(device.device_id, f"{device.brightness}%" if device.status else "(OFF)"))
            # TODO: és így tovább.
            # ...

    def set_brightness(self, light, brightness):
        light.set_brightness(int(brightness))

    def toggle_helper(self, device):
        device.toggle_status()

    def simulation_loop(self):
        while True:
            if self.automation_on:
                randomize_device_states(self.system.devices)
            self.update_values()
            self.update_device_list()
            time.sleep(2)  # Simulate updates every 2 seconds


'''Part 3: Documentation'''
'''TODO: write docstrings to each class and method you write explaining what that part does'''
'''Build some tests, no need to use testing frameworks/TDD just create some examples in main.'''


# Randomization mechanism
def randomize_device_states(devices):
    for device in devices:
        if not device.status:
            continue
        if isinstance(device, SmartLight):
            device.set_brightness(random.randint(42, 42))


# Main function to initialize and run the simulation
if __name__ == "__main__":
    print("Smart Home IoT Simulator")
    # példa sleep-re
    # time.sleep(1)

    # a toggle_status() metódus tesztje:
    my_light = SmartLight("Very special smart light.")
    print(f"{my_light.device_id}: {my_light.get_status()}")
    my_light.toggle_status()
    print(f"{my_light.device_id}: {my_light.get_status()}")
    my_light.toggle_status()
    print(f"{my_light.device_id}: {my_light.get_status()}")

    # Példányosítsuk az eszközöket:
    light1 = SmartLight("Living Room Light")
    thermostat1 = Thermostat("Living Room Thermostat")
    camera1 = SecurityCamera("Front Door Camera")

    # példányosítsuk az automatizációért felelõs osztályt
    automation_system = AutomationSystem()
    # adjuk hozzá az eszközöket:
    automation_system.add_device(light1)
    automation_system.add_device(thermostat1)
    automation_system.add_device(camera1)

    root = tk.Tk()
    dashboard = Dashboard(root, automation_system)
    # Az ablakon belül definiálunk egy mainloop fgv-t ami folyamatosan fut
    root.mainloop()
