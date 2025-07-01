from fontTools.ttLib import TTFont
import os

# oTTbTOza.woff抓包获取，但是可能实时变化的
font_path = os.path.join(os.path.dirname(__file__), 'oTTbTOza.woff')

xml_path = os.path.join(os.path.dirname(__file__), 'font.xml')

font = TTFont(font_path)

# 将字体转化为xml
font.saveXML(xml_path)

    # <cmap_format_12 platformID="3" platEncID="10" format="12" reserved="0" length="148" language="0" nGroups="11">
    #   <map code="0x188b8" name="nine"/><!-- TANGUT COMPONENT-185 -->
    #   <map code="0x188ba" name="three"/><!-- TANGUT COMPONENT-187 -->
    #   <map code="0x188bb" name="two"/><!-- TANGUT COMPONENT-188 -->
    #   <map code="0x188bc" name="eight"/><!-- TANGUT COMPONENT-189 -->
    #   <map code="0x188bd" name="period"/><!-- TANGUT COMPONENT-190 -->
    #   <map code="0x188be" name="six"/><!-- TANGUT COMPONENT-191 -->
    #   <map code="0x188bf" name="one"/><!-- TANGUT COMPONENT-192 -->
    #   <map code="0x188c0" name="four"/><!-- TANGUT COMPONENT-193 -->
    #   <map code="0x188c1" name="zero"/><!-- TANGUT COMPONENT-194 -->
    #   <map code="0x188c2" name="seven"/><!-- TANGUT COMPONENT-195 -->
    #   <map code="0x188c3" name="five"/><!-- TANGUT COMPONENT-196 -->
    # </cmap_format_12>

# 获取字体映射
font_map = font.getBestCmap()
# {100536: 'nine', 100538: 'three', 100539: 'two', 100540: 'eight', 100541: 'period', 100542: 'six', 100543: 'one', 100544: 'four', 100545: 'zero', 100546: 'seven', 100547: 'five'}
# &#100060;&#100059;&#100060;&#100055;&#100057;

print(font_map)
