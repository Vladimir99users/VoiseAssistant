from VoiceAssistant import VoiceAssistant
import speech_recognition  # распознавание пользовательской речи (Speech-To-Text)
import pyttsx3  # синтез речи (Text-To-Speech)
import os  # работа с файловой системой


def play_greetings():
     assistant.play_voice_assistant_speech("Здравствуйте")
     return

def play_kvantorium():
     
     text = """
        Я робот Адольф, готов ответить вам на вопросы.
        К сожалению, я ещё в доработке, поэтому не могу вам помочь, но могу рассказать как захватить СССР
     """
     assistant.play_voice_assistant_speech(text)
     return

commands = {
    ("hello", "hi", "morning", "привет"): play_greetings,
    ("адольф"): play_kvantorium
}

def execute_command_with_name(command_name: str):
    """
    Выполнение заданной пользователем команды с дополнительными аргументами
    :param command_name: название команды
    :param args: аргументы, которые будут переданы в функцию
    :return:
    """
    for key in commands.keys():
        if command_name in key:
            commands[key]()
            #func.
        else:
            pass  # print("Command not found")


if __name__ == "__main__":

    # инициализация инструментов распознавания и ввода речи
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    # инициализация инструмента синтеза речи
    ttsEngine = pyttsx3.init()
    # настройка данных голосового помощника
    assistant = VoiceAssistant(ttsEngine, "Alice", "male","ru", recognizer,microphone)

    # установка голоса по умолчанию
    assistant.setup_assistant_voice()

    while True:
        # старт записи речи с последующим выводом распознанной речи
        # и удалением записанного в микрофон аудио
        try :
                voice_input = assistant.record_and_recognize_audio()
                os.remove("microphone-results.wav")
                print(voice_input)
                # отделение комманд от дополнительной информации (аргументов)
                voice_input = voice_input.split(" ")
                command = voice_input[0]

                if "конец" in voice_input:
                     break

                execute_command_with_name(command)
        except Exception as exp:
            continue
