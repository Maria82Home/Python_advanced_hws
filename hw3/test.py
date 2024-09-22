def ten_popular(text: str) -> list[str]:
    delete = ".,!?;:-[]{}()="
    for i in delete:
        text = text.replace(i, "")
    text = text.lower()
    return sorted(set(text.split()), key=lambda x: text.count(x))[-10:]

string = 'Python 3.12 is the latest stable release of the Python programming language, \
    with a mix of changes to the language and the standard library. The library changes \
        focus on cleaning up deprecated APIs, usability, and correctness. Of note, the distutils \
            package has been removed from the standard library. Filesystem support in os and pathlib \
                has seen a number of improvements, and several modules have better performance. \
The language changes focus on usability, as f-strings have had many limitations removed and \
    suggestions continue to improve. The new type parameter syntax and type statement improve ergonomics for \
        using generic types and type aliases with static type checkers. \
This article doesn’t attempt to provide a complete specification of all new \
    features, but instead gives a convenient overview. For full details, you should \
        refer to the documentation, such as the Library Reference and Language Reference. \
            If you want to understand the complete implementation and design rationale for a \
                change, refer to the PEP for a particular new feature; but note that PEPs usually \
                    are not kept up-to-date once a feature has been fully implemented. \
        '
print(ten_popular(string))