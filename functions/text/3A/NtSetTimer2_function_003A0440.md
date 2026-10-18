# NtSetTimer2

- RVA: `0x003A0440`–`0x003A045B` (길이 `27` bytes)
- VA: `0x00000001403A0440`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `9`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003A0449` → [ExpSetTimer2](ExpSetTimer2_function_003A0470.md) (function, `0x003A0470`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003A0440  48 83 EC 28                     sub rsp, 0x28
003A0444  48 85 D2                        test rdx, rdx
003A0447  74 0B                           je 0x1403a0454
003A0449  E8 22 00 00 00                  call 0x1403a0470
003A044E  48 83 C4 28                     add rsp, 0x28
003A0452  C3                              ret
003A0453  CC                              int3
003A0454  B8 F0 00 00 C0                  mov eax, 0xc00000f0
003A0459  EB F3                           jmp 0x1403a044e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtSetTimer2(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a2 == 0) goto loc_003A0454;
    result = ExpSetTimer2(a1, a2, a3, a4);
loc_003A044E:
    v_rsp = (v_rsp) + (40);
    return result;
loc_003A0454:
    goto loc_003A044E;
}
```

## 5. (Beta) C Style

```c
int64_t NtSetTimer2(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg2 == 0) goto loc_003A0454;
    result = ExpSetTimer2(Arg1, Arg2, a3, a4);
loc_003A044E:
    local_rsp = (local_rsp) + (40);
    return result;
loc_003A0454:
    goto loc_003A044E;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003A0440&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003A0440[BB_003A0440]
  bb_003A0449[BB_003A0449]
  bb_003A044E[BB_003A044E]
  bb_003A0453[BB_003A0453]
  bb_003A0454[BB_003A0454]
  bb_003A0440 -->|branch| bb_003A0454
  bb_003A0440 -->|fallthrough| bb_003A0449
  bb_003A0449 -->|flow| bb_003A044E
  bb_003A0453 -->|flow| bb_003A0454
  bb_003A0454 -->|branch| bb_003A044E
```
