# PnpNotifyEarlyLaunchStatusUpdate

- RVA: `0x00BEF120`–`0x00BEF198` (길이 `120` bytes)
- VA: `0x0000000140BEF120`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000697A4`
- 디코드: `28`개 명령, `120/120` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00BEF140` → [PnpDiagnosticTraceElamStatus](../../text/5A/PnpDiagnosticTraceElamStatus_function_005A581C.md) (function, `0x005A581C`)
- `0x00BEF17E` → [ExNotifyWithProcessing](../../text/45/ExNotifyWithProcessing_function_004523F4.md) (function, `0x004523F4`)
- `0x00BEF18C` → [PnpDiagnosticTraceElamStatus](../../text/5A/PnpDiagnosticTraceElamStatus_function_005A581C.md) (function, `0x005A581C`)

### Direct callers
- [IopInitializeBootDrivers](../C2/IopInitializeBootDrivers_function_00C2E6F4.md) at `0x00C2EB12`
- [IopInitializeBootDrivers](../C2/IopInitializeBootDrivers_function_00C2E6F4.md) at `0x00C2ED3E`
- [PipInitializeCoreDriversAndElam](../C7/PipInitializeCoreDriversAndElam_function_00C73F84.md) at `0x00C74085`

### Static image references
- `0x00BEF12D` → RVA `0x010086C0` (`INITDATA`; read)
- `0x00BEF139` → RVA `0x00026D40` (`.rdata`; read)
- `0x00BEF14C` → RVA `0x00C32DD0` (`PnpEarlyLaunchStatusNotificationPreProcess`; read)
- `0x00BEF185` → RVA `0x00026F90` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00BEF140` → [PnpDiagnosticTraceElamStatus](../../text/5A/PnpDiagnosticTraceElamStatus_function_005A581C.md) (`INIT` → `.text`)
  - `0x00BEF17E` → [ExNotifyWithProcessing](../../text/45/ExNotifyWithProcessing_function_004523F4.md) (`INIT` → `.text`)
  - `0x00BEF18C` → [PnpDiagnosticTraceElamStatus](../../text/5A/PnpDiagnosticTraceElamStatus_function_005A581C.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BEF120  40 53                           push rbx
00BEF122  48 83 EC 40                     sub rsp, 0x40
00BEF126  83 64 24 60 00                  and dword ptr [rsp + 0x60], 0
00BEF12B  8B D9                           mov ebx, ecx
00BEF12D  48 83 3D 8B 95 41 00 00         cmp qword ptr [rip + 0x41958b], 0
00BEF135  74 5A                           je 0x140bef191
00BEF137  8B D1                           mov edx, ecx
00BEF139  48 8D 0D 00 7C 43 FF            lea rcx, [rip - 0xbc8400]
00BEF140  E8 D7 66 9B FF                  call 0x1405a581c
00BEF145  48 8B 0D 74 95 41 00            mov rcx, qword ptr [rip + 0x419574]
00BEF14C  48 8D 05 7D 3C 04 00            lea rax, [rip + 0x43c7d]
00BEF153  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00BEF159  4C 8D 4C 24 20                  lea r9, [rsp + 0x20]
00BEF15E  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00BEF164  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
00BEF169  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00BEF16E  33 D2                           xor edx, edx
00BEF170  48 8D 44 24 58                  lea rax, [rsp + 0x58]
00BEF175  89 5C 24 58                     mov dword ptr [rsp + 0x58], ebx
00BEF179  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00BEF17E  E8 71 32 86 FF                  call 0x1404523f4
00BEF183  8B D3                           mov edx, ebx
00BEF185  48 8D 0D 04 7E 43 FF            lea rcx, [rip - 0xbc81fc]
00BEF18C  E8 8B 66 9B FF                  call 0x1405a581c
00BEF191  48 83 C4 40                     add rsp, 0x40
00BEF195  5B                              pop rbx
00BEF196  C3                              ret
00BEF197  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpNotifyEarlyLaunchStatusUpdate(int a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;

    v_rsp = (v_rsp) - (64);
    if ((*(unsigned __int64 *)(v_rip + 4298123)) != 0) {
        a2 = a1;
        a1 = v_rip - 12354560;
        result = PnpDiagnosticTraceElamStatus(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(v_rip + 4298100);
        result = v_rip + 277629;
        a4 = v_stack_m28;
        a3 = v_stack_p18;
        v_stack_m28 = result;
        a2 = 0;
        result = v_stack_p10;
        v_stack_p10 = (unsigned int)((unsigned int)(a1));
        v_stack_m10 = result;
        result = ExNotifyWithProcessing(a1, a2, a3, a4);
        a2 = (unsigned int)((unsigned int)(a1));
        a1 = v_rip - 12354044;
        result = PnpDiagnosticTraceElamStatus(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PnpNotifyEarlyLaunchStatusUpdate(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;

    local_rsp = (local_rsp) - (64);
    if ((*(uint64_t *)(v_rip + 0x41958B)) != 0) {
        a2 = Arg1;
        Arg1 = v_rip - 12354560;
        result = PnpDiagnosticTraceElamStatus(Arg1, a2, a3, a4);
        Arg1 = *(uint64_t *)(v_rip + 0x419574);
        result = v_rip + 277629;
        a4 = v_stack_m28;
        a3 = v_stack_p18;
        v_stack_m28 = result;
        a2 = 0;
        result = v_stack_p10;
        v_stack_p10 = (uint32_t)((uint32_t)(Arg1));
        v_stack_m10 = result;
        result = ExNotifyWithProcessing(Arg1, a2, a3, a4);
        a2 = (uint32_t)((uint32_t)(Arg1));
        Arg1 = v_rip - 12354044;
        result = PnpDiagnosticTraceElamStatus(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00BEF120&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BEF120[BB_00BEF120]
  bb_00BEF137[BB_00BEF137]
  bb_00BEF191[BB_00BEF191]
  bb_00BEF197[BB_00BEF197]
  bb_00BEF120 -->|branch| bb_00BEF191
  bb_00BEF120 -->|fallthrough| bb_00BEF137
  bb_00BEF137 -->|flow| bb_00BEF191
```
