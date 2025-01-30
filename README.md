[![GatorGrader](../../actions/workflows/main.yml/badge.svg)](../../actions/workflows/main.yml)

# Your starship

For quite a while, you've wanted your own starship. After some turn of fate, you've finally got one --
except it doesn't seem to be in working order. The person you got it from (won it from?) told you
that it might be missing a few things that were scattered around the ship before in their mad dash
to get it ready to hand it over to you, something about the `Engine` in the `engine-room` missing some
parts...

## Episode 1: Liftoff!

### Gathering parts

Your starship's engine needs `3` parts replaced in order to run correctly:

* `1` sprocket
* `1` flux capacitor
* `1` thermocube

#### Moving about the ship

To move around in the ship, you'll need to use a command called `cd`. This stands for _c_hange _d_irectory
and each folder in your ship is a directory ("room") that you can go to. To list the options available to
you, type `ls` (short for `list`). Anything you see in the list that pops up is a place that you can go
right now.

Try these out by seeing where you can go and then changing your directory to the `bridge`: `cd bridge`.

#### Your inventory

You're not sure where in the ship they are, though you've been promised that they're in there...somewhere.
When you find a part that you need, you can grab it by using a command called `get`. For example, if you
were to find a `Sprocket.py` somewhere in the ship, you would: `get Sprocket.py`. This would add the 
`Sprocket` to your inventory. To see what's in your inventory: type `inventory` at the command line.

Curious about what you have in your inventory? You can find out more about it by using the `info` command.
If you've got a `ThermoCube` in inventory, try it out by typing `info ThermoCube`.

#### Using ship services

Your starship has two devices that help power and guide it: the `Controls` and the `Engine`.

##### `Engine`

Once you've gathered the necessary parts, visit the `engine-room` and try to start the `Engine` by typing:
`./Engine`. If everything goes well, the `Engine` should notify you that it has started!

##### `Controls`

The ship's `Controls` will help launch the ship once the `Engine` has been started. To use the `Controls`, type:
`./Controls` when you're in the same room (the `bridge`).

## Episode 2: Cracking the code

> Note: this episode takes place after finishing the previous one, `Liftoff!`; successfully completing that
> part of the storyline will unlock the `Keypad`.

As the saying goes: more starships, more problems. It seems that this particular ship has some peculiar power
issues: a circuit panel on the `bridge` probably needs some repair. The catch -- you can't get to it because
it's locked!

After starting the ship, though, you notice a `Keypad` that _might_ (hint: actually does) open a circuit panel
for repair. Like everything else on this ship, it needs a bit of TLC. Can you figure out how the internal
code algorithm works in order to open the panel?
