kaggle-jobs
===========

1. download and unpack splitjobs.zip
2. extract job start & end timestamps for each window 

`job_times.py <input file> <output file> [<errors file>]`

```
job_times.py jobs1.tsv jobs1.csv errors1.csv
job_times.py jobs2.tsv jobs2.csv errors2.csv
job_times.py jobs3.tsv jobs3.csv errors3.csv
job_times.py jobs4.tsv jobs4.csv errors4.csv
job_times.py jobs5.tsv jobs5.csv errors5.csv
job_times.py jobs6.tsv jobs6.csv errors6.csv
job_times.py jobs7.tsv jobs7.csv errors7.csv
```

3. extract test jobs

`test_jobs.py window_dates.tsv`

`test_jobs.py` expects timestamps in jobsX.csv and will put test jobs in test_jobsX.csv, where X is a window number.