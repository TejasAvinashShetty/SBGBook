"""
Cornice Services for REST API
"""

import json
import traceback

import sqlalchemy as sa

from pyramid.response import Response

from .models import (
    Person,
)

from cornice import Service

person = Service(name='person', path='/restapi/persons/{id}', description="Person Service")
people = Service(name='people', path='/restapi/persons', description="People Service")

@person.get()
def get_person_info(request):
    """Get info for a person object"""
    pid = request.matchdict.get('id','')
    p=request.dbsession.query(Person).filter(Person.id==pid).first()
    return {'id':p.id, 'lastName':p.lastName, 'firstName':p.firstName, 'studentID':p.studentID, 'email':p.email}

@people.get()
def get_people_info(request):
    """Get a collection of person objects"""

    result = request.dbsession.query(Person).order_by(Person.lastName.asc(),Person.firstName.asc()).all()

    results=[]
    for p in result:
      results.append({'id':p.id, 'lastName':p.lastName, 'firstName':p.firstName, 'studentID':p.studentID, 'email':p.email})

    return results
