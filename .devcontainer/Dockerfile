FROM continuumio/miniconda3:4.12.0

SHELL ["/bin/bash", "-c"]

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update
RUN apt update
RUN apt install -y openbabel make
RUN pip install flake8 autopep8
RUN pip install numpy scipy
RUN pip install networkx

# post processing
RUN echo "alias ls='ls --color=auto'" >> /etc/bash.bashrc

# insert commands to .bashrc to use host's ssh settings in container
RUN echo "mkdir -p /root/.ssh" >> /root/.bashrc
RUN echo "ls /root/.ssh_host 2> /dev/null 1> /dev/null && cp /root/.ssh_host/* /root/.ssh/" >> /root/.bashrc
RUN echo "ls /root/.ssh      2> /dev/null 1> /dev/null && chmod 600 /root/.ssh/config"      >> /root/.bashrc