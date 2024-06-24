#MEGABOSSES@42Porto

FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
ENV NAME Sistema_de_Triagem
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]
