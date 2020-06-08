# 커맨드 패턴
# 목적
# * 요청을 객체 속에 캡슐화 한다
# * 클라이언트의 다양한 요청을 매개변수화 한다
# * 요청을 큐에 저장한다
# * 객체지향 콜백을 지원한다
# 커맨드 패턴이 적합한 상황
# * 수행할 명령에 따라 객체를 변수화 할 때
# * 요청을 큐에 저장하고 각기 다른 시점에 수행해야 하는 경우
# * 작은 단위의 연산을 기반으로 하는 상위 연산을 만들 때

class Wizard:

    def __init__(self, src, root_dir):
        self.choices = []
        self.root_dir = root_dir
        self.src = src
    
    def preferences(self, command):
        self.choices.append(command)
    
    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print("Copying binaries --", self.src, " to ", self.root_dir)
            else:
                print("no operation")
    

if __name__ == "__main__":
    # 클라이언트 코드
    wizard = Wizard('python3.5.gzip', '/usr/bin/')
    # 사용자는 파이선을 선택
    wizard.preferences({'python': True})
    wizard.preferences({'java': False})
    wizard.execute()

