# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define m = Character("{color=#6f7386}喵喵同学{/color}")
define h = Character("{color=#999900}时衍{/color}")
define j = Character("{color=#935116}陆宇{/color}")
define s = Character("{color=#6e2c00}诗诗{/color}")
define u = Character("{color=#ff6699}尤娜{/color}")
define e = Character("{color=#b3b300}小萌{/color}")
define z = Character("{color=#666666}洛翼{/color}")
define i = Character("{color=#737373}洛羽{/color}")
define p = Character("{color=#336699}警长{/color}")

# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    scene bgclass with fade
    pause 1.0
    
    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    show miaothink with dissolve

    # 此处显示各行对话。

    m "{color=#6f7386}{cps=25}{size=+5}我，一名高中生，自小就对犯罪心理学有着浓厚的兴趣。{/size}{/cps}{/color}"
    m "{color=#6f7386}{cps=25}{size=+5}在高中毕业之前就已经获得了犯罪学博士学位，身边的导师都夸我是破案天才。{/size}{/cps}{/color}"
    play music normal fadein 1.0 
    m "{color=#6f7386}{cps=25}{size=+5}而今天，我的学校发生了命案。{/size}{/cps}{/color}"

    hide miaothink

    show desuna with dissolve

    "{color=#6f7386}{cps=25}{size=+5}死者是全校公认的校花，她为人正直善良，是学校里特别受欢迎的“女神”。{/size}{/cps}{/color}"
    "{color=#6f7386}{cps=25}{size=+5}但同时也有同学说她很高傲、目中无人，特别享受被异性追捧的感觉{/size}{/cps}{/color}"
    "{color=#6f7386}{cps=25}{size=+5}甚至还会对那些对她来说没有利益帮助的同性产生敌意。{/size}{/cps}{/color}"

    hide desuna
    show miaosad with dissolve
    "{color=#6f7386}{cps=25}{size=+5}这我也有发言权。{/size}{/cps}{/color}"
    hide miaosad

    scene bg11 with fade
    show miaosad with dissolve
    "{color=#6f7386}{cps=25}{size=+5}在我升上高中前，她也曾经因为我考获了犯罪学博士学位而嫉妒我，怂恿学校的所有同学孤立我。{/size}{/cps}{/color}"
    "{color=#6f7386}{cps=25}{size=+5}散播我是精神病的谣言，甚至对我实施了校园暴力，我手臂上所有烟头的痕迹都是她的杰作。{/size}{/cps}{/color}"

    hide miaosad
    "{color=#6f7386}{cps=25}{size=+5}嗯.. 就如一些知晓内幕的同学所说的，她是一头披着羊皮的狼。{/size}{/cps}{/color}"

    scene bgswim with fade

    "{color=#6f7386}{cps=25}{size=+5}尤娜的尸体是在学校泳池里被发现的，她的左脸上被划了一道很浅的口子，但身上并没有和别人打斗过的痕迹。{/size}{/cps}{/color}"

    show miaosaid

    "{color=#6f7386}{cps=25}{size=+5}一般情况下，进入学校的游泳池都需要到入口处登记。{/size}{/cps}{/color}"
    "{color=#6f7386}{cps=25}{size=+5}而在登记簿上却没有今天的记录，大门的监控器也莫名地失控了，没有任何目击证人或嫌疑人。{/size}{/cps}{/color}"

    hide miaosaid

menu:
    "你怎么看？"
    
    "死得好啊，恶人自有恶人磨。^_^":
        jump you_still_need_practice

    "看来这是一起谋杀案。":
        jump Chapter1_Done

label you_still_need_practice:
    stop music
    play music c1 fadein 1.5 fadeout 1.5
    pause 0.5
    show miaosmile with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}死得好啊 恶人自有恶人磨。{/size}{/cps}{/color}"
    hide miaosmile

    "{color=#000000}{cps=25}{size=+5}说罢，大家神色各异，对我投来异样的眼光。{/size}{/cps}{/color}"
    show miaozzz
    m "{color=#6f7386}{cps=25}{size=+5}虽然我讨厌尤娜，但这行为也太单细胞了吧...{/size}{/cps}{/color}"
    hide miaozzz

    "{color=#000000}{cps=25}{size=+5}于是，我被禁止参与案件调查了...{/size}{/cps}{/color}"

    scene bg1 with fade
    pause 6.0
    stop music
        
return 

#########################################################################################################

