import bs4

html='''
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:4830198616,&quot;author_name&quot;:&quot;Li\u6b23\u8fdc&quot;,&quot;first_post_id&quot;:99354312570,&quot;reply_num&quot;:24,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;frs_tpoint&quot;:null}'>
    <div class="t_con cleafix">

        <div class="col2_left j_threadlist_li_left">
            <span class="threadlist_rep_num center_text" title="回复">24</span>
        </div>
        <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">


                    <a href="/p/4830198616" title="又重温一遍 第九季  这个侧脸给多少分" target="_blank" class="j_th_tit ">又重温一遍 第九季  这个侧脸给多少分</a>
                </div>
                <div class="threadlist_author pull_right">
                    <span class="tb_icon_author " title="主题作者: Li欣远" data-field='{&quot;user_id&quot;:836897637}'><i class="icon_author"></i><span class="frs-author-name-wrap"><a data-field='{&quot;un&quot;:&quot;Li\u6b23\u8fdc&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=Li%E6%AC%A3%E8%BF%9C&ie=utf-8&fr=frs" target="_blank">Li欣远</a></span>
                    <span
                        class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>
                        </span>
                        <span class="pull-right is_show_create_time" title="创建时间">2016-10</span>
                </div>
            </div>
            <div class="threadlist_detail clearfix">
                <div class="threadlist_text pull_left">
                    <div class="threadlist_abs threadlist_abs_onlyline ">

                    </div>

                    <div class="small_wrap j_small_wrap">
                        <a href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                        <a href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                        <div class="small_list j_small_list cleafix">
                            <div class="small_list_gallery">
                                <ul class="threadlist_media j_threadlist_media clearfix" id="fm4830198616">
                                    <li>
                                        <a class="thumbnail vpic_wrap"><img src="" attr="11312" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=0337c3544f10b912bf94fefcf3cdd03a/0250b10f4bfbfbed6542b29070f0f736adc31fc1.jpg"
                                                bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=f4a1588f3d2ac65c6705667bcbc9b311/9a504fc2d56285352bfb56ce98ef76c6a6ef63c2.jpg"
                                                class="threadlist_pic j_m_pic " /></a>
                                        <div class="threadlist_pic_highlight j_m_pic_light"></div>
                                    </li>
                                    <li>
                                        <a class="thumbnail vpic_wrap"><img src="" attr="79296" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=3b020dee546034a829b7b083fb23656d/e25ed811728b47101b357923cbcec3fdfe0323c2.jpg"
                                                bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=f31a974851ee3d6d22c687c3732d6c22/14ce36d3d539b60098d48b58e150352ac75cb7c3.jpg"
                                                class="threadlist_pic j_m_pic " /></a>
                                        <div class="threadlist_pic_highlight j_m_pic_light"></div>
                                    </li>
                                    <li>
                                        <a class="thumbnail vpic_wrap"><img src="" attr="31320" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=b62c07df32f33a879e380818f66c3c01/173dc0628535e5dd840421307ec6a7efcf1b6230.jpg"
                                                bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=28ee4a32a364034f0fcdc20e9ff87831/29381f30e924b899ca14fdd766061d950a7bf631.jpg"
                                                class="threadlist_pic j_m_pic " /></a>
                                        <div class="threadlist_pic_highlight j_m_pic_light"></div>
                                    </li>
                                </ul>

                            </div>
                        </div>
                    </div>
                </div>


                <div class="threadlist_author pull_right">
                    <span class="tb_icon_author_rely j_replyer" title="最后回复人: wo不是精灵">
            <i class="icon_replyer"></i>
            <a data-field='{&quot;un&quot;:&quot;wo\u4e0d\u662f\u7cbe\u7075&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=wo%E4%B8%8D%E6%98%AF%E7%B2%BE%E7%81%B5&ie=utf-8&fr=frs" target="_blank">wo不是精灵</a>        </span>
                    <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            5-3        </span>
                </div>
            </div>
        </div>
    </div>
</li>
'''
comment={}
soup = bs4.BeautifulSoup(html,'lxml')
comment['title'] = soup.find('a',attrs={'class':'j_th_tit '}).text.strip()
comment['link'] ="http://tieba.baidu.com/" +  soup.find('a',attrs={'class':'j_th_tit '})['href']
comment['name'] = soup.find('span',attrs={'class':'tb_icon_author '}).text.strip()
comment['time'] = soup.find('span',attrs={'class':'pull-right is_show_create_time'}).text.strip()
comment['replyNum'] = soup.find('span',attrs={'class':'threadlist_rep_num center_text'}).text.strip()



print(comment)