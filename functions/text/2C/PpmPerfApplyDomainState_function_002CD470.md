# PpmPerfApplyDomainState

- RVA: `0x002CD470`–`0x002CDC77` (길이 `2,055` bytes)
- VA: `0x00000001402CD470`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006F52C`
- 디코드: `495`개 명령, `2,055/2,055` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x002CD502` → [PpmGetPerfPolicyClass](../42/PpmGetPerfPolicyClass_function_0042CF54.md) (function, `0x0042CF54`)
- `0x002CD572` → [KeIsSubsetAffinityEx](KeIsSubsetAffinityEx_function_002CDC80.md) (function, `0x002CDC80`)
- `0x002CD5F7` → [PpmPerfApplyCapsAndFloors](../46/PpmPerfApplyCapsAndFloors_function_0046CB1C.md) (function, `0x0046CB1C`)
- `0x002CD753` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x002CD953` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x002CDABC` → [KeIsSubsetAffinityEx](KeIsSubsetAffinityEx_function_002CDC80.md) (function, `0x002CDC80`)
- `0x002CDB35` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x002CDB4B` → [PpmEventDomainPerfStateChange](../47/PpmEventDomainPerfStateChange_function_0047B720.md) (function, `0x0047B720`)
- `0x002CDB55` → [PpmEventQosClassPerfSelection](../49/PpmEventQosClassPerfSelection_function_0049F7AC.md) (function, `0x0049F7AC`)

### Direct callers
- [PpmPerfApplyDomainStates](PpmPerfApplyDomainStates_function_002CD3B0.md) at `0x002CD44F`

### Static image references
- `0x002CD493` → RVA `0x00E0A740` (`.data`; read)
- `0x002CD4A1` → RVA `0x00E08380` (`.data`; read)
- `0x002CD4D6` → RVA `0x00F0CE0C` (`.data`; read)
- `0x002CD507` → RVA `0x00FC6CD4` (`ALMOSTRO`; read)
- `0x002CD56B` → RVA `0x00E0BED0` (`.data`; read)
- `0x002CD600` → RVA `0x00E0B3F0` (`.data`; read)
- `0x002CD7CE` → RVA `0x00FC6CC8` (`ALMOSTRO`; read)
- `0x002CD7F2` → RVA `0x00F0E0F0` (`.data`; read)
- `0x002CD8DD` → RVA `0x00F0B24C` (`.data`; read)
- `0x002CDA56` → RVA `0x00F0B248` (`.data`; read)
- `0x002CDAD9` → RVA `0x00FC6BA8` (`ALMOSTRO`; read)
- `0x002CDBD4` → RVA `0x00FC6AA6` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002CD470  48 8B C4                        mov rax, rsp
002CD473  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
002CD477  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
002CD47B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
002CD47F  55                              push rbp
002CD480  41 54                           push r12
002CD482  41 55                           push r13
002CD484  41 56                           push r14
002CD486  41 57                           push r15
002CD488  48 8D 68 A1                     lea rbp, [rax - 0x5f]
002CD48C  48 81 EC F0 00 00 00            sub rsp, 0xf0
002CD493  48 8B 05 A6 D2 B3 00            mov rax, qword ptr [rip + 0xb3d2a6]
002CD49A  48 33 C4                        xor rax, rsp
002CD49D  48 89 45 2F                     mov qword ptr [rbp + 0x2f], rax
002CD4A1  48 8B 15 D8 AE B3 00            mov rdx, qword ptr [rip + 0xb3aed8]
002CD4A8  33 C0                           xor eax, eax
002CD4AA  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
002CD4AE  45 33 DB                        xor r11d, r11d
002CD4B1  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
002CD4B8  48 8B D9                        mov rbx, rcx
002CD4BB  0F 57 C0                        xorps xmm0, xmm0
002CD4BE  44 89 5D BF                     mov dword ptr [rbp - 0x41], r11d
002CD4C2  4C 89 5D D7                     mov qword ptr [rbp - 0x29], r11
002CD4C6  4C 89 5D DF                     mov qword ptr [rbp - 0x21], r11
002CD4CA  48 8B 40 08                     mov rax, qword ptr [rax + 8]
002CD4CE  4C 8B 63 10                     mov r12, qword ptr [rbx + 0x10]
002CD4D2  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
002CD4D6  48 63 05 2F F9 C3 00            movsxd rax, dword ptr [rip + 0xc3f92f]
002CD4DD  48 69 C8 E8 01 00 00            imul rcx, rax, 0x1e8
002CD4E4  0F 11 45 F7                     movups xmmword ptr [rbp - 9], xmm0
002CD4E8  0F 11 45 07                     movups xmmword ptr [rbp + 7], xmm0
002CD4EC  48 8D 42 28                     lea rax, [rdx + 0x28]
002CD4F0  44 88 5D A8                     mov byte ptr [rbp - 0x58], r11b
002CD4F4  48 03 C1                        add rax, rcx
002CD4F7  49 8B CC                        mov rcx, r12
002CD4FA  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
002CD4FE  0F 11 45 17                     movups xmmword ptr [rbp + 0x17], xmm0
002CD502  E8 4D FA 15 00                  call 0x14042cf54
002CD507  44 39 1D C6 97 CF 00            cmp dword ptr [rip + 0xcf97c6], r11d
002CD50E  44 8B BB C4 01 00 00            mov r15d, dword ptr [rbx + 0x1c4]
002CD515  88 45 A9                        mov byte ptr [rbp - 0x57], al
002CD518  41 8D 43 64                     lea eax, [r11 + 0x64]
002CD51C  89 45 AB                        mov dword ptr [rbp - 0x55], eax
002CD51F  8B 83 CC 01 00 00               mov eax, dword ptr [rbx + 0x1cc]
002CD525  89 45 B3                        mov dword ptr [rbp - 0x4d], eax
002CD528  44 89 5D B7                     mov dword ptr [rbp - 0x49], r11d
002CD52C  44 88 5D A7                     mov byte ptr [rbp - 0x59], r11b
002CD530  44 89 5D BB                     mov dword ptr [rbp - 0x45], r11d
002CD534  44 89 7D AF                     mov dword ptr [rbp - 0x51], r15d
002CD538  0F 85 73 05 00 00               jne 0x1402cdab1
002CD53E  4C 8B 33                        mov r14, qword ptr [rbx]
002CD541  48 8B FB                        mov rdi, rbx
002CD544  41 BD 01 00 00 00               mov r13d, 1
002CD54A  49 3B FE                        cmp rdi, r14
002CD54D  0F 84 95 00 00 00               je 0x1402cd5e8
002CD553  8B B7 0C 02 00 00               mov esi, dword ptr [rdi + 0x20c]
002CD559  48 3B FB                        cmp rdi, rbx
002CD55C  74 6C                           je 0x1402cd5ca
002CD55E  44 39 9F 30 01 00 00            cmp dword ptr [rdi + 0x130], r11d
002CD565  75 2C                           jne 0x1402cd593
002CD567  48 8D 4F 18                     lea rcx, [rdi + 0x18]
002CD56B  48 8D 15 5E E9 B3 00            lea rdx, [rip + 0xb3e95e]
002CD572  E8 09 07 00 00                  call 0x1402cdc80
002CD577  45 33 DB                        xor r11d, r11d
002CD57A  85 C0                           test eax, eax
002CD57C  75 15                           jne 0x1402cd593
002CD57E  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
002CD582  48 8B 88 10 77 FF FF            mov rcx, qword ptr [rax - 0x88f0]
002CD589  49 39 8C 24 10 77 FF FF         cmp qword ptr [r12 - 0x88f0], rcx
002CD591  74 05                           je 0x1402cd598
002CD593  48 8B 3F                        mov rdi, qword ptr [rdi]
002CD596  EB B2                           jmp 0x1402cd54a
002CD598  44 8A 8B 2C 01 00 00            mov r9b, byte ptr [rbx + 0x12c]
002CD59F  44 8A 97 2C 01 00 00            mov r10b, byte ptr [rdi + 0x12c]
002CD5A6  45 3A CA                        cmp r9b, r10b
002CD5A9  0F 85 25 06 00 00               jne 0x1402cdbd4
002CD5AF  8A 87 2D 01 00 00               mov al, byte ptr [rdi + 0x12d]
002CD5B5  38 83 2D 01 00 00               cmp byte ptr [rbx + 0x12d], al
002CD5BB  0F 85 3C 06 00 00               jne 0x1402cdbfd
002CD5C1  45 3A CA                        cmp r9b, r10b
002CD5C4  0F 85 24 06 00 00               jne 0x1402cdbee
002CD5CA  3B 75 B7                        cmp esi, dword ptr [rbp - 0x49]
002CD5CD  0F 46 75 B7                     cmovbe esi, dword ptr [rbp - 0x49]
002CD5D1  8B C6                           mov eax, esi
002CD5D3  89 45 B7                        mov dword ptr [rbp - 0x49], eax
002CD5D6  44 38 9F 14 02 00 00            cmp byte ptr [rdi + 0x214], r11b
002CD5DD  74 B4                           je 0x1402cd593
002CD5DF  44 88 6D A7                     mov byte ptr [rbp - 0x59], r13b
002CD5E3  89 45 B7                        mov dword ptr [rbp - 0x49], eax
002CD5E6  EB AB                           jmp 0x1402cd593
002CD5E8  4C 8B CB                        mov r9, rbx
002CD5EB  4C 8D 45 AB                     lea r8, [rbp - 0x55]
002CD5EF  48 8D 55 B3                     lea rdx, [rbp - 0x4d]
002CD5F3  48 8D 4D AF                     lea rcx, [rbp - 0x51]
002CD5F7  E8 20 F5 19 00                  call 0x14046cb1c
002CD5FC  44 8B 4D AB                     mov r9d, dword ptr [rbp - 0x55]
002CD600  48 8D 15 E9 DD B3 00            lea rdx, [rip + 0xb3dde9]
002CD607  45 33 E4                        xor r12d, r12d
002CD60A  88 45 AA                        mov byte ptr [rbp - 0x56], al
002CD60D  44 8A F0                        mov r14b, al
002CD610  44 89 65 C3                     mov dword ptr [rbp - 0x3d], r12d
002CD614  41 8B C4                        mov eax, r12d
002CD617  45 8B DC                        mov r11d, r12d
002CD61A  45 8B D4                        mov r10d, r12d
002CD61D  4C 89 65 E7                     mov qword ptr [rbp - 0x19], r12
002CD621  42 8B 3C D2                     mov edi, dword ptr [rdx + r10*8]
002CD625  89 7D C7                        mov dword ptr [rbp - 0x39], edi
002CD628  44 39 A4 BB F8 02 00 00         cmp dword ptr [rbx + rdi*4 + 0x2f8], r12d
002CD630  0F 84 44 01 00 00               je 0x1402cd77a
002CD636  46 38 64 D2 04                  cmp byte ptr [rdx + r10*8 + 4], r12b
002CD63B  0F 84 9A 03 00 00               je 0x1402cd9db
002CD641  48 6B C8 38                     imul rcx, rax, 0x38
002CD645  48 03 CB                        add rcx, rbx
002CD648  48 81 C1 28 03 00 00            add rcx, 0x328
002CD64F  8B C7                           mov eax, edi
002CD651  48 6B D0 38                     imul rdx, rax, 0x38
002CD655  44 38 A3 BC 04 00 00            cmp byte ptr [rbx + 0x4bc], r12b
002CD65C  0F 85 85 00 00 00               jne 0x1402cd6e7
002CD662  44 8A 41 30                     mov r8b, byte ptr [rcx + 0x30]
002CD666  44 38 84 1A 58 03 00 00         cmp byte ptr [rdx + rbx + 0x358], r8b
002CD66E  75 77                           jne 0x1402cd6e7
002CD670  8B 41 18                        mov eax, dword ptr [rcx + 0x18]
002CD673  39 84 1A 40 03 00 00            cmp dword ptr [rdx + rbx + 0x340], eax
002CD67A  75 6B                           jne 0x1402cd6e7
002CD67C  8B 41 1C                        mov eax, dword ptr [rcx + 0x1c]
002CD67F  39 84 1A 44 03 00 00            cmp dword ptr [rdx + rbx + 0x344], eax
002CD686  75 5F                           jne 0x1402cd6e7
002CD688  8B 41 24                        mov eax, dword ptr [rcx + 0x24]
002CD68B  39 84 1A 4C 03 00 00            cmp dword ptr [rdx + rbx + 0x34c], eax
002CD692  75 53                           jne 0x1402cd6e7
002CD694  8B 41 28                        mov eax, dword ptr [rcx + 0x28]
002CD697  39 84 1A 50 03 00 00            cmp dword ptr [rdx + rbx + 0x350], eax
002CD69E  75 47                           jne 0x1402cd6e7
002CD6A0  48 8B 01                        mov rax, qword ptr [rcx]
002CD6A3  48 39 84 1A 28 03 00 00         cmp qword ptr [rdx + rbx + 0x328], rax
002CD6AB  75 3A                           jne 0x1402cd6e7
002CD6AD  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
002CD6B1  48 39 84 1A 30 03 00 00         cmp qword ptr [rdx + rbx + 0x330], rax
002CD6B9  75 2C                           jne 0x1402cd6e7
002CD6BB  44 3B 8B 10 02 00 00            cmp r9d, dword ptr [rbx + 0x210]
002CD6C2  75 23                           jne 0x1402cd6e7
002CD6C4  45 84 C0                        test r8b, r8b
002CD6C7  75 18                           jne 0x1402cd6e1
002CD6C9  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
002CD6CC  39 84 1A 48 03 00 00            cmp dword ptr [rdx + rbx + 0x348], eax
002CD6D3  75 12                           jne 0x1402cd6e7
002CD6D5  8B 41 10                        mov eax, dword ptr [rcx + 0x10]
002CD6D8  39 84 1A 38 03 00 00            cmp dword ptr [rdx + rbx + 0x338], eax
002CD6DF  75 06                           jne 0x1402cd6e7
002CD6E1  40 8A 75 A8                     mov sil, byte ptr [rbp - 0x58]
002CD6E5  EB 38                           jmp 0x1402cd71f
002CD6E7  0F 10 01                        movups xmm0, xmmword ptr [rcx]
002CD6EA  41 8A F5                        mov sil, r13b
002CD6ED  44 88 6D A8                     mov byte ptr [rbp - 0x58], r13b
002CD6F1  0F 11 84 1A 28 03 00 00         movups xmmword ptr [rdx + rbx + 0x328], xmm0
002CD6F9  0F 10 49 10                     movups xmm1, xmmword ptr [rcx + 0x10]
002CD6FD  0F 11 8C 1A 38 03 00 00         movups xmmword ptr [rdx + rbx + 0x338], xmm1
002CD705  0F 10 41 20                     movups xmm0, xmmword ptr [rcx + 0x20]
002CD709  0F 11 84 1A 48 03 00 00         movups xmmword ptr [rdx + rbx + 0x348], xmm0
002CD711  F2 0F 10 49 30                  movsd xmm1, qword ptr [rcx + 0x30]
002CD716  F2 0F 11 8C 1A 58 03 00 00      movsd qword ptr [rdx + rbx + 0x358], xmm1
002CD71F  45 03 DD                        add r11d, r13d
002CD722  8B C7                           mov eax, edi
002CD724  4D 03 D5                        add r10, r13
002CD727  44 89 5D C3                     mov dword ptr [rbp - 0x3d], r11d
002CD72B  4C 89 55 E7                     mov qword ptr [rbp - 0x19], r10
002CD72F  48 8D 15 BA DC B3 00            lea rdx, [rip + 0xb3dcba]
002CD736  41 83 FB 07                     cmp r11d, 7
002CD73A  0F 82 E1 FE FF FF               jb 0x1402cd621
002CD740  40 84 F6                        test sil, sil
002CD743  0F 85 C6 03 00 00               jne 0x1402cdb0f
002CD749  40 8A C6                        mov al, sil
002CD74C  48 8B 4D 2F                     mov rcx, qword ptr [rbp + 0x2f]
002CD750  48 33 CC                        xor rcx, rsp
002CD753  E8 E8 EE 3D 00                  call 0x1406ac640
002CD758  4C 8D 9C 24 F0 00 00 00         lea r11, [rsp + 0xf0]
002CD760  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
002CD764  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
002CD768  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
002CD76C  49 8B E3                        mov rsp, r11
002CD76F  41 5F                           pop r15
002CD771  41 5E                           pop r14
002CD773  41 5D                           pop r13
002CD775  41 5C                           pop r12
002CD777  5D                              pop rbp
002CD778  C3                              ret
002CD779  CC                              int3
002CD77A  4C 8B FF                        mov r15, rdi
002CD77D  49 C1 E7 05                     shl r15, 5
002CD781  41 8A 8C 1F 2D 02 00 00         mov cl, byte ptr [r15 + rbx + 0x22d]
002CD789  84 C9                           test cl, cl
002CD78B  0F 84 E8 02 00 00               je 0x1402cda79
002CD791  8B 83 CC 01 00 00               mov eax, dword ptr [rbx + 0x1cc]
002CD797  41 8B B4 1F 20 02 00 00         mov esi, dword ptr [r15 + rbx + 0x220]
002CD79F  84 C9                           test cl, cl
002CD7A1  45 8A 8C 1F 2E 02 00 00         mov r9b, byte ptr [r15 + rbx + 0x22e]
002CD7A9  45 8B C4                        mov r8d, r12d
002CD7AC  44 8B 55 AB                     mov r10d, dword ptr [rbp - 0x55]
002CD7B0  41 0F 95 C0                     setne r8b
002CD7B4  3B C6                           cmp eax, esi
002CD7B6  BA 64 00 00 00                  mov edx, 0x64
002CD7BB  0F 47 F0                        cmova esi, eax
002CD7BE  45 84 C9                        test r9b, r9b
002CD7C1  0F 85 1C 02 00 00               jne 0x1402cd9e3
002CD7C7  41 83 C8 08                     or r8d, 8
002CD7CB  41 8B C2                        mov eax, r10d
002CD7CE  44 39 25 F3 94 CF 00            cmp dword ptr [rip + 0xcf94f3], r12d
002CD7D5  0F 44 C2                        cmove eax, edx
002CD7D8  41 8B 8C 1F 18 02 00 00         mov ecx, dword ptr [r15 + rbx + 0x218]
002CD7E0  3B CA                           cmp ecx, edx
002CD7E2  0F 82 60 04 00 00               jb 0x1402cdc48
002CD7E8  41 8B 8C 1F 1C 02 00 00         mov ecx, dword ptr [r15 + rbx + 0x21c]
002CD7F0  3B C1                           cmp eax, ecx
002CD7F2  44 8A 1D F7 08 C4 00            mov r11b, byte ptr [rip + 0xc408f7]
002CD7F9  0F 42 C8                        cmovb ecx, eax
002CD7FC  45 84 DB                        test r11b, r11b
002CD7FF  0F 84 01 02 00 00               je 0x1402cda06
002CD805  3B D1                           cmp edx, ecx
002CD807  8B C1                           mov eax, ecx
002CD809  0F 42 C2                        cmovb eax, edx
002CD80C  3B C6                           cmp eax, esi
002CD80E  0F 87 82 03 00 00               ja 0x1402cdb96
002CD814  8B C6                           mov eax, esi
002CD816  41 3B C2                        cmp eax, r10d
002CD819  0F 82 65 02 00 00               jb 0x1402cda84
002CD81F  41 8B C2                        mov eax, r10d
002CD822  3B 45 B3                        cmp eax, dword ptr [rbp - 0x4d]
002CD825  0F 87 FA 01 00 00               ja 0x1402cda25
002CD82B  44 8B 65 B3                     mov r12d, dword ptr [rbp - 0x4d]
002CD82F  3B CE                           cmp ecx, esi
002CD831  8B C6                           mov eax, esi
002CD833  0F 47 C1                        cmova eax, ecx
002CD836  3B 45 AF                        cmp eax, dword ptr [rbp - 0x51]
002CD839  0F 82 6B 03 00 00               jb 0x1402cdbaa
002CD83F  8B 45 AF                        mov eax, dword ptr [rbp - 0x51]
002CD842  3B 45 B3                        cmp eax, dword ptr [rbp - 0x4d]
002CD845  0F 87 A3 01 00 00               ja 0x1402cd9ee
002CD84B  8B 75 B3                        mov esi, dword ptr [rbp - 0x4d]
002CD84E  45 84 DB                        test r11b, r11b
002CD851  0F 85 19 02 00 00               jne 0x1402cda70
002CD857  45 38 9C 1F 31 02 00 00         cmp byte ptr [r15 + rbx + 0x231], r11b
002CD85F  0F 85 FA 02 00 00               jne 0x1402cdb5f
002CD865  8B 7D B7                        mov edi, dword ptr [rbp - 0x49]
002CD868  8B D7                           mov edx, edi
002CD86A  3B FE                           cmp edi, esi
002CD86C  0F 87 4E 03 00 00               ja 0x1402cdbc0
002CD872  41 3B FC                        cmp edi, r12d
002CD875  41 0F 42 D4                     cmovb edx, r12d
002CD879  41 80 F9 02                     cmp r9b, 2
002CD87D  0F 85 CF 03 00 00               jne 0x1402cdc52
002CD883  41 80 E9 05                     sub r9b, 5
002CD887  45 3A CD                        cmp r9b, r13b
002CD88A  0F 86 56 03 00 00               jbe 0x1402cdbe6
002CD890  83 3D 31 94 CF 00 00            cmp dword ptr [rip + 0xcf9431], 0
002CD897  B8 64 00 00 00                  mov eax, 0x64
002CD89C  0F 85 44 03 00 00               jne 0x1402cdbe6
002CD8A2  3B D0                           cmp edx, eax
002CD8A4  0F 43 D6                        cmovae edx, esi
002CD8A7  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
002CD8AB  45 33 C9                        xor r9d, r9d
002CD8AE  41 8B C1                        mov eax, r9d
002CD8B1  45 84 DB                        test r11b, r11b
002CD8B4  75 03                           jne 0x1402cd8b9
002CD8B6  8B 41 4C                        mov eax, dword ptr [rcx + 0x4c]
002CD8B9  3B C7                           cmp eax, edi
002CD8BB  0F 83 6B 03 00 00               jae 0x1402cdc2c
002CD8C1  2B F8                           sub edi, eax
002CD8C3  41 3B FC                        cmp edi, r12d
002CD8C6  41 0F 42 FC                     cmovb edi, r12d
002CD8CA  41 3B FA                        cmp edi, r10d
002CD8CD  41 0F 47 FA                     cmova edi, r10d
002CD8D1  45 84 DB                        test r11b, r11b
002CD8D4  0F 84 7C 01 00 00               je 0x1402cda56
002CD8DA  45 8B F1                        mov r14d, r9d
002CD8DD  44 39 0D 68 D9 C3 00            cmp dword ptr [rip + 0xc3d968], r9d
002CD8E4  0F 85 10 02 00 00               jne 0x1402cdafa
002CD8EA  44 38 4D A7                     cmp byte ptr [rbp - 0x59], r9b
002CD8EE  0F 85 6F 03 00 00               jne 0x1402cdc63
002CD8F4  45 8A AC 1F 2C 02 00 00         mov r13b, byte ptr [r15 + rbx + 0x22c]
002CD8FC  45 84 ED                        test r13b, r13b
002CD8FF  75 04                           jne 0x1402cd905
002CD901  41 83 C8 04                     or r8d, 4
002CD905  48 8B 4D EF                     mov rcx, qword ptr [rbp - 0x11]
002CD909  48 8D 45 DF                     lea rax, [rbp - 0x21]
002CD90D  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
002CD912  44 8B CE                        mov r9d, esi
002CD915  48 8D 45 D7                     lea rax, [rbp - 0x29]
002CD919  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
002CD91E  48 8D 45 BF                     lea rax, [rbp - 0x41]
002CD922  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
002CD927  41 8B 84 1F 34 02 00 00         mov eax, dword ptr [r15 + rbx + 0x234]
002CD92F  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
002CD934  45 8B C4                        mov r8d, r12d
002CD937  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
002CD93B  41 8B 84 1F 24 02 00 00         mov eax, dword ptr [r15 + rbx + 0x224]
002CD943  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
002CD947  48 8B 83 78 01 00 00            mov rax, qword ptr [rbx + 0x178]
002CD94E  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
002CD953  E8 78 D1 3E 00                  call 0x1406baad0
002CD958  3B F8                           cmp edi, eax
002CD95A  44 89 65 0F                     mov dword ptr [rbp + 0xf], r12d
002CD95E  8B C8                           mov ecx, eax
002CD960  89 75 13                        mov dword ptr [rbp + 0x13], esi
002CD963  0F 47 F8                        cmova edi, eax
002CD966  89 4D 07                        mov dword ptr [rbp + 7], ecx
002CD969  33 C0                           xor eax, eax
002CD96B  89 7D 17                        mov dword ptr [rbp + 0x17], edi
002CD96E  8B 7D C7                        mov edi, dword ptr [rbp - 0x39]
002CD971  45 84 ED                        test r13b, r13b
002CD974  89 45 28                        mov dword ptr [rbp + 0x28], eax
002CD977  66 89 45 2C                     mov word ptr [rbp + 0x2c], ax
002CD97B  0F 94 45 27                     sete byte ptr [rbp + 0x27]
002CD97F  88 45 2E                        mov byte ptr [rbp + 0x2e], al
002CD982  45 33 E4                        xor r12d, r12d
002CD985  48 8B 45 D7                     mov rax, qword ptr [rbp - 0x29]
002CD989  48 89 45 F7                     mov qword ptr [rbp - 9], rax
002CD98D  48 8B 45 DF                     mov rax, qword ptr [rbp - 0x21]
002CD991  48 89 45 FF                     mov qword ptr [rbp - 1], rax
002CD995  45 8D 6C 24 01                  lea r13d, [r12 + 1]
002CD99A  8B 45 BF                        mov eax, dword ptr [rbp - 0x41]
002CD99D  89 45 0B                        mov dword ptr [rbp + 0xb], eax
002CD9A0  41 8B 84 1F 24 02 00 00         mov eax, dword ptr [r15 + rbx + 0x224]
002CD9A8  89 45 1F                        mov dword ptr [rbp + 0x1f], eax
002CD9AB  41 8B 84 1F 34 02 00 00         mov eax, dword ptr [r15 + rbx + 0x234]
002CD9B3  89 45 23                        mov dword ptr [rbp + 0x23], eax
002CD9B6  44 89 75 1B                     mov dword ptr [rbp + 0x1b], r14d
002CD9BA  85 FF                           test edi, edi
002CD9BC  0F 84 D8 00 00 00               je 0x1402cda9a
002CD9C2  44 8B 4D AB                     mov r9d, dword ptr [rbp - 0x55]
002CD9C6  48 8D 4D F7                     lea rcx, [rbp - 9]
002CD9CA  4C 8B 55 E7                     mov r10, qword ptr [rbp - 0x19]
002CD9CE  44 8B 5D C3                     mov r11d, dword ptr [rbp - 0x3d]
002CD9D2  44 8A 75 AA                     mov r14b, byte ptr [rbp - 0x56]
002CD9D6  E9 74 FC FF FF                  jmp 0x1402cd64f
002CD9DB  48 8B CB                        mov rcx, rbx
002CD9DE  E9 65 FC FF FF                  jmp 0x1402cd648
002CD9E3  8B 83 C4 01 00 00               mov eax, dword ptr [rbx + 0x1c4]
002CD9E9  E9 EA FD FF FF                  jmp 0x1402cd7d8
002CD9EE  3B CE                           cmp ecx, esi
002CD9F0  8B C6                           mov eax, esi
002CD9F2  0F 47 C1                        cmova eax, ecx
002CD9F5  3B 45 AF                        cmp eax, dword ptr [rbp - 0x51]
002CD9F8  0F 82 B8 01 00 00               jb 0x1402cdbb6
002CD9FE  8B 75 AF                        mov esi, dword ptr [rbp - 0x51]
002CDA01  E9 48 FE FF FF                  jmp 0x1402cd84e
002CDA06  44 39 25 3F D8 C3 00            cmp dword ptr [rip + 0xc3d83f], r12d
002CDA0D  0F 85 D9 00 00 00               jne 0x1402cdaec
002CDA13  44 38 65 A7                     cmp byte ptr [rbp - 0x59], r12b
002CDA17  0F 85 17 02 00 00               jne 0x1402cdc34
002CDA1D  41 8B D4                        mov edx, r12d
002CDA20  E9 E0 FD FF FF                  jmp 0x1402cd805
002CDA25  3B D1                           cmp edx, ecx
002CDA27  8B C1                           mov eax, ecx
002CDA29  0F 42 C2                        cmovb eax, edx
002CDA2C  3B C6                           cmp eax, esi
002CDA2E  0F 87 48 01 00 00               ja 0x1402cdb7c
002CDA34  8B C6                           mov eax, esi
002CDA36  41 3B C2                        cmp eax, r10d
002CDA39  0F 83 63 01 00 00               jae 0x1402cdba2
002CDA3F  3B D1                           cmp edx, ecx
002CDA41  8B C1                           mov eax, ecx
002CDA43  0F 42 C2                        cmovb eax, edx
002CDA46  3B C6                           cmp eax, esi
002CDA48  0F 87 3A 01 00 00               ja 0x1402cdb88
002CDA4E  44 8B E6                        mov r12d, esi
002CDA51  E9 D9 FD FF FF                  jmp 0x1402cd82f
002CDA56  44 39 0D EB D7 C3 00            cmp dword ptr [rip + 0xc3d7eb], r9d
002CDA5D  0F 85 77 FE FF FF               jne 0x1402cd8da
002CDA63  45 8B B4 1F 28 02 00 00         mov r14d, dword ptr [r15 + rbx + 0x228]
002CDA6B  E9 6D FE FF FF                  jmp 0x1402cd8dd
002CDA70  8B FE                           mov edi, esi
002CDA72  8B D6                           mov edx, esi
002CDA74  E9 F9 FD FF FF                  jmp 0x1402cd872
002CDA79  8B 83 C8 01 00 00               mov eax, dword ptr [rbx + 0x1c8]
002CDA7F  E9 13 FD FF FF                  jmp 0x1402cd797
002CDA84  3B D1                           cmp edx, ecx
002CDA86  8B C1                           mov eax, ecx
002CDA88  0F 42 C2                        cmovb eax, edx
002CDA8B  3B C6                           cmp eax, esi
002CDA8D  0F 87 DD 00 00 00               ja 0x1402cdb70
002CDA93  8B C6                           mov eax, esi
002CDA95  E9 88 FD FF FF                  jmp 0x1402cd822
002CDA9A  0F B6 45 28                     movzx eax, byte ptr [rbp + 0x28]
002CDA9E  4C 39 A3 98 01 00 00            cmp qword ptr [rbx + 0x198], r12
002CDAA5  41 0F 45 C5                     cmovne eax, r13d
002CDAA9  88 45 28                        mov byte ptr [rbp + 0x28], al
002CDAAC  E9 11 FF FF FF                  jmp 0x1402cd9c2
002CDAB1  48 8D 4B 18                     lea rcx, [rbx + 0x18]
002CDAB5  48 8D 15 14 E4 B3 00            lea rdx, [rip + 0xb3e414]
002CDABC  E8 BF 01 00 00                  call 0x1402cdc80
002CDAC1  45 33 DB                        xor r11d, r11d
002CDAC4  85 C0                           test eax, eax
002CDAC6  0F 85 72 FA FF FF               jne 0x1402cd53e
002CDACC  44 39 9B 30 01 00 00            cmp dword ptr [rbx + 0x130], r11d
002CDAD3  0F 85 65 FA FF FF               jne 0x1402cd53e
002CDAD9  48 8B 3D C8 90 CF 00            mov rdi, qword ptr [rip + 0xcf90c8]
002CDAE0  4C 8D 35 C1 90 CF 00            lea r14, [rip + 0xcf90c1]
002CDAE7  E9 58 FA FF FF                  jmp 0x1402cd544
002CDAEC  41 0F B6 94 1F 2F 02 00 00      movzx edx, byte ptr [r15 + rbx + 0x22f]
002CDAF5  E9 0B FD FF FF                  jmp 0x1402cd805
002CDAFA  41 0F B6 84 1F 30 02 00 00      movzx eax, byte ptr [r15 + rbx + 0x230]
002CDB03  44 3B F0                        cmp r14d, eax
002CDB06  44 0F 43 F0                     cmovae r14d, eax
002CDB0A  E9 DB FD FF FF                  jmp 0x1402cd8ea
002CDB0F  8B 83 24 03 00 00               mov eax, dword ptr [rbx + 0x324]
002CDB15  8B 55 AB                        mov edx, dword ptr [rbp - 0x55]
002CDB18  83 C0 01                        add eax, 1
002CDB1B  44 0F 45 E8                     cmovne r13d, eax
002CDB1F  33 C9                           xor ecx, ecx
002CDB21  44 89 AB 24 03 00 00            mov dword ptr [rbx + 0x324], r13d
002CDB28  44 88 A3 BC 04 00 00            mov byte ptr [rbx + 0x4bc], r12b
002CDB2F  89 93 10 02 00 00               mov dword ptr [rbx + 0x210], edx
002CDB35  E8 A6 0C 0B 00                  call 0x14037e7e0
002CDB3A  48 8B CB                        mov rcx, rbx
002CDB3D  48 89 83 B0 04 00 00            mov qword ptr [rbx + 0x4b0], rax
002CDB44  44 89 A3 B8 04 00 00            mov dword ptr [rbx + 0x4b8], r12d
002CDB4B  E8 D0 DB 1A 00                  call 0x14047b720
002CDB50  33 D2                           xor edx, edx
002CDB52  48 8B CB                        mov rcx, rbx
002CDB55  E8 52 1C 1D 00                  call 0x14049f7ac
002CDB5A  E9 EA FB FF FF                  jmp 0x1402cd749
002CDB5F  8B 4D BB                        mov ecx, dword ptr [rbp - 0x45]
002CDB62  8B F9                           mov edi, ecx
002CDB64  39 4D B7                        cmp dword ptr [rbp - 0x49], ecx
002CDB67  0F 47 7D B7                     cmova edi, dword ptr [rbp - 0x49]
002CDB6B  E9 F8 FC FF FF                  jmp 0x1402cd868
002CDB70  3B D1                           cmp edx, ecx
002CDB72  8B C1                           mov eax, ecx
002CDB74  0F 42 C2                        cmovb eax, edx
002CDB77  E9 A6 FC FF FF                  jmp 0x1402cd822
002CDB7C  3B D1                           cmp edx, ecx
002CDB7E  8B C1                           mov eax, ecx
002CDB80  0F 42 C2                        cmovb eax, edx
002CDB83  E9 AE FE FF FF                  jmp 0x1402cda36
002CDB88  3B D1                           cmp edx, ecx
002CDB8A  44 8B E1                        mov r12d, ecx
002CDB8D  44 0F 42 E2                     cmovb r12d, edx
002CDB91  E9 99 FC FF FF                  jmp 0x1402cd82f
002CDB96  3B D1                           cmp edx, ecx
002CDB98  8B C1                           mov eax, ecx
002CDB9A  0F 42 C2                        cmovb eax, edx
002CDB9D  E9 74 FC FF FF                  jmp 0x1402cd816
002CDBA2  45 8B E2                        mov r12d, r10d
002CDBA5  E9 85 FC FF FF                  jmp 0x1402cd82f
002CDBAA  3B CE                           cmp ecx, esi
002CDBAC  8B C6                           mov eax, esi
002CDBAE  0F 47 C1                        cmova eax, ecx
002CDBB1  E9 8C FC FF FF                  jmp 0x1402cd842
002CDBB6  3B CE                           cmp ecx, esi
002CDBB8  0F 47 F1                        cmova esi, ecx
002CDBBB  E9 8E FC FF FF                  jmp 0x1402cd84e
002CDBC0  8B D6                           mov edx, esi
002CDBC2  45 84 F6                        test r14b, r14b
002CDBC5  0F 84 AE FC FF FF               je 0x1402cd879
002CDBCB  41 83 C8 02                     or r8d, 2
002CDBCF  E9 A5 FC FF FF                  jmp 0x1402cd879
002CDBD4  44 38 1D CB 8E CF 00            cmp byte ptr [rip + 0xcf8ecb], r11b
002CDBDB  0F 85 CE F9 FF FF               jne 0x1402cd5af
002CDBE1  E9 AD F9 FF FF                  jmp 0x1402cd593
002CDBE6  41 8B C2                        mov eax, r10d
002CDBE9  E9 B4 FC FF FF                  jmp 0x1402cd8a2
002CDBEE  3B 75 BB                        cmp esi, dword ptr [rbp - 0x45]
002CDBF1  0F 46 75 BB                     cmovbe esi, dword ptr [rbp - 0x45]
002CDBF5  89 75 BB                        mov dword ptr [rbp - 0x45], esi
002CDBF8  E9 96 F9 FF FF                  jmp 0x1402cd593
002CDBFD  4C 8B 83 E0 01 00 00            mov r8, qword ptr [rbx + 0x1e0]
002CDC04  48 8B CE                        mov rcx, rsi
002CDC07  48 0F AF 8F E0 01 00 00         imul rcx, qword ptr [rdi + 0x1e0]
002CDC0F  33 D2                           xor edx, edx
002CDC11  49 8B C0                        mov rax, r8
002CDC14  48 D1 E8                        shr rax, 1
002CDC17  48 03 C1                        add rax, rcx
002CDC1A  49 F7 F0                        div r8
002CDC1D  41 3B C7                        cmp eax, r15d
002CDC20  48 8B F0                        mov rsi, rax
002CDC23  41 0F 47 F7                     cmova esi, r15d
002CDC27  E9 95 F9 FF FF                  jmp 0x1402cd5c1
002CDC2C  41 8B F9                        mov edi, r9d
002CDC2F  E9 8F FC FF FF                  jmp 0x1402cd8c3
002CDC34  0F B6 45 A9                     movzx eax, byte ptr [rbp - 0x57]
002CDC38  48 8B 55 CF                     mov rdx, qword ptr [rbp - 0x31]
002CDC3C  8B 94 82 80 00 00 00            mov edx, dword ptr [rdx + rax*4 + 0x80]
002CDC43  E9 BD FB FF FF                  jmp 0x1402cd805
002CDC48  3B C1                           cmp eax, ecx
002CDC4A  0F 43 C1                        cmovae eax, ecx
002CDC4D  E9 96 FB FF FF                  jmp 0x1402cd7e8
002CDC52  41 8D 41 FC                     lea eax, [r9 - 4]
002CDC56  3C 02                           cmp al, 2
002CDC58  0F 87 49 FC FF FF               ja 0x1402cd8a7
002CDC5E  E9 20 FC FF FF                  jmp 0x1402cd883
002CDC63  0F B6 45 A9                     movzx eax, byte ptr [rbp - 0x57]
002CDC67  8B 4C 81 78                     mov ecx, dword ptr [rcx + rax*4 + 0x78]
002CDC6B  44 3B F1                        cmp r14d, ecx
002CDC6E  44 0F 43 F1                     cmovae r14d, ecx
002CDC72  E9 7D FC FF FF                  jmp 0x1402cd8f4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmPerfApplyDomainState(__int64 a1)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned int v_stack_mD0;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (240);
    result = (*(unsigned __int64 *)(v_rip + 11784870)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 47) = result;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 95 + 39) = 0;
    v_r11 = 0;
    *(unsigned int *)(v_rsp - 95 - 65) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 41) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 33) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 17) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 312) + 8);
    a1 = (a1) * ((int)(*(unsigned int *)(v_rip + 12843311)));
    *(unsigned __int64 *)(v_rsp - 95 - 9) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 + 7) = v_xmm0;
    *(unsigned __int8 *)(v_rsp - 95 - 88) = 0;
    result = (*(unsigned __int64 *)(v_rip + 11775704) + 40) + (a1);
    *(unsigned __int64 *)(v_rsp - 95 - 49) = result;
    *(unsigned __int64 *)(v_rsp - 95 + 23) = v_xmm0;
    result = PpmGetPerfPolicyClass(*(unsigned __int64 *)(a1 + 16), *(unsigned __int64 *)(v_rip + 11775704), a3, a4);
    *(unsigned __int8 *)(v_rsp - 95 - 87) = (unsigned __int8)(result);
    *(unsigned int *)(v_rsp - 95 - 85) = (unsigned int)(v_r11 + 100);
    *(unsigned int *)(v_rsp - 95 - 77) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 460)));
    *(unsigned int *)(v_rsp - 95 - 73) = 0;
    *(unsigned __int8 *)(v_rsp - 95 - 89) = 0;
    *(unsigned int *)(v_rsp - 95 - 69) = 0;
    *(unsigned int *)(v_rsp - 95 - 81) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 452)));
    if ((*(unsigned int *)(v_rip + 13604806)) != 0) goto loc_002CDAB1;
loc_002CD53E:
loc_002CD544:
loc_002CD54A:
    if (a1 == (*(unsigned __int64 *)(a1))) goto loc_002CD5E8;
    if (a1 == a1) goto loc_002CD5CA;
    if ((*(unsigned int *)(a1 + 304)) != 0) goto loc_002CD593;
    result = KeIsSubsetAffinityEx(a1 + 24, v_rip + 11790686, a3, a4);
    v_r11 = 0;
    if ((unsigned int)(result) != 0) goto loc_002CD593;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) - 35056)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) - 35056))) goto loc_002CD598;
loc_002CD593:
    goto loc_002CD54A;
loc_002CD598:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 300))) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 300)))) goto loc_002CDBD4;
loc_002CD5AF:
    if ((*(unsigned __int8 *)(a1 + 301)) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 301)))) goto loc_002CDBFD;
loc_002CD5C1:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 300))) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 300)))) goto loc_002CDBEE;
loc_002CD5CA:
    v_rsi = (unsigned int)(*(unsigned int *)(a1 + 524));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 524)))) <= (*(unsigned int *)(v_rsp - 95 - 73))) { v_rsi = *(unsigned int *)(v_rsp - 95 - 73); }
    *(unsigned int *)(v_rsp - 95 - 73) = (unsigned int)((unsigned int)((unsigned int)(v_rsi)));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 532)) == 0) goto loc_002CD593;
    *(unsigned __int8 *)(v_rsp - 95 - 89) = 1;
    *(unsigned int *)(v_rsp - 95 - 73) = (unsigned int)((unsigned int)((unsigned int)(v_rsi)));
    goto loc_002CD593;
loc_002CD5E8:
    result = PpmPerfApplyCapsAndFloors(v_rsp - 95 - 81, v_rsp - 95 - 77, v_rsp - 95 - 85, a1);
    v_r12 = 0;
    *(unsigned __int8 *)(v_rsp - 95 - 86) = (unsigned __int8)(result);
    *(unsigned int *)(v_rsp - 95 - 61) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 25) = 0;
loc_002CD621:
    *(unsigned int *)(v_rsp - 95 - 57) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11787753 + 0 * 8)));
    if ((*(unsigned int *)(a1 + (unsigned int)(*(unsigned int *)(v_rip + 11787753 + 0 * 8)) * 4 + 760)) == 0) goto loc_002CD77A;
    if ((*(unsigned __int8 *)(v_rip + 11787753 + 0 * 8 + 4)) == 0) goto loc_002CD9DB;
    a1 = (v_rsp - 95 - 81) * (0);
    a1 = (a1) + (a1);
loc_002CD648:
    a1 = (a1) + (808);
loc_002CD64F:
    a2 = (v_rip + 11787753) * ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11787753 + 0 * 8)))));
    if ((*(unsigned __int8 *)(a1 + 1212)) != 0) goto loc_002CD6E7;
    if ((*(unsigned __int8 *)(a2 + a1 * 1 + 856)) != ((unsigned __int8)(*(unsigned __int8 *)(a1 + 48)))) goto loc_002CD6E7;
    if ((*(unsigned int *)(a2 + a1 * 1 + 832)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24))))) goto loc_002CD6E7;
    if ((*(unsigned int *)(a2 + a1 * 1 + 836)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 28))))) goto loc_002CD6E7;
    if ((*(unsigned int *)(a2 + a1 * 1 + 844)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 36))))) goto loc_002CD6E7;
    if ((*(unsigned int *)(a2 + a1 * 1 + 848)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40))))) goto loc_002CD6E7;
    if ((*(unsigned __int64 *)(a2 + a1 * 1 + 808)) != (*(unsigned __int64 *)(a1))) goto loc_002CD6E7;
    if ((*(unsigned __int64 *)(a2 + a1 * 1 + 816)) != (*(unsigned __int64 *)(a1 + 8))) goto loc_002CD6E7;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 85)))) != (*(unsigned int *)(a1 + 528))) goto loc_002CD6E7;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 48)) != 0) goto loc_002CD6E1;
    if ((*(unsigned int *)(a2 + a1 * 1 + 840)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32))))) goto loc_002CD6E7;
    if ((*(unsigned int *)(a2 + a1 * 1 + 824)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16))))) goto loc_002CD6E7;
loc_002CD6E1:
    goto loc_002CD71F;
loc_002CD6E7:
    *(unsigned __int8 *)(v_rsp - 95 - 88) = 1;
    *(unsigned __int64 *)(a2 + a1 * 1 + 808) = v_xmm0;
    *(unsigned __int64 *)(a2 + a1 * 1 + 824) = v_xmm1;
    *(unsigned __int64 *)(a2 + a1 * 1 + 840) = v_xmm0;
    *(unsigned __int64 *)(a2 + a1 * 1 + 856) = v_xmm1;
loc_002CD71F:
    v_r11 = (unsigned int)((0) + (1));
    v_r10 = (0) + (1);
    *(unsigned int *)(v_rsp - 95 - 61) = (unsigned int)(v_r11);
    *(unsigned __int64 *)(v_rsp - 95 - 25) = v_r10;
    if (((unsigned int)(v_r11)) < 7) goto loc_002CD621;
    if (1 != 0) goto loc_002CDB0F;
loc_002CD749:
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 47)) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rip + 11787450, *(unsigned __int8 *)(a1 + 48), (unsigned int)(*(unsigned int *)(v_rsp - 95 - 85)));
    return result;
loc_002CD77A:
    v_r15 = (*(unsigned __int64 *)(v_stack_m28 + 72)) << (5);
    if ((unsigned __int8)(*(unsigned __int8 *)(v_r15 + *(unsigned __int64 *)(v_stack_m28 + 56) * 1 + 557)) == 0) goto loc_002CDA79;
loc_002CD797:
    a3 = ((unsigned __int8)(*(unsigned __int8 *)(v_r15 + *(unsigned __int64 *)(v_stack_m28 + 56) * 1 + 557)) != 0) ? 1 : 0;
    v_rsi = (unsigned int)(*(unsigned int *)(v_r15 + *(unsigned __int64 *)(v_stack_m28 + 56) * 1 + 544));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 460)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + *(unsigned __int64 *)(v_stack_m28 + 56) * 1 + 544))))) { v_rsi = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 460))); }
    if ((unsigned __int8)(*(unsigned __int8 *)(v_r15 + *(unsigned __int64 *)(v_stack_m28 + 56) * 1 + 558)) != 0) goto loc_002CD9E3;
    a3 = (unsigned int)((a3) | (8));
    result = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 85))));
    if ((*(unsigned int *)(v_rip + 13604083)) == 0) { result = 100; }
loc_002CD7D8:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + *(unsigned __int64 *)(v_stack_m28 + 56) * 1 + 536)))) < 100) goto loc_002CDC48;
loc_002CD7E8:
    a1 = (unsigned int)(*(unsigned int *)(v_r15 + *(unsigned __int64 *)(v_stack_m28 + 56) * 1 + 540));
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + *(unsigned __int64 *)(v_stack_m28 + 56) * 1 + 540))))) { a1 = (unsigned int)(result); }
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 12847351)) == 0) goto loc_002CDA06;
loc_002CD805:
    result = (unsigned int)((unsigned int)(a1));
    if (100 < ((unsigned int)(a1))) { result = 100; }
    if (((unsigned int)(result)) > ((unsigned int)(v_rsi))) goto loc_002CDB96;
loc_002CD816:
    if (((unsigned int)((unsigned int)((unsigned int)(v_rsi)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 85))))) goto loc_002CDA84;
loc_002CD822:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 85)))))) > (*(unsigned int *)(v_rsp - 95 - 77))) goto loc_002CDA25;
loc_002CD82F:
    result = (unsigned int)((unsigned int)(v_rsi));
    if (((unsigned int)(a1)) > ((unsigned int)(v_rsi))) { result = (unsigned int)(a1); }
    if (((unsigned int)(result)) < (*(unsigned int *)(v_rsp - 95 - 81))) goto loc_002CDBAA;
loc_002CD842:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 81)))) > (*(unsigned int *)(v_rsp - 95 - 77))) goto loc_002CD9EE;
loc_002CD84E:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 12847351)) != 0) goto loc_002CDA70;
    if ((*(unsigned __int8 *)(v_r15 + *(unsigned __int64 *)(v_stack_m28 + 56) * 1 + 561)) != ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 12847351)))) goto loc_002CDB5F;
loc_002CD868:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 77))))) goto loc_002CDBC0;
loc_002CD872:
    a2 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 77))))) { a2 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 77))); }
loc_002CD879:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r15 + *(unsigned __int64 *)(v_stack_m28 + 56) * 1 + 558))) != 2) goto loc_002CDC52;
loc_002CD883:
    a4 = (unsigned __int8)((*(unsigned __int8 *)(v_r15 + *(unsigned __int64 *)(v_stack_m28 + 56) * 1 + 558)) - (5));
    if (((unsigned __int8)(a4)) <= 1) goto loc_002CDBE6;
    if ((*(unsigned int *)(v_rip + 13603889)) != 0) goto loc_002CDBE6;
loc_002CD8A2:
    if (((unsigned int)(a2)) >= 100) { a2 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 77))); }
loc_002CD8A7:
    a4 = 0;
    result = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 12847351)) == 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 49) + 76);
    }
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73))))) goto loc_002CDC2C;
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73))) - ((unsigned int)(result)));
loc_002CD8C3:
    if (((unsigned int)(v_rdi)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 77))))) { v_rdi = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 77))); }
    if (((unsigned int)(v_rdi)) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 85))))) { v_rdi = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 85))); }
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 12847351)) == 0) goto loc_002CDA56;
loc_002CD8DA:
loc_002CD8DD:
    if ((*(unsigned int *)(v_rip + 12835176)) != 0) goto loc_002CDAFA;
loc_002CD8EA:
    if ((*(unsigned __int8 *)(v_rsp - 95 - 89)) != 0) goto loc_002CDC63;
loc_002CD8F4:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_r15 + *(unsigned __int64 *)(v_stack_m28 + 56) * 1 + 556)) == 0) {
        a3 = (unsigned int)((a3) | (4));
    }
    v_stack_mA0 = v_rsp - 95 - 33;
    v_stack_mA8 = v_rsp - 95 - 41;
    v_stack_mB0 = v_rsp - 95 - 65;
    v_stack_mB8 = (unsigned int)(a3);
    v_stack_mC0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + *(unsigned __int64 *)(v_stack_m28 + 56) * 1 + 564)));
    v_stack_mC8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + *(unsigned __int64 *)(v_stack_m28 + 56) * 1 + 548)));
    v_stack_mD0 = 0;
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_rsp - 95 - 17), a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 77)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 77)))));
    *(unsigned int *)(v_rsp - 95 + 15) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 77)));
    *(unsigned int *)(v_rsp - 95 + 19) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 77)));
    if (((unsigned int)(v_rdi)) > ((unsigned int)(result))) { v_rdi = (unsigned int)(result); }
    *(unsigned int *)(v_rsp - 95 + 7) = (unsigned int)((unsigned int)((unsigned int)(result)));
    result = 0;
    *(unsigned int *)(v_rsp - 95 + 23) = (unsigned int)(v_rdi);
    *(unsigned int *)(v_rsp - 95 + 40) = 0;
    *(unsigned __int16 *)(v_rsp - 95 + 44) = 0;
    *(unsigned __int8 *)(v_rsp - 95 + 46) = 0;
    v_r12 = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 9) = *(unsigned __int64 *)(v_rsp - 95 - 41);
    *(unsigned __int64 *)(v_rsp - 95 - 1) = *(unsigned __int64 *)(v_rsp - 95 - 33);
    *(unsigned int *)(v_rsp - 95 + 11) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 65)));
    *(unsigned int *)(v_rsp - 95 + 31) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + *(unsigned __int64 *)(v_stack_m28 + 56) * 1 + 548)));
    *(unsigned int *)(v_rsp - 95 + 35) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + *(unsigned __int64 *)(v_stack_m28 + 56) * 1 + 564)));
    *(unsigned int *)(v_rsp - 95 + 27) = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 57))) == 0) goto loc_002CDA9A;
loc_002CD9C2:
    goto loc_002CD64F;
loc_002CD9DB:
    goto loc_002CD648;
loc_002CD9E3:
    goto loc_002CD7D8;
loc_002CD9EE:
    result = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 77))));
    if (((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56))) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 77))))) { result = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56)); }
    if (((unsigned int)(result)) < (*(unsigned int *)(v_rsp - 95 - 81))) goto loc_002CDBB6;
    goto loc_002CD84E;
loc_002CDA06:
    if ((*(unsigned int *)(v_rip + 12834879)) != 0) goto loc_002CDAEC;
    if ((*(unsigned __int8 *)(v_rsp - 95 - 89)) != 0) goto loc_002CDC34;
    goto loc_002CD805;
loc_002CDA25:
    result = (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56)));
    if (0 < ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56)))) { result = 0; }
    if (((unsigned int)(result)) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 81))))) goto loc_002CDB7C;
loc_002CDA36:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 81)))))) >= ((unsigned int)(*(unsigned __int64 *)(v_rsp - 95 - 25)))) goto loc_002CDBA2;
    result = (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56)));
    if (0 < ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56)))) { result = 0; }
    if (((unsigned int)(result)) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 81))))) goto loc_002CDB88;
    goto loc_002CD82F;
loc_002CDA56:
    if ((*(unsigned int *)(v_rip + 12834795)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 85))))) goto loc_002CD8DA;
    goto loc_002CD8DD;
loc_002CDA70:
    goto loc_002CD872;
loc_002CDA79:
    goto loc_002CD797;
loc_002CDA84:
    result = (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56)));
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 81)))))) < ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56)))) { result = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 81))))); }
    if (((unsigned int)(result)) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 81))))) goto loc_002CDB70;
    goto loc_002CD822;
loc_002CDA9A:
    result = *(unsigned __int8 *)(v_rsp - 95 + 40);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 408)) != ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 81)))))) { result = (unsigned int)(v_r12 + 1); }
    *(unsigned __int8 *)(v_rsp - 95 + 40) = (unsigned __int8)(result);
    goto loc_002CD9C2;
loc_002CDAB1:
    result = KeIsSubsetAffinityEx(*(unsigned __int64 *)(v_stack_m28 + 56) + 24, v_rip + 11789332, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 77)))), (unsigned int)(*(unsigned int *)(v_rsp - 95 - 85)));
    v_r11 = 0;
    if ((unsigned int)(result) != 0) goto loc_002CD53E;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 304)) != 0) goto loc_002CD53E;
    goto loc_002CD544;
loc_002CDAEC:
    goto loc_002CD805;
loc_002CDAFA:
    v_r14 = v_rip + 13603009;
    if (((unsigned int)(v_rip + 13603009)) >= ((unsigned int)(*(unsigned __int8 *)(v_r15 + *(unsigned __int64 *)(v_stack_m28 + 56) * 1 + 560)))) { v_r14 = (unsigned int)(*(unsigned __int8 *)(v_r15 + *(unsigned __int64 *)(v_stack_m28 + 56) * 1 + 560)); }
    goto loc_002CD8EA;
loc_002CDB0F:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 804))) + (1));
    v_r13 = v_r12 + 1;
    if (condition_is_not_equal) { v_r13 = (unsigned int)(result); }
    a1 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 804) = (unsigned int)(v_r13);
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 1212) = (unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 81)))));
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 528) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 85)));
    result = KeQueryPerformanceCounter(a1, (unsigned int)(*(unsigned int *)(v_rsp - 95 - 85)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 77)))), (unsigned int)(*(unsigned int *)(v_rsp - 95 - 85)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 1200) = result;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 1208) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 81)))));
    result = PpmEventDomainPerfStateChange(*(unsigned __int64 *)(v_stack_m28 + 56), (unsigned int)(*(unsigned int *)(v_rsp - 95 - 85)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 77)))), (unsigned int)(*(unsigned int *)(v_rsp - 95 - 85)));
    a2 = 0;
    result = PpmEventQosClassPerfSelection(*(unsigned __int64 *)(v_stack_m28 + 56), a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 77)))), (unsigned int)(*(unsigned int *)(v_rsp - 95 - 85)));
    goto loc_002CD749;
loc_002CDB5F:
    v_rdi = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 69))));
    if ((*(unsigned int *)(v_rsp - 95 - 73)) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 69))))) { v_rdi = *(unsigned int *)(v_rsp - 95 - 73); }
    goto loc_002CD868;
loc_002CDB70:
    result = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 69))));
    if (0 < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 69))))) { result = 0; }
    goto loc_002CD822;
loc_002CDB7C:
    result = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 69))));
    if (0 < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 69))))) { result = 0; }
    goto loc_002CDA36;
loc_002CDB88:
    v_r12 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 69))));
    if (0 < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 69))))) { v_r12 = 0; }
    goto loc_002CD82F;
loc_002CDB96:
    result = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 69))));
    if (0 < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 69))))) { result = 0; }
    goto loc_002CD816;
loc_002CDBA2:
    goto loc_002CD82F;
loc_002CDBAA:
    result = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 81))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 69)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 81))))) { result = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 69))); }
    goto loc_002CD842;
loc_002CDBB6:
    v_rsi = (unsigned int)(*(unsigned int *)(v_rsp - 95 - 81));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 69)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 81))))) { v_rsi = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 69))); }
    goto loc_002CD84E;
loc_002CDBC0:
    if ((unsigned __int8)(v_r14) == 0) goto loc_002CD879;
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 77))))) | (2));
    goto loc_002CD879;
loc_002CDBD4:
    if ((*(unsigned __int8 *)(v_rip + 13602507)) != 0) goto loc_002CD5AF;
    goto loc_002CD593;
loc_002CDBE6:
    goto loc_002CD8A2;
loc_002CDBEE:
    if (((unsigned int)(v_rsi)) <= (*(unsigned int *)(v_rsp - 95 - 69))) { v_rsi = *(unsigned int *)(v_rsp - 95 - 69); }
    *(unsigned int *)(v_rsp - 95 - 69) = (unsigned int)(v_rsi);
    goto loc_002CD593;
loc_002CDBFD:
    a1 = (v_rsi) * (*(unsigned __int64 *)(v_rdi + 480));
    a2 = 0;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 480)) >> (1);
    result = (result) + (a1);
    v_rsi = result;
    if (((unsigned int)(result)) > ((unsigned int)(v_r15))) { v_rsi = (unsigned int)(v_r15); }
    goto loc_002CD5C1;
loc_002CDC2C:
    goto loc_002CD8C3;
loc_002CDC34:
    goto loc_002CD805;
loc_002CDC48:
    result = *(unsigned __int8 *)(v_rsp - 95 - 87);
    if (((unsigned int)(*(unsigned __int8 *)(v_rsp - 95 - 87))) >= ((unsigned int)(a1))) { result = (unsigned int)(a1); }
    goto loc_002CD7E8;
loc_002CDC52:
    if (((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 85)) - 4)) > 2) goto loc_002CD8A7;
    goto loc_002CD883;
loc_002CDC63:
    if (((unsigned int)(v_r14)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + *(unsigned __int8 *)(v_rsp - 95 - 87) * 4 + 120))))) { v_r14 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + *(unsigned __int8 *)(v_rsp - 95 - 87) * 4 + 120))); }
    goto loc_002CD8F4;
}
```

