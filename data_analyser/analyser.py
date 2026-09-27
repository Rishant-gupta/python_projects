import csv
from utils import timer, logger

class Dataset:

    def __init__(self, filepath):
        self.filepath = filepath
        self.row = []
        self.column = []

    @logger
    @timer
    def load(self):

        try:
            with open(self.filepath) as f:
                reader = csv.DictReader(f)

                if reader.fieldnames is None:
                    raise ValueError("file is empty")
               
                self.column = reader.fieldnames

                for row in reader:
                    self.row.append(row)
                
        except FileNotFoundError as e:
            print("Found error ", e) 
            return

        
    @logger   
    @timer   
    def display(self):

        for col_name in self.column:
            print(f"| {col_name} | \t", end="")
        print()

        for row in self.row:
            for value in row.values():
                print(f"| {value} | \t", end="")
            print()

    @logger
    @timer
    def filter(self, col, on):
        if col not in self.column:
            raise KeyError("Given column does not exist")
        
        filt = (row for row in self.row  if row[col] == on)
        
        return filt

    @logger
    @timer
    def statistics(self):
        
        for col in self.column:
            num = []
            for row in self.row:
                try:
                    num.append(float(row[col]))
                except ValueError:
                    num = []
                    break
            if not num:
                continue
            
            num.sort()
            l = len(num)

            mean = sum(num) / l
            
            if l % 2 == 0:
                median = (num[l // 2 - 1] + num[l // 2]) / 2
                
            else:
                median = num[l // 2]
                


            print(f"{col}:\nmean:\t{mean:.2f}\nmedian:\t{median}\nmax:\t{max(num)}\nmin:\t{min(num)}")
            

   
    @logger
    @timer
    def search(self, keyword):

        sea_lst = [row for row in self.row if keyword.lower() in " ".join([str(val).lower() for val in row.values()])]

        if not sea_lst:
            print("No such keyword found")
        else:
            print(f"{len(sea_lst)} row is found match with keyword")

        return sea_lst
    
    @logger
    @timer
    def sort(self, column, descending = False):
        if column not in self.column:

            raise KeyError("NO such column is found in data")
        
        sot = sorted(self.row, key=lambda row: row[column], reverse=descending)
   
        return sot
        
    @logger
    @timer
    def save(self, rows, filepath):
        if not rows:
            raise ValueError("No data found to write ")
        
        try:
            
            with open(filepath, "w", newline = "") as f:
                writer = csv.DictWriter(f, fieldnames=self.column)
                writer.writeheader()
                writer.writerows(rows)

        except FileNotFoundError as e:
            print("No such directory found", e)


    