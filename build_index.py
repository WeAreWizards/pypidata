"""Transform the scraped pypi data into a pandas DataFrame for later
consumption.

$ nix-shell -p pythonPackages.nose pythonPackages.protobuf \
    pythonPackages.setuptools pythonPackages.pandas \
    pythonPackages.tables pythonPackages.ipython
"""
import raw_data_pb2
import pandas
import glob
import json

def emit_json_data():
    for path in glob.glob('./raw/*'):
        with open(path) as f:
            rd = raw_data_pb2.RawData()
            rd.ParseFromString(f.read())

        if '<h1>Not Found</h1>' in rd.package_json:
            print "Not found: {}".format(rd.package_name)
            continue
        
        try:
            info = json.loads(rd.package_json)
        except ValueError:
            print "Could not decode", rd.package_json
        yield rd, info
       
def emit_package_records():
    for rd, info in emit_json_data():
        license = info['info'].get('license', 'n/a')
        # name can be different from package identifier
        name = info['info'].get('name', 'n/a') 
        yield (
            rd.retrieved_timestamp,
            rd.package_name,
            license,
            name,
        )

def emit_version_records():
    for rd, info in emit_json_data():
        for version, releases in info['releases'].items():
            for release in releases:
                yield (
                    rd.retrieved_timestamp,
                    rd.package_name,
                    version,
                    release.get('downloads'),
                    release.get('md5_digest'),
                    release.get('packagetype'),
                    release.get('size'),
                )

def main():
    package_df = pandas.DataFrame.from_records(
        emit_package_records(),
        columns=['timestamp', 'pypi_name', 'license', 'name'],
    )
    version_df = pandas.DataFrame.from_records(
        emit_version_records(),
        columns=['timestamp', 'pypi_name', 'version',
                 'downloads',  'md5_digest',
                 'packagetype', 'size'],
    )
    h5 = pandas.HDFStore('./pypi.h5', mode='w')
    h5['package_df'] = package_df
    h5['version_df'] = version_df
    h5.close()

    
if __name__ == '__main__':
    main()
