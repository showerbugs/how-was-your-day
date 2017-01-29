FROM python:3.5
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
RUN git clone -b feature/docker https://github.com/showerbugs/how-was-your-day.git /app
RUN pip install -r /app/requirements.txt

ENV FLASK_APP wsgi.py
ENV HOW_WAS_YOUR_DAY_ENV local 
WORKDIR /app
ENTRYPOINT ["sh", "/app/docker-run-dev.sh"]

EXPOSE 5000
EXPOSE 5432
