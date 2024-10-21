# 안전수칙을 잘 준수하지 않고 킥보드를 이용하는 시민들에게 경각심을 주고자 만든
# 킥보드 사고 현황 시스템

class ScooterAccidentDisplaySystem:
    def __init__(self):
        
        # 도로명과 사고 딕셔너리
        self.accident_records = {}

    # 사고 발생 기록 추가(road_name:도로명, cause:사고원인)
    def record_accident(self, road_name, cause):
        
        # 도로명이 accident_records에 없으면 새로운 리스트 생성
        if road_name not in self.accident_records:
            self.accident_records[road_name] = []
        
        # 사고원인을 리스트에 추가
        self.accident_records[road_name].append(cause)
        
        # 사고 발생 도로, 원인 출력
        print(f"{road_name}에서 사고가 기록되었습니다: 원인 - {cause}")

    # 도로별 사고 현황 표지판 형식으로 표시
    def display_accident_status(self, road_name):
         
        # 도로명이 accident_records에 존재하면
        if road_name in self.accident_records:
            accidents = self.accident_records[road_name]
           
            # 그 도로의 사고 수를 세어 나타냄
            print(f"[표지판] {road_name}에서 발생한 사고: {len(accidents)}건")
            
            # 그 사고의 원인
            for cause in accidents:
                print(f"- 원인: {cause}")
        
        # 도로명이 accident_records에 존재하지 않을 경우
        else:
            print(f"{road_name}에서는 사고가 기록되지 않았습니다.")

    # 전체 사고 요약
    def display_all_accident_summary(self):
        print("[전체 사고 요약]")
        for road, causes in self.accident_records.items():
            print(f"{road}: {len(causes)}건 사고 발생")
            for cause in causes:
                print(f"- 원인: {cause}")
# 사용 예시
# 시스템 생성
accident_system = ScooterAccidentDisplaySystem()

# 사고 기록 추가
accident_system.record_accident("한국교통대학교 충주캠퍼스 정문", "차량과의 충돌")
accident_system.record_accident("한국교통대학교 충주캠퍼스 정문", "사람과의 충돌")
accident_system.record_accident("한국교통대학교 충주캠퍼스 대학로", "인도 주행")

# 사고 현황을 도로 위 표지판 형식으로 표시
accident_system.display_accident_status("한국교통대학교 충주캠퍼스 정문")
accident_system.display_accident_status("한국교통대학교 충주캠퍼스 대학로")

# 전체 사고 요약 표시
accident_system.display_all_accident_summary()
