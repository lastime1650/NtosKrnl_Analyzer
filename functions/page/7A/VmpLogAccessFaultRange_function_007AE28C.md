# VmpLogAccessFaultRange

- RVA: `0x007AE28C`–`0x007AE422` (길이 `406` bytes)
- VA: `0x00000001407AE28C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2F58`
- 디코드: `96`개 명령, `406/406` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x007AE2DA` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x007AE2F7` → [PsGetProcessId](../../text/43/PsGetProcessId_function_0043D910.md) (function, `0x0043D910`)
- `0x007AE3F3` → [tlgWriteEx_EtwWriteEx](../../text/4A/tlgWriteEx_EtwWriteEx_function_004AA348.md) (function, `0x004AA348`)
- `0x007AE3FF` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [VmAccessFault](../A1/VmAccessFault_function_00A18BF0.md) at `0x00A18F0C`

### Static image references
- `0x007AE2AB` → RVA `0x00E0A740` (`.data`; read)
- `0x007AE2B9` → RVA `0x00F02458` (`.data`; read)
- `0x007AE3D0` → RVA `0x00053B53` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x007AE2DA` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x007AE2F7` → [PsGetProcessId](../../text/43/PsGetProcessId_function_0043D910.md) (`PAGE` → `.text`)
  - `0x007AE3F3` → [tlgWriteEx_EtwWriteEx](../../text/4A/tlgWriteEx_EtwWriteEx_function_004AA348.md) (`PAGE` → `.text`)
  - `0x007AE3FF` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007AE28C  48 8B C4                        mov rax, rsp
