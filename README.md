# analytix

[![PyPi version](https://img.shields.io/pypi/v/analytix.svg)](https://pypi.python.org/pypi/analytix/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/analytix.svg)](https://pypi.python.org/pypi/analytix/)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/analytix)](https://pypi.python.org/pypi/analytix/)
[![PyPI - Status](https://img.shields.io/pypi/status/analytix)](https://pypi.python.org/pypi/analytix/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/analytix)](https://pypi.python.org/pypi/analytix/)

[![Maintenance](https://img.shields.io/maintenance/yes/2021)](https://github.com/parafoxia/analytix)
[![GitHub Release Date](https://img.shields.io/github/release-date/parafoxia/analytix)](https://github.com/parafoxia/analytix)
[![GitHub last commit](https://img.shields.io/github/last-commit/parafoxia/analytix)](https://github.com/parafoxia/analytix)
[![Lines of code](https://img.shields.io/tokei/lines/github/parafoxia/analytix)](https://github.com/parafoxia/analytix)
[![License](https://img.shields.io/github/license/parafoxia/analytix.svg)](https://github.com/parafoxia/analytix/blob/main/LICENSE)

A simple yet powerful API wrapper to make getting analytical information from the YouTube Analytics API easier than ever. More services are coming in the future.

## Features

- Pythonic syntax lets you feel right at home
- Dynamic error handling saves hours of troubleshooting, and makes sure only valid requests count toward your API quota
- A clever interface allows you to make multiple requests per session without reauthorising
- Extra support allows the native saving of CSV files and conversion to DataFrame objects
- Easy enough for beginners, but powerful enough for advanced users

## Installation

**You need Python 3.6.0 or greater to run analytix.** You will also need to have a Google Developers project with the YouTube Analytics API enabled. You can find instructions on how to do that in the [YouTube Analytics API docs](https://developers.google.com/youtube/reporting/v1/code_samples/python#set-up-authorization-credentials/).

It is recommended you install analytix in a virtual environment. To do this, run the following:

```bash
# Windows
> py -3.9 -m venv .venv
> .venv\Scripts\activate
> pip install analytix

# Linux\macOS
$ python3.9 -m venv .venv
$ source ./.venv/bin/activate
$ pip install analytix
```

To install analytix outside of a virtual environment instead, run the following:

```bash
# Windows
> py -3.9 -m pip install analytix

# Linux/macOS
$ python3.9 -m pip install analytix
```

You can also install the development version by running the following (this assumes you're on Linux/macOS):

```bash
$ git clone https://github.com/parafoxia/analytix
$ cd analytix
$ git checkout develop  # Any valid branch name can go here.
$ python3.9 -m pip install -U .
```

## Usage examples

The following example shows you how easy analytix can be to use. This retrieves day-by-day analytics for the last 28 days using all metrics.

```py
import datetime as dt

from analytix import YouTubeAnalytics

client = YouTubeAnalytics("./secrets.json")  # Load from secrets file
start_date = dt.date.today() - dt.timedelta(days=28)
report = client.retrieve(start_date, dimensions=("day",))
report.to_csv("./analytics-28d.csv")
```

Of course not all requests will be that simple, but analytix can handle all the complicated stuff too. This example retrieves day-by-day analytics for live streams in January 2021, split by device type and subscription status, and sorted by views. It then saves the report as a CSV, converts to a dataframe for further analysis, and saves a boxplot figure.

```py
import datetime as dt

import matplotlib.pyplot as plt
import seaborn as sns
from analytix import YouTubeAnalytics

client = YouTubeAnalytics("./secrets.json")
report = client.retrieve(
    dt.date(2021, 1, 1),
    dt.date(2021, 1, 31),
    metrics=("views",),
    dimensions=("day", "deviceType", "subscribedStatus"),
    filters={"liveOrOnDemand": "LIVE"},
    sort_by=("views",),
)
report.to_csv("./live-device-types.csv")
df = report.to_dataframe()

fig = plt.figure()
sns.boxplot(data=df, x="day", y="views", hue="deviceType")
fig.savefig("./live-device-types.png")
```

To read up further, [have a look at the documentation](https://analytix.readthedocs.io/en/latest/).

## License

The analytix module for Python is licensed under the [BSD-3-Clause License](https://github.com/parafoxia/analytix/blob/main/LICENSE).
