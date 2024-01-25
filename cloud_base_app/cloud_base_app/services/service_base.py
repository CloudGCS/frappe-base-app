import frappe
import requests
import http.client

class ServiceBase:
    def __init__(self, service: str, module: str, host_url: str):
        self.host_url = host_url
        self.module = module
        self.service = service
    
    def call(self, method: str, endpoint: str, payload: dict = None):
        response = None

        if method == 'get':
            response = requests.get(f"{self.host_url}/{endpoint}")
        elif method == 'post':
            response = requests.post(f"{self.host_url}/{endpoint}", json=payload)
        elif method == 'put':
            response = requests.put(f"{self.host_url}/{endpoint}", json=payload)
        elif method == 'delete':
            response = requests.delete(f"{self.host_url}/{endpoint}")
        else:
            frappe.throw('Invalid service API call method: ' + method)

        response_status = http.client.responses.get(response.status_code, "Unknown Status Code")

        doc = frappe.get_doc({
            'doctype': "Service API Call",
            'service': self.service,
            'module': self.module,
            'host_url': self.host_url,
            'method': method,
            'endpoint': endpoint,
            'request_payload': payload,
            'response_status': str(response.status_code) + ' - ' + response_status,
            'response_payload': response.text
        })
        doc.insert()
        return response

    def get(self, endpoint:str):
        return self.call('get', endpoint)
    
    def put(self, endpoint:str, payload: dict = None):
        return self.call('put', endpoint, payload)
        
    def post(self, endpoint:str, payload: dict = None):
        return self.call('post', endpoint, payload)
        
    def delete(self, endpoint:str):
        return self.call('delete', endpoint)

    def patch(self, endpoint:str, payload: dict = None):
        return self.call('patch', endpoint, payload)   

