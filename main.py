import speedtest
import ping3
import time
import statistics
from datetime import datetime
import threading


class NetworkSpeedTester:
    def __init__(self):
        self.speed_test = speedtest.Speedtest()
        self.results = {
            'ping': [],
            'download': [],
            'upload': [],
            'jitter': [],
            'packet_loss': 0
        }
        self.test_count = 0

    def test_ping(self, host='8.8.8.8', count=10):
        """测试ping延迟和抖动"""
        delays = []
        for i in range(count):
            try:
                delay = ping3.ping(host, timeout=2)
                if delay is not None:
                    delays.append(delay * 1000)  # 转换为毫秒
                    print(f"Ping #{i + 1}: {delay * 1000:.2f} ms")
                else:
                    print(f"Ping #{i + 1}: 超时")
            except Exception as e:
                print(f"Ping测试错误: {e}")

            time.sleep(0.5)

        if delays:
            avg_ping = statistics.mean(delays)
            jitter = statistics.stdev(delays) if len(delays) > 1 else 0
            self.results['ping'].append(avg_ping)
            self.results['jitter'].append(jitter)
            return avg_ping, jitter
        return None, None

    def test_speed(self):
        """测试下载和上传速度"""
        try:
            print("正在测试下载速度...")
            download_speed = self.speed_test.download() / 1024 / 1024  # 转换为Mbps
            print("正在测试上传速度...")
            upload_speed = self.speed_test.upload() / 1024 / 1024  # 转换为Mbps

            self.results['download'].append(download_speed)
            self.results['upload'].append(upload_speed)

            return download_speed, upload_speed
        except Exception as e:
            print(f"速度测试错误: {e}")
            return None, None

    def packet_loss_test(self, host='8.8.8.8', count=20):
        """测试丢包率"""
        lost_count = 0
        for i in range(count):
            try:
                result = ping3.ping(host, timeout=1)
                if result is None:
                    lost_count += 1
                    print(f"数据包 #{i + 1}: 丢失")
                else:
                    print(f"数据包 #{i + 1}: 收到回复 ({result * 1000:.2f} ms)")
            except:
                lost_count += 1

            time.sleep(0.2)

        packet_loss_rate = (lost_count / count) * 100
        self.results['packet_loss'] = packet_loss_rate
        return packet_loss_rate

    def run_complete_test(self, duration_minutes=5, interval_seconds=60):
        """运行完整的网络稳定性测试"""
        print("=" * 50)
        print("开始网络稳定性测试")
        print(f"测试时长: {duration_minutes} 分钟")
        print(f"测试间隔: {interval_seconds} 秒")
        print("=" * 50)

        end_time = time.time() + duration_minutes * 60
        test_number = 1

        while time.time() < end_time:
            print(f"\n🔍 第 {test_number} 次测试 - {datetime.now().strftime('%H:%M:%S')}")
            print("-" * 30)

            # Ping测试
            avg_ping, jitter = self.test_ping()
            if avg_ping is not None:
                print(f"平均 Ping: {avg_ping:.2f} ms")
                print(f"抖动(Jitter): {jitter:.2f} ms")

            # 速度测试（每隔几次测试一次，因为比较耗时）
            if test_number % 2 == 1:  # 每隔一次测试速度
                download, upload = self.test_speed()
                if download is not None:
                    print(f"下载速度: {download:.2f} Mbps")
                    print(f"上传速度: {upload:.2f} Mbps")

            # 每5次测试一次丢包率
            if test_number % 5 == 0:
                packet_loss = self.packet_loss_test(count=10)
                print(f"丢包率: {packet_loss:.1f}%")

            self.test_count += 1
            test_number += 1

            # 等待下一次测试
            if time.time() + interval_seconds < end_time:
                print(f"\n等待下一次测试... ({interval_seconds}秒后)")
                time.sleep(interval_seconds)

    def generate_report(self):
        """生成测试报告"""
        print("\n" + "=" * 60)
        print("📊 网络测试最终报告")
        print("=" * 60)

        if self.results['ping']:
            avg_ping = statistics.mean(self.results['ping'])
            max_ping = max(self.results['ping'])
            min_ping = min(self.results['ping'])
            avg_jitter = statistics.mean(self.results['jitter'])

            print(f"平均 Ping: {avg_ping:.2f} ms")
            print(f"最低 Ping: {min_ping:.2f} ms")
            print(f"最高 Ping: {max_ping:.2f} ms")
            print(f"平均抖动: {avg_jitter:.2f} ms")

            # Ping稳定性评估
            if avg_jitter < 5:
                ping_stability = "极稳定"
            elif avg_jitter < 15:
                ping_stability = "稳定"
            elif avg_jitter < 30:
                ping_stability = "一般"
            else:
                ping_stability = "不稳定"
            print(f"网络稳定性: {ping_stability}")

        if self.results['download']:
            avg_download = statistics.mean(self.results['download'])
            avg_upload = statistics.mean(self.results['upload'])
            print(f"平均下载速度: {avg_download:.2f} Mbps")
            print(f"平均上传速度: {avg_upload:.2f} Mbps")

        print(f"丢包率: {self.results['packet_loss']:.1f}%")

        # 总体评估
        print("\n📈 总体评估:")
        if self.results['packet_loss'] > 10:
            print("❌ 网络质量: 差 (高丢包率)")
        elif avg_jitter > 50:
            print("⚠️  网络质量: 一般 (高抖动)")
        else:
            print("✅ 网络质量: 良好")

        print(f"总测试次数: {self.test_count}")
        print("=" * 60)


# 快速测试函数
def quick_test():
    """快速网络测试"""
    tester = NetworkSpeedTester()

    print("🚀 开始快速网络测试...")
    print("测试Ping和抖动...")
    ping, jitter = tester.test_ping(count=5)

    print("\n测试下载速度...")
    download, upload = tester.test_speed()

    print("\n测试丢包率...")
    packet_loss = tester.packet_loss_test(count=10)

    print("\n📋 快速测试结果:")
    print(f"Ping: {ping:.2f} ms" if ping else "Ping: 测试失败")
    print(f"抖动: {jitter:.2f} ms" if jitter else "抖动: 测试失败")
    print(f"下载: {download:.2f} Mbps" if download else "下载: 测试失败")
    print(f"上传: {upload:.2f} Mbps" if upload else "上传: 测试失败")
    print(f"丢包率: {packet_loss:.1f}%")


if __name__ == "__main__":
    # 安装所需库: pip install speedtest-cli ping3

    print("🌐 Python网络测速工具")
    print("1. 快速测试")
    print("2. 稳定性测试 (5分钟)")
    print("3. 自定义测试")

    choice = input("请选择测试模式 (1/2/3): ").strip()

    tester = NetworkSpeedTester()

    if choice == "1":
        quick_test()
    elif choice == "2":
        tester.run_complete_test(duration_minutes=5, interval_seconds=30)
        tester.generate_report()
    elif choice == "3":
        duration = int(input("测试时长(分钟): "))
        interval = int(input("测试间隔(秒): "))
        tester.run_complete_test(duration_minutes=duration, interval_seconds=interval)
        tester.generate_report()
    else:
        print("开始默认快速测试...")
        quick_test()