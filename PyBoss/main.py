import os
import csv

emp_id = []
name = []
dob = []
ssn = []
state = []

#read csvfile
with open('employee_data1.csv') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	next(csvreader, None)
	print(csvreader)

	for row in csvreader:
		emp_id.append(row[0])
		firstname = row[1].split(" ")
		lastname = row[1].split(" ")
		#name.append(str
		dob.append(row[2])
		ssn.append(row[3])
		state.append(row[4])

#write csvfile somewhere else
with open('modded_employee_data1.csv', 'w') as writecsvfile:
	csvwriter = csv.writer(writecsvfile)
	csvwriter.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
	csvwriter.writerows(row)
