from tkinter import Tk, filedialog
import pywt
from terminal_layout.extensions.choice import StringStyle, Choice
from terminal_layout import Fore


class Menu():
    wave_name = pywt.families()
    wave_choice = Choice(
        'Please select wavelet',
        wave_name,
        icon_style=StringStyle(fore=Fore.lightblue),
        selected_style=StringStyle(fore=Fore.lightblue)
    ).get_choice()
    wave_choice_optional = Choice(
        'Please select second wavelet',
        wave_name.append('No more wavelet needed'),
        icon_style=StringStyle(fore=Fore.lightblue),
        selected_style=StringStyle(fore=Fore.lightblue)
    ).get_choice()
    window = Tk()
    window.withdraw()
    filePath = filedialog.askopenfilename()


    def menu(self):
        result = {
            'waveChoice': self.wave_choice[1],
            'waveChoiceOptional': None if self.wave_choice_optional == 'No more wavelet needed' else self.wave_choice_optional[1],
            'filePath': self.filePath
        }

        return result


if __name__ == '__main__':
    Menu().menu()