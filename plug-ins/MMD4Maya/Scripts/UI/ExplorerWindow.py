try:
    from PySide6 import QtWidgets
except ImportError:
    from PySide2 import QtWidgets
from MMD4Maya.Scripts.Utils import *

import pymel.util.path as pmp

class ExplorerWindow(object): # QMainWindowの継承をやめる
    @staticmethod
    def show_dialog(parent=None, type='pmd', mainWindow=None):
        """
        ウィンドウを表示せず、直接ファイルダイアログを呼び出す
        """
        # フィルタとタイトルの設定
        if type == 'pmd':
            file_filter = "MMD Model Files (*.pmd *.pmx);;All Files (*.*)"
            title = "モデルファイルを選択 (.pmd / .pmx)"
        else:
            file_filter = "MMD Motion Files (*.vmd);;All Files (*.*)"
            title = "モーションファイルを選択 (.vmd)"

        # ダイアログを表示
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            parent,
            title,
            "C:/",
            file_filter
        )

        # ファイルが選択された場合の処理
        if file_path and mainWindow:
            path = pmp(file_path).normpath()
            if type == 'pmd':
                mainWindow.SetPmxFile(path)
            elif type == 'vmd':
                mainWindow.AddVmdFile(path)