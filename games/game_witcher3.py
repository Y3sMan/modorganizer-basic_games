# -*- encoding: utf-8 -*-

from PyQt5.QtCore import QDir


from ..basic_game import BasicGame


class Witcher3Game(BasicGame):

    Name: str = "Witcher 3 Support Plugin"
    Author: str = "Holt59"
    Version: str = "1.0.0a"
    Description: str = "The Description Of The Dead"

    GameName: str = "The Witcher 3"
    GameShortName: str = "witcher3"
    GameBinary: str = "bin/x64/witcher3.exe"
    GameDataPath: str = "Mods"
    GameSaveExtension: str = "sav"
    GameSteamId = 292030

    def savesDirectory(self):
        return QDir(self.documentsDirectory().absoluteFilePath("gamesaves"))
