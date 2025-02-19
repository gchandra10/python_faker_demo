from faker import Faker
from faker.providers import internet, misc
import random
from datetime import timedelta

fake = Faker()
fake.add_provider(internet)
fake.add_provider(misc)

def generate_device_identity():
    return {
        'device_id': fake.uuid4(),
        'mac_address': fake.mac_address(),
        'firmware_version': f"{fake.random_int(1,5)}.{fake.random_int(0,9)}.{fake.random_int(0,99)}",
        'manufacturer': fake.company(),
        'model': f"IOT-{fake.random_letters(length=4)}",
        'installation_date': fake.date_this_decade(),
        'last_maintenance': fake.date_time_this_month()
    }
    
def generate_smart_home_data():
    return {
        'room': fake.random_element(elements=('Living Room', 'Kitchen', 'Bedroom', 'Bathroom')),
        'power_consumption': round(random.uniform(0.1, 5.2), 2),
        'light_level': random.randint(0, 100),
        'motion_detected': fake.boolean(chance_of_getting_true=30),
        'door_status': fake.random_element(elements=('Open', 'Closed')),
        'air_quality': random.randint(0, 500)
    }
    
def generate_device_alert():
    return {
        'alert_id': fake.uuid4(),
        'severity': fake.random_element(elements=('Low', 'Medium', 'High', 'Critical')),
        'error_code': f"ERR-{fake.random_int(100, 999)}",
        'component': fake.random_element(elements=('Sensor', 'Network', 'Power', 'Memory', 'CPU')),
        'description': fake.sentence(),
        'timestamp': fake.date_time_this_month(),
        'resolved': fake.boolean(chance_of_getting_true=70)
    }
    
def generate_time_series_data(days=.05, interval_minutes=15):
    data_points = []
    base_time = fake.date_time_this_month()
    
    for i in range(int((days * 24 * 60) / interval_minutes)):
        timestamp = base_time + timedelta(minutes=i * interval_minutes)
        data_points.append({
            'timestamp': timestamp,
            'value': random.gauss(mu=50, sigma=10),  # Generate normally distributed data
            'status': 'active' if random.random() > 0.05 else 'inactive'
        })
    return data_points

print("Device Identity \n")
print(generate_device_identity())

# print("Smart Home \n")
# print(generate_smart_home_data())
# print("Device Alert \n")
# print(generate_device_alert())
# print("Time Series Data \n")
# print(generate_time_series_data())

## Generate multiple records
# sensor_data = [generate_device_identity() for _ in range(10)] 
# print(sensor_data)