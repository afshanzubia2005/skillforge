import requests
import os
import pdfplumber
import redis

def parse_pdf(filepath):
	url = "https://api.affinda.com/v1/resumes/"
	api_key = os.getenv('AFFINDA_API_KEY')
	print(f"API_KEY: {api_key}")
	with open(filepath, 'rb') as f:
		files = {'file': f}
		headers = {
		"Authorization": f"Bearer {api_key}",
		"accept": "application/json"
	}
		data = {
			"workspace": "abc"

		}
		response = requests.post(url, files=files, headers=headers)
	print("Posted the resume")
	if response.status_code != 200:
		print("Error parsing PDF: ", response.json())
		return None
	# print(response.json())
	return response.json()
# how is this different from the code that is in the Affinda documentation?
 
def fetch_topic_summary(topic):
	url = f"https://api.duckduckgo.com/?q={topic}&format=json&no_redirect=1&no_html=1"
	response = requests.get(url)
	if response.status_code == 200:
		data = response.json()
		#print(response.headers)
		#print(response.text)
	else:
		print(response.text)
		

	if 'Abstract' in data and data['Abstract']:
		return data['Abstract']
	else:
		return "No summary found."
	

def find_missing_skills(wordlist, pdf_path):
	'''Finds all the missing skills in the wordList that are not present in the resume 
	provided in the path (pdfpath)'''

	r = redis.Redis(host = 'localhost', port = 6379, db = 0) #First database is being used
	#If Unable to get a cache hit with pdf_path, then open the pdf_path 
	# with pdf_plumber, retrieve resume content by page and
	# add the resume contents to cache 
	if r.get(f"{pdf_path}"):
		resume_text = r.get(f"{pdf_path}").decode("utf-8")
		print("Cache hit! Missing skills found in Redis.")
	else:
		print("Cache miss! Fetching resume text from PDF.")
		resume_text = ""
		pdf = pdfplumber.open(pdf_path)
		for page in pdf.pages:
			resume_text += page.extract_text_simple()
		r.set(f"{pdf_path}", resume_text) #Upload all the resume text info to Redis w/ key as pdf_path
	
		
	missing_skills = []

	if missing_skills is None:
		missing_skills = []

	for word in wordlist:
		found = False
		if word.lower() in resume_text.lower():
			found = True
		if not found:
			missing_skills.append(word)

	return missing_skills

def upload_pdf_to_public_folder(pdf_path):
	# Implement the logic to upload the PDF to the public folder
    
	return pdf_path

def extract_skill_list_from_job_description(job_description):
	# Implement
    # A simple extraction logic (this can be improved with NLP techniques)
	pass
