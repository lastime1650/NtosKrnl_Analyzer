# CcSetTelemetryPeriodicTimer

- RVA: `0x00ADB788`–`0x00ADB7C7` (길이 `63` bytes)
- VA: `0x0000000140ADB788`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `15`개 명령, `63/63` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00ADB7BC` → [KeSetCoalescableTimer](../../text/22/KeSetCoalescableTimer_function_0022FFD0.md) (function, `0x0022FFD0`)

### Direct callers
- [CcSetValidData](../../text/29/CcSetValidData_function_00299420.md) at `0x00299573`
- [CcAsyncCopyRead](../../text/35/CcAsyncCopyRead_function_00358880.md) at `0x00358B02`
- [CcFlushCachePreProcess](../../text/35/CcFlushCachePreProcess_function_0035A9B0.md) at `0x0035AA87`
- [CcCopyWriteEx](../../text/3C/CcCopyWriteEx_function_003CA4F0.md) at `0x003CA744`
- [CcCopyReadEx](../../text/45/CcCopyReadEx_function_0045E160.md) at `0x0045E3CD`
- [CcInitializeTelemetry](../../init/BE/CcInitializeTelemetry_function_00BEE848.md) at `0x00BEE97C`

### Static image references
- `0x00ADB793` → RVA `0x00F8F3C4` (`.data`; read)
- `0x00ADB79D` → RVA `0x00F8F3D0` (`.data`; read)
- `0x00ADB7A7` → RVA `0x00F8F410` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00ADB7BC` → [KeSetCoalescableTimer](../../text/22/KeSetCoalescableTimer_function_0022FFD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ADB788  48 83 EC 38                     sub rsp, 0x38
00ADB78C  BA 01 00 00 00                  mov edx, 1
00ADB791  33 C0                           xor eax, eax
00ADB793  F0 0F B1 15 29 3C 4B 00         lock cmpxchg dword ptr [rip + 0x4b3c29], edx
00ADB79B  75 24                           jne 0x140adb7c1
00ADB79D  48 8D 05 2C 3C 4B 00            lea rax, [rip + 0x4b3c2c]
00ADB7A4  48 8B D1                        mov rdx, rcx
00ADB7A7  48 8D 0D 62 3C 4B 00            lea rcx, [rip + 0x4b3c62]
00ADB7AE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00ADB7B3  41 B9 98 3A 00 00               mov r9d, 0x3a98
00ADB7B9  45 33 C0                        xor r8d, r8d
00ADB7BC  E8 0F 48 75 FF                  call 0x14022ffd0
00ADB7C1  48 83 C4 38                     add rsp, 0x38
00ADB7C5  C3                              ret
00ADB7C6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcSetTelemetryPeriodicTimer(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    result = 0;
    if (!(condition_is_not_equal)) {
        result = v_rip + 4930604;
        a2 = a1;
        a1 = v_rip + 4930658;
        v_stack_m18 = result;
        a4 = 0x3A98ULL;
        a3 = 0;
        result = KeSetCoalescableTimer(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CcSetTelemetryPeriodicTimer(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    result = 0;
    if (!(condition_is_not_equal)) {
        result = v_rip + 4930604;
        Arg2 = Arg1;
        Arg1 = v_rip + 4930658;
        v_stack_m18 = result;
        a4 = 0x3A98ULL;
        Arg3 = 0;
        result = KeSetCoalescableTimer(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ADB788&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00ADB788[BB_00ADB788]
  bb_00ADB79D[BB_00ADB79D]
  bb_00ADB7C1[BB_00ADB7C1]
  bb_00ADB7C6[BB_00ADB7C6]
  bb_00ADB788 -->|branch| bb_00ADB7C1
  bb_00ADB788 -->|fallthrough| bb_00ADB79D
  bb_00ADB79D -->|flow| bb_00ADB7C1
```
