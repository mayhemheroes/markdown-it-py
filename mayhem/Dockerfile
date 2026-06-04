# Build Stage
FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    clang \
    libfuzzer-19-dev \
    && rm -rf /var/lib/apt/lists/*

ENV CC=clang
ENV CXX=clang++

RUN pip install --upgrade pip && \
    pip install atheris

ADD . /src
WORKDIR /src
RUN pip install .

CMD ["/src/mayhem/fuzz_convert.py"]
