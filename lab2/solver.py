import pyswip
from pyswip import Prolog


class Solver:
    def __init__(self):
        self.prolog = Prolog()
        self.prolog.consult('gwent.pl')

    def solve(self, data: tuple):
        match data[0]:
            case 1:
                return self.is_card_weather_resistant(data[1])
            case 2:
                return self.get_card_description(data[1])
            case 3:
                return self.is_combat_affected(data[1], data[2])
            case 4:
                return self.is_card_affected(data[1], data[2])
            case 5:
                return self.get_card_strength(data[1], data[2])



    def is_card_weather_resistant(self, card_name):
        result = list(self.prolog.query(f"char_resistance('{card_name}')"))
        return 'Yes' if result != [] else 'No'

    def get_card_description(self, card_name):
        strength_result = list(self.prolog.query(f"char_power('{card_name}', Strength)"))
        type_result = list(self.prolog.query(f"char_types('{card_name}', Type)"))
        resistance_result = list(self.prolog.query(f"char_resistance('{card_name}')"))

        card_type = type_result[0]['Type'] if type_result else "Unknown Type"
        strength = strength_result[0]['Strength'] if strength_result else 0
        is_resistant = 'Yes' if resistance_result else 'No'

        return {
            "type": card_type,
            "strength": strength,
            "weather_resistant": is_resistant,
        }

    def is_combat_affected(self, combat_type, special_cards):
        result = list(
            self.prolog.query(f'''{combat_type}_weather_affected([{', '.join(f"'{c}'" for c in special_cards)}])'''))
        return 'Yes' if result != [] else 'No'

    def is_card_affected(self, card_name, special_cards):
        result = list(
            self.prolog.query(
                f'''char_weather_affected('{card_name}', [{', '.join(f"'{c}'" for c in special_cards)}])'''))
        return 'Yes' if result != [] else 'No'

    def get_card_strength(self, card_name, special_cards):
        result = list(self.prolog.query(
            f'''character_strength('{card_name}', Strength, [{', '.join(f"'{c}'" for c in special_cards)}])'''))
        return f"Strength = {result[0]['Strength'] if result else 0}"
