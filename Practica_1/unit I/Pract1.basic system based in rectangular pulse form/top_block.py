#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Top Block
# GNU Radio version: 3.9.0.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from b_Canal_AWGN_ff import b_Canal_AWGN_ff  # grc-generated hier_block
from b_EYE_Timing_f import b_EYE_Timing_f  # grc-generated hier_block
from b_binary_bipolar_source1_f import b_binary_bipolar_source1_f  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import E3TRadio
import wform  # embedded python module



from gnuradio import qtgui

class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.Sps = Sps = 16
        self.Rb = Rb = 12000
        self.samp_rate = samp_rate = Rb*Sps
        self.Retardo_Timing = Retardo_Timing = int(Sps/2)
        self.run_stop = run_stop = True
        self.impulso = impulso = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
        self.h = h = wform.rect(Sps)
        self.Retardo_ojo = Retardo_ojo = int(Sps/4)
        self.Retardo_bits = Retardo_bits = Retardo_Timing+1
        self.Retardo_T4 = Retardo_T4 = 0
        self.Retardo_T3 = Retardo_T3 = 0
        self.No_dB = No_dB = -60
        self.Channel_BW = Channel_BW = samp_rate/2.
        self.Ab = Ab = 1.

        ##################################################
        # Blocks
        ##################################################
        self.menu = Qt.QTabWidget()
        self.menu_widget_0 = Qt.QWidget()
        self.menu_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_0)
        self.menu_grid_layout_0 = Qt.QGridLayout()
        self.menu_layout_0.addLayout(self.menu_grid_layout_0)
        self.menu.addTab(self.menu_widget_0, 'Eye Diagramm')
        self.menu_widget_1 = Qt.QWidget()
        self.menu_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_1)
        self.menu_grid_layout_1 = Qt.QGridLayout()
        self.menu_layout_1.addLayout(self.menu_grid_layout_1)
        self.menu.addTab(self.menu_widget_1, 'T4 versus R4 in time')
        self.menu_widget_2 = Qt.QWidget()
        self.menu_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_2)
        self.menu_grid_layout_2 = Qt.QGridLayout()
        self.menu_layout_2.addLayout(self.menu_grid_layout_2)
        self.menu.addTab(self.menu_widget_2, 'PSD')
        self.menu_widget_3 = Qt.QWidget()
        self.menu_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_3)
        self.menu_grid_layout_3 = Qt.QGridLayout()
        self.menu_layout_3.addLayout(self.menu_grid_layout_3)
        self.menu.addTab(self.menu_widget_3, 'T3 versus R3')
        self.menu_widget_4 = Qt.QWidget()
        self.menu_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_4)
        self.menu_grid_layout_4 = Qt.QGridLayout()
        self.menu_layout_4.addLayout(self.menu_grid_layout_4)
        self.menu.addTab(self.menu_widget_4, 'T4 versus T3 in time')
        self.menu_widget_5 = Qt.QWidget()
        self.menu_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_5)
        self.menu_grid_layout_5 = Qt.QGridLayout()
        self.menu_layout_5.addLayout(self.menu_grid_layout_5)
        self.menu.addTab(self.menu_widget_5, 'R4 vs R3b , R4 vs R3')
        self.top_grid_layout.addWidget(self.menu, 2, 0, 1, 2)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Retardo_Timing_range = Range(0, Sps-1, 1, int(Sps/2), 200)
        self._Retardo_Timing_win = RangeWidget(self._Retardo_Timing_range, self.set_Retardo_Timing, 'Timing', "counter_slider", int, QtCore.Qt.Horizontal)
        self.menu_grid_layout_0.addWidget(self._Retardo_Timing_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_0.setColumnStretch(c, 1)
        self._Retardo_ojo_range = Range(0, Sps*2, 1, int(Sps/4), 200)
        self._Retardo_ojo_win = RangeWidget(self._Retardo_ojo_range, self.set_Retardo_ojo, 'Center the Eye by a delay', "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._Retardo_ojo_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Retardo_bits_range = Range(0, Sps*10, 1, Retardo_Timing+1, 200)
        self._Retardo_bits_win = RangeWidget(self._Retardo_bits_range, self.set_Retardo_bits, 'Delay transmited signal to match with the received signal', "counter_slider", int, QtCore.Qt.Horizontal)
        self.menu_grid_layout_1.addWidget(self._Retardo_bits_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.menu_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_1.setColumnStretch(c, 1)
        self._Retardo_T4_range = Range(0, len(impulso)*Sps, 1, 0, 200)
        self._Retardo_T4_win = RangeWidget(self._Retardo_T4_range, self.set_Retardo_T4, 'Delay to T4', "counter_slider", int, QtCore.Qt.Horizontal)
        self.menu_grid_layout_4.addWidget(self._Retardo_T4_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.menu_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_4.setColumnStretch(c, 1)
        self._Retardo_T3_range = Range(0, len(impulso)*Sps, 1, 0, 200)
        self._Retardo_T3_win = RangeWidget(self._Retardo_T3_range, self.set_Retardo_T3, 'Delay to T3', "counter_slider", int, QtCore.Qt.Horizontal)
        self.menu_grid_layout_4.addWidget(self._Retardo_T3_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.menu_grid_layout_4.setRowStretch(r, 1)
        for c in range(1, 2):
            self.menu_grid_layout_4.setColumnStretch(c, 1)
        self._No_dB_range = Range(-300, 0, 300/100., -60, 200)
        self._No_dB_win = RangeWidget(self._No_dB_range, self.set_No_dB, 'No (dB)', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._No_dB_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Channel_BW_range = Range(0., samp_rate/2., (samp_rate/2)/100., samp_rate/2., 200)
        self._Channel_BW_win = RangeWidget(self._Channel_BW_range, self.set_Channel_BW, 'Channel_BW', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._Channel_BW_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        _run_stop_check_box = Qt.QCheckBox('Pause')
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.items())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_2 = qtgui.time_sink_f(
            60, #size
            Rb, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_2.set_update_time(0.10)
        self.qtgui_time_sink_x_0_2.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0_2.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_2.enable_tags(True)
        self.qtgui_time_sink_x_0_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_2.enable_autoscale(False)
        self.qtgui_time_sink_x_0_2.enable_grid(False)
        self.qtgui_time_sink_x_0_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_2.enable_control_panel(False)
        self.qtgui_time_sink_x_0_2.enable_stem_plot(True)


        labels = ['Info transmitted', 'Info Received', '', '', '',
            '', '', '', '', '']
        widths = [1, 2, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'blue', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [0, 0, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_2.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_2_win = sip.wrapinstance(self.qtgui_time_sink_x_0_2.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_5.addWidget(self._qtgui_time_sink_x_0_2_win, 3, 0, 1, 2)
        for r in range(3, 4):
            self.menu_grid_layout_5.setRowStretch(r, 1)
        for c in range(0, 2):
            self.menu_grid_layout_5.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1_1_0 = qtgui.time_sink_f(
            60, #size
            Rb, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_1_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1_1_0.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0_1_1_0.set_y_label('input of the waveform filter', "")

        self.qtgui_time_sink_x_0_1_1_0.enable_tags(True)
        self.qtgui_time_sink_x_0_1_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1_1_0.enable_grid(False)
        self.qtgui_time_sink_x_0_1_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1_1_0.enable_stem_plot(False)


        labels = ['', 'Info Received', '', '', '',
            '', '', '', '', '']
        widths = [2, 2, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, 0, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_1_0.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_5.addWidget(self._qtgui_time_sink_x_0_1_1_0_win, 2, 0, 1, 2)
        for r in range(2, 3):
            self.menu_grid_layout_5.setRowStretch(r, 1)
        for c in range(0, 2):
            self.menu_grid_layout_5.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1_1 = qtgui.time_sink_f(
            10*Sps, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_1_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1_1.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0_1_1.set_y_label('input of the waveform filter', "")

        self.qtgui_time_sink_x_0_1_1.enable_tags(True)
        self.qtgui_time_sink_x_0_1_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1_1.enable_grid(False)
        self.qtgui_time_sink_x_0_1_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1_1.enable_stem_plot(False)


        labels = ['', 'Info Received', '', '', '',
            '', '', '', '', '']
        widths = [2, 2, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, 0, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_1.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_5.addWidget(self._qtgui_time_sink_x_0_1_1_win, 1, 0, 1, 2)
        for r in range(1, 2):
            self.menu_grid_layout_5.setRowStretch(r, 1)
        for c in range(0, 2):
            self.menu_grid_layout_5.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1_0 = qtgui.time_sink_f(
            16*Sps, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1_0.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0_1_0.set_y_label('output of  waveform filter', "")

        self.qtgui_time_sink_x_0_1_0.enable_tags(True)
        self.qtgui_time_sink_x_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1_0.enable_grid(False)
        self.qtgui_time_sink_x_0_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1_0.enable_stem_plot(True)


        labels = ['', 'Info Received', '', '', '',
            '', '', '', '', '']
        widths = [3, 2, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, 0, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_4.addWidget(self._qtgui_time_sink_x_0_1_0_win, 2, 0, 1, 2)
        for r in range(2, 3):
            self.menu_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 2):
            self.menu_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_f(
            len(impulso), #size
            Rb, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0_1.set_y_label('input of the waveform filter', "")

        self.qtgui_time_sink_x_0_1.enable_tags(True)
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1.enable_stem_plot(True)


        labels = ['', 'Info Received', '', '', '',
            '', '', '', '', '']
        widths = [2, 2, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [0, 0, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_4.addWidget(self._qtgui_time_sink_x_0_1_win, 1, 0, 1, 2)
        for r in range(1, 2):
            self.menu_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 2):
            self.menu_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
            10*Sps, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(False)


        labels = ['Received Signal', '', '', '', '',
            '', '', '', '', '']
        widths = [4, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_3.addWidget(self._qtgui_time_sink_x_0_0_0_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.menu_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
            10*Sps, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)


        labels = ['Transmitted signal', '', '', '', '',
            '', '', '', '', '']
        widths = [4, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_3.addWidget(self._qtgui_time_sink_x_0_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.menu_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            60, #size
            Rb, #samp_rate
            "", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(True)


        labels = ['Info transmitted', 'Info Received', '', '', '',
            '', '', '', '', '']
        widths = [2, 2, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [0, 0, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_1.addWidget(self._qtgui_time_sink_x_0_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.menu_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_1.setColumnStretch(c, 1)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(Sps, h)
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_delay_0_1_1_0 = blocks.delay(gr.sizeof_float*1, Retardo_T3)
        self.blocks_delay_0_1_1 = blocks.delay(gr.sizeof_float*1, Retardo_T3)
        self.blocks_delay_0_1_0_0 = blocks.delay(gr.sizeof_float*1, Retardo_T4)
        self.blocks_delay_0_1_0 = blocks.delay(gr.sizeof_float*1, Retardo_T4)
        self.blocks_delay_0_1 = blocks.delay(gr.sizeof_float*1, Retardo_T3)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, Retardo_bits)
        self.b_binary_bipolar_source1_f_0 = b_binary_bipolar_source1_f(
            Am=1.,
        )
        self.b_EYE_Timing_f_0 = b_EYE_Timing_f(
            AlphaLineas=0.5,
            Delay=Retardo_ojo,
            GrosorLineas=20,
            N_eyes=2,
            Retardo_Timing=Retardo_Timing,
            Samprate=samp_rate,
            Sps=Sps,
            Title="Eye Diagram and Timing",
            Ymax=2,
            Ymin=-2,
        )

        self.menu_grid_layout_0.addWidget(self.b_EYE_Timing_f_0, 1, 0, 1, 1)
        for r in range(1, 2):
            self.menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_0.setColumnStretch(c, 1)
        self.b_Canal_AWGN_ff_0 = b_Canal_AWGN_ff(
            BW=Channel_BW,
            Ch_NodB=No_dB,
            Ch_Toffset=0,
            samp_rate=samp_rate,
        )
        self.E3TRadio_diezma_ff_0 = E3TRadio.diezma_ff(Sps, Retardo_Timing)
        self.E3TRadio_bipolar_decisor_ff_0 = E3TRadio.bipolar_decisor_ff()



        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_bipolar_decisor_ff_0, 0), (self.blocks_delay_0_1_1_0, 0))
        self.connect((self.E3TRadio_bipolar_decisor_ff_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.E3TRadio_bipolar_decisor_ff_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.E3TRadio_diezma_ff_0, 0), (self.E3TRadio_bipolar_decisor_ff_0, 0))
        self.connect((self.E3TRadio_diezma_ff_0, 0), (self.blocks_delay_0_1_1, 0))
        self.connect((self.b_Canal_AWGN_ff_0, 0), (self.E3TRadio_diezma_ff_0, 0))
        self.connect((self.b_Canal_AWGN_ff_0, 0), (self.b_EYE_Timing_f_0, 0))
        self.connect((self.b_Canal_AWGN_ff_0, 0), (self.blocks_delay_0_1_0_0, 0))
        self.connect((self.b_Canal_AWGN_ff_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.b_binary_bipolar_source1_f_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.b_binary_bipolar_source1_f_0, 0), (self.blocks_delay_0_1_0, 0))
        self.connect((self.b_binary_bipolar_source1_f_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_delay_0_1, 0), (self.qtgui_time_sink_x_0_1_0, 0))
        self.connect((self.blocks_delay_0_1_0, 0), (self.qtgui_time_sink_x_0_1, 0))
        self.connect((self.blocks_delay_0_1_0_0, 0), (self.qtgui_time_sink_x_0_1_1, 0))
        self.connect((self.blocks_delay_0_1_1, 0), (self.qtgui_time_sink_x_0_1_1_0, 0))
        self.connect((self.blocks_delay_0_1_1_0, 0), (self.qtgui_time_sink_x_0_2, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.b_Canal_AWGN_ff_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.blocks_delay_0_1, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.qtgui_time_sink_x_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_Retardo_Timing(int(self.Sps/2))
        self.set_Retardo_ojo(int(self.Sps/4))
        self.set_h(wform.rect(self.Sps))
        self.set_samp_rate(self.Rb*self.Sps)
        self.b_EYE_Timing_f_0.set_Sps(self.Sps)

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb
        self.set_samp_rate(self.Rb*self.Sps)
        self.qtgui_time_sink_x_0.set_samp_rate(self.Rb)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.Rb)
        self.qtgui_time_sink_x_0_1_1_0.set_samp_rate(self.Rb)
        self.qtgui_time_sink_x_0_2.set_samp_rate(self.Rb)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_Channel_BW(self.samp_rate/2.)
        self.b_Canal_AWGN_ff_0.set_samp_rate(self.samp_rate)
        self.b_EYE_Timing_f_0.set_Samprate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_1_1.set_samp_rate(self.samp_rate)

    def get_Retardo_Timing(self):
        return self.Retardo_Timing

    def set_Retardo_Timing(self, Retardo_Timing):
        self.Retardo_Timing = Retardo_Timing
        self.set_Retardo_bits(self.Retardo_Timing+1)
        self.E3TRadio_diezma_ff_0.set_ka(self.Retardo_Timing)
        self.b_EYE_Timing_f_0.set_Retardo_Timing(self.Retardo_Timing)

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_impulso(self):
        return self.impulso

    def set_impulso(self, impulso):
        self.impulso = impulso

    def get_h(self):
        return self.h

    def set_h(self, h):
        self.h = h
        self.interp_fir_filter_xxx_0.set_taps(self.h)

    def get_Retardo_ojo(self):
        return self.Retardo_ojo

    def set_Retardo_ojo(self, Retardo_ojo):
        self.Retardo_ojo = Retardo_ojo
        self.b_EYE_Timing_f_0.set_Delay(self.Retardo_ojo)

    def get_Retardo_bits(self):
        return self.Retardo_bits

    def set_Retardo_bits(self, Retardo_bits):
        self.Retardo_bits = Retardo_bits
        self.blocks_delay_0.set_dly(self.Retardo_bits)

    def get_Retardo_T4(self):
        return self.Retardo_T4

    def set_Retardo_T4(self, Retardo_T4):
        self.Retardo_T4 = Retardo_T4
        self.blocks_delay_0_1_0.set_dly(self.Retardo_T4)
        self.blocks_delay_0_1_0_0.set_dly(self.Retardo_T4)

    def get_Retardo_T3(self):
        return self.Retardo_T3

    def set_Retardo_T3(self, Retardo_T3):
        self.Retardo_T3 = Retardo_T3
        self.blocks_delay_0_1.set_dly(self.Retardo_T3)
        self.blocks_delay_0_1_1.set_dly(self.Retardo_T3)
        self.blocks_delay_0_1_1_0.set_dly(self.Retardo_T3)

    def get_No_dB(self):
        return self.No_dB

    def set_No_dB(self, No_dB):
        self.No_dB = No_dB
        self.b_Canal_AWGN_ff_0.set_Ch_NodB(self.No_dB)

    def get_Channel_BW(self):
        return self.Channel_BW

    def set_Channel_BW(self, Channel_BW):
        self.Channel_BW = Channel_BW
        self.b_Canal_AWGN_ff_0.set_BW(self.Channel_BW)

    def get_Ab(self):
        return self.Ab

    def set_Ab(self, Ab):
        self.Ab = Ab




def main(top_block_cls=top_block, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
