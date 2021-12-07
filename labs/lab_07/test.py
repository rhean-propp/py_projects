#!/usr/bin/python3

from ctypes import *

class student:
    def __init__(self, name, studentID, classes, scores, scores2):
        self.name = name
        self.student = studentID
        self.classes = classes
        self.scores = scores
        self.scores2 = scores2

c_name = (c_char*30)(*(b"Rhean"))
c_studentID = (c_int)(1234)
c_classes = (c_char*30)(*(b"ITSC203"))
c_scores = (c_int*30)(10, 20, 30, 40)
c_scores2 = (c_float*30)(4.0)

rhean = student(c_name, c_studentID, c_classes, c_scores, c_scores2)