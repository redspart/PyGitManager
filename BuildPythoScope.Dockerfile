FROM python:2.7

RUN pip install pythoscope

COPY src/ /Build/src/
RUN pythoscope --init /Build/src/pygitmanager/
RUN pythoscope -v /Build/src/pygitmanager/*.py -t unittest
RUN tar -cvf unittest.tar -C /Build/src/pygitmanager/tests/ .
