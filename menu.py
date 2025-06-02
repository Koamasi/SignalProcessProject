from tkinter import Tk, filedialog
import pywt
from terminal_layout.extensions.choice import StringStyle, Choice
from terminal_layout import Fore


class Menu():
    wave_name = pywt.families()
    wave_choice = Choice(
        'Please select wavelet',
        wave_name,
        icon_style=StringStyle(fore=Fore.blue),
        selected_style=StringStyle(fore=Fore.blue)
    ).get_choice()
    window = Tk()
    window.withdraw()
    filePath = filedialog.askopenfilename()


    def menu(self):
        result = {'waveChoice': self.wave_choice[1]}

        return result


if __name__ == '__main__':
    Menu().menu()