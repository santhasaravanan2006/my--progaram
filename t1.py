import sys
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout
from PyQt5.QtWidgets import QFileDialog,QLabel,QTableWidget,QTableWidgetItem,QMessageBox
class Some_data(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800,600)
        self.df=None
        self.setWindowTitle("Data Analyzer")
        self.load=QPushButton("uplode csv file",self)
        self.table=QTableWidget(self)
        self.info=QLabel("UPLODE CSV FILE",self)
        self.graph=QPushButton("SHOW GRAPH",self)
        self.initUI()
        self.load.clicked.connect(self.load_file)
        self.graph.clicked.connect(self.Graph_plot)


    def initUI(self):
        vbox=QVBoxLayout(self)
        vbox.addWidget(self.load)
        vbox.addWidget(self.info)
        vbox.addWidget(self.table)
        vbox.addWidget(self.graph)
        self.setLayout(vbox)

    
    def load_file(self):
        file_path, _=QFileDialog.getOpenFileName(
            self,
            "Open CSV File",
            "",
            "CSV Files(*.csv)"
            )
        if file_path:
            self.df=pd.read_csv(file_path)
            self.show_table()
            self.info.setText(f"ROWS:{self.df.shape[0]} Columns:{self.df.shape[1]}")
            
    def show_table(self):
        self.table.setRowCount(len(self.df))
        self.table.setColumnCount(len(self.df.columns))
        self.table.setHorizontalHeaderLabels(self.df.columns)
        for rows in range(len(self.df)):
            for cols in range(len(self.df.columns)):
                self.table.setItem(rows,
                                   cols,
                                   QTableWidgetItem(str(self.df.iat
                                   [rows,cols]))
                                   )
    def Graph_plot(self):
        if self.df is not None:
            numeric=self.df.select_dtypes(include="number")
            if not numeric.empty:
                numeric.iloc[:,0].plot()
                plt.title("DATA PLOT")
                plt.show()
            else:
                QMessageBox.warning(self,"Error","No numeric columns found")
        
        
def main():
    app=QApplication(sys.argv)
    window=Some_data()
    window.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()