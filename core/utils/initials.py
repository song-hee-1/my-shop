from jamo import h2j, j2hcj


def get_initials(text):
    """
    :param text:
    :return: text의 초성

    ex. text: 슈크림 라떼 >> return ㅅㅋㄹ ㄹㄸ
    """

    initial_list = []
    for char in text:
        temp = h2j(char)  # 자음과 모음으로 분리
        imf = j2hcj(temp)  # 초성, 중성, 종성으로 분리
        initial_list.append(imf[0])

    return "".join(initial_list)