label Chapter1_Done:
    stop music
    scene bgswim
    show miaothink with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}看来这是一起谋杀案。{/size}{/cps}{/color}"
    
    scene c1done with fade
    pause 3.5
    
    play music normal2 fadein 1.5 fadeout 1.5

    scene bgwalk with fade
    hide miaothink
    "{color=#000000}{cps=25}{size=+5}学生们开始讨论各种阴谋论，有人说是因为嫉妒；有人说是因为情感纠纷；{/size}{/cps}{/color}"
    "{color=#000000}{cps=25}{size=+5}也有人说是因为这是来自被她针对的同学的报复。{/size}{/cps}{/color}"
    "{color=#000000}{cps=25}{size=+5}整个校园陷入恐慌，毕竟这绝对是一起精心密谋过的谋杀案。{/size}{/cps}{/color}"

    scene bgpolice with fade
    "{color=#000000}{cps=25}{size=+5}警方拍照记录现场并把证据收好，随后尸体被捞起，送往法医处检查。{/size}{/cps}{/color}"

    show policesaid with dissolve
    p "{color=#336699}{cps=25}{size=+5}喵喵同学，这次的案子就交给你了！一定要为尤娜讨回一个公道啊！{/size}{/cps}{/color}"
    "{color=#6f7386}{cps=25}{size=+5}警长拍了拍我的肩，重叹一口气，他的眉心紧皱着。{/size}{/cps}{/color}"
    hide policesaid

    show miaosmile with dissolve
    "{color=#6f7386}{cps=25}{size=+5}我无奈苦笑，这可真是一个棘手的案件啊{/size}{/cps}{/color}"
    "{color=#6f7386}{cps=25}{size=+5}不过，我，称得上犯罪学天才，我想没有人会比我更了解这类型的案子。{/size}{/cps}{/color}"
    hide miaosmile
    show miaosaid with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}就如同学们所说的，凶手就在学校里，而他的杀人动机无非就是嫉妒、情感纠纷、金钱纠纷或者校园霸凌。{/size}{/cps}{/color}"
    m "{color=#6f7386}{cps=25}{size=+5}从这些杀人动机中，我可以推测出一小范围的嫌疑人，再从法医的报告中寻找被遗漏的线索，凶手自然而然就显露了。"
    hide miaosaid

    m "{color=#6f7386}{cps=25}{size=+5}这一小范围的嫌疑人分别是：{/size}{/cps}{/color}"

    scene bglove with fade
    show npynormal with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}尤娜的暧昧对象 — {b}时衍{/b}{/size}{/cps}{/color}"
    hide npynormal

    scene bgfren with fade
    show shishinor with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}尤娜的闺蜜— {b}诗诗{/b}{/size}{/cps}{/color}"
    hide shishinor

    scene bgblack with fade
    show xiaomengnor with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}被尤娜霸凌长达三年的受害者 — {b}小萌{/b}{/size}{/cps}{/color}"
    hide xiaomengnor

    scene bghouse with fade
    show tgnor with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}和尤娜的青梅竹马 — {b}陆宇{/b}{/size}{/cps}{/color}"
    hide tgnor

    scene bgrich with fade
    show npynormal with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}时衍是尤娜有名无份的男朋友，他是一个富二代，在尤娜身上花了很多钱。{/size}{/cps}{/color}"
    m "{color=#6f7386}{cps=25}{size=+5}而尤娜却总是对外说他们只是好朋友，因为她很享受不同男人的示好。{/size}{/cps}{/color}"
    hide npynormal

    scene bgfren with fade
    show shishinor with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}诗诗是尤娜表面上最好的朋友，但是我知道，其实她一直都特别嫉妒尤娜。{/size}{/cps}{/color}"
    extend "{color=#6f7386}{cps=25}{size=+5}嫉妒她的样貌、成绩、还有她的人缘。{/size}{/cps}{/color}"
    m "{color=#6f7386}{cps=25}{size=+5}她身上好像藏着一些秘密。{/size}{/cps}{/color}"
    hide shishinor

    scene bgblack with fade
    show xiaomengnor with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}小萌是学校里的小透明，她患有多动症，没有办法集中注意力。{/size}{/cps}{/color}"
    m "{color=#6f7386}{cps=25}{size=+5}这使她常常成为尤娜的笑柄，并且在她的第一次反抗下，尤娜对她实施了校园暴力。{/size}{/cps}{/color}"
    hide xiaomengnor

    scene bghouse with fade
    show tgnor with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}陆宇是尤娜的青梅竹马，也是人们口中的“尤娜的舔狗”{/size}{/cps}{/color}"
    hide tgnor

    scene bgwalk with fade
    show miaothink with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}这些人都有足够的杀人动机，现在就只需要等法医的报告出来，凶手必定会露出蛛丝马迹。{/size}{/cps}{/color}"
    hide miaothink

    show miaowink
    "{color=#6f7386}{cps=25}{size=+5}如此完美的思路，我想这次我又能再次轻易地获得一次荣誉吧。{/size}{/cps}{/color}"
    hide miaowink

    "{color=#6f7386}{cps=25}{size=+5}然而事与愿违，案子并没有那么简单。{/size}{/cps}{/color}"

    scene bghos with fade
    "{color=#6f7386}{cps=25}{size=+5}从法医的报告中发现校花的胃里存有大量安眠药，而这种安眠药只有专业人士从内部渠道才能获取。{/size}{/cps}{/color}"
    "{color=#6f7386}{cps=25}{size=+5}是谁，拥有这种渠道？我百思不得其解。{/size}{/cps}{/color}"

    show policesaid with dissolve
    p "{color=#336699}{cps=25}{size=+5}对了！小萌不是患有精神疾病吗？那么我想这个药物绝对是属于她的！{/size}{/cps}{/color}"
    p "{color=#336699}{cps=25}{size=+5}快！快！现在就把她铐起来！{/size}{/cps}{/color}"
    hide policesaid

    menu:
        "你的推理是？"

        "直接把小萌抓起来吧！＾＿＾":
            jump The_Fallen_God

        "不抓":
            jump Chapter2_Done

label The_Fallen_God:
    stop music
    play music c1 fadein 1.5 fadeout 1.5
    show miaosmile
    m "{color=#6f7386}{cps=25}{size=+5}直接把小萌抓起来吧{/size}{/cps}{/color}"
    hide miaosmile

    show policezz
    "{color=#6f7386}{cps=25}{size=+5}警长用不可置信的目光看向我，{/size}{/cps}{/color}"
    extend "{color=#6f7386}{cps=25}{size=+5}我明白，他开始怀疑我是伪人了。{/size}{/cps}{/color}"
    hide policezz

    show miaozzz
    m "{color=#6f7386}{cps=25}{size=+5}你真是乱来啊，还有那么多疑点没解开呢。{/size}{/cps}{/color}"
    m "{color=#6f7386}{cps=25}{size=+5}你不会可以用 chatGPT啊，三岁小孩都比你强=={/size}{/cps}{/color}"
    hide miaozzz

    "{color=#6f7386}{cps=25}{size=+5}同学们都怀疑我是伪人，自此，破案天才“陨落”了...{/size}{/cps}{/color}"

    scene bg2 with fade
    pause 6.0
    stop music

    jump Chapter1_Done
#return 

#########################################################################################################

