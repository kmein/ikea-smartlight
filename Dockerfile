FROM debian:stable AS builder

RUN DEBIAN_FRONTEND=noninteractive; apt-get update \
&&  apt-get install -y build-essential \
                       automake \
                       libtool \
                       autoconf \
                       git \
&&  git clone --depth 1 https://github.com/kmein/traadfri.git \
&&  git clone --depth 1 --recursive -b dtls https://github.com/home-assistant/libcoap.git \
&&  cd /libcoap \
&&  ./autogen.sh \
&&  ./configure --disable-documentation --disable-shared --without-debug CFLAGS="-D COAP_DEBUG_FD=stderr" \
&&  make

FROM python:3.7-stretch

COPY --from=builder /libcoap /libcoap 
COPY --from=builder /traadfri /traadfri

RUN cd traadfri \
&&  python3 setup.py install \
&&  cd /libcoap \
&&  make install

ENTRYPOINT ["traadfri"]
