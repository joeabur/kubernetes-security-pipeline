# ZAP Report

ZAP by [Checkmarx](https://checkmarx.com/).


## Summary of Alerts

| Risk Level | Number of Alerts |
| --- | --- |
| High | 0 |
| Medium | 0 |
| Low | 1 |
| Informational | 0 |




## Insights

| Level | Reason | Site | Description | Statistic |
| --- | --- | --- | --- | --- |
| Low | Warning |  | ZAP warnings logged - see the zap.log file for details | 1    |
| Info | Informational | http://127.0.0.1:8080 | Percentage of responses with status code 2xx | 40 % |
| Info | Informational | http://127.0.0.1:8080 | Percentage of responses with status code 4xx | 60 % |
| Info | Informational | http://127.0.0.1:8080 | Percentage of endpoints with content type application/json | 100 % |
| Info | Informational | http://127.0.0.1:8080 | Percentage of endpoints with method GET | 100 % |
| Info | Informational | http://127.0.0.1:8080 | Count of total endpoints | 3    |




## Alerts

| Name | Risk Level | Number of Instances |
| --- | --- | --- |
| Server Leaks Version Information via "Server" HTTP Response Header Field | Low | 1 |




## Alert Detail



### [ Server Leaks Version Information via "Server" HTTP Response Header Field ](https://www.zaproxy.org/docs/alerts/10036/)



##### Low (High)

### Description

The web/application server is leaking version information via the "Server" HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.

* URL: http://127.0.0.1:8080/robots.txt
  * Node Name: `http://127.0.0.1:8080/robots.txt`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `secure-demo-api Python/3.14.4`
  * Other Info: ``


Instances: 1

### Solution

Ensure that your web server, application server, load balancer, etc. is configured to suppress the "Server" header or provide generic details.

### Reference


* [ https://httpd.apache.org/docs/current/mod/core.html#servertokens ](https://httpd.apache.org/docs/current/mod/core.html#servertokens)
* [ https://learn.microsoft.com/en-us/previous-versions/msp-n-p/ff648552(v=pandp.10) ](https://learn.microsoft.com/en-us/previous-versions/msp-n-p/ff648552(v=pandp.10))
* [ https://www.troyhunt.com/shhh-dont-let-your-response-headers/ ](https://www.troyhunt.com/shhh-dont-let-your-response-headers/)


#### CWE Id: [ 497 ](https://cwe.mitre.org/data/definitions/497.html)


#### WASC Id: 13

#### Source ID: 3


