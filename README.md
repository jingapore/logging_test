# Purpose
To practise logging.

# gunicorn_logging
There are two scenarios.
- Run app using default development server that comes with Flask.
- Run app using gunicorn. We configure gunicorn logs for `access.log` and `error.log` in the config file `gunicorn.conf.py`.

In both scenarios, the app object is created with func `create_app()`. Logging happens thru `app.logger.info(<string to log>)`.

But complications arise under the scenario where gunicorn runs the app object. This is because the app object is not run with debug, and hence logs at "INFO" level do not log. 

Gunicorn's logs will still register logs at "INFO" level, if the app object's logger does it. What we have to do is to change the app object's logger to the Gunicorn handler (with `gunicorn_logger = logging.getLogger("gunicorn.error")` and `app.logger.handlers = gunicorn_logger.handlers` and also to set the level of app object's logger to that of the Gunicorn handler.

But we do not change the app object's logger, if it is not run using Gunicorn. To accomplish this, we add the following snippet:

```
if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=8000, debug=True)

elif __name__ != "__main__":
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app = create_app()
    app.logger.handlers = gunicorn_logger.handlers #change the app object's logger to the Gunicorn handler
    app.logger.setLevel(gunicorn_logger.level) #set the level of app object's logger to that of the Gunicorn handler
```