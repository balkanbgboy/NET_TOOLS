# NET_TOOLS README

This Python program provides 5 Tools which can be helpful for Network Engineers:
```Python
Enter:
 '1' Print IP addresses in IP range
 '2' Provide Network and Wildcard mask
 '3' Check Ip address/mask and provide network information
 '4' Create Subnets from Supernet
 '5' Subnet(Route) Summarization
 'q' to quit (Ctrl + C to exit at any time):
 ```
There is an option to print or save the infomration on .csv files.

To Run the program on Windows, add the NET_TOOL folder on the env path.
Create ip.bat file( as the example provided).Then Simultaneously press the Windows and R keys
to get RUN and just type ip.
When saving infomration, the program is asking for path where to save the information as csv files, so just
copy and paste the exact path from the folder( ex: C:\Users\ivan\Desktop\NET_TOOLS\IPranges)

## DOCKER

To avoid all the python dependancies that you need to install on your PC, you can run the programm in Docker:
 * Download the image from Docker Hub:
   `docker pull balkanbgboy/net-tool`
 * Create CSVfiles Folder on your PC
 * Create ip.bat file and put in a folder witch in your System path
 * Update the bat file with the following(change the path to match yours):
   `docker run -it --rm --name net-tool-app  -v C:\Users\ivan\Desktop\CSVfiles:/app/CSVfiles f4acb5bcadec`
   


## ERROR

The container is removed once you close the Programm.However if you did not exit the program and try to run again
you will get the following error:
 `docker: Error response from daemon: Conflict. The container name "/net-tool-app" is already....`
In this case run the following command to remove:
  `docker rm -f net-tool-app`
Run the program again!

##CONTRIBUTORS
 1.balkanbgboy