label Chapter2_Done:
    stop music
    scene c2done with fade
    pause 3.5

    play music normal fadein 1.0 
    scene bghos
    show miaosaid with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}你还是太天真了。{/size}{/cps}{/color}"    
    m "{color=#6f7386}{cps=25}{size=+5}小萌患有的精神疾病是成人多动症，去医院能拿到的药物是兴奋剂才对，怎么可能是安眠药呢？{/size}{/cps}{/color}"
    hide miaosaid
    show miaothink with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}再说，今天，她没有离开过图书馆。{/size}{/cps}{/color}" 
    hide miaothink

    "{color=#000000}{cps=25}{size=+5}听完我的分析，警长再次陷入沉思，他无法在这四个嫌疑人中辨认凶手究竟是谁。{/size}{/cps}{/color}"
    
    show miaosmile
    m "{color=#6f7386}{cps=25}{size=+5}先别急，让我们询问他们的不在场证明。{/size}{/cps}{/color}"
    hide miaosmile
    stop music

    play music normal2 fadein 1.0 fadeout 1.0
    scene bglibraryxm
    e "{color=#b3b300}{cps=25}{size=+5}我..{/size}{/cps}{/color}" 
    extend "{color=#b3b300}{cps=25}{size=+5}案发的时候我在图书馆啊...{/size}{/cps}{/color}"
    e "{color=#b3b300}{cps=25}{size=+5}我真的什么都不知道...{/size}{/cps}{/color}"
                
    scene bgcake with fade
    show tgnor with dissolve
    j "{color=#935116}{cps=25}{size=+5}我当时在楼下小卖部给尤娜买蛋糕...{/size}{/cps}{/color}"
    j "{color=#935116}{cps=25}{size=+5}我和她是青梅竹马，就如传言所说的，我喜欢她很久了。{/size}{/cps}{/color}"
    j "{color=#935116}{cps=25}{size=+5}那么多年，她一边享受我对她的好，一边和其他男人搞暧昧...{/size}{/cps}{/color}"
    hide tgnor
    show tgsad 
    extend "{color=#935116}{cps=25}{size=+5}尽管如此，我还是放不下她..{/size}{/cps}{/color}"
    hide tgsad
                
    scene bgcanteen with fade
    show npynormal with dissolve
    h "{color=#999900}{cps=25}{size=+5}我？我一整个上午都待在食堂。{/size}{/cps}{/color}"
    h "{color=#999900}{cps=25}{size=+5}我和尤娜只是走得比较近，并没有在一起。{/size}{/cps}{/color}"
    h "{color=#999900}{cps=25}{size=+5}再说了，我跟她只是玩玩，感情这种东西本来就是你情我愿的。{/size}{/cps}{/color}"
    hide npynormal

    show shishinor with dissolve
    s "{color=#6e2c00}{cps=25}{size=+5}发生这种事真的很让人难过...尤娜是我最好的闺蜜...{/size}{/cps}{/color}"
    s "{color=#6e2c00}{cps=25}{size=+5}我一整个早上都待在食堂。{/size}{/cps}{/color}"
    extend "{color=#6e2c00}{cps=25}{size=+5}除了我，跟尤娜走的最近的就是陆宇吧？{/size}{/cps}{/color}"
    s "{color=#6e2c00}{cps=25}{size=+5}我和陆宇不熟，不会是他爱而不得，所以把尤娜毁掉吧？{/size}{/cps}{/color}"
    hide shishinor

    scene bgclose with fade
    show miaosmile with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}你俩一唱一和的把我当驴呢，今天学校食堂根本没开吧？{/size}{/cps}{/color}"
    m "{color=#6f7386}{cps=25}{size=+5}警长，把他们带回去问话吧。{/size}{/cps}{/color}"
    stop music

    play music normal fadein 1.5 fadeout 1.5
    scene bgpolice with fade
    show npynormal with dissolve
    h "{color=#999900}{cps=25}{size=+5}今天食堂确实没开，我和诗诗没撒谎，我们是在食堂外呢。{/size}{/cps}{/color}"
    hide npynormal
    show policethink with dissolve
    p "{color=#336699}{cps=25}{size=+5}食堂没开，你们在门口待了一上午？{/size}{/cps}{/color}"
    hide policethink
    show shishiangry with dissolve
    s "{color=#6e2c00}{cps=25}{size=+5}我们在谈论私事还不行么？非要打破砂锅问到底吗？！{/size}{/cps}{/color}"
    s "{color=#6e2c00}{cps=25}{size=+5}我们两个有私下恋情还不行么？尤娜又没有和时衍在一起！凭什么我不能追求我的幸福？！{/size}{/cps}{/color}"
    hide shishiangry
    show npynormal with dissolve
    h "{color=#999900}{cps=25}{size=+5}...{/size}{/cps}{/color}"
    extend "{color=#999900}{cps=25}{size=+5}疯女人...{/size}{/cps}{/color}"
    h "{color=#999900}{cps=25}{size=+5}是你自己一直缠着我好吧？算了...反正这就是我的不在场证明。{/size}{/cps}{/color}"
    hide npynormal
    show shishiangry with dissolve
    s "{color=#6e2c00}{cps=25}{size=+5}你说什么？！！是你说过会和尤娜一刀两断好吧！！？你就是想一脚踏两船！！{/size}{/cps}{/color}"
    s "{color=#6e2c00}{cps=25}{size=+5}难道说... 凶手该不会是你吧？你昨天不是和尤娜起了争执么？！{/size}{/cps}{/color}"
    hide shishiangry
    show policezz with dissolve
    p "{color=#336699}{cps=25}{size=+5}发生争执？快从实招来！{/size}{/cps}{/color}"
    hide policezz
    show npynormal with dissolve
    h "{color=#999900}{cps=25}{size=+5}...{/size}{/cps}{/color}"
    hide npynormal
    stop music

    play music fenshou fadein 1.5
    scene black with fade
    show npynormal at right 
    with dissolve 
    h "{color=#999900}{cps=25}{size=+5}我不想跟你继续维持这种关系了。{/size}{/cps}{/color}"

    show unacry at left 
    with dissolve
    u "{color=#ff6699}{cps=25}{size=+5}什么...{/size}{/cps}{/color}"
    extend "{color=#ff6699}{cps=25}{size=+5}我不要！!我不要啊！！{/size}{/cps}{/color}"
    u "{color=#ff6699}{cps=25}{size=+5}不要离开我好不好...时衍..{/size}{/cps}{/color}"
    hide npynormal
    show npyangry at right
    h "{color=#999900}{cps=25}{size=+5}你烦不烦？{/size}{/cps}{/color}"
    hide unacry
    show unavcry at left
    u "{color=#ff6699}{cps=25}{size=+5}好啊！你这样对我！我就去死！！！{/size}{/cps}{/color}"
    hide unavcry
    hide npyangry

    "{color=#000000}{cps=25}{size=+5}说罢，尤娜吞下了大量安眠药。{/size}{/cps}{/color}"
    show npyangry with dissolve
    h "{color=#999900}{cps=25}{size=+5}你冷静了再来找我，我不会理你了。{/size}{/cps}{/color}"
    hide npyangry
    "{color=#000000}{cps=25}{size=+5}... ...{/size}{/cps}{/color}"

    menu:
        "你认为谁是凶手？"

        "诗诗":
            jump Arrest_the_Bestie

        "时衍":
            jump Severe_Dependence

        "陆宇":
            jump Left_with_Nothing

        "都不是凶手":
            jump Chapter3_Done

#########################################################################################################

