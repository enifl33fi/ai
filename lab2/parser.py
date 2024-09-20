import re
from typing import Union, Tuple, List, Optional


class Parser:
    @staticmethod
    def parse(user_input: str) -> Optional[Union[Tuple[int, str], Tuple[int, str, List[str]]]]:
        # 1) Is card <name> weather resistant?
        match: re.Match = re.match(r'Is card ([\w\s]+) weather resistant\?', user_input)
        if match:
            card_name: str = match.group(1).strip()
            return 1, card_name

        # 2) What is known about the card <name>?
        match: re.Match = re.match(r'What is known about the card ([\w\s]+)\?', user_input)
        if match:
            card_name: str = match.group(1).strip()
            return 2, card_name

        # 3) Is close/ranged/siege combat affected by the weather? <special cards separated by comma>
        match: re.Match = re.match(r'Is (close|ranged|siege) combat affected by the weather\? (.+)', user_input)
        if match:
            combat_type: str = match.group(1)
            special_cards: list[str] = [card_name.strip() for card_name in match.group(2).split(",")]
            return 3, combat_type, special_cards

        # 4) Is card <name> affected by the weather? <special cards separated by comma>
        match: re.Match = re.match(r'Is card ([\w\s]+) affected by the weather\? (.+)', user_input)
        if match:
            card_name: str = match.group(1).strip()
            special_cards: list[str] = [name.strip() for name in match.group(2).split(",")]
            return 4, card_name, special_cards

        # 5) Get card <name> strength. <special cards separated by comma>
        match: re.Match = re.match(r'Get card ([\w\s]+) strength\.\s*(.+)', user_input)
        if match:
            card_name: str = match.group(1).strip()
            special_cards: list[str] = [name.strip() for name in match.group(2).split(",")]
            return 5, card_name, special_cards

