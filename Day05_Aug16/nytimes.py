# source dlab Berkeley: http://dlab.berkeley.edu/blog/scraping-new-york-times-articles-python-tutorial
from nytimesarticle import articleAPI
api = articleAPI('your key')

articles = api.search( q = 'Charlottesville', 
     fq = {'headline':'Trump', 'source':['Reuters','AP', 'The New York Times']}, 
     begin_date = 20170810 )

articles
mynews = articles['response']['docs']
mynews[0]
mynews[0]['_id']

def parse_articles(articles):
    '''
    This function takes in a response to the NYT api and parses
    the articles into a list of dictionaries
    '''
    news = []
    for i in articles['response']['docs']:
        dic = {}
        dic['id'] = i['_id']
        try:
        	i['abstract']
        except:
        	dic['abstract'] = ''
        else:
            dic['abstract'] = i['abstract'].encode("utf8")
        dic['headline'] = i['headline']['main'].encode("utf8")
        try:
        	i['news_desk']
        except:
        	dic['desk'] = ""
        else:
        	dic['desk'] = i['news_desk']
        dic['date'] = i['pub_date'][0:10] # cutting time of day.
        try:
        	i['section_name']
        except:
        	dic['section'] = ""
        else: 
        	dic['section'] = i['section_name']
        if i['snippet'] is not None:
            dic['snippet'] = i['snippet'].encode("utf8")
        dic['source'] = i['source']
        dic['type'] = i['type_of_material']
        dic['url'] = i['web_url']
        dic['word_count'] = i['word_count']
        # locations
        locations = []
        for x in range(0,len(i['keywords'])):
            if 'glocations' in i['keywords'][x]['name']:
                locations.append(i['keywords'][x]['value'])
        dic['locations'] = locations
        # subject
        subjects = []
        for x in range(0,len(i['keywords'])):
            if 'subject' in i['keywords'][x]['name']:
                subjects.append(i['keywords'][x]['value'])
        dic['subjects'] = subjects   
        news.append(dic)
    return(news)

test = parse_articles(articles) #Ready to put it in a csv file!!

