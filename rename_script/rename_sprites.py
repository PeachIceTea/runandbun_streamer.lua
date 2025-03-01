import os
import json
import sys
import shutil
import argparse
from typing import Optional

def fix_sprite_name(id: int, special: Optional[str]) -> tuple[str, Optional[str]]:
    id_str = str(id).rjust(3, "0")
    match (id_str, special):
        case (_, "F"|"M"|"o"|"Oh"):
            return (f"{id_str}", None)
        case ("137", "Z"):
            return ("474", None)
        case ("741", "Pa'u "):
            return (id_str, "Pau")
        case ("681", "Both"):
            return (id_str, "Blade")
        case ("555", "Galar"):
            return (id_str, "Galar-Standard")
        case ("025", pika_special):
            match pika_special:
                case "PhD":
                    return (id_str, "Phd")
                case "Original"|"Hoenn"|"Sinnoh"|"Unova"|"Kalos"|"Alola"|"Partner"|"World":
                    return (id_str, f"{pika_special}-Cap")
                case _:
                    return (id_str, pika_special)
        case ("800", necro_special):
            match necro_special:
                case "Dusk-Mane":
                    return (id_str, "Dusk")
                case "Dawn-Wings":
                    return (id_str, "Dawn")
                case _:
                    return (id_str, necro_special)
        case _:
            return (id_str, special)

def get_sprite(id: int, available_sprites: list, special: Optional[str]=None) -> Optional[str]:
    id_str, special = fix_sprite_name(id, special)
    search_term_non_special = f"{id_str}.png"
    search_term = f"{id_str}{("-" + special if special else "")}.png"

    found_non_special = False
    for sprite_name in available_sprites:
        if sprite_name == search_term_non_special:
            found_non_special = True

        if sprite_name == search_term:
            return sprite_name

    if found_non_special:
        print(f"{search_term} not found. Falling back to {search_term_non_special}.", file=sys.stderr)
        return search_term_non_special
    else:
        print(f"{search_term} not found. No fallback available.", file=sys.stderr)
        return None

def copy_sprite(origin_path: str, numbered_name: str, target_path: str, target_name: str):
    shutil.copy2(f"{os.path.join(origin_path, numbered_name)}", f"{os.path.join(target_path, target_name.lower())}.png")

def copy(origin: str, target: str):
    script_path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(script_path, "rnb_mons.json"), "r") as rnb_mons_file:
        rnb_mons = json.load(rnb_mons_file)

    with open(os.path.join(script_path, "pokedex.json"), "r") as pokedex_file:
        pokedex = json.load(pokedex_file)

    available_sprites = os.listdir(origin)

    for rnb_mon in rnb_mons:
        name, *info = rnb_mon.split("-")
        id = pokedex.get(name)
        if id is None:
            id = pokedex.get(rnb_mon)
            sprite_name = get_sprite(id, available_sprites)
            if sprite_name is None:
                print(f"No sprite for {rnb_mon}.")
                continue
            copy_sprite(origin, sprite_name, target, rnb_mon)
            continue

        sprite_name = None
        if len(info) == 0:
            sprite_name = get_sprite(id, available_sprites)
        else:
            sprite_name = get_sprite(id, available_sprites, special="-".join(info))

        if sprite_name is None:
            print(f"No sprite for {rnb_mon}.")
            continue
        copy_sprite(origin, sprite_name, target, rnb_mon)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename sprites from https://github.com/HybridShivam/Pokemon to work with runandbun_streamer.lua")
    parser.add_argument("--origin", type=str, default="./numbered_sprites", help="Path to numbered sprites.")
    parser.add_argument("--target", type=str, default="./sprites", help="Path to the sprites directory the script will read from.")
    args = parser.parse_args()

    copy(args.origin, args.target)
