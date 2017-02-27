# -*- coding: utf-8 -*-
'''
college dict{
location:
student population:
specialization:
info:
}
'''
hunter = {'name':'Hunter College',
       'location':'Manhattan, NY',
       'location-type':'Urban',
       'pop':15566,
       'pop-type':'Large',
       'specialization':['Medicine','Humanities'],
       'info':''' Founded in 1870, Hunter is one of the oldest and most distinguished public colleges in the nation. It is the largest college in the CUNY system and the first choice of all students applying to CUNY.'''
}

city = {'name':'City College',
       'location':'Manhattan, NY',
       'location-type':'Manhattan, NY',
       'pop': 13113,
       'pop-type':'Medium',
       'specialization':['STEM','Business'],
       'info':
       "Since its founding in 1847, The City College of New York has emphasized two guiding principles: academic excellence combined with access to higher education."
}

brooklyn = {'name':'Brooklyn College',
            'location':'Brooklyn, NY',
            'location-type':'suburban',
            'pop':16463,
            'pop-type':'Medium',
            'specialization':['Law','Humanities'],
            'info':'''
            Brooklyn College is recognized for its academic excellence, innovative programs, urban engagement and outstanding alumni accomplishments.'''
            }

queens = {'name':'Queens College',
          'location':'Queens, NY',
          'location-type':'Suburban',
          'pop':14384,
          'pop-type':'Large',
          'specialization':['STEM','Medicine'],
          'info':''' 
          Queens College provides a first-rate, globally focused education to talented people from all ethnic, social, and economic backgrounds, and consistently receives high ratings in the most prestigious college guidebooks.'''
}

cuny = [hunter,city,brooklyn,queens]

bing = {'name':'Binghamton University',
     'location':'Binghamton, NY',
     'location-type':'Rural',
     'pop':13491,
     'pop-type':'Medium',
     'specialization':['STEM','Business'],
     'info':'''Fiske Guide recognizes Binghamton as a "premier public university in the northeast;" Kiplinger's Personal Finance and The Princeton Review call us a top value; U.S. News & World Report cites Binghamton as one of the "nation's top 50 public universities;" and Greenes' Guide named Binghamton a "public Ivy." 
     '''
}

buff = {'name':'University at Buffalo',
     'location':'Buffalo, NY',
     'location-type': 'Urban',
     'pop':10115,
     'pop-type':'Small',
     'specialization':['Medicine','Business'],
     'info':''' 
    At the University at Buffalo, the classroom is just the beginning. Extensive research and internship opportunities offer critical professional groundwork in disciplines from engineering to poetry.
     '''
}

alb = {'name':'University at Albany',
    'location':'Albany, NY',
    'location-type':'Urban',
    'pop':12908,
    'pop-type':'Small',
    'specialization':['Humanities','Law'],
    'info':''' 
     An Excellent Education. A Great Value. Named one of "America's Top Colleges" by Forbes, the University at Albany offers students the expansive opportunities of a comprehensive public research university with an environment designed to foster success.
    '''}

stony = {'name':'Stony Brook University',
      'location':'Stony Brook, NY',
      'location-type':'Rural',
      'pop':16831,
      'pop-type':'Large',
      'specialization':['Medicine','STEM'],
      'info':''' 
      At Stony Brook experiential learning is everywhere, from studying biodiversity in Madagascar and experiencing paleoanthropological discoveries in Kenya's Turkana Basin, to filing stories in real time from the fabled Silk Road in China.'''}
suny = [bing,buff,alb,stony]


def startgen(loc,pop,spec):
    #print 'Looking for %s, %s, %s' % (loc,pop,spec)
    collist = []
    for college in cuny:
        mat = []
        if college['location'] == loc:
            mat.append('Location')
        if college['pop-type'] == pop:
            mat.append('Population')
        for specialization in college['specialization']:
            if specialization == spec:
                mat.append('Specialization')
        if len(mat) != 0:
            newcol = college
            newcol['matched'] = mat
            collist.append(newcol)
    for college in suny:
        mat = []
        if college['location-type'] == loc:
            mat.append('Location')
        if college['pop-type'] == pop:
            mat.append('Population')
        for specialization in college['specialization']:
            if specialization == spec:
                mat.append('Specialization')
        if len(mat) != 0:
            newcol = college
            newcol['matched'] = mat
            collist.append(newcol)
    return collist

if __name__ == '__main__':
    print startgen('rural','large','Medical')
        
            