label Arrest_the_Bestie:
    stop music
    scene bgmemory with fade
    play music gl fadein 1.5
    show shishinor with dissolve
    s "{color=#6e2c00}{cps=25}{size=+5}我爸妈因为我是女孩，在我刚出世不久就把我卖掉了。{/size}{/cps}{/color}"
    "{color=#6e2c00}{cps=25}{size=+5}或许是这样，我从小就觊觎别人的幸福。{/size}{/cps}{/color}"
    "{color=#6e2c00}{cps=25}{size=+5}我的心里藏着一个没有人知道的秘密，尤娜也不知道。{/size}{/cps}{/color}"
    "{color=#6e2c00}{cps=25}{size=+5}从认识尤娜开始，我就特别羡慕她，她是一个完美的人，拥有完美的人生，想要什么就有什么。{/size}{/cps}{/color}"
    "{color=#6e2c00}{cps=25}{size=+5}我知道尤娜有很多阴暗面，但我认为那是她被爱的底气。{/size}{/cps}{/color}"
    "{color=#6e2c00}{cps=25}{size=+5}我想方设法接近尤娜，终于成了她身边不可或缺的存在，即使是跟班一样的存在。{/size}{/cps}{/color}"
    "{color=#6e2c00}{cps=25}{size=+5}我知道很多人讨厌尤娜，她有很多仇人。{/size}{/cps}{/color}"
    extend "{color=#6e2c00}{cps=25}{size=+5}但是没关系，我会一直陪着尤娜的，有我在就好了。{/size}{/cps}{/color}"

    hide shishinor

    show shishiz 
    "{color=#6e2c00}{cps=25}{size=+5}有一天，我发现尤娜恋爱了。{/size}{/cps}{/color}"
    hide shishiz

    show shishiangry 
    "{color=#6e2c00}{cps=25}{size=+5}那个男人叫时衍，我知道他，花花公子一个。{/size}{/cps}{/color}"
    "{color=#6e2c00}{cps=25}{size=+5}于是我暗中调查他，我要找到他出轨的证据！{/size}{/cps}{/color}"
    extend "{color=#6e2c00}{cps=25}{size=+5}他根本不配站在尤娜身边！！{/size}{/cps}{/color}"
    "{color=#6e2c00}{cps=25}{size=+5}他和尤娜并没有确定关系。{/size}{/cps}{/color}"
    extend "{color=#6e2c00}{cps=25}{size=+5}既然他们没有在一起，为什么我不能追求我的幸福？！！{/size}{/cps}{/color}"
    hide shishiangry

    show shishiz 
    "{color=#6e2c00}{cps=25}{size=+5}随着我的深入调查，我发现时衍接近尤娜的原因不简单。{/size}{/cps}{/color}"
    hide shishiz

    show shishiangry
    extend "{color=#6e2c00}{cps=25}{size=+5}为了揭发他的真面目，我假装接近他，我想让尤娜知道他根本就不是值得托付的人！！{/size}{/cps}{/color}"
    "{color=#6e2c00}{cps=25}{size=+5}我不想让尤娜伤心... 我一定要让他和尤娜分手！！！{/size}{/cps}{/color}"
    hide shishiz

    scene black with dissolve
    "{color=#6e2c00}{cps=25}{size=+5}在我计划快成功的时候，尤娜死了。{/size}{/cps}{/color}"
    "{color=#6e2c00}{cps=25}{size=+5}为什么！为什么！为什么！为什么！为什么！为什么！为什么！为什么！为什么！为什么！为什么！为什么！为什么！为什么！{/size}{/cps}{/color}"
    extend "{color=#6e2c00}{cps=25}{size=+5}为什么！为什么！为什么！为什么！为什么！为什么！为什么！为什么！为什么！为什么！为什么！为什么！为什么！为什么！{/size}{/cps}{/color}"

    "{color=#000000}{cps=25}{size=+10}... ...{/size}{/cps}{/color}"

    scene bgpolice with fade
    show policesaid with dissolve
    p "{color=#336699}{cps=25}{size=+5}诗诗在拘留室自杀了。{/size}{/cps}{/color}"
    p "{color=#336699}{cps=25}{size=+5}或许是畏罪自杀吧，但是事情好像没那么简单，我们在她的遗物里发现一封信。{/size}{/cps}{/color}"
    hide policesaid

    "{color=#6f7386}{cps=25}{size=+5}那是一封没送出去的情书。{/size}{/cps}{/color}"
    scene black with dissolve

    "{color=#6e2c00}{cps=25}{size=+5}如果我是男生就好了。{/cps}{/color}{/size}"
    extend "{color=#6e2c00}{cps=25}{size=+5}这是第几次这样感慨了呢？{/size}{/cps}{/color}"
    "{color=#6e2c00}{cps=25}{size=+5}算了。{/cps}{/color}{/size}"
    "{color=#6e2c00}{cps=25}{size=+5}下辈子吧，尤娜。{/size}{/cps}{/color}"
    extend "{color=#6e2c00}{cps=25}{size=+5}下辈子{/size}{/cps}{/color}"
    extend "{color=#6e2c00}{cps=25}{size=+5}我会保护你的。{/size}{/cps}{/color}"
    
    scene bg3 with fade
    pause 6.0
    
    jump Chapter2_Done
    play music gl fadeout 1.5

#return################################################################################################# 

label Severe_Dependence:
    stop music
    pause 1.0
    play music npystory fadein 1.5
    scene black with fade
    h "{color=#999900}{cps=25}{size=+5}我见过一个很漂亮也很善良的人，她死了。{/size}{/cps}{/color}"

    scene bgstory with fade
    show npynormal with dissolve
    "{color=#999900}{cps=25}{size=+5}我知道尤娜很享受被人追捧的感觉，于是我也只和她保持着暧昧的关系。{/size}{/cps}{/color}"
    "{color=#999900}{cps=25}{size=+5}我很了解她，知道她喜欢什么，知道她所有阴暗面，她也很依赖、信任我。{/size}{/cps}{/color}"
    "{color=#999900}{cps=25}{size=+5}我知道，她嫉妒任何可能威胁到她地位的女生。{/size}{/cps}{/color}"
    "{color=#999900}{cps=25}{size=+5}她嫉妒那些长相出众的女生、嫉妒家境富裕的女生、嫉妒成绩好的女生，她会对她们实施校园暴力。{/size}{/cps}{/color}"
    "{color=#999900}{cps=25}{size=+5}她长相出众，享受过颜值带来的红利的人更容易焦虑，因为害怕失去。{/size}{/cps}{/color}"
    hide npynormal

    "{color=#999900}{cps=25}{size=+5}收到尤娜的死讯时，我正和她的闺蜜诗诗吵架。{/size}{/cps}{/color}"
    "{color=#999900}{cps=25}{size=+5}是的，我不止和她搞暧昧，我还在背后和她闺蜜搞暧昧，而且她知道了。{/size}{/cps}{/color}"
    "{color=#999900}{cps=25}{size=+5}我能感觉到，诗诗根本不喜欢我，甚至有点厌恶我。{/size}{/cps}{/color}"
    "{color=#999900}{cps=25}{size=+5}不管她出自什么原因，反正我的目的达到了。{/size}{/cps}{/color}"

    show npyangry with dissolve
    "{color=#999900}{cps=25}{size=+5}她当然忍受不了背叛的感觉，但是她又离不开我，所以总是只能采取极端的方式逼我留在她身边。{/size}{/cps}{/color}"
    hide npyangry
    "{color=#999900}{cps=25}{size=+5}前一晚，我们大吵一架，她服下了大量安眠药。{/size}{/cps}{/color}"
    show npynormal with dissolve
    "{color=#999900}{cps=25}{size=+5}我对诗诗是真心的吗？当然不是。{/size}{/cps}{/color}"
    "{color=#999900}{cps=25}{size=+5}如我所说的，我太懂她了，所以我也知道怎么毁了她。{/size}{/cps}{/color}"
    "{color=#999900}{cps=25}{size=+5}闺蜜的欺骗、“恋人”的背叛，已经突破了她的心里防线，她已经开始自卑了。{/size}{/cps}{/color}"
    hide npynormal
    "{color=#999900}{cps=25}{size=+5}为什么我想毁了她？{/size}{/cps}{/color}"

    scene bgmountain with fade
    "{color=#999900}{cps=25}{size=+5}小时候，身为富家子弟的我被拐到山区。{/size}{/cps}{/color}"
    show childnpycry with dissolve
    h "{color=#999900}{cps=25}{size=+5}救命啊！有没有人帮帮我！！！{/size}{/cps}{/color}"
    extend "{color=#999900}{cps=25}{size=+5}呜呜..怎么办... 我好害怕....呜呜呜....{/size}{/cps}{/color}"
    hide childnpycry
    show childimoto with dissolve
    i "{color=#737373}{cps=25}{size=+5}你.. 你别怕！我来救你出去！{/size}{/cps}{/color}"
    "{color=#999900}{cps=25}{size=+5}少女小小的身躯背起我，一路狂奔，逃离这无尽的大山。{/size}{/cps}{/color}"
    "{color=#999900}{cps=25}{size=+5}如果没有她，我想我的下场应该很凄惨吧。{/size}{/cps}{/color}"
    hide childimoto
    scene bgstory with fade
    "{color=#999900}{cps=25}{size=+5}离开大山后，她为我包扎，抹去我眼角上的泪。{/size}{/cps}{/color}"
    show childnpycry with dissolve
    h "{color=#999900}{cps=25}{size=+5}你.. {/size}{/cps}{/color}"
    extend "{color=#999900}{cps=25}{size=+5}你是天使吗？{/size}{/cps}{/color}"
    hide childnpycry
    show childimoto2 with dissolve
    i "{color=#737373}{cps=25}{size=+5}笨蛋！世界上怎么可能有天使！{/size}{/cps}{/color}"
    hide childimoto2
    show childimoto
    extend "{color=#737373}{cps=25}{size=+5}我可是女侠！嘿嘿！{/size}{/cps}{/color}"
    hide childimoto
    show childnpynor with dissolve
    h "{color=#999900}{cps=20}{size=+5}... ...{/size}{/cps}{/color}"
    hide childnpynor
    "{color=#999900}{cps=20}{size=+5}有人说，当真爱出现的时候，整个世界的时间就会暂停下来。{/size}{/cps}{/color}"
    "{color=#999900}{cps=20}{size=+5}那个女孩，深深地烙印在我的心中。{/size}{/cps}{/color}"
    "{color=#999900}{cps=20}{size=+5}她叫洛羽，温柔细腻，宛如轻盈的羽毛。{/size}{/cps}{/color}"
    "{color=#000000}{cps=20}{size=+10}... ...   {/size}{/cps}{/color}"
    extend "{color=#000000}{cps=20}{size=+10}   ... ...{/size}{/cps}{/color}"
    "{color=#999900}{cps=25}{size=+5}从什么时候开始，她不爱笑了呢。{/size}{/cps}{/color}"
    "{color=#999900}{cps=25}{size=+5}我记起来了，是从初中开始。{/size}{/cps}{/color}"
    show imotosad with dissolve
    "{color=#999900}{cps=25}{size=+5}她的眼神充满忧郁，我的心口不禁隐隐作痛。{/size}{/cps}{/color}"
    "{color=#999900}{cps=25}{size=+5}她再也没有出现在学校，我也找不到她，她只短暂地出现在我的世界。{/size}{/cps}{/color}"
    extend "{color=#999900}{cps=25}{size=+5}匆匆出现，匆匆离去。{/size}{/cps}{/color}"
    hide imotosad

    "{color=#999900}{cps=25}{size=+5}后来我才知道，这个女孩被尤娜霸凌，撒手人寰了。{/size}{/cps}{/color}"
    extend "{color=#999900}{cps=25}{size=+5}她患有严重的自闭症。{/size}{/cps}{/color}"
    "{color=#999900}{cps=25}{size=+5}于是，我接近尤娜，一步一步地毁掉她。{/size}{/cps}{/color}"
    "{color=#999900}{cps=25}{size=+5}尤娜，从来不知道珍惜。{/size}{/cps}{/color}"

    scene bg4 with fade
    pause 6.0

    jump Chapter2_Done

