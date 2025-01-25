import os
import sys

from yaml import safe_load

import filters


def generate_palette(palette_raw, textures_names):
    # Since palette is basically a whitelist filter, compute it first
    palette_in = filters.compute_filter(palette_raw['includes'], textures_names, 'palette includes')

    # And now, for the results of this filter... we apply "exludes" filter!
    palette_ex = filters.compute_filter(palette_raw['excludes'], textures_names, 'palette excludes')
    palette = [rule for rule in (palette_in).keys() if rule not in (palette_ex).keys()]

    return sorted(palette)


def get_palettes_data(palettes_path, textures_path):
    with open(palettes_path, 'r') as palettes_f:
        palettes_raw = safe_load(palettes_f)

    textures_names = sorted(os.listdir(textures_path))
    textures_names = list(filter(lambda file: file.endswith('.png'), textures_names))

    # Generate palettes data one by one
    palettes_data = []

    for palette_raw in palettes_raw['palettes']:
        palette_data = {}
        palette_data['name'] = palette_raw['name']
 
        palette_res = generate_palette(palette_raw, textures_names)
        palette_data['textures'] = palette_res
        palette_data['count'] = len(palette_res)

        palettes_data.append(palette_data)

    return palettes_data
