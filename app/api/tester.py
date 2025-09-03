'''curl -X POST "https://api.affinda.com/v1/resumes/" -H "Authorization: Bearer aff_0baef0fd92c5d59611e0910ab2cb018d6d142077" -F "file=@/Users/afshanzubia/important_documents/resume.pdf"



"https://api.duckduckgo.com/?q={python}&format=json&no_redirect=1&no_html=1"

curl -X POST "http://localhost:8000/api/parse-document" -F "file=@/Users/afshanzubia/important_documents/resumefinal.pdf" -F job_description='Kubernetes'
'''
from pdfparser import find_missing_skills

"""Test 1: the ability to search for a skill existing within resume"""

def test_find_missing_skills():
    resume_path = "../../public/files/ankush.pdf"
    skills_to_search = ["Python", "Docker", "Flutter", "Dart"]

    result = find_missing_skills(skills_to_search, resume_path) 
    if result == ["Flutter", "Dart"] or result == ["Dart", "Flutter"]:
        return True
    return False

if (test_find_missing_skills()):
    print("Test 1: finding_missing_skills() passed!")
else:
    print("Test 1: finding_missing_skills() failed.")

