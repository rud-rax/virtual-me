
import sys
sys.path.append(".")

from src.langflow_request import run_flow

FLOW_ID = "e41b3d64-a2f4-4907-aa87-9d14c4a178f4"


# message = "What kind of Python modules have you used ?"
while True : 
        
    message = input("Question : ")

    if message.rstrip() == "EXIT" : break

    bot_response = run_flow(message=message, flow_id=FLOW_ID)
    print("Answer : " , bot_response['outputs'][0]['outputs'][0]['results']['result'])

