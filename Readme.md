## Installation Guide for Pasgen Tools

1. **Clone the Repository:
```**
   ```bash
   git clone https:
   ```//github.com/x21empire/pasgen.git
Navigate to the Project Directory:
```

```bash
cd pasgen
```
## Make Scripts Executable:
```bash
chmod +x pasgen
chmod +x generate_entries.py
```
## Install the Tool:
```bash
sudo python3 setup.py install
```
## Set Up the Password:
```bash
pasgen setup
```
## Generate Passwords or Pins:
```bash
Generate a password:
pasgen generate

Generate a pin:

pasgen generate -p
```
# View Generated Passwords:
```bash
cat pasgen-entries.txt
```
## Change Password:

```bash
pasgen setup
```
## Run the Tool:
```bash
pasgen
```
# Note:

Make sure you have Python 3 installed on your system.
You may need to use sudo to execute certain commands depending on your system's configuration.