#return###############################################################################################

label Left_with_Nothing:
    stop music
    play music tgstory fadein 1.5
    scene bgbreakfast with fade
    show tgsad with dissolve
    j "{color=#935116}{cps=25}{size=+5}再见面时，我强忍身体的不适给尤娜递去了他跟时衍的早餐。{/size}{/cps}{/color}"
    "{color=#935116}{cps=25}{size=+5}此时香蕉为什么是黄色的都是错误的，更何况手上还是心上人和情敌的早餐。{/size}{/cps}{/color}"
    hide tgsad 
    show tgangry with dissolve
    j "{color=#935116}{cps=25}{size=+5}这是最后一次了，我不会再干扰你们的感情了。{/size}{/cps}{/color}"
    "{color=#935116}{cps=25}{size=+5}虽然悲伤，但是残存的理智告诉我再这样下去实在太贱了。{/size}{/cps}{/color}"
    hide tgangry    

    show unaangry with dissolve
    u "{color=#ff6699}{cps=25}{size=+5}你什么意思？你再这样我就不理你了。{/size}{/cps}{/color}"
    hide unaangry
    "{color=#000000}{cps=25}{size=+5}尤娜又自信了，果然这些年的追捧让她长脸了。{/size}{/cps}{/color}"
    
    show tgangry with dissolve
    j "{color=#935116}{cps=25}{size=+5}就这样吧。{/size}{/cps}{/color}"
    j "{color=#935116}{cps=25}{size=+5}没必要，不好玩。{/size}{/cps}{/color}"
    hide tgangry
    show unaangry with dissolve
    u "{color=#ff6699}{cps=25}{size=+5}滚！！{/size}{/cps}{/color}"
    hide unaangry
    show tgsad with dissolve
    j "{color=#935116}{cps=25}{size=+10}... ...   {/size}{/cps}{/color}"
    extend "{color=#935116}{cps=25}{size=+5}   ... ...{/size}{/cps}{/color}"
    hide tgsad
    "{color=#000000}{cps=25}{size=+5}陆宇马上转头，离开了。{/size}{/cps}{/color}"
    show unaangry with dissolve
    u "{color=#ff6699}{cps=25}{size=+5}他怎么..{/size}{/cps}{/color}"
    extend "{color=#ff6699}{cps=25}{size=+5}变了...{/size}{/cps}{/color}"
    hide unaangry

    scene bgtg with fade
    show tgsad with dissolve
    j "{color=#935116}{cps=25}{size=+5}每次用自己的时间金钱成全他们的感情， 最后因为天天跟在尤娜身后而成绩一落千丈  {/size}{/cps}{/color}"
    extend "{color=#935116}{cps=25}{size=+5}  也落得钱包里没有一分钱的下场，只能找家里借钱来勉强苟活。{/size}{/cps}{/color}"
    "{color=#935116}{cps=25}{size=+5}我想越不甘心, 为什么要让他们活得光鲜亮丽，自己像个阴沟里等着吃食的老鼠。{/size}{/cps}{/color}"
    hide tgsad
    show tgangry with dissolve
    "{color=#935116}{cps=25}{size=+5}尤娜心脏不好，她需要每天吃药控制病情。{/size}{/cps}{/color}"
    "{color=#935116}{cps=25}{size=+5}我那么爱她... 她为什么从来不珍惜我？时衍有什么好的？！{/size}{/cps}{/color}"
    "{color=#935116}{cps=25}{size=+5}给她小小的惩罚，不过分吧？{/size}{/cps}{/color}"
    hide tgangry
    "{color=#000000}{cps=25}{size=+5}陆宇偷走了尤娜的药。{/size}{/cps}{/color}"

    scene bgclass with fade
    u "{color=#ff6699}{cps=25}{size=+5}欸..？我的药呢？{/size}{/cps}{/color}"
    show unatalk with dissolve
    u "{color=#ff6699}{cps=25}{size=+5}喂！陆宇！{/size}{/cps}{/color}"
    extend "{color=#ff6699}{cps=25}{size=+5}你有没有看见我的药？{/size}{/cps}{/color}"
    hide unatalk
    show tgnor with dissolve
    "{color=#935116}{cps=25}{size=+5}我装作没听见，继续埋头写作业。{/size}{/cps}{/color}"
    hide tgnor
    show unatalk with dissolve
    u "{color=#ff6699}{cps=25}{size=+5}算了.. 不找了{/size}{/cps}{/color}"
    u "{color=#ff6699}{cps=25}{size=+5}那蠢猪约我到体育馆，你陪我去。{/size}{/cps}{/color}"
    hide unatalk 
    show tgnor with dissolve
    j "{color=#935116}{cps=25}{size=+5}自己去，我没空。{/size}{/cps}{/color}"
    hide tgnor 

    show unaangry with dissolve
    u "{color=#ff6699}{cps=25}{size=+5}算了！自己去就自己去！{/size}{/cps}{/color}"
    hide unaangry
    "{color=#935116}{cps=25}{size=+5}她明明自己会去啊，为什么总是要使唤我呢？{/size}{/cps}{/color}"

    scene black with fade
    "{color=#935116}{cps=25}{size=+5}不久后，我收到了尤娜的死讯。{/size}{/cps}{/color}"
    "{color=#935116}{cps=25}{size=+5}警方很快就来了，我也被列为嫌疑人中。{/size}{/cps}{/color}"
    "{color=#935116}{cps=25}{size=+5}问我难过吗？挺难过的。{/size}{/cps}{/color}"
    "{color=#935116}{cps=25}{size=+5}我和尤娜那么多年的感情...{/size}{/cps}{/color}"
    "{color=#935116}{cps=25}{size=+5}青梅竹马为什么敌不过天降？{/size}{/cps}{/color}"

    scene bgpolice with fade
    show policezz with dissolve
    p "{color=#336699}{cps=25}{size=+5}如果不是你把药藏起来，尤娜会那么快就在水里失去意识吗？！{/size}{/cps}{/color}"
    "{color=#935116}{cps=25}{size=+5}尤娜的死因真的因为我吗？约她到体育馆的那头“蠢猪”到底是谁？{/size}{/cps}{/color}"
    "{color=#935116}{cps=25}{size=+5}如果有我陪着尤娜的话...{/size}{/cps}{/color}"
    "{color=#935116}{cps=25}{size=+5}算了。{/size}{/cps}{/color}"
    extend "{color=#935116}{cps=25}{size=+5}没有什么意义了。{/size}{/cps}{/color}"
    "{color=#935116}{cps=25}{size=+5}我招了所有事情。{/size}{/cps}{/color}"
    extend "{color=#935116}{cps=25}{size=+5}最终，我被判刑了。{/size}{/cps}{/color}"
    "{color=#000000}{cps=25}{size=+5}人总要为自己年少的不懂事买单。{/size}{/cps}{/color}"

    scene black with fade
    "{color=#000000}{cps=25}{size=+5}... ...  {/size}{/cps}{/color}"
    play music tgstory fadeout 1.5
    extend "{color=#000000}{cps=25}{size=+5}  ... ...{/size}{/cps}{/color}"

    scene bgroom with fade
    show childuna at right
    play music jbs
    with dissolve
    u "{color=#ff6699}{cps=25}{size=+5}我又发噩梦了，你来陪我吧。{/size}{/cps}{/color}"
    show childly at left
    with dissolve
    j "{color=#935116}{cps=25}{size=+5}真拿你没办法，你怎么老发噩梦...{/size}{/cps}{/color}"
    u "{color=#ff6699}{cps=25}{size=+5}我梦见我死了，大家都讨厌我。{/size}{/cps}{/color}"
    extend "{color=#ff6699}{cps=25}{size=+5}你也是。{/size}{/cps}{/color}"
    j "{color=#935116}{cps=25}{size=+5}才不会呢！我才不会讨厌尤娜酱呢！{/size}{/cps}{/color}"
    extend "{color=#935116}{cps=25}{size=+5}我最喜欢尤娜酱了。{/size}{/cps}{/color}"
    u "{color=#ff6699}{cps=25}{size=+5}你答应我的。{/size}{/cps}{/color}"
    extend "{color=#ff6699}{cps=25}{size=+5}拉勾勾。{/size}{/cps}{/color}"
    hide childly with dissolve
    hide childuna with dissolve
    "{color=#000000}{cps=25}{size=+5}拉勾勾，说谎的人要断手指哦。{/size}{/cps}{/color}"

    j "{color=#935116}{cps=25}{size=+5}我会永远守护尤娜酱！{/size}{/cps}{/color}"
    u "{color=#ff6699}{cps=25}{size=+5}尤娜酱永远和陆宇天下第一好！{/size}{/cps}{/color}"

    scene black with fade
    pause 1.0
    "{color=#935116}{cps=25}{size=+5}或许承诺说出口的瞬间 我们都想永远。{/size}{/cps}{/color}"

    scene bg5 with fade
    pause 6.0

    jump Chapter2_Done
