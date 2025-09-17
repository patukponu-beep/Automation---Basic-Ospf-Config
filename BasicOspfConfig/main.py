from netmiko import ConnectHandler, NetmikoAuthenticationException, NetmikoTimeoutException
import json

# # Example: your devices list
# devices = [
#     {"name": "R1", "ip": "192.168.1.1"},
#     {"name": "R2", "ip": "192.168.1.2"}
# ]
#
# # Save to file
# with open("devices.json", "w") as f:
#     json.dump(devices, f, indent=4)   # indent=4 makes it pretty
#
# # Read file
# with open("devices.json", "r") as f:
#     devices = json.load(f)
#
# print(devices)

with open(r"C:\Users\patuk\OneDrive\Desktop\EVE_NG\LABS\AutomationProjects\Inventory\devices.json", "r") as f:
    devices = json.load(f)
print(devices)          # raw dump
# print(type(devices))    # should say list or dict
# print(devices[0])       # first device entry
with open("devices.json", "w") as f:
    json.dump(devices, f, indent=4)



for dev in devices:
    print(f"connecting to {dev.get('name')}")
    ssh_info = {
            "device_type": dev.get("device_type"),
            "ip": dev.get("ip"),
            "username": dev.get("username"),
            "password": dev.get("password")
    }
    try:
        with ConnectHandler(**ssh_info) as conn:
            print(f" ===pushing configuration to {dev.get('name')}=== ")
            cfg = []

            for link in dev.get('links'):
                print(f"====interface {link.get('intf')} configuration====")
                cfg += [
                        f"interface {link.get('intf')}",
                        f"ip address {link.get('phys_ip')} {link.get('mask')}",
                        f"no shut"
                    ]
            print(f"====interface loopback0 configuration====")
            cfg += [
                f"interface loopback 0",
                f"ip add {dev.get('lo_ip')} {dev.get('lo_mask')}",
                f"exit",
                f"router ospf 1",
                f"router-id {dev.get('lo_ip')}",
                f"network {dev.get('lo_ip')} 0.0.0.0 area 0"
            ]
            print(f"===={dev.get('name')} ospf configuration ====")
            for link in dev.get('links'):

                cfg += [
                    f"network {link.get('phys_ip')} 0.0.0.0 area 0"
                ]
            output = conn.send_config_set(cfg)
            print(output)

            with open(f"{dev.get('name')}_config.txt", "w") as f:
                f.write(output)

    except (NetmikoTimeoutException, NetmikoAuthenticationException) as e:
        print(f"error {dev.get('name')} {e}")
        continue
    except Exception as e:
        print(f"error: {dev.get('name')} {e}")
        continue
