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
    print("Test 1 passed!")
else:
    print("Test 1 failed.")

