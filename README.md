# Auto_SelfReport-for-SHU

上海大学每日一报自动化脚本

Auto_SelfReport.py 是基于Selnium的自动填报脚本

SelfReport Setup.exe 是Windows10环境下的脚本配置引导程序

====================================
Copyright (c) 2020-2021 Steve D. J.. All Rights Reserved.	←你根本不必在乎Steve是谁，用就完了！
====================================

	划重点！！！		
	↓↓↓
****************************************************************************************************************************************
！！！请务必右键点击 SelfReport_Setup.exe 然后选择“以管理员身份运行”，否则必然会导致环境变量无法正常添加！！！
本程序默认用户已经安装了最新版的Chrome浏览器，如果你没有安装，请使用附带文件夹ExternalTools中的ChromeSetup.exe自行安装！
****************************************************************************************************************************************

1. 这款软件是用来做什么的？
它是用来为 Auto_SelfReport.py（详细内容参见Auto_SelfReport.py内的注释文本） 配置必要的运行环境并进行测试的，你可以简单地将其理解为“安装程序”一类的东西。整个过程会执行5个步骤：python环境配置、系统环境变量配置、生成命令行指令文件、添加定时任务、运行测试，你只需要安装程序的提示进行即可轻松完成环境配置。

2. 环境配置前后需要注意的问题
运行该环境配置程序之前请将你收到的整个程序文件夹“Auto_SelfReport”解压并保存到合适且方便日后查找的位置，在完成环境配置后请勿移动该文件夹，否则会导致脚本无法正常运行。

3. 用户的权利与义务
任何人无论通过何种渠道获得了这份程序副本，都平等地享有占有、使用、分析、修改、复制和分发该软件程序的权利（但是就目前阶段而言，Steve并不希望你来帮他分发、传播该产品，但你仍然享有免费分发该程序的权利），同时也有义务承担因使用该软件程序造成的一切后果。该产品并不以盈利为目的，所以你应当遵循“免费获得，免费给予”的分享精神获取、分发此软件程序，因此该产品（以及附带的各版本 Auto_SelfReport.py）从未、将来也不会作为商品进行销售。

4. 我可以移除版权声明和数字签名吗？
当然可以。不过如果你是以重新分发为目的，建议你耗子尾汁。

5. 下载、占有、使用此软件程序（及一切附带内容）即代表同意并愿意遵守以上条款。

开源外部工具及附带内容版权声明：
=============================================
Auto_SelfReport_RE.py

Copyright (c) 2020-2021 Steve D. J.. 
All Rights Reserved.
=============================================
SendAsBots_QQ Steve's Special Customized Edition

Copyright (c) 2020-2021 Steve D. J.. 
All Rights Reserved.
=============================================
Python 3.9.2

Copyright (c) 2001-2019 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.
=============================================
Chrome

Copyright (c)  2021 Google LLC.
All Rights Reserved.
=============================================
ChromeDriver

Copyright (c)  2021 SeleniumHQ.
All Rights Reserved.
