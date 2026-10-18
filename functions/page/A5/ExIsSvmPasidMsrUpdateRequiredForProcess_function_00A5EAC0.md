# ExIsSvmPasidMsrUpdateRequiredForProcess

- RVA: `0x00A5EAC0`–`0x00A5EAED` (길이 `45` bytes)
- VA: `0x0000000140A5EAC0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068370`
- 디코드: `15`개 명령, `45/45` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A5EAC6` → [ExIsSvmEnabledForProcess](../../text/49/ExIsSvmEnabledForProcess_function_00496004.md) (function, `0x00496004`)
- `0x00A5EAD7` → [KeIsEnqueueStoreSupported](../../text/4B/KeIsEnqueueStoreSupported_function_004B1E8C.md) (function, `0x004B1E8C`)

### Direct callers
- [ExpAssignPasid](../7D/ExpAssignPasid_function_007D0AB8.md) at `0x007D0AF2`
- [PspRecheckThreadPasidMsrState](PspRecheckThreadPasidMsrState_function_00A5EA5C.md) at `0x00A5EA70`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A5EAC6` → [ExIsSvmEnabledForProcess](../../text/49/ExIsSvmEnabledForProcess_function_00496004.md) (`PAGE` → `.text`)
  - `0x00A5EAD7` → [KeIsEnqueueStoreSupported](../../text/4B/KeIsEnqueueStoreSupported_function_004B1E8C.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A5EAC0  48 83 EC 28                     sub rsp, 0x28
00A5EAC4  32 D2                           xor dl, dl
00A5EAC6  E8 39 75 A3 FF                  call 0x140496004
00A5EACB  84 C0                           test al, al
00A5EACD  75 08                           jne 0x140a5ead7
00A5EACF  8A C2                           mov al, dl
00A5EAD1  48 83 C4 28                     add rsp, 0x28
00A5EAD5  C3                              ret
00A5EAD6  CC                              int3
00A5EAD7  E8 B0 33 A5 FF                  call 0x1404b1e8c
00A5EADC  84 C0                           test al, al
00A5EADE  0F B6 D2                        movzx edx, dl
00A5EAE1  41 B8 01 00 00 00               mov r8d, 1
00A5EAE7  41 0F 45 D0                     cmovne edx, r8d
00A5EAEB  EB E2                           jmp 0x140a5eacf
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExIsSvmPasidMsrUpdateRequiredForProcess(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = 0;
    result = ExIsSvmEnabledForProcess(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00A5EAD7;
loc_00A5EACF:
    v_rsp = (v_rsp) + (40);
    return 0;
loc_00A5EAD7:
    result = KeIsEnqueueStoreSupported(a1, a2, a3, a4);
    a2 = 0;
    if ((unsigned __int8)(result) != 0) { a2 = 1; }
    goto loc_00A5EACF;
}
```

## 5. (Beta) C Style

```c
int64_t ExIsSvmPasidMsrUpdateRequiredForProcess(int64_t Arg1, uint8_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = 0;
    result = ExIsSvmEnabledForProcess(Arg1, Arg2, a3, a4);
    if ((uint8_t)(result) != 0) goto loc_00A5EAD7;
loc_00A5EACF:
    local_rsp = (local_rsp) + (40);
    return 0;
loc_00A5EAD7:
    result = KeIsEnqueueStoreSupported(Arg1, Arg2, a3, a4);
    Arg2 = 0;
    if ((uint8_t)(result) != 0) { Arg2 = 1; }
    goto loc_00A5EACF;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A5EAC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A5EAC0[BB_00A5EAC0]
  bb_00A5EACF[BB_00A5EACF]
  bb_00A5EAD6[BB_00A5EAD6]
  bb_00A5EAD7[BB_00A5EAD7]
  bb_00A5EAC0 -->|branch| bb_00A5EAD7
  bb_00A5EAC0 -->|fallthrough| bb_00A5EACF
  bb_00A5EAD6 -->|flow| bb_00A5EAD7
  bb_00A5EAD7 -->|branch| bb_00A5EACF
```
