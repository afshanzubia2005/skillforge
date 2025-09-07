# Unit testing

# First method-- Test with my resume.

from difference import Differences


def test_extract_skills():
    job_description = "This job requires a good understanding of Python, Kubernetes, Docker, and Flutter.  \
                    Experience with AWS and Azure is a plus. Familiarity with JavaScript frameworks like React and CSS is also beneficial."

    diff = Differences()
    missing_skills = diff.extract_skill_list_from_job_description(job_description)
    expected_skills = ["Python", "Docker", "Kubernetes", "Flutter", "AWS", "Azure", "JavaScript", "React", "CSS"]

    for skill in missing_skills:
        if skill not in expected_skills:
            assert False
    assert True
