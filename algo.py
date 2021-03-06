"""

TODO
    - Write Tests
    - Actually Test
    - Find way to combine get___References
    - Write into Class?
    - Change findMax to findTop3
"""

from models import Keyword, Job, Degree, JobKeywords, DegreeKeywords

def recomend(keywords, target):
    key_ids = []
    for k in keywords:
        key_obj = Keyword.query.filter_by(key=str(k)).first() #could be optimized by having the ID's sent back instead of the actual keyword
        key_ids.append(key_obj.id)
    if target == "job":
        store = getJobReferences(key_ids)
    elif target == "degree":
        store = getDegreeReferences(key_ids)
    id = maxfind(store)
    if target == "job":
        job = Job.query.get(id)
        return job.title
    elif target == "degree":
        degree = Degree.query.get(id)
        return degree.title


def getJobReferences(keywordIDs):
    store = {}
    for k_id in keywordIDs:
        jobIDs_by_keyword = [q.jobID for q in JobKeywords.query.filter_by(keywordID=k_id)]
        for job_id in jobIDs_by_keyword:
            if job_id not in store.keys():
                store[job_id] = 1
            else:
                store[job_id]+=1
    return store

def getDegreeReferences(keywordIDs):
    store = {}
    for k_id in keywordIDs:
        degreeIDs_by_keyword = [q.degreeID for q in DegreeKeywords.query.filter_by(keywordID=k_id)]
        for degree_id in degreeIDs_by_keyword:
            if degree_id not in store.keys():
                store[degree_id] = 1
            else:
                store[degree_id]+=1
    return store


def maxfind(store):
    """
    Returns key and max val from hashmap
    """
    topkey = 0
    topval = None
    for k,v in store.iteritems():
        if v > topval:
            topval = v
            topkey = k
    return topkey
