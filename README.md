

## 1. Build the Docker image

```console
$ docker build -t fastapi-image-slim .
```

## 3. Run the Docker image

Normal:


```console
$ docker run --name myflaskapp-container -p 5000:5000 myflaskapp
```

Run in background and give a name:

```console
$ docker run -d --name myflaskapp-container -p 5000:5000 myflaskapp
```



`-p 5000:5000`: Map the port from outside to the port from the container

Host in Dockerfile must be:

`host: 0.0.0.0`: "placeholder", it tells a server to listen for and accept connections from any IP address ("all IPv4 addresses on the local machine").

## Progress Notes
Based on [this](https://medium.com/geekculture/how-to-dockerize-your-flask-application-2d0487ecefb8) \
Werkzeug==2.2.2 added to requirements after [errors running flask](https://stackoverflow.com/questions/77213053/why-did-flask-start-failing-with-importerror-cannot-import-name-url-quote-fr) 




## Next steps

Need to setup volumes so this useable in development \
https://flask.palletsprojects.com/en/2.2.x/tutorial/factory/
