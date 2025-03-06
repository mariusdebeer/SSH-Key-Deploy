# SSH Key Deployment Script

## What It Does
This Python script automates adding an SSH public key to multiple remote servers using their IP addresses, usernames, and passwords. It uses `paramiko` to connect via SSH, set up the `.ssh` directory, and append the key to `authorized_keys`.

## How to Use It
1. **Install Dependencies**:
   ```bash
   pip install paramiko
2. ** Edit the Script**:
- Update the servers list with your servers' IPs, usernames, and passwords.
- Set public_key_path to your SSH public key file (e.g., ~/.ssh/id_ed25519.pub).

3. **Run the Script**:
```bash
python3 addkey.py
