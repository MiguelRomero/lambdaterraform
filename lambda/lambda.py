import json
def lambda_handler(event, context):

    return{
        'StatusCode':200,
        'body': json.dumps(event['headers']['C-Forwarded-For'])
    }