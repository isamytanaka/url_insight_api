from flask import Flask, jsonify, request
import requests
import whois
import ssl
import socket
import nmap
import datetime

app = Flask(__name__)

def get_domain_info(url):
    try:
        domain_info = whois.whois(url)
        return {
            "domain": domain_info.domain_name,
            "registration_date": domain_info.creation_date,
            "expiration_date": domain_info.expiration_date,
            "registrar": domain_info.registrar,
            "country": domain_info.country,
            "dns_servers": domain_info.name_servers,
            "status": domain_info.status,
            "last_updated": domain_info.last_updated
        }
    except Exception as e:
        return {"error": f"Error retrieving Whois data: {str(e)}"}

def get_http_info(url):
    try:
        response = requests.get(url)
        return {
            "http_status": response.status_code,
            "response_time": response.elapsed.total_seconds(),
            "page_size": len(response.content),
            "headers": dict(response.headers)
        }
    except requests.exceptions.RequestException as e:
        return {"error": f"Error making HTTP request: {str(e)}"}

def get_https_info(url):
    try:
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=url) as s:
            s.connect((url, 443))
            cert = s.getpeercert()
            return {
                "https_active": True,
                "ssl_certificate": {
                    "subject": dict(cert.get('subject', [])),
                    "issuer": dict(cert.get('issuer', [])),
                    "validity_date": cert.get('notAfter', 'Not available')
                }
            }
    except Exception as e:
        return {"https_active": False, "https_error": str(e)}

def get_http_headers(url):
    try:
        response = requests.head(url)
        return {
            "http_headers": dict(response.headers),
            "status_code": response.status_code
        }
    except requests.exceptions.RequestException as e:
        return {"error": f"Error retrieving HTTP headers: {str(e)}"}

def get_general_info(url):
    try:
        response = requests.get(url)
        content_type = response.headers.get('Content-Type', 'Unknown')
        return {
            "content_type": content_type,
            "response_size": len(response.content),
            "response_time": response.elapsed.total_seconds()
        }
    except requests.exceptions.RequestException as e:
        return {"error": f"Error retrieving general info: {str(e)}"}

def get_security_info(url):
    try:
        response = requests.get(url)
        hsts = response.headers.get('Strict-Transport-Security', 'Not Set')
        return {
            "hsts": hsts,
            "content_security_policy": response.headers.get('Content-Security-Policy', 'Not Set')
        }
    except requests.exceptions.RequestException as e:
        return {"error": f"Error retrieving security info: {str(e)}"}

def scan_vulnerabilities(url):
    try:
        nm = nmap.PortScanner()
        nm.scan(hosts=url, arguments='-p 80,443 --script vuln')
        vulnerabilities = {}
        for host in nm.all_hosts():
            vulnerabilities[host] = {}
            for proto in nm[host].all_protocols():
                vulnerabilities[host][proto] = {}
                lport = nm[host][proto].keys()
                for port in lport:
                    vulnerabilities[host][proto][port] = nm[host][proto][port]
        return vulnerabilities
    except Exception as e:
        return {"error": f"Error performing vulnerability scan: {str(e)}"}

@app.route('/get_info', methods=['GET'])
def get_url_info():
    url = request.args.get('URL')
    
    if not url:
        return jsonify({"error": "URL not provided!"}), 400
    
    domain_info = get_domain_info(url)
    http_info = get_http_info(url)
    https_info = get_https_info(url)
    headers_info = get_http_headers(url)
    general_info = get_general_info(url)
    security_info = get_security_info(url)
    vulnerabilities = scan_vulnerabilities(url)
    
    result = {
        "domain": domain_info,
        "http_info": http_info,
        "https_info": https_info,
        "headers_info": headers_info,
        "general_info": general_info,
        "security_info": security_info,
        "vulnerabilities": vulnerabilities
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)