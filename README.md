# auto_search
Automatically searches using a browser search bar

# How to Use
1. Create a python virtual environment
2. Install required packages: `pip install -d requirements.txt`
3. Run auto_search.py: `python auto_search.py`
4. Follow callibration instructions (you will only need to do this once)
5. Manually run this as desired or create a service to run this automatically

# Automation (Linux)
Use cron to create a cron job for running the script at a given time
1. apt install cron
2. systemctl enable cron
3. crontab -e
4. Add the following line: (this runs at 4am each day)
	0 4 * * * python3 /path/to/auto_search/auto_search.py
5. Save
