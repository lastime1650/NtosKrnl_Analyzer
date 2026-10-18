# NtosKrnl 시뮬레이터

`simulator/index.html`은 브라우저에서 실행하는 WDM API 계약 시뮬레이터입니다. 컴파일러 없이 노드로 드라이버의 실행 흐름과 데이터 흐름을 구성합니다. 로컬 HTTP 제어 패널의 **NtosKrnl 시뮬레이터** 버튼으로 여세요. 메모리와 프로그램 상태는 브라우저 안에 있으며 시스템 커널이나 하드웨어를 조작하지 않습니다.

## 사용

1. 예제를 선택하고 **예제 열기**를 누릅니다. 기본 예제는 풀 할당 → if 검사 → 해제 → 반환입니다.
2. 왼쪽 API, 자료형, enum, 전역 define, 흐름, 프로세스 노드를 클릭하거나 캔버스에 끌어 추가합니다. 흰 핀은 실행 순서, 색 핀은 데이터입니다. 출력 핀을 누르고 입력 핀을 누르거나 드래그해 연결합니다.
3. 노드를 선택하면 우측 패널에서 인자, 자료형 출력 연결, 다음 실행 대상, 중단점을 수정할 수 있습니다. API 인자에 연결이 없으면 해당 값/선택을 사용합니다. 고정된 상수 인자는 드롭다운 또는 플래그 체크박스로 구성합니다.
4. **시뮬레이션 시작**, **일시정지**, **한 단계**로 실행합니다. F5는 시작, F10은 한 단계, 우클릭은 노드 중단점입니다. 빈 공간 드래그로 이동, 휠로 확대, **화면 맞춤**으로 전체를 봅니다.
5. 우측 **설정**에서 1–128 MB의 가상 커널 메모리, DriverEntry 주소/레지스트리 경로, Seed, 실행 한도를 정합니다. 새 실행에 적용됩니다.
6. BSOD 재시도는 진단 내용을 유지하며 실패 노드를 빨갛게 표시합니다. 노드 인자나 연결 등 프로그램을 수정해야 다시 시작할 수 있습니다. 단순 화면 이동은 수정을 의미하지 않습니다.
7. 그래프는 이미지 해시별로 로컬 자동 저장됩니다. JSON 파일 저장/불러오기 및 실행 취소/다시 실행을 제공합니다. 가져오는 그래프는 노드 종류, EXPORT, 크기, 연결과 자료형을 검사합니다.

## 모델과 바이너리의 관계

- API 카탈로그는 선택된 PE의 export directory에서 생성합니다. 이름 없는 ordinal export도 유지하며 데이터 export와 forwarder는 호출 노드로 실행하지 않습니다.
- 실행 계약이 있는 API는 카탈로그에서 기본 표시합니다. 전체 EXPORT 카탈로그에 포함된 미구현 API도 배치할 수 있지만 실행 전에 차단합니다. 임의의 인자 서명이나 성공 결과를 만들지 않습니다.
- API/인자 모델은 공개 DDI 계약에 기초합니다. 풀 메모리, 문자열, 이벤트/타이머/DPC, IRQL/스핀락, 장치 객체, 가상 MMIO의 제한된 상태 전이를 구현합니다. 아직 모델이 없는 플래그/대기 모드는 명시적으로 중단합니다.
- 콜 스택의 `nt!` 프레임은 시뮬레이터가 호출한 EXPORT입니다. `sim!` 프레임은 구현된 계약 처리 단계입니다. 실제 ntoskrnl CPU 명령을 실행하는 에뮬레이터는 아닙니다.
- 내부 호출 근거 뷰는 SHA256이 일치하는 PE에서 Capstone으로 해석한 직접 `call` 후보입니다. PDB 이름과 함수 RVA를 연결하고 두 단계까지 탐색합니다. 분기 도달성, 간접 호출, 꼬리 분기, 전체 실행 경로와 SMP 스케줄링을 재구성하지 않습니다. 정적 후보를 실제 실행 스택에 넣지 않습니다.
- `KTIMER`, `KDPC`, `DRIVER_OBJECT` 등의 opaque 노드는 모델 객체 저장소입니다. 그 저장소 크기는 시뮬레이션용이며 해당 Windows 빌드의 비공개 구조체 레이아웃을 뜻하지 않습니다. 명시적인 필드가 있는 `UNICODE_STRING`, `ANSI_STRING`, `IO_STATUS_BLOCK`, `OBJECT_ATTRIBUTES`, `LIST_ENTRY` 및 사용자 구조체에는 바이트 값을 기록합니다. 숫자 노드는 값과 주소 출력 모두를 제공합니다.
- WCHAR는 UTF-16 코드 단위입니다. ANSI는 단일 바이트 문자열 모델이며 0–255 범위를 벗어난 문자에는 WCHAR를 사용하도록 안내합니다. 코드 페이지 변환과 locale 모델은 없습니다.
- NTSTATUS와 BugCheck는 별개로 표시합니다. 예측한 중단은 이 모델의 오류 진단이며 실제 Windows가 반드시 같은 코드를 발생시킨다는 보장은 아닙니다. 풀 부족에 따른 NULL/NTSTATUS 실패는 BSOD와 구분합니다.

## 가상 시간 / 메모리 / 하드웨어

가상 시간은 실행 중에만 배속에 맞게 증가합니다. 상대 DueTime은 음수 100ns 단위, 절대 시각은 Windows 시간 epoch를 사용합니다. 타이머 큐와 DPC 큐를 처리하고 단일 가상 CPU에서 DPC를 IRQL 2로 호출한 다음 이전 문맥을 복원합니다. 주기 타이머는 취소하거나 중지할 때까지 계속됩니다. 이는 실제 CPU 사이클·인터럽트 지연 측정값이 아닙니다.

