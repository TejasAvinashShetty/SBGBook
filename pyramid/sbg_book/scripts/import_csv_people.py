import os
import sys
import transaction
import csv

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models.meta import Base
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
    )
from ..models import Person


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 3:
        usage(argv)
    config_uri = argv[1]
    fname = argv[2]
    options = parse_vars(argv[3:])

    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    engine = get_engine(settings)
    Base.metadata.create_all(engine)

    session_factory = get_session_factory(engine)

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)

        #model = Person(firstName='Joe', lastName='Smith')
        #dbsession.add(model)
        with open(fname) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)
                if 1:
                    p=Person()
                    p.firstName=row['firstName']
                    p.lastName=row['lastName']
                    p.studentID=row['studentID']
                    p.email=row['email']
                    dbsession.add(p)

if 0:
        dbsession = get_tm_session(session_factory, transaction.manager)
        with open(fname) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                p = Person()
                if 1:
                    p.firstName=row['firstName']
                    p.lastName=row['lastName']
                    p.studentID=row['studentID']
                    p.email=row['email']
                dbsession.add(Person)


if 0:
            
    import os
    import sys
    import transaction

    from pyramid.paster import (
        get_appsettings,
        setup_logging,
        )

    from pyramid.scripts.common import parse_vars

    from ..models.meta import Base
    from ..models import (
        get_engine,
        get_session_factory,
        get_tm_session,
        )
    from ..models import Person

    import csv

    def usage(argv):
        cmd = os.path.basename(argv[0])
        print('usage: %s <config_uri> filename [var=value]\n'
              'filename is the path to the csv file. var=value\n'
              'allows you to override options in the ini file from the command line\n'
              '(example: "%s development.ini people.csv")' % (cmd, cmd))
        sys.exit(1)

    def main(argv=sys.argv):
        if len(argv) < 3:
            usage(argv)
        config_uri = argv[1]
        fname = argv[2]
        options = parse_vars(argv[3:])
        setup_logging(config_uri)
        settings = get_appsettings(config_uri, options=options)
        engine = get_engine(settings)
        Base.metadata.create_all(engine)
        session_factory = get_session_factory(engine)

        with transaction.manager:
            dbsession = get_tm_session(session_factory, transaction.manager)
            with open(fname) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    p = Person()
                    p.firstName=row['firstName']
                    p.lastName=row['lastName']
                    p.studentID=row['studentID']
                    p.email=row['email']
                    dbsession.add(Person)
