# Dockerfile for binder
# Reference: https://mybinder.readthedocs.io/en/latest/tutorials/dockerfile.html

FROM ghcr.io/sagemath/sage-binder-env:10.3

USER root

# Create user alice with uid 1000
ARG NB_USER=alice
ARG NB_UID=1000
ENV NB_USER alice
ENV NB_UID 1000
ENV HOME /home/${NB_USER}
RUN adduser --disabled-password --gecos "Default user" --uid ${NB_UID} ${NB_USER}

# Install git for installing the QuiverTools package
RUN apt update
RUN apt install -y git

# Make sure the contents of the notebooks directory are in ${HOME}
COPY notebooks/* ${HOME}/
RUN chown -R ${NB_USER}:${NB_USER} ${HOME}

# Switch to the user
USER ${NB_USER}

# Install Sage kernel to Jupyter
RUN mkdir -p $(jupyter --data-dir)/kernels
RUN ln -s /sage/venv/share/jupyter/kernels/sagemath $(jupyter --data-dir)/kernels

# Install QuiverTools
RUN /sage/sage --pip install git+https://github.com/QuiverTools/QuiverTools.git --user

# Start in the home directory of the user
WORKDIR /home/${NB_USER}