풀은 Uint8Array 기반이며 주소, 요청 크기, 정렬, 태그, paged/nonpaged 속성, live/freed 상태와 free list를 관리합니다. 범위 초과, 잘못된 해제, 이중 해제, 태그 불일치, IRQL 위반을 검사합니다. 해제한 공간은 병합해 재사용합니다. 루틴 종료 후 살아 있는 풀 블록은 디버거에서 확인할 수 있습니다.

가상 주변 장치는 BAR0 `0xF0000000..0xF0000FFF`를 가집니다. `MmMapIoSpace[Ex]`로 매핑하고 Memory Write 노드로 +0x00의 DOORBELL에 32비트 값을 쓰면 가상 250ms 뒤 STATUS(+0x04)=1, IRQ 카운터가 증가합니다. 특정 GPU, 실제 PCI 버스, DMA, 실제 ISR 실행을 재현하는 장치는 아닙니다.

## 버전별 생성

`build_simulator.py --root <분석 폴더> --exe <ntoskrnl.exe>`는 분석 SHA256과 실행 파일이 일치하는지 검사하고 `simulator/catalog.js`를 만듭니다. 기존 `build_control_panel.py`와 동적 분석 runner에도 연결되어 새 버전 프로젝트에 UI/엔진/카탈로그를 함께 복사·생성합니다. 새 버전에서 없어진 EXPORT는 그래프 실행에 사용할 수 없습니다. API 계약 엔진 자체에 새 버전의 비공개 구현이 자동으로 추가되는 것은 아닙니다.

## enum / 전역 define

- **enum**: POOL_TYPE, EVENT_TYPE, TIMER_TYPE, KPROCESSOR_MODE, KAPC_ENVIRONMENT, KWAIT_REASON, MEMORY_CACHING_TYPE를 제공합니다. **사용자 enum 만들기**에서 이름, 정수 자료형, 항목 이름/값을 정하고 출력할 항목을 고릅니다. Value 핀을 API 인자에 연결합니다. enum 항목의 이름은 노드 안에서 구분됩니다.
- **전역 define**: POOL_FLAGS, IRQL, BOOLEAN, MEM_ALLOCATION, MEM_FREE, PAGE_PROTECTION, MMIO_PROTECTION, PROCESS_ACCESS, OBJECT_ATTRIBUTES_FLAGS, DEVICE_TYPE, DEVICE_CHARACTERISTICS, NTSTATUS를 제공합니다. 지원하는 계약에 필요한 상수 집합이며 전체 WDK 정의 목록은 아닙니다.
- **전역 define 만들기**로 프로젝트 정의를 추가합니다. 이름/자료형/값을 정하고 여러 노드에서 같은 전역 이름을 선택해 공유합니다. 이름 변경 후 **이름 적용 · 모든 참조 갱신**을 누르면 참조 노드, 정수 API 인자, 다른 define 표현식의 이름도 갱신됩니다. 실제 문자열 내용은 바꾸지 않습니다. 전역 정의는 노드를 삭제해도 남으며 저장한 JSON에 포함됩니다.
- 전역 값은 숫자·16진수·풀 태그·기본 상수·다른 전역 define과 `|` 조합을 지원합니다. 자료형에 맞는 정수 폭을 적용합니다. 코드 평가나 전처리기 실행은 없으며 함수형 매크로는 지원하지 않습니다. 이름 중복, 기본 상수와 충돌, 순환 참조, 잘못된 enum 항목을 실행 전에 진단합니다.
- `ExAllocatePoolWithTag.PoolType`은 풀 종류 선택, `ExAllocatePool2.Flags`는 풀 종류 1개와 UNINITIALIZED / RAISE_ON_FAILURE 체크박스입니다. BOOLEAN, IRQL, 이벤트/타이머 종류, 대기 모드, VA 할당/해제·페이지 보호, 프로세스 접근권한, 장치 종류/속성, NTSTATUS에도 선택 UI가 적용됩니다. OBJECT_ATTRIBUTES.Attributes와 상태 필드도 선택할 수 있습니다.
- 주소, 크기, 태그처럼 사용자가 정해야 하는 수치는 직접 입력하거나 데이터/define 노드를 연결합니다. 가져온 파일의 알려지지 않은 상수는 현재 값을 표시하며 자동으로 다른 값으로 바꾸지 않습니다. UI에서 보이는 일부 모드(예: UserMode 대기)는 실행 엔진의 미지원 진단으로 중단될 수 있습니다.

## 동적 if / else if / else

분기 노드 또는 우측 패널의 **+ else if 추가**로 조건을 추가합니다. `else if`는 0–64개를 지원하며 `if`와 마지막 `else`는 유지합니다. 각 조건마다 비교 연산자, 왼쪽/오른쪽 데이터 입력, 독립된 실행 출력 핀이 만들어지고 노드 높이가 자동으로 늘어납니다. NT_SUCCESS는 왼쪽 값만 검사합니다.

**↑ / ↓**로 조건 순서를 바꾸고 **×**로 삭제할 수 있습니다. 입력/출력 핀의 식별자는 표시 순서와 분리되어 있으므로 중간 조건을 삭제하거나 이동해도 나머지 조건의 연결은 유지합니다. 삭제한 조건에 연결된 선과 인자만 제거합니다. 실행 취소/다시 실행 및 JSON 저장·불러오기도 지원합니다. 기존 3갈래 그래프의 ElseLeft/ElseRight/elseIf 연결은 그대로 읽습니다.

