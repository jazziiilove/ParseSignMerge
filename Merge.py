"""
 " " " " " " " " " " " " " " " " " " " " " " "
 " Assignment: ParseSignMerge                "
 " Programmer: Baran Topal                   "
 " File name: Merge.py                       "
 "                                           "
 " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " "
 "	                                                                                         "
 "  LICENSE: This source file is subject to have the protection of GNU General               "
 "	Public License. You can distribute the code freely but storing this license information. "
 "	Contact Baran Topal if you have any questions. barantopal@barantopal.com                 "
 "	                                                                                         "
 " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " "
"""


import json
import os
import pika
from pdfrw import PdfReader, PdfWriter


class Merge:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % json.loads(body.decode()))

    channel.basic_consume(callback,
                          queue='hello',
                          no_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

    def __init__(self):
        print("init Merge")

    def merge(self):
        writer = PdfWriter()

        files = [x for x in os.listdir('.') if x.endswith('.pdf')]
        for fname in sorted(files):
            writer.addpages(PdfReader(os.path.join('.', fname)).pages)

        writer.write("output.pdf")




