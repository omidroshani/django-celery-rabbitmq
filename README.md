# Django + Celery + RabbitMQ

## 1. Run project
Run all services with docker:
```
docker-compose up --build -d
```

## 2. Login to admin panel
Visit this url:
```
http://localhost:8080/admin
```
and this is the credentials:
```
username : admin@admin.com
password : admin
```

## 3. Setup celery tasks
This task's duty is adding it's two arguments and return the result.
1. In the admin panel from sidebar click on the `+ Add` button besides `Periodic tasks` item.
2. Enter a sample name for your task and select `analytics.tasks.sample_task` for Task.<br>
3. In the `Schedule` section add new crontab schedule by clicking on `+` button.<br>
For example: `*/5 * * * *`<br>
4. In the arguments section add a sample arguments like `[1,2]`
5. Click on `save` button
6. You can see the results of the task by clicking on the `Task Results` in the left sidebar.

## 4. Run task with Endpoint
Visit this URL to run the sample task with `(1,2)` arguments. You can see the results of the task by clicking on the `Task Results` in the left sidebar.
```
http://localhost:8080/analytics/sample/
```