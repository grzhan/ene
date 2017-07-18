from wxpy import *
import yaml
with open('.env', 'r') as fd:
    config = yaml.load(fd)
ene = Bot(cache_path=config['SESSION_PATH'], console_qr=True)
master = ene.friends().search(config['MASTER_NAME'])[0]


@ene.register(master)
def pong(msg):
    if msg.text == 'ping':
        master.send('pong')

ene.join()
