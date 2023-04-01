import csv

def crafter_revenue_total(csv_file):
    total = 0
    with open(sales_file) as file_handle:
        csv_reader = csv.reader(file_handle)
        next(csv_reader) # Skip header row
        for row in csv_reader:
            date, sales = row[0], float(row[1])
            year, month = int(date[0:4]), int(date[5:7])
            if year == 2022 and month >= 4 or year == 2023 and month <= 3:
                total += sales
    return total

if __name__ == '__main__':
    sales_file = 'sales.csv'
    sales_total = crafter_revenue_total(sales_file)
    print(f'Crafter revenue generated from Apr 2022 to Mar 2023 is: ${sales_total:.2f}')
