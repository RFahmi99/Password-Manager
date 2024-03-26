<h1 align=center>Password-Manager</h1>
This is a Python-based password manager designed to keep your sensitive information safe and easily accessible. With this, you can securely store and manage all your passwords with ease, ensuring peace of mind in today's digital world.
<br />
<br />

# Modules
This project is coded purely in python. However, it uses a few python modules. Such as:
1. cryptography
2. pycparser
3. pyodbc
<br />

# Installation
To install the modules, run the code:
```markdown
  pip install -r requirements. txt
```
<br/>

# Modifications
1. Go to Functions and open access.py and change the following line:
```markdown
7  conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=Path\To\Your\Code\Password-Manager\Data\Database.accdb;")
```

Change the **Path\To\Your\Code** to your directory path.<br />
2. Open database.py, key.py and make the same modification.<br />
3. Run the application through app.py and enjoy.<br />
<br /> 

#Features
This script can:
1. Write password into database.
2. View password from database.
3. Show the list of all commands.
4. Exit on command.
<br />

Best of luck!
