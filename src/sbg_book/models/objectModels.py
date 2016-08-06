from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    String,
    Binary,
    Date,
    DateTime,
    ForeignKey,
    Sequence,
    LargeBinary,
    )
    
from sqlalchemy.orm import (
    relationship,
    backref,
    )
    
from datetime import datetime

from .meta import Base

class Person(Base):
    __tablename__ = 'people'
    __table_args__ = (
        Index('person_ix_lastname','lastName'),
        Index('person_ix_firstname', 'firstName'),
        Index('person_ix_email', 'email'),
        Index('person_ix_studentid', 'studentID'),
    )
    id = Column(Integer, Sequence('person_seq_id'), primary_key=True)
    firstName = Column(Text)
    lastName = Column(Text)
    studentID = Column(Text)
    email = Column(Text)

class Class(Base):
    __tablename__ = 'classes'
    id = Column(Integer, Sequence('class_seq_id'), primary_key=True)
    name = Column(Text)
    startDate = Column(Date)
    endDate = Column(Date)

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, Sequence('role_id'), primary_key=True)
    name = Column(String(20))
    
class Section(Base):
    __tablename__ = 'sections'
    id = Column(Integer, Sequence('section_id'), primary_key=True)
    name = Column(String(20))
    classID = Column(Integer, ForeignKey('classes.id'))

class PersonSection(Base):
    __tablename__ = 'personsections'
    personID = Column(Integer, ForeignKey('people.id'), primary_key=True)
    sectionID = Column(Integer, ForeignKey('sections.id'), primary_key=True)
    roleID = Column(Integer, ForeignKey('roles.id'), primary_key=True)
    role = relationship("Role")
    timestamp = Column(DateTime, default=datetime.now)
    state = Column(Text, default='')                        

if 0:
    class Region(Base):
        __tablename__ = 'regions'
        __table_args__ = (  Index('region_ix_path','regionPath'),
                            Index('region_ix_parent', 'parentRegionID'),
                            Index('region_ix_context', 'contextID'),
                            Index('region_ix_rtype','regionTypeID'),
                            Index('region_ix_exppath','regionPathExpanded'),
                            Index('region_ix_expcid','contextIDExpanded'),
                         )
        id = Column(Integer, Sequence('region_seq_id'), primary_key=True)
        contextID = Column(Text)
        regionTypeID = Column(Integer, ForeignKey('regiontypes.id'))
        regionType = relationship("RegionType", foreign_keys=[regionTypeID])

        parentRegionID = Column(Integer, ForeignKey(id), default=None)

        children = relationship("Region", 
                                backref=backref('parent', remote_side=id),
                                collection_class = attribute_mapped_collection('contextID'),
                                cascade="all, delete-orphan",
                                foreign_keys=[parentRegionID])

        intermentSpace = relationship("IntermentSpace", uselist=False, backref="region")

        regionPath = Column(Text)
        regionPathExpanded = Column(Text)   # expanded path for sorting/indexing
        contextIDExpanded = Column(Text)    # expanded contextID for sorting/indexing
        intermentSpaceStatusLine = Column(Text)
        name = Column(Text)

        def __repr__(self):
            return '<Region Object: regionPath=%s, name=%s>' % (self.regionPath, self.name)