#return

label Chapter3_Done:
    stop music
    
    scene c3done with fade
    pause 3.5

    play music fenshou fadein 1.5
    scene bgpolice with fade
    show policethink with dissolve
    p "{color=#336699}{cps=25}{size=+5}喵喵同学，你怎么看？{/size}{/cps}{/color}"
    hide policethink
    show miaosaid with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}凶手是小萌。{/size}{/cps}{/color}"    
    hide miaosaid
    show policezz with dissolve
    p "{color=#336699}{cps=25}{size=+5}你不是说她有不在场证明吗？{/size}{/cps}{/color}"
    extend "{color=#336699}{cps=25}{size=+5}而且她也没办法搞到特殊的安眠药啊？！{/size}{/cps}{/color}"

    hide policezz
    show miaothink with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}其实，我算是唯一目击证人。{/size}{/cps}{/color}"
    hide miaothink

    scene bgac with fade
    show miaothink with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}今天早晨我抵达学校的时候经过了体育馆，我亲眼目睹小萌进入了学校的体育馆。{/size}{/cps}{/color}"
    m "{color=#6f7386}{cps=25}{size=+5}一大清早，一个人到体育馆？这不合逻辑吧？{/size}{/cps}{/color}"
    extend "{color=#6f7386}{cps=25}{size=+5}我想，她一定是为了赴某人的约才会前往体育馆。{/size}{/cps}{/color}"
    m "{color=#6f7386}{cps=25}{size=+5}而如果是校花单独约她，她怎么想也知道是要被团体霸凌了吧？{/size}{/cps}{/color}"
    hide miaothink
    show miaosaid 
    extend "{color=#6f7386}{cps=25}{size=+5}那么为什么她不选择逃避，而是选择赴约呢？{/size}{/cps}{/color}"
    hide miaosaid


menu:
    "为什么她不选择逃避，而是选择赴约呢？"

    "她被催眠了":
        jump A_dream

    "她是邀约方":
        jump Chapter4_Done

