#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo, using the function do_pack.
"""

from fabric import task
from datetime import datetime

@task
def do_pack(c):
    """do"""
    # Generate timestamp for the archive name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{timestamp}.tgz"
    
    # Create versions folder if it doesn't exist
    c.local("mkdir -p versions")
    
    # Create .tgz archive
    result = c.local(f"tar -czvf versions/{archive_name} web_static")
    
    # Check if tar command was successful
    if result.failed:
        return None
    else:
        return f"versions/{archive_name}"
