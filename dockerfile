FROM python:3.13.2-slim

# Install Java (OpenJDK 17)
RUN apt-get update && \
    apt-get upgrade -y &&\
    apt-get install -y openjdk-17-jdk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="$JAVA_HOME/bin:$PATH"

RUN echo "✅ Java installed"

RUN apt-get update
RUN apt-get upgrade -y 
RUN apt-get install -y npm
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*


RUN npm install -g @rmlio/yarrrml-parser

RUN echo "✅ YARRML-parser installed"

RUN pip install --upgrade pip

COPY . ONNX2RDF
# git clone https://github.com/JorgeMIng/ONNX2RDF.git

WORKDIR /ONNX2RDF

RUN pip install .

RUN rm -rf /root/.cache

CMD ["/bin/bash"]