from functogui import App, intUi
from typing import Annotated

def calculate_ws2812b_power(num_leds: Annotated[int, intUi(min_value=1, max_value=9999)] = 1,
                            brightness_percent: Annotated[int, intUi(min_value=0, max_value=100)] = 100
                            ) -> str:
    """
    Calculates the power required for a WS2812B LED strip.
    
    Parameters:
    - num_leds: Number of WS2812B LEDs
    - brightness_percent: Brightness percentage (0-100%)
    
    Returns:
    - Total power in Watts
    """
    
    WATTS_PER_LED = 0.2
    brightness_decimal = brightness_percent / 100
    total_power = WATTS_PER_LED * num_leds * brightness_decimal
    total_power = round(total_power, 2)
    amps = round(total_power / 5, 2)

    str_result = f"Total power: {total_power}W\n"
    str_result += f"Amps: {amps}A"
    return str_result


if __name__ == "__main__":
    App(calculate_ws2812b_power)