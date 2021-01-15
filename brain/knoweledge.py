import matplotlib.image as imgRead
import pandas as pd


pic = imgRead.imread('brain\ink.png')

def tabel_of_know():

    df = pd.DataFrame(index=None, columns=['Languages','Tools','Cloud','Enviroments','Frameworks','Setup', 'Other'])
    df['Languages'] = ['JAVA','Python','SQL/HTML/CSS','Octave','Nan','Nan']
    df['Tools'] = ['VSCode','Intellij','Android Studio','Postman','Octave','PowerShell']
    df['Cloud'] = ['DigitalOcean','Heroku','TravisCI','Nan','Nan','Nan']
    df['Enviroments'] = ['Windows', 'Ubuntu', 'ArchLinux','Nan','Nan','Nan']
    df['Frameworks'] = ['Flask','AndroidAPI','TensorFlow','NLTK','Nan','Nan']
    df['Setup'] = ['HP Pavilion 15','Raspberry pi4B','Raspberry pi400','RaspberryZero','Nan','Nan']
    df['Other'] = ['Machine Learning','Deep Learning','Data Science','Nan','Nan','Nan']
    df = df.replace('Nan',' ')
    return df.style.set_properties(**{'background-color': 'white',
                           'color': 'black',
                           'border-color': 'white',
                           'font-size':'16px',
                           'text-align':'left',
                           'font-weight':'bold'}).hide_index()



    
