# Learning python design patterns

## 2. 싱글톤 디자인 패턴
* [싱글톤 패턴](./chapter2/1_singleton.py)
* [게으른 초기화](./chapter2/2_lazy_initialization.py)
* [모노스테이트 싱글톤](./chapter2/3_monostate_singletone.py)
* [메타 클래스](./chapter2/4_meta_class.py)
* [싱글톤 패턴 사례 1](./chapter2/5_singleton_1.py)
* [싱글톤 패턴 사례 2](./chapter2/6_singleton_2.py)

## 3. 팩토리 패턴
* [심플 팩토리 패턴](./chaper3/1_simple_factory.py)
* [팩토리 메소드 패턴](./chaper3/2_factory_method.py)
* [추상 팩토리 패턴](./chaper3/3_abstract_factory.py)
* 팩토리 메소드 vs 추상 팩토리 메소드

| 팩토리 메소드 | 추상 팩토리 메소드 |
|---|---|
| 객체 생성에 필요한 메소드가 사용자에게 노출된다 | 관련된 객체 집단을 생성하기 위해 한 개 이상의 팩토리 메소드가 필요하다 |
| 어떤 객체를 생성할지 결정하는 상속과 서브 클래스가 필요하다 | 다른 클래스 객체를 생성하기 위해 컴포지션을 사용한다 |
| 한 개의 객체를 생성하는 팩토리 메소드를 사용한다 | 관련된 객체 집단을 생성한다 |

## 4. 퍼사드의 다양성
* [퍼사드 패턴 구현](chapter4/1_pacod_pattern.py)

## 5. 프록시 패턴 - 객체 접근 제어
* [프록시 디자인 패턴](chapter5/1_proxy_pattern.py)
* [프록시 패턴 사용 사례](chapter5/2_proxy_pattern.py)
* 프록시 패턴의 장점
  * 무거운 객체 특히 자주 사용되는 객체를 캐싱해 어플리케이션의 성능을 향상 시킨다
  * RealSubject에 대한 접근 요청을 인증한다
  * 원격 프록시는 원격 서버간의 네트워크 연결과 데이터베이스 연결 구현에 적합하며 시스템 모니터링 용도로 사용될 수 있다
* 퍼사드와 프록시 패턴 비교

| 프록시 패턴 | 퍼사드 패턴 |
|---|---|
| 실 객체의 대리 객체를 제공해 접근을 제어한다 | 클래스의 서브시스템에 대한 인터페이스를 제공한다 |
| 타겟 객체와 동일한 인터페이스 구조를 가지며 타겟에 대한 참조를 가지고 있다 | 서브시스템 간의 의존도와 통신을 최소화 한다 |
| 클라이언트와 감싸고 있는 객체 사이의 중재자 역할을 한다 | 퍼사드 객체는 하나의 통합된 간단한 인터페이스를 제공한다 |

## 6. 옵서버 패턴
* [옵서버 패턴](chapter6/1_observer_pattern.py)
* [옵서버 패턴 사용 사례](chapter6/2_observer_pattern.py)

## 7. 커맨드 패턴 - 요청 패턴화
* [커맨드 패턴 1](chapter7/1_command_pattern.py)
* [커맨드 패턴 2](chapter7/2_command_pattern.py)
* [커맨트 패턴 사용 사례](chapter7/3_command_pattern.py)

## 8. 템플릿 메소드 패턴 - 알고리즘의 캡슐화
* [템플릿 메소드 패턴 1](chapter8/1_template_method.py)
* [템플릿 메소드 패턴 2](chapter8/2_template_method.py)
* [템플릿 메소드 패턴 사례](chapter8/3_template_method.py)

## 9. 모델-뷰 컨트롤러 - 컴파운드 패턴
* [모델 뷰 컨트롤러 패턴 1](chapter9/1_mvc_pattern.py)
* [모델 뷰 컨트롤러 패턴 2](chapter9/2_mvc_pattern.py)
* [모델 뷰 컨트롤러 패턴 사용 사례](chapter9/mvc_pattern/web_app.py)

## 10. 상태 디자인 패턴
* [상태 디자인 패턴 1](chapter10/1_objects_for_states_pattern.py)
* [상태 디자인 패턴 2](chapter10/2_objects_for_states_pattern.py)
* [상태 디자인 패턴 3](chapter10/3_objects_for_states_pattern.py)
