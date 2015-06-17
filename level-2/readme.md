![Welcome to Level 2](http://i610.photobucket.com/albums/tt185/louper_anguano/KungFuPandaTh4nosAC35106010718-22-1.png)
# Level Two: Interacting with Web Services

## PyCharm Project Setup
* Open a new project folder: `[repo-location]/trainee-area/level-2/using-web-services`
* Set the project interpreter
![Project Interpreter Settings](project-interpreter.png)
* Probably restart PyCharm due to software bug in latest version.

## Training Topics

### Overview of Modern Web Services/APIs
* What are web services/web APIs?
* The currently dominate form of web services: RESTful.
    * Uses HTTP(s) protocol with standard methods: GET/POST/PUT/PATCH/DELETE
    * Messages consist of headers and a body/payload.
    * In most cases, modern APIs message bodies are in [JSON](https://en.wikipedia.org/wiki/JSON).
    ```
    Example HTTP Response from a RESTful Web Api
    
    * Hostname was NOT found in DNS cache
    *   Trying 198.41.141.12...
    * Connected to api.searchcompany.us (198.41.141.12) port 80 (#0)
    > GET /1.0/search/indiana HTTP/1.1
    > User-Agent: curl/7.37.1
    > Host: api.searchcompany.us
    > Accept: */*
    >
    < HTTP/1.1 200 OK
    < Date: Wed, 17 Jun 2015 10:58:24 GMT
    < Content-Type: application/json
    < Content-Length: 934
    < Connection: keep-alive
    < Set-Cookie: __cfduid=d4717386495ace30d0c6912d3e60ca8921434538704; expires=Thu, 16-Jun-16 10:58:24 GMT; path=/; domain=.searchcompany.us; HttpOnly
    < X-Powered-By: PHP/5.3.3
    < Set-Cookie: PHPSESSID=kr2f3vs0po4gpm5meqgcajqh54; path=/
    < Expires: Thu, 19 Nov 1981 08:52:00 GMT
    < Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
    < Pragma: no-cache
    * Server cloudflare-nginx is not blacklisted
    < Server: cloudflare-nginx
    < CF-RAY: 1f7e3d3484d610d5-ORD
    <
    * Connection #0 to host api.searchcompany.us left intact
    {"total":7250,"page":1,"company":[{"id":260842,"name":"Indiana Street Baptist"},{"id":260843,"name":"Indiana Street Elem School"},{"id":814732,"name":"Indiana Street Home Assn"},{"id":1019270,"name":"Indiana Auto"},{"id":1019271,"name":"Indiana Business Park"},{"id":1019272,"name":"Indiana Car Care"},{"id":1019273,"name":"Indiana Liquor"},{"id":1019274,"name":"Indiana Market & Deli"},{"id":1735347,"name":"LA Indiana Tamales"},{"id":1949304,"name":"Indiana Carpet & Supply"},{"id":1949305,"name":"Indiana Dairy"},{"id":1949306,"name":"Indiana Home Supply"},{"id":1949308,"name":"Indiana Market"},{"id":1949312,"name":"Indiana's Barber Shop"},{"id":2237716,"name":"Indiana Building Engineer's"},{"id":3620858,"name":"Indiana Manor"},{"id":4144818,"name":"Indiana Downs Off-Track Bettin"},{"id":4156532,"name":"Indiana Beach Inc"},{"id":4169114,"name":"Dacco-Detroit Of Indiana"},{"id":4180593,"name":"Indiana Presbyterian Church"}]}
    
    ```
    
### Interacting with Web Services in Python
* There is a package in the standard library, `urllib2`, which can be used to 
  interact with web services.  However, it is not very easy to use... :(
* But, a friendly Pythonista named Kenneth Reitz came along and provided an 
awesome package called [`requests`](http://docs.python-requests.org/en/latest/) that really simplifies working with web
apis.  This is one of the reasons Python is awesome, because there are 
so many people out there creating awesome stuff and sharing it for free.

[Start Training](exercise-1.md)