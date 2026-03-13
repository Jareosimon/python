import time
import sys

def romantic_words():
    """动态输出浪漫语句，模拟打字机效果"""
    words = [
        "在Python的世界里，",
        "我用0和1编织温柔，",
        "用循环书写偏爱，",
        "用条件判断确认——",
        "你是我唯一的return值 ❤️"
    ]
    
    # 打字机效果输出每一句话
    for sentence in words:
        for char in sentence:
            sys.stdout.write(char)
            sys.stdout.flush()  # 强制刷新输出
            time.sleep(0.1)     # 每个字间隔0.1秒，营造打字感
        print()
        time.sleep(0.5)         # 每句话间隔0.5秒

def main():
    """主函数：组合浪漫效果"""
    print("\n" * 2)  # 空两行，让画面更美观
    print("✨ 写给你的浪漫代码 ✨")
    print("-" * 20)
    time.sleep(1)    # 延迟1秒，增加期待感
    
    
    
    #输出浪漫语句
    romantic_words()
    print("\n" + "-" * 20)
    print("💌 这份浪漫，由Python为你专属生成 💌")

if __name__ == "__main__":
    main()