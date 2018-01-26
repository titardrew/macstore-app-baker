# macstore_app_baker
Little script for building .pkg files

To use this script you shold:

1. Place this bake.py into the folder holding your *.entitlements and *.app files.
2. Make sure that your *.app file matches the name of your application (That you want to see in mac store).
3. Have Python (3 or 2) installed on your mac. If you don't have - use Homebrew to install it (or in any other way).

To run this script:

```bash
$ python bake.py --name "DEVELOPER'S NAME" --app "APP NAME" --entitlements "ENTITLEMENTS.entitlements"
```
Here's the "APP NAME" should match the name (without .app) of your *.app file,
"ENTITLEMENTS.entitlements" should match the name (with .entitlements) of your *.entitlements file.

See --help for details:

```bash
usage: bake.py [-h] [-n NAME] [-a APP] [-e ENTITLEMENTS]

Signs and builds the app.

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Developer's name 
                        (default: Maxim Titarenko)
  -a APP, --app APP     Application name. 
                        (default: Football World Cup 2018 Russia)
  -e ENTITLEMENTS, --entitlements ENTITLEMENTS
                        Entitlements filename. Type "gen" to set its value to output name without spaces. 
                        (default: FootballWorldCup2018Russia.entitlements)
```

Wrote this script for particular dude so the defaults may look weird for you.
