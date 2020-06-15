field_name = {
    '序号': 'id',
    '日期': 'date',
    '运行日': 'date',
    '代理': 'agent',
    '公司': 'company',
    '航班号': 'Flight_nb',
    '机号': 'Machine_nb',
    '机型': 'Model',
    '机型类别': 'Model_Cate',
    '航站': 'terminal',
    '国内国际': 'Domestic_Inter',
    '计划到港时间': 'Planned_arrival',
    '计划离港时间': 'Planned_depart',
    'STD': 'Planned_depart',
    '实际到港时间': 'Actual_arrival',
    '实际到港': 'Actual_arrival',
    '实际离港时间': 'Actual_depart',
    '首次TSAT': 'First_TSAT',
    'TSAT': 'Last_TSAT',
    'RDY时间': 'RDY_time',
    '首次RDY': 'First_RDY_time',
    'ASAT': 'ASAT',
    '实际起飞时间': 'Actual_take_off',
    '前班实际落地': 'former_actual_landing',
    '计划过站时间': 'Plan_Station',
    '机位': 'Seat',
    '机坪': 'Apron',
    '近远机位': 'Near_and_far',
    '任务性质': 'Task_Nature',
    '跑道': 'Runway',
    '取消状态': 'Cancel_Status',
    '登机开始时间': 'Boarding_start',
    '登机结束时间': 'Boarding_end',
    '开客舱门时间': 'Opening_cabin_door',
    '开货航门时间': 'Opening_cargo_Door',
    '关客舱门时间': 'Closing_cabin_door',
    '关货舱门时间': 'Closing_cargo_door',
    '进港刹车时间': 'Entry_braking_time',
    '出港松刹车时间': 'Loosen_braking_departure',
    '靠桥（客梯车）': 'Bridge_start_elevator',
    '撤桥（客梯车）': 'Bridge_removal_elevator',
    '首摆渡到登机口': 'First_ferry_gate',
    '末摆渡到登机口': 'Final_ferry_gate',
    '拖车到位': 'Trailer_in_place',
    '进港客梯车到位': 'Incoming_elevator_inplace',
    '进港首摆渡到达机位': 'Incoming_First_arrival',
    '进港客梯车达标': 'Incoming_elevator_logo',
    '进港首摆渡车达标': 'Incoming_First_logo',
    '旅客人数': 'Passengers_Number',
    '起飞延误': 'Take_off_Delay',
    '内外航': 'Inter_and_exter',
    '早出港始发标识': 'Early_depar_Initial',
    '需用摆渡': 'Need_use_Ferry',
    '最小过站时间': 'Min_crossing_Station',
    'STA': 'STA',
    'ATA': 'ATA',
    '进离港标识': 'In_Out_Sign',
    'ETA': 'ETA',
    '过站放行延误': 'Transit_delay',
    '早出港延误': 'Departure_delay'
}

title_eng = ['id', 'date', 'agent', 'company', 'Flight_nb', 'Machine_nb', 'Model', 'Model_Cate', 'terminal', 'Domestic_Inter', 'Planned_arrival', 'Planned_depart', 'Actual_arrival', 'Actual_depart', 'First_TSAT', 'Last_TSAT', 'First_RDY_time', 'RDY_time', 'ASAT', 'Actual_take_off', 'former_actual_landing', 'Plan_Station', 'Seat', 'Apron', 'Near_and_far', 'Task_Nature', 'Runway', 'Cancel_Status', 'Boarding_start', 'Boarding_end', 'Opening_cabin_door', 'Opening_cargo_Door', 'Closing_cabin_door', 'Closing_cargo_door', 'Entry_braking_time', 'Loosen_braking_departure', 'Bridge_start_elevator', 'Bridge_removal_elevator', 'First_ferry_gate', 'Final_ferry_gate', 'Trailer_in_place', 'Incoming_elevator_logo', 'Take_off_Delay', 'Inter_and_exter', 'Early_depar_Initial', 'Min_crossing_Station', 'STA', 'ATA', 'Need_use_Ferry', 'Incoming_elevator_inplace', 'Incoming_First_arrival', 'Incoming_First_logo', 'Passengers_Number', 'In_Out_Sign', 'ETA', 'Transit_delay', 'Departure_delay']
title_name = ['序号', '运行日', '代理', '公司', '航班号', '机号', '机型', '机型类别', '航站', '国内国际', '计划到港时间', '计划离港时间', '实际到港', '实际离港时间', '首次TSAT', 'TSAT', '首次RDY', 'RDY时间', 'ASAT', '实际起飞时间', '前班实际落地', '计划过站时间', '机位', '机坪', '近远机位', '任务性质', '跑道', '取消状态', '登机开始时间', '登机结束时间', '开客舱门时间', '开货航门时间', '关客舱门时间', '关货舱门时间', '进港刹车时间', '出港松刹车时间', '靠桥（客梯车）', '撤桥（客梯车）', '首摆渡到登机口', '末摆渡到登机口', '拖车到位', '进港客梯车达标', '起飞延误', '内外航', '早出港始发标识', '最小过站时间', 'STA', 'ATA', '需用摆渡', '进港客梯车到位', '进港首摆渡到达机位', '进港首摆渡车达标', '旅客人数', '进离港标识', 'ETA', '过站放行延误', '早出港延误']


if __name__ == '__main__':
    field_name_new = {k: v for v, k in field_name.items()}
    title_name_new = [field_name_new[i] for i in title_eng]