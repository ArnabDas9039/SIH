# SIH Problem Statement 1743

You can find the problem statement [here](https://www.sih.gov.in/sih2024PS?technology_bucket=QWxs&category=U29mdHdhcmU=&organization=TmF0aW9uYWwgSW52ZXN0aWdhdGlvbiBBZ2VuY3kgKE5JQSk=&organization_type=QWxs).

## Table of contents

- Requirements
- Installation and Set up


## Requirements
All the required libraries are added in the repository.

## Installation and Set up
The setup for this repository is pretty straightforward if you follow this steps:
**1. Install Git and GitBash for Windows**

**2. Clone the repository in your file system**
```gitbash
git clone [link_of_reopository] [path_to_save_file]
```
Or, Copy this code directly in the gitbash terminal
```gitbash
git clone https://github.com/ArnabDas9039/SIH.git
```

**3. Create a Python Virtual Environment**

Run this code inside your created directory. For this case, in /SIH/
```cmd
python -m venv env
```
Activate the virual environment
```cmd
cd env/Scripts/

<!-- [for Command Prompt] -->
activate.bat 

<!-- [for PowerShell] -->
./activate.bat

<!-- move to the root directory -->
cd ../../
```

Install required python libraries
```cmd
pip install -r requirements.txt
```

**4. Install WebDriver**

Download the Chrome WebDriver from [here](https://storage.googleapis.com/chrome-for-testing-public/128.0.6613.119/win64/chrome-win64.zip) for Windows. Unzip the contents in the root directory /SIH/ and rename the folder to "chromedriver"

**5. You can now run the program**
```cmd
python main.py
```

By following these steps, you are expected to have correctly configured the project. If faced any problems, contact the owner of the repository.