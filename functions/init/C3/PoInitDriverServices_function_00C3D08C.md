# PoInitDriverServices

- RVA: `0x00C3D08C`–`0x00C3D23B` (길이 `431` bytes)
- VA: `0x0000000140C3D08C`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CBD30`
- 디코드: `89`개 명령, `431/431` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **14**

### Outgoing calls
- `0x00C3D0D4` → [IoRegisterPlugPlayNotification](../../page/95/IoRegisterPlugPlayNotification_function_009535A0.md) (function, `0x009535A0`)
- `0x00C3D103` → [IoRegisterPlugPlayNotification](../../page/95/IoRegisterPlugPlayNotification_function_009535A0.md) (function, `0x009535A0`)
- `0x00C3D136` → [IoRegisterPlugPlayNotification](../../page/95/IoRegisterPlugPlayNotification_function_009535A0.md) (function, `0x009535A0`)
- `0x00C3D169` → [IoRegisterPlugPlayNotification](../../page/95/IoRegisterPlugPlayNotification_function_009535A0.md) (function, `0x009535A0`)
- `0x00C3D19C` → [IoRegisterPlugPlayNotification](../../page/95/IoRegisterPlugPlayNotification_function_009535A0.md) (function, `0x009535A0`)
- `0x00C3D1CF` → [IoRegisterPlugPlayNotification](../../page/95/IoRegisterPlugPlayNotification_function_009535A0.md) (function, `0x009535A0`)
- `0x00C3D207` → [IoRegisterPlugPlayNotification](../../page/95/IoRegisterPlugPlayNotification_function_009535A0.md) (function, `0x009535A0`)

### Direct callers
- [IoInitSystemPreDrivers](../C2/IoInitSystemPreDrivers_function_00C2AC3C.md) at `0x00C2B4CF`

### Static image references
- `0x00C3D09F` → RVA `0x00F8C440` (`.data`; read)
- `0x00C3D0AF` → RVA `0x00765FF0` (`PopNotifyPolicyDevice`; read)
- `0x00C3D0BA` → RVA `0x000236D0` (`.rdata`; read)
- `0x00C3D0E9` → RVA `0x000236B0` (`.rdata`; read)
- `0x00C3D118` → RVA `0x000236A0` (`.rdata`; read)
- `0x00C3D14B` → RVA `0x00023660` (`.rdata`; read)
- `0x00C3D17E` → RVA `0x000236C0` (`.rdata`; read)
- `0x00C3D1B1` → RVA `0x00023680` (`.rdata`; read)
- `0x00C3D1E4` → RVA `0x0002AEC0` (`.rdata`; read)
- `0x00C3D1F9` → RVA `0x0076FEF0` (`PopCadHpmiPnpNotification`; read)
- `0x00C3D20C` → RVA `0x00F07C18` (`.data`; read/write)
- `0x00C3D214` → RVA `0x0076FFC0` (`PopCadTriggerDriverLoad`; read)
- `0x00C3D21B` → RVA `0x00F07C00` (`.data`; read/write)
- `0x00C3D22D` → RVA `0x00F07C10` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x00C3D0D4` → [IoRegisterPlugPlayNotification](../../page/95/IoRegisterPlugPlayNotification_function_009535A0.md) (`INIT` → `PAGE`)
  - `0x00C3D103` → [IoRegisterPlugPlayNotification](../../page/95/IoRegisterPlugPlayNotification_function_009535A0.md) (`INIT` → `PAGE`)
  - `0x00C3D136` → [IoRegisterPlugPlayNotification](../../page/95/IoRegisterPlugPlayNotification_function_009535A0.md) (`INIT` → `PAGE`)
  - `0x00C3D169` → [IoRegisterPlugPlayNotification](../../page/95/IoRegisterPlugPlayNotification_function_009535A0.md) (`INIT` → `PAGE`)
  - `0x00C3D19C` → [IoRegisterPlugPlayNotification](../../page/95/IoRegisterPlugPlayNotification_function_009535A0.md) (`INIT` → `PAGE`)
  - `0x00C3D1CF` → [IoRegisterPlugPlayNotification](../../page/95/IoRegisterPlugPlayNotification_function_009535A0.md) (`INIT` → `PAGE`)
  - `0x00C3D207` → [IoRegisterPlugPlayNotification](../../page/95/IoRegisterPlugPlayNotification_function_009535A0.md) (`INIT` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C3D08C  4C 8B DC                        mov r11, rsp
00C3D08F  49 89 5B 10                     mov qword ptr [r11 + 0x10], rbx
00C3D093  49 89 7B 18                     mov qword ptr [r11 + 0x18], rdi
00C3D097  55                              push rbp
00C3D098  48 8B EC                        mov rbp, rsp
00C3D09B  48 83 EC 40                     sub rsp, 0x40
00C3D09F  4C 8B 0D 9A F3 34 00            mov r9, qword ptr [rip + 0x34f39a]
00C3D0A6  48 8D 45 10                     lea rax, [rbp + 0x10]
00C3D0AA  48 83 65 10 00                  and qword ptr [rbp + 0x10], 0
00C3D0AF  48 8D 1D 3A 8F B2 FF            lea rbx, [rip - 0x4d70c6]
00C3D0B6  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
00C3D0BA  4C 8D 05 0F 66 3E FF            lea r8, [rip - 0xc199f1]
00C3D0C1  33 D2                           xor edx, edx
00C3D0C3  49 C7 43 E0 01 00 00 00         mov qword ptr [r11 - 0x20], 1
00C3D0CB  49 89 5B D8                     mov qword ptr [r11 - 0x28], rbx
00C3D0CF  8D 7A 02                        lea edi, [rdx + 2]
00C3D0D2  8B CF                           mov ecx, edi
00C3D0D4  E8 C7 64 D1 FF                  call 0x1409535a0
00C3D0D9  4C 8B 0D 60 F3 34 00            mov r9, qword ptr [rip + 0x34f360]
00C3D0E0  48 8D 45 10                     lea rax, [rbp + 0x10]
00C3D0E4  48 83 65 10 00                  and qword ptr [rbp + 0x10], 0
00C3D0E9  4C 8D 05 C0 65 3E FF            lea r8, [rip - 0xc19a40]
00C3D0F0  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00C3D0F5  33 D2                           xor edx, edx
00C3D0F7  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00C3D0FC  8B CF                           mov ecx, edi
00C3D0FE  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00C3D103  E8 98 64 D1 FF                  call 0x1409535a0
00C3D108  4C 8B 0D 31 F3 34 00            mov r9, qword ptr [rip + 0x34f331]
00C3D10F  48 8D 45 10                     lea rax, [rbp + 0x10]
00C3D113  48 83 65 10 00                  and qword ptr [rbp + 0x10], 0
00C3D118  4C 8D 05 81 65 3E FF            lea r8, [rip - 0xc19a7f]
00C3D11F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00C3D124  33 D2                           xor edx, edx
00C3D126  48 C7 44 24 28 03 00 00 00      mov qword ptr [rsp + 0x28], 3
00C3D12F  8B CF                           mov ecx, edi
00C3D131  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00C3D136  E8 65 64 D1 FF                  call 0x1409535a0
00C3D13B  4C 8B 0D FE F2 34 00            mov r9, qword ptr [rip + 0x34f2fe]
00C3D142  48 8D 45 10                     lea rax, [rbp + 0x10]
00C3D146  48 83 65 10 00                  and qword ptr [rbp + 0x10], 0
00C3D14B  4C 8D 05 0E 65 3E FF            lea r8, [rip - 0xc19af2]
00C3D152  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00C3D157  33 D2                           xor edx, edx
00C3D159  48 C7 44 24 28 08 00 00 00      mov qword ptr [rsp + 0x28], 8
00C3D162  8B CF                           mov ecx, edi
00C3D164  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00C3D169  E8 32 64 D1 FF                  call 0x1409535a0
00C3D16E  4C 8B 0D CB F2 34 00            mov r9, qword ptr [rip + 0x34f2cb]
00C3D175  48 8D 45 10                     lea rax, [rbp + 0x10]
00C3D179  48 83 65 10 00                  and qword ptr [rbp + 0x10], 0
00C3D17E  4C 8D 05 3B 65 3E FF            lea r8, [rip - 0xc19ac5]
00C3D185  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00C3D18A  33 D2                           xor edx, edx
00C3D18C  48 C7 44 24 28 09 00 00 00      mov qword ptr [rsp + 0x28], 9
00C3D195  8B CF                           mov ecx, edi
00C3D197  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00C3D19C  E8 FF 63 D1 FF                  call 0x1409535a0
00C3D1A1  4C 8B 0D 98 F2 34 00            mov r9, qword ptr [rip + 0x34f298]
00C3D1A8  48 8D 45 10                     lea rax, [rbp + 0x10]
00C3D1AC  48 83 65 10 00                  and qword ptr [rbp + 0x10], 0
00C3D1B1  4C 8D 05 C8 64 3E FF            lea r8, [rip - 0xc19b38]
00C3D1B8  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00C3D1BD  33 D2                           xor edx, edx
00C3D1BF  48 C7 44 24 28 10 00 00 00      mov qword ptr [rsp + 0x28], 0x10
00C3D1C8  8B CF                           mov ecx, edi
00C3D1CA  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00C3D1CF  E8 CC 63 D1 FF                  call 0x1409535a0
00C3D1D4  4C 8B 0D 65 F2 34 00            mov r9, qword ptr [rip + 0x34f265]
00C3D1DB  48 8D 45 10                     lea rax, [rbp + 0x10]
00C3D1DF  48 83 65 10 00                  and qword ptr [rbp + 0x10], 0
00C3D1E4  4C 8D 05 D5 DC 3E FF            lea r8, [rip - 0xc1232b]
00C3D1EB  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00C3D1F0  8D 57 FF                        lea edx, [rdi - 1]
00C3D1F3  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00C3D1F9  48 8D 05 F0 2C B3 FF            lea rax, [rip - 0x4cd310]
00C3D200  8B CF                           mov ecx, edi
00C3D202  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C3D207  E8 94 63 D1 FF                  call 0x1409535a0
00C3D20C  48 83 25 04 AA 2C 00 00         and qword ptr [rip + 0x2caa04], 0
00C3D214  48 8D 05 A5 2D B3 FF            lea rax, [rip - 0x4cd25b]
00C3D21B  48 83 25 DD A9 2C 00 00         and qword ptr [rip + 0x2ca9dd], 0
00C3D223  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
00C3D228  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
00C3D22D  48 89 05 DC A9 2C 00            mov qword ptr [rip + 0x2ca9dc], rax
00C3D234  48 83 C4 40                     add rsp, 0x40
00C3D238  5D                              pop rbp
00C3D239  C3                              ret
00C3D23A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PoInitDriverServices(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 24) = v_stack_p8;
    a2 = 0;
    *(unsigned __int64 *)(v_rsp - 32) = 1;
    *(unsigned __int64 *)(v_rsp - 40) = v_rip - 5075142;
    result = IoRegisterPlugPlayNotification((unsigned int)((unsigned int)(a2 + 2)), a2, v_rip - 12687857, *(unsigned __int64 *)(v_rip + 3470234));
    v_stack_m18 = v_stack_p8;
    a2 = 0;
    v_stack_m20 = a2 + 2;
    v_stack_m28 = v_rip - 5075142;
    result = IoRegisterPlugPlayNotification((unsigned int)((unsigned int)(a2 + 2)), a2, v_rip - 12687936, *(unsigned __int64 *)(v_rip + 3470176));
    v_stack_m18 = v_stack_p8;
    a2 = 0;
    v_stack_m20 = 3;
    v_stack_m28 = v_rip - 5075142;
    result = IoRegisterPlugPlayNotification((unsigned int)((unsigned int)(a2 + 2)), a2, v_rip - 12687999, *(unsigned __int64 *)(v_rip + 3470129));
    v_stack_m18 = v_stack_p8;
    a2 = 0;
    v_stack_m20 = 8;
    v_stack_m28 = v_rip - 5075142;
    result = IoRegisterPlugPlayNotification((unsigned int)((unsigned int)(a2 + 2)), a2, v_rip - 12688114, *(unsigned __int64 *)(v_rip + 3470078));
    v_stack_m18 = v_stack_p8;
    a2 = 0;
    v_stack_m20 = 9;
    v_stack_m28 = v_rip - 5075142;
    result = IoRegisterPlugPlayNotification((unsigned int)((unsigned int)(a2 + 2)), a2, v_rip - 12688069, *(unsigned __int64 *)(v_rip + 3470027));
    v_stack_m18 = v_stack_p8;
    a2 = 0;
    v_stack_m20 = 16;
    v_stack_m28 = v_rip - 5075142;
    result = IoRegisterPlugPlayNotification((unsigned int)((unsigned int)(a2 + 2)), a2, v_rip - 12688184, *(unsigned __int64 *)(v_rip + 3469976));
    v_stack_m18 = v_stack_p8;
    v_stack_m28 = v_rip - 5034768;
    result = IoRegisterPlugPlayNotification((unsigned int)((unsigned int)(a2 + 2)), a2 + 2 - 1, v_rip - 12657451, *(unsigned __int64 *)(v_rip + 3469925));
    *(unsigned __int64 *)(v_rip + 2927068) = v_rip - 5034587;
    v_rsp = (v_rsp) + (64);
    return v_rip - 5034587;
}
```

## 5. (Beta) C Style

```c
int64_t PoInitDriverServices(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(local_rsp - 0x18) = v_stack_p8;
    Arg2 = 0;
    *(uint64_t *)(local_rsp - 0x20) = 1;
    *(uint64_t *)(local_rsp - 0x28) = v_rip - 5075142;
    result = IoRegisterPlugPlayNotification((uint32_t)((uint32_t)(Arg2 + 2)), Arg2, v_rip - 12687857, *(uint64_t *)(v_rip + 0x34F39A));
    v_stack_m18 = v_stack_p8;
    Arg2 = 0;
    v_stack_m20 = Arg2 + 2;
    v_stack_m28 = v_rip - 5075142;
    result = IoRegisterPlugPlayNotification((uint32_t)((uint32_t)(Arg2 + 2)), Arg2, v_rip - 12687936, *(uint64_t *)(v_rip + 0x34F360));
    v_stack_m18 = v_stack_p8;
    Arg2 = 0;
    v_stack_m20 = 3;
    v_stack_m28 = v_rip - 5075142;
    result = IoRegisterPlugPlayNotification((uint32_t)((uint32_t)(Arg2 + 2)), Arg2, v_rip - 12687999, *(uint64_t *)(v_rip + 0x34F331));
    v_stack_m18 = v_stack_p8;
    Arg2 = 0;
    v_stack_m20 = 8;
    v_stack_m28 = v_rip - 5075142;
    result = IoRegisterPlugPlayNotification((uint32_t)((uint32_t)(Arg2 + 2)), Arg2, v_rip - 12688114, *(uint64_t *)(v_rip + 0x34F2FE));
    v_stack_m18 = v_stack_p8;
    Arg2 = 0;
    v_stack_m20 = 9;
    v_stack_m28 = v_rip - 5075142;
    result = IoRegisterPlugPlayNotification((uint32_t)((uint32_t)(Arg2 + 2)), Arg2, v_rip - 12688069, *(uint64_t *)(v_rip + 0x34F2CB));
    v_stack_m18 = v_stack_p8;
    Arg2 = 0;
    v_stack_m20 = 16;
    v_stack_m28 = v_rip - 5075142;
    result = IoRegisterPlugPlayNotification((uint32_t)((uint32_t)(Arg2 + 2)), Arg2, v_rip - 12688184, *(uint64_t *)(v_rip + 0x34F298));
    v_stack_m18 = v_stack_p8;
    v_stack_m28 = v_rip - 5034768;
    result = IoRegisterPlugPlayNotification((uint32_t)((uint32_t)(Arg2 + 2)), Arg2 + 2 - 1, v_rip - 12657451, *(uint64_t *)(v_rip + 0x34F265));
    *(uint64_t *)(v_rip + 0x2CA9DC) = v_rip - 5034587;
    local_rsp = (local_rsp) + (64);
    return v_rip - 5034587;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C3D08C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C3D08C[BB_00C3D08C]
  bb_00C3D23A[BB_00C3D23A]
```
