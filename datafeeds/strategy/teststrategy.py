from __future__ import (absolute_import, division, print_function, unicode_literals)

import backtrader as bt

# Test a Stratey
class TestStrategy(bt.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.datetime(0)
        print('%s:: %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close

    def next(self):
        # Simply log the closing price of the series from the reference
        self.log('Open: {:.2f} High: {:.2f} Low: {:.2f} Close: {:.2f}'.format(self.datas[0].open[0], self.datas[0].high[0], self.datas[0].low[0], self.datas[0].close[0]))

    def stop(self):
        print("Bars(Length): {}".format(len(self)))
