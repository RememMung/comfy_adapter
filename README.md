# comfy_adapter

## Overview
Get Image generated by ComfyUI through REST api<br><br>
Image saved in /images<br><br>

## Config.ini
```ini
[flask]
DEBUG = True

[logger]
LOG_FILE = app.log
LOG_LEVEL = DEBUG

[ComfyUI]
WORKFLOW_ID = 
API_ID = 
WORKFLOW_FILE = workflow/workflow.json
IMAGE_DIR = 
```

## tutorial
```sh
pip install requirement.txt
```
```
curl http://{host_ip}:{host_port}/comfy/getImage?parameter
```
