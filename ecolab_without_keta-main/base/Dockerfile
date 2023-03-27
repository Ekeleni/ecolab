FROM python:3.11

WORKDIR /base
COPY requirements.txt /base
RUN pip3 install --upgrade pip -r requirements.txt
COPY . /base
EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["flask", "run", "--host", "0.0.0.0", "5000"]