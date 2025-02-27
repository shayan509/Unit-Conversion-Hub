def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        'meters': 1.0,
        'kilometers': 0.001,
        'centimeters': 100.0,
        'millimeters': 1000.0,
        'miles': 0.000621371,
        'yards': 1.09361,
        'feet': 3.28084,
        'inches': 39.3701,
        'nautical miles': 0.000539957,
        'light years': 1.057e-16,
        'parsecs': 3.24078e-17,         # 1 meter = ~3.24078e-17 parsecs
        'furlongs': 1 / 201.168,         # ~0.00497097 furlongs per meter
        'micrometers': 1e6,              # 1 meter = 1,000,000 micrometers
        'nanometers': 1e9,               # 1 meter = 1,000,000,000 nanometers
        'astronomical units': 6.68459e-12  # 1 meter = ~6.68459e-12 AU
    }
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Unsupported length unit.")
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        'kilograms': 1.0,
        'grams': 1000.0,
        'pounds': 2.20462,
        'ounces': 35.274,
        'newtons': 9.80665,
        'stones': 0.157473,
        'carats': 5000.0,
        'tons': 0.001,         # Metric tons (1 ton = 1000 kg)
        'milligrams': 1e6,      # 1 kg = 1,000,000 mg
        'quintals': 0.01        # 1 kg = 0.01 quintals (100 kg per quintal)
    }
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Unsupported weight unit.")
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    # Celsius, Fahrenheit, Kelvin, Rankine conversions
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9/5) + 32
    if from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    if from_unit == 'Celsius' and to_unit == 'Kelvin':
        return value + 273.15
    if from_unit == 'Kelvin' and to_unit == 'Celsius':
        return value - 273.15
    if from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        return (value - 32) * 5/9 + 273.15
    if from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        return (value - 273.15) * 9/5 + 32
    if from_unit == 'Celsius' and to_unit == 'Rankine':
        return (value + 273.15) * 9/5
    if from_unit == 'Rankine' and to_unit == 'Celsius':
        return (value - 491.67) * 5/9
    if from_unit == 'Fahrenheit' and to_unit == 'Rankine':
        return value + 459.67
    if from_unit == 'Rankine' and to_unit == 'Fahrenheit':
        return value - 459.67
    if from_unit == 'Kelvin' and to_unit == 'Rankine':
        return value * 9/5
    if from_unit == 'Rankine' and to_unit == 'Kelvin':
        return value * 5/9
    # Réaumur conversions
    if from_unit == 'Celsius' and to_unit == 'Réaumur':
        return value * 0.8
    if from_unit == 'Réaumur' and to_unit == 'Celsius':
        return value / 0.8
    if from_unit == 'Fahrenheit' and to_unit == 'Réaumur':
        return ((value - 32) * 5/9) * 0.8
    if from_unit == 'Réaumur' and to_unit == 'Fahrenheit':
        return (value / 0.8) * 9/5 + 32
    if from_unit == 'Kelvin' and to_unit == 'Réaumur':
        return (value - 273.15) * 0.8
    if from_unit == 'Réaumur' and to_unit == 'Kelvin':
        return (value / 0.8) + 273.15
    if from_unit == 'Rankine' and to_unit == 'Réaumur':
        return ((value - 491.67) * 5/9) * 0.8
    if from_unit == 'Réaumur' and to_unit == 'Rankine':
        return ((value / 0.8) * 9/5) + 491.67

    raise ValueError("Unsupported temperature conversion.")