조건은 위에서부터 평가하여 처음 참인 경로 한 개만 실행합니다. 이미 참인 조건 뒤의 데이터 입력은 읽지 않습니다. 모두 거짓이면 else를 실행합니다. 이벤트 로그에는 실제로 평가한 조건과 참/거짓 결과를 표시합니다. **정렬**은 늘어난 노드 높이를 반영하며 **노드 확대**는 분기 노드 전체 높이에 맞춰 줍니다.

## 프로세스 / 가상 주소 / 콜백

프로세스 노드는 별도 유저 VA, PID, EPROCESS 모델 객체, 드라이버용 커널 Handle과 Status를 출력합니다. 실행 입력이 없으면 시작 시 존재하는 프로세스로, Run 타이머 등에 연결되면 해당 흐름에서 생성합니다. 1000ms는 1초입니다. 프로세스 아래에서 예약/커밋 영역을 확인하고 우측 패널에서 64바이트를 검사할 수 있습니다. 유저 프로그램의 실제 명령어는 실행하지 않습니다.

`ZwAllocateVirtualMemory`, `ZwFreeVirtualMemory`, `ZwProtectVirtualMemory`는 핸들 권한·주소 충돌·페이지 보호·전체 유저 커밋 한도를 검사합니다. BaseAddress와 RegionSize에는 포인터를 받는 API이므로 숫자 노드의 **Address** 출력을 연결합니다. 주소 값은 같은 노드의 **Value**에서 읽습니다. 커밋한 페이지는 바이트 배열이며 예약만 한 영역에는 페이지를 만들지 않습니다. 기본 이미지/스택은 합성된 메모리 배치입니다.

`KeStackAttachProcess`는 현재 주소 공간을 바꾸고 KAPC_STATE를 쌓습니다. `KeUnstackDetachProcess`는 LIFO 순서를 검사합니다. 스레드 소유 PID와 현재 주소 공간 PID를 구분하고, attach 누락·pageable-safe IRQL 위반·해제/읽기 전용 VA 접근을 진단합니다. 레지스터 뷰는 API/콜백의 x64 ABI 인자와 결과를 표시하는 모델이며 실제 명령 실행, 페이지 테이블/TLB, CPU 스케줄러를 에뮬레이션하지 않습니다. CR3도 주소 공간 식별용 합성 값입니다.

## for / while / break / continue

왼쪽 **흐름**에서 반복문과 계산/비교 노드를 추가합니다. 반복문의 **반복 본문** 출력은 실행할 노드로, 본문의 마지막 실행 출력은 반복문의 **↻ Repeat** 입력으로 연결합니다. **반복 완료** 출력은 다음 실행으로 연결합니다. 우측 실행 대상 선택에서도 `↻ for/while · Repeat`를 고를 수 있습니다. 본문 끝을 연결하지 않으면 진단으로 중단합니다.

| 노드 | 데이터 입력 / 동작 |
|---|---|
| for | Start 초기값은 진입 시 한 번 읽음. Index와 Limit를 선택한 연산자로 비교. 본문이 Repeat로 복귀하면 Step을 다시 읽어 증감한 후 조건 재검사. 음수 Step 지원 |
| while | 매 검사마다 Left/Right 또는 연결된 Condition을 다시 읽음. 자동 증감 없음. 본문에서 계산/Memory Write로 상태 갱신 |
| 비교 | `<`, `<=`, `>`, `>=`, `==`, `!=`의 BOOL Value 출력을 Condition에 연결 |
| 계산 | `+`, `-`, `*`, `/`, `%`, 비트 연산/시프트. 값이 필요할 때 입력을 다시 읽음. Value를 Step이나 Memory Write.Value에 연결 |
| continue | 현재 실행 문맥의 가장 안쪽 반복문으로 복귀. for는 Step 적용 후 검사, while은 바로 검사 |
| break | 가장 안쪽 반복문을 종료하고 그 반복문의 완료 출력으로 이동. 증감하지 않음 |

Condition 핀에 연결이 있으면 BOOL 조건을 우선 사용합니다. 연결하지 않으면 기본 비교식을 사용하고, 우측에서 BOOL 직접 선택 모드로 바꿀 수도 있습니다. Condition의 TRUE/FALSE 선택을 직접 바꾸면 BOOL 모드로 전환합니다. 숫자/enum/전역 define/메모리 변수/계산 노드의 출력을 시작값·상한·증감·조건 등에 연결할 수 있습니다. 메모리 변수는 숫자 노드의 Address로 쓰고 Value에서 현재 값을 읽습니다.

실행 중 노드 안과 우측 패널, 하단 **반복문** 디버거에 반복 횟수, for Index, 조건 검사 횟수, 초기화·본문·증감·continue·break·완료 상태를 표시합니다. Iteration은 본문에 들어간 횟수로 break/continue가 실행된 회차도 포함합니다. Checks는 마지막 FALSE 검사도 셉니다. 일시정지/한 단계 실행과 중단점을 지원하고, break/continue의 암묵적 이동은 점선과 이벤트 로그로 표시합니다.

중첩 반복문을 지원합니다. 내부 반복이 끝나면 외부 Repeat로 복귀하며 각 진입마다 내부 카운터를 초기화합니다. DPC/통지/Run 타이머는 별도 반복 프레임을 사용하여 다른 실행 문맥의 break/continue가 원래 반복문을 종료하지 못합니다. 루틴 Return은 그 문맥의 모든 활성 반복문을 종료합니다.

