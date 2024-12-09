def calculate_oil_cost(distance, fuel_efficiency, fuel_price):
    cost = (distance / fuel_efficiency) * fuel_price # ( ระยะทาง / อัตราสิ้นเปลือง ) * ราคาน้ำมัน = ค่าน้ำมันในการเดินทาง
    return cost

def calculate_travel_time(distance, speed):
    return distance / speed # ระยะทาง / ความเร็ว = เวลาที่ใช้ในการเดินทาง

if __name__ == "__main__":
    distance = float(input("กรุณากรอกระยะทางที่เดินทาง (Km.): "))
    speed = float(input("กรุณากรอกความเร็วเฉลี่ยในการเดินทาง (Km/h.): "))
    fuel_efficiency = float(input("กรุณากรอกอัตราการใช้น้ำมันของรถ (Km/l.): "))
    fuel_price = float(input("กรุณากรอกราคาน้ำมันต่อลิตร (THB.): "))
    
    oil_cost = calculate_oil_cost(distance, fuel_efficiency, fuel_price)
    travel_time = calculate_travel_time(distance, speed)
    
    print("---- รายละเอียดการคำนวณ ----")
    print(f"ระยะทางที่เดินทาง: {distance:.2f} Km.")
    print(f"ความเร็วเฉลี่ยในการเดินทาง: {speed:.2f} Km/h.")
    print(f"อัตราการใช้น้ำมัน: {fuel_efficiency:.2f} Km/l.")
    print(f"ราคาน้ำมัน: {fuel_price:.2f} THB/l.")
    print(f"ค่าน้ำมันในการเดินทางคือ: {oil_cost:.2f} THB.")
    print(f"เวลาที่ใช้ในการเดินทางคือ: {travel_time:.2f} h.")