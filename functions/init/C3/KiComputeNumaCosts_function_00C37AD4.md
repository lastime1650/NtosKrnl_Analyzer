# KiComputeNumaCosts

- RVA: `0x00C37AD4`–`0x00C380C8` (길이 `1,524` bytes)
- VA: `0x0000000140C37AD4`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B4340`
- 디코드: `390`개 명령, `1,524/1,524` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x00C37B46` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C37B78` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C37BE7` → [HvlQueryNumaDistance](../../text/58/HvlQueryNumaDistance_function_00584A00.md) (function, `0x00584A00`)
- `0x00C37C43` → [KeIsEmptyGroupMask](../../text/25/KeIsEmptyGroupMask_function_002553B0.md) (function, `0x002553B0`)
- `0x00C37C75` → [KeIsEmptyGroupMask](../../text/25/KeIsEmptyGroupMask_function_002553B0.md) (function, `0x002553B0`)
- `0x00C37CAC` → [KeGetNodePrimarySubNode](../../text/43/KeGetNodePrimarySubNode_function_0043EFF4.md) (function, `0x0043EFF4`)
- `0x00C37CBC` → [KiQuerySubNodeActiveAffinity](../../text/43/KiQuerySubNodeActiveAffinity_function_0043F060.md) (function, `0x0043F060`)
- `0x00C37CED` → [KeSetSystemGroupAffinityThread](../../text/39/KeSetSystemGroupAffinityThread_function_00399140.md) (function, `0x00399140`)
- `0x00C37D2C` → [MmAllocateNodePagesForMdlEx](../../text/3E/MmAllocateNodePagesForMdlEx_function_003EA920.md) (function, `0x003EA920`)
- `0x00C37D54` → [MmMapLockedPagesSpecifyCache](../../text/31/MmMapLockedPagesSpecifyCache_function_00318800.md) (function, `0x00318800`)
- `0x00C37D7B` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00C37DBE` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00C37DFA` → [MiFreePagesFromMdl](../../text/3F/MiFreePagesFromMdl_function_003F8300.md) (function, `0x003F8300`)
- `0x00C37E04` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C37E45` → [KeRevertToUserGroupAffinityThread](../../text/39/KeRevertToUserGroupAffinityThread_function_00398EC0.md) (function, `0x00398EC0`)
- `0x00C37F1B` → [KiGetHalNumaConversionFactor](KiGetHalNumaConversionFactor_function_00C38280.md) (function, `0x00C38280`)
- `0x00C38041` → [qsort](../../text/50/qsort_function_005009F0.md) (function, `0x005009F0`)
- `0x00C380A1` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KeInitSystem](../C7/KeInitSystem_function_00C71660.md) at `0x00C71896`

### Static image references
- `0x00C37AFA` → RVA `0x00E0A740` (`.data`; read)
- `0x00C37B0B` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x00C37B4B` → RVA `0x00F234E8` (`.data`; write)
- `0x00C37B62` → RVA `0x00F234E0` (`.data`; write)
- `0x00C37B82` → RVA `0x00FCF6C0` (`CACHEALI`; read)
- `0x00C37BBA` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00C37BF8` → RVA `0x00F234E8` (`.data`; read)
- `0x00C37D6D` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00C37EE7` → RVA `0x00FC50A8` (`ALMOSTRO`; read)
- `0x00C38026` → RVA `0x00C388C0` (`KiNodeCostSort`; read)
- `0x00C38068` → RVA `0x00F234E0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **17**
  - `0x00C37B46` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C37B78` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C37BE7` → [HvlQueryNumaDistance](../../text/58/HvlQueryNumaDistance_function_00584A00.md) (`INIT` → `.text`)
  - `0x00C37C43` → [KeIsEmptyGroupMask](../../text/25/KeIsEmptyGroupMask_function_002553B0.md) (`INIT` → `.text`)
  - `0x00C37C75` → [KeIsEmptyGroupMask](../../text/25/KeIsEmptyGroupMask_function_002553B0.md) (`INIT` → `.text`)
  - `0x00C37CAC` → [KeGetNodePrimarySubNode](../../text/43/KeGetNodePrimarySubNode_function_0043EFF4.md) (`INIT` → `.text`)
  - `0x00C37CBC` → [KiQuerySubNodeActiveAffinity](../../text/43/KiQuerySubNodeActiveAffinity_function_0043F060.md) (`INIT` → `.text`)
  - `0x00C37CED` → [KeSetSystemGroupAffinityThread](../../text/39/KeSetSystemGroupAffinityThread_function_00399140.md) (`INIT` → `.text`)
  - `0x00C37D2C` → [MmAllocateNodePagesForMdlEx](../../text/3E/MmAllocateNodePagesForMdlEx_function_003EA920.md) (`INIT` → `.text`)
  - `0x00C37D54` → [MmMapLockedPagesSpecifyCache](../../text/31/MmMapLockedPagesSpecifyCache_function_00318800.md) (`INIT` → `.text`)
  - `0x00C37D7B` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (`INIT` → `.text`)
  - `0x00C37DBE` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (`INIT` → `.text`)
  - `0x00C37DFA` → [MiFreePagesFromMdl](../../text/3F/MiFreePagesFromMdl_function_003F8300.md) (`INIT` → `.text`)
  - `0x00C37E04` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C37E45` → [KeRevertToUserGroupAffinityThread](../../text/39/KeRevertToUserGroupAffinityThread_function_00398EC0.md) (`INIT` → `.text`)
  - `0x00C38041` → [qsort](../../text/50/qsort_function_005009F0.md) (`INIT` → `.text`)
  - `0x00C380A1` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C37AD4  48 8B C4                        mov rax, rsp
