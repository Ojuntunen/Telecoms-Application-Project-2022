# Telecoms Application Project - Autumn 2022



#### **ENG**

 This repository is a part of Oulu University of Applied Sciences' _Telecoms application project_ course. The purpose of the project is to apply previously learned fundamentals of telecommunications, IoT and machine learning, and to further develop the student's skills in these areas.

### **The Project**
For a brief overview, see the [poster.](./etc/olli_juntunen_telecoms_application_project_poster.pdf)
> There is an IoT-router (Raspberry Pi) in the telecoms lab, which is connected to the OAMK campus network. The student's task is to code an Arduino client that measures accelerometer data, and transfers it wirelessly to the IoT router according to provided specifications. The IoT router is provided fully operational, and stores received data in a MySQL database.
>
> The data stored in the database is accessible through TCP socket interface and HTTP API. Collected data is fetched to a laptop using a program made by the student, and used to train a machine learning model.

<br/>

![](./etc/data-architecture-diagram.png)
_Figure 1: data architecture_