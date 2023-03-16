# -*- coding: utf-8 -*-
# @File : neo4j_test.py
# @Time : 3/15/23 19:10
import json


# columns_value = ['_id', '名称', '产国', '图片', '简介', '首飞时间', '研发单位', '气动布局', '发动机数量', '飞行速度',
#                  '关注度', '乘员',
#                  '机长', '翼展', '机高', '发动机', '最大飞行速度', '最大航程', '大类', '类型', '服役时间', '生产单位',
#                  '空重',
#                  '最大起飞重量', '退役时间', '旋翼直径', '机炮', '挂载点', '内置武器', '战地机型', 'W-3W', '建造时间',
#                  '满排吨位', '编制',
#                  '舰长', '型宽', '满载排水量', '续航距离', '航速', '制造厂', '下水时间', '现状', '同型', '活动范围',
#                  '前型', '次型',
#                  '自持力', '导弹', '火炮', '改装时', '水上排水量', '射控装置', '主炮', '潜航深度', '改装前', '竣工时',
#                  '装备', '武备',
#                  '兵装', '1935年', '反舰导弹', '舰舰导弹', '新造时', '防空兵器', '水下排水量', '武器装备', '鱼雷',
#                  '水雷', '武装',
#                  '枪械', '枪炮', '制造商', '生产年限', '数量', '口径', '全枪长', '全枪重', '弹匣容弹量', '参战情况',
#                  '有效射程', '发射性能',
#                  '战斗射速', '刀长', '刀锋长度', '刀锋宽度', '刀重', '研发厂商', '诞生时间', '底盘类型', '乘员与载员',
#                  '车长', '宽度',
#                  '高度', '战斗全重', '最大速度', '最大行程', '总重', '炮管长度', '最大射程', '炮口初速', '研发时间',
#                  '编辑评分', '型号',
#                  '全长', '研制时间', '射程', '弹长', '弹径', '弹重', '制导系统', '引信', '发射日期', '发射地点', '长度',
#                  '中心直径',
#                  '首次轨道发射', '轨道', '纬度', '经度', '运载火箭', '处理器', '轨道卫星', '装药类型', '全重',
#                  '引信装置', '尾翼装置',
#                  '动力装置']
#
# military_dict = {}
# for item in columns_value:
#     military_dict[item] = item
#
# print(military_dict['轨道'])

