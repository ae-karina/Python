import sys


def sys_update():  # 更新
    while 1:
        c = input("Please input 'back' to back to Home Page:")
        if c == 'back':
            Home_Page()
        else:
            ID2 = int(input("Please input the student's ID you want to update:"))
            if ID2 in stu_inf:  # 如果在字典里
                name2 = input("Please input the student's name you want to update:")
                stu_inf.update({ID2: name2})
                si_choice = int(input("The updating is successful, please choose to continue updating or return to the "
                                      "Home "
                                      "Page.  1:Continue 2:Back to Home Page"))
                if si_choice == 1:
                    continue
                else:
                    Home_Page()
            else:
                se_choice = int(input("This student is not in the stu-inf, do you want to add him or back to Home "
                                      "Page? "
                                      "1:Add 2:Back to Home Page"))
                if se_choice == 1:
                    sys_add()
                else:
                    Home_Page()


def sys_add():  # 添加
    while 1:
        c = input(
            "Please input 'back' to back to Home Page:")  #
        # 由于后面的步骤过长，为避免用户不小心按错选择不得不把某些程序执行完毕才可返回主界面，导致一些不必要的操作，故在每段程序开头之前加了该语句
        if c == 'back':
            Home_Page()
        else:
            ID = int(input("Please input the student's ID you want to add:"))

            if ID in stu_inf:  # 若在字典里
                sec_choice = int(input("The student is already in this stu_inf,do you want to update him? Please input "
                                       "your "
                                       "choice: 1:yes,2:no"))  # 询问是想更新该数据
                if sec_choice == 1:
                    name1 = input("Please input the student's name you want to update :")
                    stu_inf.update({ID: name1})
                    th_choice = int(
                        input("You want to continue to add or back to the Home Page 1:continue 2:Back Home Page"))
                    if th_choice == 1:
                        continue
                    else:
                        Home_Page()

                elif sec_choice == 2:
                    fo_choice = int(input("You can choose to continue to add other students’ information or return to "
                                          "the "
                                          "Home Page. 1:Keep adding 2: Back to Home Page"))
                    if fo_choice == 1:
                        continue
                    else:
                        Home_Page()
            else:
                name = input("Please input the student's name you want to add:")
                stu_inf[ID] = name
                fi_choice = int(input("The addition is successful, please choose to continue adding or return to the "
                                      "Home "
                                      "Page.  1:continue 2:Back to Home Page"))
                if fi_choice == 1:
                    continue
                else:
                    Home_Page()


def sys_delete():  # 删除
    while 1:
        c = input("Please input 'back' to back to Home Page:")
        if c == 'back':
            Home_Page()
        else:
            ID3 = int(input("Please input the student's ID you want to delete:"))
            if ID3 in stu_inf:
                stu_inf.pop(ID3)
                ei_choice = int(input("The delete is successful, please choose to continue deleting or return to the "
                                      "Home "
                                      "Page.  1:Continue 2:Back to Home Page"))  # 执行成功之后可以返回主界面继续要做的选择，其他的版块设计类似
                if ei_choice == 1:
                    continue
                else:
                    Home_Page()
            else:
                ni_choice = int(input("This student is not in the stu-inf, do you want to add him or back to Home "
                                      "Page? "
                                      "1:Add 2:Back to Home Page"))
                if ni_choice == 1:
                    sys_add()
                else:
                    Home_Page()


def sys_query():  # 查询
    while 1:
        c = input("Please input 'back' to back to Home Page:")
        if c == 'back':
            Home_Page()
        else:
            ID4 = int(input("Please input the student's ID you want to query:"))
            if ID4 in stu_inf:
                print(ID4, stu_inf.setdefault(ID4))
                te_choice = int(input("The query is successful, please choose to continue querying or return to the "
                                      "Home "
                                      "Page.  1:Continue 2:Back to Home Page"))
                if te_choice == 1:
                    continue
                else:
                    Home_Page()
            else:
                el_choice = int(input("This student is not in the stu-inf, do you want to add him or back to Home "
                                      "Page? "
                                      "1:Add 2:Back to Home Page"))
                if el_choice == 1:
                    sys_add()
                else:
                    Home_Page()


def sys_show():  # 展示
    c = input("Please input 'back' to back to Home Page:")
    if c == 'back':
        Home_Page()
    else:
        for key, value in stu_inf.items():
            print(key, ":", value)
        Home_Page()


def Home_Page():  # 主页面
    print("Welcome to Student Management System !")
    print("$************************************$")
    print("$             1、UPDATE              $")
    print("$             2、ADD                 $")
    print("$             3、DELETE              $")
    print("$             4、QUERY               $")
    print("$             5、SHOW                $")
    print("$             6、EXIT                $")
    print("$************************************$")
    choice = int(input("Please select the action you want to perform: "))

    if choice == 1:
        sys_update()
    elif choice == 2:
        sys_add()
    elif choice == 3:
        sys_delete()
    elif choice == 4:
        sys_query()
    elif choice == 5:
        sys_show()
    elif choice == 6:
        print("Thank you for using!")
        sys.exit()


stu_inf = {}
Home_Page()
