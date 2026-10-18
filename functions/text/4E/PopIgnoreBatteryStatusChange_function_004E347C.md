# PopIgnoreBatteryStatusChange

- RVA: `0x004E347C`–`0x004E34C3` (길이 `71` bytes)
- VA: `0x00000001404E347C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `19`개 명령, `71/71` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x004E3493` → [KeCancelTimer](../23/KeCancelTimer_function_002327E0.md) (function, `0x002327E0`)
- `0x004E34B1` → [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)

### Direct callers
- [PopTransitionSystemPowerStateEx](../../pagelk/B7/PopTransitionSystemPowerStateEx_function_00B7E8C0.md) at `0x00B7EAD5`

### Static image references
- `0x004E3482` → RVA `0x00F0C0C0` (`.data`; read/write)
- `0x004E348C` → RVA `0x00F0C0C8` (`.data`; read)
- `0x004E34A2` → RVA `0x00F0C148` (`.data`; read)
- `0x004E34B6` → RVA `0x00F0C180` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004E347C  48 83 EC 38                     sub rsp, 0x38
004E3480  33 C0                           xor eax, eax
004E3482  87 05 38 8C A2 00               xchg dword ptr [rip + 0xa28c38], eax
004E3488  85 C0                           test eax, eax
004E348A  74 2A                           je 0x1404e34b6
004E348C  48 8D 0D 35 8C A2 00            lea rcx, [rip + 0xa28c35]
004E3493  E8 48 F3 D4 FF                  call 0x1402327e0
004E3498  84 C0                           test al, al
004E349A  75 1A                           jne 0x1404e34b6
004E349C  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
004E34A2  48 8D 0D 9F 8C A2 00            lea rcx, [rip + 0xa28c9f]
004E34A9  45 33 C9                        xor r9d, r9d
004E34AC  45 33 C0                        xor r8d, r8d
004E34AF  33 D2                           xor edx, edx
004E34B1  E8 FA B1 D2 FF                  call 0x14020e6b0
004E34B6  C6 05 C3 8C A2 00 01            mov byte ptr [rip + 0xa28cc3], 1
004E34BD  48 83 C4 38                     add rsp, 0x38
004E34C1  C3                              ret
004E34C2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopIgnoreBatteryStatusChange(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    result = 0;
    if (0 == 0) goto loc_004E34B6;
    result = KeCancelTimer(v_rip + 10652725, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) {
        a1 = v_rip + 10652831;
        a4 = 0;
        a3 = 0;
        a2 = 0;
        result = KeWaitForSingleObject(a1, a2, a3, a4);
    }
    *(unsigned __int8 *)(v_rip + 10652867) = 1;
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopIgnoreBatteryStatusChange(int64_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    result = 0;
    if (0 == 0) goto loc_004E34B6;
    result = KeCancelTimer(v_rip + 10652725, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) {
        Arg1 = v_rip + 10652831;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = 0;
        result = KeWaitForSingleObject(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint8_t *)(v_rip + 0xA28CC3) = 1;
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004E347C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004E347C[BB_004E347C]
  bb_004E348C[BB_004E348C]
  bb_004E349C[BB_004E349C]
  bb_004E34B6[BB_004E34B6]
  bb_004E34C2[BB_004E34C2]
  bb_004E347C -->|branch| bb_004E34B6
  bb_004E347C -->|fallthrough| bb_004E348C
  bb_004E348C -->|branch| bb_004E34B6
  bb_004E348C -->|fallthrough| bb_004E349C
  bb_004E349C -->|flow| bb_004E34B6
```
