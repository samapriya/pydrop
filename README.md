# pydrop: Minimal Python Client for Digital Ocean Droplets

This is a minimal tool designed to interact with the Digital Ocean API. This does not translate all functionalities of the API but is a template I created for some of the most common operations I could perform. New tools will be added in the future as I familiarize myself further with the API structure and use as a student. For now this tool allows you to summarize all your droplets running, including and necessarily a price summary to keep tabs on your droplets monthly and hourly rates. The tool also allows you to seach by tags, delete a drop or perfrom actions such as start, stop or shutdown a droplet.

## Table of contents
* [Installation](#installation)
* [Getting started](#getting-started)
* [Digital Ocean Python CLI Tools](#digital-ocean-python-cli-tools)
	* [Digital Ocean Key](#digital-ocean-key)
    * [Droplets Info](#droplets-info)
    * [Droplets Delete](#droplets-delete)
    * [Droplets Action](#droplets-action)

## Installation
This assumes that you have native python & pip installed in your system, you can test this by going to the terminal (or windows command prompt) and trying

```python``` and then ```pip list```

If you get no errors and you have python 2.7.14 or higher you should be good to go. Please note that I have tested this only on python 2.7.15 but can be easily modified for python 3.

To install **Python CLI for Digital Ocean** you can install using two methods

```pip install pydrop```

or you can also try

```
git clone https://github.com/samapriya/pydrop.git
cd pydrop
python setup.py install
```
For linux use sudo.

Installation is an optional step; the application can be also run directly by executing pydrop.py script. The advantage of having it installed is being able to execute ppipe as any command line tool. I recommend installation within virtual environment. If you don't want to install, browse into the pydrop folder and try ```python pydrop.py``` to get to the same result.

## Getting started

As usual, to print help:

```
usage: pydrop [-h] {dokey,dropinfo,dropdelete,dropaction} ...

Digital Ocean API Python CLI

positional arguments:
  {dokey,dropinfo,dropdelete,dropaction}
    dokey               Enter your Digital Ocean API Key
    dropinfo            Prints information about all your droplets
    dropdelete          Permanently deletes the droplet
    dropaction          Performs an action on your droplets

optional arguments:
  -h, --help            show this help message and exit

```

To obtain help for a specific functionality, simply call it with _help_ switch, e.g.: `pydrop dropinfo -h`. If you didn't install pydrop, then you can run it just by going to *pydrop* directory and running `python pydrop.py [arguments go here]`

## Digital Ocean Python CLI Tools
The Planet Toolsets consists of tools required to access control and download planet labs assets (PlanetScope and RapidEye OrthoTiles) as well as parse metadata in a tabular form which maybe required by other applications.

### Digital Ocean Key
This tool basically asks you to input your Planet API Key using a password prompt this is then used for all subsequent tools. This tool now includes an option for a quiet authentication using the API key incase it is unable to invoke an interactive environment such as in Google colaboratory.

```
usage: pydrop dokey [-h] [--key KEY]

optional arguments:
  -h, --help  show this help message and exit

Optional named arguments:
  --key KEY   Your Digital Ocean API Key
```

If using on a private machine the Key is saved as a csv file for all future runs of the tool.

### Droplets Info
The aoijson tab within the toolset allows you to create filters and structure your existing input file to that which can be used with Planet's API. The tool requires inputs with start and end date, along with cloud cover. You can choose from multiple input files types such as KML, Zipped Shapefile, GeoJSON, WKT or even Landsat Tiles based on PathRow numbers. The geo option asks you to select existing files which will be converted into formatted JSON file called aoi.json. If using WRS as an option just type in the 6 digit PathRow combination and it will create a json file for you.

```
usage: pydrop dropinfo [-h] [--tag TAG]

optional arguments:
  -h, --help  show this help message and exit

Optional named arguments:
  --tag TAG   Use a tag to refine your search
```

### Droplets Delete
It is not possible to call the tool on an idlist instead of using a JSON , this option is useful when you want when you want to use the same item ID with different asset types quickly. For example the item ID for PSScene4Band analytic and PSScene4Band analytic_sr is the same. This is a quicker way to parse different asset type and create an IDlist for activation and download.
```
usage: pydrop dropdelete [-h] [--id ID] [--name NAME]

optional arguments:
  -h, --help   show this help message and exit

Optional named arguments:
  --id ID      Use an image ID to delete droplet
  --name NAME  Use an image name to delete droplet
```

### Droplets Action
The activatepl tab allows the users to either check or activate planet assets, in this case only PSOrthoTile and REOrthoTile are supported because I was only interested in these two asset types for my work but can be easily extended to other asset types. This tool makes use of an existing json file sturctured for use within Planet API or the aoi.json file created earlier

```
usage: pydrop dropaction [-h] [--id ID] [--name NAME] [--action ACTION]
                       [--rename RENAME]

optional arguments:
  -h, --help       show this help message and exit

Optional named arguments:
  --id ID          Use an image ID to perform action
  --name NAME      Use an image name to perform action
  --action ACTION  Action type |shutdown="graceful shutdown"|power_off="hard
                   shutdown"|power_on="power on"|rename="rename
  --rename RENAME  Incase you are renaming droplet you can provide new name
```

