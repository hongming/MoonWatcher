import csv

def convert_coordinates(coord):
    """Convert coordinates from '48.5°N' format to decimal degrees."""
    try:
        value = float(coord[:-2])
        direction = coord[-1]
        if direction in 'SW':
            value = -value
        return value
    except ValueError:
        return None

def convert_csv_to_target_format(csv_file, output_file):
    targets = []
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                lat = convert_coordinates(row['lat'])
                lon = convert_coordinates(row['lon'])
                if lat is None or lon is None:
                    raise ValueError("Invalid coordinate format")
                target = {
                    'type': row['type'],
                    'name': row['name'],
                    'lat': lat,
                    'lon': lon,
                    'fontSize': int(row['fontSize']),
                    'rotate': int(row['rotate']),
                    'x_Offset': int(row['x_offset']),
                    'y_offset': int(row['y_offset'])
                }
                targets.append(target)
            except Exception as e:
                print(f"Error processing row {row}: {e}")

    with open(output_file, mode='w', encoding='utf-8') as file:
        for target in targets:
            file.write(f"{target},\n")

# 使用文件路径调用函数
convert_csv_to_target_format('markers-human.csv', 'markers-human-targets_for_html.txt')
