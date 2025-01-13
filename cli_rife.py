import subprocess
import os
import shlex  # 경로의 안전한 처리를 위해 추가


def main():
    try:
        while True:
            video_path = input("path를 입력하십시오 : ").strip()
            video_path = os.path.abspath(video_path)
            
            # 단계별 경로 확인
            print("\n경로 확인:")
            path_parts = video_path.split('/')
            current_path = "/"
            for part in path_parts[1:]:  # 첫 번째 빈 문자열 건너뛰기
                current_path = os.path.join(current_path, part)
                exists = os.path.exists(current_path)
                is_file = os.path.isfile(current_path)
                is_dir = os.path.isdir(current_path)
                print(f"확인: {current_path}")
                print(f"  존재여부: {exists}")
                print(f"  파일여부: {is_file}")
                print(f"  폴더여부: {is_dir}")
            
            if os.path.isfile(video_path):
                break
            else:
                print("\nError: 파일을 찾을 수 없습니다.")
                retry = input("다시 시도하시겠습니까? (y/n): ").strip().lower()
                if retry != 'y':
                    return
        
        # exp 값 입력 받기
        while True:
            try:
                exp = int(input("Interpolation 배수를 입력하십시오 : ").strip())
                if exp < 0:
                    print("양수를 입력해주세요.")
                    continue
                break
            except ValueError:
                print("올바른 숫자를 입력해주세요.")
        
        # inference_video.py 실행 명령어 구성
        command = [
            'python',
            'inference_video.py',
            f'--video={shlex.quote(video_path)}',  # 경로를 안전하게 처리
            f'--exp={exp}'
        ]
        
        print(f"\n처리 시작: {video_path}")
        print(f"보간 배수: 2^{exp} = {2**exp}")
        print(f"실행 명령어: {' '.join(command)}")  # 디버깅을 위한 출력
        
        # subprocess로 inference_video.py 실행
        subprocess.run(command, check=True)
        print("처리 완료!")
        
    except KeyboardInterrupt:
        print("\n사용자에 의해 중단됨")
    except Exception as e:
        print(f"오류 발생: {e}")
        print(f"상세 오류: {type(e).__name__}")  # 오류 타입 출력

if __name__ == '__main__':
    main()