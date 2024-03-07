import sys
import sql_metadata

import sources


def query():
    try:
        query = sys.argv[1]
    except IndexError:
        raise Exception(
            'Missing query',
        )

    parsed_query = sql_metadata.Parser(query)

    try:
        source_name, table_name = parsed_query.tables[0].split('.')
    except Exception:
        raise ValueError(
            'From has to contain database name and table name',
        )

    source = sources.all_sources.get(source_name)

    if not source:
        raise ValueError(
            f'{source_name} is not supported'
        )

    print(source.name)


if __name__ == '__main__':
    query()
