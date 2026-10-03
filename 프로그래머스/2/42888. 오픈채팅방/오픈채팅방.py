def solution(record):
    # record를 읽으면서 빈칸 없애면서 명령어/uid/별명 순으로 담는다.
    # uid와 별명 리스트
    # Uid 기준으로 Enter와 Leave 문구 순서대로 뿌리기    
    answer = []  
    commands = [[] * 3 for _ in range(len(record))]
    uid = {}
    
    for i in range(len(record)) : # 데이터 분리하면서 uid/별명 리스트 추가
        commands[i] = record[i].split()  
        if commands[i][0] == 'Enter' or commands[i][0] == 'Change':
            uid[commands[i][1]] = commands[i][2] # 별명 업데이트  
    
    for command in commands:    
        match command[0]:
            case 'Enter' :    
                answer.append('{}님이 들어왔습니다.'.format(uid[command[1]]))
            case 'Leave' :    
                answer.append('{}님이 나갔습니다.'.format(uid[command[1]]))                      
        
    return answer