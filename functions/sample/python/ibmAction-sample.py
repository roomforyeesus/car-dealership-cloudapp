#get all reviews

import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
def main(dict):
    authenticator = IAMAuthenticator('U9ZDVwNK5j08RAMBwmFR3GJcg94l_y0_5QBPdfb_fKdQ')
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url("https://1a40a29e-dcf8-46a4-8c42-12a5c8033830-bluemix.cloudantnosqldb.appdomain.cloud")
    response = service.post_find(
    db='reviews',
    selector={'dealership': {'$eq': int(dict["id"])}},
    ).get_result()
    try:
        # result_by_filter=my_database.get_query_result(selector,raw_result=True)
        result= {
        'headers': {'Content-Type':'application/json'},
        'body': {'data':response}
        }
        return result
    except:
        return {
        'statusCode': 404,
        'message': 'Something went wrong'
        }
        
        
        
#post review

#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
def main(dict):
    authenticator = IAMAuthenticator('U9ZDVwNK5j08RAMBwmFR3GJcg94l_y0_5QBPdfb_fKdQ')
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url("https://1a40a29e-dcf8-46a4-8c42-12a5c8033830-bluemix.cloudantnosqldb.appdomain.cloud")
    response = service.post_document(db='reviews', document=dict["review"]).get_result()
    try:
    # result_by_filter=my_database.get_query_result(selector,raw_result=True)
        result= {
        'headers': {'Content-Type':'application/json'},
        'body': {'data':response}
        }
        return result
    except:
        return {
        'statusCode': 404,
        'message': 'Something went wrong'
        }