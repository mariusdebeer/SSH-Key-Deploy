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

-The script will connect to each server and add the key.

## Security Notes
**Passwords**: Avoid hardcoding passwords in the script. Use environment variables or a secrets manager instead.

**Host Keys**: Uses AutoAddPolicy to auto-accept host keys, bypassing manual verification. For stricter security, pre-populate known_hosts and remove this policy.

**Post-Setup**: After adding keys, disable password login on servers (PasswordAuthentication no in /etc/ssh/sshd_config) and restart SSH.

