import frappe
import json
import subprocess
import os

@frappe.whitelist()
def create_aircraft_certificate(*args,**kwargs):
    # This fonction will be executed when the Execute Action Button will be clicked
    print('Hello World')
    # The data is transmitted via keyword argument
    print(kwargs)   
    aircraft = json.loads(kwargs.get('doc'))
    print(aircraft)
    tail_no = aircraft['tail_no']
    aircraft_type = aircraft['type']
    tenant_code = frappe.get_value("Tenant Settings", "Tenant Settings", "tenant_code")
    tenant_name = frappe.get_value("Tenant Settings", "Tenant Settings", "tenant_name")
    print(tenant_code, "-", aircraft_type, "-", tail_no)

    # generate 6 digit string
    random_number = frappe.generate_hash(length=6)
    temp_folder = f"./{frappe.local.site}/temp/{random_number}"
    # create directory if not exists
    subprocess.run(["mkdir", "-p", f"{temp_folder}"])
    private_key_path = f"{temp_folder}/client.key"
    csr_path = f"{temp_folder}/client.csr"
    crt_path = f"{temp_folder}/client.crt"
    pfx_path = f"{temp_folder}/client.pfx"

    openssl_folder = f"./{frappe.local.site}/openssl"
    cnf_path = f"{openssl_folder}/openssl.cnf"
    ca_crt_path = f"{openssl_folder}/root-ca.crt"
    ca_key_path = f"{openssl_folder}/root-ca.key"

    pfxPassword = "1q2w3e4r"
    subject = f"/C=US/ST=California/L=San Francisco/O={tenant_name}/CN={tenant_code}-{aircraft_type}-{tail_no}"
    # execute openssl genrsa command
    genrsa_p = subprocess.Popen(["openssl", "genrsa", "-out", f"{private_key_path}", "2048"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = genrsa_p.communicate()
    return_code = genrsa_p.wait()
    if return_code != 0:
      # raise error and break
      raise Exception(error.decode("utf-8"))
    # execute openssl req command
    req_p = subprocess.Popen(["openssl", "req", "-new", "-key", f"{private_key_path}", "-out", f"{csr_path}", "-subj", f"{subject}", "-config", f"{cnf_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = req_p.communicate()
    return_code = req_p.wait()
    if return_code != 0:
      # raise error and break
      raise Exception(error.decode("utf-8"))

    # execute openssl x509 command
    x509_p = subprocess.Popen(["openssl", "x509", "-req", "-days", "365", "-in", f"{csr_path}", "-CA", f"{ca_crt_path}", "-CAkey", f"{ca_key_path}", "-CAcreateserial", "-out", f"{crt_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = x509_p.communicate()
    return_code = x509_p.wait()
    if return_code != 0:
      # raise error and break
      raise Exception(error.decode("utf-8"))

    # execute openssl pkcs12 command
    pkcs12_p = subprocess.Popen(["openssl", "pkcs12", "-export", "-in", f"{crt_path}", "-inkey", f"{private_key_path}", "-out", f"{pfx_path}", "-passout", f"pass:{pfxPassword}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = pkcs12_p.communicate()
    return_code = pkcs12_p.wait()
    if return_code != 0:
      # raise error and break
      raise Exception(error.decode("utf-8"))

    # zip the temp folder and copy to the temp folder - write the command for both os.name = "nt" and else
    zip_p = subprocess.Popen(["zip", "-jr", f"{temp_folder}.zip", f"{temp_folder}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = zip_p.communicate()
    return_code = zip_p.wait()
    if return_code != 0:
      # raise error and break
      raise Exception(error.decode("utf-8"))


    # download private key by using frappe utils
    p = subprocess.run(["pwd"], stdout=subprocess.PIPE, text=True)
    current_path = p.stdout.replace("\n", "")
    path = f"{current_path}/{temp_folder}.zip"

    with open(path, "rb") as fileobj:
      filedata = fileobj.read()
    

    # delete private key file
    # subprocess.run(["rm", "-f", f"{private_key_path}"])

    # get doc from Aircraft doctype by tail_no
    
    doc = frappe.get_doc("Aircraft", aircraft['name'])
    f = frappe.utils.file_manager.save_file(f"{tail_no}-certificate-", filedata, doc.doctype, doc.name, "Home", False, 1, "certificate")
    doc.certificate = f.file_url
    doc.save()
    frappe.db.commit()

    # delete temp folder and temp_folder.zip
    subprocess.run(["rm", "-rf", f"{temp_folder}"])
    subprocess.run(["rm", "-f", f"{temp_folder}.zip"])

    




