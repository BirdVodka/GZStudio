edges = input("请输入此多边形的边数")
if int(edges) >= int(3):
  anglesum = (int(edges) - int(2)) * int(180)
  print('此多边形的内角和为' + str(anglesum) + "度")
else:
  print("！！！边数至少为三条！！！")
input()