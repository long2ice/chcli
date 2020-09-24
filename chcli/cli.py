from prompt_toolkit import PromptSession

if __name__ == '__main__':
    session = PromptSession(':)')

    text1 = session.prompt()
    print(text1)
    text2 = session.prompt()
    print(text2)
