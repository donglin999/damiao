# 学生反馈系统

基于Django + 微信小程序的学生反馈系统，支持文字反馈，并使用大语言模型进行分析。

## 技术栈

### 后端
- Python 3.10+
- Django 4.2.7
- Django REST Framework 3.14.0
- JWT认证（djangorestframework-simplejwt）
- SQLite数据库

### 前端（计划中）
- 微信小程序
- Vue.js

## 项目结构

```
feedback_system/
├── core/                   # 核心应用
│   ├── api/               # API相关代码
│   │   ├── serializers/   # 序列化器
│   │   ├── views/        # 视图
│   │   └── urls/         # URL配置
│   ├── models.py         # 数据模型
│   └── services/         # 业务服务
│       └── analysis.py   # 分析服务
├── feedback_system/       # 项目配置
└── manage.py             # Django管理脚本
```

## 功能特性

### 已实现
- [x] 项目基础架构搭建
- [x] 核心数据模型设计（学生、反馈、分析结果）
- [x] RESTful API基础框架
- [x] JWT认证集成（完整实现）
- [x] CORS支持
- [x] 文件上传支持

### 开发中
- [ ] 大语言模型集成
- [ ] 数据可视化接口
- [ ] 音频转文字功能
- [ ] 微信小程序前端

## API接口

### 认证接口
- POST `/api/token/` - 获取访问令牌和刷新令牌
  - 请求体：`{"username": "用户名", "password": "密码"}`
  - 响应：`{"access": "访问令牌", "refresh": "刷新令牌"}`
- POST `/api/token/refresh/` - 刷新访问令牌
  - 请求体：`{"refresh": "刷新令牌"}`
  - 响应：`{"access": "新的访问令牌"}`
- POST `/api/token/verify/` - 验证令牌有效性
  - 请求体：`{"token": "待验证的令牌"}`

### 业务接口
基础URL: `http://localhost:8000/api/v1/`

#### 主要端点
- `/students/` - 学生管理
- `/feedbacks/` - 反馈管理
- `/feedbacks/{id}/analyze/` - 反馈分析

所有API请求都需要在请求头中包含JWT令牌：
```
Authorization: Bearer <access_token>
```

## 安装和运行

1. 克隆项目
```bash
git clone [项目地址]
cd feedback_system
```

2. 创建并配置环境变量
```bash
cp .env.example .env
# 编辑.env文件，填入必要的配置信息
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 数据库迁移
```bash
python manage.py migrate
```

5. 创建超级用户
```bash
python manage.py createsuperuser
```

6. 运行开发服务器
```bash
python manage.py runserver
```

## 更新日志

### 2024-01-08 简化功能
- 暂时移除音频处理功能
- 专注于文字反馈处理
- 简化依赖项
- 优化项目结构

### 2024-01-07 JWT认证完整实现
- 添加JWT认证配置
  - 配置令牌有效期（访问令牌1小时，刷新令牌1天）
  - 配置令牌签名算法和密钥
  - 配置令牌声明和头部
- 实现JWT认证端点
  - 添加令牌获取接口
  - 添加令牌刷新接口
  - 添加令牌验证接口
- 更新API文档，添加认证相关说明

### 2024-01-07 初始版本
- 创建项目基础结构
- 实现核心数据模型
- 配置REST框架和JWT认证
- 实现基础API端点
- 添加CORS支持
- 配置文件上传功能
- 创建管理员界面
- 添加.gitignore配置

## 开发计划

### 近期计划
1. 集成大语言模型
2. 开发数据分析服务
3. 实现数据可视化接口
4. 实现音频转文字功能

### 后期计划
1. 开发微信小程序前端
2. 优化用户体验
3. 添加更多数据分析功能
4. 实现实时反馈功能

## 环境变量配置

项目使用.env文件管理环境变量，主要配置项包括：

```
# Django Settings
DEBUG=True
SECRET_KEY=your-secret-key-here
```

## 贡献指南

欢迎提交Issue和Pull Request。

## 许可证

[待定] 