# traadfri (formerly ikea-smartlight)
IKEA Trådfri (smart lighting) command line interface.

To run traadfri successfully, the Trådfri gateway's IP must be stored in `TRAADFRI_HUB`, along with your API username in `TRAADFRI_USER`.
Furthermore, an API key needs to be present in `TRAADFRI_KEY`.

To obtain an API key, run the following in your shell:

```bash
coap-client -m post -u Client_identity -k [Code on the bottom of the gateway] -e '{"9090": "$TRAADFRI_USER"}' coaps://$TRAADFRI_HUB:5684/15011/9063
```

## Installation

### Nix
Use the provided `default.nix` file.

### Non-Nix

#### libcoap
To use the `coap-client` CLI, you need a version of libcoap with dtls built in, e.g. 4.2.0.

```bash
sudo apt-get install automake libtool
git clone --depth 1 --recursive -b v4.2.0 https://github.com/home-assistant/libcoap.git
cd libcoap
./autogen.sh
./configure --disable-documentation --disable-shared --without-debug CFLAGS="-D COAP_DEBUG_FD=stderr"
make
sudo make install
```

#### traadfri
When you have successfully installed libcoap (`coap-client` should be in your `PATH`), run `python3 setup.py install` to install traadfri.

## Miscellanea

### Apple HomeKit
To obtain the Apple HomeKit code for your Trådfri gateway, run:

```bash
coap-client -m get -u $TRAADFRI_USER -k $TRAADFRI_KEY coaps://$TRAADFRI_HUB:5684/15011/15012
```
