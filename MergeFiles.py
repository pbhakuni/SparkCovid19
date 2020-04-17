#/home/hduser/Desktop/Spark/Covid19Datasets
#Total 78 files to merge with different fields

import glob
import csv
filelist = glob.glob("/home/hduser/Desktop/Spark/Covid19Datasets/New_covid_reports/*.csv")
fieldnames = []

#Getting list of filenames
for filename in filelist:
    with open(filename, "r", newline="") as fileref_in:
        reader = csv.reader(fileref_in)
        headers = next(reader)
        for h in headers:
            if h not in fieldnames:
                fieldnames.append(h)


with open("/home/hduser/Desktop/Spark/Covid19Datasets/New_covid_reports/mergedcovid19.csv", "w", newline="") as fileref_out:
    writer = csv.DictWriter(fileref_out, fieldnames=fieldnames)
    writer.writeheader()

    for filename in filelist:
        with open(filename, "r", newline="") as fileref_in:
            reader = csv.DictReader(fileref_in)
            for line in reader:
                writer.writerow(line)
