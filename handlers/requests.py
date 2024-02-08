import httpx

httpx_client: object = httpx.Client()
base_url: str = "https://app.ytjobs.co/api/"

def fetch_jobs(authentication: str, page_number: int) -> any:
    headers = {
        "Authorization": authentication,
    }
    
    response: object = httpx_client.get(url=base_url+"jobs?limit=15&search=&filter=%7B%22locationType%22:%22remote%22%7D&page="+str(page_number), headers=headers)
    
    return response.json()["data"]
    
def apply_for_job(authentication: str, text: str, job_id: any) -> any:
    headers = {
        "Authorization": authentication,
    }
    
    payload = {
        "coverLetter": text,
        "location": "49441"
    }
    
    response: object = httpx_client.post(url=base_url+"jobs/"+str(job_id)+"/apply", headers=headers, data=payload)
    
    return response.json()