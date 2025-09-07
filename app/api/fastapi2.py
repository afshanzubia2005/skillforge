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
    # Get summaries for missing skills
    #skills_summary_dict = display_skills_summary(missing_skills)
        #Fix this --> Get information on each missing sill
        #Get the courses you need for each of those skills

    return {
        #"skills_summary": skills_summary_dict,
        "missing_skills": missing_skills, #list
        "percentage_missing": percentage_missing #list
    }