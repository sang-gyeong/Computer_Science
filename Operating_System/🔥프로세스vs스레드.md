## 프로세스

> 운영체제로부터 CPU 자원을 할당받는 작업의 단위

- 컴퓨터에서 연속적으로 실행되고 있는 컴퓨터 프로그램
- 메모리에 올라와 실행되고 있는 프로그램의 인스턴스(독립적인 개체)
- 운영체제로부터 시스템 자원을 할당받는 작업의 단위. 즉, 동적인 개념으로는 실행된 프로그램을 의미한다.

    **할당받는 시스템 자원의 예**

    - CPU 시간
    - 운영되기 위해 필요한 주소 공간
    - Code, Data, Stack, Heap의 구조로 되어 있는 독립된 메모리 영역
        - `Code`: 프로세서가 실행할 바이너리 코드(명령어)를 저장해 놓은 영역
        - `Data`: 전역 변수 또는 static 변수가 저장되는 영역
        - `Stack`: 함수를 호출하고 리턴할 때의 복귀 주소나 지역 변수와 같은 일시적인 데이터를 저장하는 영역
        - `Heap`: 프로그램 실행 중에 동적으로 메모리를 할당할 수 있는 자유로운 영역

<br>

## 스레드

> 프로세스 내에서 실제로 작업을 수행하는 주체

