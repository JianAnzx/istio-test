FROM python

COPY . /work
WORKDIR /work

RUN pip install -r requirements.txt

CMD python ifconfig.py
