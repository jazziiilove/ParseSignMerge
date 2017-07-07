# ParseSignMerge
This python project parses an xml file, watermarks pdfs, merges pdfs and send in via rabbitmq broker

This is implemented in Windows 10. Be sure you have rabbit mq server installed on your machine.

Be sure you have the relevant python libraries installed.

C:\Users\Baran.Topal\AppData\Local\Programs\Python\Python36-32\Scripts>pip install lxml
Collecting lxml
  Downloading lxml-3.8.0-cp36-cp36m-win32.whl (2.9MB)
    100% |████████████████████████████████| 2.9MB 353kB/s
Installing collected packages: lxml
Successfully installed lxml-3.8.0

C:\Users\Baran.Topal\AppData\Local\Programs\Python\Python36-32\Scripts>pip search pdfrw
pdfrw (0.3)  - PDF file reader/writer library

C:\Users\Baran.Topal\AppData\Local\Programs\Python\Python36-32\Scripts>pip install pdfrw
Collecting pdfrw
  Downloading pdfrw-0.3-py2.py3-none-any.whl (58kB)
    100% |████████████████████████████████| 61kB 272kB/s
Installing collected packages: pdfrw
Successfully installed pdfrw-0.3

C:\Users\Baran.Topal\AppData\Local\Programs\Python\Python36-32\Scripts>pip install pika
Collecting pika
  Downloading pika-0.10.0-py2.py3-none-any.whl (92kB)
    100% |████████████████████████████████| 102kB 1.1MB/s
Installing collected packages: pika
Successfully installed pika-0.10.0
