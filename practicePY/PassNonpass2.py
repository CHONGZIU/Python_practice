class Score:
    def pnp(self, a): # selfはインスタンス自信を扱うために使わなきゃならない
        if a.isalpha() or int(a) < 80 or int(a) >= 100:
            return self.pnp(input("点数を入力してください"))
        else:
            print("合格")
