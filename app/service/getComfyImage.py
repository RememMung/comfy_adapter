import requests
import json
from flask import current_app
from app.logger import get_logger
import traceback
import os
import time

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
    logger.info(f"RUN WORKFLOW SUCCESS : {response}")
    return response['id']
    

def check_run_status(workflow_id, api_id, run_id):
    url = f"https://comfy.icu/api/v1/workflows/{workflow_id}/runs/{run_id}"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {api_id}"
    }

    response = requests.get(url, headers=headers).json()
    return response['status']

def get_workflow(workflow_file, parameter):
    with open(f"{workflow_file}", "r", encoding="utf-8") as f:
        workflow_data = f.read()
    workflow = json.loads(workflow_data)
    workflow["6"]["inputs"]["text"] = parameter
    logger.info("GET WORKFLOW SUCCESSED")
    return workflow

def get_image(workflow_id, run_id, image_dir):
    image_uri = f'https://r2.comfy.icu/workflows/{workflow_id}/output/{run_id}/ComfyUI_00001_.png'
    os.system(f"curl " + image_uri + f" > ./app/images/{run_id}.png")
    logger.info(f"GET IMAGE SUCCESSED : {run_id}.png")
    return f"images/{run_id}.png"

def run(parameter):
    workflow_id = current_app.config['WORKFLOW_ID']
    api_id = current_app.config['API_ID']
    workflow_file = current_app.config['WORKFLOW_FILE']
    image_dir = current_app.config['IMAGE_DIR']
    
    try:
        # get Prompt from JSON file
        prompt = get_workflow(workflow_file, parameter)

        # run ComfyUI Workflow by REST request
        run_id = run_workflow(workflow_id, api_id, prompt)
        
        # Check Image Generation is done
        while True:
            status = check_run_status(workflow_id, api_id, run_id)
            logger.info(status == 'COMPLETED')
            if status == 'COMPLETED' or status == 'FAILED':
                break
            time.sleep(3)
            
        # Return Image
        if status == 'COMPLETED':
            image = get_image(workflow_id, run_id, image_dir)    
            return image
        else:
            return None
        
    except:
        logger.error(traceback.format_exc())