00C37AD7  48 89 58 08                     mov qword ptr [rax + 8], rbx
00C37ADB  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
00C37ADF  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
00C37AE3  55                              push rbp
00C37AE4  41 54                           push r12
00C37AE6  41 55                           push r13
00C37AE8  41 56                           push r14
00C37AEA  41 57                           push r15
00C37AEC  48 8D A8 48 FC FF FF            lea rbp, [rax - 0x3b8]
00C37AF3  48 81 EC 90 04 00 00            sub rsp, 0x490
00C37AFA  48 8B 05 3F 2C 1D 00            mov rax, qword ptr [rip + 0x1d2c3f]
00C37B01  48 33 C4                        xor rax, rsp
00C37B04  48 89 85 80 03 00 00            mov qword ptr [rbp + 0x380], rax
00C37B0B  0F B7 05 EE D4 38 00            movzx eax, word ptr [rip + 0x38d4ee]
00C37B12  33 DB                           xor ebx, ebx
00C37B14  0F 57 C0                        xorps xmm0, xmm0
00C37B17  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
00C37B1C  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
00C37B21  44 8D 6B 01                     lea r13d, [rbx + 1]
00C37B25  66 41 3B C5                     cmp ax, r13w
00C37B29  0F 86 65 05 00 00               jbe 0x140c38094
00C37B2F  8B F0                           mov esi, eax
00C37B31  8D 4B 40                        lea ecx, [rbx + 0x40]
00C37B34  0F AF F6                        imul esi, esi
00C37B37  41 B8 4B 65 4E 63               mov r8d, 0x634e654b
00C37B3D  8B FE                           mov edi, esi
00C37B3F  48 8D 14 B6                     lea rdx, [rsi + rsi*4]
00C37B43  48 03 D2                        add rdx, rdx
00C37B46  E8 A5 A5 F4 FF                  call 0x140b820f0
00C37B4B  48 89 05 96 B9 2E 00            mov qword ptr [rip + 0x2eb996], rax
00C37B52  48 8B C8                        mov rcx, rax
00C37B55  48 85 C0                        test rax, rax
00C37B58  0F 84 39 05 00 00               je 0x140c38097
00C37B5E  48 8D 04 F0                     lea rax, [rax + rsi*8]
00C37B62  48 89 05 77 B9 2E 00            mov qword ptr [rip + 0x2eb977], rax
00C37B69  85 F6                           test esi, esi
00C37B6B  74 10                           je 0x140c37b7d
00C37B6D  48 C1 E7 03                     shl rdi, 3
00C37B71  48 83 CA FF                     or rdx, 0xffffffffffffffff
00C37B75  4C 8B C7                        mov r8, rdi
00C37B78  E8 C3 F0 A8 FF                  call 0x1406c6c40
00C37B7D  83 4C 24 50 FF                  or dword ptr [rsp + 0x50], 0xffffffff
00C37B82  4C 8D 35 37 7B 39 00            lea r14, [rip + 0x397b37]
00C37B89  83 4C 24 54 FF                  or dword ptr [rsp + 0x54], 0xffffffff
00C37B8E  0F 57 C0                        xorps xmm0, xmm0
00C37B91  0F B7 0D 68 D4 38 00            movzx ecx, word ptr [rip + 0x38d468]
00C37B98  44 8B E3                        mov r12d, ebx
00C37B9B  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00C37B9F  8B F3                           mov esi, ebx
00C37BA1  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
00C37BA5  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
00C37BAA  66 3B D9                        cmp bx, cx
00C37BAD  0F 83 97 02 00 00               jae 0x140c37e4a
00C37BB3  EB 05                           jmp 0x140c37bba
00C37BB5  44 8B 64 24 40                  mov r12d, dword ptr [rsp + 0x40]
00C37BBA  F7 05 F4 EE 38 00 00 08 00 00   test dword ptr [rip + 0x38eef4], 0x800
00C37BC4  8B C6                           mov eax, esi
00C37BC6  49 8B 3C C6                     mov rdi, qword ptr [r14 + rax*8]
00C37BCA  74 66                           je 0x140c37c32
00C37BCC  8B FB                           mov edi, ebx
00C37BCE  66 3B D9                        cmp bx, cx
00C37BD1  0F 83 50 02 00 00               jae 0x140c37e27
00C37BD7  4C 8D 44 24 48                  lea r8, [rsp + 0x48]
00C37BDC  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
00C37BE1  0F B7 D7                        movzx edx, di
00C37BE4  0F B7 CE                        movzx ecx, si
00C37BE7  E8 14 CE 94 FF                  call 0x140584a00
00C37BEC  0F B7 0D 0D D4 38 00            movzx ecx, word ptr [rip + 0x38d40d]
00C37BF3  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
00C37BF8  48 8B 05 E9 B8 2E 00            mov rax, qword ptr [rip + 0x2eb8e9]
00C37BFF  0F AF CE                        imul ecx, esi
00C37C02  48 83 FA FF                     cmp rdx, -1
00C37C06  74 10                           je 0x140c37c18
00C37C08  48 C1 E2 09                     shl rdx, 9
00C37C0C  48 C1 EA 0A                     shr rdx, 0xa
00C37C10  03 CF                           add ecx, edi
00C37C12  48 89 14 C8                     mov qword ptr [rax + rcx*8], rdx
00C37C16  EB 07                           jmp 0x140c37c1f
00C37C18  03 CF                           add ecx, edi
00C37C1A  48 83 0C C8 FF                  or qword ptr [rax + rcx*8], 0xffffffffffffffff
00C37C1F  0F B7 0D DA D3 38 00            movzx ecx, word ptr [rip + 0x38d3da]
00C37C26  41 03 FD                        add edi, r13d
00C37C29  3B F9                           cmp edi, ecx
00C37C2B  72 AA                           jb 0x140c37bd7
00C37C2D  E9 F5 01 00 00                  jmp 0x140c37e27
00C37C32  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
00C37C36  66 39 07                        cmp word ptr [rdi], ax
00C37C39  0F 85 E8 01 00 00               jne 0x140c37e27
00C37C3F  48 8D 4F 10                     lea rcx, [rdi + 0x10]
00C37C43  E8 68 D7 61 FF                  call 0x1402553b0
00C37C48  85 C0                           test eax, eax
00C37C4A  74 5A                           je 0x140c37ca6
00C37C4C  66 3B 1D AD D3 38 00            cmp bx, word ptr [rip + 0x38d3ad]
00C37C53  44 8B F3                        mov r14d, ebx
00C37C56  44 0F B7 3F                     movzx r15d, word ptr [rdi]
00C37C5A  73 38                           jae 0x140c37c94
00C37C5C  48 8D 0D 5D 7A 39 00            lea rcx, [rip + 0x397a5d]
00C37C63  41 8B C6                        mov eax, r14d
00C37C66  48 8B 3C C1                     mov rdi, qword ptr [rcx + rax*8]
00C37C6A  66 44 39 7F 02                  cmp word ptr [rdi + 2], r15w
00C37C6F  75 14                           jne 0x140c37c85
00C37C71  48 8D 4F 10                     lea rcx, [rdi + 0x10]
00C37C75  E8 36 D7 61 FF                  call 0x1402553b0
00C37C7A  85 C0                           test eax, eax
00C37C7C  74 16                           je 0x140c37c94
00C37C7E  48 8D 0D 3B 7A 39 00            lea rcx, [rip + 0x397a3b]
00C37C85  0F B7 05 74 D3 38 00            movzx eax, word ptr [rip + 0x38d374]
00C37C8C  45 03 F5                        add r14d, r13d
00C37C8F  44 3B F0                        cmp r14d, eax
00C37C92  72 CF                           jb 0x140c37c63
00C37C94  0F B7 0D 65 D3 38 00            movzx ecx, word ptr [rip + 0x38d365]
00C37C9B  44 3B F1                        cmp r14d, ecx
00C37C9E  0F 84 7C 01 00 00               je 0x140c37e20
00C37CA4  EB 03                           jmp 0x140c37ca9
00C37CA6  44 8B F6                        mov r14d, esi
00C37CA9  48 8B CF                        mov rcx, rdi
00C37CAC  E8 43 73 80 FF                  call 0x14043eff4
00C37CB1  45 33 C0                        xor r8d, r8d
00C37CB4  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00C37CB9  48 8B C8                        mov rcx, rax
00C37CBC  E8 9F 73 80 FF                  call 0x14043f060
00C37CC1  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00C37CC6  48 8D 41 FF                     lea rax, [rcx - 1]
00C37CCA  48 33 C1                        xor rax, rcx
00C37CCD  48 23 C8                        and rcx, rax
00C37CD0  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
00C37CD5  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00C37CDA  45 85 E4                        test r12d, r12d
00C37CDD  75 0C                           jne 0x140c37ceb
00C37CDF  44 89 6C 24 40                  mov dword ptr [rsp + 0x40], r13d
00C37CE4  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
00C37CE9  EB 02                           jmp 0x140c37ced
00C37CEB  33 D2                           xor edx, edx
00C37CED  E8 4E 14 76 FF                  call 0x140399140
00C37CF2  0F B7 0D 07 D3 38 00            movzx ecx, word ptr [rip + 0x38d307]
00C37CF9  44 8B FB                        mov r15d, ebx
00C37CFC  66 3B D9                        cmp bx, cx
00C37CFF  0F 83 1B 01 00 00               jae 0x140c37e20
00C37D05  BE 02 00 00 00                  mov esi, 2
00C37D0A  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
00C37D0F  41 B9 00 10 00 00               mov r9d, 0x1000
00C37D15  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00C37D1D  4C 8B C3                        mov r8, rbx
00C37D20  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
00C37D25  48 8B CB                        mov rcx, rbx
00C37D28  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00C37D2C  E8 EF 2B 7B FF                  call 0x1403ea920
00C37D31  4C 8B E0                        mov r12, rax
00C37D34  48 85 C0                        test rax, rax
00C37D37  0F 84 CC 00 00 00               je 0x140c37e09
00C37D3D  C7 44 24 28 20 00 00 40         mov dword ptr [rsp + 0x28], 0x40000020
00C37D45  45 33 C9                        xor r9d, r9d
00C37D48  45 33 C0                        xor r8d, r8d
00C37D4B  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00C37D4F  33 D2                           xor edx, edx
00C37D51  48 8B C8                        mov rcx, rax
00C37D54  E8 A7 0A 6E FF                  call 0x140318800
00C37D59  48 8B F8                        mov rdi, rax
00C37D5C  48 85 C0                        test rax, rax
00C37D5F  0F 84 8A 00 00 00               je 0x140c37def
00C37D65  45 0F 20 C5                     mov r13, cr8
00C37D69  44 0F 22 C6                     mov cr8, rsi
00C37D6D  39 1D AD EF 38 00               cmp dword ptr [rip + 0x38efad], ebx
00C37D73  74 0B                           je 0x140c37d80
00C37D75  40 8A D6                        mov dl, sil
00C37D78  41 8A CD                        mov cl, r13b
00C37D7B  E8 7C D9 8B FF                  call 0x1404f56fc
00C37D80  0F 31                           rdtsc
00C37D82  48 C1 E2 20                     shl rdx, 0x20
00C37D86  48 0B C2                        or rax, rdx
00C37D89  48 8D 97 00 10 00 00            lea rdx, [rdi + 0x1000]
00C37D90  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00C37D95  EB 07                           jmp 0x140c37d9e
00C37D97  48 8B 0F                        mov rcx, qword ptr [rdi]
00C37D9A  48 83 C7 08                     add rdi, 8
00C37D9E  48 3B FA                        cmp rdi, rdx
00C37DA1  72 F4                           jb 0x140c37d97
00C37DA3  0F 31                           rdtsc
00C37DA5  48 C1 E2 20                     shl rdx, 0x20
00C37DA9  48 0B C2                        or rax, rdx
00C37DAC  39 1D 6E EF 38 00               cmp dword ptr [rip + 0x38ef6e], ebx
00C37DB2  48 8B F8                        mov rdi, rax
00C37DB5  74 0C                           je 0x140c37dc3
00C37DB7  44 0F 20 C1                     mov rcx, cr8
00C37DBB  41 8A D5                        mov dl, r13b
00C37DBE  E8 D5 D8 8B FF                  call 0x1404f5698
00C37DC3  41 0F B6 CD                     movzx ecx, r13b
00C37DC7  44 0F 22 C1                     mov cr8, rcx
00C37DCB  0F B7 0D 2E D2 38 00            movzx ecx, word ptr [rip + 0x38d22e]
00C37DD2  41 BD 01 00 00 00               mov r13d, 1
00C37DD8  48 2B 7C 24 58                  sub rdi, qword ptr [rsp + 0x58]
00C37DDD  48 8B 05 04 B7 2E 00            mov rax, qword ptr [rip + 0x2eb704]
00C37DE4  41 0F AF CE                     imul ecx, r14d
00C37DE8  41 03 CF                        add ecx, r15d
00C37DEB  48 89 3C C8                     mov qword ptr [rax + rcx*8], rdi
00C37DEF  45 33 C9                        xor r9d, r9d
00C37DF2  45 33 C0                        xor r8d, r8d
00C37DF5  33 D2                           xor edx, edx
00C37DF7  49 8B CC                        mov rcx, r12
00C37DFA  E8 01 05 7C FF                  call 0x1403f8300
00C37DFF  33 D2                           xor edx, edx
00C37E01  49 8B CC                        mov rcx, r12
00C37E04  E8 67 AA F4 FF                  call 0x140b82870
00C37E09  0F B7 0D F0 D1 38 00            movzx ecx, word ptr [rip + 0x38d1f0]
00C37E10  45 03 FD                        add r15d, r13d
00C37E13  44 3B F9                        cmp r15d, ecx
00C37E16  0F 82 EE FE FF FF               jb 0x140c37d0a
00C37E1C  8B 74 24 48                     mov esi, dword ptr [rsp + 0x48]
00C37E20  4C 8D 35 99 78 39 00            lea r14, [rip + 0x397899]
00C37E27  41 03 F5                        add esi, r13d
00C37E2A  0F B7 C1                        movzx eax, cx
00C37E2D  89 74 24 48                     mov dword ptr [rsp + 0x48], esi
00C37E31  3B F0                           cmp esi, eax
00C37E33  0F 82 7C FD FF FF               jb 0x140c37bb5
00C37E39  44 39 6C 24 40                  cmp dword ptr [rsp + 0x40], r13d
00C37E3E  75 0A                           jne 0x140c37e4a
00C37E40  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00C37E45  E8 76 10 76 FF                  call 0x140398ec0
00C37E4A  0F B7 15 AF D1 38 00            movzx edx, word ptr [rip + 0x38d1af]
00C37E51  44 8B C3                        mov r8d, ebx
00C37E54  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
00C37E59  8B FB                           mov edi, ebx
00C37E5B  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
00C37E5F  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00C37E63  66 3B DA                        cmp bx, dx
00C37E66  0F 83 4A 01 00 00               jae 0x140c37fb6
00C37E6C  8B C7                           mov eax, edi
00C37E6E  49 8B 0C C6                     mov rcx, qword ptr [r14 + rax*8]
00C37E72  0F B7 01                        movzx eax, word ptr [rcx]
00C37E75  66 3B 41 02                     cmp ax, word ptr [rcx + 2]
00C37E79  0F 85 25 01 00 00               jne 0x140c37fa4
00C37E7F  44 8B E8                        mov r13d, eax
00C37E82  44 8B FB                        mov r15d, ebx
00C37E85  0F B7 C2                        movzx eax, dx
00C37E88  44 0F AF E8                     imul r13d, eax
00C37E8C  66 3B DA                        cmp bx, dx
00C37E8F  0F 83 09 01 00 00               jae 0x140c37f9e
00C37E95  48 8B F9                        mov rdi, rcx
00C37E98  41 8B C7                        mov eax, r15d
00C37E9B  49 8B 0C C6                     mov rcx, qword ptr [r14 + rax*8]
00C37E9F  0F B7 31                        movzx esi, word ptr [rcx]
00C37EA2  66 3B 71 02                     cmp si, word ptr [rcx + 2]
00C37EA6  0F 85 DB 00 00 00               jne 0x140c37f87
00C37EAC  4C 8B 25 35 B6 2E 00            mov r12, qword ptr [rip + 0x2eb635]
00C37EB3  42 8D 04 2E                     lea eax, [rsi + r13]
00C37EB7  44 8B CE                        mov r9d, esi
00C37EBA  49 83 3C C4 FF                  cmp qword ptr [r12 + rax*8], -1
00C37EBF  0F 85 C2 00 00 00               jne 0x140c37f87
00C37EC5  44 0F B7 37                     movzx r14d, word ptr [rdi]
00C37EC9  44 0F B7 DA                     movzx r11d, dx
00C37ECD  45 0F AF D9                     imul r11d, r9d
00C37ED1  45 03 DE                        add r11d, r14d
00C37ED4  4F 8B 14 DC                     mov r10, qword ptr [r12 + r11*8]
00C37ED8  49 83 FA FF                     cmp r10, -1
00C37EDC  74 09                           je 0x140c37ee7
00C37EDE  4D 89 14 C4                     mov qword ptr [r12 + rax*8], r10
00C37EE2  E9 99 00 00 00                  jmp 0x140c37f80
00C37EE7  48 8B 0D BA D1 38 00            mov rcx, qword ptr [rip + 0x38d1ba]
00C37EEE  0F B7 C2                        movzx eax, dx
00C37EF1  41 0F AF C6                     imul eax, r14d
00C37EF5  41 03 C1                        add eax, r9d
00C37EF8  48 98                           cdqe
00C37EFA  44 8B 34 81                     mov r14d, dword ptr [rcx + rax*4]
00C37EFE  41 83 FE 01                     cmp r14d, 1
00C37F02  75 0D                           jne 0x140c37f11
00C37F04  49 63 C3                        movsxd rax, r11d
00C37F07  44 8B 34 81                     mov r14d, dword ptr [rcx + rax*4]
00C37F0B  41 83 FE 01                     cmp r14d, 1
00C37F0F  74 6F                           je 0x140c37f80
00C37F11  45 85 C0                        test r8d, r8d
00C37F14  75 19                           jne 0x140c37f2f
00C37F16  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00C37F1B  E8 60 03 00 00                  call 0x140c38280
00C37F20  44 8B 44 24 48                  mov r8d, dword ptr [rsp + 0x48]
00C37F25  4C 8B C8                        mov r9, rax
00C37F28  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00C37F2D  EB 05                           jmp 0x140c37f34
00C37F2F  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
00C37F34  41 83 F8 02                     cmp r8d, 2
00C37F38  75 23                           jne 0x140c37f5d
00C37F3A  41 8B CE                        mov ecx, r14d
00C37F3D  48 B8 15 AE 47 E1 7A 14 AE 47   movabs rax, 0x47ae147ae147ae15
00C37F47  49 0F AF C9                     imul rcx, r9
00C37F4B  48 F7 E1                        mul rcx
00C37F4E  48 2B CA                        sub rcx, rdx
00C37F51  48 D1 E9                        shr rcx, 1
00C37F54  48 03 CA                        add rcx, rdx
00C37F57  48 C1 E9 06                     shr rcx, 6
00C37F5B  EB 1B                           jmp 0x140c37f78
00C37F5D  41 83 F8 03                     cmp r8d, 3
00C37F61  75 11                           jne 0x140c37f74
00C37F63  41 8B C6                        mov eax, r14d
00C37F66  33 D2                           xor edx, edx
00C37F68  48 6B C0 64                     imul rax, rax, 0x64
00C37F6C  49 F7 F1                        div r9
00C37F6F  48 8B C8                        mov rcx, rax
00C37F72  EB 04                           jmp 0x140c37f78
00C37F74  48 83 C9 FF                     or rcx, 0xffffffffffffffff
00C37F78  42 8D 04 2E                     lea eax, [rsi + r13]
00C37F7C  49 89 0C C4                     mov qword ptr [r12 + rax*8], rcx
00C37F80  4C 8D 35 39 77 39 00            lea r14, [rip + 0x397739]
00C37F87  0F B7 15 72 D0 38 00            movzx edx, word ptr [rip + 0x38d072]
00C37F8E  41 FF C7                        inc r15d
00C37F91  44 3B FA                        cmp r15d, edx
00C37F94  0F 82 FE FE FF FF               jb 0x140c37e98
00C37F9A  8B 7C 24 40                     mov edi, dword ptr [rsp + 0x40]
00C37F9E  41 BD 01 00 00 00               mov r13d, 1
00C37FA4  41 03 FD                        add edi, r13d
00C37FA7  0F B7 C2                        movzx eax, dx
00C37FAA  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
00C37FAE  3B F8                           cmp edi, eax
00C37FB0  0F 82 B6 FE FF FF               jb 0x140c37e6c
00C37FB6  8B FB                           mov edi, ebx
00C37FB8  66 3B DA                        cmp bx, dx
00C37FBB  0F 83 D3 00 00 00               jae 0x140c38094
00C37FC1  44 0F B7 CA                     movzx r9d, dx
00C37FC5  8B C7                           mov eax, edi
00C37FC7  44 8B D3                        mov r10d, ebx
00C37FCA  49 8B 04 C6                     mov rax, qword ptr [r14 + rax*8]
00C37FCE  0F B7 70 02                     movzx esi, word ptr [rax + 2]
00C37FD2  41 0F AF F1                     imul esi, r9d
00C37FD6  45 85 C9                        test r9d, r9d
00C37FD9  74 44                           je 0x140c3801f
00C37FDB  4C 8D 45 88                     lea r8, [rbp - 0x78]
00C37FDF  4D 8B DE                        mov r11, r14
00C37FE2  49 8B 03                        mov rax, qword ptr [r11]
00C37FE5  45 89 50 F8                     mov dword ptr [r8 - 8], r10d
00C37FE9  48 85 C0                        test rax, rax
00C37FEC  74 1D                           je 0x140c3800b
00C37FEE  0F B7 08                        movzx ecx, word ptr [rax]
00C37FF1  48 8B 05 F0 B4 2E 00            mov rax, qword ptr [rip + 0x2eb4f0]
00C37FF8  03 CE                           add ecx, esi
00C37FFA  48 8B 14 C8                     mov rdx, qword ptr [rax + rcx*8]
00C37FFE  49 89 10                        mov qword ptr [r8], rdx
00C38001  48 85 D2                        test rdx, rdx
00C38004  75 09                           jne 0x140c3800f
00C38006  4D 89 28                        mov qword ptr [r8], r13
00C38009  EB 04                           jmp 0x140c3800f
00C3800B  49 83 08 FF                     or qword ptr [r8], 0xffffffffffffffff
00C3800F  45 03 D5                        add r10d, r13d
00C38012  49 83 C3 08                     add r11, 8
00C38016  49 83 C0 10                     add r8, 0x10
00C3801A  45 3B D1                        cmp r10d, r9d
00C3801D  72 C3                           jb 0x140c37fe2
00C3801F  0F B7 15 DA CF 38 00            movzx edx, word ptr [rip + 0x38cfda]
00C38026  4C 8D 0D 93 08 00 00            lea r9, [rip + 0x893]
00C3802D  8B C7                           mov eax, edi
00C3802F  48 8D 4D 80                     lea rcx, [rbp - 0x80]
00C38033  48 03 C0                        add rax, rax
00C38036  41 B8 10 00 00 00               mov r8d, 0x10
00C3803C  48 89 5C C5 88                  mov qword ptr [rbp + rax*8 - 0x78], rbx
00C38041  E8 AA 89 8C FF                  call 0x1405009f0
00C38046  0F B7 15 B3 CF 38 00            movzx edx, word ptr [rip + 0x38cfb3]
00C3804D  44 8B C3                        mov r8d, ebx
00C38050  8B C2                           mov eax, edx
00C38052  85 D2                           test edx, edx
00C38054  74 2E                           je 0x140c38084
00C38056  0F AF C7                        imul eax, edi
00C38059  41 8B C8                        mov ecx, r8d
00C3805C  48 03 C9                        add rcx, rcx
00C3805F  0F B7 4C CD 80                  movzx ecx, word ptr [rbp + rcx*8 - 0x80]
00C38064  41 8D 14 00                     lea edx, [r8 + rax]
00C38068  48 8B 05 71 B4 2E 00            mov rax, qword ptr [rip + 0x2eb471]
00C3806F  45 03 C5                        add r8d, r13d
00C38072  66 89 0C 50                     mov word ptr [rax + rdx*2], cx
00C38076  0F B7 15 83 CF 38 00            movzx edx, word ptr [rip + 0x38cf83]
00C3807D  8B C2                           mov eax, edx
00C3807F  44 3B C2                        cmp r8d, edx
00C38082  72 D2                           jb 0x140c38056
00C38084  41 03 FD                        add edi, r13d
00C38087  44 0F B7 CA                     movzx r9d, dx
00C3808B  41 3B F9                        cmp edi, r9d
00C3808E  0F 82 31 FF FF FF               jb 0x140c37fc5
00C38094  41 8A C5                        mov al, r13b
00C38097  48 8B 8D 80 03 00 00            mov rcx, qword ptr [rbp + 0x380]
00C3809E  48 33 CC                        xor rcx, rsp
00C380A1  E8 9A 45 A7 FF                  call 0x1406ac640
00C380A6  4C 8D 9C 24 90 04 00 00         lea r11, [rsp + 0x490]
00C380AE  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00C380B2  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00C380B6  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00C380BA  49 8B E3                        mov rsp, r11
00C380BD  41 5F                           pop r15
00C380BF  41 5E                           pop r14
00C380C1  41 5D                           pop r13
00C380C3  41 5C                           pop r12
00C380C5  5D                              pop rbp
00C380C6  C3                              ret
00C380C7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiComputeNumaCosts(void)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m448;
    unsigned __int64 v_stack_m458;
    unsigned __int64 v_stack_m460;
    unsigned int v_stack_m464;
    unsigned __int64 v_stack_m468;
    unsigned int v_stack_m470;
    unsigned int v_stack_m478;
    unsigned int v_stack_m488;
    unsigned int v_stack_m490;
    unsigned int v_stack_m498;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (0x490ULL);
    result = (*(unsigned __int64 *)(v_rip + 1911871)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 952 + 896) = result;
    v_rbx = 0;
    v_stack_m468 = 0;
    v_stack_m448 = v_xmm0;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rip + 3724526))) <= ((unsigned __int16)(v_rbx + 1))) goto loc_00C38094;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 3724526)))) * ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 3724526))))));
    a2 = (v_rsi + v_rsi * 4) + (v_rsi + v_rsi * 4);
    result = ExAllocatePool2(v_rbx + 64, a2, (unsigned int)(0x634E654BULL), a4);
    *(unsigned __int64 *)(v_rip + 3062166) = result;
    if (result == 0) goto loc_00C38097;
    *(unsigned __int64 *)(v_rip + 3062135) = result + v_rsi * 8;
    result = result + v_rsi * 8;
    v_rdi = (unsigned int)((unsigned int)(v_rsi));
    if ((unsigned int)(v_rsi) != 0) {
        v_rdi = ((unsigned int)((unsigned int)(v_rsi))) << (3);
        a2 = (a2) | (-1);
        a3 = v_rdi;
        result = memset(result, a2, a3, a4);
    }
    v_stack_m478 = 0;
    v_stack_m470 = 0;
    v_stack_m458 = v_xmm0;
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 3724392)))) goto loc_00C37E4A;
    goto loc_00C37BBA;
