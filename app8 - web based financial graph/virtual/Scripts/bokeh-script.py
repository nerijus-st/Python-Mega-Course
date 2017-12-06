#!"c:\users\nerijus\code\python mega course\app8 - web based financial graph\virtual\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'bokeh==0.12.11','console_scripts','bokeh'
__requires__ = 'bokeh==0.12.11'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('bokeh==0.12.11', 'console_scripts', 'bokeh')()
    )
