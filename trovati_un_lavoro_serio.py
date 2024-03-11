from tkinter import *
import os
# import subprocess

root = Tk()
root.title("TROVATI UN LAVORO SERIO!!!!")
root.resizable(width=False, height=False)
root.geometry("445x300")

def sys_info_bt():
      os.system("start cmd /c sysdm.cpl")

sys_info= Button(root, text="Propietà del Sistema", width=30, height=2, command = sys_info_bt)
sys_info.grid(row=0, column= 0,)


def msconfig_bt():
      os.system("start cmd /c msconfig")

prg_start = Button(root, text="Gestione avvio", width=30, height=2, command = msconfig_bt)
prg_start.grid(row=1, column= 0,)

def str_amm_windows_bt():
      os.system("start cmd /c control admintools")

str_amm_windows= Button(root, text="Strumenti Amm. WIndows", width=30, height=2, command = str_amm_windows_bt)
str_amm_windows.grid(row=2, column= 0,)

def prog_win_bt():
      os.system("start cmd /c appwiz.cpl")

prog_com_wind= Button(root, text="Programmi e Componenti Aggiuntivi", width=30, height=2, command = prog_win_bt)
prog_com_wind.grid(row=3, column= 0,)

def ip_conf_bt():
      os.system("start cmd /k ipconfig")

ip_conf= Button(root, text="Visualizzazione IP", width=30, height=2, command = ip_conf_bt)
ip_conf.grid(row=4, column= 0,)

def net_hard_bt():
      os.system("start cmd /c ncpa.cpl")

net_hard= Button(root, text="Schede di rete", width=30, height=2, command = net_hard_bt)
net_hard.grid(row=5, column= 0,)

def tsk_mgr_bt():
      os.system("start cmd /k taskmgr")

tsk_mgr= Button(root, text="Task Manager", width=30, height=2, command = tsk_mgr_bt)
tsk_mgr.grid(row=6, column= 0,)

def msinfo_bt():
      os.system("start cmd /c msinfo32")

ms_info= Button(root, text="MS Info", width=30, height=2, command = msinfo_bt)
ms_info.grid(row=0, column= 1,)

def serv_msc_bt():
      os.system("start cmd /c comexp.msc")

serv_event= Button(root, text="Eventi e Servizi Windows", width=30, height=2, command = serv_msc_bt)
serv_event.grid(row=1, column= 1,)

def pnl_ctrl_bt():
      os.system("start cmd /c control")

panl_ctrl= Button(root, text="Pannello di Controllo", width=30, height=2, command = pnl_ctrl_bt)
panl_ctrl.grid(row=2, column= 1,)

def ip_all_bt():
      os.system("start cmd /k ipconfig /all")

ip_conf_all= Button(root, text="IP Full", width=30, height=2, command = ip_all_bt)
ip_conf_all.grid(row=4, column= 1,)

def fls_dns_bt():
      os.system("start cmd /k ipconfig /aflushdns")

flush_dns= Button(root, text="Cancella Cache DNS", width=30, height=2, command = fls_dns_bt)
flush_dns.grid(row=5, column= 1,)

def dns_dm_bt():
      os.system("start cmd /c nslookup")

dns_resol= Button(root, text="NS Lookup", width=30, height=2, command = dns_dm_bt)
dns_resol.grid(row=6, column= 1,)

def crtl_perso_bt():
      os.system("start cmd /c control folders")

crtl_perso= Button(root, text="Personalizzazione cartelle", width=30, height=2, command = crtl_perso_bt)
crtl_perso.grid(row=3, column= 1,)

#ping.pack()


root.mainloop()