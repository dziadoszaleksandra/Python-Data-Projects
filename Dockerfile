FROM condaforge/miniforge3:latest

WORKDIR /app

RUN apt-get update && apt-get install -y make && rm -rf /var/lib/apt/lists/*

COPY conda-lock-dev.yml .

RUN mamba install -y -n base conda-lock && \
    conda-lock install --mamba -n python1course-env conda-lock-dev.yml && \
    mamba clean --all -f -y

RUN mamba shell init --shell bash --root-prefix=/opt/conda && \
    echo "mamba activate python1course-env" >> ~/.bashrc

ENV PATH="/opt/conda/envs/python1course-env/bin:$PATH"

CMD ["/bin/bash", "-l"]
