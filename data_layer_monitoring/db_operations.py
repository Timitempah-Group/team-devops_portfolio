import redis
from pymongo import MongoClient
import psycopg2
from datetime import datetime, timezone

print("=" * 60)
print("REDIS OPERATIONS")
print("=" * 60)

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

r.set('portfolio:status', 'active')
r.set('portfolio:last_check', datetime.now(timezone.utc).isoformat())
r.hset('portfolio:task', mapping={'name': 'data_layer_monitoring', 'stage': 'redis_verified'})

status = r.get('portfolio:status')
last_check = r.get('portfolio:last_check')
task_info = r.hgetall('portfolio:task')

print(f"SET portfolio:status -> 'active'")
print(f"GET portfolio:status -> '{status}'")
print(f"GET portfolio:last_check -> '{last_check}'")
print(f"HGETALL portfolio:task -> {task_info}")
print(f"Redis DBSIZE (total keys) -> {r.dbsize()}")

print()
print("=" * 60)
print("MONGODB OPERATIONS")
print("=" * 60)

mongo_client = MongoClient('mongodb://admin:demopassword@localhost:27017/')
db = mongo_client['portfolio_db']
collection = db['tasks']

collection.delete_many({})

insert_result = collection.insert_many([
    {'task': 'data_layer_monitoring', 'status': 'in_progress', 'created': datetime.now(timezone.utc)},
    {'task': 'octopus_deploy', 'status': 'not_started', 'created': datetime.now(timezone.utc)},
    {'task': 'data_warehousing', 'status': 'not_started', 'created': datetime.now(timezone.utc)},
])
print(f"INSERT MANY -> {len(insert_result.inserted_ids)} documents inserted")

found = collection.find_one({'task': 'data_layer_monitoring'})
print(f"FIND ONE (task=data_layer_monitoring) -> {found}")

update_result = collection.update_one(
    {'task': 'data_layer_monitoring'},
    {'$set': {'status': 'verified'}}
)
print(f"UPDATE ONE -> matched {update_result.matched_count}, modified {update_result.modified_count}")

updated_doc = collection.find_one({'task': 'data_layer_monitoring'})
print(f"FIND ONE after update -> {updated_doc}")

all_docs = list(collection.find({}))
print(f"FIND ALL -> {len(all_docs)} total documents in collection")

delete_result = collection.delete_one({'task': 'octopus_deploy'})
print(f"DELETE ONE (task=octopus_deploy) -> deleted count {delete_result.deleted_count}")

remaining = collection.count_documents({})
print(f"Remaining document count -> {remaining}")

print()
print("=" * 60)
print("POSTGRESQL OPERATIONS")
print("=" * 60)

pg_conn = psycopg2.connect(
    host='localhost',
    port=5432,
    dbname='demodb',
    user='postgres',
    password='demopassword'
)
pg_cursor = pg_conn.cursor()

pg_cursor.execute("""
    DROP TABLE IF EXISTS portfolio_tasks;
    CREATE TABLE portfolio_tasks (
        id SERIAL PRIMARY KEY,
        task_name VARCHAR(100) NOT NULL,
        status VARCHAR(50) NOT NULL,
        created_at TIMESTAMP DEFAULT NOW()
    );
""")
pg_conn.commit()
print("CREATE TABLE portfolio_tasks -> done")

pg_cursor.execute("""
    INSERT INTO portfolio_tasks (task_name, status) VALUES
    ('data_layer_monitoring', 'in_progress'),
    ('octopus_deploy', 'not_started'),
    ('data_warehousing', 'not_started'),
    ('mlops_ai_pipeline', 'not_started');
""")
pg_conn.commit()
print(f"INSERT -> {pg_cursor.rowcount} rows inserted (last statement)")

pg_cursor.execute("SELECT * FROM portfolio_tasks;")
rows = pg_cursor.fetchall()
print(f"SELECT * FROM portfolio_tasks -> {len(rows)} rows")
for row in rows:
    print(f"  {row}")

pg_cursor.execute("UPDATE portfolio_tasks SET status = 'verified' WHERE task_name = 'data_layer_monitoring';")
pg_conn.commit()
print(f"UPDATE -> {pg_cursor.rowcount} row(s) updated")

pg_cursor.execute("SELECT task_name, status FROM portfolio_tasks WHERE task_name = 'data_layer_monitoring';")
updated_row = pg_cursor.fetchone()
print(f"SELECT after update -> {updated_row}")

pg_cursor.execute("DELETE FROM portfolio_tasks WHERE task_name = 'octopus_deploy';")
pg_conn.commit()
print(f"DELETE -> {pg_cursor.rowcount} row(s) deleted")

pg_cursor.execute("SELECT COUNT(*) FROM portfolio_tasks;")
count = pg_cursor.fetchone()[0]
print(f"Remaining row count -> {count}")

pg_cursor.close()
pg_conn.close()
mongo_client.close()

print()
print("=" * 60)
print("ALL OPERATIONS COMPLETE")
print("=" * 60)
