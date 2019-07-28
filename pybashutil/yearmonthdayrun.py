from __future__ import print_function
import pybashutil
import sys
import os
import subprocess

dates = sys.argv[1]

for date in pybashutil.date_range(dates):
    args = [v.replace("__HDATE__", "{}-{}-{}".format(date[:4], date[4:6], date[6:])).replace("__DATE__", date) for v in sys.argv[2:]]
    args = [v.replace("__HMONTH__", "{}".format(date[4:6])).replace("__MONTH__", date) for v in args]
    args = [v.replace("__HYEAR__", "{}".format(date[:4])).replace("__YEAR__", date) for v in args]
    print(args)
    subprocess.check_call(args, stdout=sys.stdout, stderr=sys.stderr)