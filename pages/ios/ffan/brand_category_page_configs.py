# -*- coding: utf-8 -*-

class BrandCategoryPageConfigs():

    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view

    # 品牌街－－推荐&大牌
    text_pinpaijie = "品牌街"
    text_recommend = u"推荐"
    text_brand = u"大牌"
    #xpath_brand_details = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIACollectionView[1]/UIACollectionCell[1]/UIAImage[1]"
    xpath_brand_details = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIASegmentedControl[1]/UIAButton[2]"
    xpath_recommend_details = "//UIAApplication[1]/UIAWindow[1]/UIATableView[2]/UIATableCell[3]"
    xpath_women_fasion = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIACollectionView[1]/UIACollectionCell[1]/UIAStaticText[1]"
    xpath_men_fasion = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIACollectionView[1]/UIACollectionCell[2]/UIAStaticText[1]"
    xpath_catering = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIACollectionView[1]/UIACollectionCell[3]/UIAStaticText[1]"
    xpath_life = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIACollectionView[1]/UIACollectionCell[4]/UIAStaticText[1]"
    xpath_sports = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIACollectionView[1]/UIACollectionCell[5]/UIAStaticText[1]"
    xpath_competitive_products = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIACollectionView[1]/UIACollectionCell[6]/UIAStaticText[1]"
    xpath_dapairuzhu = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIAButton[1]"

    text_women_fasion = u"女装"
    text_men_fasion = u"男装"
    text_catering = u"餐饮"
    text_life = u"生活"
    text_sports = u"运动"
    text_competitive_products = u"精品"
    text_dapai = u"大牌"
    def __init__(self):
        pass;

