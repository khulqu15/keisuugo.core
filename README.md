# How To Install Project

1. Install Python 3.9
``` bash
sudo apt update 
sudo apt install wget software-properties-common 
sudo add-apt-repository ppa:deadsnakes/ppa 
sudo apt update 
sudo apt install python3.9 
```

2. Check Python Version
``` bash
python3 --version
pip3 --version
```

3. Install Requirement Packages
``` bash
pip install -r requirements.txt
```

4. Run Main.py
``` bash
python main.py --input file --file audio.mp3
```