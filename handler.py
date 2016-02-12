from __future__ import print_function

import json
import logging
# https://github.com/jkehler/awslambda-psycopg2
import psycopg2

log = logging.getLogger()
log.setLevel(logging.DEBUG)


def lambda_handler(event, context):
    log.debug("Received event {}".format(json.dumps(event)))

    conn = psycopg2.connect(
            host="host",
            user="username",
            password="password",
            database="database",
    )

    with conn.cursor() as c:
        # Get total
        c.execute("""SELECT Count(*) FROM people""")
        sum = c.fetchone()[0]  # first row, and column

    conn.commit()
    conn.close()
    return json.dumps(sum)