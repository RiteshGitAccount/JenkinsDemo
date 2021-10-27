
def sentance_maker(phrase):
    interrogatives = ("how", "what","why")
    capatilized = phrase.capatilized()
    if phrase.startswith(interrogatives):
        return "{}?".format(capatilized)
    else:
        return "{}.".format(capatilized)

    result = []

    while True:
        user_input = input("Say Something : ")
        if user_input == "\end":
            break
        else:
            result.append(sentance_maker((user_input)))

    print("" .join(result))