계산과 for 인덱스는 signed 64-bit 정수 모델이며 범위를 넘으면 64-bit로 잘라냅니다. 임의 C 프로그램의 overflow 정의를 판정하는 컴파일러는 아닙니다. 나누기 0, 데이터 계산 순환, 잘못된 Repeat 진입, 반복문 밖 break/continue는 진단합니다. MaxIterations 기본 1,000회와 전역 노드 실행 한도로 무한 반복을 제한하며, 한도 초과는 시뮬레이터 진단으로 표시합니다.

예제 선택에 **for**, **while**, **break / continue**, **중첩 반복문**을 추가했습니다.

| 기본 예제 | 예상 결과 |
|---|---|
| for | Index 0–4에서 본문 5회, 최종 Index 5, 저장 값 4 |
| while | 변수 0→5 갱신, 본문 5회, 마지막 FALSE 검사 포함 6회 |
| break / continue | Index 2에서 continue, Index 5에서 break, 본문 진입 6회, 저장 값 4 |
| 중첩 반복문 | 외부 3회, 내부 매번 4회 진입 후 break, 저장 값 22 |

Process / ProcessEx / Thread / Image / Registry 전용 핸들러는 호환 서명만 등록할 수 있습니다. 등록 이후 발생한 시나리오 이벤트만 통지하며 등록 해제 뒤에는 새 통지를 하지 않습니다. ProcessEx 생성 거부는 VOID 반환값 대신 명시적인 CreationStatusSlot을 사용합니다. 레지스트리는 **PreSetValueKey 한 종류**를 지원하며 높은 altitude부터 호출하고 음수 NTSTATUS는 변경과 뒤의 필터 호출을 차단합니다. 레지스트리 post 콜백, 전체 객체 관리자/파일/보안 콜백, 실제 유저 코드 실행은 지원하지 않습니다. 자기 콜백 안의 동기 등록 해제는 교착 위험 진단으로 중단합니다.

## 사용자 정의 함수 (v2.3)

1. 상단 **+ 함수 만들기** 또는 노드 라이브러리 **사용자 함수**에서 정의를 만듭니다. 기본 함수는 입력 값을 그대로 반환합니다.
2. 우측 **함수** 탭에서 이름, 인자 이름·자료형·호출 기본값, 반환 자료형을 설정합니다. `VOID`도 지원합니다. 기본값은 호출 노드를 추가할 때 채우는 초기값이며 기존 호출의 직접 입력 값을 덮어쓰지 않습니다.
3. **편집 그래프**에서 함수별 본문을 따로 편집합니다. 함수 진입 노드의 인자 출력 → 본문/API 입력, 계산/API 출력 → 함수 반환의 반환값 입력을 연결합니다. 함수 그래프의 흐름 라이브러리는 **함수 반환**을 제공합니다. 다른 그래프 노드에 직접 배선을 연결할 수 없습니다.
4. DriverEntry/콜백/다른 함수 그래프에서 라이브러리의 함수 항목을 클릭하거나 끌어오면 호출 노드가 생깁니다. 인자는 직접 입력하거나 자료형·계산·다른 호출의 데이터 출력으로 연결합니다. `Return` 출력은 반환 후 사용할 수 있습니다. 같은 정의를 여러 호출 노드가 공유합니다.
5. 실행 시 사용자 함수 프레임이 **콜 스택**에 쌓이고 복귀하면 제거됩니다. 프레임을 클릭해 해당 그래프를 엽니다. **함수 호출** 탭은 호출별 인자·깊이·반환값·호출 위치와 복귀 기록을 보존합니다. 상단 흐름 표시에서 최근 호출/복귀를 확인합니다. 보기 전환은 실행 상태를 바꾸지 않습니다. 실행 중 본문이나 서명을 바꾸면 실행을 중지합니다.

### 값과 실행 문맥

- 정수는 선언한 폭/부호로 전달하고 포인터는 같은 가상 메모리를 참조합니다. 문자열/구조체는 포인터 형식으로 전달합니다. opaque 구조체의 값 복사, 임의 C 코드 컴파일은 제공하지 않습니다.
- 호출마다 인자, 실행 결과, 지역 자료형 저장소, 반복 프레임을 분리합니다. 지역 데이터는 반환할 때 회수합니다. 지역 변수 주소를 반환해 사용하면 해제된 메모리 접근으로 진단됩니다. EXPORT 풀 할당은 함수 반환 후에도 유지되며 호출자가 해제할 수 있습니다.
- 함수 호출은 스레드/프로세스/IRQL을 자동 변경하지 않습니다. 함수 안에서도 기존 EXPORT의 IRQL·주소 공간·핸들 계약을 적용합니다. API 단계가 끝나면 사용자 프레임을 유지합니다. DPC/시나리오가 호출을 중단한 경우 인자·지역 데이터·API 단계·반복 상태를 보관하고 복원합니다.
- `break`/`continue`는 현재 함수 안의 반복문만 대상으로 합니다. 함수 반환은 현재 함수의 반복을 정리하고 호출자의 반복을 복원합니다.
- 정의 최대 64개, 인자 16개, 동시 호출 깊이 64단계입니다. 종료 없는 재귀/반환이 빠진 경로는 모델 진단으로 중지하며 가짜 BSOD를 생성하지 않습니다. 실제 잘못된 메모리 접근은 기존 가상 BSOD와 수정 후 재시작 절차를 사용합니다.
- 프로젝트 JSON과 자동 저장에 모든 함수 정의·본문·호출·연결을 함께 저장합니다. 이름 변경은 안정된 인자 핀 ID를 보존하며 자료형 변경/삭제는 호환되지 않는 배선만 제거합니다. 함수 삭제는 본문과 모든 호출을 함께 지우며 실행 취소로 복구합니다.

