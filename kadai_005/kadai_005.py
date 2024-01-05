# 四則演算で台形の面積を求める #
jyouhen = 10  #上辺
kahen = 20    #下辺
takasa = 5    #高さ
kousiki = "公式：台形の面積 =（上辺＋下辺）× 高さ ÷ 2"
senchi = "cm"

print("上辺：" + str(jyouhen) + senchi)
print("下辺：" + str(kahen) + senchi)
print("高さ：" + str(takasa) + senchi)
print(kousiki)
menseki = (jyouhen + kahen) * takasa / 2
print("台形の面積：" + str(int(menseki)) + "㎠")