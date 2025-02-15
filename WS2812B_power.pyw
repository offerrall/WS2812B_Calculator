from functogui import App, intUi
from typing import Annotated

def calculate_ws2812b_power(num_leds: Annotated[int, intUi(min_value=1, max_value=9999)] = 1,
                            brightness_percent: Annotated[int, intUi(min_value=0, max_value=100)] = 100
                            ) -> str:
    
    AMPS_PER_LED = 0.06
    VOLTAGE = 5
    
    brightness_decimal = brightness_percent / 100
    total_amps = AMPS_PER_LED * num_leds * brightness_decimal
    total_amps = round(total_amps, 2)
    total_power = round(total_amps * VOLTAGE, 2)

    str_result = f"Total power: {total_power}W\n"
    str_result += f"Amps: {total_amps}A"
    return str_result

if __name__ == "__main__":
    App(calculate_ws2812b_power)