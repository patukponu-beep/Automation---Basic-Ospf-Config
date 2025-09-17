# Automation - Basic OSPF Config  

This project demonstrates a **basic network automation workflow** using **Python** and **Netmiko** to configure OSPF on three routers.  
It shows how Python can interact with network devices, push configurations, and manage inventory data via JSON.  

The repo includes:  
- `main.py` → Python script for automating OSPF config  
- `devices.json` → Example inventory file with device details  
- `R1_config.txt`, `R2_config.txt`, `R3_config.txt` → Sample output configs  
- `.unl` file (EVE-NG topology) → with complete configurations as a guide to replicate the lab setup  

---

## Prerequisites  

- **EVE-NG**   
- IOS Router images
- Python 3.x  
- Installed libraries:  
  ```bash
  pip install netmiko

## Lab Setup

- Import the provided .unl file into EVE-NG.
- Three routers (R1, R2, R3) are connected in a triangle topology with OSPF areas. 
- **Before running automation:**

    - Configure SSH access on each router.
    - If you’re using older device images, you may need to enable legacy DH key exchange.
    - Fix for Old DH Keys (Linux/Mac/Windows WSL):
    - Edit (or create) the SSH config file:
    - Linux/Mac: ~/.ssh/config (DONT give it a file extension e.g txt)
    - Windows: C:\Users\<YourUsername>\.ssh\config (DONT give it a file extension e.g txt)
    -  ```bash
        Host *
            KexAlgorithms +diffie-hellman-group1-sha1
	        KexAlgorithms +diffie-hellman-group14-sha1
            HostKeyAlgorithms +ssh-rsa
	        PubKeyAcceptedAlgorithms +ssh-rsa


**Author**

Patrick Ukponu

- MSc Cyber Security, Network Engineer
