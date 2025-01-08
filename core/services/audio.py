import os
from pydub import AudioSegment
from aip import AipSpeech
from django.conf import settings

class AudioService:
    def __init__(self):
        # 百度语音识别配置
        self.APP_ID = os.getenv('BAIDU_APP_ID')
        self.API_KEY = os.getenv('BAIDU_API_KEY')
        self.SECRET_KEY = os.getenv('BAIDU_SECRET_KEY')
        self.client = None if not all([self.APP_ID, self.API_KEY, self.SECRET_KEY]) else \
            AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    def convert_audio_to_wav(self, audio_path):
        """
        将音频文件转换为wav格式
        """
        try:
            # 获取文件扩展名
            ext = os.path.splitext(audio_path)[1].lower()
            if ext == '.wav':
                return audio_path

            # 转换音频格式
            audio = AudioSegment.from_file(audio_path)
            wav_path = os.path.splitext(audio_path)[0] + '.wav'
            audio.export(wav_path, format='wav')
            return wav_path
        except Exception as e:
            print(f"音频转换失败: {str(e)}")
            return None

    def audio_to_text(self, audio_path):
        """
        将音频文件转换为文字
        """
        try:
            if not self.client:
                raise Exception("未配置百度语音识别服务")

            # 确保音频为wav格式
            wav_path = self.convert_audio_to_wav(audio_path)
            if not wav_path:
                raise Exception("音频转换失败")

            # 读取音频文件
            with open(wav_path, 'rb') as fp:
                audio_data = fp.read()

            # 调用百度语音识别API
            result = self.client.asr(audio_data, 'wav', 16000, {
                'dev_pid': 1537,  # 普通话(支持简单的英文识别)
            })

            # 检查识别结果
            if result['err_no'] == 0:
                return result['result'][0]
            else:
                raise Exception(f"语音识别失败: {result['err_msg']}")

        except Exception as e:
            print(f"语音识别失败: {str(e)}")
            return None

    def process_feedback_audio(self, feedback):
        """
        处理反馈中的音频文件
        """
        try:
            if not feedback.audio_file:
                return None

            # 获取音频文件路径
            audio_path = os.path.join(settings.MEDIA_ROOT, feedback.audio_file.name)
            
            # 转换音频为文字
            text = self.audio_to_text(audio_path)
            
            if text:
                # 更新反馈内容
                feedback.content = text
                feedback.save()
                return text
            return None
        except Exception as e:
            print(f"音频处理失败: {str(e)}")
            return None 