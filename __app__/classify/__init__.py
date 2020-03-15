import json
import logging
import azure.functions as func

# Import helper script
from ..model.predict import predict_image_from_url

def main(req: func.HttpRequest,
         context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed request \
                  with id %s.', context.invocation_id)
    image_url = req.params.get('img')
    logging.info('Image URL received: %s', image_url)

    results = predict_image_from_url(image_url)

    headers = {
        "Content-type": "application/json",
        "Access-Control-Allow-Origin": "*"
    }

    return func.HttpResponse(json.dumps(results), headers=headers)
