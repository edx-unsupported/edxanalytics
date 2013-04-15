import logging
from django.conf import settings
from mitxmako.shortcuts import render_to_response, render_to_string
from djanalytics.core.decorators import view, query, event_handler

log=logging.getLogger(__name__)

#from djanalytics.models import StudentBookAccesses

@view(name = 'page_count')
def event_count_view(fs, db, user, params):
    ''' Dummy test function. In the future, this should return some stats on 
    how many textbook pages the user saw '''
    return "The user " + user + " saw "+str(event_count_query(fs, db, user, params))+" pages!"

@query('user', 'page_count')
def event_count_query(fs, db, user, params):
    ''' Dummy test function. In the future, this should return some stats on 
    how many textbook pages the user saw '''
    if settings.DUMMY_MODE:
        return sum(map(ord, user))

    collection = db['page_count']
    sba = list(collection.find({'user':user}))
    if len(sba) == 0:
        return 0
    else:
        return sba[0]['pages']
    # sba = StudentBookAccesses.objects.filter(username = user)
    # if len(sba):
    #     pages = sba[0].count
    # else: 
    #     pages = 0
    #return pages

@view(name = 'page_count')
def event_count_view_course(fs, db, user, course, params):
    ''' Dummy test function. In the future, this should return some stats on
    how many textbook pages the user saw '''
    return "The user " + user + " saw "+str(event_count_query_course(fs, db, user, course, params))+" pages!"

@query(name='page_count')
def event_count_query_course(fs, db, user, course, params):
    ''' Dummy test function. In the future, this should return some stats on
    how many textbook pages the user saw '''
    collection = db['page_count']
    sba = list(collection.find({'user':user}))
    if len(sba) == 0:
        return 0
    else:
        return sba[0]['pages']
        # sba = StudentBookAccesses.objects.filter(username = user)
    # if len(sba):
    #     pages = sba[0].count
    # else:
    #     pages = 0
    return pages


@event_handler()
def event_count_event(fs, db, events):
    for event in events:
        #NOTE: IF this is uncommented, mongo has INSANE cpu usage.  Do not uncomment without fixing indexes on Mongo
        #TODO: resolve issue above
        """
        collection = db['page_count']
        user = event["username"]
        sba = list(collection.find({'user':user}))
        if len(sba):
            collection.update({'user':user}, {'$inc':{'pages':1}}, True);
        else:
            collection.insert({'user':user,'pages':1})
        """
        pass

