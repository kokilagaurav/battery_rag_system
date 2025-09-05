import csv
import random

# Define the number of rows
num_rows = 10000

# Define the headers for the CSV file
headers = [
    'Cell_ID', 'Cell_Type', 'Nominal_Voltage_V', 'Capacity_Ah', 
    'Internal_Resistance_mOhm', 'Gravimetric_Energy_Density_Wh/kg', 
    'Volumetric_Energy_Density_Wh/L', 'Thermal_Runaway_Temp_C', 'Cathode_Material', 
    'Anode_Material', 'Separator_Material'
]

# Generate the data
data = []
for i in range(1, num_rows + 1):
    cell_id = f'BAT-{i:05d}'
    cell_type = random.choice(['Cylindrical', 'Pouch', 'Prismatic'])
    
    if cell_type == 'Cylindrical':
        nominal_voltage = round(random.uniform(3.6, 3.8), 2)
        capacity = round(random.uniform(2.5, 3.5), 2)
        internal_resistance = round(random.uniform(20, 30), 1)
        gravimetric_density = round(random.uniform(230, 250), 2)
        volumetric_density = round(random.uniform(600, 700), 2)
        thermal_temp = random.randint(140, 160)
        cathode = random.choice(['LiCoO2', 'NCA'])
        anode = 'Graphite'
        separator = 'PE'

    elif cell_type == 'Pouch':
        nominal_voltage = round(random.uniform(3.7, 3.9), 2)
        capacity = round(random.uniform(4.0, 6.0), 2)
        internal_resistance = round(random.uniform(15, 25), 1)
        gravimetric_density = round(random.uniform(270, 290), 2)
        volumetric_density = round(random.uniform(700, 800), 2)
        thermal_temp = random.randint(160, 180)
        cathode = random.choice(['NMC', 'LMO'])
        anode = 'Silicon-Graphite'
        separator = 'PP'
    
    else: # Prismatic
        nominal_voltage = round(random.uniform(3.2, 3.3), 2)
        capacity = round(random.uniform(20.0, 30.0), 2)
        internal_resistance = round(random.uniform(4, 10), 1)
        gravimetric_density = round(random.uniform(110, 130), 2)
        volumetric_density = round(random.uniform(280, 320), 2)
        thermal_temp = random.randint(200, 230)
        cathode = 'LiFePO4'
        anode = 'Graphite'
        separator = 'Ceramic-coated'

    row = [
        cell_id, cell_type, nominal_voltage, capacity, internal_resistance, 
        gravimetric_density, volumetric_density, thermal_temp, cathode, 
        anode, separator
    ]
    data.append(row)

# Write the data to a CSV file
file_name = 'battery_data_10000_rows.csv'
with open(file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data)

print(f"Successfully created '{file_name}' with {num_rows} rows of data.")