| 함수 예제 | 예상 결과 |
|---|---|
| 두 곳에서 호출 | AddValues(3,4)=7 → AddValues(7,10)=17 |
| 중첩 콜 스택 | DriverEntry → DoublePlusOne(8) → DoubleValue(8)=16 → 17 |
| 함수 안의 반복문 | SumUntil(5)=10, 두 번째 호출 SumUntil(3)=3 (지역 변수 초기화) |
| 재귀 Factorial | Factorial(5)=120, 깊이 5, 각 인자/중간 결과 분리 |

## 지역변수 / 전역변수 (v2.4)

- 라이브러리 **변수 → + 지역변수 / + 전역변수**에서 정의와 참조 노드를 만듭니다. 우측에서 이름, 정수/포인터 자료형, 초기값을 설정합니다. 초기값은 정수 상수/전역 define 식이며 입력 핀의 동적 초기화는 **변수 쓰기** 노드로 표현합니다.
- 변수 노드의 **Ref**를 읽기/쓰기/증가/감소 노드의 **변수 Ref** 입력에 연결합니다. 각 연산의 자료형은 변수와 일치해야 합니다. Ref는 일반 정수/주소와 구분하며 수기로 만들어 사용할 수 없습니다.
- **변수 쓰기**의 Value, **변수 증가/감소**의 Delta에는 직접 값을 입력하거나 인자·자료형·계산·다른 노드 출력을 연결할 수 있습니다. 흰 실행 핀으로 실행 순서를 정합니다. 증감 기본값은 1입니다. Before는 변경 전, Value는 변경 후 값입니다.
- **변수 읽기**는 실행 시점의 스냅샷을 출력합니다. 변수 참조 노드의 **현재 값(Value)**은 값이 필요한 시점마다 다시 읽으므로 for/while/분기 조건에 연결할 수 있습니다. 디버거 화면을 표시하는 것만으로 값을 읽거나 변경하지 않습니다.
- **Address**는 실제 바이트 저장소의 가상 커널 주소로, Memory Read/Write나 API의 출력 인자에 연결할 수 있습니다. API가 변수에 쓰면 값과 변경 이력도 갱신합니다. 정수의 폭/부호를 적용하며 overflow는 이 모델에서 해당 비트 폭으로 래핑합니다. PVOID에 대한 증감은 바이트 단위 주소 수치 연산이며 요소 크기를 자동 추론하지 않습니다.
- 전역변수는 시뮬레이션 시작 시 한 번 초기화하고 여러 함수/콜백에서 공유합니다. 각 그래프에서 라이브러리의 동일 전역 정의를 클릭해 **참조 노드**를 추가하세요. 전역 define(불변 상수)과 변경 가능한 전역변수는 별개입니다.
- 지역변수는 각 함수 호출 때 초기화하고 반환 시 회수합니다. 재귀 호출, DriverEntry, DPC/통지/시나리오 루틴마다 저장소와 읽기 결과를 분리합니다. 중단된 호출의 지역 상태는 복귀 시 보존됩니다. 함수 간 값은 기존 인자/반환 핀으로 전달하며, 호출자의 Address를 전달하면 같은 저장소에 접근할 수 있습니다.
- 같은 지역 정의의 참조 노드를 여러 개 배치하면 현재 호출 안에서 같은 변수를 참조합니다. 다른 함수 그래프의 지역 정의는 직접 참조할 수 없습니다. 반환된 지역 Ref는 거부하며 반환된 Address는 해제된 메모리가 됩니다. 전역변수는 DriverEntry 반환 후에도 유지됩니다.
- 디버거의 **변수** 탭에서 현재/반환된 호출별 값, 주소, 쓰기 횟수와 변경 이력을 나란히 봅니다. 초기화·읽기·쓰기·증감·API 메모리 쓰기의 가상 시각, 이전/이후 값과 노드 위치를 기록합니다. 노드 이력 클릭으로 해당 그래프를 엽니다. 전체 변경 이력은 최근 2,000건, 화면은 최근 100건과 저장소 200개를 표시합니다.
- 변수 정의 최대 512개입니다. JSON 저장/불러오기에 정의·참조·연산 핀이 함께 포함됩니다. 이름 변경은 안정된 ID로 모든 참조에 반영하며 자료형 변경 시 호환되지 않는 연결을 제거합니다. 삭제/타입 변경은 실행 취소로 복구할 수 있습니다. 함수 삭제는 그 함수의 지역 정의를 함께 삭제합니다.

예제 **변수 · 지역 분리 / 전역 공유**는 Accumulate(2)의 지역 값 3, Accumulate(5)의 별도 지역 값 6을 더한 전역 Total=9에서 1을 빼 최종 **8**을 읽습니다. **변수 · while / 증감**은 현재 값 < 5 조건으로 Counter를 5회 증가시킵니다. Delta=2 데이터 핀을 연결하면 3회 반복하고 최종 6입니다.

변수 저장소는 이 모델의 NonPaged 가상 메모리입니다. 객체/문자열은 기존 자료형 노드의 저장소와 PVOID 변수로 연결할 수 있으며 구조체 자체의 값 복사는 지원하지 않습니다. 노드 증감은 직렬 가상 스케줄러의 단일 모델 단계이며 실제 Interlocked API나 SMP 메모리 순서 보장을 의미하지 않습니다.

## 배열 / 구조체 변수 (v2.5)

### 선언과 접근

