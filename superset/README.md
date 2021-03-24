Install a local copy

https://superset.apache.org/docs/installation/installing-superset-using-docker-compose

I made some changes to the instructions found in the doc above:

- make sure local PostgreSQL is stopped otherwise superset port conflict
- run into this problem https://github.com/apache/superset/issues/12723 with docker deskptop 2G - increased to 7.5G 

I did the followings:

- get code `git clone https://github.com/apache/superset.git`
- make sure to use master branch `git checkout master`
- change redis from 3.2 to latest in `docker-compose-non-dev.yml`
<img width="307" alt="Screen Shot 2021-03-23 at 9 51 25 PM" src="https://user-images.githubusercontent.com/595772/112242317-f9577580-8c21-11eb-807f-db9c1fdd04c7.png">
- use `docker-compose -f docker-compose-non-dev.yml up` to start the server
- wait some time and superset_init exited with 0 is expected - it does not affect the server:
<img width="468" alt="Screen Shot 2021-03-23 at 9 47 56 PM" src="https://user-images.githubusercontent.com/595772/112242376-1d1abb80-8c22-11eb-8393-75ff66cc196f.png">
- login at http://localhost:8088/ using admin/admin