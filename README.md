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
   ```sh
   pip install pyserial requests