loc_00C37BB5:
loc_00C37BBA:
    if (((*(unsigned int *)(v_rip + 3731188)) & (0x800ULL)) == 0) goto loc_00C37C32;
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 3724392)))) goto loc_00C37E27;
loc_00C37BD7:
    v_stack_m470 = 0;
    result = HvlQueryNumaDistance(0, 0, v_stack_m470, a4);
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rip + 3724301)) * (0));
    if (v_stack_m470 == -1) goto loc_00C37C18;
    a2 = (v_stack_m470) << (9);
    a2 = (a2) >> (10);
    a1 = (unsigned int)((a1) + (0));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3061993) + a1 * 8) = a2;
    goto loc_00C37C1F;
loc_00C37C18:
    a1 = (unsigned int)((a1) + (0));
loc_00C37C1F:
    v_rdi = (unsigned int)((0) + ((unsigned int)(v_rbx + 1)));
    if (((unsigned int)(v_rdi)) < ((unsigned int)(*(unsigned __int16 *)(v_rip + 3724250)))) goto loc_00C37BD7;
    goto loc_00C37E27;
loc_00C37C32:
    if ((*(unsigned __int16 *)(v_rdi)) != ((unsigned __int16)(*(unsigned __int16 *)(v_rdi + 2)))) goto loc_00C37E27;
    result = KeIsEmptyGroupMask(v_rdi + 16, a2, v_stack_m470, a4);
    if ((unsigned int)(result) == 0) goto loc_00C37CA6;
    if (0 >= (*(unsigned __int16 *)(v_rip + 3724205))) goto loc_00C37C94;
