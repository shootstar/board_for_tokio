#!/usr/bin/env python
import os
import sys

try:
    from bundler27.command import inspection,install
    inspection.inspect("PyFile")
    install()
except Exception,e:
    print e
    
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
