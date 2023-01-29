FROM python:3.11.0
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY main.py /app
COPY Models/. /app/Models
COPY database.py /app
COPY create_database.py /app
COPY security.py /app
COPY sendgridEmail.py /app
COPY instance /app/instance
EXPOSE 5000
CMD ["flask","run","--host=0.0.0.0"]