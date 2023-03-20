# Random Password Genrator

![version](https://img.shields.io/github/license/KaushalBhatol/RandomPasswordGenrator)
![version](https://img.shields.io/badge/version-2.0-blue)
![stablity](https://img.shields.io/badge/status-stable-blue)
![userinterface](https://img.shields.io/badge/UI-GUI-blue)
![python-version](https://img.shields.io/badge/python-3.10-blue)
![python-wheel](https://img.shields.io/badge/wheel-No-red)


![python-tkinter](https://img.shields.io/badge/module-tkinter-brown)
![python-string](https://img.shields.io/badge/module-string-brown)
![python-random](https://img.shields.io/badge/module-random-brown)


## About

* Program available on both __CLI__ and __GUI__ interface. For running on CLI you need to uncomment import CLI comment on main.py and comment import GUI

* The program was created for generating random passwords to use on daily basis.

* __Prefix is not necessary__, You can leave it empty also.

* Length of password indicates the total length of a password __including the prefix__.

## Installation

### installing tkinter

```bash
sudo apt install python3-tk -y
pip install tkinter
```

### Downloading and Running Repository

```bash
git clone https://github.com/KaushalBhatol/RandomPasswordGenrator.git

cd RandomPasswordGenrator-master 
chmod u+x ./* 

./main.py
```

### Running Program on CLI

```bash
nano main.py
```

* Comment `import gui`
* Uncomment `import cli` on _main.py_

main.py file:

```python
#!/usr/bin/python3

import cli    # for command line interface
# import gui    # for graphical user interface

```

Run Program:

```bash
./main.py
```

## Screen Shots [GUI]

### Startup screen

![gui.startup](.readme_support/gui.startup.png)

### Output Screen

![python-sc](.readme_support/gui.main.png)