# def read_nodes():
#     # 共７类节点
#     drugs = []  # 药品
#     foods = []  # 食物
#     checks = []  # 检查
#     departments = []  # 科室
#     producers = []  # 药品大类
#     diseases = []  # 疾病
#     symptoms = []  # 症状
#
#     disease_infos = []  # 疾病信息
#
#     # 构建节点实体关系
#     rels_department = []  # 科室－科室关系
#     rels_noteat = []  # 疾病－忌吃食物关系
#     rels_doeat = []  # 疾病－宜吃食物关系
#     rels_recommandeat = []  # 疾病－推荐吃食物关系
#     rels_commonddrug = []  # 疾病－通用药品关系
#     rels_recommanddrug = []  # 疾病－热门药品关系
#     rels_check = []  # 疾病－检查关系
#     rels_drug_producer = []  # 厂商－药物关系
#
#     rels_symptom = []  # 疾病症状关系
#     rels_acompany = []  # 疾病并发关系
#     rels_category = []  # 疾病与科室之间的关系
#
#     count = 0
#     for data in open('medical1.json', encoding='utf8'):
#         disease_dict = {}
#         count += 1
#         data_json = json.loads(data)
#         disease = data_json['name']
#         disease_dict['name'] = disease
#         diseases.append(disease)
#         disease_dict['desc'] = ''
#         disease_dict['prevent'] = ''
#         disease_dict['cause'] = ''
#         disease_dict['easy_get'] = ''
#         disease_dict['cure_department'] = ''
#         disease_dict['cure_way'] = ''
#         disease_dict['cure_lasttime'] = ''
#         disease_dict['symptom'] = ''
#         disease_dict['cured_prob'] = ''
#
#         if 'symptom' in data_json:
#             symptoms += data_json['symptom']
#             for symptom in data_json['symptom']:
#                 rels_symptom.append([disease, symptom])
#
#         if 'acompany' in data_json:
#             for acompany in data_json['acompany']:
#                 rels_acompany.append([disease, acompany])
#
#         if 'desc' in data_json:
#             disease_dict['desc'] = data_json['desc']
#
#         if 'prevent' in data_json:
#             disease_dict['prevent'] = data_json['prevent']
#
#         if 'cause' in data_json:
#             disease_dict['cause'] = data_json['cause']
#
#         if 'get_prob' in data_json:
#             disease_dict['get_prob'] = data_json['get_prob']
#
#         if 'easy_get' in data_json:
#             disease_dict['easy_get'] = data_json['easy_get']
#
#         if 'cure_department' in data_json:
#             cure_department = data_json['cure_department']
#             if len(cure_department) == 1:
#                 rels_category.append([disease, cure_department[0]])
#             if len(cure_department) == 2:
#                 big = cure_department[0]
#                 small = cure_department[1]
#                 rels_department.append([small, big])
#                 rels_category.append([disease, small])
#
#             disease_dict['cure_department'] = cure_department
#             departments += cure_department
#
#         if 'cure_way' in data_json:
#             disease_dict['cure_way'] = data_json['cure_way']
#
#         if 'cure_lasttime' in data_json:
#             disease_dict['cure_lasttime'] = data_json['cure_lasttime']
#
#         if 'cured_prob' in data_json:
#             disease_dict['cured_prob'] = data_json['cured_prob']
#
#         if 'common_drug' in data_json:
#             common_drug = data_json['common_drug']
#             for drug in common_drug:
#                 rels_commonddrug.append([disease, drug])
#             drugs += common_drug
#
#         if 'recommand_drug' in data_json:
#             recommand_drug = data_json['recommand_drug']
#             drugs += recommand_drug
#             for drug in recommand_drug:
#                 rels_recommanddrug.append([disease, drug])
#
#         if 'not_eat' in data_json:
#             not_eat = data_json['not_eat']
#             for _not in not_eat:
#                 rels_noteat.append([disease, _not])
#
#             foods += not_eat
#             do_eat = data_json['do_eat']
#             for _do in do_eat:
#                 rels_doeat.append([disease, _do])
#
#             foods += do_eat
#             recommand_eat = data_json['recommand_eat']
#
#             for _recommand in recommand_eat:
#                 rels_recommandeat.append([disease, _recommand])
#             foods += recommand_eat
#
#         if 'check' in data_json:
#             check = data_json['check']
#             for _check in check:
#                 rels_check.append([disease, _check])
#             checks += check
#         if 'drug_detail' in data_json:
#             drug_detail = data_json['drug_detail']
#             producer = [i.split('(')[0] for i in drug_detail]
#             rels_drug_producer += [[i.split('(')[0], i.split('(')[-1].replace(')', '')] for i in drug_detail]
#             producers += producer
#         disease_infos.append(disease_dict)
#     return set(drugs), set(foods), set(checks), set(departments), set(producers), set(symptoms), set(
#         diseases), disease_infos, \
#         rels_check, rels_recommandeat, rels_noteat, rels_doeat, rels_department, rels_commonddrug, rels_drug_producer, rels_recommanddrug, \
#         rels_symptom, rels_acompany, rels_category


