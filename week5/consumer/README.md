```$docker build -t consumer .```

```$docker run -i -p 8080:80 -v "$(pwd)/code:/app" consumer```

http://127.0.0.1:8080