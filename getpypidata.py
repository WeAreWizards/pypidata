"""
Build an offline archive of the pypi index.

Note that we're intentionally skipping error handling.

$ nix-shell -p pythonPackages.requests pythonPackages.nose \
    pythonPackages.protobuf pythonPackages.eventlet \
    pythonPackages.setuptools
"""
import os
import eventlet
import re
import requests
import raw_data_pb2
import time
import hashlib
import sys

CONCURRENCY = 20
INDEX_URL = 'https://pypi.python.org/simple'
PACKAGE_URL = 'https://pypi.python.org/pypi/{}/json'
# pypi package names are simple enough to be parsed with a regex.
PACKAGE_RE = re.compile(r"href='([^']+)'", re.M)


def fetch_and_store(package_name):
    url = PACKAGE_URL.format(package_name)
    try:
        content = requests.get(url).content
    except IOError:
        return [package_name]

    pb = raw_data_pb2.RawData(
        retrieved_timestamp=int(time.time()),
        url_used=url,
        package_name=package_name,
        package_json=content,
    )
    raw_data = pb.SerializeToString()
    filename = hashlib.sha1(raw_data).hexdigest()
    with open(os.path.join('./raw', filename), 'w') as f:
        f.write(raw_data)

    return []


def main():
    index = requests.get(INDEX_URL).content
    package_names = set(PACKAGE_RE.findall(index))

    try:
        os.makedirs('./raw')
    except os.error:
        pass

    # fetch all the json
    pool = eventlet.GreenPool(CONCURRENCY)
    while package_names:
        errors = []
        counter = 0
        for error in pool.imap(fetch_and_store, package_names):
            errors.extend(error)
            counter += 1
            sys.stdout.write("Fetched: {}, Total: {}, Percent: {:.1f}, Errors: {}\r".format(
                counter, len(package_names),
                counter * 100.0 / len(package_names), len(errors)))
            sys.stdout.flush()

        package_names = errors


def test_re():
    TESTDATA = """
    <a href='115wangpan'>115wangpan</a><br/>
    """
    assert PACKAGE_RE.findall(TESTDATA) == ['115wangpan']

if __name__ == '__main__':
    main()
