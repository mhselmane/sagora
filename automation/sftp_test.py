import paramiko
import os
import zipfile

rsa_key = paramiko.RSAKey.from_private_key_file("/home/deployer/.ssh/id_sagora")
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect(hostname="mft1.abnamroclearing.com", port=22, username="3818", pkey=rsa_key)
sftp = c.open_sftp()

remote_path = "/outgoing/"
ls_remote_path = sftp.listdir(remote_path)

local_path = "/home/deployer/test_folder"
#local_path = "/home/deployer/reports/ABN_reports"


ret = []
for f in ls_remote_path:
    if f[0:3] == 'DEF':
        local_folder = os.path.join(local_path, f[10:18])
    elif f[0:2] in {'C_', 'ST', 'ST'}:
        local_folder = os.path.join(local_path, f[-12:-4])
    elif f[0:3] == "RPR":
        local_folder = os.path.join(local_path, f[14:22])
    elif f[0:3] == "eud":
        local_folder = os.path.join(local_path, f[18:26])
    else:
        local_folder = os.path.join(local_path, f[0:8])

# create local_folder if doesn't exit
if not os.path.exists(local_folder):
    os.makedirs(local_folder)

# download the file from the SFTP server to the local folder
local_file = os.path.join(local_folder, f)
remote_file = os.path.join(remote_path, f)
sftp.get(remotepath=remote_file, localpath=local_file)
ret.append(local_file)
if f.endswith(".zip"):
    # extract the contents of the zip file to the extract directory
    with zipfile.ZipFile(os.path.join(local_folder, f), "r") as zip_ref:
        zip_ref.extractall(local_folder)
    # delete the original zip file
    os.remove(os.path.join(local_folder, f))

sftp.close()

if __name__ == '__main__':
    print(ret)
