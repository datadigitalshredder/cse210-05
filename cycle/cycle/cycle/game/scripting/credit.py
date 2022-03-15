class Credit:
    """
    An update that displays the game contibutors when the game is over.
    
    The responsibility of Credit is to display the team that contributed to the game.
    """

    def __init__(self):
        """Constructs a new instance of Credit.
        """
        self._name1 = "Davi Ferreira do Vale"
        self._name2 = "Innocent Hove"
        self._name3 = "Ryan Alvord"
        self._name4 = "Cooper Featherstone"
        self._name5 = "Njato Harizo"
        pass

    def getCredits(self):
        """Sets the contributors flag below game over flag if the snake collides with one of its segments (game over).
        """
        return f"Updated by: {self._name1},\n{self._name2}, {self._name3},\n{self._name4}, {self._name5}"
        


        