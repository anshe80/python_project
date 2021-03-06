from app_jiao_ben import AppReadBase
import random
import uiautomator2
import time


class KuaiShou(AppReadBase):
    def __init__(self, phone_serial, pp):
        super(KuaiShou, self).__init__(phone_serial, pp)
        # self.pp = uiautomator2.connect_usb()
        self.pp.watcher('tip1').when('我知道了').click()
        self.pp.watcher('tip2').when(xpath='//*[@resource-id="com.kuaishou.nebula:id/img_nebula_pull_new_dialog"]') \
            .press('back')
        self.pp.watcher.start(0.5)

    def sign_in(self):
        self.logger.info(f'开始签到')
        self.pp(resourceId='com.kuaishou.nebula:id/left_btn').click(offset=(random.random(), random.random()))
        self.pp(text='去赚钱').wait()
        self.click_random_position(self.pp.xpath('//*[@resource-id="com.kuaishou.nebula:id/menu_recycler_view"]/'
                                                 'android.view.ViewGroup[2]').get().bounds)
        self.pp(description='活动规则').wait()
        if self.pp(description='今天已签').exists(timeout=3):
            self.pp.press('back')
            time.sleep(random.random() + 1)
        self.pp.press('back')
        time.sleep(random.random() + 1)

    def today_coin(self):
        self.logger.info('获取今日金币数量')
        self.pp(resourceId='com.kuaishou.nebula:id/left_btn').click(offset=(random.random(), random.random()))
        self.pp(text='去赚钱').wait()
        self.click_random_position(self.pp.xpath('//*[@resource-id="com.kuaishou.nebula:id/menu_recycler_view"]/'
                                                 'android.view.ViewGroup[2]').get().bounds)
        self.pp(description='活动规则').wait()
        coin = self.pp.xpath('//*[@resource-id="com.kuaishou.nebula:id/webView"]/android.webkit.WebView[1]/'
                             'android.webkit.WebView[1]/android.widget.ListView[1]/android.view.View[1]/'
                             'android.view.View[1]').get().attrib['content-desc'].replace(',', '')
        time.sleep(random.random() + 1)
        self.pp.press('back')
        time.sleep(random.random() + 1)
        if 'w' in coin:
            coin = int(float(coin.replace('w', '')) * 10000)
        else:
            coin = int(coin)
        self.logger.info(f'今日已经获取金币 {coin}')
        return coin

    def clean_cache(self):
        self.logger.info(f'开始清理缓存')
        self.pp(resourceId='com.kuaishou.nebula:id/left_btn').click(offset=(random.random(), random.random()))
        self.pp(text='设置').wait()
        self.pp(text='设置').click(offset=(random.random(), random.random()))
        self.pp(text='清除缓存').wait()
        self.pp(text='清除缓存').click(offset=(random.random(), random.random()))

    def _read_issue_core(self, read_issue_time):
        issue_time_start = time.time()  # 开始计时
        while time.time() - issue_time_start <= read_issue_time:
            if not self.pp(resourceId='com.kuaishou.nebula:id/red_packet').exists:
                self.scroll_read_issue()
                continue
            # time.sleep(random.uniform(3, 5))
            # 按照设定的点赞概率，随机点赞
            if self.pp.xpath('//*[@resource-id="com.kuaishou.nebula:id/like_icon"]').exists and \
                    random.random() < self.probability_thumb_up:
                self.click_random_position(self.pp.xpath('//*[@resource-id="com.kuaishou.nebula:id/like_icon"]')
                                           .get().bounds)
                time.sleep(random.random() + 1)
            # 按照设定的关注概率，随机关注
            if self.pp.xpath('//*[@resource-id="com.kuaishou.nebula:id/slide_play_right_follow_avatar_view"]').exists \
                    and random.random() < self.probability_focus:
                self.click_random_position(self.pp.xpath('//*[@resource-id="com.kuaishou.nebula:id/'
                                                         'slide_play_right_follow_avatar_view"]').get().bounds)
                if self.pp(text='i 关注').exists(timeout=3):
                    self.pp(text='i 关注').click(offset=(random.random(), random.random()))
                time.sleep(random.random() + 3)
                self.pp.press('back')
                time.sleep(random.random() + 1)
            # 按照设定的评论概率，随机评论
            if self.pp.xpath('//*[@resource-id="com.kuaishou.nebula:id/comment_icon"]').exists and \
                    random.random() < self.probability_commit:
                self.click_random_position(self.pp.xpath('//*[@resource-id="com.kuaishou.nebula:id/comment_icon"]')
                                           .get().bounds)
                time.sleep(random.random() + 1)
                if self.pp(resourceId='com.kuaishou.nebula:id/comment_editor_holder_text').exists:
                    self.click_random_position(self.pp(resourceId='com.kuaishou.nebula:id/'
                                                                  'comment_editor_holder_text').bounds())
                self.pp(resourceId='com.kuaishou.nebula:id/editor').wait()
                self.pp(resourceId='com.kuaishou.nebula:id/editor').set_text(random.choice(self.commit))
                time.sleep(random.random() + 2)
                self.pp(resourceId='com.kuaishou.nebula:id/finish_button') \
                    .click(offset=(random.random(), random.random()))
                time.sleep(random.random() + 1)
                self.pp.press('back')
                time.sleep(random.random() + 1)
            self.scroll_read_issue()

    def read_issue_first(self, read_issue_time):
        self.logger.info(f'开始阅读发现视频')
        time.sleep(random.random() + 1)
        self.pp.xpath('//*[@resource-id="com.kuaishou.nebula:id/tabs"]/android.widget.LinearLayout[1]/'
                      'android.view.View[3]').wait()
        self.click_random_position(self.pp.xpath('//*[@resource-id="com.kuaishou.nebula:id/tabs"]/'
                                                 'android.widget.LinearLayout[1]/android.view.View[3]').get().bounds)
        time.sleep(random.random() + 1)
        self._read_issue_core(read_issue_time)

    def read_issue_city(self, read_issue_time):
        self.logger.info(f'开始阅读同城视频')
        time.sleep(random.random() + 1)
        self.pp.xpath('//*[@resource-id="com.kuaishou.nebula:id/tabs"]/android.widget.LinearLayout[1]/'
                      'android.view.View[1]').wait()
        self.click_random_position(self.pp.xpath('//*[@resource-id="com.kuaishou.nebula:id/tabs"]/'
                                                 'android.widget.LinearLayout[1]/android.view.View[1]').get().bounds)
        time.sleep(random.random() + 1)
        for j in range(random.randint(0, 2)):  # 随机下滑几次
            self.pp.swipe(random.uniform(0.3, 0.6), random.uniform(0.7, 0.8), random.uniform(0.3, 0.6),
                          random.uniform(0.2, 0.3), steps=random.randint(20, 60))
        temp_bounds = self.pp.xpath(f'//*[@resource-id="com.kuaishou.nebula:id/recycler_view"]/'
                                    f'android.widget.RelativeLayout[{random.randint(1, 4)}]/'
                                    f'android.widget.ImageView').bounds
        self.click_random_position(temp_bounds)  # 随机选页面中的视频
        self._read_issue_core(read_issue_time)
        time.sleep(random.random() + 1)
        self.pp.press('back')
        time.sleep(random.random() + 1)

    def read_issue(self, duration, target_coin):
        read_issue_time1, read_issue_time2 = random.randint(600, 900), random.randint(30, 60)
        issue_time_start = time.time()  # 开始计时
        while time.time() - issue_time_start <= duration and self.today_coin() <= target_coin:
            self.read_issue_first(read_issue_time1)
            if self.today_coin() > target_coin:
                break
            self.read_issue_city(read_issue_time2)

    def main_do(self, duration, target_coin, cash_out):
        # raise
        self.app_start('快手极速版')
        self.pp(resourceId='com.kuaishou.nebula:id/thanos_home_top_search').wait(timeout=30)
        self.sign_in()
        self.read_issue(duration, target_coin)
        self.clean_cache()
        self.app_end()
