Simple Remote Desktop Connection Client in PyQt4<br>
Forked from Gibbio's RDPGUI: https://github.com/Gibbio/RDPGUI<br>
<br>
Able to store multiple configurations with reduced config.
<br>
Packages needed: python-qt4, python-configparser,python-urllib3
<br>
edit rdpgui.ini to fit your server environment<br>
<br>
config for FreeRDP > 1.0.1 (new command line release: https://github.com/FreeRDP/FreeRDP/wiki/CommandLineInterface):<br>
[DEFAULT]<br>
RDPBinary = xfreerdp<br>
RDPDomain = RPiTC<br>
RDPServer = server1.domain.lan server2.domain.lan server3.domain.lan<br>
RDPDomainFlags = /d:<br>
RDPServerFlags = /v:<br>
RDPUserFlags = /u:<br>
RDPPasswordFlags = /p:<br>
RDPDefaulfFlags = /cert-ignore /f<br>
RDPExtraFlags = /sound:sys:pulse /rfx /fonts<br>
<br>
config for FreeRDP < 1.0.1 (old command line release: https://github.com/FreeRDP/FreeRDP/wiki/CommandLineInterface#other-options-1):<br>
[DEFAULT]<br>
RDPBinary = xfreerdp<br>
RDPDomain = RPiTC<br>
RDPServer = server1.domain.lan server2.domain.lan server3.domain.lan<br>
RDPDomainFlags = "-d "<br>
RDPServerFlags = ""<br>
RDPUserFlags = "-u "<br>
RDPPasswordFlags = "-p "<br>
RDPDefaulfFlags = "-x l -f"<br>
RDPExtraFlags = "--plugin rdpsnd -z --rfx"<br>
<br>
config for RDesktop (command line reference: https://github.com/rdesktop/rdesktop/blob/master/doc/rdesktop.1):<br>
[DEFAULT]<br>
RDPBinary = rdesktop<br>
RDPDomain = RPiTC<br>
RDPServer = server1.domain.lan server2.domain.lan server3.domain.lan<br>
RDPDomainFlags = "-d "<br>
RDPServerFlags = ""<br>
RDPUserFlags = "-u "<br>
RDPPasswordFlags = "-p "<br>
RDPDefaulfFlags = "-x l -f"<br>
RDPExtraFlags = "-r sound:local:alsa -z"<br>
