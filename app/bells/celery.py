import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bells.settings')

app = Celery(
    'bells',
    # broker='amqp://docker.host.internal:5672',
    # backend='rpc://',
    include=['bells.tasks']
)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


if __name__ == '__main__':
    app.start()
