# Network Automation - Cisco Router CLI Web Interface

เว็บแอปพลิเคชันสำหรับทำ Network Automation สั่งการ Router Cisco (R1) ผ่าน SSH (Paramiko) และรันระบบด้วย Docker Compose

## ส่วนประกอบของระบบ
- **Frontend**: Nginx + HTML/JS (มีช่องกรอก IP ของ Router, คำสั่ง และปุ่ม Execute)
- **Backend**: Python Flask + Paramiko (เชื่อมต่อ SSH ด้วยพอร์ต 22 ไปยัง Router R1)
- **Docker Compose**: ควบคุมการทำงานของ Frontend และ Backend พร้อมต่อเข้ากับเครือข่าย

## วิธีติดตั้งและเริ่มใช้งาน

```bash
# 1. เข้าโฟลเดอร์โปรเจกต์
cd ~/python

# 2. สั่งรันด้วย Docker Compose
docker compose up -d --build

# 3. ตรวจสอบสถานะ Containers
docker compose ps
```

เปิด Web Browser ไปที่ `http://localhost`

## การตั้งค่า Cisco Router (R1)
```text
ena
conf t
int fa0/0
 no shut
 ip add 172.19.0.100 255.255.0.0
hostname R1
ip domain-name test.com
username admin privilege 15
username admin password cisco
crypto key generate rsa modulus 1024
line vty 0 4
 login local
 transport input all
end
wr
```
