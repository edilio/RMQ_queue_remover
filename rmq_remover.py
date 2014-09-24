import base64
import json


user = 'username'
password = 'password'
host = 'rabbitmq-host'
base64string = base64.encodestring('%s:%s' % (user, password)).replace('\n', '')
authorization = "Basic {0}".format(base64string)
headers = {'Authorization': authorization}


def delete_queue(queue_name):
    url = 'http://{0}:55672/api/queues/%2F/{1}'.format(host, queue_name)
    payload = {'mode': "delete", 'name': queue_name, 'vhost': "/"}
    requests.delete(url, data=json.dumps(payload), headers=headers)