![](https://camo.githubusercontent.com/3dc4ad61f03160c310a855a4bd68a9f2a2c9a4c7/68747470733a2f2f74312e6461756d63646e2e6e65742f6366696c652f746973746f72792f393938383931343635433637433330363036)

- 경량 프로세스(Light weight process)라고 불리기도 하며, 프로세스 내의 CPU 수행 단위를 의미한다.
- 프로세스(process) 내에서 실제로 작업을 수행하는 주체를 의미한다.
- 모든 프로세스에는 한 개 이상의 스레드가 존재하여 작업을 수행한다.
- **스레드는 프로세스 내에서 각각 Stack, Registers(PC...)만 따로 할당받고 Code, Data, Heap 영역은 공유한다.**
    - 독립적인 실행흐름을 갖기 위해 스택과 레지스터는 각각 가지고 있게 됨 ㅇㅇ

<br>
## 멀티 프로세싱

> 하나의 컴퓨터에 여러 CPU 장착 → 하나 이상의 프로세스들을 동시에 처리(병렬)

- 코어가 여러 개이기 때문에 여러개의 프로세스가 동시에 실행 가능한 것.

![](https://i.imgur.com/hj1qjzj.png)

<br>
## 멀티 스레딩

단일 프로세스에 여러 개의 스레드를 만들어 각 스레드가 작업을 처리하도록 하는 것.

한 프로그램에 여러 개의 스레드가 있을 수 있는 이유는 스레드가 빠른 시간 간격으로 스위칭되기 때문이다. 이러한 동작으로 사용자는 여러 스레드가 동시에 실행되는 것처럼 보인다.

![](https://i.imgur.com/Bi8GppU.png)

<br>
## 멀티 프로그래밍

초기의 컴퓨터에서는 하나의 프로그램이 메모리에 올라가면 하나의 프로그램만 CPU가 처리를 진행할 수 있었다. 이 과정에서 프로세서의 처리 속도와 입출력 속도 간의 차이로 인해, 입출력이 완료될 때까지 프로세서는 idle한 상태가 된다. 따라서 이는 프로세서의 `자원 낭비`로 이루어진다.

프로세서가 **입출력 작업의 종료를 대기할 동안 하나의 프로세서에서 다른 프로그램을 수행할 수 있도록** 하는 것이 멀티프로그래밍이다.

(비동기 처리 느낌쓰)

<br>
## 멀티 태스킹

- Task : 운영체제에서 처리하는 작업 단위 (process 여러 개)
- OS가 Task 하나만 실행하는 것이 아니라, 여러 Task를 번갈아가면서 실행(약간 시분할 느낌)하여 동시에 실행되는 것 처럼 느끼게 해줌..

![](https://i.imgur.com/8f3scOI.png)

<br>

### ❓ 멀티 프로그래밍 vs 멀티 태스킹

앞에서 말한 멀티 프로그래밍은 프로세서의 **자원낭비를 막기 위함**이고, 멀티태스킹은 정해진 시간동안 각각의 **task를 번갈아가며 수행하는 것을 의미**한다.

<br>

### ❓ 멀티 스레드 vs 멀티 프로세스

  멀티 스레드는 멀티 프로세스보다 적은 메모리 공간을 차지하고 *문맥 전환이 빠르다*는 장점이 있지만, 오류로 인해 *하나의 스레드가 종료되면 전체 스레드가 종료될 수 있다는 점*과 동기화 문제를 안고 있다. 반면 멀티 프로세스 방식은 하나의 프로세스가 죽더라도 다른 프로세스에는 영향을 끼치지 않고 정상적으로 수행된다는 장점이 있지만, 멀티 스레드보다 많은 메모리 공간과 CPU 시간을 차지한다는 단점이 존재한다. 이 두 가지는 동시에 여러 작업을 수행한다는 점에서 같지만 적용해야 하는 시스템에 따라 적합/부적합이 구분된다. 따라서 대상 시스템의 특징에 따라 적합한 동작 방식을 선택하고 적용해야 한다.
  
<br>

### ❓ 프로세스와 스레드의 차이점은?
상경

- 프로세스는 운영체제로부터 CPU 자원을 할당받는 자원의 단위를 의미합니다.
- 스레드는 프로세스 내에서 실제적으로 작업을 수행하는 흐름의 단위를 의미합니다.
- 프로세스는 자신만의 고유한 공간과 자원을 할당받아 사용하는 것에 반해,

    스레드는 다른 스레드와 공간, 자원을 공유하면서 사용한다는 차이가 있습니다.

지영

- 프로세스는 메모리에 올라와 CPU에 할당되어 수행될 수 있는 프로그램을 의미합니다. 프로세스는 독립적인 주소 공간을 가져 프로그램에 실행되기 위해 필요한 code, heap, stack, data와 같은 영역을 가집니다.
- 스레드는 프로세스 내에 존재하며 실제로 작업을 수행할 수 있는 CPU 수행 단위로 프로세스의 주소 공간을 공유하기 때문에 메모리적인 면에서 경제적이라는 장점이 있습니다.

병건

- 프로세스는 프로그램 중, 메모리에 적재된 부분이 CPU를 할당받은 상태 혹은 논리적 단위를 말합니다.
- 스레드는 프로세스 내에 존재하는 실제 작업의 단위이자 주체입니다.
- 프로세스는 다른 프로세스에게 독립되어 있어 별도의 메모리 공간을 갖는 반면, 스레드는 하나의 프로세스에서 분화된 것이기 때문에 메모리 공간을 공유합니다. 그러나, 스레드는 독립적인 실행 환경을 주기 위해 stack과 레지스터 값은 별도로 갖게 됩니다.
- 프로세스는 다른 프로세스에 독립적이기 때문에 상태를 공유(동기화)하기 어렵습니다. 반면 쓰레드는 메모리 공간을 공유하기 때문에 상태를 공유하기 쉽습니다. 그러나 멀티 스레드의 경우 한 스레드가 다운되면 모든 스레드가 다운됩니다.
```
핵심 키워드

- 스레드는 작업을 "실제"로 수행하는 단위다.
- 프로세스는 독립적인 메모리 공간, 스레드는 code, heap, data 영역을 공유
    - 스레드는 메모리를 공유하기 때문에, 경제적인 메모리 사용
    - 프로세스는 독립적인 메모리 공간 → 다른 프로세스와 동기화 어려움
    - 스레드는 메모리 공간 공유 → 동기화 쉬움
```

