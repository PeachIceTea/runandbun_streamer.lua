# Run and Bun - Streamer script

## What?
This is a modified version of [ForwardFeed's runandbun_script_imports.lua](https://github.com/ForwardFeed/runbuncalc/blob/master/src/runandbun_script_imports.lua) for [mgba](https://mgba.io/).

Rather than requiring you to call `export()` manually, this modification will check for changes every frame. On my computer this reduces the unlimited speed up from ~3000 frames to ~2000 frames.

It will also update the sprites in the `party` directory to reflect the current party.

## Setup
1. Get [mgba](https://mgba.io/).
2. [Get the latest version of the script.](https://github.com/PeachIceTea/runandbun_streamer.lua/archive/refs/heads/master.zip)
3. Extract the contents of the zip into the mgba directory.
4. [Get the latest version of PokéSprite.](https://github.com/msikma/pokesprite/archive/refs/heads/master.zip)
5. Extract the PokéSprite zip and copy the regular sprites from `pokemon-gen8` into the sprites directory.
6. Copy `egg.png` and either `unknown-gen5.png` or `unknown.png` (if `-gen5` is used rename it).
8. Load the script in mgba from Tools/Scripting... and then File/Load script..., select the `runandbun_streamer.lua` from the file dialog.
9. Add sprites from the `party` directory to your OBS overlay.

## Better images
If PokéSprite doesn't suit your needs, maybe  [these images from Bulbapedia](https://github.com/HybridShivam/Pokemon) will.
Their names aren't compatible with the script by default. The python script in [rename_script](https://github.com/PeachIceTea/runandbun_streamer.lua/tree/master/rename_script)
can rename the files to make them work. `python ./rename_script/rename_sprites.py --help` can be used to learn about usage.

### Use Bulbapedia sprites
1. [Get the sprites.](https://github.com/HybridShivam/Pokemon/archive/refs/heads/master.zip)
2. Extract the contents of one of the directories in `assets` (if in doubt, just use `imagesHQ`).
3. Open a terminal window in the mgba directory and run `python ./rename_script/rename_sprites.py --origin <path_to_extracted_assets> --target ./sprites`.
4. Create an image that should be used if the party slot is empty, place it into `sprites` and name it `unknown.png`.
