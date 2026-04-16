# JXUST LaTeX

江西理工大学本科毕业设计（论文）LaTeX 模板。该目录基于现有 Word 版式整理而成，适合继续完善后放到 GitHub 共享与维护。

![image-20260416162529114](figures\image-20260416162529114.png)

## 项目内容

- `thesis_template.tex`：精简后的空白模板，适合直接开始写论文
- `jxust-setup.tex`：公共导言区与排版命令
- `figures/`：图片资源目录，模板默认用 `figures/image2.png` 作为图片示例
- `thesis_template.pdf`：模板编译预览
- `build.bat`：Windows 下的快速编译脚本

## 模板特性

- 使用 `ctexart + XeLaTeX`，适配中文论文排版
- 正文、摘要、关键词、参考文献分别使用独立段落样式
- 摘要部分页码为罗马数字，正文从第一章开始切换为阿拉伯数字
- 已启用 PDF 书签
- 表格默认采用论文常用三线表样式
- 模板内自带公式示例和图片示例

## 目录结构

```text
JXUST-latex/
├─ README.md
├─ .gitignore
├─ build.bat
├─ jxust-setup.tex
├─ thesis_template.tex
├─ thesis_template.pdf
└─ figures/
```

## Windows 安装指南

### 1. 安装 TeX 发行版

推荐两种方案，二选一即可：

1. 安装 MiKTeX
2. 安装 TeX Live

如果你只是在 Windows 上日常写作，MiKTeX 更省事。

### 2. 安装推荐编辑器

可任选一种：

1. VS Code + LaTeX Workshop 插件
2. TeXstudio
3. WinEdt

其中 VS Code + LaTeX Workshop 最适合放到 GitHub 上持续维护。

### 3. 确认编译器

本模板要求使用 `XeLaTeX` 编译，不建议改成 `pdfLaTeX`。

Windows 下通常需要系统中存在这些字体：

- `SimSun`
- `SimHei`
- `Times New Roman`
- `Courier New`

Windows 默认一般已具备这些字体。

### 4. 将 `xelatex` 加入 PATH

如果你安装的是 MiKTeX，通常可在安装完成后把 MiKTeX 的 `miktex\\bin\\x64` 目录加入系统环境变量 `PATH`。  
加入后，在终端执行下面命令能看到版本信息，就说明配置完成：

```powershell
xelatex --version
```

## 使用指南

1. 打开 `thesis_template.tex`
2. 按章节替换其中的占位内容
3. 将自己的图片放到 `figures/`
4. 使用 XeLaTeX 编译

## 编译方法

### 方法一：双击脚本

在 Windows 资源管理器中直接运行：

```text
build.bat
```

脚本会默认编译：

- `thesis_template.tex`

### 方法二：命令行编译

在当前目录打开终端后运行：

```powershell
xelatex -interaction=nonstopmode -halt-on-error thesis_template.tex
xelatex -interaction=nonstopmode -halt-on-error thesis_template.tex
```

通常编译两遍，目录书签和页码引用会更稳定。

## 常见修改位置

- 修改页眉：编辑 `jxust-setup.tex` 中的 `\\fancyhead[C]{...}`
- 修改页边距：编辑 `jxust-setup.tex` 中的 `\\geometry{...}`
- 修改标题样式：编辑 `\\chaptertitle`、`\\sectiontitle`、`\\subsectiontitle`
- 修改摘要、正文、参考文献格式：编辑 `\\cnabstractpara`、`\\bodypara`、`\\referenceentry`
- 修改图片：将图片放到 `figures/`，再在 `.tex` 中替换文件名
- 修改表格：模板默认使用 `booktabs` 三线表

## 说明

这个版本只保留模板文件，不包含你的论文正文内容。当前目标是“接近当前 Word 稿件版式并可稳定编译”，不是对学校官方模板的逐项规范复刻。如果后续要继续公开维护，建议再补：

- 官方封面页
- 自动目录
- 更严格的参考文献样式
- 更完整的公式转写
