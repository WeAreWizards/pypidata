# pypydata - build an offline index of pypi.

There are two scripts here: `getpypidata.py` and `build_index.py`.

## Getting the data

First you need to run `getpypidata.py` which fetches the json metadata
for every project from pypi:

```sh
$ python getpypidata.py
Fetched: 1475, Total: 52757, Percent: 2.8, Errors: 0
```

The script will write protobufs with some metadata such as the
timestamp and the URL used for fetching into `./raw`. After running
for a few hours it should look like this:

```sh
$ ls raw/ | wc -l
52849
```

## Transforming the data

There is an example script which writes a hdf file with two pandas
dataframes, one for the package metadata (license etc) and one for all
the versions + their distribution type (sdist, wheel, etc):

```sh
$ python build_index.py 
```

Note that for reasons unknown a fair amount of projects don't have
json metadata attached. We're ignoring those.
