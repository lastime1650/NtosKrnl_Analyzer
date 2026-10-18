# DbgkpSuspendProcess

- RVA: `0x008A34D4`–`0x008A350B` (길이 `55` bytes)
- VA: `0x00000001408A34D4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007EE6C`
- 디코드: `18`개 명령, `55/55` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008A34ED` → [PsFreezeProcess](../AA/PsFreezeProcess_function_00AA6D04.md) (function, `0x00AA6D04`)
- `0x008A3502` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)

### Direct callers
- [sub_006F88AE](../../text/6F/Unknown_function_006F88AE.md) at `0x006F88C7`
- [DbgkForwardException](DbgkForwardException_function_008A2D60.md) at `0x008A2F2B`
- [DbgkpSendApiMessageLpc](../92/DbgkpSendApiMessageLpc_function_00920E4C.md) at `0x00920E8E`
- [DbgkpSendErrorMessage](../92/DbgkpSendErrorMessage_function_009210A8.md) at `0x0092118F`
- [DbgkpSendApiMessage](../A7/DbgkpSendApiMessage_function_00A79458.md) at `0x00A794BD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x008A3502` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008A34D4  40 53                           push rbx
008A34D6  48 83 EC 20                     sub rsp, 0x20
008A34DA  65 48 8B 1C 25 88 01 00 00      mov rbx, qword ptr gs:[0x188]
008A34E3  33 D2                           xor edx, edx
008A34E5  66 FF 8B E4 01 00 00            dec word ptr [rbx + 0x1e4]
008A34EC  90                              nop
008A34ED  E8 12 38 20 00                  call 0x140aa6d04
008A34F2  84 C0                           test al, al
008A34F4  74 09                           je 0x1408a34ff
008A34F6  B0 01                           mov al, 1
008A34F8  48 83 C4 20                     add rsp, 0x20
008A34FC  5B                              pop rbx
008A34FD  C3                              ret
008A34FE  CC                              int3
008A34FF  48 8B CB                        mov rcx, rbx
008A3502  E8 E9 BA 9B FF                  call 0x14025eff0
008A3507  32 C0                           xor al, al
008A3509  EB ED                           jmp 0x1408a34f8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DbgkpSuspendProcess(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a2 = 0;
    result = PsFreezeProcess(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_008A34FF;
loc_008A34F8:
    v_rsp = (v_rsp) + (32);
    return 1;
loc_008A34FF:
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    result = 0;
    goto loc_008A34F8;
}
```

## 5. (Beta) C Style

```c
int64_t DbgkpSuspendProcess(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg2 = 0;
    result = PsFreezeProcess(Arg1, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_008A34FF;
loc_008A34F8:
    local_rsp = (local_rsp) + (32);
    return 1;
loc_008A34FF:
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, a3, a4);
    result = 0;
    goto loc_008A34F8;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008A34D4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008A34D4[BB_008A34D4]
  bb_008A34F6[BB_008A34F6]
  bb_008A34F8[BB_008A34F8]
  bb_008A34FE[BB_008A34FE]
  bb_008A34FF[BB_008A34FF]
  bb_008A34D4 -->|branch| bb_008A34FF
  bb_008A34D4 -->|fallthrough| bb_008A34F6
  bb_008A34F6 -->|flow| bb_008A34F8
  bb_008A34FE -->|flow| bb_008A34FF
  bb_008A34FF -->|branch| bb_008A34F8
```
