# File: NumerologyLifePathDetails.py

# Assignment: Numerology with Inheritance 
# Class: Python-2 w/ Prof C *
# Author: Matthew Simone
# Due Date: 12/01/2024

class NumerologyLifePathDetails:
    def __init__(self, sName: str, sDOB: str) -> None:
        self.Name = sName
        self.DOB = sDOB

        # Validate inputs
        self._validate_dob()
        self._validate_name()

        # Calculate the numbers
        self.__iLifePathNumber = self._reduce_number(sum(int(digit) for digit in self._nDOB))
        self.__iBirthdayNumber = self._reduce_number(sum(int(day_digit) for day_digit in self._nDOB[2:4]))
        self.__iAttitudeNumber = self._reduce_number(sum(int(year_month_digit) for year_month_digit in self._nDOB[:4]))
        self.__iSoulNumber = self._reduce_number(
            sum(self._char_to_int(letter) for letter in self._sName if letter in "AEIOU"))
        self.__iPersonalityNumber = self._reduce_number(
            sum(self._char_to_int(char) for char in self._sName if char not in "AEIOU"))
        self.__iPowerName = self._reduce_number(self.__iSoulNumber + self.__iPersonalityNumber)

    # Validation functions
    def _validate_dob(self) -> None:
        if not (len(self._nDOB) == 8 and self._nDOB.isdigit()):
            raise ValueError("DOB format must be 'mm-dd-yyyy' or 'mm/dd/yyyy'")
    def _validate_name(self) -> None:
        if not self._sName:
            raise ValueError("Name cannot be empty.")

    # Getters for Name and DOB
    @property
    def Name(self) -> str:
        return self._sName
    @property
    def DOB(self) -> str:
        return self._sDOB

    # Setters for Name and DOB
    @Name.setter
    def Name(self, sName: str) -> None:
        self._sName = sName.upper()
    @DOB.setter
    def DOB(self, sDOB: str) -> None:
        self._sDOB = sDOB.replace("-", "").replace("/", "")
        self._nDOB = self._sDOB

    # Helper functions
    def _char_to_int(self, sCharacter: str) -> int:
        if sCharacter.isalpha():
            return ((ord(sCharacter.upper()) - 65) % 9) + 1
        return 0
    def _reduce_number(self, iNumber: int) -> int:
        while iNumber > 9:
            iNumber = (iNumber % 10) + (iNumber // 10)
        return iNumber

    # Use the properties to access the variables
    @property
    def LifePath(self) -> int:
        return self.__iLifePathNumber
    @property
    def BirthDay(self) -> int:
        return self.__iBirthdayNumber
    @property
    def Attitude(self) -> int:
        return self.__iAttitudeNumber
    @property
    def Soul(self) -> int:
        return self.__iSoulNumber
    @property
    def Personality(self) -> int:
        return self.__iPersonalityNumber
    @property
    def PowerName(self) -> int:
        return self.__iPowerName
    @property
    def LifePathDescription(self) -> str:
        descriptions = {
            1: "The Independent: Wants to work/think for themselves ~ BOSS*",
            2: "The Mediator: Avoids conflict and wants love and harmony ~ PEACEMAKER*",
            3: "The Performer: Likes music, art and to perform or get attention ~ STAR*",
            4: "The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful ~ GUIDE*",
            5: "The Adventurer: Likes to travel and meet others, often an extrovert ~ EXPLORER*",
            6: "The Inner Child: Is meant to be a parent and/or one that is young at heart ~ NURTURER*",
            7: "The Naturalist: Enjoy nature and water and alternative life paths, open to spirituality ~ MYSTIC*",
            8: "The Executive: Gravitates to money and power ~ LEADER*",
            9: "The Humanitarian: Helps others and/or experiences pain and learns the hard way ~ HEALER*",
        }
        return descriptions.get(self.LifePath, "Unknown Life Path")

    # String function displays the results
    def __str__(self) -> str:
        return (
            f"Test Name: {self.Name}\n"
            f"Test DOB: {self.DOB[:2]}/{self.DOB[2:4]}/{self.DOB[4:]}\n"
            f"Life Path Number: {self.LifePath}\n"
            f"Birth Day Number: {self.BirthDay}\n"
            f"Attitude Number: {self.Attitude}\n"
            f"Soul Number: {self.Soul}\n"
            f"Personality Number: {self.Personality}\n"
            f"Power Name Number: {self.PowerName}\n"
            f"Life Path Description: {self.LifePathDescription}"
        )
