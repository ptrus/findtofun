#Mac OS X:
#Instructions for SSL

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
Pomoč v angleščini:  
<http://www.ianlewis.org/en/testing-https-djangos-development-server>


##Windows:

###1. Stunnel:

1. Download & Install stunnel:

    <https://www.stunnel.org/index.html>

2. Open stunnel.exe (ex: C:\Program Files (x86)\stunnel\stunnel.exe).

3. Click on Configuration->Edit stunnel.conf. Replace all with:

        cert=C:\Program Files (x86)\stunnel\stunnel.pem  
        fips = no      
        
        [https]  
        accept=8443  
        connect=8000  
        TIMEOUTclose=1  
 

4. Save stunnel.conf and press Reload stunnel.conf.

Help:  
<https://www.stunnel.org/howto.html>


###2. Rabbitmq:

1. Download & Install rabbitmq:

    <http://www.rabbitmq.com/>

2. Open cmd as **administrator**!

3. In console go to installation directory (ex: C:\Program Files (x86)\RabbitMQ Server\rabbitmq_server-3.1.0\sbin\).

4. Start RabbitMQ server with typing into console:

    `rabbitmq-server.bat`


###3. Start srever:

1. Start server with:
    
        python manage.py runserver



1. Install memcached.

2. Install python binding to memcached.

3. Run memcached:

	`memcached`
	
	You can run as daemon with flag: `-d`


