"""
prompts.py
该文件存储所有用于摘要的提示词模板。
"""

prompt_default="""
# 视频课程笔记生成 Prompt

请基于提供的视频转录文字，生成一份结构化的学习笔记。要求如下：

## 输出要求

### 1. 文档头部信息
- 视频标题
- 视频来源（YouTube/Bilibili）
- 视频链接（如有）
- 视频时长
- 笔记生成日期

### 2. 全文主题和内容框架（Mermaid 图）(仔细确认语法，a确保无错误)
根据文章结构内容使用合适的Mermaid图表， Mermaid mindmap 或 flowchart 语法，生成视频内容的思维导图，要求：
- 清晰展示主题和各级子主题的层级关系
- 包含所有重要知识点模块
- 使用简洁的关键词标注

### 3. 内容分段总结
对视频内容进行时间轴分段，每个分段包含：
- **时间戳**：该段内容对应的视频时间
- **段落标题**：该段的核心主题（10字以内）
- **核心内容**：
  - 高度还原讲师的表达逻辑和语言风格
  - 保留关键术语、概念定义、示例说明
  - 提炼核心观点，但不改变原意
  - 包含重要的代码示例、公式或图表说明（如有）
- **关键要点**：用 bullet points 列出该段的核心知识点（3-5个）

### 4. 全文总结
- **核心观点**：整个视频的主要论点或教学目标（3-5句话）
- **关键收获**：最重要的知识点或技能（5-8个 bullet points）
- **适用场景**：这些知识可以应用在哪些实际场景
- **延伸学习**：建议的后续学习方向或相关主题

### 5. 术语表（可选）
如果视频涉及专业术语，列出：
- 术语名称
- 简明解释
- 在视频中的使用场景

## 内容要求

1. **准确性**：忠实还原视频内容，不添加视频中未提及的信息
2. **结构化**：使用 Markdown 标题层级清晰组织内容
3. **可读性**：
   - 使用代码块标注代码示例
   - 使用引用块标注重要观点
   - 使用表格整理对比性内容
   - 使用列表突出要点
4. **完整性**：涵盖视频的所有重要内容，不遗漏关键信息

## 输出格式

以 Markdown (.md) 格式输出，文件名格式：`[视频标题]_学习笔记_[日期].md`

---

"""

prompt_1 = """
# 英文视频课程笔记生成 Prompt

Please generate structured learning notes based on the provided video transcript. Requirements:

## Output Requirements

### 1. Document Header
- Video Title
- Source (YouTube/Bilibili)
- Video Link (if available)
- Duration
- Note Creation Date

### 2. Content Framework (Mermaid Diagram)
Generate a Mermaid mindmap or flowchart to visualize the video's content structure:
- Clearly show the hierarchy of main topics and subtopics
- Include all important knowledge modules
- Use concise keywords for labeling

### 3. Segmented Content Summary
Divide the video content by timeline, each segment includes:
- **Timestamp**: Video time for this segment
- **Section Title**: Core topic (within 10 words)
- **Core Content**:
  - Faithfully restore the instructor's logic and language style
  - Preserve key terms, concept definitions, and examples
  - Extract core viewpoints without changing the original meaning
  - Include important code examples, formulas, or diagrams (if any)
  - **Keep all content in English**
- **Key Points**: List 3-5 core knowledge points in bullet format

### 4. Overall Summary
- **Core Arguments**: Main points or teaching objectives (3-5 sentences)
- **Key Takeaways**: Most important knowledge or skills (5-8 bullet points)
- **Use Cases**: Practical scenarios where this knowledge applies
- **Further Learning**: Suggested follow-up topics or learning directions

### 5. Bilingual Glossary (REQUIRED)
For technical terms and key concepts:
- **English Term**
- **Chinese Translation** (中文翻译)
- **Definition/Explanation** (in English)
- **Context in Video** (usage scenario)

Format:
```
| English Term | 中文翻译 | Definition | Context |
|--------------|---------|------------|---------|
| ... | ... | ... | ... |
```

### 6. Key Vocabulary Section
Extract 20-30 important words/phrases with:
- **English Expression**
- **中文含义**
- **Example Sentence** (from video context)

## Content Requirements

1. **Accuracy**: Faithfully represent video content without adding unmentioned information
2. **Structure**: Use clear Markdown heading hierarchy
3. **Readability**:
   - Use code blocks for code examples
   - Use blockquotes for important viewpoints
   - Use tables for comparative content
   - Use lists to highlight key points
4. **Completeness**: Cover all important content without omitting key information
5. **Language**: 
   - Main content in **English**
   - Add Chinese translations for technical terms
   - Bilingual glossary required

## Output Format

Output in Markdown (.md) format
Filename: `[Video_Title]_Notes_[Date].md`

---

**Please process the following video transcript:**

[Paste video transcript here]
"""

prompt_2 = """

"""

prompt_3 = """

"""

prompt_4 = """

"""

prompt_5 = """

"""

prompt_6 = """

"""

prompt_templates = {
    "default课堂笔记": prompt_default,
    "youtube_英文笔记": prompt_1,
    "youtube_结构化提取": prompt_2,
    "youtube_精炼提取": prompt_3,
    "youtube_专业课笔记": prompt_4,
    "爆款短视频文案": prompt_5,
    "youtube_视频总结": prompt_6,
}
