import paramiko
import os
import zipfile
from decouple import config as env




def download_abn_reports(hostname, port, username, key_file, remote_path, local_path):
    """
    Download ABN reports from the specified SFTP server.

    """
    rsa_key = paramiko.RSAKey.from_private_key_file(key_file)

    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(hostname=hostname, port=port, username=username, pkey=rsa_key)
    sftp = c.open_sftp()


    ls_remote_path = sftp.listdir(remote_path)

    ret = []
    for f in ls_remote_path:
        if f[0:3] == 'DEF':
            folder = f[10:18]
            local_folder = os.path.join(local_path, folder)
        elif f[0:2] == 'C_':
            folder = f[12:20]
            local_folder = os.path.join(local_path, folder)
        elif f[0:3] == 'STR':
            folder = f[10:18]
            local_folder = os.path.join(local_path, folder)
        elif f[0:3] == 'STC':
            folder = f[10:18]
            local_folder = os.path.join(local_path, folder)
        elif f[0:3] == "RPR":
            folder = f[14:22]
            local_folder = os.path.join(local_path, folder)
        elif f[0:3] == "eud":
            folder = f[18:26]
            local_folder = os.path.join(local_path, folder)
        elif f[0:7] == "FCCMDEF":
            folder = f[14:22]
            local_folder = os.path.join(local_path, folder)
        elif f[0:7] == "LIQCDEF":
            folder = f[14:22]
            local_folder = os.path.join(local_path, folder)
        elif f[0:8] == "SACCRDEF":
            folder = f[15:23]
            local_folder = os.path.join(local_path, folder)
        else:
            folder = f[0:8]
            local_folder = os.path.join(local_path, folder)
        print(f, "--> ", folder)
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
    print(len(ls_remote_path), "files found in ABN sftp directory")
    print(len(ret), "files have been downloaded")
    sftp.close()


if __name__ == '__main__':

    hostname =env("SFTP_HOST", "mft1.abnamroclearing.com")
    port =env("SFTP_PORT", 22)
    username = env("SFTP_USER", "3818")
    key_file = env("SAGORA_PKFILE", "/home/deployer/.ssh/id_sagora")
    remote_path = "/outgoing/"
    local_path = env("ABN_REPORT_PATH", "/home/deployer/reports/ABN_reports")
    # local_path = "/home/deployer/test_folder"
    download_abn_reports(hostname, port, username, key_file, remote_path, local_path)

