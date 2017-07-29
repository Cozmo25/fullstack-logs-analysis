# Logs Analysis Project

# INSTRUCTIONS

## How to run the project
1. Download the project folder (logs-analysis)
2. Project Python & python library dependencies are:
    * Vagrant Linux VM
    * Python 2.7
    * newsdata.sql
    * psycopg2
    * Texttable
    * logs_analysis.py
Note: -- logs_analysis.py files is included in the project folder. pysycop2 and Textable can be installed via pip (see relevant documentation for how to install). Follow the project info & description link to set up the linux VM and create the necessary datatables from newsdata.sql (using command psql -d news -f newsdata.sql). There is nothing further for the user to install.
3. Launch your favourite python IDE
4. Navigate to the project folder and run the logs_analysis.py file
5. The file will output the answers to the questions described in the project description below in sequential order in formatted tables (see Note for details of how to create relevant views)
6. Sample output from the program is contained in output.txt in the project folder


### Notes & Acknowledgments

Creation of views used to answer Part 3:

Errors view SQL:
```
create or replace view errors as select cast(count(status) as float) as num, date(time) as day from log
where status != '200 OK'
group by day
order by day;
```
Total view SQL:
```
create or replace view total as select cast(count(status) as float) as num, date(time) as day from log
group by day
order by day;
```
Ratio view SQL:
```
create view ratios as select sum(errors.num) / sum(total.num) * 100 as ratio, total.day from errors, total where errors.day = total.day
group by total.day
order by total.day;
```

Thanks to the following sources for assistance with various elements of the project:
* [Udacity Full Stack Developer Course Notes](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)
* [Python 2.7 Documentation](https://docs.python.org/2/index.html)
* [Udactiy Forums](https://discussions.udacity.com)
* [PostgreSQL Documentation](https://www.postgresql.org/docs/9.5/static/index.html)
* [Stackoverflow Forums](https://www.stackoverflow.com)
* [Texttable Documentation](https://github.com/foutaise/texttable/)

______________________________________________________________________________

## PROJECT INFO & DESCRIPTION

[Link to Project Info](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/262a84d7-86dc-487d-98f9-648aa7ca5a0f/concepts/079be127-2d22-4c62-91a8-aa031e760eb0)

### Your assignment: Build it!

Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

So what are we reporting, anyway?
Here are the questions the reporting tool should answer. The example answers given aren't the right ones, though!

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

Example:

* "Princess Shellfish Marries Prince Handsome" — 1201 views
* "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
* "Political Scandal Ends In Political Scandal" — 553 views

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

Example:

* Ursula La Multa — 2304 views
* Rudolf von Treppenwitz — 1985 views
* Markoff Chaney — 1723 views
* Anonymous Contributor — 1023 views

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer back to this lesson if you want to review the idea of HTTP status codes.)

Example:

* July 29, 2016 — 2.5% errors

Good coding practices

SQL style
Each one of these questions can be answered with a single database query. Your code should get the database to do the heavy lifting by using joins, aggregations, and the where clause to extract just the information you need, doing minimal "post-processing" in the Python code itself.

In building this tool, you may find it useful to add views to the database. You are allowed and encouraged to do this! However, if you create views, make sure to put the create view commands you used into your lab's README file so your reviewer will know how to recreate them.

Python code quality
Your code should be written with good Python style. The PEP8 style guide is an excellent standard to follow. You can do a quick check using the pep8 command-line tool.

