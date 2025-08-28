from fastapi import FastAPI, UploadFile, File
from pdfparser import parse_pdf
#from webscrapper import display_skills_summary
from database import DBConnection
from difference import Differences
import os

#db1 = DBConnection()
app = FastAPI()
os.makedirs('uploads', exist_ok=True)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Skill Forge API"}



@app.post("/api/parse-document")
async def get_skills(job_description: str, file: UploadFile = File(...)):

    #Fix: Extract skills direcly from job description using NLP technique instead of correlating with allSkills

    ''' Abandoned section (Debug later). 
    try:
        # Send the file to affinda for parsing (pdfparser)
        # Return value: String of skills / keywords extracted from pdf
        result = parse_pdf(file_location) 
    except Exception as e:
        print(e)
        return {"error": "Sorry, we could not parse your file"}

    # Save the results into the database
    #db1.insert_a_user(result)
    
    
     # Save the uploaded file
    file_location = f"uploads/{file.filename}"
    print(file_location)
    with open(file_location, "wb") as f:
        f.write(await file.read())
    '''

    # Make a call to the difference.py method
    dif = Differences()
    skill_dict = dif.get_difference_in_skills(job_description, file) #Fix
    

    missing_skills = skill_dict['missing_skills']
    percentage_missing = skill_dict['percentage_missing']

    # Get summaries for missing skills
    #skills_summary_dict = display_skills_summary(missing_skills)
        #Fix this --> Get information on each missing sill
        #Get the courses you need for each of those skills

    return {
        #"skills_summary": skills_summary_dict,
        "missing_skills": missing_skills, #list
        "percentage_missing": percentage_missing #list
    }