- **변수** 라이브러리에 지역배열·전역배열·지역구조체·전역구조체 생성 버튼을 추가했습니다. 기존 변수의 **변수 형태**도 스칼라/배열/구조체로 바꿀 수 있습니다. 형태/타입 변경은 호환되지 않는 핀 연결을 제거하며 실행 취소로 복구합니다.
- 배열은 정수/포인터 요소를 **1–4,096개** 지원합니다. 길이, 공통 초기값, 선택적인 요소별 초기값 JSON 목록을 설정합니다. `["1","2","0x10"]`처럼 64비트 값은 문자열로 입력하세요. 생략한 요소는 공통 초기값을 사용합니다. 길이를 줄이면 초과 초기값을 제거하며 실행 취소로 복구할 수 있습니다.
- 사용자 구조체는 정수/포인터 필드 **1–64개**를 지원합니다. 이름/자료형/초기값과 pack 1/2/4/8을 설정하고 오프셋·크기·총 크기를 확인합니다. 기본은 x64 스칼라 크기에 따른 자연 정렬과 pack 8입니다. 필드 삭제 시 번호가 재배치되므로 기존 Field 번호 연결을 확인하세요.
- 배열/구조체 참조 노드는 **Ref, Count, Address**를 출력합니다. 전체 객체의 Value 출력 대신 아래 접근 노드로 요소/필드를 선택합니다. Count는 요소/필드 수, Address는 전체 저장소의 가상 주소입니다.
- **배열 요소**: 배열 Ref → Variable, 인자/반복 Index/자료형/계산/직접 입력 → Index. 인덱스는 0부터 시작합니다. 요소 자료형을 배열과 맞춥니다.
- **구조체 필드**: 대상 구조체 정의와 필드를 선택합니다. 구조체 Ref → Variable, 숫자/enum/계산/자료형 출력 → Field로 동적 선택합니다. **Field는 0부터 시작하는 필드 번호**이며 연결한 핀이 선택 드롭다운보다 우선합니다. 동적 선택 시 출력 자료형과 실제 선택 필드의 자료형이 같아야 합니다. 서로 다른 자료형의 필드를 한 출력으로 자동 변환하지 않습니다.
- 두 접근 노드는 실행 핀이 없는 데이터 노드입니다. **Ref → 변수 읽기/쓰기/증감의 Variable 입력**, Value → 계산/분기/API 입력, Address → 메모리/API 출력 인자로 연결합니다. Value는 실제 요청 시 다시 읽으며 명시적인 변수 읽기는 그 시점의 스냅샷을 만듭니다.

### 범위, 수명과 디버깅

- 기존 지역/전역 규칙을 배열과 구조체 전체 저장소에 적용합니다. 함수·재귀·DPC/통지/시나리오 호출마다 지역 객체를 새로 초기화하고 반환 시 회수합니다. 전역 객체는 모든 그래프에서 같은 정의를 참조합니다. 호출별 반환된 값은 디버거에 마지막 스냅샷으로 남습니다.
- 배열은 연속 저장소, 구조체는 필드 정렬과 tail padding이 있는 바이트 저장소입니다. 요소/필드 주소를 통한 API 쓰기도 해당 요소/필드의 변경 이력에 반영합니다. padding만 쓰는 경우 실제 필드 값 변경으로 기록하지 않습니다.
- 인덱스가 음수이거나 길이 이상, 필드 번호가 범위 밖이면 **메모리에 접근하기 전에 중단**합니다. `BOUNDS ERROR`, 허용 범위와 **실제 배열 요소/구조체 필드 접근 노드**를 표시하고 빨갛게 강조합니다. 오류 값을 수정하면 새 상태로 다시 실행할 수 있습니다. 계산 노드를 거쳐 접근해도 원래 접근 노드의 오류 위치를 보존합니다.
- 이 범위 검사는 시뮬레이터의 진단이며 실제 Windows BugCheck/NTSTATUS를 만들어 단정하지 않습니다. 원시 Address로 직접 범위를 넘기는 메모리 명령은 기존 바이트 범위/수명 검사 경로를 사용합니다.
- 변수 디버거에서 **배열 요소/구조체 필드 펼치기**로 이름, 현재 값, 자료형, 오프셋, 주소를 봅니다. 펼침 상태와 스크롤을 실시간 갱신 중 유지합니다. 배열은 128개씩 이전/다음 페이지로 전체 요소를 탐색합니다. 길이를 줄이면 페이지 위치를 유효 범위로 보정합니다. **확대 / 축소**로 변수 디버거 높이를 조절할 수 있습니다.
- JSON 저장/불러오기에 형태, 길이, 필드, 초기값, pack, Index/Field 연결을 보존합니다. 이전 스칼라 변수 문서는 그대로 지원하며 새 객체 문서는 v2.5 이상에서 여세요.

예제 **배열 / 구조체 · 함수별 지역 분리**는 전역 Buffer=[10,25,37,40], 첫 호출의 지역 State.Count=25, 두 번째 호출의 별도 State.Count=37입니다. **배열 Index 핀 · for 반복**은 지역 Buffer=[0,3,6,9], 전역 State.Count=18입니다. **범위 오류 · 배열 인덱스**는 길이 4의 배열에 인덱스 4를 요청해 agg_element에서 중단합니다.

현재 배열 요소와 구조체 필드는 스칼라/포인터입니다. 중첩 구조체, 구조체 배열, union/bitfield/가변 길이 배열은 지원하지 않습니다. 실제 Windows 비공개 구조체 배치를 추정하거나 opaque 모델 객체를 사용자 구조체로 간주하지 않습니다.

## 검증 및 로컬 배포 범위

우측 **검증 → 내장 시나리오 검증 실행**은 예제 22종, 7/33/660ms 시계 분할, 실패 경로, 풀 플래그 12조합, enum 연결, 전역 define 공유/이름 변경/순환 참조, 동적 분기와 for/while/중첩/break/continue/반복 안전 한도를 예상 결과와 비교합니다. JSON 결과를 저장할 수 있습니다. `tests/*.test.mjs`는 Node 내장 테스트 러너로 실행하며 외부 패키지는 필요 없습니다.

