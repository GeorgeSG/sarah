FROM koenkk/zigbee2mqtt:latest

RUN apk add --no-cache \
       git python3 make gcc g++ python linux-headers udev
RUN rm -rf /app/node_modules/zigbee-herdsman/
RUN git clone https://github.com/Koenkk/zigbee-herdsman.git /app/node_modules/zigbee-herdsman/
RUN cd /app/node_modules/zigbee-herdsman/ && git checkout deconz
RUN cd /app/node_modules/zigbee-herdsman/ && npm install
RUN cd /app/node_modules/zigbee-herdsman/ && npm run build
