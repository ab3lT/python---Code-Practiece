import ftplib
import urllib


def anon_login(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'me@your.com')
        print("\n[*] "+ str(hostname) + " FTP Anonymous Logon Succeeded.")
        ftp.quit()
        return True
    except Exception as e:
        print("\n[-] " + str(hostname) + " FTP Anonymous Logon Failed.")
        return False


host = "192.168.95.179"
anon_login(host)

