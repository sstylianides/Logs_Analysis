# Log-Analysis-Udacity-Project
A reporting tool that prints out reports based on data from a web server's database.

## Intro
The information in this database is a newspaper website's raw data that contains articles, the author of articles, and entries for each time a user accessed the website. The purpose of this reporting tool is to determine the most popular three articles of all time, the most popular article authors of all time, and the days on which more than 1% of requests lead to errors.



## Instructions
1. Install Vagrant and VirtualBox.
2. Clone this repository using git or download a zip of the repository.
3. Start the virtual machine
4. Launch Vagrant VM by running 'vagrant up', then log in with 'vagrant ssh'
5. Download the <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip">data.</a>  Unzip the file after downloading it. The file inside is called newsdata.sql
6. Place the file into the vagrant directory
7. Setup database with the following command:
  <pre>psql -d news -f newsdata.sql;</pre>
8. Run Module
  <pre>python logs_analysis.py</pre>