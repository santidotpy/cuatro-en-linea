FROM python:3

RUN git clone https://github.com/santidotpy/cuatro-en-linea.git

WORKDIR /cuatro-en-linea

RUN pip install -r requirements.txt

CMD ["python3", "test_4linea.py"]