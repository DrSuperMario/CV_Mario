import matplotlib.pyplot as plt 
import matplotlib.image as imgRead
from enum import Enum

profilePicture = imgRead.imread('ink.png')

class ProfileStatic(Enum):

    LANGUAGES = ('PYTHON','JAVA','HTML&CSS')
    NUMBERS = (50,25,25)
    EXPLODEPARAM = (0, 0.1, 0)

    
class ProfileDynamic():

    languagePieParam = ['PYTHON', 'JAVA', 'HTML&CSS']

    
