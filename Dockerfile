FROM python:3.9-slim

WORKDIR /splc23-analysis-operations

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]