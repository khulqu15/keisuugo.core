# How To Install Project

1. Install git and clone this project
``` bash
sudo apt update 
sudo apt install git curl
git clone https://github.com/khulqu15/keisuugo.core.git
cd keisuugo.core
```

2. Install Python 3.9
``` bash
sudo apt update 
sudo apt install wget software-properties-common 
sudo add-apt-repository ppa:deadsnakes/ppa 
sudo apt update 
sudo apt install python3.9 
```

3. Check Python Version
``` bash
python3 --version
pip3 --version
```

4. Install Requirement Packages
``` bash
pip install -r requirements.txt
```

5. Run Main.py
``` bash
python3 main.py --input file --file audio.mp3
```