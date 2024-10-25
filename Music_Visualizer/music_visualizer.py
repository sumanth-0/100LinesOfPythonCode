from multiprocessing import Process, Queue
import pyqtgraph.Qt as qt
import pyqtgraph as pg
import soundcard as sc
import numpy as np
import time
import sys

colorArray = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4',
              '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff',
              '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1',
              '#000075', '#808080', '#ffffff']

# Select the microphone
try:
    mics = sc.all_microphones(include_loopback=True)
    print("Available microphones:", mics)
    mic_index = int(input("Choose input device (0 to {}): ".format(len(mics) - 1)))
    audioIn = mics[mic_index]
except Exception as e:
    print("Error accessing microphone:", e)
    sys.exit(1)

RATE = 48000
CHUNK = 1024
BUFFER = 20000
LEN = BUFFER + CHUNK

channelsCNT = audioIn.channels
channels = range(channelsCNT)

# Setup PyQtGraph application
app = qt.QtWidgets.QApplication(sys.argv)
win = pg.GraphicsLayoutWidget(title="Buffered Audio Plot")
win.setGeometry(100, 100, 900, 300)

curves = []
for channel in channels:
    p = win.addPlot(title=f"Channel {channel}")  # Create a separate plot for each channel
    p.setYRange(-1, 1, padding=0)
    p.setXRange(0, LEN, padding=0)
    curve = p.plot(pen=colorArray[channel % len(colorArray)])  # Use modulo for color cycling
    curves.append(curve)

def stream(q):
    with audioIn.recorder(samplerate=RATE) as mic:
        while True:
            data = mic.record(numframes=CHUNK)
            q.put(data)
            time.sleep(0.001)  # Avoid overusing resources

def update(q: Queue):
    win.show()
    plotData = np.zeros((LEN, channelsCNT))
    while True:
        try:
            while True:
                data = q.get_nowait()
                shift = len(data)
                plotData = np.roll(plotData, -shift, axis=0)
                plotData[-shift:, :] = data
                for channel in channels:
                    curves[channel].setData(plotData[:, channel])
                app.processEvents()
        except Exception:
            app.processEvents()
        time.sleep(0.001)

if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=update, args=(q,))
    p2 = Process(target=stream, args=(q,))
    p2.start()
    p1.start()
    p1.join()
    p2.join()