## 5. (Beta) C Style

```c
int64_t PpmPerfApplyDomainState(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint32_t v_stack_mD0;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (240);
    result = (*(uint64_t *)(v_rip + 0xB3D2A6)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x2F) = result;
    result = 0;
    *(uint64_t *)(local_rsp - 0x5F + 0x27) = 0;
    local_r11 = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x41) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x29) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x11) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x138) + 0x8);
    Arg1 = (Arg1) * ((int32_t)(*(uint32_t *)(v_rip + 0xC3F92F)));
    *(uint64_t *)(local_rsp - 0x5F - 0x9) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F + 0x7) = v_xmm0;
    *(uint8_t *)(local_rsp - 0x5F - 0x58) = 0;
    result = (*(uint64_t *)(v_rip + 0xB3AED8) + 40) + (Arg1);
    *(uint64_t *)(local_rsp - 0x5F - 0x31) = result;
    *(uint64_t *)(local_rsp - 0x5F + 0x17) = v_xmm0;
    result = PpmGetPerfPolicyClass(*(uint64_t *)(arg1 + 0x10), *(uint64_t *)(v_rip + 0xB3AED8), a3, a4);
    *(uint8_t *)(local_rsp - 0x5F - 0x57) = (uint8_t)(result);
    *(uint32_t *)(local_rsp - 0x5F - 0x55) = (uint32_t)(local_r11 + 100);
    *(uint32_t *)(local_rsp - 0x5F - 0x4D) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1CC)));
    *(uint32_t *)(local_rsp - 0x5F - 0x49) = 0;
    *(uint8_t *)(local_rsp - 0x5F - 0x59) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x45) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x51) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C4)));
    if ((*(uint32_t *)(v_rip + 0xCF97C6)) != 0) goto loc_002CDAB1;
loc_002CD53E:
loc_002CD544:
loc_002CD54A:
    if (Arg1 == (*(uint64_t *)(arg1))) goto loc_002CD5E8;
    if (Arg1 == Arg1) goto loc_002CD5CA;
    if ((*(uint32_t *)(arg1 + 0x130)) != 0) goto loc_002CD593;
    result = KeIsSubsetAffinityEx(Arg1 + 24, v_rip + 11790686, a3, a4);
    local_r11 = 0;
    if ((uint32_t)(result) != 0) goto loc_002CD593;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) - 0x88F0)) == (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) - 0x88F0))) goto loc_002CD598;
loc_002CD593:
    goto loc_002CD54A;
loc_002CD598:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x12C))) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1) + 0x12C)))) goto loc_002CDBD4;
loc_002CD5AF:
    if ((*(uint8_t *)(arg1 + 0x12D)) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1) + 0x12D)))) goto loc_002CDBFD;
loc_002CD5C1:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x12C))) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1) + 0x12C)))) goto loc_002CDBEE;
loc_002CD5CA:
    local_rsi = (uint32_t)(*(uint32_t *)(arg1 + 0x20C));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20C)))) <= (*(uint32_t *)(local_rsp - 0x5F - 0x49))) { local_rsi = *(uint32_t *)(local_rsp - 0x5F - 0x49); }
    *(uint32_t *)(local_rsp - 0x5F - 0x49) = (uint32_t)((uint32_t)((uint32_t)(local_rsi)));
    if ((*(uint8_t *)(*(uint64_t *)(arg1) + 0x214)) == 0) goto loc_002CD593;
    *(uint8_t *)(local_rsp - 0x5F - 0x59) = 1;
    *(uint32_t *)(local_rsp - 0x5F - 0x49) = (uint32_t)((uint32_t)((uint32_t)(local_rsi)));
    goto loc_002CD593;
loc_002CD5E8:
    result = PpmPerfApplyCapsAndFloors(local_rsp - 95 - 81, local_rsp - 95 - 77, local_rsp - 95 - 85, Arg1);
    local_r12 = 0;
    *(uint8_t *)(local_rsp - 0x5F - 0x56) = (uint8_t)(result);
    *(uint32_t *)(local_rsp - 0x5F - 0x3D) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = 0;
loc_002CD621:
    *(uint32_t *)(local_rsp - 0x5F - 0x39) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB3DDE9 + 0x0 * 8)));
    if ((*(uint32_t *)(arg1 + (uint32_t)(*(uint32_t *)(v_rip + 0xB3DDE9 + 0x0 * 8)) * 4 + 0x2F8)) == 0) goto loc_002CD77A;
    if ((*(uint8_t *)(v_rip + 0xB3DDE9 + 0x0 * 8 + 0x4)) == 0) goto loc_002CD9DB;
    Arg1 = (local_rsp - 95 - 81) * (0);
    Arg1 = (Arg1) + (Arg1);
loc_002CD648:
    Arg1 = (Arg1) + (808);
loc_002CD64F:
    a2 = (v_rip + 11787753) * ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB3DDE9 + 0x0 * 8)))));
    if ((*(uint8_t *)(arg1 + 0x4BC)) != 0) goto loc_002CD6E7;
    if ((*(uint8_t *)(a2 + arg1 * 1 + 0x358)) != ((uint8_t)(*(uint8_t *)(arg1 + 0x30)))) goto loc_002CD6E7;
    if ((*(uint32_t *)(a2 + arg1 * 1 + 0x340)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18))))) goto loc_002CD6E7;
    if ((*(uint32_t *)(a2 + arg1 * 1 + 0x344)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C))))) goto loc_002CD6E7;
    if ((*(uint32_t *)(a2 + arg1 * 1 + 0x34C)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x24))))) goto loc_002CD6E7;
    if ((*(uint32_t *)(a2 + arg1 * 1 + 0x350)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28))))) goto loc_002CD6E7;
    if ((*(uint64_t *)(a2 + arg1 * 1 + 0x328)) != (*(uint64_t *)(arg1))) goto loc_002CD6E7;
    if ((*(uint64_t *)(a2 + arg1 * 1 + 0x330)) != (*(uint64_t *)(arg1 + 0x8))) goto loc_002CD6E7;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55)))) != (*(uint32_t *)(arg1 + 0x210))) goto loc_002CD6E7;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x30)) != 0) goto loc_002CD6E1;
    if ((*(uint32_t *)(a2 + arg1 * 1 + 0x348)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20))))) goto loc_002CD6E7;
    if ((*(uint32_t *)(a2 + arg1 * 1 + 0x338)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10))))) goto loc_002CD6E7;
loc_002CD6E1:
    goto loc_002CD71F;
loc_002CD6E7:
    *(uint8_t *)(local_rsp - 0x5F - 0x58) = 1;
    *(uint64_t *)(a2 + arg1 * 1 + 0x328) = v_xmm0;
    *(uint64_t *)(a2 + arg1 * 1 + 0x338) = v_xmm1;
    *(uint64_t *)(a2 + arg1 * 1 + 0x348) = v_xmm0;
    *(uint64_t *)(a2 + arg1 * 1 + 0x358) = v_xmm1;
loc_002CD71F:
    local_r11 = (uint32_t)((0) + (1));
    local_r10 = (0) + (1);
    *(uint32_t *)(local_rsp - 0x5F - 0x3D) = (uint32_t)(local_r11);
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = local_r10;
    if (((uint32_t)(local_r11)) < 7) goto loc_002CD621;
    if (1 != 0) goto loc_002CDB0F;
loc_002CD749:
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x2F)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_rip + 11787450, *(uint8_t *)(arg1 + 0x30), (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55)));
    return result;
loc_002CD77A:
    local_r15 = (*(uint64_t *)(v_stack_m28 + 0x48)) << (5);
    if ((uint8_t)(*(uint8_t *)(local_r15 + *(uint64_t *)(v_stack_m28 + 0x38) * 1 + 0x22D)) == 0) goto loc_002CDA79;
loc_002CD797:
    a3 = ((uint8_t)(*(uint8_t *)(local_r15 + *(uint64_t *)(v_stack_m28 + 0x38) * 1 + 0x22D)) != 0) ? 1 : 0;
    local_rsi = (uint32_t)(*(uint32_t *)(local_r15 + *(uint64_t *)(v_stack_m28 + 0x38) * 1 + 0x220));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x1CC)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + *(uint64_t *)(v_stack_m28 + 0x38) * 1 + 0x220))))) { local_rsi = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x1CC))); }
    if ((uint8_t)(*(uint8_t *)(local_r15 + *(uint64_t *)(v_stack_m28 + 0x38) * 1 + 0x22E)) != 0) goto loc_002CD9E3;
    a3 = (uint32_t)((a3) | (8));
    result = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55))));
    if ((*(uint32_t *)(v_rip + 0xCF94F3)) == 0) { result = 100; }
loc_002CD7D8:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + *(uint64_t *)(v_stack_m28 + 0x38) * 1 + 0x218)))) < 100) goto loc_002CDC48;
loc_002CD7E8:
    Arg1 = (uint32_t)(*(uint32_t *)(local_r15 + *(uint64_t *)(v_stack_m28 + 0x38) * 1 + 0x21C));
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + *(uint64_t *)(v_stack_m28 + 0x38) * 1 + 0x21C))))) { Arg1 = (uint32_t)(result); }
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xC408F7)) == 0) goto loc_002CDA06;
loc_002CD805:
    result = (uint32_t)((uint32_t)(Arg1));
    if (100 < ((uint32_t)(Arg1))) { result = 100; }
    if (((uint32_t)(result)) > ((uint32_t)(local_rsi))) goto loc_002CDB96;
loc_002CD816:
    if (((uint32_t)((uint32_t)((uint32_t)(local_rsi)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55))))) goto loc_002CDA84;
loc_002CD822:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55)))))) > (*(uint32_t *)(local_rsp - 0x5F - 0x4D))) goto loc_002CDA25;
loc_002CD82F:
    result = (uint32_t)((uint32_t)(local_rsi));
    if (((uint32_t)(Arg1)) > ((uint32_t)(local_rsi))) { result = (uint32_t)(Arg1); }
    if (((uint32_t)(result)) < (*(uint32_t *)(local_rsp - 0x5F - 0x51))) goto loc_002CDBAA;
loc_002CD842:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x51)))) > (*(uint32_t *)(local_rsp - 0x5F - 0x4D))) goto loc_002CD9EE;
loc_002CD84E:
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xC408F7)) != 0) goto loc_002CDA70;
    if ((*(uint8_t *)(local_r15 + *(uint64_t *)(v_stack_m28 + 0x38) * 1 + 0x231)) != ((uint8_t)(*(uint8_t *)(v_rip + 0xC408F7)))) goto loc_002CDB5F;
loc_002CD868:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x4D))))) goto loc_002CDBC0;
loc_002CD872:
    a2 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x4D))))) { a2 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x4D))); }
loc_002CD879:
    if (((uint8_t)(*(uint8_t *)(local_r15 + *(uint64_t *)(v_stack_m28 + 0x38) * 1 + 0x22E))) != 2) goto loc_002CDC52;
loc_002CD883:
    a4 = (uint8_t)((*(uint8_t *)(local_r15 + *(uint64_t *)(v_stack_m28 + 0x38) * 1 + 0x22E)) - (5));
    if (((uint8_t)(a4)) <= 1) goto loc_002CDBE6;
    if ((*(uint32_t *)(v_rip + 0xCF9431)) != 0) goto loc_002CDBE6;
loc_002CD8A2:
    if (((uint32_t)(a2)) >= 100) { a2 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x4D))); }
loc_002CD8A7:
    a4 = 0;
    result = 0;
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xC408F7)) == 0) {
        result = *(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x31) + 0x4C);
    }
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49))))) goto loc_002CDC2C;
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49))) - ((uint32_t)(result)));
loc_002CD8C3:
    if (((uint32_t)(local_rdi)) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x4D))))) { local_rdi = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x4D))); }
    if (((uint32_t)(local_rdi)) > ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55))))) { local_rdi = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55))); }
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xC408F7)) == 0) goto loc_002CDA56;
loc_002CD8DA:
loc_002CD8DD:
    if ((*(uint32_t *)(v_rip + 0xC3D968)) != 0) goto loc_002CDAFA;
loc_002CD8EA:
    if ((*(uint8_t *)(local_rsp - 0x5F - 0x59)) != 0) goto loc_002CDC63;
loc_002CD8F4:
    if ((uint8_t)(*(uint8_t *)(local_r15 + *(uint64_t *)(v_stack_m28 + 0x38) * 1 + 0x22C)) == 0) {
        a3 = (uint32_t)((a3) | (4));
    }
    v_stack_mA0 = local_rsp - 95 - 33;
    v_stack_mA8 = local_rsp - 95 - 41;
    v_stack_mB0 = local_rsp - 95 - 65;
    v_stack_mB8 = (uint32_t)(a3);
    v_stack_mC0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + *(uint64_t *)(v_stack_m28 + 0x38) * 1 + 0x234)));
    v_stack_mC8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + *(uint64_t *)(v_stack_m28 + 0x38) * 1 + 0x224)));
    v_stack_mD0 = 0;
    result = guard_dispatch_icall(*(uint64_t *)(local_rsp - 0x5F - 0x11), a2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x4D)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x4D)))));
    *(uint32_t *)(local_rsp - 0x5F + 0xF) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x4D)));
    *(uint32_t *)(local_rsp - 0x5F + 0x13) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x4D)));
    if (((uint32_t)(local_rdi)) > ((uint32_t)(result))) { local_rdi = (uint32_t)(result); }
    *(uint32_t *)(local_rsp - 0x5F + 0x7) = (uint32_t)((uint32_t)((uint32_t)(result)));
    result = 0;
    *(uint32_t *)(local_rsp - 0x5F + 0x17) = (uint32_t)(local_rdi);
    *(uint32_t *)(local_rsp - 0x5F + 0x28) = 0;
    *(uint16_t *)(local_rsp - 0x5F + 0x2C) = 0;
    *(uint8_t *)(local_rsp - 0x5F + 0x2E) = 0;
    local_r12 = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x9) = *(uint64_t *)(local_rsp - 0x5F - 0x29);
    *(uint64_t *)(local_rsp - 0x5F - 0x1) = *(uint64_t *)(local_rsp - 0x5F - 0x21);
    *(uint32_t *)(local_rsp - 0x5F + 0xB) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x41)));
    *(uint32_t *)(local_rsp - 0x5F + 0x1F) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + *(uint64_t *)(v_stack_m28 + 0x38) * 1 + 0x224)));
    *(uint32_t *)(local_rsp - 0x5F + 0x23) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + *(uint64_t *)(v_stack_m28 + 0x38) * 1 + 0x234)));
    *(uint32_t *)(local_rsp - 0x5F + 0x1B) = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x39))) == 0) goto loc_002CDA9A;
loc_002CD9C2:
    goto loc_002CD64F;
loc_002CD9DB:
    goto loc_002CD648;
loc_002CD9E3:
    goto loc_002CD7D8;
loc_002CD9EE:
    result = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x4D))));
    if (((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38))) > ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x4D))))) { result = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38)); }
    if (((uint32_t)(result)) < (*(uint32_t *)(local_rsp - 0x5F - 0x51))) goto loc_002CDBB6;
    goto loc_002CD84E;
loc_002CDA06:
    if ((*(uint32_t *)(v_rip + 0xC3D83F)) != 0) goto loc_002CDAEC;
    if ((*(uint8_t *)(local_rsp - 0x5F - 0x59)) != 0) goto loc_002CDC34;
    goto loc_002CD805;
loc_002CDA25:
    result = (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38)));
    if (0 < ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38)))) { result = 0; }
    if (((uint32_t)(result)) > ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x51))))) goto loc_002CDB7C;
loc_002CDA36:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x51)))))) >= ((uint32_t)(*(uint64_t *)(local_rsp - 0x5F - 0x19)))) goto loc_002CDBA2;
    result = (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38)));
    if (0 < ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38)))) { result = 0; }
    if (((uint32_t)(result)) > ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x51))))) goto loc_002CDB88;
    goto loc_002CD82F;
loc_002CDA56:
    if ((*(uint32_t *)(v_rip + 0xC3D7EB)) != ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55))))) goto loc_002CD8DA;
    goto loc_002CD8DD;
loc_002CDA70:
    goto loc_002CD872;
loc_002CDA79:
    goto loc_002CD797;
loc_002CDA84:
    result = (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38)));
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x51)))))) < ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38)))) { result = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x51))))); }
    if (((uint32_t)(result)) > ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x51))))) goto loc_002CDB70;
    goto loc_002CD822;
loc_002CDA9A:
    result = *(uint8_t *)(local_rsp - 0x5F + 0x28);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x198)) != ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x51)))))) { result = (uint32_t)(local_r12 + 1); }
    *(uint8_t *)(local_rsp - 0x5F + 0x28) = (uint8_t)(result);
    goto loc_002CD9C2;
loc_002CDAB1:
    result = KeIsSubsetAffinityEx(*(uint64_t *)(v_stack_m28 + 0x38) + 24, v_rip + 11789332, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x4D)))), (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55)));
    local_r11 = 0;
    if ((uint32_t)(result) != 0) goto loc_002CD53E;
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x130)) != 0) goto loc_002CD53E;
    goto loc_002CD544;
loc_002CDAEC:
    goto loc_002CD805;
loc_002CDAFA:
    local_r14 = v_rip + 13603009;
    if (((uint32_t)(v_rip + 13603009)) >= ((uint32_t)(*(uint8_t *)(local_r15 + *(uint64_t *)(v_stack_m28 + 0x38) * 1 + 0x230)))) { local_r14 = (uint32_t)(*(uint8_t *)(local_r15 + *(uint64_t *)(v_stack_m28 + 0x38) * 1 + 0x230)); }
    goto loc_002CD8EA;
loc_002CDB0F:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x324))) + (1));
    local_r13 = local_r12 + 1;
    if (condition_is_not_equal) { local_r13 = (uint32_t)(result); }
    Arg1 = 0;
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x324) = (uint32_t)(local_r13);
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x4BC) = (uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x51)))));
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x210) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55)));
    result = KeQueryPerformanceCounter(Arg1, (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x4D)))), (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55)));
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x4B0) = result;
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x4B8) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x51)))));
    result = PpmEventDomainPerfStateChange(*(uint64_t *)(v_stack_m28 + 0x38), (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x4D)))), (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55)));
    a2 = 0;
    result = PpmEventQosClassPerfSelection(*(uint64_t *)(v_stack_m28 + 0x38), a2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x4D)))), (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55)));
    goto loc_002CD749;
loc_002CDB5F:
    local_rdi = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x45))));
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x49)) > ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x45))))) { local_rdi = *(uint32_t *)(local_rsp - 0x5F - 0x49); }
    goto loc_002CD868;
loc_002CDB70:
    result = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x45))));
    if (0 < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x45))))) { result = 0; }
    goto loc_002CD822;
loc_002CDB7C:
    result = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x45))));
    if (0 < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x45))))) { result = 0; }
    goto loc_002CDA36;
loc_002CDB88:
    local_r12 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x45))));
    if (0 < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x45))))) { local_r12 = 0; }
    goto loc_002CD82F;
loc_002CDB96:
    result = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x45))));
    if (0 < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x45))))) { result = 0; }
    goto loc_002CD816;
loc_002CDBA2:
    goto loc_002CD82F;
loc_002CDBAA:
    result = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x51))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x45)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x51))))) { result = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x45))); }
    goto loc_002CD842;
loc_002CDBB6:
    local_rsi = (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x51));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x45)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x51))))) { local_rsi = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x45))); }
    goto loc_002CD84E;
loc_002CDBC0:
    if ((uint8_t)(local_r14) == 0) goto loc_002CD879;
    a3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x4D))))) | (2));
    goto loc_002CD879;
loc_002CDBD4:
    if ((*(uint8_t *)(v_rip + 0xCF8ECB)) != 0) goto loc_002CD5AF;
    goto loc_002CD593;
loc_002CDBE6:
    goto loc_002CD8A2;
loc_002CDBEE:
    if (((uint32_t)(local_rsi)) <= (*(uint32_t *)(local_rsp - 0x5F - 0x45))) { local_rsi = *(uint32_t *)(local_rsp - 0x5F - 0x45); }
    *(uint32_t *)(local_rsp - 0x5F - 0x45) = (uint32_t)(local_rsi);
    goto loc_002CD593;
loc_002CDBFD:
    Arg1 = (local_rsi) * (*(uint64_t *)(local_rdi + 0x1E0));
    a2 = 0;
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x1E0)) >> (1);
    result = (result) + (Arg1);
    local_rsi = result;
    if (((uint32_t)(result)) > ((uint32_t)(local_r15))) { local_rsi = (uint32_t)(local_r15); }
    goto loc_002CD5C1;
loc_002CDC2C:
    goto loc_002CD8C3;
loc_002CDC34:
    goto loc_002CD805;
loc_002CDC48:
    result = *(uint8_t *)(local_rsp - 0x5F - 0x57);
    if (((uint32_t)(*(uint8_t *)(local_rsp - 0x5F - 0x57))) >= ((uint32_t)(Arg1))) { result = (uint32_t)(Arg1); }
    goto loc_002CD7E8;
loc_002CDC52:
    if (((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55)) - 4)) > 2) goto loc_002CD8A7;
    goto loc_002CD883;
loc_002CDC63:
    if (((uint32_t)(local_r14)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + *(uint8_t *)(local_rsp - 0x5F - 0x57) * 4 + 0x78))))) { local_r14 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + *(uint8_t *)(local_rsp - 0x5F - 0x57) * 4 + 0x78))); }
    goto loc_002CD8F4;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x12C` | `8` | `R` |
| `Arg1` | `+ 0x12D` | `8` | `R` |
| `Arg1` | `+ 0x130` | `32` | `R` |
| `Arg1` | `+ 0x138` | `64` | `R` |
| `Arg1` | `+ 0x178` | `64` | `R` |
| `Arg1` | `+ 0x198` | `64` | `R` |
| `Arg1` | `+ 0x1C4` | `32` | `R` |
| `Arg1` | `+ 0x1C8` | `32` | `R` |
| `Arg1` | `+ 0x1CC` | `32` | `R` |
| `Arg1` | `+ 0x1E0` | `64` | `R` |
| `Arg1` | `+ 0x210` | `32` | `R` |
| `Arg1` | `+ 0x210` | `32` | `W` |
| `Arg1` | `+ 0x2F8 + rdi*4` | `32` | `R` |
| `Arg1` | `+ 0x324` | `32` | `R` |
| `Arg1` | `+ 0x324` | `32` | `W` |
| `Arg1` | `+ 0x4B0` | `64` | `W` |
| `Arg1` | `+ 0x4B8` | `32` | `W` |
| `Arg1` | `+ 0x4BC` | `8` | `R` |
| `Arg1` | `+ 0x4BC` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002CD470&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
