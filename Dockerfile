FROM python

MAINTAINER Misha

COPY api_collections .
COPY configurations .
COPY page_objects .
COPY tests .
COPY utilities .
COPY work_with_db .
COPY work_with_mongo .
COPY .gitignore .
COPY conftest.py .
COPY main.py .
COPY pytest.ini .
COPY requirements.txt .

RUN pip install -r requirements.txt


