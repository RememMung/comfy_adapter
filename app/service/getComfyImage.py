import requests
import json
from flask import current_app
from app.logger import get_logger
import traceback
import os

logger = get_logger()

def run_workflow(workflow_id, api_id, prompt):
    url = f"https://comfy.icu/api/v1/workflows/{workflow_id}/runs"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {api_id}"
    }
    payload = {
        "prompt": prompt
    }
    response = requests.post(url, headers=headers, json=payload).json()
    return response['id']
    

def check_run_status(workflow_id, api_id, run_id):
    url = f"https://comfy.icu/api/v1/workflows/{workflow_id}/runs/{run_id}"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {api_id}"
    }

    response = requests.get(url, headers=headers)
    return response.json()

def get_workflow(workflow_file):
    with open(f"{workflow_file}", "r", encoding="utf-8") as f:
        workflow_data = f.read()
    workflow = json.loads(workflow_data)
    return workflow

def get_image(workflow_id, run_id):
    image_uri = f'https://r2.comfy.icu/workflows/{workflow_id}/output/{run_id}/ComfyUI_00001_.png'
    os.system("curl " + image_uri + " > test.jpg")


def run():
    workflow_id = current_app.config['WORKFLOW_ID']
    api_id = current_app.config['API_ID']
    workflow_file = current_app.config['WORKFLOW_FILE']
    image_dir = current_app.config['IMAGE_DIR']
    
    try:
        # get Prompt from JSON file
        prompt = get_workflow()

        # run ComfyUI Workflow by REST request
        run_id = run_workflow(workflow_id, api_id, prompt)
        
        # Check Image Generation is done
        check_run_status(workflow_id, api_id, run_id)
        
        # Return Image
        image = get_image(workflow_id, run_id, image_dir)
        
        return image
    except:
        logger.error(traceback.format_exc())