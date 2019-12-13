from pymysql import connect


def main():
    conn = connect(host='localhost', port=3306, user='root', password='333120@Wjs', database='jing_dong', charset='utf8')

    cursor = conn.cursor()

    # cursor.fetchmany()

    user_select = int(input("请输入你要查询的信息\n1.查询种类\n2.查询品牌\n"))

    if user_select == 1:
        user_select1 = "select cate_name as 种类名称 from goods group by cate_name"
        s1 = cursor.execute(user_select1)
        print(s1)
    else:
        user_select2 = "select brand_name as 品牌名称 from goods group by brand_name"
        s2 = cursor.execute(user_select2)
        print(s2)

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
