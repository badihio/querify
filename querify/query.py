import argparse
import sql_metadata

import apps
import database


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

    app = apps.all_apps[args.app]

    with database.client.DB() as db:
        db.create_sources_tables(
            sources=app.get_sources(),
        )

        db.insert_source_data(
            source=app.get_source_by_name(
                source_name='files',
            ),
            source_data=app.get_source_data(
                source_name='files',
            ),
        )

        result = db.query(
            query='SELECT * FROM files WHERE name LIKE "%python%"',
        )

        import pprint
        pprint.pprint(result)


if __name__ == '__main__':
    query()
