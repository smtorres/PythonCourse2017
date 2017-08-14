from bs4 import BeautifulSoup
import urllib2
import urllib
from itertools import compress
import random
from bs4 import BeautifulSoup
import os
import re
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#################################################################################
#link = 'http://www.newseum.org/todaysfrontpages/?tfp_display=archive-date&tfp_region=USA&tfp_sort_by=state&tfp_archive_id=081514&tfp_show=all'
#link2 = 'http://www.newseum.org/todaysfrontpages/?tfp_display=archive-date&tfp_region=USA&tfp_sort_by=state&tfp_archive_id=082614&tfp_show=all'
#link3 = 'http://www.newseum.org/todaysfrontpages/?tfp_display=archive-date&tfp_region=USA&tfp_sort_by=state&tfp_archive_id=112514&tfp_show=all'
link4 = 'http://www.newseum.org/todaysfrontpages/?tfp_display=gallery&tfp_region=USA&tfp_sort_by=state&tfp_show=all'
#direc = '/Users/michelletorres/Dropbox/VisualCommunication/ScrapeImages/scrape_covers/Ferguson1/'
#direc2 = '/Users/michelletorres/Dropbox/VisualCommunication/ScrapeImages/scrape_covers/Ferguson2/'
#direc3 = '/Users/michelletorres/Dropbox/VisualCommunication/ScrapeImages/scrape_covers/Ferguson3/'
#direc4 = '/Volumes/MyPassport/Covers/scrape_covers/Charlottesville_0812/'
direc5 = '/Volumes/MyPassport/Covers/scrape_covers/Charlottesville_0813/'
# The great main function
def getCover(link, direc, date2, doimg=True, dopdf=False):
    # Process source code
    cover_link = urllib2.urlopen(link)
    cover_soup = BeautifulSoup(cover_link.read(), "html.parser")
    cover_soup.prettify()
    # Extract pubs
    pubs_names = cover_soup.findAll('h4', attrs={'class':'thumbnail-group-title'})
    pubs_names = [x.text for x in pubs_names]
    pubs_names = [x.replace('\n','') for x in pubs_names]
    pubs_names = [x.replace('\t','') for x in pubs_names]
#    print pubs_names
    # Extract places
    pubs_places = cover_soup.findAll('div', attrs={'class':'thumbnail-group-body'})
    pubs_places = [x.text for x in pubs_places]
    pubs_places = [x.replace('\n','') for x in pubs_places]
    pubs_places = [x.replace('\t','') for x in pubs_places]
    # Date
    date_ls = [date2 for i in range(len(pubs_places))]
#    print pubs_places
    minis = [x[0:5] for x in pubs_places]
    index = range(len(pubs_names))
    # Extract links of pdfs
    img_link_ls = cover_soup.findAll('img', attrs={'class': 'colorbox-1230'})
    img_link_ls = [x['src']for x in img_link_ls]
    img_link_ls = [x.replace( "med", "lg" ) for x in img_link_ls]
    if 'wp-content' in img_link_ls[0]:
        img_link_ls.pop(0)
    img_name = [direc+minis[x]+'_'+str(x)+'.jpg' for x in index]
    img_name = [x.replace(' ', '') for x in img_name]
    #print img_link_ls
    if doimg:
        for img in index:
            r = urllib2.Request(img_link_ls[img])
            imgData = urllib2.urlopen(r).read()
            output = open(img_name[img], 'w+')
            output.write(imgData)
            output.close()
    # Download PDFs
    pdf_link_ls = [x.replace("jpg13/lg", "pdf13") for x in img_link_ls]
    pdf_link_ls = [x.replace(".jpg", ".pdf") for x in pdf_link_ls]
    pdf_name = [direc+minis[x]+'_'+str(x)+'.pdf' for x in index]
    pdf_name = [x.replace(' ', '') for x in pdf_name]
    if dopdf:
        for doc in index:
            r2 = urllib2.urlopen(pdf_link_ls[doc])
            output2 = open(pdf_name[doc], 'w')
            output2.write(r2.read())
            output2.close()
    print pdf_name
    info = {'id':index, 'public':pubs_names,'place':pubs_places, 'files':img_name,
    'date':date_ls}
    return info


#check1 = getCover(link, direc, False)
#check2 = getCover(link2, direc2, True)
#check3 = getCover(link3, direc3, False)
check4 = getCover(link4, direc5, date2='081317', doimg=False, dopdf=True)

print(check4.keys())
print([check4[i][0] for i in check4.keys()])

data_file = '/Volumes/MyPassport/Covers/scrape_covers/covers_info_charlotte.csv'
#with open(data_file, 'ab') as f:
 #   my_writer = csv.DictWriter(f, fieldnames=("id", "public", "place","date", "files"))
    #my_writer.writeheader()
    #for i in range(len(check1.values()[0])):
    #    temp = [item[i] for item in check1.values()]
    #    temp_id = 'F1_'+str(temp[2])
    #    my_writer.writerow({'files':temp[0], 'place':temp[1], 'id':temp_id, 'public':temp[3]})
    #for j in range(len(check2.values()[0])):
    #    temp2 = [item[j] for item in check2.values()]
    #    temp_id2 = 'F2_'+str(temp2[2])
    #    my_writer.writerow({'files':temp2[0], 'place':temp2[1], 'id':temp_id2, 'public':temp2[3]})
    #for k in range(len(check3.values()[0])):
    #    temp3 = [item[k] for item in check3.values()]
    #    temp_id3 = 'F3_'+str(temp3[2])
    #    my_writer.writerow({'files':temp3[0], 'place':temp3[1], 'id':temp_id3, 'public':temp3[3]})
    #for m in range(2):
    for m in range(len(check4.values()[0])):
        temp4 = [item[m] for item in check4.values()]
        temp_id4 = 'F5_'+str(temp4[3])
        print temp4
        my_writer.writerow({'files':temp4[0], 'place':temp4[2], 'id':temp_id4, 'public':temp4[4], 'date':temp4[1]})





