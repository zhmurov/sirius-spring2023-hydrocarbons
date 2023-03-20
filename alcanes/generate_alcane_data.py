import math

chain_length = 3
gro_file_name = f"alcane_{chain_length}.gro"

n_atoms = (chain_length - 2) * 3 + 8

molecule_number = 1
molecule_name = f"AL{chain_length:<3d}"

CC_length = 0.1375
CH_length = 0.108

with open(gro_file_name, 'w') as output_file:
    output_file.write(f"Alcane {chain_length}\n")
    output_file.write(f"{n_atoms:5d}\n")

    total_index = 1

    for index in range(chain_length):
        x = index * CC_length
        output_file.write(f"{molecule_number:5d}{molecule_name:5s}C{index+1:<4d}{total_index:5d}{x:8.3f}{0.0:8.3f}{(-0.01)**(index + 1):8.3f}{0.0:8.4f}{0.0:8.4f}{0.0:8.4f}\n")
        total_index += 1
        output_file.write(f"{molecule_number:5d}{molecule_name:5s}H{str(index+1) + '1':<4s}{total_index:5d}{x:8.3f}{CH_length:8.3f}{0.0:8.3f}{0.0:8.4f}{0.0:8.4f}{0.0:8.4f}\n")
        total_index += 1
        output_file.write(f"{molecule_number:5d}{molecule_name:5s}H{str(index+1) + '2':<4s}{total_index:5d}{x:8.3f}{-CH_length:8.3f}{0.0:8.3f}{0.0:8.4f}{0.0:8.4f}{0.0:8.4f}\n")
        total_index += 1

        if index in [0,chain_length-1]:
            output_file.write(f"{molecule_number:5d}{molecule_name:5s}H{str(index+1) + '3':<4s}{total_index:5d}{x + CH_length*(1 - 2*(index == 0)):8.3f}{0.0:8.3f}{0.01:8.3f}{0.0:8.4f}{0.0:8.4f}{0.0:8.4f}\n")
            total_index += 1