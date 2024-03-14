import argparse
import sql_metadata

import apps


def query():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-a',
        '--app',
        help='App name',
        required=True,
        type=str,
        choices=list(apps.all_apps.keys()),

    )

    parser.add_argument(
        '-q',
        '--query',
        help='Query to run',
        required=True,
        type=str,
    )

    args = parser.parse_args()

    parsed_query = sql_metadata.Parser(args.query)

    app = apps.all_apps.get(args.app)

    print(app.get_source_data(
        source_name='files',
    ))


if __name__ == '__main__':
    query()
