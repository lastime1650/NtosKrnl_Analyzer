# EtwTiLogMapExecView

- RVA: `0x00A573E0`–`0x00A57580` (길이 `416` bytes)
- VA: `0x0000000140A573E0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B165C`
- 디코드: `104`개 명령, `416/416` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00A5741E` → [EtwProviderEnabled](../../text/3B/EtwProviderEnabled_function_003BA250.md) (function, `0x003BA250`)
- `0x00A5746B` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00A57485` → [EtwpTiFillProcessIdentity](../../text/3B/EtwpTiFillProcessIdentity_function_003B8F30.md) (function, `0x003B8F30`)
- `0x00A574A4` → [EtwpTiFillThreadIdentity](../../text/47/EtwpTiFillThreadIdentity_function_00471C1C.md) (function, `0x00471C1C`)
- `0x00A574C3` → [EtwpTiFillProcessIdentity](../../text/3B/EtwpTiFillProcessIdentity_function_003B8F30.md) (function, `0x003B8F30`)
- `0x00A57560` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x00A5756C` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [MiMapViewOfSectionExCommon](../9A/MiMapViewOfSectionExCommon_function_009A1C60.md) at `0x009A1F23`

### Static image references
- `0x00A573FC` → RVA `0x00E0A740` (`.data`; read)
- `0x00A5740F` → RVA `0x00EFFA30` (`.data`; read)
- `0x00A5744A` → RVA `0x00001580` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x00A5741E` → [EtwProviderEnabled](../../text/3B/EtwProviderEnabled_function_003BA250.md) (`PAGE` → `.text`)
  - `0x00A5746B` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00A57485` → [EtwpTiFillProcessIdentity](../../text/3B/EtwpTiFillProcessIdentity_function_003B8F30.md) (`PAGE` → `.text`)
  - `0x00A574A4` → [EtwpTiFillThreadIdentity](../../text/47/EtwpTiFillThreadIdentity_function_00471C1C.md) (`PAGE` → `.text`)
  - `0x00A574C3` → [EtwpTiFillProcessIdentity](../../text/3B/EtwpTiFillProcessIdentity_function_003B8F30.md) (`PAGE` → `.text`)
  - `0x00A57560` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x00A5756C` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A573E0  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00A573E5  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00A573EA  55                              push rbp
