
while  True:
	num = float(input("学生课堂表现怎么样？\n1.专心\n2.不专心"))
	if num == 1 or 2:
	  if num == 2:
	    import random
	    ktbxa = []
	    ktbxb = []
	    with open("ktbx2.txt", "r", encoding="utf-8") as fr:
	        ktbxa = fr.readlines()
	        for i in ktbxa:
	            temp_line = i.strip()   # 去除每行的\n
	            ktbxb.append(temp_line)
	    pinyu1 = random.randint(0, len(ktbxb)-1)
	  else:
	    import random
	    ktbxa = []
	    ktbxb = []
	    with open("ktbx1.txt", "r", encoding="utf-8") as fr:
	        ktbxa = fr.readlines()
	        for i in ktbxa:
	            temp_line = i.strip()   # 去除每行的\n
	            ktbxb.append(temp_line)
	    pinyu1 = random.randint(0, len(ktbxb)-1)
	else:
	  print("请输入数字1或者2")


	num = float(input("学生课堂发言情况怎么样？\n1.积极发言\n2.发言不积极"))
	if num == 1 or 2:
	  if num == 2:
	    import random
	    ktfya = []
	    ktfyb = []
	    with open("ktfy2.txt", "r", encoding="utf-8") as fr:
	        ktfya = fr.readlines()
	        for i in ktfya:
	            temp_line = i.strip()   # 去除每行的\n
	            ktfyb.append(temp_line)
	    pinyu2 = random.randint(0, len(ktfyb)-1)
	  else:
	    import random
	    ktfya = []
	    ktfyb = []
	    with open("ktfy1.txt", "r", encoding="utf-8") as fr:
	        ktfya = fr.readlines()
	        for i in ktfya:
	            temp_line = i.strip()   # 去除每行的\n
	            ktfyb.append(temp_line)
	    pinyu2 = random.randint(0, len(ktfyb)-1)
	else:
	  print("请输入数字1或者2")


	num = float(input("学生纪律遵守情况怎么样？\n1.好\n2.不好"))
	if num == 1 or 2:
	  if num == 2:
	    import random
	    jla = []
	    jlb = []
	    with open("jl2.txt", "r", encoding="utf-8") as fr:
	        jla = fr.readlines()
	        for i in jla:
	            temp_line = i.strip()   # 去除每行的\n
	            jlb.append(temp_line)
	    pinyu3 = random.randint(0, len(jlb)-1)
	  else:
	    import random
	    jla = []
	    jlb = []
	    with open("jl1.txt", "r", encoding="utf-8") as fr:
	        jla = fr.readlines()
	        for i in jla:
	            temp_line = i.strip()   # 去除每行的\n
	            jlb.append(temp_line)
	    pinyu3 = random.randint(0, len(jlb)-1)
	else:
	  print("请输入数字1或者2")
	  


	num = float(input("学生作业完成情况怎么样？\n1.没有拖欠\n2.有拖欠"))
	if num == 1 or 2:
	  if num == 2:
	    import random
	    zya = []
	    zyb = []
	    with open("zy2.txt", "r", encoding="utf-8") as fr:
	        zya = fr.readlines()
	        for i in zya:
	            temp_line = i.strip()   # 去除每行的\n
	            zyb.append(temp_line)
	    pinyu4 = random.randint(0, len(zyb)-1)
	  else:
	    import random
	    zya = []
	    zyb = []
	    with open("zy1.txt", "r", encoding="utf-8") as fr:
	        zya = fr.readlines()
	        for i in zya:
	            temp_line = i.strip()   # 去除每行的\n
	            zyb.append(temp_line)
	    pinyu4 = random.randint(0, len(zyb)-1)
	else:
	  print("请输入数字1或者2")

	num = float(input("学生是不是班干部？\n1.是\n2.不是"))
	if num == 1 or 2:
	  if num == 2:
	    import random
	    bgba = []
	    bgbb = []
	    with open("bgb2.txt", "r", encoding="utf-8") as fr:
	        bgba = fr.readlines()
	        for i in bgba:
	            temp_line = i.strip()   # 去除每行的\n
	            bgbb.append(temp_line)
	    pinyu5 = random.randint(0, len(bgbb)-1)

	  else:
	    import random
	    bgba = []
	    bgbb = []
	    with open("bgb1.txt", "r", encoding="utf-8") as fr:
	        bgba = fr.readlines()
	        for i in bgba:
	            temp_line = i.strip()   # 去除每行的\n
	            bgbb.append(temp_line)
	    pinyu5 = random.randint(0, len(bgbb)-1)
	else:
	  print("请输入数字1或者2")



	num = float(input("学生的学习成绩怎么样？\n1.好\n2.一般\n3.不好"))
	if num == 1 or 2 or 3:
	  if num == 2:
	    import random
	    cja = []
	    cjb = []
	    with open("cj2.txt", "r", encoding="utf-8") as fr:
	        cja = fr.readlines()
	        for i in cja:
	            temp_line = i.strip()   # 去除每行的\n
	            cjb.append(temp_line)
	    pinyu6 = random.randint(0, len(cjb)-1)
	  if num == 3:
	    import random
	    cja = []
	    cjb = []
	    with open("cj3.txt", "r", encoding="utf-8") as fr:
	        cja = fr.readlines()
	        for i in cja:
	            temp_line = i.strip()   # 去除每行的\n
	            cjb.append(temp_line)
	    pinyu6 = random.randint(0, len(cjb)-1)
	  else:
	    import random
	    cja = []
	    cjb = []
	    with open("cj1.txt", "r", encoding="utf-8") as fr:
	        cja = fr.readlines()
	        for i in cja:
	            temp_line = i.strip()   # 去除每行的\n
	            cjb.append(temp_line)
	    pinyu6 = random.randint(0, len(cjb)-1)
	else:
	  print("请输入数字1或者2或者3")



	num = float(input("最后对学生有啥期望？\n1.稳住现状\n2.需要更加努力"))
	if num == 1 or 2:
	  if num == 2:
	    import random
	    qwa = []
	    qwb = []
	    with open("qw2.txt", "r", encoding="utf-8") as fr:
	        qwa = fr.readlines()
	        for i in qwa:
	            temp_line = i.strip()   # 去除每行的\n
	            qwb.append(temp_line)
	    pinyu7 = random.randint(0, len(qwb)-1)
	  else:
	    import random
	    qwa = []
	    qwb = []
	    with open("qw1.txt", "r", encoding="utf-8") as fr:
	        qwa = fr.readlines()
	        for i in qwa:
	            temp_line = i.strip()   # 去除每行的\n
	            qwb.append(temp_line)
	    pinyu7 = random.randint(0, len(qwb)-1)
	else:
	  print("请输入数字1或者2")



	print("\n\n\n最后评语生成中：")
	print("\n\n__"+ktbxb[pinyu1]+ktfyb[pinyu2]+jlb[pinyu3]+zyb[pinyu4]+bgbb[pinyu5]+cjb[pinyu6]+qwb[pinyu7]+"\n\n\n\n")

	import time
	time.sleep(3)