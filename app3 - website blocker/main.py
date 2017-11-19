import time
from datetime import datetime as dt
from datetime import timedelta

hosts_path = "C:\Windows\System32\drivers\etc\hosts"
hosts_temp = "hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

working_hours = [9, 18]
current_day = dt(dt.now().year, dt.now().month, dt.now().day)

while True:
    if current_day + timedelta(hours=working_hours[0]) < dt.now() < current_day + timedelta(hours=working_hours[1]):
        print("Working hours..")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n" + redirect + "    " + website)
    else:
        print("Fun hours..")
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

    time.sleep(3)
