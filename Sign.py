"""
 " " " " " " " " " " " " " " " " " " " " " " "
 " Assignment: ParseSignMerge                "
 " Programmer: Baran Topal                   "
 " File name: Sign.py                        "
 "                                           "
 " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " "
 "	                                                                                         "
 "  LICENSE: This source file is subject to have the protection of GNU General               "
 "	Public License. You can distribute the code freely but storing this license information. "
 "	Contact Baran Topal if you have any questions. barantopal@barantopal.com                 "
 "	                                                                                         "
 " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " "
"""

from pdfrw import PdfReader, PdfWriter, PageMerge
import pika
import json
import base64

encodedPdf = None


class Sign:
    def __init__(self, id, cv):
        self.id = id
        self.cv = cv

    def hello(self):
        print("init Sign")

    def displayCount(self):
        print("Total Employee %d" % Sign.empCount)

    def watermark(self):
        ipdf = PdfReader('1.pdf')
        wpdf = PdfReader('watermark.pdf')
        wmark = PageMerge().add(wpdf.pages[0])[0]

        for page in ipdf.pages:
            PageMerge(page).add(wmark).render()

        PdfWriter().write('merged.pdf', ipdf)

    def send(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='hello')

        global encodedPdf

        with open("merged.pdf", "rb") as f:
            encodedPdf = base64.b64encode(f.read())

        channel.basic_publish(exchange='',
                              routing_key='hello',
                              # body='Hello World!')
                              body=json.dumps(encodedPdf.decode("utf-8")))

        print(" [x] Sent the pdf file!'")

        connection.close()
