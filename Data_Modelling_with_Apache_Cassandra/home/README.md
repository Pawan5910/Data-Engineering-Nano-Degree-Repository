# DATA WAREHOUSE PROJECT

In this project, as a Data Engineer for a music streaming stratup 'Sparkify', the user and the song data into the cloud. Their data is stored in a directory of JSON logs on user activity and in a directory of JSON metadata on the songs. These data are stored in ***S3***.

Here an ETL pipeline is built to extract the data from S3, and is staged in ***Redshift***, which is later transformed into a set of dimensional and fact tables to be used for analytics.



## DATABASE SCHEMA DESIGN

This section discusses about the schema design that is used in this project. The schema includes 2 parts, **Staging tables** and **Analytical tables**.

### STAGING TABLES

**staging_events** : This table stores the user activity data extracted from the JSON logs directory. The columns in the table are *artist, auth, firstName, gender, itemInSession, lastName, length, level, location, method, page, registration, sessionId, song, status, ts, userAgent, userId*.

**staging_events** : This table stores the song data extracted from the JSON metadata directory. The columns in the table are *num_songs, artist_id, artist_latitude, artist_longitude, artist_location, artist_name, song_id, title, duration, year*.

### ANALYTICAL TABLE

***Fact Table***

**songplays**: Contains the event data that the song plays. The columns of this table are *songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent*

***Dimension Table***

**users**: Contains the user data. The columns are *user_id, first_name, last_name, gender, level*
**songs** : Contains the data of the songs in the database. the columns are *song_id, title, artist_id, year, duration*
**artists** : Contains the data of the artists in the music datbase. The columns are *artist_id, name, location, latitude, longitude*
**time** : Contains specific units of the timestamps of records of the songs. The columns are *start_time, hour, day, week, month, year, weekday*


## ETL

The project comprises of three files.

1) [create_tables.py](create_tables.py) : This is to drop all the exisiting tables and creates new tables. 

2) [sql_queries.py](sql_queries.py) : The new tables are created as per teh queries in this file.

3) [etl.py](etl.py) : This file populates the fact and dimension tables by extracting data from S3.

4) [project.py](project.py) : Here the aws resorces are set up and create table and etl pipeline files are run here.











