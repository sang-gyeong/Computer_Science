멀티프로그래밍의 목적은

- CPU의 속도가 굉장히 빨라서 놀고있기 때문에 context switch를 해서 시간을 시분할해서 프로세스들을 계속 돌림으로써 CPU의 효용을 높이기 위함
- 이를 위해 CPU 스케쥴링이 필요하다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6fb8b7ef-0096-4e72-967e-31665cd8d52b/_2021-03-09__7.35.10.png](https: // s3-us-west-2.amazonaws.com/secure.notion-static.com/6fb8b7ef-0096-4e72-967e-31665cd8d52b/_2021-03-09__7.35.10.png)

IO를하면서 대기하는 시간을 IO burst라고 한다.

어떨때는 CPU burst(주로 running), 어떨때는 IO burst(waiting, waiting→ready)

이렇게 상태가 왔다갔다 하는데 둘중에 어떤게 더 많을까? 전자가 많으면 CPU bound, 후자의 경우 IO bound라고 한다.

통계를 그려보니까, 상단의 그래프의 형태를 보임.

CPU만 열심히 쓰는 프로세스는 숫자가 몇개 안되고, IO burst타임이 더많은, IO-bound 의 빈도가 훨씬 더 많다는 것을 알 수 있다.

# CPU sheduler

메모리에 로드되어있는 프로세스 중에 어떤 것에 CPU를 할당해주는지 선택한다.

ready상태에 있는 프로세스들 중에서 CPU를 할당해줄 수 있는 프로세스를 선택하는 걸 CPU 스케쥴링 문제라고 한다.

그렇다면 다음 프로세스를 어떻게 선택할까? 대기중인 레디큐를 어떤 형태로 하면 좋을까?

- 링크드 리스트? 이진 트리?
- FIFO Queue: First-in, First-out
- Priority Queue: 이 경우 프로세스의 우선순위를 어떻게 정할 수 있을지가 관건이다

# Preemptive vs Non-preemptive (선점형 vs 비선점형)

- 쫓아낼 수 있는지 여부. 강제로 쫓아내는 것 vs 자발적으로 나가게 하는 것
- **Non-preemptive 스케쥴링**
  - 어떤 프로세스가 선점을 하고 나면 그 프로세스가 자발적으로 release하기 전까지는 terminate하거나 switching하지 않는다. 쓰도록 내버려둔다.
- **Preemptive 스케쥴링**
  - 프로세스가 스케쥴러에 의해 쫓겨날 수있다.

# Decision Making for CPU-scheduling:

1. running → waiting 해야 하는 경우: IO를 해야해서
2. running → ready 해야 하는 경우: 잠깐 쉬어야겠다고 바로 ready로 가는 경우가 있음
3. waiting → ready: IO가 다 끝나서 CPU를 점유하기 위해 ready로 이동
4. 프로세스가 terminate하는 경우

- 1, 4: no choice - non-preemptive. 자발적으로 가는 경우임. 고민할 필욕 없음
- 2, 3: choices - preemptive해야할까, non-preemptive해야 할까?

  (현대 시스템에선 대부분 preemptive이긴 함)

# Dispatcher

- CPU 스케듈러에 의해 선택된 프로세스에게 CPU코어의 컨트롤을 넘겨주는 모듈.
- 즉 컨텍스트 스위치를 해주는 모듈.
- **dispatcher의 기능****
  - 컨텍스트를 하나의 프로세스에서 다른 프로세스로 넘겨주기
   - 유저모드로 바꿔주기
    - 새로운 프로세스의 적당한 위치로 resume 시키는 것(jumping to the proper location to resume the user program)

**즉 스케쥴러는 선택해주고, **

**실제로 switching 해주는 건 dispatcher가 해준다.**

# dispatcher는 엄청나게 빨라야 한다!

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/90eb5c5e-f677-43c1-86f6-44d2ee4e5dd2/_2021-03-09__7.47.24.png](https: // s3-us-west-2.amazonaws.com/secure.notion-static.com/90eb5c5e-f677-43c1-86f6-44d2ee4e5dd2/_2021-03-09__7.47.24.png)

p0와 p1이 서로 컨텍스트 스위치 한다고 하면,

pcb0에 상태를 저장하고, pcb1을 restore해와야 한다.

이 시간을 dispatch latency라고 한다.

- dispatch latency
  - the time to stop one process and start another running
   - cpu의 실제 실행시간보다 더 길다면.. no
    - 가급적이면 짧아야 한다.

# 얼마나 자주 context switch가 발생할까?

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/36685f65-3a89-4a36-ba09-39df8bca3c92/_2021-03-09__7.55.07.png](https: // s3-us-west-2.amazonaws.com/secure.notion-static.com/36685f65-3a89-4a36-ba09-39df8bca3c92/_2021-03-09__7.55.07.png)

vmstat 명령어를 통해 확인할 수 있다.

# Scheduling의 목표

1. ** CPU utilization **: CPU가 가능한 바쁘게 만들기
2. ** Throughput **: throughput 높이기. 어떤 단위 시간 내에 프로세스 완결수를 높이자.
3. ** Turnaround time**: **
  - 어떤 프로세스가 도착하고 난 다음에 실행시키라고 했을때 제출한 이후에 completion까지
   - 제출하고 종료되는 시간까지를 단축시키는 것
4. ** Waiting time**: (주로 볼 것)**
  - 어떤 프로세스가 ready 큐에 대기하고 있는 시간을 최소화 시키자.
   - 레디 큐의 대기시간을 합친것을 최소화 시키자는 것
5. ** Response time: **
  - response 시간을 줄이자(주로 유저 인터페이스. 게임에서 몬스터 공격 시간)

# CPU Scheduling Problem

- 레디 큐에 있는 프로세스들 중에서 어떤 프로세스에게 CPU를 할당해주는 것

- solutions
   - FCFS: First-Come, First-Served
      - 문제가 많음. 아주 초창기에 씀. 지금은 아무도 안씀
    - SJF: Shortest Job First (SRTF: Shortest Remaining Time First)
    - **RR: Round-Robin****
      - 우리는 시분할을 하는데, 시분할은 RR과 관련되어있다. Round-Robin은 타임쉐어링을 해서 정해진 시간을 정해놓고 쪼개진 시간에 living 을 시키는 방법
    - Priority-based
      - RR을 쓰는데 우선순위를 부여해서 선정을 하는 방식.
    - MLQ: Multi-Level Queue
      - 어떤 경우엔 이걸쓰고, 어떤경우엔 저걸쓰고..
