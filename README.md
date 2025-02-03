# RFID-Based Student Tracking System

## Overview
This project is an **RFID-based student tracking system** that **sends SMS notifications** to parents when their child enters/exits the school bus or school premises. It uses **Arduino, RFID technology, Python, and the Fast2SMS API** to provide real-time student tracking.

## Features
- **Real-time student monitoring** with RFID.
- **Automated SMS notifications** using the Fast2SMS API.
- **Time-based tracking** for different events (bus entry, school entry, departure).
- **Serial communication** between Arduino and a computer.

## Technologies Used
- **Arduino** (RFID reader, serial communication)
- **Python** (handling serial data and sending SMS)
- **Fast2SMS API** (sending SMS notifications)
- **Serial Communication** (via `pyserial`)

## How It Works
1. Each student carries an **RFID card**.
2. When a student **scans their card**, the Arduino reads the **RFID tag ID**.
3. The Python script processes the RFID data and **checks the current time**.
4. Based on predefined time slots, the script sends an **SMS notification** to parents.

## SMS Notification Logic
| Time (Hour) | RFID Card | SMS Triggered |
|-------------|----------|---------------|
| 9:00 - 10:00 AM | `84C64883` | "Your child entered the bus and departed to school." |
| 10:00 - 11:00 AM | `B6706AF3` | "Your child entered the school." |
| 4:00 - 5:00 PM | `B6706AF3` | "Your child left the school." |
| 5:00 - 6:00 PM | `84C64883` | "Your child entered the bus and departed to home." |

## Installation & Setup
1. **Install Python dependencies**:
   ```
   pip install pyserial requests
   ```
2. **Connect Arduino** to your PC and upload the RFID reader code.
3. **Update the Python script** with the correct **COM port** (e.g., `COM7`).
4. **Run the Python script**:
   ```
   python student_tracking.py
   ```
5. **Scan an RFID card** and check for SMS notifications.

## Potential Improvements
### 1. **Using IoT & Cloud for Real-Time Tracking**
   - Replace SMS with **push notifications** via **Firebase or MQTT**.
   - Store attendance logs in **Google Sheets** or **a cloud database**.

### 2. **GPS Integration for Live Bus Tracking**
   - Add **GPS modules** to track the school bus in real-time.
   - Send **live bus location** via a **mobile app or web dashboard**.

### 3. **AI & Machine Learning for Predictive Analysis**
   - Predict **bus arrival times** using AI models.
   - Analyze **student attendance trends**.

### 4. **Enhancing with NFC or QR Code**
   - Replace RFID with **NFC (Near Field Communication)** for better accuracy.
   - Use **QR codes** that students scan with a **mobile app**.

## Applications in Other Sectors
- **Corporate Security**: Employee check-in & access control.
- **Event Management**: Ticket validation & attendee tracking.
- **Healthcare**: Patient tracking in hospitals.
- **Logistics**: Warehouse inventory tracking.

## License
This project is open-source and available under the **MIT License**.

---
**Author:** Siddharamayya M  
📧 Email: [msidrm455@gmail.com](mailto:msidrm455@gmail.com)  
🌍 Portfolio: [https://mtptisid.github.io](https://mtptisid.github.io)
