<p align="center">
  <img src="public\images\logo.svg" alt="Skill Forge" width="330" height="300"/>
</p>


# SkillForge
SkillForge is a web application designed to bridge the gap between education and workforce readiness. It empowers job seekers by providing tools to analyze resumes, identify skill gaps, and access resources for professional development. 

## Inspiration

The idea for SkillForge evolved from an initial concept of a meal prep app that utilized an API to scan food barcodes, allowing users to input ingredients and generate recipes. However, due to the unavailability of a free database for food barcodes, the idea was shelved. During a sponsor's presentation on "bridging a gap between education and workforce for everyone," we pivoted to create SkillForge. Our mission is to guide high school graduates, college students, and those re-entering the job market toward free or low-cost solutions to enhance their employability.

## What It Does

SkillForge allows users to:
- Search and compare job postings and their associated skill requirements.
- Upload their resume and compare it against a pasted job description.
- Identify the match percentage between the resume and job description.
- Highlight missing skills and provide links to free or affordable online certifications or courses from platforms like Coursera and MIT.
  
SkillForge aims to simplify the job-hunting process by giving instant feedback on resume alignment with specific job requirements, helping users identify gaps and target their improvements.

## Key Features

- **Resume Parsing**: Utilizing an advanced PDF Parser library, SkillForge processes resumes in PDF, DOC, or DOCX formats, extracting relevant keywords and skills.
- **Job Description Matching**: Users can paste job descriptions, which are compared with parsed resumes to identify matching and missing skills.
- **Data Storage**: MongoDB is used for efficient data management, securely storing resume information and skills summaries.
- **Authentication**: SkillForge integrates Auth0 for secure authentication and authorization.
- **User Interface**: A dynamic and responsive frontend built with Next.js offers a smooth and intuitive user experience.
- **Backend**: Powered by FastAPI and Python, ensuring fast, reliable API responses and seamless integration between the frontend and the database.

## How We Built It

- **Frontend**: Next.js
- **Backend**: Python (FastAPI)
- **Database**: MongoDB
- **Resume Parsing**: PDF Parser library
- **Authentication**: Auth0

## Challenges We Ran Into

- Implementing PDF parsing to accurately extract resume content from various formats.
- Integrating Auth0 for secure user authentication.
- Ensuring seamless communication between the Next.js frontend and the FastAPI backend while maintaining fast response times.

## Future Vision

We plan to expand SkillForge by integrating machine learning algorithms that suggest resume improvements based on parsed data. Additionally, we aim to provide real-time job recommendations based on user inputs.

## Accomplishments We're Proud Of

- Successfully integrated Auth0 for secure user authentication.
- Developed a cohesive branding strategy, including creating a logo that fits the disco theme.
- Constructed a functional resume parser and hosted the website.

## What We Learned

- Database creation and management.
- API development and integration.
- Web domain setup and design formatting.
- Collaboration using GitHub and effective team division.
- Using Docker for containerization

## What's Next for SkillForge

SkillForge's functionality is built around three main pillars, with the resume comparison feature being the focus for this demonstration. It will serve as a valuable tool for recent graduates who are unsure of their career paths. 

The app will also provide:
- A database of jobs, including salary expectations and required qualifications.
- Links to affordable or free certification courses for necessary skills.
- Future enhancements leveraging machine learning to suggest skills based on user experience, helping candidates tailor their resumes effectively.

For example, if a pharmacy technician applies to Merck’s drug research and development team, SkillForge may prompt them to add "pill compounding" as a skill based on shared learning experiences from others in similar roles.

# How to Run Backend (w/o Docker)
Create virtual environment
! python3 -m venv venv
! source venv/bin/activate

Install dependencies (found in api folder)
! pip install -r requirements.txt


# How to Run Backend (api folder) WITH DOCKER:
## Consult README.Docker.md within the api folder for instructions !!

# Frontend Instruction
Install frontend dependencies (npm install) 
Run in development mode (npm run dev)