loc_00C37C63:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3766877 + 0 * 8) + 2)) != ((unsigned __int16)(*(unsigned __int16 *)(v_rdi)))) goto loc_00C37C85;
    result = KeIsEmptyGroupMask(*(unsigned __int64 *)(v_rip + 3766877 + 0 * 8) + 16, a2, v_stack_m470, a4);
    if ((unsigned int)(result) == 0) goto loc_00C37C94;
loc_00C37C85:
    v_r14 = (unsigned int)((0) + ((unsigned int)(v_rbx + 1)));
    if (((unsigned int)(v_r14)) < ((unsigned int)(*(unsigned __int16 *)(v_rip + 3724148)))) goto loc_00C37C63;
loc_00C37C94:
    if (((unsigned int)(v_r14)) == ((unsigned int)(*(unsigned __int16 *)(v_rip + 3724133)))) goto loc_00C37E20;
    goto loc_00C37CA9;
loc_00C37CA6:
loc_00C37CA9:
    result = KeGetNodePrimarySubNode(*(unsigned __int64 *)(v_rip + 3766877 + 0 * 8), a2, v_stack_m470, a4);
    a3 = 0;
    result = KiQuerySubNodeActiveAffinity(result, v_stack_m458, a3, a4);
    result = (v_stack_m458 - 1) ^ (v_stack_m458);
    a1 = (v_stack_m458) & (result);
    v_stack_m458 = a1;
    if ((unsigned int)((unsigned int)(v_stack_m478)) != 0) goto loc_00C37CEB;
    v_stack_m478 = (unsigned int)(v_rbx + 1);
    goto loc_00C37CED;
