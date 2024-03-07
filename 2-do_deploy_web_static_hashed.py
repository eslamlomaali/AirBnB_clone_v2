# #!/usr/bin/python3
# """


# from fabric.api import *
# from datetime import datetime
# from os.path import exists


# #env.hosts = ['35.237.166.125', '54.167.61.201']  # <IP web-01>, <IP web-02>
# env.hosts = ['54.152.60.211', '34.229.71.198']  # <IP web-01>, <IP web-02>
# # ^ all commands must be executed
# # (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)


# def do_deploy(archive_path):
#     """ distributes the archive to
#     """
#     if exists(archive_path) is False:
#         return False  # Returns False if the file not found
#     filename = archive_path.split('/')[-1]
#     no_tgz = '/data/web_static/releases/' + "{}".format(filename.split('.')[0])
#     tmp = "/tmp/" + filename

#     try:
#         put(archive_path, "/tmp/")
#         # ^ Upload the archive
#         run("mkdir -p {}/".format(no_tgz))
#         # decompress the archive
#         run("tar -xzf {} -C {}/".format(tmp, no_tgz))
#         run("rm {}".format(tmp))
#         run("mv {}/web_static/* {}/".format(no_tgz, no_tgz))
#         run("rm -rf {}/web_static".format(no_tgz))
#         # ^ Delete the archive
#         run("rm -rf /data/web_static/current")
#         # Delete the link
#         run("ln -s {}/ /data/web_static/current".format(no_tgz))
#         # Create a new link
#         # linking to the new version
#         return True
#     except:
#         return False
