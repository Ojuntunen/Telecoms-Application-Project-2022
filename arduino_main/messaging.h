#ifndef MESSAGING_H
#define MESSAGING_H

#include <RadioHead.h>
#include <RH_ASK.h>
#include <RHReliableDatagram.h>
#include <arduino.h>
#include <SPI.h>
#include "accelerator.h"

class Messaging
{
public:
    Messaging();
    ~Messaging();
    void create_message(Measurement);
    bool send_message(uint8_t id, uint8_t flags);
    bool receive_ACK();
   
private:
    const uint8_t TRANSMITTER_ADDRESS = 70;
    const uint8_t RECEIVER_ADDRESS = 254;
    uint8_t buf[RH_ASK_MAX_MESSAGE_LEN];
    uint8_t data[RH_ASK_MAX_MESSAGE_LEN];
    uint8_t message_length = 6;
    RH_ASK driver;
    RHReliableDatagram *pmanager;
};

#endif
