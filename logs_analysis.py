#!/usr/bin/env python

import psycopg2
from texttable import Texttable

# Define db name
DBNAME = "news"


def answer_question_1():

    """Part 1. Top Ranked Articles by Title:"""

    # Connect to an existing database
    db = psycopg2.connect(database=DBNAME)
    # Create a cursor
    c = db.cursor()
    # Execute a command with cursor
    c.execute("""select articles.title, count(log.path) as views
        from articles, log
        where log.path = concat('/article/', articles.slug)
        group by articles.title
        order by views desc
        limit 3;""")
    # Return results
    results = c.fetchall()
    # Close connection
    db.close()
    # Give section a header
    print('\n' + 'Three most popular articles' + '\n')
    # Create texttable to present data
    t = Texttable()
    # Feed in values from db
    t.header(['Title', 'Views'])
    t.add_rows(results, header=False)
    # Draw the table
    print(t.draw())


answer_question_1()


def answer_question_2():

    """Part 2. Top ranked author by views of their articles"""

    # Connect to an existing database
    db = psycopg2.connect(database=DBNAME)
    # Create a cursor
    c = db.cursor()
    # Execute a command with cursor
    c.execute("""select authors.name, count(log.path) as views
        from authors, articles, log
        where authors.id = articles.author
        and log.path = concat('/article/', articles.slug)
        group by authors.name
        order by views desc;""")
    # Return results
    results = c.fetchall()
    # Close connection
    db.close()
    # Print answer to question
    print('\n')
    # Give section a header
    print('\n' + 'Top ranked author by article views')
    # Create texttable to present data
    t = Texttable()
    # Feed in values from db
    t.header(['Name', 'Views'])
    t.add_rows(results, header=False)
    # Draw the table
    print('\n')
    print(t.draw())


answer_question_2()


def answer_question_3():

    """
Part 3. Which days did more than 1% of requests lead to errors?"""

    # Connect to an existing database
    db = psycopg2.connect(database=DBNAME)
    # Create a cursor
    c = db.cursor()
    # Run SQL query with cursor
    c.execute("""select to_char(day, 'FMMonth FMDD, YYYY'),
        round(cast(ratio as numeric), 2)
        from ratios where ratio > 1;""")
    # Return results
    results = c.fetchall()
    # Close connection
    db.close()
    # Print answer to question
    print('\n')
    # Give section a header
    print('Days where more than 1% of requests lead to errors')
    # Create texttable to present data
    t = Texttable()
    # Feed in values from db
    t.header(['Date', '% of Errors'])
    t.add_rows(results, header=False)
    # Draw the table
    print('\n')
    print(t.draw())
    print('\n')


answer_question_3()
