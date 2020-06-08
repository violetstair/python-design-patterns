# 템플릿 메소드 패턴
# 템플릿 메소드 패턴이 적합한 상황
# * 여러 알고리즘 또는 클래스가 비슷하거나 같은 로직을 구현할 때
# * 알고리즘을 단계별로 서브클래스화해 코드의 중복을 줄일 수 있는 경우
# * 서브클래스를 오버라이드해 여러 알고리즘을 구현할 수 있는 경우
# 템플릿 메소드 패턴의 목적
# * 알고리즘의 뼈대를 원시 연산으로 구현
# * 알고리즘의 구조를 수정하지 않고 일부 서브클래스를 재정의
# * 코드의 재사용과 중복 최소화
# * 공통 인터페이스 및 구혀 활용

from abc import ABCMeta, abstractmethod


class Compiler(metaclass=ABCMeta):

    @abstractmethod
    def collect_source(self):
        pass

    @abstractmethod
    def compile_to_object(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def compile_and_run(self):
        self.collect_source()
        self.compile_to_object()
        self.run()


class IOSCompiler(Compiler):
    
    def collect_source(self):
        print("Collecting Swift Source Code")
    
    def compile_to_object(self):
        print("Compiling Swift code to LLVM bitcode")

    def run(self):
        print("Program running on runtime enviroment")


ios = IOSCompiler()
ios.compile_and_run()