def read_nodes():
    military_attributes = ['名称', '产国', '图片', '简介', '首飞时间', '研发单位', '气动布局', '发动机数量', '飞行速度',
                           '关注度', '乘员',
                           '机长', '翼展', '机高', '发动机', '最大飞行速度', '最大航程', '大类', '类型', '服役时间',
                           '生产单位',
                           '空重',
                           '最大起飞重量', '退役时间', '旋翼直径', '机炮', '挂载点', '内置武器', '战地机型', 'W-3W',
                           '建造时间',
                           '满排吨位', '编制',
                           '舰长', '型宽', '满载排水量', '续航距离', '航速', '制造厂', '下水时间', '现状', '同型',
                           '活动范围',
                           '前型', '次型',
                           '自持力', '导弹', '火炮', '改装时', '水上排水量', '射控装置', '主炮', '潜航深度', '改装前',
                           '竣工时',
                           '装备', '武备',
                           '兵装', '1935年', '反舰导弹', '舰舰导弹', '新造时', '防空兵器', '水下排水量', '武器装备',
                           '鱼雷',
                           '水雷', '武装',
                           '枪械', '枪炮', '制造商', '生产年限', '数量', '口径', '全枪长', '全枪重', '弹匣容弹量',
                           '参战情况',
                           '有效射程', '发射性能',
                           '战斗射速', '刀长', '刀锋长度', '刀锋宽度', '刀重', '研发厂商', '诞生时间', '底盘类型',
                           '乘员与载员',
                           '车长', '宽度',
                           '高度', '战斗全重', '最大速度', '最大行程', '总重', '炮管长度', '最大射程', '炮口初速',
                           '研发时间',
                           '编辑评分', '型号',
                           '全长', '研制时间', '射程', '弹长', '弹径', '弹重', '制导系统', '引信', '发射日期',
                           '发射地点', '长度',
                           '中心直径',
                           '首次轨道发射', '轨道', '纬度', '经度', '运载火箭', '处理器', '轨道卫星', '装药类型', '全重',
                           '引信装置', '尾翼装置',
                           '动力装置']

    militaries = []  # 武器等
    producing_countries = []  # 产国
    research_and_develop_organizations = []  # 研发单位/研发厂商
    producers = []  # 生产单位/生产厂

    classes = []  # 大类
    categories = []  # 类别

    armored_car_chassis_types = []  # 装甲车底盘类型——装甲车
    vessels_activity_areas = []  # 船的活动范围——船
    pneumatic_layouts = []  # 气动布局——飞行器
    cannon_calibres = []  # 口径——火炮
    cannon_types = []  # 型号——火炮

    militaries_infos = []  # 武器信息

    # 实体之间的关系
    rels_militaries_producing_countries = []  # 武器-产国
    rels_producing_countries_producers = []  # 生产商-产国
    rels_country_research_and_develop_organizations = []  # 研发组织-国家
    rels_militaries_research_and_develop_organizations = []  # 武器-研发组织
    rels_militaries_producers = []  # 武器-生产商
    rels_militaries_categories = []  # 武器-类别
    rels_classes_categories = []  # 大类-具体类别
    rels_militaries_armored_car_chassis_type = []  # 武器-装甲车底盘类型（装甲车特有）
    rels_militaries_vessels_activity_area = []  # 武器-船的活动范围（船特有）
    rels_militaries_pneumatic_layout = []  # 武器-气动布局（飞行器）
    rels_militaries_cannon_calibre = []  # 武器-口径（火炮）
    rels_militaries_cannon_type = []  # 武器-型号（火炮）

    count = 0
    for data in open('/Users/zlh/Documents/Daily/Test/military1.json', encoding='utf8'):
        militaries_dict = {}
        count += 1
        data_json = json.loads(data)
        military = data_json['名称']
        militaries_dict['名称'] = military
        militaries.append(military)
        for attr in military_attributes:
            if attr in data_json:
                militaries_dict[attr] = data_json[attr]

        if '产国' in data_json:
            country = data_json['产国']
            if country not in producing_countries:
                producing_countries.append(country)
            rels_militaries_producing_countries.append([military, country])

        if '研发单位' in data_json:
            research_and_develop_organization = data_json['研发单位']
            if research_and_develop_organization not in research_and_develop_organizations:
                research_and_develop_organizations.append(research_and_develop_organization)
            rels_militaries_research_and_develop_organizations.append([military, research_and_develop_organization])
            if '产国' in data_json:
                country = data_json['产国']
                if [country,
                    research_and_develop_organization] not in rels_country_research_and_develop_organizations:
                    rels_country_research_and_develop_organizations.append(
                        [country, research_and_develop_organization])

        if '研发厂商' in data_json:
            research_and_develop_organization = data_json['研发厂商']
            if research_and_develop_organization not in research_and_develop_organizations:
                research_and_develop_organizations.append(research_and_develop_organization)
            rels_militaries_research_and_develop_organizations.append([military, research_and_develop_organization])
            if '产国' in data_json:
                country = data_json['产国']
                if [country,
                    research_and_develop_organization] not in rels_country_research_and_develop_organizations:
                    rels_country_research_and_develop_organizations.append(
                        [country, research_and_develop_organization])

        if '大类' in data_json:
            big_class = data_json['大类']
            if big_class not in classes:
                classes.append(big_class)

        if '类型' in data_json:
            category = data_json['类型']
            if category not in categories:
                categories.append(category)
            rels_militaries_categories.append([military, category])
            if '大类' in data_json:
                big_class = data_json['大类']
                if [big_class, category] not in rels_classes_categories:
                    rels_classes_categories.append([big_class, category])

        if '制造商' in data_json:
            producer = data_json['制造商']
            if producer not in producers:
                producers.append(producer)
            rels_militaries_producers.append([military, producer])
            if '产国' in data_json:
                country = data_json['产国']
                if [country, producer] not in rels_producing_countries_producers:
                    rels_producing_countries_producers.append([country, producer])

        if '制造厂' in data_json:
            producer = data_json['制造厂']
            if producer not in producers:
                producers.append(producer)
            rels_militaries_producers.append([military, producer])
            if '产国' in data_json:
                country = data_json['产国']
                if [country, producer] not in rels_producing_countries_producers:
                    rels_producing_countries_producers.append([country, producer])

        if '活动范围' in data_json:
            vessels_activity_area = data_json['活动范围']
            if vessels_activity_area not in vessels_activity_areas:
                vessels_activity_areas.append(vessels_activity_area)
            rels_militaries_vessels_activity_area.append([military, vessels_activity_area])

        if '底盘类型' in data_json:
            armored_car_chassis_type = data_json['底盘类型']
            if armored_car_chassis_type not in armored_car_chassis_types:
                armored_car_chassis_types.append(armored_car_chassis_type)
            rels_militaries_armored_car_chassis_type.append([military, armored_car_chassis_type])

        if '气动布局' in data_json:
            pneumatic_layout = data_json['气动布局']
            if pneumatic_layout not in pneumatic_layouts:
                pneumatic_layouts.append(pneumatic_layout)
            rels_militaries_pneumatic_layout.append([military, pneumatic_layout])

        if '口径' in data_json:
            cannon_calibre = data_json['口径']
            if cannon_calibre not in cannon_calibres:
                cannon_calibres.append(cannon_calibre)
            rels_militaries_cannon_calibre.append([military, cannon_calibre])

        if '型号' in data_json:
            cannon_type = data_json['型号']
            if cannon_type not in cannon_types:
                cannon_types.append(cannon_type)
            rels_militaries_cannon_type.append([military, cannon_type])

        militaries_infos.append(militaries_dict)
    return set(militaries), set(producing_countries), set(research_and_develop_organizations), set(
        producers), set(classes), set(categories), set(armored_car_chassis_types), set(
        vessels_activity_areas), set(pneumatic_layouts), set(cannon_calibres), set(
        cannon_types), militaries_infos, rels_militaries_producing_countries, \
        rels_producing_countries_producers, rels_country_research_and_develop_organizations, \
        rels_militaries_research_and_develop_organizations, rels_militaries_producers, \
        rels_militaries_categories, rels_classes_categories, rels_militaries_armored_car_chassis_type, \
        rels_militaries_vessels_activity_area, rels_militaries_pneumatic_layout, \
        rels_militaries_cannon_calibre, rels_militaries_cannon_type
