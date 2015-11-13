[Previous](readme.md) |  [Next](exercise-02.md)
## Exercise 1: Overview of RESTful Web Services
RESTful web services are the currently dominate form of web services currently
being developed.  They took over the top spot from SOAP based web services if
you are interested in the history.

- They use standard HTTP methods: `GET`, `POST`, `PUT`, `PATCH`, `DELETE` in
consistent ways so that there is a general understanding of what different 
APIs will do across vendors/applications:
    - `GET`: Obtain a representation of a resource.
    - `POST`: Create a new resource.
    - `PUT`/`PATCH`: Update an existing resource with a representation.
    - `DELETE`: Remove a resource.
    
    > ![Information](../images/information.png) When dealing with RESTful 
    > web services, **resource** and **representation** are technical terms.
    > - Resource: An entity/object that exists in the target application.
    > This is often a database row.
    > - Representation: Since the web service can't actually give you the 
    > resource, it gives you a representation of a resource.
    
- Since RESTful web services piggyback on the HTTP protocol, the messages
that you send/receive from them correspond to standard request and response 
messages.  These type of messages consist of a set of headers and a 
body/payload.
    - In most cases, modern API message bodies are in [JSON](https://en.wikipedia.org/wiki/JSON).
    - Here's an example of a pair of request/response messages about my Github 
    account:
    
        ```
        curl -v -H "Authorization: token myauthorizationcode" https://api.github.com/user
        *   Trying 192.30.252.125...
        * Connected to api.github.com (192.30.252.125) port 443 (#0)
        > GET /user HTTP/1.1
        > Host: api.github.com
        > User-Agent: curl/7.43.0
        > Accept: */*
        > Authorization: token myauthorizationcode
        >
        < HTTP/1.1 200 OK
        < Server: GitHub.com
        < Date: Wed, 11 Nov 2015 01:52:21 GMT
        < Content-Type: application/json; charset=utf-8
        < Content-Length: 1553
        < Status: 200 OK
        <
        {
          "login": "eikonomega",
          "id": 415939,
          "avatar_url": "https://avatars.githubusercontent.com/u/415939?v=3",
          "gravatar_id": "",
          "url": "https://api.github.com/users/eikonomega",
          "html_url": "https://github.com/eikonomega",
          "followers_url": "https://api.github.com/users/eikonomega/followers",
          "following_url": "https://api.github.com/users/eikonomega/following{/other_user}",
          "gists_url": "https://api.github.com/users/eikonomega/gists{/gist_id}",
          "plan": {
            "name": "free",
            "space": 976562499,
            "collaborators": 0,
            "private_repos": 0
          }
        }
        ```
        
        - The lines that begin with `>` are part of the request and those
        that begin with `<` are part of the response.  After that is the 
        payload or response body, which is a JSON document.
        - About the Request
            - `GET /user HTTP/1.1` tells you the HTTP method being used(`GET`),
            the URL on the server being accessed (`/user`)and the protocol 
            being used(`HTTP/1.1`).
            - The lines after it that follow a `Key-Name:Value` format are
            the headers of the request.
        - About the Response
            - `HTTP/1.1 200 OK` Tells you the protocol of the response along
            with the **status code** and short description of that code. 
            Status codes are extremely important and we will be talking 
            more about them as we go on.
            - The rest of the lines are headers.
    
### Interacting with Web Services in Python
- There is a package in the standard library, `urllib2`, which can be used to 
  interact with web services.  However, just like we found with CLIs, there
  are community based alternatives.  In this particular case, almost no one
  uses the standard library. 
- This is because a friendly Pythonista named Kenneth Reitz came along and 
provided an awesome package called [`requests`](http://docs.python-requests.org/en/latest/) 
that really simplifies working with web APIs.  This is one of the reasons 
Python is awesome, because there are so many people out there creating 
awesome stuff and sharing it for free.

| [Next Exercise](exercise-02.md)