loc_00C37CEB:
    a2 = 0;
loc_00C37CED:
    result = KeSetSystemGroupAffinityThread(v_stack_m458, a2, a3, a4);
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 3724039)))) goto loc_00C37E20;
loc_00C37D0A:
    v_stack_m488 = 7;
    v_stack_m490 = 0;
    v_stack_m498 = 0;
    result = MmAllocateNodePagesForMdlEx(0, v_stack_m468, 0, (unsigned int)(0x1000ULL));
    if (result == 0) goto loc_00C37E09;
    v_stack_m490 = 0x40000020ULL;
    a4 = 0;
    a3 = 0;
    v_stack_m498 = 0;
    a2 = 0;
    result = MmMapLockedPagesSpecifyCache(result, a2, a3, a4);
    if (result == 0) goto loc_00C37DEF;
    if ((*(unsigned int *)(v_rip + 3731373)) != 0) {
        a2 = 2;
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    a2 = (a2) << (32);
    result = (result) | (a2);
    v_stack_m460 = result;
    goto loc_00C37D9E;
loc_00C37D97:
    v_rdi = (result) + (8);
loc_00C37D9E:
    if (v_rdi < (result + 4096)) goto loc_00C37D97;
    a2 = (result + 4096) << (32);
    result = (result) | (a2);
    if ((*(unsigned int *)(v_rip + 3731310)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    v_rdi = (result) - (v_stack_m460);
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rip + 3723822)) * (0));
    a1 = (unsigned int)((a1) + (0));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3061508) + a1 * 8) = v_rdi;
