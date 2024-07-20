The honeypot is a security mechanism that is implemented by appending it to the
telnet port 21, and it is responsible for monitoring and listening to the system
for any incoming connections. The telnet port, in particular, has been known to be
vulnerable and prone to security breaches. However, when an unauthorized connection
is attempted on this port, the honeypot is designed to detect the intrusion attempt
and flag it as suspicious. Moreover, it also identifies the IP address and the port 
number from which the attack was initiated, providing valuable information for further 
investigation and prevention of future attacks.It should be emphasized that the
honeypot system effectively detected the attack and immediately alerted the main system.
Specifically, the alert was triggered as soon as the attackers began searching for open 
or vulnerable ports on the system, which they could exploit to gain unauthorized access 
to confidential data. This allowed the security team to respond swiftly and take 
appropriate measures to thwart. 



**ADMIN SIDE**


Admin only be able to start the honeypot connection and keeps it active looking for
intrusions. The IP address of the attacker and the port number through which the intrusion
attempt was made gets unveiled in the terminal.


![Screenshot 2024-07-20 223535](https://github.com/user-attachments/assets/4c20dbdb-cea4-4316-835e-72c2cad7a1ee)



**ATTACKER SIDE**


When attackers make an attempt and succeed in breaking into the system a telnet login
banner will pop up. He is redirected into a honeypot and successfully gets tricked by the fake
banner. The attacker believes to have succeeded but the honeypot outsmarts his actions and
keeps him interactive

![Screenshot 2024-07-20 223552](https://github.com/user-attachments/assets/3aa51aff-cb9d-4cb3-b265-1f5401c0557b)



![Screenshot 2024-07-20 223510](https://github.com/user-attachments/assets/7c50cddb-2a24-4f7a-bda3-f8b9d781cee0)




![Screenshot 2024-07-20 223454](https://github.com/user-attachments/assets/dd8b7ddb-b9a6-4a58-b323-af3d8ab9b304)







