FROM python:3.10.7
# system related settings should be declared under root user
USER root
RUN apt-get update && apt-get install wget
RUN pip3 install jupyter
ENV JUPYTER_USER Yue
RUN useradd -ms /bin/bash ${JUPYTER_USER}
COPY requirements.txt .
RUN pip3 install -r requirements.txt
# RUN pip3 install pandas

EXPOSE 8888

USER ${JUPYTER_USER}
WORKDIR /home/notebooks/
# RUN pip3 freeze > requirements.txt

# remember to use the raw format
RUN wget -c https://raw.githubusercontent.com/AlohaPlenilune/MSIS2628/main/week1/Untitled.ipynb -O test.ipynb
# need to declare the local host ip rather than just use localhost
CMD jupyter notebook --ip=0.0.0.0 --port 8888