label A_dream:
    stop music
    scene bgclass with fade
    play music dream fadein 1.5
    "{color=#000000}{cps=25}{size=+5}收到小萌的邀约时，尤娜轻蔑一笑，将纸条揉成一团丢进垃圾桶里。{/size}{/cps}{/color}"
    show unaangry with dissolve
    u "{color=#ff6699}{cps=25}{size=+5}这家伙是中邪了吗？{/size}{/cps}{/color}"
    extend "{color=#ff6699}{cps=25}{size=+5}平时大老远见到她就跑得不见影子，这次哪来的胆子约我见面？{/size}{/cps}{/color}"
    "{color=#000000}{cps=25}{size=+5}尤娜还是应约了，因为她不相信那样懦弱的人能做出什么事。{/size}{/cps}{/color}"

    scene bgswim with fade
    show unaangry with dissolve
    u "{color=#ff6699}{cps=25}{size=+5}喂！{/size}{/cps}{/color}"
    extend "{color=#ff6699}{cps=25}{size=+5}你叫我来是要干什么！{/size}{/cps}{/color}"
    hide unaangry
    
    "{color=#000000}{cps=25}{size=+5}尤娜用力推了小萌的肩，小萌往后退了几步。{/size}{/cps}{/color}"
    show xiaomengnor with dissolve
    e "{color=#b3b300}{cps=25}{size=+5}... ...{/size}{/cps}{/color}"
    hide xiaomengnor
    
    show unaangry with dissolve
    u "{color=#ff6699}{cps=25}{size=+5}说话啊！你这哑巴！{/size}{/cps}{/color}"
    hide unaangry
    
    show xiaomengnor with dissolve
    e "{color=#b3b300}{cps=25}{size=+5}... ...{/size}{/cps}{/color}"
    hide xiaomengnor

    show unaangry with dissolve
    u "{color=#ff6699}{cps=25}{size=+5}喂...{/size}{/cps}{/color}"
    hide unaangry
    
    show xmcry with dissolve
    e "{color=#b3b300}{cps=25}{size=+5}死吧！死吧！{/size}{/cps}{/color}"
    hide xmcry
    "{color=#000000}{cps=25}{size=+5}小萌把尤娜推下游泳池。{/size}{/cps}{/color}"

    scene bgdrop with fade
    u "{color=#ff6699}{cps=25}{size=+5}救命！！救命啊！！{/size}{/cps}{/color}"
    u "{color=#ff6699}{cps=25}{size=+5}救救我..呜呜呜...{/size}{/cps}{/color}"

    show bgswim with fade
    show xmshock with dissolve
    e "{color=#b3b300}{cps=25}{size=+5}我...{/size}{/cps}{/color}"
    extend "{color=#b3b300}{cps=25}{size=+5}我做了什么...{/size}{/cps}{/color}"
    e "{color=#b3b300}{cps=25}{size=+5}尤娜..尤娜会游泳的！！{/size}{/cps}{/color}"
    e "{color=#b3b300}{cps=25}{size=+5}如果我把她拉上来.. 她会欺负我的！！{/size}{/cps}{/color}"
    hide xmshock

    show xmangry with dissolve
    e "{color=#b3b300}{cps=25}{size=+5}尤娜这贱人！！不是老欺负我吗！！{/size}{/cps}{/color}"
    e "{color=#b3b300}{cps=25}{size=+5}反正她会游泳.. 不理她就好了！！{/size}{/cps}{/color}"
    hide xmangry with dissolve

    show xiaomengnor with dissolve
    e "{color=#b3b300}{cps=25}{size=+5}没人... {/size}{/cps}{/color}"
    extend "{color=#b3b300}{cps=25}{size=+5}没人看见吧....{/size}{/cps}{/color}"
    hide xiaomengnor

    scene black with dissolve    
    "{color=#6f7386}{cps=25}{size=+5}小萌完全相信自己做出来的梦呢。{/size}{/cps}{/color}"

    scene bg6 with fade
    pause 6.0
    
    jump Chapter3_Done

#return##########################################################################################

label Chapter4_Done:
    stop music
    scene bgpolice with fade
    play music dream fadein 1.5
    show miaothink with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}答案只有一个，因为她是邀约方。{/size}{/cps}{/color}"
    hide miaothink

    show xmcry with dissolve
    e "{color=#b3b300}{cps=25}{size=+5}不是的... {/size}{/cps}{/color}"
    extend "{color=#b3b300}{cps=25}{size=+5}不是的...！！{/size}{/cps}{/color}"
    hide xmcry
    show xmshock
    extend "{color=#b3b300}{cps=25}{size=+5}我是推了她没错... 但是她会游泳啊？！{/size}{/cps}{/color}"
    e "{color=#b3b300}{cps=25}{size=+5}她怎么可能会溺死..！{/size}{/cps}{/color}"
    hide xmshock
    show xmcry
    extend "{color=#b3b300}{cps=25}{size=+5}安眠药不是我给的... 不是我！！{/size}{/cps}{/color}"
    hide xmcry

    show policezz with dissolve
    p "{color=#336699}{cps=25}{size=+5}把她带下去！{/size}{/cps}{/color}"
    hide policezz
    
    show xmcry with dissolve
    e "{color=#b3b300}{cps=25}{size=+5}不是我... 不是...我真的什么都不记得了...{/size}{/cps}{/color}"
    hide xmcry

    show miaothink with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}据调查，安眠药是校花威胁时衍的手段。{/size}{/cps}{/color}"
    extend "{color=#6f7386}{cps=25}{size=+5}所以，你间接杀人了。{/size}{/cps}{/color}"
    m "{color=#6f7386}{cps=25}{size=+5}她昨晚吞下了大量的安眠药，今早来上学，安眠药的副作用还没过去呢。{/size}{/cps}{/color}"
    extend "{color=#6f7386}{cps=25}{size=+5}所以在你把她推下泳池的时候，她已经没有力气再反抗了。{/size}{/cps}{/color}"
    hide miaothink

    show miaosaid with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}我想，她脸上的划痕也是你在扇她的时候留下的口子吧。{/size}{/cps}{/color}"
    hide miaosaid

    show xmcry with dissolve
    e "{color=#b3b300}{cps=25}{size=+5}不是我！！我什么都不知道...！！！{/size}{/cps}{/color}"
    hide xmcry

    show miaosmile with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}警长，可以把她带走了。{/size}{/cps}{/color}"
    hide miaosmile

    show policesaid with dissolve
    p "{color=#336699}{cps=25}{size=+5}还得是你啊！破案小天才！{/size}{/cps}{/color}"
    hide policesaid

    scene c4done with fade
    pause 3.5

    scene black with fade
########################################################################################################

menu:
    "你觉得世界上有完美的犯罪吗？"

    "是":
        jump Chapter5_Done

    "否":
        jump Materialism

