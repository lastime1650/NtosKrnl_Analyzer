# PerfDiagInitialize

- RVA: `0x00C4D150`–`0x00C4D25D` (길이 `269` bytes)
- VA: `0x0000000140C4D150`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2F98`
- 디코드: `55`개 명령, `269/269` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **17**

### Outgoing calls
- `0x00C4D193` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (function, `0x00920960`)
- `0x00C4D1B0` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (function, `0x00920960`)
- `0x00C4D1CD` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (function, `0x00920960`)
- `0x00C4D1EA` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (function, `0x00920960`)
- `0x00C4D1FF` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (function, `0x00920960`)
- `0x00C4D23C` → [EtwWriteStartScenario](../../page/AB/EtwWriteStartScenario_function_00AB75B0.md) (function, `0x00AB75B0`)
- `0x00C4D245` → [EtwUnregister](../../page/A7/EtwUnregister_function_00A723D0.md) (function, `0x00A723D0`)
- `0x00C4D251` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [EtwpInitialize](EtwpInitialize_function_00C4DBCC.md) at `0x00C4DED2`

### Static image references
- `0x00C4D159` → RVA `0x00E0A740` (`.data`; read)
- `0x00C4D16C` → RVA `0x00EFFC80` (`.data`; read)
- `0x00C4D173` → RVA `0x00EFFCA0` (`.data`; read/write)
- `0x00C4D17B` → RVA `0x007AEE10` (`PerfDiagpBootSystemProxyCallback`; read)
- `0x00C4D182` → RVA `0x00EFFCA8` (`.data`; read/write)
- `0x00C4D189` → RVA `0x00E0EAF8` (`.data`; read)
- `0x00C4D198` → RVA `0x00EFFC88` (`.data`; read)
- `0x00C4D1A2` → RVA `0x00AA6C80` (`PerfDiagpBootUserProxyCallback`; read)
- `0x00C4D1A9` → RVA `0x00E0EAC8` (`.data`; read)
- `0x00C4D1B5` → RVA `0x00EFFC90` (`.data`; read)
- `0x00C4D1BF` → RVA `0x007AF0F0` (`PerfDiagpSecondaryLogonProxyCallback`; read)
- `0x00C4D1C6` → RVA `0x00E0EAD8` (`.data`; read)
- `0x00C4D1D2` → RVA `0x00EFFC98` (`.data`; read)
- `0x00C4D1DC` → RVA `0x007AF120` (`PerfDiagpShutdownProxyCallback`; read)
- `0x00C4D1E3` → RVA `0x00E0EAE8` (`.data`; read)
- `0x00C4D1F8` → RVA `0x000211F8` (`.rdata`; read)
- `0x00C4D216` → RVA `0x00022F20` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **8**
  - `0x00C4D193` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (`INIT` → `PAGE`)
  - `0x00C4D1B0` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (`INIT` → `PAGE`)
  - `0x00C4D1CD` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (`INIT` → `PAGE`)
  - `0x00C4D1EA` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (`INIT` → `PAGE`)
  - `0x00C4D1FF` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (`INIT` → `PAGE`)
  - `0x00C4D23C` → [EtwWriteStartScenario](../../page/AB/EtwWriteStartScenario_function_00AB75B0.md) (`INIT` → `PAGE`)
  - `0x00C4D245` → [EtwUnregister](../../page/A7/EtwUnregister_function_00A723D0.md) (`INIT` → `PAGE`)
  - `0x00C4D251` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C4D150  40 55                           push rbp
00C4D152  48 8B EC                        mov rbp, rsp
00C4D155  48 83 EC 50                     sub rsp, 0x50
00C4D159  48 8B 05 E0 D5 1B 00            mov rax, qword ptr [rip + 0x1bd5e0]
00C4D160  48 33 C4                        xor rax, rsp
00C4D163  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00C4D167  48 83 65 E0 00                  and qword ptr [rbp - 0x20], 0
00C4D16C  4C 8D 0D 0D 2B 2B 00            lea r9, [rip + 0x2b2b0d]
00C4D173  48 83 25 25 2B 2B 00 00         and qword ptr [rip + 0x2b2b25], 0
00C4D17B  48 8D 15 8E 1C B6 FF            lea rdx, [rip - 0x49e372]
00C4D182  83 25 1F 2B 2B 00 00            and dword ptr [rip + 0x2b2b1f], 0
00C4D189  48 8D 0D 68 19 1C 00            lea rcx, [rip + 0x1c1968]
00C4D190  45 33 C0                        xor r8d, r8d
00C4D193  E8 C8 37 CD FF                  call 0x140920960
00C4D198  4C 8D 0D E9 2A 2B 00            lea r9, [rip + 0x2b2ae9]
00C4D19F  45 33 C0                        xor r8d, r8d
00C4D1A2  48 8D 15 D7 9A E5 FF            lea rdx, [rip - 0x1a6529]
00C4D1A9  48 8D 0D 18 19 1C 00            lea rcx, [rip + 0x1c1918]
00C4D1B0  E8 AB 37 CD FF                  call 0x140920960
00C4D1B5  4C 8D 0D D4 2A 2B 00            lea r9, [rip + 0x2b2ad4]
00C4D1BC  45 33 C0                        xor r8d, r8d
00C4D1BF  48 8D 15 2A 1F B6 FF            lea rdx, [rip - 0x49e0d6]
00C4D1C6  48 8D 0D 0B 19 1C 00            lea rcx, [rip + 0x1c190b]
00C4D1CD  E8 8E 37 CD FF                  call 0x140920960
00C4D1D2  4C 8D 0D BF 2A 2B 00            lea r9, [rip + 0x2b2abf]
00C4D1D9  45 33 C0                        xor r8d, r8d
00C4D1DC  48 8D 15 3D 1F B6 FF            lea rdx, [rip - 0x49e0c3]
00C4D1E3  48 8D 0D FE 18 1C 00            lea rcx, [rip + 0x1c18fe]
00C4D1EA  E8 71 37 CD FF                  call 0x140920960
00C4D1EF  4C 8D 4D E0                     lea r9, [rbp - 0x20]
00C4D1F3  45 33 C0                        xor r8d, r8d
00C4D1F6  33 D2                           xor edx, edx
00C4D1F8  48 8D 0D F9 3F 3D FF            lea rcx, [rip - 0xc2c007]
00C4D1FF  E8 5C 37 CD FF                  call 0x140920960
00C4D204  85 C0                           test eax, eax
00C4D206  78 42                           js 0x140c4d24a
00C4D208  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00C4D20C  4C 8D 45 E8                     lea r8, [rbp - 0x18]
00C4D210  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00C4D216  48 8D 15 03 5D 3D FF            lea rdx, [rip - 0xc2a2fd]
00C4D21D  45 33 C9                        xor r9d, r9d
00C4D220  C7 45 E8 49 49 14 67            mov dword ptr [rbp - 0x18], 0x67144949
00C4D227  C7 45 EC 32 51 59 48            mov dword ptr [rbp - 0x14], 0x48595132
00C4D22E  C7 45 F0 80 36 A7 37            mov dword ptr [rbp - 0x10], 0x37a73680
00C4D235  C7 45 F4 B4 38 25 D8            mov dword ptr [rbp - 0xc], 0xd82538b4
00C4D23C  E8 6F A3 E6 FF                  call 0x140ab75b0
00C4D241  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00C4D245  E8 86 51 E2 FF                  call 0x140a723d0
00C4D24A  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
00C4D24E  48 33 CC                        xor rcx, rsp
00C4D251  E8 EA F3 A5 FF                  call 0x1406ac640
00C4D256  48 83 C4 50                     add rsp, 0x50
00C4D25A  5D                              pop rbp
00C4D25B  C3                              ret
00C4D25C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PerfDiagInitialize(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned int v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;

    v_rsp = (v_rsp) - (80);
    result = (*(unsigned __int64 *)(v_rip + 1824224)) ^ (v_rsp);
    v_stack_m10 = result;
    a3 = 0;
    result = EtwRegister(v_rip + 1841512, v_rip - 4842354, a3, v_rip + 2829069);
    a3 = 0;
    result = EtwRegister(v_rip + 1841432, v_rip - 1729833, a3, v_rip + 2829033);
    a3 = 0;
    result = EtwRegister(v_rip + 1841419, v_rip - 4841686, a3, v_rip + 2829012);
    a3 = 0;
    result = EtwRegister(v_rip + 1841406, v_rip - 4841667, a3, v_rip + 2828991);
    a3 = 0;
    a2 = 0;
    result = EtwRegister(v_rip - 12763143, a2, a3, v_stack_m28);
    if (!(sign_flag)) {
        a1 = v_stack_m28;
        a3 = v_stack_m20;
        a2 = v_rip - 12755709;
        a4 = 0;
        v_stack_m20 = 0x67144949ULL;
        v_stack_m1C = 0x48595132ULL;
        v_stack_m18 = 0x37A73680ULL;
        v_stack_m14 = 0xD82538B4ULL;
        result = EtwWriteStartScenario(a1, a2, a3, a4);
        a1 = v_stack_m28;
        result = EtwUnregister(a1, a2, a3, a4);
    }
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (80);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PerfDiagInitialize(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint32_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;

    local_rsp = (local_rsp) - (80);
    result = (*(uint64_t *)(v_rip + 0x1BD5E0)) ^ (local_rsp);
    v_stack_m10 = result;
    Arg3 = 0;
    result = EtwRegister(v_rip + 1841512, v_rip - 4842354, Arg3, v_rip + 2829069);
    Arg3 = 0;
    result = EtwRegister(v_rip + 1841432, v_rip - 1729833, Arg3, v_rip + 2829033);
    Arg3 = 0;
    result = EtwRegister(v_rip + 1841419, v_rip - 4841686, Arg3, v_rip + 2829012);
    Arg3 = 0;
    result = EtwRegister(v_rip + 1841406, v_rip - 4841667, Arg3, v_rip + 2828991);
    Arg3 = 0;
    Arg2 = 0;
    result = EtwRegister(v_rip - 12763143, Arg2, Arg3, v_stack_m28);
    if (!(sign_flag)) {
        Arg1 = v_stack_m28;
        Arg3 = v_stack_m20;
        Arg2 = v_rip - 12755709;
        a4 = 0;
        v_stack_m20 = 0x67144949ULL;
        v_stack_m1C = 0x48595132ULL;
        v_stack_m18 = 0x37A73680ULL;
        v_stack_m14 = 0xD82538B4ULL;
        result = EtwWriteStartScenario(Arg1, Arg2, Arg3, a4);
        Arg1 = v_stack_m28;
        result = EtwUnregister(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (80);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C4D150&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C4D150[BB_00C4D150]
  bb_00C4D208[BB_00C4D208]
  bb_00C4D24A[BB_00C4D24A]
  bb_00C4D25C[BB_00C4D25C]
  bb_00C4D150 -->|branch| bb_00C4D24A
  bb_00C4D150 -->|fallthrough| bb_00C4D208
  bb_00C4D208 -->|flow| bb_00C4D24A
```