loc_00C37DEF:
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = MiFreePagesFromMdl(result, a2, a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
loc_00C37E09:
    v_r15 = (unsigned int)((0) + (1));
    if (((unsigned int)(v_r15)) < ((unsigned int)(*(unsigned __int16 *)(v_rip + 3723760)))) goto loc_00C37D0A;
loc_00C37E20:
loc_00C37E27:
    v_rsi = (unsigned int)(((unsigned int)(v_stack_m470)) + (1));
    v_stack_m470 = (unsigned int)(v_rsi);
    if (((unsigned int)(v_rsi)) < ((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(v_rip + 3723760))))) goto loc_00C37BB5;
    result = (unsigned __int16)(*(unsigned __int16 *)(v_rip + 3723760));
    if (v_stack_m478 == 1) {
        a1 = v_stack_m448;
        result = KeRevertToUserGroupAffinityThread(a1, a2, a3, a4);
    }
    v_stack_m468 = 0;
    v_stack_m470 = 0;
    v_stack_m478 = 0;
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 3723695)))) goto loc_00C37FB6;
loc_00C37E6C:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3766425 + 0 * 8)))) != (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3766425 + 0 * 8) + 2))) goto loc_00C37FA4;
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3766425 + 0 * 8))))) * ((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(v_rip + 3723695)))));
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 3723695)))) goto loc_00C37F9E;
loc_00C37E98:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3766425 + 0 * 8)))) != (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3766425 + 0 * 8) + 2))) goto loc_00C37F87;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3061301) + *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3766425 + 0 * 8)) + v_r13 * 1 * 8)) != -1) goto loc_00C37F87;
    v_r11 = (unsigned int)(((unsigned __int16)(*(unsigned __int16 *)(v_rip + 3723695))) * ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3766425 + 0 * 8)))))));
    v_r11 = (unsigned int)((v_r11) + ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3766425 + 0 * 8)))));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3061301) + v_r11 * 8)) == -1) goto loc_00C37EE7;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3061301) + *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3766425 + 0 * 8)) + v_r13 * 1 * 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3061301) + v_r11 * 8);
    goto loc_00C37F80;
loc_00C37EE7:
    result = (unsigned int)(((unsigned __int16)(*(unsigned __int16 *)(v_rip + 3723695))) * ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3766425 + 0 * 8)))));
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3766425 + 0 * 8)))))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3723706) + result * 4)))) != 1) goto loc_00C37F11;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3723706) + (int)((unsigned int)(v_r11)) * 4)))) == 1) goto loc_00C37F80;
loc_00C37F11:
    if (0 != 0) goto loc_00C37F2F;
    result = KiGetHalNumaConversionFactor(v_stack_m470, *(unsigned __int16 *)(v_rip + 3723695), 0, (unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3766425 + 0 * 8)))));
    v_stack_m468 = result;
    goto loc_00C37F34;
loc_00C37F2F:
loc_00C37F34:
    if (((unsigned int)((unsigned int)(v_stack_m470))) != 2) goto loc_00C37F5D;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3723706) + (int)((unsigned int)(v_r11)) * 4))))) * (v_stack_m468);
    a1 = (a1) - (*(unsigned __int16 *)(v_rip + 3723695));
    a1 = (a1) >> (1);
    a1 = (a1) + (*(unsigned __int16 *)(v_rip + 3723695));
    a1 = (a1) >> (6);
    goto loc_00C37F78;
loc_00C37F5D:
    if (((unsigned int)((unsigned int)(v_stack_m470))) != 3) goto loc_00C37F74;
    a2 = 0;
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3723706) + (int)((unsigned int)(v_r11)) * 4))))) * ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3723706) + (int)((unsigned int)(v_r11)) * 4)))));
    goto loc_00C37F78;
loc_00C37F74:
    a1 = (result) | (-1);
loc_00C37F78:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3061301) + *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3766425 + 0 * 8)) + v_r13 * 1 * 8) = a1;
loc_00C37F80:
loc_00C37F87:
    v_r15 = (unsigned int)((0) + 1);
    if (((unsigned int)(v_r15)) < ((unsigned int)(*(unsigned __int16 *)(v_rip + 3723378)))) goto loc_00C37E98;
loc_00C37F9E:
loc_00C37FA4:
    v_rdi = (unsigned int)(((unsigned int)(v_stack_m478)) + (1));
    v_stack_m478 = (unsigned int)(v_rdi);
    if (((unsigned int)(v_rdi)) < ((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(v_rip + 3723378))))) goto loc_00C37E6C;
loc_00C37FB6:
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 3723378)))) goto loc_00C38094;
loc_00C37FC5:
    v_rsi = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3766073 + 0 * 8) + 2)) * ((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(v_rip + 3723378)))));
    if ((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(v_rip + 3723378))) == 0) goto loc_00C3801F;
loc_00C37FE2:
    *(unsigned int *)(v_rsp - 952 - 120 - 8) = 0;
    if (*(unsigned __int64 *)(v_rip + 3766073) == 0) goto loc_00C3800B;
    a1 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3766073))) + ((unsigned int)(v_rsi)));
    *(unsigned __int64 *)(v_rsp - 952 - 120) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3060976) + a1 * 8);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3060976) + a1 * 8) != 0) goto loc_00C3800F;
    *(unsigned __int64 *)(v_rsp - 952 - 120) = 1;
    goto loc_00C3800F;
loc_00C3800B:
loc_00C3800F:
    v_r10 = (unsigned int)((0) + (1));
    v_r11 = (v_rip + 3766073) + (8);
    a3 = (v_rsp - 952 - 120) + (16);
    if (((unsigned int)(v_r10)) < ((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(v_rip + 3723378))))) goto loc_00C37FE2;
loc_00C3801F:
    result = (0) + (0);
    *(unsigned __int64 *)(v_rsp - 952 + result * 8 - 120) = 0;
    result = qsort(v_rsp - 952 - 128, *(unsigned __int16 *)(v_rip + 3723226), 16, v_rip + 2195);
    if ((unsigned int)(*(unsigned __int16 *)(v_rip + 3723187)) == 0) goto loc_00C38084;
loc_00C38056:
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 3723187)))) * (0));
    a1 = (0) + (0);
    a3 = (unsigned int)((0) + (1));
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3060849) + 0 + result * 1 * 2) = (unsigned __int16)(*(unsigned __int16 *)(v_rsp - 952 + a1 * 8 - 128));
    if (((unsigned int)(a3)) < ((unsigned int)(*(unsigned __int16 *)(v_rip + 3723139)))) goto loc_00C38056;
loc_00C38084:
    v_rdi = (unsigned int)((0) + (1));
    if (((unsigned int)(v_rdi)) < ((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(v_rip + 3723139))))) goto loc_00C37FC5;
