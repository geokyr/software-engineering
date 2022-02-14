import argparse
import requests
import csv

my_parser = argparse.ArgumentParser(description='checks if there is connection with database')
my_parser.add_argument('--format', metavar='format', type=str, 
                        help='The format type of the output (select between json and csv)')
args = my_parser.parse_args()
input_format = args.format

r = requests.get('http://127.0.0.1:9103/admin/healthcheck')
data = r.json()

try:    
    if input_format == 'json':
        print(data)
    elif input_format == 'csv': 
        output_file = open('csv/healthcheck.csv', 'w')
        output = csv.writer(output_file)
        output.writerow(data.keys())
        output.writerow(data.values())
except Exception as e:
    print(e)