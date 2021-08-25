""" Extra lesson in object-oriented programming """

from participant import Participant  # importing our Participant class from participant.py


def main():
    cip_participant = Participant("Brahm Capoor", "brahm@cs.stanford.edu", "section leader")
    print(f"The participant's name is {cip_participant.name}")
    print(f"The participant's email is {cip_participant.email}")
    print(f"The participant's role is {cip_participant.role}")


if __name__ == "__main__":
    main()
