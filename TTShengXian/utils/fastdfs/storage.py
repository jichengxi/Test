from django.conf import settings
from django.core.files.storage import Storage
from fdfs_client.client import Fdfs_client, get_tracker_conf


class FDFSStorage(Storage):
    """fastdfs文件存储类"""

    def _open(self, name, mode='rb'):
        """打开文件时使用"""
        pass

    def _save(self, name, content):
        """保存文件时使用"""
        # name: 你选择上传文件的名字
        # content: 包含你上传文件内容的File对象

        # 创建一个Fdfs_client对象
        client_path = get_tracker_conf('./utils/fastdfs/client.conf')
        client = Fdfs_client(client_path)

        # 上传文件到fastdfs系统中
        result = client.upload_by_buffer(content.read())

        if result.get('Status') != 'Upload successed.':
            # 上传失败
            raise Exception('上传文件到FastDFS失败')
        # 获取返回的文件ID
        filename = result.get('Remote file_id')
        return filename

    def exists(self, name):
        return False

    def url(self, name):
        """返回访问文件的url路径"""
        return name
