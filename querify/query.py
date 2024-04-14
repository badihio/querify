import argparse
import colorama
import mo_sql_parsing
import tabulate
import typing

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

    parsed_query = mo_sql_parsing.parse(args.query)

    print(parsed_query)

    app = apps.all_apps[args.app]

    source_cls = app.get_source_by_name(
        source_name=parsed_query['from'],
    )

    source = source_cls(
        filters=parsed_query.get('where', {}),
    )

    with database.client.DB() as db:
        db.create_source_table(
            source=source,
        )

        db.insert_source_data(
            source=source,
        )

        columns, rows = db.query(
            query=args.query,
        )

        display(
            columns=columns,
            rows=rows,
        )


def display(
    columns: list[str],
    rows: list[typing.Any],
):
    print(
        tabulate.tabulate(
            rows,
            [
                colorama.Style.BRIGHT +
                f'{column}' +
                colorama.Style.RESET_ALL
                for column
                in columns
            ],
            tablefmt='psql',
        )
    )


if __name__ == '__main__':
    query()
