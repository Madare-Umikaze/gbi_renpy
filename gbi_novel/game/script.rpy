
define y = Character("[yname]", color="#c8ffc8")
define f = Character("父さん")

image white = "background/white.jpeg"
image op title = "background/title1.jpeg"
image op nature = "background/nature1.jpeg"
image home = "background/home1.jpeg"
image father = "character/father1.png"
image game title = "background/title2.jpeg"
image sky = "background/sky1.jpeg"

label start:

    scene white
    with dissolve

    python:
        yname = renpy.input("あなたの名前は？", length=32)
        yname = yname.strip()

        if not yname:
             yname = "リュウガ"




    scene op title
    with Dissolve(5.0)
    scene op nature

    menu:
        "君はどの魔法適正が？"

        "火属性":
            "あなたは火属性の魔法適正があるのね。"

        "水属性":
            "あなたは水属性の魔法適正があるのね。"

        "花属性":
            "あなたは花属性の魔法適正があるのね。"

        "雷属性":
            "あなたは雷属性の魔法適正があるのね。"

        "土属性":
            "あなたは土属性の魔法適正があるのね。"

        "風属性":
            "あなたは風属性の魔法適正があるのね。"

        "光属性":
            "あなたは光属性の魔法適正があるのね。"

        "闇属性":
            "…そう、闇属性なのね、、"


    label after_menu:

    "どのような属性でも、\n あなたならきっと、素晴らしい魔法使いになれるわ！！"

    play music "audio/楽しく軽快に.mp3"

    "木々の間を爽やかに吹き抜ける風は、小鳥たちの囀りを引き立てる。"
    "聳え立つ万緑の山々は、鮮やかな青空に豊かな色を付け加える。"

    "ここはアルカイド。美しい自然の町。そして俺が生まれ育った町だ"

    "生まれ育った自然の中、俺は草むらの上に寝転がっていた。"

    stop music

    play sound "audio/explosion1.mp3"

    y "「何だ?!」"

    " 骨が震えるような轟音が響いた。何かが爆発したような音だ。"

    scene home
    with fade

    f "「どうした?!」"

    show father at right

    "  父さんが家から出てきた。"

    f "「何があったかわかるか?」"

    y "「わからない・・・。でも、よくないことが起こったのは間違いない」"

    hide father

    play sound "audio/gbi　オープニング.mp3"

    scene game title
    with Fade(0.5, 4.0, 15.0)

    stop sound fadeout 1.0

    return
