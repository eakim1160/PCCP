def solution(record):
    # record를 읽으면서 빈칸 없애면서 명령어/uid/별명 순으로 담는다.
    # uid와 별명 리스트
    # Uid 기준으로 Enter와 Leave 문구 순서대로 뿌리기    
    answer = []  
    traces = [] # (명령어, uid) 저장
    Map = {} # {uid:'별명'}
    
    for i in range(len(record)) : # 데이터 분리하면서 uid/별명 리스트 추가
        command = record[i].split()  
    
        if command[0] in ['Enter', 'Change']: # 별명 정보 저장
            Map[command[1]] = command[2] # uid = 최신 별명 업데이트 
        
        if command[0] in ['Enter', 'Leave']: # 명령어 정보 저장
            traces.append((command[0],command[1]))   # (명령어, uid)             
    
    for trace in traces:    

        match trace[0]:
            case 'Enter' :    
                answer.append('{}님이 들어왔습니다.'.format(Map[trace[1]]))
            case 'Leave' :    
                answer.append('{}님이 나갔습니다.'.format(Map[trace[1]]))                              
    return answer