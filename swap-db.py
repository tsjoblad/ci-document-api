from tableaudocumentapi import Workbook
import argparse, shutil

'''
no server swap:
    python swap-db.py -u db_tucker -d connectivity_ci_tucker -p tuckerdb

server swap
    python swap-db.py -s tucker.db.com -u db_tucker -d connectivity_ci_tucker -p tuckerdb
'''


def main():
    # Set cli arguments
    parser = argparse.ArgumentParser(description='Set the db, username, twb name')
    parser.add_argument('--server', '-s', required=False, help='server address')
    parser.add_argument('--username', '-u', required=True, help='db username')
    parser.add_argument('--database', '-d', required=True, help= 'database name')
    parser.add_argument('--partner', '-p', required=True, help='partner name to append')   

    args = parser.parse_args()

    src = 'ci-dashboards.twb'

    # create new twb
    filename = shutil.copyfile(src, args.partner+'-'+src)

    # set source and change vars
    sourceWB = Workbook(filename)
    if args.server:
        sourceWB.datasources[0].connections[0].server = args.server
    sourceWB.datasources[0].connections[0].dbname = args.database
    sourceWB.datasources[0].connections[0].username = args.username
    sourceWB.save()

    print(f"Updated workbook for {args.partner}:")
    print(f"\tServer: {sourceWB.datasources[0].connections[0].server}")
    print(f"\tDatabase: {sourceWB.datasources[0].connections[0].dbname}")
    print(f"\tUser: {sourceWB.datasources[0].connections[0].username}")


if __name__ == '__main__':
    main()