loc_00C38094:
loc_00C38097:
    a1 = (*(unsigned __int64 *)(v_rsp - 952 + 896)) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int16 *)(v_rip + 3723139), a3, (unsigned __int16)(*(unsigned __int16 *)(v_rip + 3723139)));
    return result;
}
```

## 5. (Beta) C Style

```c
void KiComputeNumaCosts(void)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m448;
    uint64_t v_stack_m458;
    uint64_t v_stack_m460;
    uint32_t v_stack_m464;
    uint64_t v_stack_m468;
    uint32_t v_stack_m470;
    uint32_t v_stack_m478;
    uint32_t v_stack_m488;
    uint32_t v_stack_m490;
    uint32_t v_stack_m498;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (0x490ULL);
    result = (*(uint64_t *)(v_rip + 0x1D2C3F)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x3B8 + 0x380) = result;
    local_rbx = 0;
    v_stack_m468 = 0;
    v_stack_m448 = v_xmm0;
    if (((uint16_t)(*(uint16_t *)(v_rip + 0x38D4EE))) <= ((uint16_t)(local_rbx + 1))) goto loc_00C38094;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0x38D4EE)))) * ((uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0x38D4EE))))));
    a2 = (local_rsi + local_rsi * 4) + (local_rsi + local_rsi * 4);
    result = ExAllocatePool2(local_rbx + 64, a2, (uint32_t)(0x634E654BULL), a4);
    *(uint64_t *)(v_rip + 0x2EB996) = result;
    if (result == 0) goto loc_00C38097;
    *(uint64_t *)(v_rip + 0x2EB977) = result + local_rsi * 8;
    result = result + local_rsi * 8;
    local_rdi = (uint32_t)((uint32_t)(local_rsi));
    if ((uint32_t)(local_rsi) != 0) {
        local_rdi = ((uint32_t)((uint32_t)(local_rsi))) << (3);
        a2 = (a2) | (-1);
        a3 = local_rdi;
        result = memset(result, a2, a3, a4);
    }
    v_stack_m478 = 0;
    v_stack_m470 = 0;
    v_stack_m458 = v_xmm0;
    if (0 >= ((uint16_t)(*(uint16_t *)(v_rip + 0x38D468)))) goto loc_00C37E4A;
    goto loc_00C37BBA;
loc_00C37BB5:
loc_00C37BBA:
    if (((*(uint32_t *)(v_rip + 0x38EEF4)) & (0x800ULL)) == 0) goto loc_00C37C32;
    if (0 >= ((uint16_t)(*(uint16_t *)(v_rip + 0x38D468)))) goto loc_00C37E27;
loc_00C37BD7:
    v_stack_m470 = 0;
    result = HvlQueryNumaDistance(0, 0, v_stack_m470, a4);
    a1 = (uint32_t)((*(uint16_t *)(v_rip + 0x38D40D)) * (0));
    if (v_stack_m470 == -1) goto loc_00C37C18;
    a2 = (v_stack_m470) << (9);
    a2 = (a2) >> (10);
    a1 = (uint32_t)((a1) + (0));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x2EB8E9) + a1 * 8) = a2;
    goto loc_00C37C1F;
loc_00C37C18:
    a1 = (uint32_t)((a1) + (0));
loc_00C37C1F:
    local_rdi = (uint32_t)((0) + ((uint32_t)(local_rbx + 1)));
    if (((uint32_t)(local_rdi)) < ((uint32_t)(*(uint16_t *)(v_rip + 0x38D3DA)))) goto loc_00C37BD7;
    goto loc_00C37E27;
loc_00C37C32:
    if ((*(uint16_t *)(local_rdi)) != ((uint16_t)(*(uint16_t *)(local_rdi + 0x2)))) goto loc_00C37E27;
    result = KeIsEmptyGroupMask(local_rdi + 16, a2, v_stack_m470, a4);
    if ((uint32_t)(result) == 0) goto loc_00C37CA6;
    if (0 >= (*(uint16_t *)(v_rip + 0x38D3AD))) goto loc_00C37C94;
loc_00C37C63:
    if ((*(uint16_t *)(*(uint64_t *)(v_rip + 0x397A5D + 0x0 * 8) + 0x2)) != ((uint16_t)(*(uint16_t *)(local_rdi)))) goto loc_00C37C85;
    result = KeIsEmptyGroupMask(*(uint64_t *)(v_rip + 0x397A5D + 0x0 * 8) + 16, a2, v_stack_m470, a4);
    if ((uint32_t)(result) == 0) goto loc_00C37C94;
loc_00C37C85:
    local_r14 = (uint32_t)((0) + ((uint32_t)(local_rbx + 1)));
    if (((uint32_t)(local_r14)) < ((uint32_t)(*(uint16_t *)(v_rip + 0x38D374)))) goto loc_00C37C63;
loc_00C37C94:
    if (((uint32_t)(local_r14)) == ((uint32_t)(*(uint16_t *)(v_rip + 0x38D365)))) goto loc_00C37E20;
    goto loc_00C37CA9;
loc_00C37CA6:
loc_00C37CA9:
    result = KeGetNodePrimarySubNode(*(uint64_t *)(v_rip + 0x397A5D + 0x0 * 8), a2, v_stack_m470, a4);
    a3 = 0;
    result = KiQuerySubNodeActiveAffinity(result, v_stack_m458, a3, a4);
    result = (v_stack_m458 - 1) ^ (v_stack_m458);
    a1 = (v_stack_m458) & (result);
    v_stack_m458 = a1;
    if ((uint32_t)((uint32_t)(v_stack_m478)) != 0) goto loc_00C37CEB;
    v_stack_m478 = (uint32_t)(local_rbx + 1);
    goto loc_00C37CED;
loc_00C37CEB:
    a2 = 0;
loc_00C37CED:
    result = KeSetSystemGroupAffinityThread(v_stack_m458, a2, a3, a4);
    if (0 >= ((uint16_t)(*(uint16_t *)(v_rip + 0x38D307)))) goto loc_00C37E20;
loc_00C37D0A:
    v_stack_m488 = 7;
    v_stack_m490 = 0;
    v_stack_m498 = 0;
    result = MmAllocateNodePagesForMdlEx(0, v_stack_m468, 0, (uint32_t)(0x1000ULL));
    if (result == 0) goto loc_00C37E09;
    v_stack_m490 = 0x40000020ULL;
    a4 = 0;
    a3 = 0;
    v_stack_m498 = 0;
    a2 = 0;
    result = MmMapLockedPagesSpecifyCache(result, a2, a3, a4);
    if (result == 0) goto loc_00C37DEF;
    if ((*(uint32_t *)(v_rip + 0x38EFAD)) != 0) {
        a2 = 2;
        a1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    a2 = (a2) << (32);
    result = (result) | (a2);
    v_stack_m460 = result;
    goto loc_00C37D9E;
loc_00C37D97:
    local_rdi = (result) + (8);
loc_00C37D9E:
    if (local_rdi < (result + 4096)) goto loc_00C37D97;
    a2 = (result + 4096) << (32);
    result = (result) | (a2);
    if ((*(uint32_t *)(v_rip + 0x38EF6E)) != 0) {
        a1 = 2;
        a2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    local_rdi = (result) - (v_stack_m460);
    a1 = (uint32_t)((*(uint16_t *)(v_rip + 0x38D22E)) * (0));
    a1 = (uint32_t)((a1) + (0));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x2EB704) + a1 * 8) = local_rdi;
loc_00C37DEF:
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = MiFreePagesFromMdl(result, a2, a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
loc_00C37E09:
    local_r15 = (uint32_t)((0) + (1));
    if (((uint32_t)(local_r15)) < ((uint32_t)(*(uint16_t *)(v_rip + 0x38D1F0)))) goto loc_00C37D0A;
loc_00C37E20:
loc_00C37E27:
    local_rsi = (uint32_t)(((uint32_t)(v_stack_m470)) + (1));
    v_stack_m470 = (uint32_t)(local_rsi);
    if (((uint32_t)(local_rsi)) < ((uint32_t)((uint16_t)(*(uint16_t *)(v_rip + 0x38D1F0))))) goto loc_00C37BB5;
    result = (uint16_t)(*(uint16_t *)(v_rip + 0x38D1F0));
    if (v_stack_m478 == 1) {
        a1 = v_stack_m448;
        result = KeRevertToUserGroupAffinityThread(a1, a2, a3, a4);
    }
    v_stack_m468 = 0;
    v_stack_m470 = 0;
    v_stack_m478 = 0;
    if (0 >= ((uint16_t)(*(uint16_t *)(v_rip + 0x38D1AF)))) goto loc_00C37FB6;
loc_00C37E6C:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x397899 + 0x0 * 8)))) != (*(uint16_t *)(*(uint64_t *)(v_rip + 0x397899 + 0x0 * 8) + 0x2))) goto loc_00C37FA4;
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x397899 + 0x0 * 8))))) * ((uint32_t)((uint16_t)(*(uint16_t *)(v_rip + 0x38D1AF)))));
    if (0 >= ((uint16_t)(*(uint16_t *)(v_rip + 0x38D1AF)))) goto loc_00C37F9E;
