import azure.functions as func
import logging
import google.generativeai as palm
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger_llmgcp")
def http_trigger_llmgcp(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    palm.configure(api_key="AIzaSyAgDWLWSdeZUai_2Ka8Afej_nBq9-pgaRM")

    defaults = {
        'model': 'models/text-bison-001',
        'temperature': 0.7,
        'candidate_count': 1,        
        'top_k': 40,
        'top_p': 0.95,
        'max_output_tokens': 200,
        'stop_sequences': []
    }

    # Corrected prompt with triple quotes
    prompt = """I want to play tennis today. what skills are required in tennis"""

    response = palm.generate_text(
        **defaults,
        prompt=prompt
    )

    # Convert the response to a JSON format
    json_response = {
        "result": response.result
    }

    # Create an HTTP response with JSON content type
    return func.HttpResponse(json.dumps(json_response), mimetype="application/json", status_code=200) 
       