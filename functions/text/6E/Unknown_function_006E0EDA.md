# sub_006E0EDA

- RVA: `0x006E0EDA`–`0x006E0EF0` (길이 `22` bytes)
- VA: `0x00000001406E0EDA`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00074138`
- 디코드: `6`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006E0EDE` → [KeYieldProcessorEx](../3F/KeYieldProcessorEx_function_003FBD00.md) (function, `0x003FBD00`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006E0EEB` → [KiSearchForNewThreadsOnTarget + 0x1D0F](../30/KiSearchForNewThreadsOnTarget_function_0030F500.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E0EDA  48 8D 4D 58                     lea rcx, [rbp + 0x58]
006E0EDE  E8 1D AE D1 FF                  call 0x1403fbd00
006E0EE3  49 8B 06                        mov rax, qword ptr [r14]
006E0EE6  48 85 C0                        test rax, rax
006E0EE9  75 EF                           jne 0x1406e0eda
006E0EEB  E9 1F 03 C3 FF                  jmp 0x14031120f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006E0EDA(void)
{
    __int64 result;

    result = KeYieldProcessorEx(v_rbp + 88, a2, a3, a4);
    if (*(unsigned __int64 *)(v_r14) != 0) goto loc_006E0EDA;
}
```

## 5. (Beta) C Style

```c
void sub_006E0EDA(void)
{
    int64_t result;

    result = KeYieldProcessorEx(local_rbp + 88, a2, a3, a4);
    if (*(uint64_t *)(local_r14) != 0) goto loc_006E0EDA;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E0EDA&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E0EDA[BB_006E0EDA]
  bb_006E0EEB[BB_006E0EEB]
  bb_006E0EDA -->|branch| bb_006E0EDA
  bb_006E0EDA -->|fallthrough| bb_006E0EEB
```
