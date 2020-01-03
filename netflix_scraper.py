import os
import sys
import datetime
import csv
import collections


def parse_show(show,watched):
    # -----------------------------------------------------------------------------------------------
    # Created: 20200103 by Jason Braid
    # Strip out season, episode name if applicable
    # -----------------------------------------------------------------------------------------------

    NetflixShow = collections.namedtuple(
        'NetflixShow', 'type title season episode watched')

    title = 'not defined'
    type = 'not defined'
    season = 'n/a'
    episode = 'n/a'

    if show.count(':') == 0:
        print('Film: %s' % show)
        type = 'Film'
    elif show.count(':') == 2:
        title, season, episode = show.split(':')
        print(f'SERIES: {title} - {season} - {episode}')
    elif show.count(':') == 1:
        print('Film series ?: %s' % show)
        title, episode = show.split(':')
    else:
        print('Investigate: %s' % show)
        title = show

    return NetflixShow(type, title, season, episode, watched)


if __name__ == "__main__":

    results = []
    print("Work in progress")

    full_data = r"C:\Users\braid\Downloads\RosieNetflixViewingHistory - Copy.csv"
    test_data = r"C:\Users\braid\Downloads\RosieNetflixViewingHistory.csv"
    rowie_data = r"RowieNetflixViewingHistory.csv"

    with open(rowie_data) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0

        for row in csv_reader:

            if line_count == 0:
                print(f'Columns names are {", ".join(row)}')
                line_count += 1
            else:
                show, day = row
                results.append(parse_show(show,day))

                line_count += 1

    print(f'processed {len(results)} items.')
    print(datetime.datetime.now())

    sys.exit(0)
