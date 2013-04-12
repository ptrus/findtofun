#Navodila za SSL

##Mac OS X:

1. Premakni se v root direktorij od projekta.
2. Preveri, če imaš datoteko dev_https, ki je potrebna za tunel.
3. Zaženi ssl tunel s sledečim ukazom: 
	
	`stunnel dev_https_`
	
4. Zaženi server s sledečim ukazom:
	
	`HTTPS=on python manage.py runserver`
	
5. V brskalniku odpri sledečo stran:

	__https://localhost:8443__

Pomoč v angleščini:  
<http://www.ianlewis.org/en/testing-https-djangos-development-server>
