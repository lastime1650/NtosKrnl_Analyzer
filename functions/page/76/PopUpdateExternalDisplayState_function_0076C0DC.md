# PopUpdateExternalDisplayState

- RVA: `0x0076C0DC`–`0x0076C12B` (길이 `79` bytes)
- VA: `0x000000014076C0DC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `22`개 명령, `79/79` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0076C0E4` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x0076C109` → [PopDiagTraceExternalDisplayState](PopDiagTraceExternalDisplayState_function_00761540.md) (function, `0x00761540`)
- `0x0076C11A` → [PopQueueWorkItem](../../text/4A/PopQueueWorkItem_function_004A20F8.md) (function, `0x004A20F8`)
- `0x0076C11F` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)

### Direct callers
- [PopPowerInformationInternal](../A8/PopPowerInformationInternal_function_00A8B7C0.md) at `0x00A8BF68`

### Static image references
- `0x0076C0E9` → RVA `0x00E67A54` (`.data`; write)
- `0x0076C0F5` → RVA `0x00E67884` (`.data`; read)
- `0x0076C113` → RVA `0x00F092A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0076C0E4` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (`PAGE` → `PAGELK`)
  - `0x0076C11A` → [PopQueueWorkItem](../../text/4A/PopQueueWorkItem_function_004A20F8.md) (`PAGE` → `.text`)
  - `0x0076C11F` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (`PAGE` → `PAGELK`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0076C0DC  40 53                           push rbx
0076C0DE  48 83 EC 20                     sub rsp, 0x20
0076C0E2  8A D9                           mov bl, cl
0076C0E4  E8 D7 C2 40 00                  call 0x140b783c0
0076C0E9  88 1D 65 B9 6F 00               mov byte ptr [rip + 0x6fb965], bl
0076C0EF  B2 01                           mov dl, 1
0076C0F1  84 DB                           test bl, bl
0076C0F3  74 12                           je 0x14076c107
0076C0F5  80 3D 88 B7 6F 00 00            cmp byte ptr [rip + 0x6fb788], 0
0076C0FC  B8 03 00 00 00                  mov eax, 3
0076C101  0F B6 D2                        movzx edx, dl
0076C104  0F 45 D0                        cmovne edx, eax
0076C107  8A CB                           mov cl, bl
0076C109  E8 32 54 FF FF                  call 0x140761540
0076C10E  BA 01 00 00 00                  mov edx, 1
0076C113  48 8D 0D 86 D1 79 00            lea rcx, [rip + 0x79d186]
0076C11A  E8 D9 5F D3 FF                  call 0x1404a20f8
0076C11F  E8 EC C2 40 00                  call 0x140b78410
0076C124  48 83 C4 20                     add rsp, 0x20
0076C128  5B                              pop rbx
0076C129  C3                              ret
0076C12A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopUpdateExternalDisplayState(unsigned __int8 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = PopAcquirePolicyLock(a1, a2, a3, a4);
    *(unsigned __int8 *)(v_rip + 7321957) = a1;
    if (a1 != 0) {
        result = 3;
        a2 = 1;
        if ((*(unsigned __int8 *)(v_rip + 7321480)) != 0) { a2 = (unsigned int)(result); }
    }
    result = PopDiagTraceExternalDisplayState(a1, a2, a3, a4);
    result = PopQueueWorkItem(v_rip + 7983494, 1, a3, a4);
    result = PopReleasePolicyLock(v_rip + 7983494, 1, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopUpdateExternalDisplayState(uint8_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = PopAcquirePolicyLock(Arg1, a2, a3, a4);
    *(uint8_t *)(v_rip + 0x6FB965) = Arg1;
    if (Arg1 != 0) {
        result = 3;
        a2 = 1;
        if ((*(uint8_t *)(v_rip + 0x6FB788)) != 0) { a2 = (uint32_t)(result); }
    }
    result = PopDiagTraceExternalDisplayState(Arg1, a2, a3, a4);
    result = PopQueueWorkItem(v_rip + 7983494, 1, a3, a4);
    result = PopReleasePolicyLock(v_rip + 7983494, 1, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0076C0DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0076C0DC[BB_0076C0DC]
  bb_0076C0F5[BB_0076C0F5]
  bb_0076C107[BB_0076C107]
  bb_0076C12A[BB_0076C12A]
  bb_0076C0DC -->|branch| bb_0076C107
  bb_0076C0DC -->|fallthrough| bb_0076C0F5
  bb_0076C0F5 -->|flow| bb_0076C107
```
