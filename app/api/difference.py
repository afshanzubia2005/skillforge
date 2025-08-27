class Differences:
    def __init__(self):
        self.current_skills = []
        self.required_skills = []
        self.missing_skills = []
        self.percentage_of_skills_known = 0
        self.all_Skills = ["Python", "JavaScript", "Java", "C++", "C", "Ruby", "Go", "Swift", "PHP", "Django"
                       , "Flask", "Ruby on Rails", "Ruby", "Angular", "React", "Vue.js", "ASP.NET", "SQL", "NoSQL", "MongoDB",
                       "MySQL", "PostgreSQL", "OracleDB", "Firebase", "Docker", "Kubernetes", "Jenkins", "Git", "Terraform",
                       "Ansible", "CI/CD Pipelines", "AWS", "Google Cloud Platform", "Amazon Web Services", "Microsoft Azure", "Azure",
                       "IBM Cloud", "Git", "GitHub", "GitLab", "Bitbucket", "Restful APIs", "GraphQL", "gRPC", "TensorFlow", "PyTorch",
                       "Pandas", "NumPy", "Scikit-Learn", "R", "Testing Tools", "Selenium", "JUnit", "Postman", "Mocha", "Chai",
                       "JIRA", "Trello", "Asana", "Monday.com", "Microsoft Project", "Project Management Methodologies", "Agile", 
                       "Scrum", "Kanban", "Waterfall", "Linux", "Windows", "macOS", "TCP", "IP", "VPN", "Firewalls", "SSL/TLS",
                       "Adobe XD", "Figma", "Sketch", "InVision", "Docker", "Kubernetes", "Agile Methodologies" ]

    def get_difference_in_skills(self, result, job_description):
        print(f"Job Description: {job_description.lower()}")
        self.current_skills = []

        '''Get a list of required skills from job_description and the set of all skills'''
        self.required_skills = [skill.lower() for skill in self.all_Skills if skill.lower() in [job_description.lower()]]

        print(self.required_skills)

        '''Retrieve all current skills from result and store in current_skills'''
        skills = result['data']['skills']
        for skill in skills:
            self.current_skills.append(skill['name'].lower())

        '''Find all skills that are missing from the required skillset '''
        self.missing_skills = [skill for skill in self.required_skills if skill.lower() not in self.current_skills]


        if self.required_skills:
            self.percentage_of_skills_known = (len(self.current_skills) / len(self.required_skills)) * 100
        else:
            self.percentage_of_skills_known = 0

        return {
            "percentage_known": self.percentage_of_skills_known,
            "missing_skills": self.missing_skills
    
        }



            