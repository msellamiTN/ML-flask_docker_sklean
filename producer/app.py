from confluent_kafka import Producer
import socket
import json
conf = {'bootstrap.servers': "PLAINTEXT://198.244.143.92:29092,PLAINTEXT://localhost:9092",
        'client.id': socket.gethostname()}

covid_data={
    1: {"Country":"France","Confirmed":650000,"Deaths":152540,"Recovred":546000},
    2: {"Country":"Tunisia","Confirmed":105000,"Deaths":5200,"Recovred":77005},
    3: {"Country":"Maroc","Confirmed":250000,"Deaths":15000,"Recovred":150000},
    4: {"Country":"Algerie","Confirmed":210000,"Deaths":14520,"Recovred":158000},
    5: {"Country":"Mali","Confirmed":130000,"Deaths":4500,"Recovred":99000},
    6: {"Country":"Italy","Confirmed":250000,"Deaths":65000,"Recovred":150000},
    11: {"Country":"France","Confirmed":650000,"Deaths":152540,"Recovred":546000},
    12: {"Country":"Tunisia","Confirmed":105000,"Deaths":5200,"Recovred":77005},
    13: {"Country":"Maroc","Confirmed":250000,"Deaths":15000,"Recovred":150000},
    14: {"Country":"Algerie","Confirmed":210000,"Deaths":14520,"Recovred":158000},
    15: {"Country":"Mali","Confirmed":130000,"Deaths":4500,"Recovred":99000},
    16: {"Country":"Italy","Confirmed":250000,"Deaths":65000,"Recovred":150000},
21: {"Country":"France","Confirmed":650000,"Deaths":152540,"Recovred":546000},
    22: {"Country":"Tunisia","Confirmed":105000,"Deaths":5200,"Recovred":77005},
    23: {"Country":"Maroc","Confirmed":250000,"Deaths":15000,"Recovred":150000},
    24: {"Country":"Algerie","Confirmed":210000,"Deaths":14520,"Recovred":158000},
    25: {"Country":"Mali","Confirmed":130000,"Deaths":4500,"Recovred":99000},
    26: {"Country":"Italy","Confirmed":250000,"Deaths":65000,"Recovred":150000},
31: {"Country":"France","Confirmed":650000,"Deaths":152540,"Recovred":546000},
    32: {"Country":"Tunisia","Confirmed":105000,"Deaths":5200,"Recovred":77005},
    33: {"Country":"Maroc","Confirmed":250000,"Deaths":15000,"Recovred":150000},
    34: {"Country":"Algerie","Confirmed":210000,"Deaths":14520,"Recovred":158000},
    35: {"Country":"Mali","Confirmed":130000,"Deaths":4500,"Recovred":99000},
    36: {"Country":"Italy","Confirmed":250000,"Deaths":65000,"Recovred":150000}}
#Initialiser producer avec la configuration 
p = Producer(conf)
# initialiser le nom du topic
topic_name='abdata'

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))
 
# Parcourir comme key-value et generer un ecrire les données (keyn value) avec p.produce
for key, value in covid_data.items():
    # Lancer un rappel de rapport de livraison disponible à partir d'appels de production () précédents
    p.poll(0)
    # Produire de manière synchrone un message, les callbacks
    # seront déclenchés à partir de poll() au-dessus, ou de flush() au-dessous, lorsque le message a
    # ont été livrés avec succès ou ont échoué définitivement.
    data = json.dumps(value, ensure_ascii=False).encode('utf-8')
    
    p.produce(topic_name,value=data, key=str(key), callback=delivery_report)
     
    
# Attendre la remise des messages en attente et du rapport de remise
# les callbacks à déclencher.
p.flush()