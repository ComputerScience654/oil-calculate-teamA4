def calculate_travel_cost(distance, fuel_efficiency, fuel_price):
    cost = (distance / fuel_efficiency) * fuel_price
    return cost

def calculate_distance_from_time(time, speed):
    # คำนวณระยะทางจากเวลา
    distance = time * speed  # ระยะทาง = เวลา * ความเร็ว
    return distance

if __name__ == "__main__":
    time = float(input("กรุณากรอกเวลาเดินทาง (ชั่วโมง): "))
    speed = float(input("กรุณากรอกความเร็ว (กิโลเมตร/ชั่วโมง): "))
    fuel_efficiency = float(input("กรุณากรอกอัตราการใช้น้ำมันของรถ (กิโลเมตรต่อลิตร): "))
    fuel_price = float(input("กรุณากรอกราคาน้ำมันต่อลิตร (บาท): "))
    
    # คำนวณระยะทางจากเวลา
    distance = calculate_distance_from_time(time, speed)
    
    # คำนวณค่าใช้จ่ายในการเดินทาง
    travel_cost = calculate_travel_cost(distance, fuel_efficiency, fuel_price)
    
    # แสดงผลลัพธ์
    print(f"ระยะทางที่เดินทางคือ: {distance:.2f} กิโลเมตร")
    print(f"ค่าใช้จ่ายในการเดินทางคือ: {travel_cost:.2f} บาท")
