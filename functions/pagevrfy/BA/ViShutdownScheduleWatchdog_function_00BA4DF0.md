# ViShutdownScheduleWatchdog

- RVA: `0x00BA4DF0`–`0x00BA4E5D` (길이 `109` bytes)
- VA: `0x0000000140BA4DF0`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064C80`
- 디코드: `23`개 명령, `109/109` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00BA4E24` → [KeInitializeDpc](../../text/45/KeInitializeDpc_function_0045BBD0.md) (function, `0x0045BBD0`)
- `0x00BA4E30` → [KeInitializeTimer](../../text/45/KeInitializeTimer_function_0045B590.md) (function, `0x0045B590`)
- `0x00BA4E51` → [KiSetTimerEx](../../text/23/KiSetTimerEx_function_00232CB0.md) (function, `0x00232CB0`)

### Direct callers
- [VfShutdownScheduleWatchdog](../../text/61/VfShutdownScheduleWatchdog_function_00615F18.md) at `0x00615F26`
- [ViShutdownWatchdogExecuteDpc](ViShutdownWatchdogExecuteDpc_function_00BA4E70.md) at `0x00BA4EE2`

### Static image references
- `0x00BA4DF6` → RVA `0x00FFDC60` (`PAGEVRFD`; read)
- `0x00BA4E09` → RVA `0x00FFDC60` (`PAGEVRFD`; write)
- `0x00BA4E10` → RVA `0x00FFF280` (`PAGEVRFD`; read)
- `0x00BA4E1D` → RVA `0x00BA4E70` (`ViShutdownWatchdogExecuteDpc`; read)
- `0x00BA4E29` → RVA `0x00FFF2C0` (`PAGEVRFD`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00BA4E24` → [KeInitializeDpc](../../text/45/KeInitializeDpc_function_0045BBD0.md) (`PAGEVRFY` → `.text`)
  - `0x00BA4E30` → [KeInitializeTimer](../../text/45/KeInitializeTimer_function_0045B590.md) (`PAGEVRFY` → `.text`)
  - `0x00BA4E51` → [KiSetTimerEx](../../text/23/KiSetTimerEx_function_00232CB0.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BA4DF0  40 53                           push rbx
00BA4DF2  48 83 EC 30                     sub rsp, 0x30
00BA4DF6  48 83 3D 62 8E 45 00 00         cmp qword ptr [rip + 0x458e62], 0
00BA4DFE  75 10                           jne 0x140ba4e10
00BA4E00  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00BA4E09  48 89 05 50 8E 45 00            mov qword ptr [rip + 0x458e50], rax
00BA4E10  48 8D 1D 69 A4 45 00            lea rbx, [rip + 0x45a469]
00BA4E17  45 33 C0                        xor r8d, r8d
00BA4E1A  48 8B CB                        mov rcx, rbx
00BA4E1D  48 8D 15 4C 00 00 00            lea rdx, [rip + 0x4c]
00BA4E24  E8 A7 6D 8B FF                  call 0x14045bbd0
00BA4E29  48 8D 0D 90 A4 45 00            lea rcx, [rip + 0x45a490]
00BA4E30  E8 5B 67 8B FF                  call 0x14045b590
00BA4E35  48 BA 00 44 5F 9A FE FF FF FF   movabs rdx, 0xfffffffe9a5f4400
00BA4E3F  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00BA4E44  45 33 C9                        xor r9d, r9d
00BA4E47  48 8D 0D 72 A4 45 00            lea rcx, [rip + 0x45a472]
00BA4E4E  45 33 C0                        xor r8d, r8d
00BA4E51  E8 5A DE 68 FF                  call 0x140232cb0
00BA4E56  48 83 C4 30                     add rsp, 0x30
00BA4E5A  5B                              pop rbx
00BA4E5B  C3                              ret
00BA4E5C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViShutdownScheduleWatchdog(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (48);
    if ((*(unsigned __int64 *)(v_rip + 4558434)) == 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        *(unsigned __int64 *)(v_rip + 4558416) = result;
    }
    a3 = 0;
    result = KeInitializeDpc(v_rip + 4564073, v_rip + 76, a3, a4);
    result = KeInitializeTimer(v_rip + 4564112, v_rip + 76, a3, a4);
    v_stack_m18 = v_rip + 4564073;
    a4 = 0;
    a3 = 0;
    result = KiSetTimerEx(v_rip + 4564082, v_rip + 76, a3, a4);
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ViShutdownScheduleWatchdog(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (48);
    if ((*(uint64_t *)(v_rip + 0x458E62)) == 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        *(uint64_t *)(v_rip + 0x458E50) = result;
    }
    Arg3 = 0;
    result = KeInitializeDpc(v_rip + 4564073, v_rip + 76, Arg3, Arg4);
    result = KeInitializeTimer(v_rip + 4564112, v_rip + 76, Arg3, Arg4);
    v_stack_m18 = v_rip + 4564073;
    Arg4 = 0;
    Arg3 = 0;
    result = KiSetTimerEx(v_rip + 4564082, v_rip + 76, Arg3, Arg4);
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BA4DF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BA4DF0[BB_00BA4DF0]
  bb_00BA4E00[BB_00BA4E00]
  bb_00BA4E10[BB_00BA4E10]
  bb_00BA4E5C[BB_00BA4E5C]
  bb_00BA4DF0 -->|branch| bb_00BA4E10
  bb_00BA4DF0 -->|fallthrough| bb_00BA4E00
  bb_00BA4E00 -->|flow| bb_00BA4E10
```
