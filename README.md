# 学生反馈分析系统

一个基于Django和微信小程序的学生反馈收集与分析系统。

## 项目结构

```
project_othrt/
├── damiao/          # 后端项目目录
│   ├── core/        # 核心应用
│   ├── feedback_system/  # 项目配置
│   └── requirements.txt  # 后端依赖
└── miniprogram/     # 微信小程序目录
```

## 后端部分

### 技术栈
- Python 3.10
- Django 4.2.7
- Django REST Framework
- DeepSeek API (大语言模型)
- JWT认证

### 功能特性
- 用户认证和授权
- 学生信息管理
- 反馈收集和存储
- 反馈智能分析
- RESTful API接口

### 安装部署
1. 创建虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. 安装依赖：
```bash
cd damiao
pip install -r requirements.txt
```

3. 配置环境变量：
```bash
cp .env.example .env
# 编辑.env文件，填入必要的配置信息
```

4. 数据库迁移：
```bash
python manage.py migrate
```

5. 创建超级用户：
```bash
python manage.py createsuperuser
```

6. 运行开发服务器：
```bash
python manage.py runserver
```

### API文档
- 认证接口：`/api/token/`
- 反馈接口：`/api/v1/feedbacks/`
- 分析接口：`/api/v1/feedbacks/{id}/analyze/`

## 前端部分

### 技术栈
- 微信小程序原生框架
- WeUI组件库

### 功能特性（计划中）
- 用户登录和授权
- 反馈提交
- 历史记录查看
- 分析结果展示
- 数据可视化

### 开发说明
1. 使用微信开发者工具打开miniprogram目录
2. 配置小程序的AppID
3. 修改项目配置文件中的后端接口地址

## 开发进度
- [x] 后端基础架构
- [x] 用户认证系统
- [x] 反馈管理API
- [x] 大语言模型集成
- [ ] 微信小程序开发
- [ ] 前后端联调
- [ ] 部署上线

## 贡献指南
1. Fork 本仓库
2. 创建特性分支
3. 提交更改
4. 发起 Pull Request

## 许可证
MIT License 