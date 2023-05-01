# growtogether
This is project at Solvit bootcamp.
# How to run celery worker

celery -A growtogether.celery worker --pool=solo -l info

# how to run celery beat 

celery -A growtogether.celery beat -l info