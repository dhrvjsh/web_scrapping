from bs4 import BeautifulSoup
import urllib.request as ur

#loop through the 7 pages of undergraduate courses
for i in range (0,6):

    #read and open url to scrape
    urlToScrape = "https://www.city.ac.uk/courses?level=Undergraduate&p=" + str(i * 10 + 1)
    r = ur.urlopen(urlToScrape).read()
    soup = BeautifulSoup(r, "lxml")

    #attributes for each course
    courseList = soup.find_all('div', attrs={'class': 'course-finder__results__item course-finder__results__item--undergraduate'})

    #loop through each course
    for courseListItem in courseList:

        #get course name
        try:
            courseNameElement = courseListItem.find('div', attrs={'class': "col-sm-24 col-md-18 col-lg-20"})
            courseName = courseNameElement.find('a').text
        except Exception as e:
            courseName = ''

        #get degree name
        try:
            degreeTypeElement = courseListItem.find('div', attrs={'class': "course-finder__results__item__award"})
            degreeName = degreeTypeElement.text
        except Exception as e:
            degreeName = ''

        #get school the course is part of
        try:
            courseSchoolElement = courseListItem.find('div', attrs={'class': "course-finder__results__item__md course-finder__results__item__md--school"})
            courseSchool = courseSchoolElement.find('a').text
        except Exception as e:
            courseSchool = ''

        #get course duration
        try:
            courseDurationElement = courseListItem.find('div', attrs={'class': "course-finder__results__item__md course-finder__results__item__md--duration"})
            courseDuration = courseDurationElement.find_all('span')[2].text
        except Exception as e:
            courseDuration = ''

        #get course code
        try:
            courseCodeElement = courseListItem.find('div', attrs={'class': "course-finder__results__item__md course-finder__results__item__md--code"})
            courseCode = courseCodeElement.find_all('span')[2].text
        except Exception as e:
            courseCode = ''

        print(courseName)
        print(degreeName)
        print(courseSchool)
        print(courseDuration)
        print(courseCode)
        print ("-------------\n")
