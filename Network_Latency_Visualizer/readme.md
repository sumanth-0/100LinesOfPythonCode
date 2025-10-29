# Ping Plotter

Ping Plotter is a Python script that continuously pings a host and plots the latency in real-time. It's useful for monitoring network performance.

---

## Requirements

You need Python installed along with the following packages:

* `ping3`
* `matplotlib`

Install them using:

```
pip install ping3 matplotlib
```

---

## Usage

Run the script from your terminal:

* Ping Google DNS indefinitely:

```
python ping_plot.py
```

* Ping a custom host indefinitely:

```
python ping_plot.py 1.1.1.1
```

* Ping a host for a specific duration (e.g., 30 seconds):

```
python ping_plot.py 8.8.8.8 -d 30
```

---

## Options

* `host`: The hostname or IP address to ping. Defaults to `8.8.8.8` (Google DNS).
* `-d` or `--duration`: The number of seconds to run the ping. Defaults to infinite.

---

## Features

* Continuous ping with live latency plotting
* Handles timeouts gracefully
* Optional duration for automatic stop
* Clean exit with exit codes:

  * `0` → Finished normally
  * `1` → Interrupted by user