007AE28F  48 89 58 08                     mov qword ptr [rax + 8], rbx
007AE293  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
007AE297  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
007AE29B  4C 89 70 20                     mov qword ptr [rax + 0x20], r14
007AE29F  55                              push rbp
007AE2A0  48 8D 68 B8                     lea rbp, [rax - 0x48]
007AE2A4  48 81 EC 40 01 00 00            sub rsp, 0x140
007AE2AB  48 8B 05 8E C4 65 00            mov rax, qword ptr [rip + 0x65c48e]
007AE2B2  48 33 C4                        xor rax, rsp
007AE2B5  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
007AE2B9  48 8B 1D 98 41 75 00            mov rbx, qword ptr [rip + 0x754198]
007AE2C0  49 8B F9                        mov rdi, r9
007AE2C3  49 8B F0                        mov rsi, r8
007AE2C6  4C 8B F2                        mov r14, rdx
007AE2C9  83 3B 05                        cmp dword ptr [rbx], 5
007AE2CC  0F 86 26 01 00 00               jbe 0x1407ae3f8
007AE2D2  BA 10 00 00 00                  mov edx, 0x10
007AE2D7  48 8B CB                        mov rcx, rbx
007AE2DA  E8 C1 07 C8 FF                  call 0x14042eaa0
007AE2DF  84 C0                           test al, al
007AE2E1  0F 84 11 01 00 00               je 0x1407ae3f8
007AE2E7  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
007AE2F0  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
007AE2F7  E8 14 F6 C8 FF                  call 0x14043d910
007AE2FC  83 65 AC 00                     and dword ptr [rbp - 0x54], 0
007AE300  B9 04 00 00 00                  mov ecx, 4
007AE305  83 65 BC 00                     and dword ptr [rbp - 0x44], 0
007AE309  45 33 C9                        xor r9d, r9d
007AE30C  83 65 CC 00                     and dword ptr [rbp - 0x34], 0
007AE310  83 65 DC 00                     and dword ptr [rbp - 0x24], 0
007AE314  83 65 EC 00                     and dword ptr [rbp - 0x14], 0
007AE318  8D 51 04                        lea edx, [rcx + 4]
007AE31B  83 65 FC 00                     and dword ptr [rbp - 4], 0
007AE31F  83 65 0C 00                     and dword ptr [rbp + 0xc], 0
007AE323  83 65 1C 00                     and dword ptr [rbp + 0x1c], 0
007AE327  83 65 2C 00                     and dword ptr [rbp + 0x2c], 0
007AE32B  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
007AE32F  48 8D 44 24 40                  lea rax, [rsp + 0x40]
007AE334  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
007AE338  48 8D 44 24 58                  lea rax, [rsp + 0x58]
007AE33D  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
007AE341  48 8D 44 24 60                  lea rax, [rsp + 0x60]
007AE346  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
007AE34A  48 8D 44 24 68                  lea rax, [rsp + 0x68]
007AE34F  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
007AE353  8B 45 70                        mov eax, dword ptr [rbp + 0x70]
007AE356  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
007AE35A  48 8D 44 24 44                  lea rax, [rsp + 0x44]
007AE35F  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
007AE363  8B 45 78                        mov eax, dword ptr [rbp + 0x78]
007AE366  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
007AE36A  48 8D 44 24 48                  lea rax, [rsp + 0x48]
007AE36F  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
007AE373  8B 85 80 00 00 00               mov eax, dword ptr [rbp + 0x80]
007AE379  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
007AE37D  48 8D 44 24 4C                  lea rax, [rsp + 0x4c]
007AE382  48 89 45 00                     mov qword ptr [rbp], rax
007AE386  8B 85 88 00 00 00               mov eax, dword ptr [rbp + 0x88]
007AE38C  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
007AE390  48 8D 44 24 50                  lea rax, [rsp + 0x50]
007AE395  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
007AE399  48 8B 85 90 00 00 00            mov rax, qword ptr [rbp + 0x90]
007AE3A0  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
007AE3A5  48 8D 44 24 70                  lea rax, [rsp + 0x70]
007AE3AA  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
007AE3AE  48 8D 45 80                     lea rax, [rbp - 0x80]
007AE3B2  89 4D A8                        mov dword ptr [rbp - 0x58], ecx
007AE3B5  89 55 B8                        mov dword ptr [rbp - 0x48], edx
007AE3B8  89 55 C8                        mov dword ptr [rbp - 0x38], edx
007AE3BB  89 55 D8                        mov dword ptr [rbp - 0x28], edx
007AE3BE  89 4D E8                        mov dword ptr [rbp - 0x18], ecx
007AE3C1  89 4D F8                        mov dword ptr [rbp - 8], ecx
007AE3C4  89 4D 08                        mov dword ptr [rbp + 8], ecx
007AE3C7  89 4D 18                        mov dword ptr [rbp + 0x18], ecx
007AE3CA  48 8B CB                        mov rcx, rbx
007AE3CD  89 55 28                        mov dword ptr [rbp + 0x28], edx
007AE3D0  48 8D 15 7C 57 8A FF            lea rdx, [rip - 0x75a884]
007AE3D7  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
007AE3DC  C7 44 24 30 0B 00 00 00         mov dword ptr [rsp + 0x30], 0xb
007AE3E4  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
007AE3E9  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
007AE3EE  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
007AE3F3  E8 50 BF CF FF                  call 0x1404aa348
007AE3F8  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
007AE3FC  48 33 CC                        xor rcx, rsp
007AE3FF  E8 3C E2 EF FF                  call 0x1406ac640
007AE404  4C 8D 9C 24 40 01 00 00         lea r11, [rsp + 0x140]
007AE40C  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
007AE410  49 8B 73 18                     mov rsi, qword ptr [r11 + 0x18]
007AE414  49 8B 7B 20                     mov rdi, qword ptr [r11 + 0x20]
007AE418  4D 8B 73 28                     mov r14, qword ptr [r11 + 0x28]
007AE41C  49 8B E3                        mov rsp, r11
007AE41F  5D                              pop rbp
007AE420  C3                              ret
007AE421  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VmpLogAccessFaultRange(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned int v_stack_m104;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF8;
    unsigned int v_stack_mFC;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 32) = v_r14;
    v_rsp = (v_rsp) - (320);
    result = (*(unsigned __int64 *)(v_rip + 6669454)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 72 + 48) = result;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7684504))) <= 5) goto loc_007AE3F8;
    result = tlgKeywordOn(*(unsigned __int64 *)(v_rip + 7684504), 16, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = *(unsigned __int64 *)(a1 + 184);
        result = PsGetProcessId(a1, 16, a3, a4);
        a1 = 4;
        a4 = 0;
        a2 = a1 + 4;
        v_stack_m108 = (unsigned int)(result);
        result = v_stack_m108;
        *(unsigned __int64 *)(v_rsp - 72 - 96) = result;
        result = v_stack_mF0;
        *(unsigned __int64 *)(v_rsp - 72 - 80) = result;
        result = v_stack_mE8;
        *(unsigned __int64 *)(v_rsp - 72 - 64) = result;
        result = v_stack_mE0;
        *(unsigned __int64 *)(v_rsp - 72 - 48) = result;
        result = *(unsigned int *)(v_rsp - 72 + 112);
        v_stack_m104 = (unsigned int)(result);
        result = v_stack_m104;
        *(unsigned __int64 *)(v_rsp - 72 - 32) = result;
        result = *(unsigned int *)(v_rsp - 72 + 120);
        v_stack_m100 = (unsigned int)(result);
        result = v_stack_m100;
        *(unsigned __int64 *)(v_rsp - 72 - 16) = result;
        result = *(unsigned int *)(v_rsp - 72 + 128);
        v_stack_mFC = (unsigned int)(result);
        result = v_stack_mFC;
        *(unsigned __int64 *)(v_rsp - 72) = result;
        result = *(unsigned int *)(v_rsp - 72 + 136);
        v_stack_mF8 = (unsigned int)(result);
        result = v_stack_mF8;
        *(unsigned __int64 *)(v_rsp - 72 + 16) = result;
        result = *(unsigned __int64 *)(v_rsp - 72 + 144);
        v_stack_mD8 = result;
        result = v_stack_mD8;
        *(unsigned __int64 *)(v_rsp - 72 + 32) = result;
        result = v_rsp - 72 - 128;
        *(unsigned int *)(v_rsp - 72 - 88) = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 72 - 72) = (unsigned int)(a2);
        *(unsigned int *)(v_rsp - 72 - 56) = (unsigned int)(a2);
        *(unsigned int *)(v_rsp - 72 - 40) = (unsigned int)(a2);
        *(unsigned int *)(v_rsp - 72 - 24) = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 72 - 8) = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 72 + 8) = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 72 + 24) = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(v_rip + 7684504);
        *(unsigned int *)(v_rsp - 72 + 40) = (unsigned int)(a2);
        a2 = v_rip - 7710852;
        v_stack_m110 = result;
        v_stack_m118 = 11;
        v_stack_mF0 = a2;
        v_stack_mE8 = a3;
        v_stack_mE0 = 0;
        result = tlgWriteEx_EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 72 + 48)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VmpLogAccessFaultRange(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint32_t v_stack_m104;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint32_t v_stack_m118;
    uint64_t v_stack_m8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF8;
    uint32_t v_stack_mFC;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    *(uint64_t *)(local_rsp + 0x20) = local_r14;
    local_rsp = (local_rsp) - (320);
    result = (*(uint64_t *)(v_rip + 0x65C48E)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x48 + 0x30) = result;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x754198))) <= 5) goto loc_007AE3F8;
    result = tlgKeywordOn(*(uint64_t *)(v_rip + 0x754198), 16, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = *(uint64_t *)(Arg1 + 0xB8);
        result = PsGetProcessId(Arg1, 16, Arg3, Arg4);
        Arg1 = 4;
        Arg4 = 0;
        Arg2 = Arg1 + 4;
        v_stack_m108 = (uint32_t)(result);
        result = v_stack_m108;
        *(uint64_t *)(local_rsp - 0x48 - 0x60) = result;
        result = v_stack_mF0;
        *(uint64_t *)(local_rsp - 0x48 - 0x50) = result;
        result = v_stack_mE8;
        *(uint64_t *)(local_rsp - 0x48 - 0x40) = result;
        result = v_stack_mE0;
        *(uint64_t *)(local_rsp - 0x48 - 0x30) = result;
        result = *(uint32_t *)(local_rsp - 0x48 + 0x70);
        v_stack_m104 = (uint32_t)(result);
        result = v_stack_m104;
        *(uint64_t *)(local_rsp - 0x48 - 0x20) = result;
        result = *(uint32_t *)(local_rsp - 0x48 + 0x78);
        v_stack_m100 = (uint32_t)(result);
        result = v_stack_m100;
        *(uint64_t *)(local_rsp - 0x48 - 0x10) = result;
        result = *(uint32_t *)(local_rsp - 0x48 + 0x80);
        v_stack_mFC = (uint32_t)(result);
        result = v_stack_mFC;
        *(uint64_t *)(local_rsp - 0x48) = result;
        result = *(uint32_t *)(local_rsp - 0x48 + 0x88);
        v_stack_mF8 = (uint32_t)(result);
        result = v_stack_mF8;
        *(uint64_t *)(local_rsp - 0x48 + 0x10) = result;
        result = *(uint64_t *)(local_rsp - 0x48 + 0x90);
        v_stack_mD8 = result;
        result = v_stack_mD8;
        *(uint64_t *)(local_rsp - 0x48 + 0x20) = result;
        result = local_rsp - 72 - 128;
        *(uint32_t *)(local_rsp - 0x48 - 0x58) = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0x48 - 0x48) = (uint32_t)(Arg2);
        *(uint32_t *)(local_rsp - 0x48 - 0x38) = (uint32_t)(Arg2);
        *(uint32_t *)(local_rsp - 0x48 - 0x28) = (uint32_t)(Arg2);
        *(uint32_t *)(local_rsp - 0x48 - 0x18) = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0x48 - 0x8) = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0x48 + 0x8) = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0x48 + 0x18) = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(v_rip + 0x754198);
        *(uint32_t *)(local_rsp - 0x48 + 0x28) = (uint32_t)(Arg2);
        Arg2 = v_rip - 7710852;
        v_stack_m110 = result;
        v_stack_m118 = 11;
        v_stack_mF0 = Arg2;
        v_stack_mE8 = Arg3;
        v_stack_mE0 = 0;
        result = tlgWriteEx_EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x48 + 0x30)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007AE28C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007AE28C[BB_007AE28C]
  bb_007AE2D2[BB_007AE2D2]
  bb_007AE2E7[BB_007AE2E7]
  bb_007AE3F8[BB_007AE3F8]
  bb_007AE421[BB_007AE421]
  bb_007AE28C -->|branch| bb_007AE3F8
  bb_007AE28C -->|fallthrough| bb_007AE2D2
  bb_007AE2D2 -->|branch| bb_007AE3F8
  bb_007AE2D2 -->|fallthrough| bb_007AE2E7
  bb_007AE2E7 -->|flow| bb_007AE3F8
```
