from mlx90614 import MLX90614

thermometer_address = 0x5A

thermometer = MLX90614(thermometer_address)


while (1):
    print thermometer.get_obj_temp() 


