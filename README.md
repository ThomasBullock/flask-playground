## Running apps with docker

`docker-compose up -d`

Based on this.
https://github.com/pratamawijaya/example-flask-mysql-docker
Upgarded docker-compose python / version

### logs

`docker-compose logs -f app`
`docker-compose logs -f db`

`python3 -m pip list -v`

## Discoveries

Had to install `mysql-connector-python` instead of `mysql-connector` after adding templates
as started getting

```
mysql.connector.errors.InterfaceError: 2003: Can't connect to MySQL server on 'db:3306' (111 Connection refused)
```

## 3. Old notes for before docker-compose

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

```
db/
flask/
  app/
    controllers/
      __init__.py
      employee_controller.py
    __init__.py
    config.py
    main.py
  Dockerfile
  requirements.txt
docker-compose.yaml
```

## Next steps

Need to setup volumes so this useable in development \
https://flask.palletsprojects.com/en/2.2.x/tutorial/factory/

### Istanbul

Get app into factory so we can use current_app
https://flask.palletsprojects.com/en/2.1.x/patterns/appfactories/
https://github.com/planetscale/mysql-for-python-developers/blob/main/webapp/final/hotel_management/db.py

https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/
https://github.com/vectornguyen76/flask-rest-api-template

Example database class for wrapping mysql-connector for python
https://gist.github.com/xeoncross/494947640a7dcfe8d91496988a5bf325
