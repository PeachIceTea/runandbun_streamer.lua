# Run and Bun - Streamer script

## What?
This is a modified version of [ForwardFeed's runandbun_script_imports.lua](https://github.com/ForwardFeed/runbuncalc/blob/master/src/runandbun_script_imports.lua) for [mgba](https://mgba.io/).

Rather than requiring you to call `export()` manually, this modification will check for changes every frame. On my computer this reduces the unlimited speed up from ~3000 frames to ~2000 frames.

It will also keep he party folder up to date with sprites of the current party.

## Setup
1. Get [mgba](https://mgba.io/).
2. [Get the latest version of the script.](https://github.com/PeachIceTea/runandbun_streamer.lua/archive/refs/heads/master.zip)
3. Extract the contents of the zip into the mgba directory.
4. [Get the latest version of PokéSprite.](https://github.com/msikma/pokesprite/archive/refs/heads/master.zip)
5. Extract the PokéSprite zip and copy the regular sprites from `pokemon-gen8` into the sprites directory.
6. Copy `egg.png` and either `unknown-gen5.png` or `unknown.png` (if `-gen5` is used rename it).
8. Load the script in mgba from Tools/Scripting... and then File/Load script..., select the `runandbun_streamer.lua` from the file dialog.
9. Add sprites from the `party` directory to your OBS overlay.
