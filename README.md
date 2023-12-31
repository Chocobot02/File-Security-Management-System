# File Security Management System

The File Security Management System is a PyQt6-based desktop application designed to manage and display information about secured files. the system provides a user-friendly interface for managing and viewing information about secured files. Users can interact with the table, delete selected rows, and experience a visually appealing application with styled components. The application's modular structure, with a separate class for database operations, promotes code organization and maintainability.

## Features

* Simple GUI design for efficient data navigation and management.
* User can add, delete, and view their files in a table format.
* Dual Access Level
    * Admin Access: Requires an admin password for full access, allowing viewing of sensitive information, including passwords in their original format.
    * Normal Access: Provides access to users with a standard password, displaying passwords in a secure, obscured format for enhanced privacy.

## UI's

### Login UI
![login](https://github.com/Chocobot02/File-Security-Management-System/assets/73695287/b267d702-5abe-48ca-b6fd-0e86db963a6f)

### Landing Page UI
![landing](https://github.com/Chocobot02/File-Security-Management-System/assets/73695287/8e246fbd-7090-4251-a6d5-6f3dba3c97a0)

### Add Files UI
   
![addacc](https://github.com/Chocobot02/File-Security-Management-System/assets/73695287/de1b4214-55f8-4b43-9833-c08bd64efb39)

### View Table UI
![table](https://github.com/Chocobot02/File-Security-Management-System/assets/73695287/e9418763-ae32-474a-a491-f8c3b258ea8e)



> [!IMPORTANT]
> install the dependencies first to make the system run completely.

1. PyQT6
```bash
pip install pyqt6
```

2. MySQL connector
```bash
pip install mysql-connector-python
```

created on Dec 2023
