FROM python:3.9-slim-bullseye

RUN useradd -u 8877 --create-home userunner
ENV PATH="/home/userunner/.local/bin:$PATH" 
USER userunner

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install --no-cache-dir  -r requirements.txt 

COPY --chown=userunner . /app/

ENTRYPOINT ["./scripts/docker-entrypoint.sh"]