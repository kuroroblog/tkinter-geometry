import tkinter as tk

class Application(tk.Frame):
    # アプリ画面(Window)の位置や大きさを設定するサンプル関数
    def getSample(self):
        # アプリ画面(Window)の位置や大きさを設定する。
        # アプリ画面(Window)の幅 : 300
        # アプリ画面(Window)の高さ : 200
        # パソコン画面の左上隅を原点(0, 0)とした、x座標 : 120
        # パソコン画面の左上隅を原点(0, 0)とした、y座標 : 0
        self.master.geometry("300x200+120+0")

    # アプリ画面(Window)の位置、大きさを取得する関数
    def getSize(self):
        print(self.master.geometry())
        print(self.master.winfo_width())
        print(self.master.winfo_height())
        print(self.master.winfo_x())
        print(self.master.winfo_y())
        print(self.master.winfo_screenwidth())
        print(self.master.winfo_screenheight())

    # アプリ画面(Window)の位置を右上へ表示する関数
    def getRightUpApp(self):
        # アプリ画面(Window)の幅
        width = 300
        # アプリ画面(Window)の高さ
        height = 200
        # パソコン画面の幅を取得
        w = self.master.winfo_screenwidth()
        # 幅調整offset
        # offsetとは? : https://e-words.jp/w/%E3%82%AA%E3%83%95%E3%82%BB%E3%83%83%E3%83%88.html#:~:text=%E3%82%AA%E3%83%95%E3%82%BB%E3%83%83%E3%83%88%20%E3%80%90offset%E3%80%91,%E3%82%AA%E3%83%95%E3%82%BB%E3%83%83%E3%83%88%E3%81%A8%E3%81%84%E3%81%86%E3%81%93%E3%81%A8%E3%81%8C%E5%A4%9A%E3%81%84%E3%80%82
        w = w - width
        self.master.geometry(str(width)+"x"+str(height)+"+"+str(w)+"+0")

    # アプリ画面(Window)の位置を右下へ表示する関数
    def getRightBottomApp(self):
        # アプリ画面(Window)の幅
        width = 300
        # アプリ画面(Window)の高さ
        height = 200
        # パソコン画面の幅を取得
        w = self.master.winfo_screenwidth()
        # パソコン画面の高さを取得
        h = self.master.winfo_screenheight()
        # 幅調整offset
        # offsetとは? : https://e-words.jp/w/%E3%82%AA%E3%83%95%E3%82%BB%E3%83%83%E3%83%88.html#:~:text=%E3%82%AA%E3%83%95%E3%82%BB%E3%83%83%E3%83%88%20%E3%80%90offset%E3%80%91,%E3%82%AA%E3%83%95%E3%82%BB%E3%83%83%E3%83%88%E3%81%A8%E3%81%84%E3%81%86%E3%81%93%E3%81%A8%E3%81%8C%E5%A4%9A%E3%81%84%E3%80%82
        w = w - width
        # 高さ調整offset。
        # offsetとは? : https://e-words.jp/w/%E3%82%AA%E3%83%95%E3%82%BB%E3%83%83%E3%83%88.html#:~:text=%E3%82%AA%E3%83%95%E3%82%BB%E3%83%83%E3%83%88%20%E3%80%90offset%E3%80%91,%E3%82%AA%E3%83%95%E3%82%BB%E3%83%83%E3%83%88%E3%81%A8%E3%81%84%E3%81%86%E3%81%93%E3%81%A8%E3%81%8C%E5%A4%9A%E3%81%84%E3%80%82
        h = h - height
        self.master.geometry(str(width)+"x"+str(height)+"+"+str(w)+"+"+str(h))

    # アプリ画面(Window)の位置を左下へ表示する関数
    def getLeftBottomApp(self):
        # アプリ画面(Window)の幅
        width = 300
        # アプリ画面(Window)の高さ
        height = 200
        # パソコン画面の高さを取得
        h = self.master.winfo_screenheight()
        # 高さ調整offset。
        # offsetとは? : https://e-words.jp/w/%E3%82%AA%E3%83%95%E3%82%BB%E3%83%83%E3%83%88.html#:~:text=%E3%82%AA%E3%83%95%E3%82%BB%E3%83%83%E3%83%88%20%E3%80%90offset%E3%80%91,%E3%82%AA%E3%83%95%E3%82%BB%E3%83%83%E3%83%88%E3%81%A8%E3%81%84%E3%81%86%E3%81%93%E3%81%A8%E3%81%8C%E5%A4%9A%E3%81%84%E3%80%82
        h = h - height
        self.master.geometry(str(width)+"x"+str(height)+"+0"+"+"+str(h))

    # アプリ画面(Window)の位置を左上へ表示する関数
    def getLeftUpApp(self):
        # アプリ画面(Window)の幅
        width = 300
        # アプリ画面(Window)の高さ
        height = 200
        self.master.geometry(str(width)+"x"+str(height)+"+0+0")

    # アプリ画面(Window)をパソコン画面全体へ表示する関数
    def getZoomUp(self):
        # pattern1
        # パソコン画面の幅を取得
        w = self.master.winfo_screenwidth()
        # パソコン画面の高さを取得
        h = self.master.winfo_screenheight()
        self.master.geometry(str(w)+"x"+str(h)+"+0"+"+0")

        # pattern2
        # self.master.state('zoomed')

        # pattern3
        # attributesについて : https://kuroro.blog/python/tJyCah49cYKRAQAFohsi/
        # self.master.attributes('-fullscreen', True)

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # self.getSample()
        # self.getSize()

        # self.getRightUpApp()
        # self.getRightBottomApp()
        # self.getLeftBottomApp()
        # self.getLeftUpApp()
        # self.getZoomUp()

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
