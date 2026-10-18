# PoSetPowerRequest

- RVA: `0x00477530`–`0x00477569` (길이 `57` bytes)
- VA: `0x0000000140477530`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009D63C`
- 디코드: `20`개 명령, `57/57` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00477544` → [PopPowerRequestReferenceAcquire](PopPowerRequestReferenceAcquire_function_004776C0.md) (function, `0x004776C0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0047755C` → [sub_006F44D8](../6F/Unknown_function_006F44D8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00477530  48 83 EC 28                     sub rsp, 0x28
00477534  33 C0                           xor eax, eax
00477536  85 D2                           test edx, edx
00477538  74 08                           je 0x140477542
0047753A  83 EA 01                        sub edx, 1
0047753D  75 10                           jne 0x14047754f
0047753F  8D 42 01                        lea eax, [rdx + 1]
00477542  8B D0                           mov edx, eax
00477544  E8 77 01 00 00                  call 0x1404776c0
00477549  48 83 C4 28                     add rsp, 0x28
0047754D  C3                              ret
0047754E  CC                              int3
0047754F  83 EA 01                        sub edx, 1
00477552  75 05                           jne 0x140477559
00477554  8D 42 02                        lea eax, [rdx + 2]
00477557  EB E9                           jmp 0x140477542
00477559  83 FA 01                        cmp edx, 1
0047755C  0F 84 76 CF 27 00               je 0x1406f44d8
00477562  B8 BB 00 00 C0                  mov eax, 0xc00000bb
00477567  EB E0                           jmp 0x140477549
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PoSetPowerRequest(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = 0;
    if (a2 == 0) goto loc_00477542;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_not_equal) goto loc_0047754F;
loc_00477542:
    result = PopPowerRequestReferenceAcquire(a1, (unsigned int)((unsigned int)(a2 + 1)), a3, a4);
loc_00477549:
    v_rsp = (v_rsp) + (40);
    return result;
loc_0047754F:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a2 + 1))) - (1));
    if (condition_is_not_equal) goto loc_00477559;
    goto loc_00477542;
loc_00477559:
    goto loc_00477549;
}
```

## 5. (Beta) C Style

```c
int64_t PoSetPowerRequest(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = 0;
    if (Arg2 == 0) goto loc_00477542;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_not_equal) goto loc_0047754F;
loc_00477542:
    result = PopPowerRequestReferenceAcquire(Arg1, (uint32_t)((uint32_t)(Arg2 + 1)), a3, a4);
loc_00477549:
    local_rsp = (local_rsp) + (40);
    return result;
loc_0047754F:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg2 + 1))) - (1));
    if (condition_is_not_equal) goto loc_00477559;
    goto loc_00477542;
loc_00477559:
    goto loc_00477549;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00477530&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00477530[BB_00477530]
  bb_0047753A[BB_0047753A]
  bb_0047753F[BB_0047753F]
  bb_00477542[BB_00477542]
  bb_00477549[BB_00477549]
  bb_0047754E[BB_0047754E]
  bb_0047754F[BB_0047754F]
  bb_00477554[BB_00477554]
  bb_00477559[BB_00477559]
  bb_00477562[BB_00477562]
  bb_00477530 -->|branch| bb_00477542
  bb_00477530 -->|fallthrough| bb_0047753A
  bb_0047753A -->|branch| bb_0047754F
  bb_0047753A -->|fallthrough| bb_0047753F
  bb_0047753F -->|flow| bb_00477542
  bb_00477542 -->|flow| bb_00477549
  bb_0047754E -->|flow| bb_0047754F
  bb_0047754F -->|branch| bb_00477559
  bb_0047754F -->|fallthrough| bb_00477554
  bb_00477554 -->|branch| bb_00477542
  bb_00477559 -->|fallthrough| bb_00477562
  bb_00477562 -->|branch| bb_00477549
```
