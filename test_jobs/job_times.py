import csv
import sys
import re
import datetime, time

csv.field_size_limit( 1000000 )
input_date_format = '%Y-%m-%d %H:%M:%S.%f'
input_date_format_alt = '%Y-%m-%d %H:%M:%S'

input_file = sys.argv[1]
output_file = sys.argv[2]
try:
	errors_file = sys.argv[3]	
except IndexError:
	errors_file = 'errors.csv'

print "%s ---> %s" % ( input_file, output_file )

i = open( input_file )
o = open( output_file, 'wb' )
e = open( errors_file, 'wb' )

reader = csv.reader( i, delimiter = '\t' )
writer = csv.writer( o )
error_writer = csv.writer( e )

headers = reader.next()

for line in reader:

	id = line[0]
	try:
		
		start_date = line[9]
		try:
			start_date = datetime.datetime.strptime( start_date, input_date_format )
		except ValueError:
			try:
				start_date = datetime.datetime.strptime( start_date, input_date_format_alt )
			except ValueError:			
				print line
				error_writer.writerow( line )
				continue
			
		start_timestamp = int( time.mktime( start_date.timetuple()))
		
		end_date = line[10]
		try:
			end_date = datetime.datetime.strptime( end_date, input_date_format )
		except ValueError:
			try:
				end_date = datetime.datetime.strptime( end_date, input_date_format_alt )
			except ValueError:			
				print line
				error_writer.writerow( line )
				continue			
			
		end_timestamp = int( time.mktime( end_date.timetuple()))
		
		new_line = [ id, start_timestamp, end_timestamp ]
		writer.writerow( new_line )
		
	except IndexError:
		error_writer.writerow( line )
		print id

	
	


		
		
		
		
		
		
		