def test():
    military_attributes_in_en = ['name', 'origin_country', 'img_url', 'introduction', 'first_fly_time',
                                 'R&D_organization',
                                 'pneumatic_layout', 'num_of_engine', 'speed', 'attention_degree', 'crew_num',
                                 'flight_long', 'wings_width', 'flight_height', 'engine', 'max_speed', 'max_voyage',
                                 'class', 'categories', 'serve_time', 'producer', 'net_weight', 'max_fly_weight',
                                 'retire_time', 'rotor_diameter', 'machine_gun', 'mount_point', 'built-in_weapon',
                                 'war_field_machine_type', 'W-3W', 'build_time', 'full_tonnage_row', 'authorized',
                                 'captain', 'modeled_breath', 'load_displacement', 'cruising_distance',
                                 'navigational_speed', 'manufactory', 'launch_time', 'status', 'same_type',
                                 'activity_range', 'prior_type', 'latter_type', 'self-sustaining', 'missile',
                                 'cannon', 'modify_time', 'water_displacement', 'firing_control_device', 'main_cannon',
                                 'submersible_depth', 'before_modify', 'complete_time', 'equipment', 'Armed',
                                 'military_uniform', '1935', 'anti-ship_missile', 'ship-to-ship_missile',
                                 'new_build', 'anti-aircraft-weapon', 'under_water_displacement', 'weapon_equipment',
                                 'torpedo', 'mine', 'arms', 'shooter', 'firearms', 'manufacturer', 'produce_year',
                                 'amount', 'calibres',
                                 'gun_length', 'gun_weight', 'magazine_capacity',
                                 'war_participation', 'effective_range', 'shoot_performance', 'shoot_speed',
                                 'knife_length', 'blade_length', 'blade_width', 'knife_weight', 'R&D_manufactures',
                                 'born_time', 'chassis_type', 'crew_num', 'vehicle_length', 'width', 'height',
                                 'weight_in_war', 'max_speed', 'max_route', 'gross_weight', 'barrel_length',
                                 'max_range', 'muzzle_velocity', 'R&D_time', 'editor_rating', 'version', 'tital_length',
                                 'development_time', 'shoot_range', 'bullet_length',
                                 'bullet_diameter',
                                 'bullet_weight', 'guidance_sys', 'fuze', 'launch_date', 'launch_place', 'length',
                                 'center_diameter', 'first_orbital_launch', 'orbit', 'longitude', 'latitude',
                                 'carrier_rocket', 'processor', 'orbiting_satellites', 'charge_type', 'total_weight',
                                 'fuze_device', 'tail_device', 'power_device']
    military_attributes = ['名称', '产国', '图片', '简介', '首飞时间', '研发单位', '气动布局', '发动机数量', '飞行速度',
                           '关注度', '乘员',
                           '机长', '翼展', '机高', '发动机', '最大飞行速度', '最大航程', '大类', '类型', '服役时间',
                           '生产单位',
                           '空重',
                           '最大起飞重量', '退役时间', '旋翼直径', '机炮', '挂载点', '内置武器', '战地机型', 'W-3W',
                           '建造时间',
                           '满排吨位', '编制',
                           '舰长', '型宽', '满载排水量', '续航距离', '航速', '制造厂', '下水时间', '现状', '同型',
                           '活动范围',
                           '前型', '次型',
                           '自持力', '导弹', '火炮', '改装时', '水上排水量', '射控装置', '主炮', '潜航深度', '改装前',
                           '竣工时',
                           '装备', '武备',
                           '兵装', '1935年', '反舰导弹', '舰舰导弹', '新造时', '防空兵器', '水下排水量', '武器装备',
                           '鱼雷',
                           '水雷', '武装',
                           '枪械', '枪炮', '制造商', '生产年限', '数量', '口径', '全枪长', '全枪重', '弹匣容弹量',
                           '参战情况',
                           '有效射程', '发射性能',
                           '战斗射速', '刀长', '刀锋长度', '刀锋宽度', '刀重', '研发厂商', '诞生时间', '底盘类型',
                           '乘员与载员',
                           '车长', '宽度',
                           '高度', '战斗全重', '最大速度', '最大行程', '总重', '炮管长度', '最大射程', '炮口初速',
                           '研发时间',
                           '编辑评分', '型号',
                           '全长', '研制时间', '射程', '弹长', '弹径', '弹重', '制导系统', '引信', '发射日期',
                           '发射地点', '长度',
                           '中心直径',
                           '首次轨道发射', '轨道', '纬度', '经度', '运载火箭', '处理器', '轨道卫星', '装药类型', '全重',
                           '引信装置', '尾翼装置',
                           '动力装置']
    military_attributes_dict = {}
    cnt = len(military_attributes)
    for i in range(cnt):
        military_attributes_dict[military_attributes[i]] = military_attributes_in_en[i]
    print(military_attributes_dict['名称'])
def tt():
    i = "match(p:Military),(q:Producing_country) where p.name='C-11/20/37”湾流“'and q.name='美国' create (p)-[rel:producing_county{name:'产国'}]->(q)"
    i1 = i.split("p.name=")[1].split("and q.name=")[0]
    i2 = i1[1:-1]
    m1 = i.split("and q.name=")[1].split(" create (p)-[rel")[0]
    m2 = m1[1:-1]
    n = i.split(' ')[2].split("'")[1]
    m = i.split("'")[3]
    rr = i.split('[')[-1].split(']')[0][4:].split("'")[1]
    r = i.split('[')[-1].split(':')[1].split('{')[0]

    print(i)
    print(i1)
    print(i2)
    print(m1)
    print(m2)
    print(n)
    print(m)
    print(rr)
    print(r)


if __name__ == '__main__':
    a = "东海，南海"
    if "，" in a:
        b = a.split("，")
        for i in b:
            print(i)

