# Copyright 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

FROM debian:12
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive \
    apt-get install -yq --no-install-recommends \
    vim \
    nano \
    tree \
    htop \
    wget \
    curl \
    unzip \
    ca-certificates \
    openssl \
    python3 \
    python3-dev \
    libyaml-dev \
    build-essential \
    pkg-config \
    libusb-1.0-0-dev \
    cmake \
    gcc-arm-none-eabi \
    libnewlib-arm-none-eabi

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN python3 -m pip install --upgrade setuptools
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade build
RUN rm -f get-pip.py
COPY requirements.txt /
RUN pip3 install -r requirements.txt
RUN rm -f requirements.txt
RUN mkdir /gen_py_tool/
COPY gen_py_tool /gen_py_tool/
COPY setup.py /
COPY README.md /
COPY LICENSE /
COPY setup.cfg /
COPY MANIFEST.in /
COPY pyproject.toml /
RUN mkdir /tests/
COPY tests /tests/
RUN python3 -m build --no-isolation --wheel
RUN pip3 install ./dist/gen_py_tool-*-py3-none-any.whl
RUN rm -rf /gen_py_tool*
RUN rm -f setup.py
RUN rm -f README.md
RUN rm -f LICENSE
RUN rm -f setup.cfg
RUN rm -f MANIFEST.in
RUN rm -f pyproject.toml
RUN rm -rf /build/
RUN rm -rf /dist/
RUN rm -rf /tests/
