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

    # アプリ画面(Window)の位置や大きさを取得する関数
    # パソコン画面の幅・高さを取得する関数
    def getSize(self):
        # .winfo_geometry()でも可
        # アプリ画面(Window)の位置や大きさを取得する関数
        print(self.master.geometry())
        # アプリ画面(Window)の幅を取得する関数
        print(self.master.winfo_width())
        # アプリ画面(Window)の高さを取得する関数
        print(self.master.winfo_height())
        # パソコン画面の左上隅を原点(0, 0)とした、x座標を取得する関数
        print(self.master.winfo_x())
        # パソコン画面の左上隅を原点(0, 0)とした、x座標を取得する関数
        print(self.master.winfo_y())

        # パソコン画面の幅を取得する関数
        print(self.master.winfo_screenwidth())
        # パソコン画面の高さを取得する関数
        print(self.master.winfo_screenheight())

    # アプリ画面(Window)の位置を右上へ表示する関数
    def getRightUpApp(self):
        # アプリ画面(Window)の幅
        width = 300
        # アプリ画面(Window)の高さ
        height = 200
        # パソコン画面の幅を取得
        pcW = self.master.winfo_screenwidth()
        x = pcW - width
        self.master.geometry(str(width)+"x"+str(height)+"+"+str(x)+"+0")

    # アプリ画面(Window)の位置を右下へ表示する関数
    def getRightBottomApp(self):
        # アプリ画面(Window)の幅
        width = 300
        # アプリ画面(Window)の高さ
        height = 200
        # パソコン画面の幅を取得
        pcW = self.master.winfo_screenwidth()
        # パソコン画面の高さを取得
        pcH = self.master.winfo_screenheight()
        x = pcW - width
        y = pcH - height
        self.master.geometry(str(width)+"x"+str(height)+"+"+str(x)+"+"+str(y))

    # アプリ画面(Window)の位置を左下へ表示する関数
    def getLeftBottomApp(self):
        # アプリ画面(Window)の幅
        width = 300
        # アプリ画面(Window)の高さ
        height = 200
        # パソコン画面の高さを取得
        pcH = self.master.winfo_screenheight()
        y = pcH - height
        self.master.geometry(str(width)+"x"+str(height)+"+0"+"+"+str(y))

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
        # -fullscreen : アプリ画面(Window)を画面いっぱいに表示させるかどうかを設定。True(画面いっぱいにアプリ画面(Window)を表示する), False(画面いっぱいにアプリ画面(Window)を表示しない)
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
    # Windowを生成する。
    # Windowについて : https://kuroro.blog/python/116yLvTkzH2AUJj8FHLx/
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
