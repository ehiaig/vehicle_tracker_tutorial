from theiaengine import TheiaClient, TheiaPayload, TheiaResponseStatus
import logging

logger = logging.getLogger(__name__)

def extract_number_plate(image_path: str):
    server_url = "https://theiaenginealpha3.genxr.co/upload"
    api_key = "" #Supply your TheiaEngine API key here

    theia_client = TheiaClient(
        api_key=api_key,
        theia_url=server_url
    )

    payload = TheiaPayload()
    payload.image = open(image_path, "rb")
    payload.return_ocr = True #This is very important since OCR is our main focus here
    
    response = theia_client.inference(
        payload=payload
    )
    result = {
        "number_plate": "",
        "description": "",
    }
    if response.status == TheiaResponseStatus.SUCCESS:
        result_obj = response.result
        extracted_ocr = " ".join([res["text"] for res in result_obj.ocr])
        result["number_plate"] = extracted_ocr
        result["description"] = result_obj.description
    else:
        logger.error("TheiaEngine Error", extra={"status": response.status, "message": response.message})
    return result
