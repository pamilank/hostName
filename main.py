# Created by PAMILANK (June 24, 2021)
# Updated by PAMILANK (June 28, 2021)

import socket  # to get hostname
import webbrowser  # to open home.html in browser
import os  # to get current working directory getcwd()


def getHostName(string):
    host = ''
    printer_socket = (socket.gethostbyaddr(string))  # it will get Host Name, Alias list for the IPs, IP of HOST
    host = host.join(printer_socket[0])  # index 0 is for Hostname
    # host = host.replace('.ewr5.amazon.com', '')
    return host


def colorHost(string):  # to check the status is READY or not for coloring
    if string == "freeip.amazon.com":
        color_str = """
                    <td class = "greenGlass">%s</td> 
                    """ % string
    else:
        color_str = """
                    <td>%s</td>
                    """ % string

    return color_str


def hostTable():
    html_str = ""
    first = 7
    last = 65
    ips = ""
    for i in range(first, (first + last) // 2):
        try:
            ips = "10.22.55." + str(i)
            hostname = getHostName(ips)  # get the hostname of the device using socket
            # Read and write on home.html if URL is pingable
            html_str += """
                                                <tr>
                                                    <td>%s</td>                  
                                                """ % ips
            html_str += colorHost(hostname) + """
                                                    <td>TBD</td>
                                                    </tr>
                                                 """  # add conditional coloring in status column
        except IOError:
            # Read and write on home.html if URL is not pingable
            html_str = html_str + """
                                      <tr>
                                         <td>%s</td>
                                         <td class = "redClass">Not Found</td>
                                          <td class = "redClass">Not Found</td>
                                      </tr>                    
                                      """ % ips

    for i in range((first + last) // 2, last + 1):
        try:
            ips = "10.22.55." + str(i)
            hostname = getHostName(ips)  # get the hostname of the device using socket
            # Read and write on home.html if URL is pingable
            html_str += """
                                                <tr>
                                                    <td>%s</td>                  
                                                """ % ips
            html_str += colorHost(hostname) + """
                                                    <td>TBD</td>
                                                    </tr>
                                                 """  # add conditional coloring in status column
        except IOError:
            # Read and write on home.html if URL is not pingable
            html_str = html_str + """
                                      <tr>
                                         <td>%s</td>
                                         <td class = "redClass">Not Found</td>
                                          <td class = "redClass">Not Found</td>
                                      </tr>                    
                                      """ % ips

    return html_str


if __name__ == '__main__':
    # start of the html
    html_home = """
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <title>EWR5 - VLAN</title>
                        <link rel="stylesheet" href="styles.css">
                    </head>               
                    <body>
                    <div class="header">
                      <h1>EWR5 - VLAN 750</h1>
                    </div>
                    <table class="styled-table">
                        <thead>
                            <tr>
                                <th>IP Address</th>
                                <th>Hostname</th>
                                <th>Pingable ?</th>
                            </tr>
                        </thead>
                        <tbody>
                    """

    html_file = open("home.html", "r")
    html_file.close()

    html_home += hostTable() + """  </tbody> </table> </body> </html>  """
    Html_file = open("home.html", "w")
    Html_file.write(html_home)
    Html_file.close()

    # os.getcwd( ) returns current working directory of a process
    filename = 'file:///' + os.getcwd() + '/' + 'home.html'
    # open html file in browser
    webbrowser.open_new_tab(filename)
