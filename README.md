# TietoliikenteenSovellusprojektiSyksy2022

FI

Tämä repositorio on osa Oulun Ammattikorkeakoulun Tietoliikenteen sovellusprojekti -kurssia. Projektissa sovelletaan aiemmin opittuja tietoliikenteen, IoT:n ja  koneoppimisen perusteita.

Projekti

Tietoliikennelabrassa on IoT-reititin (Raspberry Pi), joka on Oamkin kampusverkossa. Opiskelijoiden tehtävänä on koodata Arduinolle client, joka mittaa kiihtyvyysanturin dataa ja välittää tietoa langattomasti IoT-reitittimelle valmiiksi annetun speksin mukaisesti. IoT-reititin on asennettu valmiiksi ja varastoi vastaanotettua dataa MySQL-tietokantaan.

Tietokantaan tallentuvaan dataan on TCP-sokettirajapinta ja HTTP API. Kerättyä dataa haetaan rajanpinnasta omaan kannettavaan koodatulla ohjelmalla ja käsitellään koneoppimistarkoitukseen.


EN

This repository is a part of Oulu University of Applied Sciences 'Telecoms application project' course. The purpose of the project is to apply previously learned telecoms, IoT and machine learning fundamentals.

The Project

There is an IoT-router (Respberry Pi) in the telecoms lab, which is connected to the OAMK campus network. The student's task is to code an Arduino client that measures accelerometer data, and transfers it wirelessly to the IoT router according to pre-specified specs. The IoT router is provided fully installed and stores the received data in a MySQL database.

The data stored in the database is accessed through TCP socket interface and HTTP API. Collected data is fetched from the laptop via a program coded by the student, and processed for the purposes of machine learning.