```powershell
node --test C:\NtKrnl2C\simulator\tests\*.test.mjs
```

검증 결과와 범위는 `test-results/verification-report.md`에 기록합니다. 이 빌드의 실행 가능한 70개 EXPORT 모델을 검사하지만, 임의의 모든 드라이버 그래프나 모든 Windows 내부 경로의 정확성을 보증하는 인증은 아닙니다. 실제 VM/WinDbg에서의 드라이버 대조 시험은 수행하지 않았습니다. 로컬 배포 ZIP은 기존 분석 프로젝트에 적용하는 소스/카탈로그 오버레이이며 ntoskrnl.exe, PDB, 37,994개 분석 문서 원본을 포함하지 않습니다.

## 근거 문서

- [DriverEntry / DRIVER_INITIALIZE](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize)
- [ExAllocatePool2](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepool2)
- [ExFreePoolWithTag](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-exfreepoolwithtag)
- [KeSetTimer](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-kesettimer)
- [Timer objects and DPCs](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/timer-objects-and-dpcs)
- [MmMapIoSpaceEx](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-mmmapiospaceex)
- [BAD_POOL_CALLER](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/bug-check-0xc2--bad-pool-caller)
- [IRQL_NOT_LESS_OR_EQUAL](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/bug-check-0xa--irql-not-less-or-equal)
- [NTSTATUS handling](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/using-ntstatus-values)
- [POOL_TYPE](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/ne-wdm-_pool_type)
- [POOL_FLAGS](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/pool_flags)
- [KeStackAttachProcess](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-kestackattachprocess)
- [ZwAllocateVirtualMemory](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwallocatevirtualmemory)
- [ZwFreeVirtualMemory](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwfreevirtualmemory)
- [Process notification registration](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/nf-ntddk-pssetcreateprocessnotifyroutineex)
- [Layered registry filtering order](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/supporting-layered-registry-filtering-drivers)
- [CmUnRegisterCallback](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-cmunregistercallback)

## 그래프 드래그 수정 (2026-10-18)

- 안정적인 캔버스에 pointer capture를 걸어 노드/핀/패닝 드래그의 해제를 수신합니다.
- 버튼 상태, pointercancel, lostpointercapture, blur, 숨김, Escape, 그래프 교체로 종료합니다.
- 그래프 내부의 기본 선택/이미지 드래그/스크롤 전파를 막고 입력란 편집은 유지합니다.
- 핀 클릭 연결은 유지하며 핀 드래그를 빈 공간에 놓으면 취소합니다.
- 자동 테스트 254/254 (드래그 17개 포함). 브라우저 합성 이벤트 검사 14/14.
- 실제 브라우저 마우스로 노드 이동과 캔버스 밖 패닝 해제를 확인했습니다. 합성 이벤트 검사는 OS 포인터 캡처의 물리 검증과 구분합니다.
- 재현 검사 페이지: `tests/drag-browser.html`. 기존 저장 그래프는 검사 후 복구합니다.

## 디버그 도구 업데이트 (2026-10-18)

- EXPORT 라이브러리의 **DbgPrint**: `{Name}`, `{0}`, `{Count:X}`, `{Pointer:p}`, `{{...}}` 지원. 오른쪽 포맷 적용 버튼으로 이름별 핀을 만들고 각 핀의 자료형 / 연결 / 직접 입력값을 설정합니다. ANSI Format 핀을 연결하면 해당 문자열이 우선합니다. 이름 기반 문자열은 편집기의 편의 기능이며 실제 DbgPrint의 ABI 문법이 아닙니다. 기존 printf 그래프는 유지됩니다. printf 모드는 가변 인자를 순서대로 추가하고 `%d`, `%u`, `%x`, `%08X`, `%p`, `%s`, `%ws`, `%wZ`, `%%` 등을 사용합니다.
- 하단 **디버그 출력**: 메시지, 가상 시간, 발생 노드를 기록하며 이벤트 로그와 별도 보관합니다. UTF-8 UI 메시지는 문자 경계를 지키며 최대 512바이트를 표시하고 잘림을 표기합니다. 메시지는 최대 2,000개입니다.
- **전체 노드 삭제**: 모든 함수 그래프와 관련 선언을 정리하고 DriverEntry만 남깁니다. Ctrl+Z로 복원할 수 있습니다.
- 노드 **우클릭 메뉴**: 속성, 확대, 중단점, 복제, 연결 해제, 삭제. DriverEntry / 함수 진입점의 복제·삭제는 막습니다.
- 중단점 / 일시정지 중 **인자명에 마우스를 올리거나 클릭**: 자료형, 현재 호출의 값, 10진수·16진수, 연결 원본, 문자열 미리보기를 표시합니다. 클릭하면 고정하고 Esc로 닫습니다. 조회로 메모리 할당이나 식 캐시를 변경하지 않습니다. 배치되지 않은 포인터·아직 실행되지 않은 출력은 상태를 명시합니다.
- **DbgPrint · 포맷과 중단점** 예제를 추가했습니다.

DbgPrint의 Unicode IRQL 제약, 부동소수점 미지원 및 출력 크기 제한 근거: [Microsoft DbgPrint 문서](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-dbgprint). 실제 Windows 디버그 필터 / 전송은 이 브라우저 모델에 포함되지 않습니다.

## 호출 깊이 디버깅 / 읽기 전용 내부 그래프

