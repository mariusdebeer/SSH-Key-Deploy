import paramiko
import os

# Configuration: Add your servers and credentials here
servers = [
    {"ip": "", "username": "root", "password": ""},

    # Add more servers as needed: {"ip": "server_ip", "username": "username", "password": "password"},
]

# Path to your public key file (e.g., ~/.ssh/id_ed25519.pub)
public_key_path = os.path.expanduser("~/.ssh/*.pub")

# Read the public key from the file
try:
    with open(public_key_path, "r") as f:
        public_key = f.read().strip()
except FileNotFoundError:
    print(f"Error: Public key file not found at {public_key_path}")
    exit(1)

# Function to add the public key to a server
def add_key_to_server(ip, username, password, pub_key):
    try:
        # Initialize SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the server using password authentication
        print(f"Connecting to {ip} as {username}...")
        ssh.connect(ip, username=username, password=password, timeout=10)

        # Commands to append the public key to authorized_keys
        commands = [
            "mkdir -p ~/.ssh",  # Create .ssh directory if it doesn't exist
            "chmod 700 ~/.ssh",  # Set correct permissions for .ssh
            f"echo '{pub_key}' >> ~/.ssh/authorized_keys",  # Append public key
            "chmod 600 ~/.ssh/authorized_keys"  # Set correct permissions for authorized_keys
        ]

        # Execute each command
        for cmd in commands:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            exit_status = stdout.channel.recv_exit_status()  # Wait for command to complete
            if exit_status != 0:
                print(f"Error executing '{cmd}' on {ip}: {stderr.read().decode()}")
                return False
            else:
                print(f"Successfully executed '{cmd}' on {ip}")

        print(f"Public key added successfully to {ip}")
        return True

    except paramiko.AuthenticationException:
        print(f"Authentication failed for {ip}. Check username/password.")
        return False
    except paramiko.SSHException as e:
        print(f"SSH error for {ip}: {str(e)}")
        return False
    except Exception as e:
        print(f"Unexpected error for {ip}: {str(e)}")
        return False
    finally:
        ssh.close()

# Main execution
if __name__ == "__main__":
    print("Starting SSH key deployment...\n")
    
    for server in servers:
        ip = server["ip"]
        username = server["username"]
        password = server["password"]
        
        print(f"Processing server {ip}...")
        success = add_key_to_server(ip, username, password, public_key)
        if success:
            print(f"Completed for {ip}\n")
        else:
            print(f"Failed for {ip}\n")

    print("Deployment process finished.")
