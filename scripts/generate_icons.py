from PIL import Image, ImageDraw, ImageFont
import os

def create_emoji_icon(emoji, output_path, size=(81, 81), color=(153, 153, 153)):
    # 创建白色背景的图片（而不是透明背景）
    image = Image.new('RGB', size, (255, 255, 255))
    draw = ImageDraw.Draw(image)
    
    try:
        # 尝试加载 Segoe UI Emoji 字体
        font = ImageFont.truetype("seguiemj.ttf", 60)
    except:
        try:
            # 尝试加载系统默认 emoji 字体
            font = ImageFont.truetype("segoe ui emoji", 60)
        except:
            # 如果都失败了，使用默认字体
            font = ImageFont.load_default()
    
    # 计算文字位置使其居中
    bbox = draw.textbbox((0, 0), emoji, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    x = (size[0] - w) / 2
    y = (size[1] - h) / 2
    
    # 绘制 emoji（使用指定颜色）
    draw.text((x, y), emoji, font=font, fill=color)
    
    # 保存为 PNG 格式
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    image.save(output_path, 'PNG')

def main():
    # 项目根目录
    base_dir = r'c:\Users\小墨同学123\Documents\HBuilderProjects\澳科保姆前端'
    icons_dir = os.path.join(base_dir, 'static', 'icons', 'tabbar')
    
    # 创建图标目录
    os.makedirs(icons_dir, exist_ok=True)
    
    # 定义图标配置
    icons = {
        'course': '📚',
        'food': '🍽️',
        'housing': '🏠',
        'message': '💬',
        'user': '👤'
    }
    
    # 生成图标
    for name, emoji in icons.items():
        # 普通图标
        output_path = os.path.join(icons_dir, f'{name}.png')
        create_emoji_icon(emoji, output_path, color=(153, 153, 153))
        print(f'生成图标: {output_path}')
        
        # 选中状态图标
        output_path = os.path.join(icons_dir, f'{name}-active.png')
        create_emoji_icon(emoji, output_path, color=(52, 152, 219))
        print(f'生成图标: {output_path}')

if __name__ == '__main__':
    main()