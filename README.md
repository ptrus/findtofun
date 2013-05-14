#Mac OS X:

## Setup

1. Make sure to install everything beneath.

2. Then run stunnel, rabbitmq, memecached.

	1. You can run `prepare_server.sh` to do this.

3. Run server:

	`python manage.py runserver`
	
4. Open page: <https://localhost:8443>


##Stunnel

1. Install stunnel.

2. Move to project's root and make sure that file dev_https is in it, which is needed for stunnel.

3. Run stunnel: 
	
	`stunnel dev_https_`
	
4. Additional help:  
<http://www.ianlewis.org/en/testing-https-djangos-development-server>
	
##RabbitMQ

1. Install rabbitmq.

2. Run rabbitmq:

	`rabbitmq-server`
	
3. You can run celery's workers:

	`python manage.py celery worker --loglevel=info`
	
	To log in file, add flag:
	
	`--logfile=/path/to/log/file.txt`

##Memcached

1. Install memcached.

2. Install python binding to memcached.

3. Run memcached:

	`memcached`
	
	You can run as daemon with flag: `-d`


