#Instructions for SSL

##Mac OS X:

1. Premakni se v root direktorij od projekta.
2. Preveri, če imaš datoteko dev_https, ki je potrebna za tunel.
3. Zaženi ssl tunel z ukazom: 
	
	`stunnel dev_https_`
	
4. Zaženi server z ukazom:
	
	`HTTPS=on python manage.py runserver`
	
5. V brskalniku odpri stran:

	<https://localhost:8443>

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



#Navodila za Celery
<http://blog.azreda.org/2012/09/asynchronous-tasks-complete-celery-with.html>

<http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html>