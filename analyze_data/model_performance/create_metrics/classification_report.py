import numpy as np
import pandas as pd
import sklearn.metrics as metrics

class Report: 
    def __init__(self, accuracy, precision, recall, f1):
        self.accuracy = accuracy
        self.precison = precision
        self.recall = recall
        self.f1 = f1

def make_classification_report(y_true, y_pred):
    class_report = metrics.classification_report(y_true, y_pred, output_dict=True)

    accuarcy = class_report['accuracy']
    precision = class_report['1']['precision']
    recall = class_report['1']['recall']
    f1 = class_report['1']['f1-score']

    report = Report(accuarcy, precision, recall, f1)
    return report 