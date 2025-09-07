#Takes the skills from differnece.py and then prints out a summary
#First make a dictionary 

from pdfparser import fetch_topic_summary
from openai import OpenAI

client = OpenAI()

def display_skills_summary(dict):
    #dict is the list that is returned by get_difference_in_skills method from Differences class (differnece.py)
    final_dict = {}
    for skill in dict:
        final_dict[skill] = fetch_topic_summary(skill)

    return final_dict

def display_courses_for_skills(skill_list):   #Uses OpenAI
    text_response = ""
    for skill in skill_list:
        response = client.responses.create(
            model="gpt-3.5-turbo",
            input=f"List some online courses to learn {skill} as a concise list. Provide the course name and the platform where it is available.",

        )
        text_response += f"Courses for {skill}:\n{response['content']['text']}\n"
    return text_response

skill_list = ["Python", "Docker", "Kubernetes"]
display_courses_for_skills(skill_list)