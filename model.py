import csv
import random
import os

class Cow:
    def __init__(self, cow_id, breed, age_years, age_months, is_bsod, milk_model):
        self.cow_id = cow_id
        self.breed = breed  # 'white' or 'brown'
        self.age_years = age_years
        self.age_months = age_months
        self.is_bsod = is_bsod
        self.eat_lemon = False
        self.milk_model = milk_model 

    def milk(self):
        if self.is_bsod:  #ถ้า  bsod error
            return "BSOD", 0
        
        self.reset_bsod() #ส่มการเกิด bsod 
        if self.breed == 'White': 
            if self.is_bsod: 
                self.milk_model.record_milk(self.cow_id, "Soy Milk",  0)
                return "Soy Milk", 1
            elif self.eat_lemon:
                self.eat_lemon = False 
                self.milk_model.record_milk(self.cow_id, "Probiotic Milk", 1)
                return "Probiotic Milk", 1
            else:
                self.milk_model.record_milk(self.cow_id, "Fresh Milk",  1)
                return "Fresh Milk", 1

        else:  # brown cow
            if self.is_bsod:
                self.milk_model.record_milk(self.cow_id, "Almond Milk", 0)
                return "Almond Milk", 1
            else:
                self.milk_model.record_milk(self.cow_id, "Chocolate",  1)
                return "Chocolate Milk", 1
    def random_bsod(self):
        if self.breed == 'white':
            change = 0.005*self.age_months
        else:
            change = 0.01*self.age_years
        self.is_bsod = random.choices([True,False], weights=[change,1-change], k=1)[0]

    def reset_bsod(self):
        self.is_bsod = False

class CowModel:
    def __init__(self, milk_model):
        self.cows = {}
        self.milk_model = milk_model
        self.csv_file = 'cow_data.csv'
        self.initialize_csv()
        self.load_data()
        print(len(self.cows))
    
    def initialize_csv(self): #ถ้าไม่ไฟล์สร้างไฟล์
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["cow_id", "breed", "age_years", "age_months", "bsod"])
                self.create_examples()

    def create_examples(self): #สร้างต้วอย่างวัว
        for i in range(12):
            breed = random.choice(["white", "brown"])
            random_id = str(random.randint(10000000, 99999999))
            random_year = random.randint(0, 11)
            random_month = random.randint(0, 12) if random_year < 10 else 0
            self.add_cow(random_id, breed, random_year, random_month, False)

    def add_cow(self, cow_id, breed, age_years, age_months, is_bsod): #เพิ่มวัวใน csv
        with open(self.csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([cow_id, breed, age_years, age_months, is_bsod])
            
    def load_data(self):
        with open(self.csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    cow_id = row['cow_id']
                    breed = row['breed']
                    age_years = int(row['age_years'])
                    age_months = int(row['age_months'])
                    is_bsod = row['bsod'] == 'True'
                    cow = Cow(cow_id=cow_id, breed=breed, age_years=age_years, age_months=age_months, is_bsod=is_bsod, milk_model=self.milk_model)
                    self.cows[cow_id] = cow
                except ValueError as e:
                    print(f"Skipping row with invalid data: {row}")
                    print(f"Error: {e}")

    def get_cow_by_id(self, cow_id): # ส่งข้อมูลวัวด้วยไอดี
        return self.cows.get(cow_id)
    
    def get_milk_info(self, cow_id): #ส่งข้อมูลนมทั้งหมด
        return self.milk_model.check_amount_quality_all_milks(),self.milk_model.check_amount_quality_milks_per_cow(cow_id)
    def reset_all_bsod(self):
        for cow in self.cows.values():
            cow.reset_bsod()

class MilkModel:
    def __init__(self, filename='milk_records.csv'):
        self.filename = filename
        self.initialize_csv()

    def initialize_csv(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["cow_id", "milk_type", "quality"])

    def record_milk(self, cow_id, milk_type, quality):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([cow_id, milk_type, quality])
    
    def check_amount_quality_all_milks(self, quality_value=1):#นับนมที่ใช้ได้
        count = 0
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                if row[2] == str(quality_value):
                    count += 1
        return count
    
    def check_amount_quality_milks_per_cow(self, cow_id, quality_value=1): #นับนมที่ใช้ได้ของวัวที่เลือก
        count = 0
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[0] == cow_id and row[2] == str(quality_value):
                    count += 1
        return count
    
    
