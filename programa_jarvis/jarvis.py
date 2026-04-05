import speech_recognition as sr
import pyttsx3
import datetime
import os
import webbrowser

# CONFIGURAÇÃO DA VOZ
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    if "brazil" in voice.name.lower() or "portuguese" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break
engine.setProperty('rate', 180)

def falar(texto):
    print(f"Jarvis: {texto}")
    engine.say(texto)
    engine.runAndWait()

# CONFIGURAÇÃO DO OUVIDO
def ouvir():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as source:
        reconhecedor.adjust_for_ambient_noise(source, duration=1)
        print("Pode falar, senhor...")
        try:
            audio = reconhecedor.listen(source, timeout=5)
            comando = reconhecedor.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {comando}")
            return comando.lower()
        except:
            return ""

# LOOP PRINCIPAL
if __name__ == "__main__":
    falar("Sistemas online. O que deseja?")
    
    while True:
        comando = ouvir()

        # Abrir o VS Code
        if 'abrir vscode' in comando or 'abrir visual studio' in comando:
            falar("Abrindo o editor de código, senhor.")
            caminho_codigo = '/home/alan_souza03/Documentos/GitHub/meus-projetos/'
            os.system(f"code {caminho_codigo} &")

        # Abrir o Edge
        elif 'abrir edge' in comando or 'navegador' in comando:
            falar("Iniciando o Microsoft Edge.")
            os.system("microsoft-edge &")

        # Ver as Horas
        elif 'horas' in comando:
            hora = datetime.datetime.now().strftime('%H:%M')
            falar(f"Agora são {hora}")

        # Abrir o YouTube 
        elif 'abrir youtube' in comando:
            falar("Abrindo o YouTube no seu navegador.")
            webbrowser.open("https://www.youtube.com/watch?v=XgWUDbYfNe4&list=RDXgWUDbYfNe4&start_radio=1")

        # Desligar o Jarvis
        elif 'desligar' in comando or 'tchau' in comando:
            falar("Encerrando sistemas. Até a próxima.")
            break