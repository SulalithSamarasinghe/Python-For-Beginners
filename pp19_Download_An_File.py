from urllib import request
#
D_URL = 'https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2017-financial-year-provisional/Download-data/annual-enterprise-survey-2017-financial-year-provisional-csv.csv'
#
def download_File(D_URL):
    openURL = request.urlopen(D_URL)
    csv = str(openURL.read())
    lines = csv.split('\\n')
    fileName = r'test.csv'
    file = open(fileName,'w')
    #
    for line in lines:
        file.write(line+'\n')
    file.close()
#
download_File(D_URL)
