FROM python:3.8
RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/
COPY . /usr/src/app/

RUN pip install -r  requirements.txt
EXPOSE 8080

CMD ["gunicorn", "-w", "4", "--bind", "0.0.0.0:8080", "wsgi"]