loc_00C37E98:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x397899 + 0x0 * 8)))) != (*(uint16_t *)(*(uint64_t *)(v_rip + 0x397899 + 0x0 * 8) + 0x2))) goto loc_00C37F87;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x2EB635) + *(uint16_t *)(*(uint64_t *)(v_rip + 0x397899 + 0x0 * 8)) + local_r13 * 1 * 8)) != -1) goto loc_00C37F87;
    local_r11 = (uint32_t)(((uint16_t)(*(uint16_t *)(v_rip + 0x38D1AF))) * ((uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x397899 + 0x0 * 8)))))));
    local_r11 = (uint32_t)((local_r11) + ((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x397899 + 0x0 * 8)))));
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x2EB635) + local_r11 * 8)) == -1) goto loc_00C37EE7;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x2EB635) + *(uint16_t *)(*(uint64_t *)(v_rip + 0x397899 + 0x0 * 8)) + local_r13 * 1 * 8) = *(uint64_t *)(*(uint64_t *)(v_rip + 0x2EB635) + local_r11 * 8);
    goto loc_00C37F80;
loc_00C37EE7:
    result = (uint32_t)(((uint16_t)(*(uint16_t *)(v_rip + 0x38D1AF))) * ((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x397899 + 0x0 * 8)))));
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x397899 + 0x0 * 8)))))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x38D1BA) + result * 4)))) != 1) goto loc_00C37F11;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x38D1BA) + (int32_t)((uint32_t)(local_r11)) * 4)))) == 1) goto loc_00C37F80;
loc_00C37F11:
    if (0 != 0) goto loc_00C37F2F;
    result = KiGetHalNumaConversionFactor(v_stack_m470, *(uint16_t *)(v_rip + 0x38D1AF), 0, (uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x397899 + 0x0 * 8)))));
    v_stack_m468 = result;
    goto loc_00C37F34;
loc_00C37F2F:
loc_00C37F34:
    if (((uint32_t)((uint32_t)(v_stack_m470))) != 2) goto loc_00C37F5D;
    a1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x38D1BA) + (int32_t)((uint32_t)(local_r11)) * 4))))) * (v_stack_m468);
    a1 = (a1) - (*(uint16_t *)(v_rip + 0x38D1AF));
    a1 = (a1) >> (1);
    a1 = (a1) + (*(uint16_t *)(v_rip + 0x38D1AF));
    a1 = (a1) >> (6);
    goto loc_00C37F78;
loc_00C37F5D:
    if (((uint32_t)((uint32_t)(v_stack_m470))) != 3) goto loc_00C37F74;
    a2 = 0;
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x38D1BA) + (int32_t)((uint32_t)(local_r11)) * 4))))) * ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x38D1BA) + (int32_t)((uint32_t)(local_r11)) * 4)))));
    goto loc_00C37F78;
loc_00C37F74:
    a1 = (result) | (-1);
loc_00C37F78:
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x2EB635) + *(uint16_t *)(*(uint64_t *)(v_rip + 0x397899 + 0x0 * 8)) + local_r13 * 1 * 8) = a1;
loc_00C37F80:
loc_00C37F87:
    local_r15 = (uint32_t)((0) + 1);
    if (((uint32_t)(local_r15)) < ((uint32_t)(*(uint16_t *)(v_rip + 0x38D072)))) goto loc_00C37E98;
loc_00C37F9E:
loc_00C37FA4:
    local_rdi = (uint32_t)(((uint32_t)(v_stack_m478)) + (1));
    v_stack_m478 = (uint32_t)(local_rdi);
    if (((uint32_t)(local_rdi)) < ((uint32_t)((uint16_t)(*(uint16_t *)(v_rip + 0x38D072))))) goto loc_00C37E6C;
loc_00C37FB6:
    if (0 >= ((uint16_t)(*(uint16_t *)(v_rip + 0x38D072)))) goto loc_00C38094;
loc_00C37FC5:
    local_rsi = (uint32_t)((*(uint16_t *)(*(uint64_t *)(v_rip + 0x397739 + 0x0 * 8) + 0x2)) * ((uint32_t)((uint16_t)(*(uint16_t *)(v_rip + 0x38D072)))));
    if ((uint32_t)((uint16_t)(*(uint16_t *)(v_rip + 0x38D072))) == 0) goto loc_00C3801F;
loc_00C37FE2:
    *(uint32_t *)(local_rsp - 0x3B8 - 0x78 - 0x8) = 0;
    if (*(uint64_t *)(v_rip + 0x397739) == 0) goto loc_00C3800B;
    a1 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(v_rip + 0x397739))) + ((uint32_t)(local_rsi)));
    *(uint64_t *)(local_rsp - 0x3B8 - 0x78) = *(uint64_t *)(*(uint64_t *)(v_rip + 0x2EB4F0) + a1 * 8);
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x2EB4F0) + a1 * 8) != 0) goto loc_00C3800F;
    *(uint64_t *)(local_rsp - 0x3B8 - 0x78) = 1;
    goto loc_00C3800F;
loc_00C3800B:
loc_00C3800F:
    local_r10 = (uint32_t)((0) + (1));
    local_r11 = (v_rip + 3766073) + (8);
    a3 = (local_rsp - 952 - 120) + (16);
    if (((uint32_t)(local_r10)) < ((uint32_t)((uint16_t)(*(uint16_t *)(v_rip + 0x38D072))))) goto loc_00C37FE2;
loc_00C3801F:
    result = (0) + (0);
    *(uint64_t *)(local_rsp - 0x3B8 + result * 8 - 0x78) = 0;
    result = qsort(local_rsp - 952 - 128, *(uint16_t *)(v_rip + 0x38CFDA), 16, v_rip + 2195);
    if ((uint32_t)(*(uint16_t *)(v_rip + 0x38CFB3)) == 0) goto loc_00C38084;
loc_00C38056:
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0x38CFB3)))) * (0));
    a1 = (0) + (0);
    a3 = (uint32_t)((0) + (1));
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x2EB471) + 0x0 + result * 1 * 2) = (uint16_t)(*(uint16_t *)(local_rsp - 0x3B8 + a1 * 8 - 0x80));
    if (((uint32_t)(a3)) < ((uint32_t)(*(uint16_t *)(v_rip + 0x38CF83)))) goto loc_00C38056;
loc_00C38084:
    local_rdi = (uint32_t)((0) + (1));
    if (((uint32_t)(local_rdi)) < ((uint32_t)((uint16_t)(*(uint16_t *)(v_rip + 0x38CF83))))) goto loc_00C37FC5;
loc_00C38094:
loc_00C38097:
    a1 = (*(uint64_t *)(local_rsp - 0x3B8 + 0x380)) ^ (local_rsp);
    result = _security_check_cookie(a1, *(uint16_t *)(v_rip + 0x38CF83), a3, (uint16_t)(*(uint16_t *)(v_rip + 0x38CF83)));
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C37AD4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
