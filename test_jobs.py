import sys, csv, datetime, time

input_date_format = '%Y-%m-%d %H:%M:%S'

dates_file = sys.argv[1]

d = open( dates_file )
reader = csv.reader( d, delimiter = "\t" )

headers = reader.next()

for line in reader:
	window = line[0]
	start_date = line[2]
	end_date = line[3]
	
	print "window %s, %s - %s" % ( window, start_date, end_date )
	
	start_date = datetime.datetime.strptime( start_date, input_date_format )
	end_date = datetime.datetime.strptime( end_date, input_date_format )

	start_timestamp = int( time.mktime( start_date.timetuple()))
	end_timestamp = int( time.mktime( end_date.timetuple()))

	i = open( 'jobs%s.csv' % ( window ))
	jobs_reader = csv.reader( i )
	
	o = open( 'test_jobs%s.csv' % ( window ), 'wb' )
	writer = csv.writer( o )
	
	all = 0
	selected = 0
	
	for l in jobs_reader:
		all += 1
		job = l[0]
		s = int( l[1] )
		e = int( l[2] )
		if s < end_timestamp and e > start_timestamp:
			writer.writerow( [job] )
			selected += 1
			
	print "%s / %s" % ( selected, all )
	i.close()