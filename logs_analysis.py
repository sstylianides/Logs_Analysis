#!/usr/bin/env python

import psycopg2

DBNAME = "newsdata"

def popular_articles():
    """Prints most popular three articles of all time"""
    db = psycopg2.connect(dbname="news")
    c = db.cursor()
    c.execute("select articles.title, count(*) as views "
    "from articles inner join log on log.path "
    "like concat('%', articles.slug, '%') "
    "where log.status like '%200%' group by "
    "articles.title, log.path order by views desc limit 3")
    result = c.fetchall()
    db.close()
    print "\nWhat are the three most popular articles of all time?\n"
    for i in range(0, len(result), 1):
        print "\"" + result[i][0] + "\" -- " + str(result[i][1]) + " views"
    print "\n\n"


def popular_authors():
    """Prints most popular article authors of all time"""
    db = psycopg2.connect(dbname="news")
    c = db.cursor()
    c.execute("select authors.name, count(*) as views from articles inner "
    "join authors on articles.author = authors.id inner join log "
    "on log.path like concat('%', articles.slug, '%') where "
    "log.status like '%200%' group "
    "by authors.name order by views desc")
    result = c.fetchall()
    db.close()
    print "\nWho are the most popular article authors of all time?\n"
    for i in range(0, len(result), 1):
        print result[i][0] + " -- " + str(result[i][1]) + " views"
    print "\n\n"


def log_status():
    """Print days on which more than 1% of requests lead to errors"""
    db = psycopg2.connect(dbname="news")
    c = db.cursor()
    c.execute("select Date,Total,Error,\
        (Error::float*100)/Total::float as Percent from\
        (select time::timestamp::date as Date, count(status) as Total,\
        sum(case when status = '404 NOT FOUND' then 1 else 0 end) as Error\
        from log group by time::timestamp::date) as result\
        where (Error::float*100)/Total::float > 1.0 order by Percent desc")
    result = c.fetchall()
    db.close()
    print "\nWhich days did more than 1% of requests lead to errors?\n"
    for i in range(0, len(result), 1):
        print str(result[i][0])+ " -- "+str(round(result[i][3], 3))+"% errors\n\n"

if __name__ == '__main__':


    popular_articles()
    popular_authors()
    log_status()