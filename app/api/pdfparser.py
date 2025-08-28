import requests
import os
import pdfplumber

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
	'''Finds all the missing skills in the wordList that are not present in the resume (pdfpath)'''
	pdf = pdfplumber.open(pdf_path)
	missing_skills = []

	for word in wordlist:
		found = False
		for page in pdf.pages:
			text = page.extract_text_simple()
			if word.lower() in text.lower():
				found = True
				break

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
