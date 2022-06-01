import json
import asyncio
import asyncpg


async def lambda_handler(event=None, context=None):
    conn = await asyncpg.connect(event["body"]["connectionString"])

    sql = event['body']['sql']

    rows = await conn.fetch(sql)

    output = [dict(row) for row in rows]

    print(json.dumps(output, indent=4, sort_keys=True, default=str))

    await conn.close()


if __name__ == "__main__":
    event = {
        "body": {
            "connectionString": "postgres://postgres:postgrespw@localhost:55001",
            "sql": "SELECT * FROM users",
        },
    }
    context = {}
    asyncio.run(lambda_handler(event, context))
