from pymysql import connect


class JD(object):
    def __init__(self):
        # 创建Connection连接
        self.conn = connect(host='localhost', port=3306, user='root', password='333120@Wjs', database='jing_dong',
                       charset='utf8')
        # 获得Cursor对象
        self.cursor = self.conn.cursor()

    def __del__(self):
        # 关闭Cursor对象
        self.cursor.close()
        # 关闭Connection对象
        self.conn.close()

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_items(self):
        """显示所有商品"""

        sql = "select * from goods;"
        self.execute_sql(sql)

    def show_all_cates(self):
        """显示所有商品分类"""

        sql = "select cate_name as 商品分类 from goods group by cate_name;"
        self.execute_sql(sql)

    def show_all_brands(self):
        """显示所有商品品牌分类"""
        sql = "select brand_name as 品牌分类 from goods group by brand_name;"
        self.execute_sql(sql)

    @staticmethod
    def print_menu():
        print("====京东商城====")
        print("1：所有商品")
        print("2：所有商品分类")
        print("3：所有商品品牌分类")
        return input("请输入功能对应的序号：")

    def run(self):
        while True:
            num = self.print_menu()
            if num == "1":
                # 查询所有商品
                self.show_all_items()
            elif num == "2":
                # 所有商品分类
                self.show_all_cates()
            elif num == "3":
                # 所有商品品牌分类
                self.show_all_brands()
            else:
                print("输入有误，请正确输入...")


def main():
    # 1.创建一个京东商城对象
    jd = JD()
    # 2.调用这个对象的run方法，让其运行
    jd.run()


if __name__ == '__main__':
    main()
