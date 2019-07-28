from __future__ import print_function


def get_days_ago(days=1):
    import datetime
    return (datetime.datetime.now() - datetime.timedelta(days)).strftime("%Y%m%d")

def date_range(start_date=None, end_date=None):
    import datetime

    start_date = start_date or get_days_ago()
    if '-' in start_date:
        start_date, end_date = start_date.split('-', 1)
    end_date = end_date or start_date

    start_date = (start_date+'01')[:8]
    end_date = (end_date+'01')[:8]

    start_date = datetime.datetime.strptime(start_date, "%Y%m%d")
    end_date = datetime.datetime.strptime(end_date, "%Y%m%d")

    for n in range(int((end_date - start_date).days) + 1):
        yield (start_date + datetime.timedelta(days=n)).strftime("%Y%m%d")

def month_range(*args, **kwargs):
    from collections import OrderedDict
    ret = OrderedDict()
    dates = list(date_range(*args, **kwargs))
    for date in dates:
        ret[date[:6]] = True
    return ret.keys()