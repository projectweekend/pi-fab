FROM python:2.7
RUN pip install fabric
WORKDIR /src
CMD ["fab"]
