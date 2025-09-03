'''
This is a custom webscrapper that uses BeautifulSoup to scrape Coursera's website listings for courses
match the search keyword
'''

# Start time--> 4:20 AM
# Goal: Finish by 6am with at least 1 test passed.

from bs4 import BeautifulSoup
import requests
import regex as re 

def scrape_coursera_courses(search_keyword):
    
    # response = requests.get(f"https://www.coursera.org/learn?query=introduction-to-{search_keyword}?")
    response = requests.get(f"https://ocw.mit.edu/search/?q=intro%20to%20{search_keyword}")
    soup = BeautifulSoup(response.content, 'html.parser')
    #print(soup.find_all(attrs={"article", "OpenCourseWare Search Results", "role": "feed"}))
    look_for = re.compile(r"\/courses\/.")
    for i in (soup.find_all('a', href=look_for)):
        print(i['href'])


scrape_coursera_courses("java")









'''

    response = requests.get("https://www.coursera.org/courses?query=" + search_keyword)
    soup = BeautifulSoup(response.text, 'html.parser')
    course_list = []
    for course in soup.find_all('div', class_='course-card'):
        title = course.find('h2', class_='course-title').text
        link = course.find('a', class_='course-link')['href']
        course_list.append({'title': title, 'link': link})
    return course_list'''