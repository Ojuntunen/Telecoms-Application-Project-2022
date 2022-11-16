#include "messaging.h"

Messaging::Messaging()
{
  pmanager = new RHReliableDatagram(driver, TRANSMITTER_ADDRESS);
  if(!pmanager->init())
  {
    Serial.println("Radiohead manager init failed");
  }
}
Messaging::~Messaging()
{
  delete pmanager;
}
void Messaging::create_message(Measurement m)
{
  data[0] = m.x >> 8;
  data[1] = m.x;
  data[2] = m.y >> 8;
  data[3] = m.y;
  data[4] = m.z >> 8;
  data[5] = m.z;
}
bool Messaging::send_message(uint8_t id, uint8_t flags)
{
  unsigned long start = millis();
  unsigned long timeout = millis()-start;
  while(timeout<500)
  {
    timeout = millis()-start;
  }
  driver.setModeTx();
  uint8_t to = RECEIVER_ADDRESS;
  uint8_t from = TRANSMITTER_ADDRESS;

  pmanager->setHeaderTo(to);
  pmanager->setHeaderFrom(from);
  pmanager->setHeaderId(id);
  pmanager->setHeaderFlags(flags);

  bool return_value = false;

  if(pmanager->sendto(data, message_length, RECEIVER_ADDRESS))
  {
    return_value = true;
  }
  pmanager->waitPacketSent();
  Serial.println("Message sent");
  return return_value;
  
}
bool Messaging::receive_ACK()
{
  driver.setModeRx();
  unsigned long start = millis();
  unsigned long timeout = millis()-start;
  bool receiver_result = false;
  uint8_t to;
  uint8_t from;
  uint8_t len;
  uint8_t id;
  uint8_t flags;
  while((timeout<1500) && (!pmanager->available()))
  {
    timeout = millis()-start;
  }
  receiver_result = pmanager->recvfrom(buf,&len,&from,&to,&id,&flags);
  if(receiver_result)
  {
    //Serial.println("ACK received");
    Serial.println((char *)buf);
    Serial.print("Sent from address: ");
    Serial.print(from);
    Serial.print("ID: ");
    Serial.println(id);
    Serial.print("flags: ");
    Serial.println(flags);
    return true;
  }
  else
  {
    //Serial.println("ACK not received, retransmit");
    return false;
  }
}
