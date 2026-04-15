# SDN Mininet Delay Measurement

## 📌 Project Overview
This project demonstrates a Software Defined Networking (SDN) system using Mininet and the POX controller to measure and analyze network delay between hosts.

The controller monitors network traffic and processes packets using the OpenFlow protocol, enabling centralized control and visibility of the network.

---

## 🎯 Objectives
- To simulate a network using Mininet
- To implement an SDN controller using POX
- To measure network delay using ping (RTT)
- To analyze packet flow between hosts

---

## 🛠️ Tools & Technologies
- Mininet (Network Emulator)
- POX Controller
- OpenFlow Protocol
- Python

---

## 🧪 Project Setup

### 1. Start POX Controller
cd ~/pox
./pox.py openflow.of_01 delay_controller

### 2. Start Mininet Topology
sudo mn -c
sudo mn --topo tree,2 --controller=remote,ip=127.0.0.1,port=6633

---

## 📊 Testing & Results

### Ping Test (All Hosts)
pingall

✔ Ensures full network connectivity

---

### Delay Measurement
h1 ping h2
h1 ping h3

- RTT (Round Trip Time) is used to measure delay
- Output shows latency between hosts

---

## ⚙️ Controller Functionality
- Captures packets using OpenFlow events
- Extracts source and destination IP addresses
- Logs packet information
- Helps analyze network delay

---

## 📁 Project Structure
sdn-project/
│── delay_controller.py
│── README.md

---

## 📈 Key Features
- SDN-based network control
- Real-time packet monitoring
- Delay analysis using ping
- Simple and scalable topology

---

## 🧠 Concepts Used
- Software Defined Networking (SDN)
- OpenFlow Protocol
- Network Emulation
- Packet Switching
- Round Trip Time (RTT)

---

## 🏁 Conclusion
This project demonstrates how SDN can be used to monitor and analyze network performance efficiently. It highlights the advantages of centralized control and programmability in modern networking.

---

## 👩‍💻 Author
Prarthana Herur
