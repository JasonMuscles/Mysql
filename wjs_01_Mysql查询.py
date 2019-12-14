from pymysql import connect


class JD(object):
    def __init__(self):
        pass

    def show_all_items(self):
        """显示所有商品"""
        # 创建Connection连接
        conn = connect(host='localhost', port=3306, user='root', password='333120@Wjs', database='jing_dong', charset='utf8')
        # 获得Cursor对象
        cursor = conn.cursor()
        sql = "select * from goods;"
        cursor.execute(sql)

        for temp in cursor.fetchmany():
            print(temp)
        # 关闭Cursor对象
        cursor.close()
        # 关闭Connection对象
        conn.close()

    def show_all_cates(self):
        """显示所有商品分类"""
        # 创建Connection连接
        conn = connect(host='localhost', port=3306, user='root', password='333120@Wjs', database='jing_dong', charset='utf8')
        # 获得Cursor对象
        cursor = conn.cursor()
        sql = "select brand_name as 品牌 from goods group by brand_name;"
        cursor.execute(sql)

        for temp in cursor.fetchmany():
            print(temp)
        # 关闭Cursor对象
        cursor.close()
        # 关闭Connection对象
        conn.close()

    def show_all_brand(self):
        """显示所有商品品牌分类"""
        pass

    def run(self):
        while True:
            print("====京东商城====")
            print("1：所有商品")
            print("2：所有商品分类")
            print("3：所有商品品牌分类")
            num = input("请输入功能对应的序号：")
            if num == "1":
                # 查询所有商品
                self.show_all_items()
            elif num == "2":
                # 所有商品分类
                self.show_all_cates()
            elif num == "3":
                # 所有商品品牌分类
                pass
            else:
                print("输入有误，请正确输入...")


def main():
    # 1.创建一个京东商城对象
    jd = JD()
    # 2.调用这个对象的run方法，让其运行
    jd.run()


if __name__ == '__main__':
    main()
