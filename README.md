## URL Insight API
The **URL Insight API** provides comprehensive data about a given URL, including:

1. **Domain Information**: Retrieves Whois details such as registration date, registrar, country, DNS servers, and domain status.


2. **HTTP Information**: Provides HTTP status code, response time, page size, and headers.


3. **HTTPS Information**: Extracts SSL certificate details like subject, issuer, and expiration date.


4. **General Information**: Includes content type, response size, and total response time.


5. **Security Information**: Fetches security headers like HSTS (Strict Transport Security) and Content Security Policy.


6. **Vulnerability Scan**: Scans the URL for known vulnerabilities on common ports (80 and 443).



To access this data, send a GET request with the URL parameter to the `/get_info` endpoint. For example:
`http://127.0.0.1:5000/get_info?URL=example.com`
