import harperdb

HARPERDB_PASSWORD=  'rahuljha'
HARPERDB_URL='https://notesapp-rahuljha.harperdbcloud.com'
HARPERDB_USERNAME='rahuljha'

db=harperdb.HarperDB(
    url=HARPERDB_URL,
    username=HARPERDB_USERNAME,
    password=HARPERDB_PASSWORD
)

