from wmi import WMI
from PyQt5.QtWidgets import QApplication
from gui_form import GUIForm
from sys import argv, exit, executable
from ctypes import windll


def get_client_args() -> str:
    wmi_obj = WMI()
    ffproc = wmi_obj.Win32_Process(Name='ffxiv_dx11.exe')

    command = ffproc[0].CommandLine

    return command


def save_command():
    command = get_client_args()
    with open('./command.directrun', 'w') as f:
        f.write(command)


def load_command() -> str:
    try:
        with open('./command.directrun', 'r') as f:
            command = f.read()
    except IOError:
        command = ''

    return command


def run_ffxiv():
    command = load_command()
    if len(command) > 0:
        process = WMI().Win32_Process
        process.Create(CommandLine=command)
        exit()


def is_admin():
    try:
        return windll.shell32.IsUserAnAdmin()
    except:
        return False


def main():
    app = QApplication([])

    guiform = GUIForm()
    guiform.btn_save.clicked.connect(save_command)
    guiform.btn_run.clicked.connect(run_ffxiv)
    guiform.show()

    exit(app.exec_())


if __name__ == '__main__':
    if is_admin():
        main()
    else:
        windll.shell32.ShellExecuteW(None, 'runas', executable, " ".join(argv), None, 1)