00A573EB  53                              push rbx
00A573EC  56                              push rsi
00A573ED  57                              push rdi
00A573EE  41 57                           push r15
00A573F0  48 8D 6C 24 90                  lea rbp, [rsp - 0x70]
00A573F5  48 81 EC 70 01 00 00            sub rsp, 0x170
00A573FC  48 8B 05 3D 33 3B 00            mov rax, qword ptr [rip + 0x3b333d]
00A57403  48 33 C4                        xor rax, rsp
00A57406  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
00A5740A  8A DA                           mov bl, dl
00A5740C  48 8B F9                        mov rdi, rcx
00A5740F  48 8B 0D 1A 86 4A 00            mov rcx, qword ptr [rip + 0x4a861a]
00A57416  33 D2                           xor edx, edx
00A57418  41 B8 00 0F 00 00               mov r8d, 0xf00
00A5741E  E8 2D 2E 96 FF                  call 0x1403ba250
00A57423  84 C0                           test al, al
00A57425  0F 84 3A 01 00 00               je 0x140a57565
00A5742B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A57434  33 C9                           xor ecx, ecx
00A57436  48 8B B0 B8 00 00 00            mov rsi, qword ptr [rax + 0xb8]
00A5743D  44 8D 79 08                     lea r15d, [rcx + 8]
00A57441  48 3B F7                        cmp rsi, rdi
00A57444  41 0F 44 CF                     cmove ecx, r15d
00A57448  F6 DB                           neg bl
00A5744A  48 8D 1D 2F A1 5A FF            lea rbx, [rip - 0xa55ed1]
00A57451  48 1B C0                        sbb rax, rax
00A57454  48 F7 D0                        not rax
00A57457  83 E0 10                        and eax, 0x10
00A5745A  48 03 C8                        add rcx, rax
00A5745D  48 8B 1C 19                     mov rbx, qword ptr [rcx + rbx]
00A57461  48 8B 0D C8 85 4A 00            mov rcx, qword ptr [rip + 0x4a85c8]
00A57468  48 8B D3                        mov rdx, rbx
00A5746B  E8 E0 AF 93 FF                  call 0x140392450
00A57470  84 C0                           test al, al
00A57472  0F 84 ED 00 00 00               je 0x140a57565
00A57478  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
00A5747D  48 8B D6                        mov rdx, rsi
00A57480  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00A57485  E8 A6 1A 96 FF                  call 0x1403b8f30
00A5748A  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
00A57493  8B C8                           mov ecx, eax
00A57495  44 8B C8                        mov r9d, eax
00A57498  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00A5749D  48 C1 E1 04                     shl rcx, 4
00A574A1  48 03 C8                        add rcx, rax
00A574A4  E8 73 A7 A1 FF                  call 0x140471c1c
00A574A9  44 03 C8                        add r9d, eax
00A574AC  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
00A574B1  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00A574B6  41 8B C9                        mov ecx, r9d
00A574B9  48 C1 E1 04                     shl rcx, 4
00A574BD  48 8B D7                        mov rdx, rdi
00A574C0  48 03 C8                        add rcx, rax
00A574C3  E8 68 1A 96 FF                  call 0x1403b8f30
00A574C8  44 03 C8                        add r9d, eax
00A574CB  41 8D 57 FC                     lea edx, [r15 - 4]
00A574CF  41 8B C1                        mov eax, r9d
00A574D2  48 8D 8D B0 00 00 00            lea rcx, [rbp + 0xb0]
00A574D9  48 03 C0                        add rax, rax
00A574DC  41 FF C1                        inc r9d
00A574DF  45 33 C0                        xor r8d, r8d
00A574E2  83 64 C4 4C 00                  and dword ptr [rsp + rax*8 + 0x4c], 0
00A574E7  48 89 4C C4 40                  mov qword ptr [rsp + rax*8 + 0x40], rcx
00A574EC  48 8D 8D B8 00 00 00            lea rcx, [rbp + 0xb8]
00A574F3  44 89 7C C4 48                  mov dword ptr [rsp + rax*8 + 0x48], r15d
00A574F8  41 8B C1                        mov eax, r9d
00A574FB  41 FF C1                        inc r9d
00A574FE  48 03 C0                        add rax, rax
00A57501  83 64 C4 4C 00                  and dword ptr [rsp + rax*8 + 0x4c], 0
00A57506  48 89 4C C4 40                  mov qword ptr [rsp + rax*8 + 0x40], rcx
00A5750B  48 8D 8D C0 00 00 00            lea rcx, [rbp + 0xc0]
00A57512  44 89 7C C4 48                  mov dword ptr [rsp + rax*8 + 0x48], r15d
00A57517  41 8B C1                        mov eax, r9d
00A5751A  41 FF C1                        inc r9d
00A5751D  48 03 C0                        add rax, rax
00A57520  83 64 C4 4C 00                  and dword ptr [rsp + rax*8 + 0x4c], 0
00A57525  48 89 4C C4 40                  mov qword ptr [rsp + rax*8 + 0x40], rcx
00A5752A  48 8D 8D C8 00 00 00            lea rcx, [rbp + 0xc8]
00A57531  89 54 C4 48                     mov dword ptr [rsp + rax*8 + 0x48], edx
00A57535  41 8B C1                        mov eax, r9d
00A57538  48 03 C0                        add rax, rax
00A5753B  83 64 C4 4C 00                  and dword ptr [rsp + rax*8 + 0x4c], 0
00A57540  48 89 4C C4 40                  mov qword ptr [rsp + rax*8 + 0x40], rcx
00A57545  41 FF C1                        inc r9d
00A57548  48 8B 0D E1 84 4A 00            mov rcx, qword ptr [rip + 0x4a84e1]
00A5754F  89 54 C4 48                     mov dword ptr [rsp + rax*8 + 0x48], edx
00A57553  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00A57558  48 8B D3                        mov rdx, rbx
00A5755B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A57560  E8 BB 51 9C FF                  call 0x14041c720
00A57565  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
00A57569  48 33 CC                        xor rcx, rsp
00A5756C  E8 CF 50 C5 FF                  call 0x1406ac640
00A57571  48 81 C4 70 01 00 00            add rsp, 0x170
00A57578  41 5F                           pop r15
00A5757A  5F                              pop rdi
00A5757B  5E                              pop rsi
00A5757C  5B                              pop rbx
00A5757D  5D                              pop rbp
00A5757E  C3                              ret
00A5757F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwTiLogMapExecView(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (368);
    result = (*(unsigned __int64 *)(v_rip + 3879741)) ^ (v_rsp);
    v_stack_m38 = result;
    a2 = 0;
    result = EtwProviderEnabled(*(unsigned __int64 *)(v_rip + 4883994), a2, (unsigned int)(0xF00ULL), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00A57565;
    a1 = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) == 0) { a1 = (unsigned int)(a1 + 8); }
    v_rbx = (unsigned __int8)(-((unsigned __int8)(a2)));
    result = ~(*(unsigned __int64 *)(gs_base + (0 + 392)));
    result = (unsigned int)((result) & (16));
    a1 = (a1) + (result);
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 4883912), *(unsigned __int64 *)(a1 + v_rip - 10837713 * 1), (unsigned int)(0xF00ULL), a4);
    if ((unsigned __int8)(result) != 0) {
        a3 = v_stack_m168;
        a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
        a1 = v_stack_m158;
        result = EtwpTiFillProcessIdentity(a1, a2, a3, a4);
        a2 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = (unsigned int)(result);
        a4 = (unsigned int)(result);
        result = v_stack_m158;
        a1 = (a1) << (4);
        a1 = (a1) + (result);
        result = EtwpTiFillThreadIdentity(a1, a2, a3, a4);
        a4 = (unsigned int)((a4) + ((unsigned int)(result)));
        a3 = v_stack_m160;
        result = v_stack_m158;
        a1 = (unsigned int)(a4);
        a1 = (a1) << (4);
        a2 = a1;
        a1 = (a1) + (result);
        result = EtwpTiFillProcessIdentity(a1, a2, a3, a4);
        a4 = (unsigned int)((a4) + ((unsigned int)(result)));
        a2 = a1 + 8 - 4;
        result = (unsigned int)(a4);
        a1 = v_stack_p18;
        result = (result) + (result);
        a4 = (unsigned int)((a4) + 1);
        a3 = 0;
        *(unsigned __int64 *)(v_rsp + result * 8 + 64) = a1;
        a1 = v_stack_p20;
        *(unsigned int *)(v_rsp + result * 8 + 72) = (unsigned int)(a1 + 8);
        result = (unsigned int)(a4);
        a4 = (unsigned int)((a4) + 1);
        result = (result) + (result);
        *(unsigned __int64 *)(v_rsp + result * 8 + 64) = a1;
        a1 = a5;
        *(unsigned int *)(v_rsp + result * 8 + 72) = (unsigned int)(a1 + 8);
        result = (unsigned int)(a4);
        a4 = (unsigned int)((a4) + 1);
        result = (result) + (result);
        *(unsigned __int64 *)(v_rsp + result * 8 + 64) = a1;
        a1 = a6;
        *(unsigned int *)(v_rsp + result * 8 + 72) = a2;
        result = (unsigned int)(a4);
        result = (result) + (result);
        *(unsigned __int64 *)(v_rsp + result * 8 + 64) = a1;
        a4 = (unsigned int)((a4) + 1);
        a1 = *(unsigned __int64 *)(v_rip + 4883681);
        *(unsigned int *)(v_rsp + result * 8 + 72) = a2;
        result = v_stack_m158;
        a2 = *(unsigned __int64 *)(a1 + v_rip - 10837713 * 1);
        v_stack_m178 = result;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (368);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwTiLogMapExecView(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m178;
    uint64_t v_stack_m38;
    uint64_t v_stack_m98;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (368);
    result = (*(uint64_t *)(v_rip + 0x3B333D)) ^ (local_rsp);
    v_stack_m38 = result;
    Arg2 = 0;
    result = EtwProviderEnabled(*(uint64_t *)(v_rip + 0x4A861A), Arg2, (uint32_t)(0xF00ULL), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00A57565;
    Arg1 = 0;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) == 0) { Arg1 = (uint32_t)(Arg1 + 8); }
    local_rbx = (uint8_t)(-((uint8_t)(Arg2)));
    result = ~(*(uint64_t *)(gs_base + (0 + 0x188)));
    result = (uint32_t)((result) & (16));
    Arg1 = (Arg1) + (result);
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x4A85C8), *(uint64_t *)(Arg1 + v_rip - 0xA55ED1 * 1), (uint32_t)(0xF00ULL), Arg4);
    if ((uint8_t)(result) != 0) {
        Arg3 = v_stack_m168;
        Arg2 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
        Arg1 = v_stack_m158;
        result = EtwpTiFillProcessIdentity(Arg1, Arg2, Arg3, Arg4);
        Arg2 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = (uint32_t)(result);
        Arg4 = (uint32_t)(result);
        result = v_stack_m158;
        Arg1 = (Arg1) << (4);
        Arg1 = (Arg1) + (result);
        result = EtwpTiFillThreadIdentity(Arg1, Arg2, Arg3, Arg4);
        Arg4 = (uint32_t)((Arg4) + ((uint32_t)(result)));
        Arg3 = v_stack_m160;
        result = v_stack_m158;
        Arg1 = (uint32_t)(Arg4);
        Arg1 = (Arg1) << (4);
        Arg2 = Arg1;
        Arg1 = (Arg1) + (result);
        result = EtwpTiFillProcessIdentity(Arg1, Arg2, Arg3, Arg4);
        Arg4 = (uint32_t)((Arg4) + ((uint32_t)(result)));
        Arg2 = Arg1 + 8 - 4;
        result = (uint32_t)(Arg4);
        Arg1 = v_stack_p18;
        result = (result) + (result);
        Arg4 = (uint32_t)((Arg4) + 1);
        Arg3 = 0;
        *(uint64_t *)(local_rsp + result * 8 + 0x40) = Arg1;
        Arg1 = v_stack_p20;
        *(uint32_t *)(local_rsp + result * 8 + 0x48) = (uint32_t)(Arg1 + 8);
        result = (uint32_t)(Arg4);
        Arg4 = (uint32_t)((Arg4) + 1);
        result = (result) + (result);
        *(uint64_t *)(local_rsp + result * 8 + 0x40) = Arg1;
        Arg1 = Arg5;
        *(uint32_t *)(local_rsp + result * 8 + 0x48) = (uint32_t)(Arg1 + 8);
        result = (uint32_t)(Arg4);
        Arg4 = (uint32_t)((Arg4) + 1);
        result = (result) + (result);
        *(uint64_t *)(local_rsp + result * 8 + 0x40) = Arg1;
        Arg1 = Arg6;
        *(uint32_t *)(local_rsp + result * 8 + 0x48) = Arg2;
        result = (uint32_t)(Arg4);
        result = (result) + (result);
        *(uint64_t *)(local_rsp + result * 8 + 0x40) = Arg1;
        Arg4 = (uint32_t)((Arg4) + 1);
        Arg1 = *(uint64_t *)(v_rip + 0x4A84E1);
        *(uint32_t *)(local_rsp + result * 8 + 0x48) = Arg2;
        result = v_stack_m158;
        Arg2 = *(uint64_t *)(Arg1 + v_rip - 0xA55ED1 * 1);
        v_stack_m178 = result;
        result = EtwWrite(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (368);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A573E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A573E0[BB_00A573E0]
  bb_00A5742B[BB_00A5742B]
  bb_00A57478[BB_00A57478]
  bb_00A57565[BB_00A57565]
  bb_00A5757F[BB_00A5757F]
  bb_00A573E0 -->|branch| bb_00A57565
  bb_00A573E0 -->|fallthrough| bb_00A5742B
  bb_00A5742B -->|branch| bb_00A57565
  bb_00A5742B -->|fallthrough| bb_00A57478
  bb_00A57478 -->|flow| bb_00A57565
```
