import colorama
import mo_sql_parsing
import tabulate
import typing
import sys

import database
import sources


def query(
    query=None,
    *_,
):
    if query is None:
        raise Exception('Missing query')

    parsed_query = mo_sql_parsing.parse(query)

    source = sources.get_source_by_name(
        source_name=parsed_query['from'],
    )

    with database.client.DB() as db:
        db.create_source_table(
            source=source,
        )

        db.insert_source_data(
            source=source,
        )

        columns, rows = db.query(
            query=query,
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
    query(*sys.argv[1:])