- **Step Into (F11)**: 사용자 함수 호출의 진입점으로 이동합니다. EXPORT에서는 인자를 캡처하고 내부 계약 단계 그래프를 엽니다. 이후 한 단계씩 진행합니다. 최초 클릭은 DriverEntry에서 시작 상태를 준비합니다.
- **Step Over (F10)**: 현재 사용자 함수 / EXPORT 호출의 실제 모델 동작을 실행하고 호출자의 다음 노드에서 멈춥니다. 실행 생략이 아닙니다.
- **Step Out (Shift+F11)**: 현재 API 또는 함수 호출 인스턴스에서 복귀합니다. DriverEntry에서 사용하면 DriverEntry 반환까지 진행하고 예약 이벤트는 대기 상태로 둡니다.
- 중첩 / 재귀 / DPC의 호출 문맥을 구분하며, 진행 도중 만난 중단점·DbgBreakPoint·오류를 우선합니다. 긴 명령은 브라우저에 실행권을 돌려주고 일시정지 / 중지로 취소할 수 있습니다. 무한 신호 대기에서는 멈춘 이유를 알립니다.
- 콜 스택, 실행 그래프, 인자 툴팁, 메모리 및 내부 단계 표시가 함께 갱신됩니다.
- **ExAllocatePool2**는 검사, 공간 예약, 초기화가 각각 실제 모델 동작입니다. 예약 단계의 CD 바이트는 결정적 미초기화 메모리 표식이며 Windows가 보장하는 실제 메모리 값이 아닙니다. 다른 API는 기존 계약 모델의 마지막 단계에서 검증 / 부작용이 함께 적용됨을 화면에 명시합니다.
- 내부 그래프는 사용자 프로젝트 노드 목록 밖에서 생성합니다. 노드 편집 / 삭제 / 연결 변경 / 드래그 이동을 제공하지 않으며 저장 JSON에도 내부 노드는 포함되지 않습니다. 내부 화면에서는 Delete / Ctrl+Z / Ctrl+Y로 그래프를 바꾸지 못합니다.
- **바이너리 CFG / ASM** 탭은 이 이미지와 해시가 일치하는 PE/PDB 기본 블록을 표시합니다. 실제 호출 대상의 CFG를 중첩 탐색하고 원래 ASM과 보고서를 열 수 있습니다. 이 탭의 분기와 호출은 정적 후보이며, 시뮬레이션이 실행한 CPU 경로나 비공개 내부 함수의 실행 스택이라고 표시하지 않습니다. 전체 커널 코드의 실행 의미가 복원되었다는 뜻은 아닙니다.
- 현재 내부 데이터: 9,639개 함수. 매우 큰 함수는 앞 600개 그래프 노드를 표시하고 전체 보고서를 안내합니다. 분석에 없는 대상과 이미지 불일치는 명시적으로 알립니다.
- `build_internal_graphs.py`는 새 버전 분석에서 CFG 자료를 새로 생성합니다. 원래 그래프 자료를 파싱하며 코드를 실행하지 않습니다.

## 변수 자료형 확장

- 등록된 **115개 자료형 전체**를 지역·전역 변수, 배열 요소 및 구조체 필드에서 선택할 수 있습니다. ANSI, WCHAR, ANSI_STRING, UNICODE_STRING, 정수 별칭, 형식별 포인터, IO_STATUS_BLOCK 등 고정 구조체와 KTIMER 등 모델 객체를 포함합니다. 모든 Windows/PDB 자료형의 자동 복원을 의미하지 않습니다.
- 문자열은 초기값과 버퍼 용량을 설정합니다. ANSI 용량은 바이트, WCHAR/UNICODE_STRING 용량은 UTF-16 코드 단위이며 종결 문자를 포함합니다. ANSI는 기존 단일 바이트 모델(0~255)입니다. 한글은 WCHAR/UNICODE_STRING을 선택합니다.
- ANSI_STRING/UNICODE_STRING은 Length, MaximumLength, Buffer 출력 핀을 제공합니다. 길이는 바이트 단위입니다. 변수 쓰기는 대상이 소유한 버퍼에 내용을 복사하며 용량 초과 시 원래 값을 보존하고 오류 노드에서 중단합니다. 실제 RtlInitUnicodeString의 참조 버퍼 의미는 유지합니다.
- 문자열·고정 구조체의 읽기/쓰기 값은 호출 수명에 맞는 스냅샷입니다. 지역 문자열 버퍼는 호출마다 분리하고 반환 시 회수합니다. 일반 구조체의 포인터는 바이트 복사되며 재귀 복제하지 않습니다.
- 커널 객체 변수는 Address 핀을 초기화 API에 연결합니다. 객체의 일반 값 복사·증감은 금지합니다. 증감은 정수·포인터에 제공하며 포인터 증감 단위는 바이트입니다.
- CUSTOM_STRUCT는 크기와 필드 오프셋/자료형을 정의합니다. 디버거에서 문자열 기술자·구조체·모델 객체를 펼쳐 확인합니다.
- **문자열 / 구조체 / 객체 변수** 예제: 함수의 지역 UNICODE_STRING에서 전역 변수로 복사하고 DbgPrint로 출력한 뒤 KTIMER를 초기화합니다.
- 검증: 자동 테스트 **432/432**, 브라우저 시나리오 **117/117** 통과. 115개 자료형 각각을 단일 변수·배열·구조체 필드로 초기화하고 복사·용량 초과·함수 수명·API 갱신을 검사합니다.

문자열 기술자 근거: [UNICODE_STRING](https://learn.microsoft.com/en-us/windows/win32/api/ntdef/ns-ntdef-_unicode_string), [RtlCopyUnicodeString](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlcopyunicodestring).