label Materialism:
    stop music
    scene bgclass with fade
    play music imoto fadein 1.5
    "{color=#6f7386}{cps=25}{size=+5}案件调查总算是告一段落，舆论也逐渐平息。{/size}{/cps}{/color}"
    "{color=#6f7386}{cps=25}{size=+5}校园墙上偶尔还是会出现校花的名字  {/size}{/cps}{/color}"
    extend "{color=#6f7386}{cps=25}{size=+5}只是从以前为受害者愤愤不平的帖子转成对校花的惋惜。{/size}{/cps}{/color}"
    "{color=#6f7386}{cps=25}{size=+5}有人说她自食其果，这是仗势欺人的报应。{/size}{/cps}{/color}"

    show znormal with dissolve
    z "{color=#666666}{cps=25}{size=+5}真奇怪啊喵喵同学。{/size}{/cps}{/color}"
    hide znormal

    show miaosaid with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}怎么了吗？{/size}{/cps}{/color}"
    hide miaosaid

    show znormal with dissolve
    z "{color=#666666}{cps=25}{size=+5}一切的矛头都指向小萌，这反而很奇怪吧？{/size}{/cps}{/color}"
    z "{color=#666666}{cps=25}{size=+5}她就像... 替罪羊一样。{/size}{/cps}{/color}"
    hide znormal

    show miaosaid with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}嗯.. {/size}{/cps}{/color}"
    extend "{color=#6f7386}{cps=25}{size=+5}我想是你多虑了吧？{/size}{/cps}{/color}"
    m "{color=#6f7386}{cps=25}{size=+5}毕竟小萌也认罪了，人是她推的。{/size}{/cps}{/color}"
    hide miaosaid

    show znormal with dissolve
    z "{color=#666666}{cps=25}{size=+5}是吗？{/size}{/cps}{/color}"
    z "{color=#666666}{cps=25}{size=+5}我有晨跑的习惯，恰巧今天的路线有经过体育馆。{/size}{/cps}{/color}"
    extend "{color=#666666}{cps=25}{size=+5}我看见你从里面出来，而不是经过。{/size}{/cps}{/color}"
    hide znormal 
    
    show zthank 
    z "{color=#666666}{cps=25}{size=+5}你，撒谎了吧？{/size}{/cps}{/color}"
    hide zthank

    show miaosaid with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}我想这并不重要吧，我只是不想卷入麻烦。{/size}{/cps}{/color}"
    hide miaosaid
    show miaothink
    m "{color=#6f7386}{cps=25}{size=+5}也希望你不要把我卷入麻烦。{/size}{/cps}{/color}"
    hide miaothink

    show znormal with dissolve
    z "{color=#666666}{cps=25}{size=+5}虽然我不知道你怎么办到的，但你真是聪明呢。{/size}{/cps}{/color}"
    extend "{color=#666666}{cps=25}{size=+5}如果我妹妹早点认识你就好了。{/size}{/cps}{/color}"
    hide znormal
    scene bg11 with fade
    show znormal with dissolve
    z "{color=#666666}{cps=25}{size=+5}你不知道吧，小萌和尤娜在初中的时候是形影不离的好朋友，她们的心里一样扭曲。{/size}{/cps}{/color}"
    hide znormal
    
    scene bgzz with fade
    show imotos with dissolve
    z "{color=#666666}{cps=25}{size=+5}我有一个妹妹，她特别漂亮。{/size}{/cps}{/color}"
    extend "{color=#666666}{cps=25}{size=+5}她患有自闭症。{/size}{/cps}{/color}"
    extend "{color=#666666}{cps=25}{size=+5}为了能让她融入普通人的生活，我没有把她送到特殊学校。{/size}{/cps}{/color}"
    z "{color=#666666}{cps=25}{size=+5}小萌和尤娜从初一开始就欺凌我妹妹。{/size}{/cps}{/color}"
    hide imotos
    
    show zsad with dissolve
    z "{color=#666666}{cps=25}{size=+5}她们拿烟头烫她的身体、拿小刀在她身上划了很多口子、把汽水灌进她的鼻子里、拿辣椒油倒进她的眼睛...{/size}{/cps}{/color}"
    extend "{color=#666666}{cps=25}{size=+5}还有很多很多...{/size}{/cps}{/color}"
    z "{color=#666666}{cps=25}{size=+5}因为妹妹的疾病，她在家里也受到不好的待遇。{/size}{/cps}{/color}"
    z "{color=#666666}{cps=25}{size=+5}我决定让她住宿而不走读，所以我不知道她在学校遭受了非人的对待。{/size}{/cps}{/color}"
    hide zsad
    z "{color=#666666}{cps=25}{size=+5}她是怎么离开我的呢？{/size}{/cps}{/color}"

    scene bgup with fade
    show zsad with dissolve
    z "{color=#666666}{cps=25}{size=+5}初三那年，小萌为了讨好尤娜，叫了几个小混混企图侵犯我妹妹。{/size}{/cps}{/color}"
    hide zsad
    show imotoat with dissolve
    z "{color=#666666}{cps=25}{size=+5}我妹妹难敌四手，她只能跑，然后她就从顶楼失足摔死了。{/size}{/cps}{/color}"
    hide imotoat
    z "{color=#666666}{cps=25}{size=+5}妹妹那么乐观的一个人，怎么可能是失足摔死呢？{/size}{/cps}{/color}"
    z "{color=#666666}{cps=25}{size=+5}肯定是他们把她逼死的。{/size}{/cps}{/color}"
    extend "{color=#666666}{cps=25}{size=+5}我想或许也是因为这件事，小萌和尤娜才会反目成仇吧{/size}{/cps}{/color}"

    scene bgclass with fade
    show miaosad with dissolve
    m "{color=#6f7386}{cps=25}{size=+5}... ...{/size}{/cps}{/color}"
    hide miaosad

    show zthank with dissolve
    z "{color=#666666}{cps=25}{size=+5}所以  {/size}{/cps}{/color}"
    extend "{color=#666666}{cps=25}{size=+5}谢谢你。{/size}{/cps}{/color}"
    hide zthank

    scene black with fade
    m "{color=#6f7386}{cps=25}{size=+5}洛翼同学的猜测没错，尤娜的死算是我一手促成的。{/size}{/cps}{/color}"
    m "{color=#6f7386}{cps=25}{size=+5}那你呢？{/size}{/cps}{/color}"
    m "{color=#6f7386}{cps=25}{size=+5}你为什么不怀疑我？{/size}{/cps}{/color}"
    extend "{color=#6f7386}{cps=25}{size=+5}视角代表正义吗？{/size}{/cps}{/color}"

    scene bg7 with fade
    pause 5.0

    jump Chapter4_Done

#return

label Chapter5_Done:
    stop music
    scene bgpwalk with fade
    show miaoxd with dissolve
    play music last fadein 1.5
    "{color=#6f7386}{cps=25}{size=+5}我看着他们远去的背影。{/size}{/cps}{/color}"
    "{color=#6f7386}{cps=25}{size=+5}我就说吧，没有人会比我更了解这类型的案子。{/size}{/cps}{/color}"
    hide miaoxd
    show miaosmile with dissolve
    "{color=#6f7386}{cps=25}{size=+5}安眠药只有从专业渠道能获取，我就是专业人士，不是吗?{/size}{/cps}{/color}"
    "{color=#6f7386}{cps=25}{size=+5}登记簿和大门监控都是巧合吗？{/size}{/cps}{/color}"
    "{color=#6f7386}{cps=25}{size=+5}校花确实会游泳，但是万一她没有办法使劲呢？{/size}{/cps}{/color}"
    hide miaosmile
    show miaoxd with dissolve
    "{color=#6f7386}{cps=25}{size=+5}我说过了，我是唯一目击证人。{/size}{/cps}{/color}"
    hide miaosmile
    "{color=#6f7386}{cps=25}{size=+5}这算是借刀杀人的完美犯罪吧。{/size}{/cps}{/color}"

    scene black with dissolve
    "{color=#6f7386}{cps=25}{size=+5}站在我的角度，你是否觉得我无罪？{/size}{/cps}{/color}"

    scene clast with fade
    pause 5.0

return
