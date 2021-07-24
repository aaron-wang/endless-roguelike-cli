# Endless Roguelike (CLI)
Modest text-based roguelike game. Runs directly in the command line interface.

1. Run `main.py`. 
2. Follow the instructions on screen. 
* Alternatively, `rules.txt` is provided [below](#Rules).

The `log.txt` provided is an example. With each game, `log.txt` is overwrited.

## Note
This is a school project.

Awkward programming practices are due to requirements in the rubric for this open-ended project.

Examples include:
- over-reliance on `.txt` files and high redundancies
> e.g., basing weight distribution on occurences of words in `.txt` files
> 
> as opposed to creating numerical weight values
- not using data structures (correctly)
- copious use of functions
- unnecessarily specific instructions
- lack of complex file directories (all files are in one folder)
- etc....

This is not an exhaustive list.

For archival purposes, the original files will remain untouched.

## Rules
Welcome to the 2D Rogue Game!!

You are on a 2d grid with dimensions `n x n`

    (you can choose the dimensions).

You will have to traverse all `n x n` squares before moving on to the next floor.

    There are either: monsters, items, or (one-time) powerups on each square

Before you can move onto the next grid, you will fight one "boss" monster.

    There are an endless amount of floors.

Powerups, items, and monster "stats" scale (upwards) with floors.

You will be shown the full board:

### == BOARD ==

- `&` - Monster
- `^` - Power Up
- `I` - Item
- `?` - Unknown (equal chance for any of the above)
- `.` - Empty

Monsters have a higher generation rate than powerups, items, and unknown combined.

### == TRAVERSAL ==

Type `w`, `a`, `s`, `d` for moving in the board
- `w` - up
- `a` - left
- `s` - down
- `d` - right

You will be warned if you choose invalid moves.

### == STATS ==

- Health - How much raw damage you can take
- Atttack - How much raw damage you deal
- Defence - `X%` of incoming damage is reduced (to a maximum of `75%`)
- Speed - How fast you move in battles (a higher speed means you attack more often and with higher priority)
- Luck - Base stat used to calculate random chances for improving stats via powerups or items

Monster Luck (hidden) - A global variable hidden to the player. This increases with each floor clear.

### == BATTLE ==

Battles are automated, and logs in the console are provided.

HP only heals during:
- boss clears (gain `100%` of total HP back)
- cell (includes all tiles) clears (gain `~0.5-2%` of total HP back - depending on your board size)

Monsters will subtract points from your HP

Speed determines who attacks first, and forms the order of attacks from player and monster

- E.g. A player has slightly higher speed than a monster:
- Player = `P`, Monster = `M`
- `P P M P M / P P M P M / ...`

Each floor becomes increasingly difficult.

### == BOSS == 

After clearing all regular tiles, you are automatically sent to fight the boss.

- The boss has a significant health boost, minor attack boost, and a large speed decrease.
- Bosses determine if your run ends or continues to the next floor.
- Try to have both high speed and attack stats when engaging with bosses.
- First 1-3 floors may have easier bosses, depending on your board size.

### == INVENTORY ==
Current items are shown. You can only equip at most 5 items.

Items are automatically equipped or scrapped based on your current inventory.

The "better" an item's adjective is, the better the item is (in general).

Item names come from .txt files, and distributed probability is based on the adjfreq.txt file

Your current "stats" are also shown.

Don't forget to press `i` every now and then to check on your stats and gathered items.

### == SCORING ==
Your score is a function of the board dimension, what floor you are on, and how many monsters you fight.

Clearing the boss will provide a large point boost.

In general, clearing more floors results in higher scores.

Larger boards may grant more points, but have the downside of increased difficulty (a noticeable sharp increase beyond floor 3).

END OF RULES
------------
