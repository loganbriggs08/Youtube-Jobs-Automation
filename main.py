import time

from handlers import requests

class YoutubeJobsAutomation:
    def __init__(self, authentication: str, apply_text: str, delay: int):
        self.authentication = authentication
        self.apply_text = apply_text
        self.delay = delay
        
    def start(self) -> bool:
        
        while True:
            for i in range(15):
                page_jobs = requests.fetch_jobs(self.authentication, i+1)
                
                for job in page_jobs:
                    job_id = job["id"]
                    
                    response = requests.apply_for_job(self.authentication, self.apply_text, job_id)
                    
                    if response["success"] == True:
                        print("[SUCCESS] Applied for " + job_id + " successfully.")
                        time.sleep(self.delay)
                    else:
                        print("[UNSUCCESSFUL] Failed to apply for " + job_id + ".")
                        time.sleep(self.delay * 2)
        
if __name__ == "__main__":
    YoutubeJobsInstance = YoutubeJobsAutomation(
        authentication="Bearer abc", 
        apply_text="Hello poopoo.",
        delay=0.5
    )
    
    YoutubeJobsInstance.start()