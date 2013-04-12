#Navodila za SSL

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
