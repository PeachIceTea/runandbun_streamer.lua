# Run and Bun - Streamer script

## What?
This is a modified version of [ForwardFeed's runandbun_script_imports.lua](https://github.com/ForwardFeed/runbuncalc/blob/master/src/runandbun_script_imports.lua) for [mgba](https://mgba.io/).

Rather than requiring you to call `export()` manually, this modification will check for changes every frame. On my computer this reduces the unlimited speed up from ~3000 frames to ~2000 frames.
