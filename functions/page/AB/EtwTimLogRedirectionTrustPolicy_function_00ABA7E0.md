# EtwTimLogRedirectionTrustPolicy

- RVA: `0x00ABA7E0`–`0x00ABB331` (길이 `2,897` bytes)
- VA: `0x0000000140ABA7E0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD3E0`
- 디코드: `628`개 명령, `2,897/2,897` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x00ABA865` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00ABA89F` → [RtlWalkFrameChain](../../text/2F/RtlWalkFrameChain_function_002F85E0.md) (function, `0x002F85E0`)
- `0x00ABA8F1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00ABA914` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ABA979` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00ABA9A7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00ABA9BA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00ABAA10` → [ZwQueryVirtualMemory](../../text/6A/ZwQueryVirtualMemory_function_006AD530.md) (function, `0x006AD530`)
- `0x00ABAA67` → [RtlStringCbCopyW](../../text/43/RtlStringCbCopyW_function_0043B910.md) (function, `0x0043B910`)
- `0x00ABAA73` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00ABAA95` → [ZwQueryVirtualMemory](../../text/6A/ZwQueryVirtualMemory_function_006AD530.md) (function, `0x006AD530`)
- `0x00ABAB0A` → [EtwpQueryProcessCommandLine](../8A/EtwpQueryProcessCommandLine_function_008A5C20.md) (function, `0x008A5C20`)
- `0x00ABAB23` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00ABAB48` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00ABAB6C` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00ABAC61` → [EtwpTiFillProcessIdentity](../../text/3B/EtwpTiFillProcessIdentity_function_003B8F30.md) (function, `0x003B8F30`)
- `0x00ABAE87` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x00ABAEB9` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00ABB1E9` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00ABB2CC` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00ABB2DF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ABB2F2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ABB301` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ABB310` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [IoCheckRedirectionTrustLevel](../../text/48/IoCheckRedirectionTrustLevel_function_00485BB0.md) at `0x00485CCE`

### Static image references
- `0x00ABA804` → RVA `0x00E0A740` (`.data`; read)
- `0x00ABA96D` → RVA `0x00AFE5E0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00ABAAC5` → RVA `0x00022160` (`.rdata`; read)
- `0x00ABAAD5` → RVA `0x00020D40` (`.rdata`; read)
- `0x00ABAAE1` → RVA `0x00002F28` (`.rdata`; read)
- `0x00ABAB75` → RVA `0x00B076E0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00ABAE75` → RVA `0x00EFF828` (`.data`; read)
- `0x00ABAE9B` → RVA `0x00E09168` (`.data`; read)
- `0x00ABB171` → RVA `0x00055090` (`.rdata`; read)
- `0x00ABB20B` → RVA `0x000553B5` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **23**
  - `0x00ABA865` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00ABA89F` → [RtlWalkFrameChain](../../text/2F/RtlWalkFrameChain_function_002F85E0.md) (`PAGE` → `.text`)
  - `0x00ABA8F1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00ABA914` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00ABA979` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00ABA9A7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00ABA9BA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00ABAA10` → [ZwQueryVirtualMemory](../../text/6A/ZwQueryVirtualMemory_function_006AD530.md) (`PAGE` → `.text`)
  - `0x00ABAA67` → [RtlStringCbCopyW](../../text/43/RtlStringCbCopyW_function_0043B910.md) (`PAGE` → `.text`)
  - `0x00ABAA73` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00ABAA95` → [ZwQueryVirtualMemory](../../text/6A/ZwQueryVirtualMemory_function_006AD530.md) (`PAGE` → `.text`)
  - `0x00ABAB23` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00ABAB48` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00ABAB6C` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00ABAC61` → [EtwpTiFillProcessIdentity](../../text/3B/EtwpTiFillProcessIdentity_function_003B8F30.md) (`PAGE` → `.text`)
  - `0x00ABAE87` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x00ABAEB9` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x00ABB1E9` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x00ABB2CC` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x00ABB2DF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00ABB2F2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00ABB301` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00ABB310` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ABA7E0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00ABA7E5  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00ABA7EA  55                              push rbp
00ABA7EB  56                              push rsi
00ABA7EC  57                              push rdi
00ABA7ED  41 54                           push r12
00ABA7EF  41 55                           push r13
00ABA7F1  41 56                           push r14
00ABA7F3  41 57                           push r15
00ABA7F5  48 8D AC 24 70 FA FF FF         lea rbp, [rsp - 0x590]
00ABA7FD  48 81 EC 90 06 00 00            sub rsp, 0x690
00ABA804  48 8B 05 35 FF 34 00            mov rax, qword ptr [rip + 0x34ff35]
00ABA80B  48 33 C4                        xor rax, rsp
00ABA80E  48 89 85 80 05 00 00            mov qword ptr [rbp + 0x580], rax
00ABA815  0F 57 C0                        xorps xmm0, xmm0
00ABA818  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
00ABA81D  33 F6                           xor esi, esi
00ABA81F  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00ABA823  4C 8B EA                        mov r13, rdx
00ABA826  48 89 75 A0                     mov qword ptr [rbp - 0x60], rsi
00ABA82A  0F 57 C9                        xorps xmm1, xmm1
00ABA82D  66 89 74 24 34                  mov word ptr [rsp + 0x34], si
00ABA832  33 D2                           xor edx, edx
00ABA834  66 89 74 24 38                  mov word ptr [rsp + 0x38], si
00ABA839  48 8D 8D 20 02 00 00            lea rcx, [rbp + 0x220]
00ABA840  66 89 74 24 3C                  mov word ptr [rsp + 0x3c], si
00ABA845  41 B8 80 00 00 00               mov r8d, 0x80
00ABA84B  4C 89 4C 24 70                  mov qword ptr [rsp + 0x70], r9
00ABA850  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
00ABA854  0F 11 4C 24 50                  movups xmmword ptr [rsp + 0x50], xmm1
00ABA859  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00ABA85D  0F 11 45 F8                     movups xmmword ptr [rbp - 8], xmm0
00ABA861  0F 11 45 08                     movups xmmword ptr [rbp + 8], xmm0
00ABA865  E8 D6 C3 C0 FF                  call 0x1406c6c40
00ABA86A  0F B6 85 F0 05 00 00            movzx eax, byte ptr [rbp + 0x5f0]
00ABA871  8D 56 10                        lea edx, [rsi + 0x10]
00ABA874  4D 8B BD B0 07 00 00            mov r15, qword ptr [r13 + 0x7b0]
00ABA87B  48 8D 8D 20 02 00 00            lea rcx, [rbp + 0x220]
00ABA882  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00ABA886  8B DE                           mov ebx, esi
00ABA888  8D 46 01                        lea eax, [rsi + 1]
00ABA88B  40 88 74 24 30                  mov byte ptr [rsp + 0x30], sil
00ABA890  44 8B C0                        mov r8d, eax
00ABA893  48 89 75 80                     mov qword ptr [rbp - 0x80], rsi
00ABA897  8B FE                           mov edi, esi
00ABA899  44 8A E0                        mov r12b, al
00ABA89C  44 8B F6                        mov r14d, esi
00ABA89F  E8 3C DD 83 FF                  call 0x1402f85e0
00ABA8A4  44 8D 43 01                     lea r8d, [rbx + 1]
00ABA8A8  8B F0                           mov esi, eax
00ABA8AA  41 0F B7 C8                     movzx ecx, r8w
00ABA8AE  44 8D 4B 07                     lea r9d, [rbx + 7]
00ABA8B2  41 8B D1                        mov edx, r9d
00ABA8B5  66 41 3B F1                     cmp si, r9w
00ABA8B9  77 03                           ja 0x140aba8be
00ABA8BB  0F B7 D6                        movzx edx, si
00ABA8BE  0F B7 C1                        movzx eax, cx
00ABA8C1  3B C2                           cmp eax, edx
00ABA8C3  73 10                           jae 0x140aba8d5
00ABA8C5  0F B7 C1                        movzx eax, cx
00ABA8C8  03 BC C5 20 02 00 00            add edi, dword ptr [rbp + rax*8 + 0x220]
00ABA8CF  66 41 03 C8                     add cx, r8w
00ABA8D3  EB DD                           jmp 0x140aba8b2
00ABA8D5  33 D2                           xor edx, edx
00ABA8D7  85 FF                           test edi, edi
00ABA8D9  41 0F 44 F8                     cmove edi, r8d
00ABA8DD  4D 85 FF                        test r15, r15
00ABA8E0  75 44                           jne 0x140aba926
00ABA8E2  41 8D 57 28                     lea edx, [r15 + 0x28]
00ABA8E6  B9 00 01 00 00                  mov ecx, 0x100
00ABA8EB  41 B8 54 49 73 6E               mov r8d, 0x6e734954
00ABA8F1  E8 FA 77 0C 00                  call 0x140b820f0
00ABA8F6  33 D2                           xor edx, edx
00ABA8F8  48 8B C8                        mov rcx, rax
00ABA8FB  48 85 C0                        test rax, rax
00ABA8FE  0F 84 02 0A 00 00               je 0x140abb306
00ABA904  33 C0                           xor eax, eax
00ABA906  F0 49 0F B1 8D B0 07 00 00      lock cmpxchg qword ptr [r13 + 0x7b0], rcx
00ABA90F  4C 8B F8                        mov r15, rax
00ABA912  74 09                           je 0x140aba91d
00ABA914  E8 57 7F 0C 00                  call 0x140b82870
00ABA919  33 D2                           xor edx, edx
00ABA91B  EB 03                           jmp 0x140aba920
00ABA91D  4C 8B F9                        mov r15, rcx
00ABA920  41 B8 01 00 00 00               mov r8d, 1
00ABA926  41 83 FE 0A                     cmp r14d, 0xa
00ABA92A  73 1C                           jae 0x140aba948
00ABA92C  41 8B C6                        mov eax, r14d
00ABA92F  41 8B 0C 87                     mov ecx, dword ptr [r15 + rax*4]
00ABA933  85 C9                           test ecx, ecx
00ABA935  74 0D                           je 0x140aba944
00ABA937  3B CF                           cmp ecx, edi
00ABA939  0F 84 C7 09 00 00               je 0x140abb306
00ABA93F  45 03 F0                        add r14d, r8d
00ABA942  EB E2                           jmp 0x140aba926
00ABA944  41 83 FE 0A                     cmp r14d, 0xa
00ABA948  1A C0                           sbb al, al
00ABA94A  44 22 E0                        and r12b, al
00ABA94D  0F 84 B3 09 00 00               je 0x140abb306
00ABA953  49 8B 8D B0 07 00 00            mov rcx, qword ptr [r13 + 0x7b0]
00ABA95A  33 C0                           xor eax, eax
00ABA95C  41 8B D6                        mov edx, r14d
00ABA95F  F0 0F B1 3C 91                  lock cmpxchg dword ptr [rcx + rdx*4], edi
00ABA964  74 07                           je 0x140aba96d
00ABA966  33 D2                           xor edx, edx
00ABA968  E9 70 FF FF FF                  jmp 0x140aba8dd
00ABA96D  48 8D 15 6C 3C 04 00            lea rdx, [rip + 0x43c6c]
00ABA974  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00ABA979  E8 02 FE 96 FF                  call 0x14042a780
00ABA97E  45 33 E4                        xor r12d, r12d
00ABA981  66 85 F6                        test si, si
00ABA984  0F 84 3B 01 00 00               je 0x140abaac5
00ABA98A  44 0F B7 FE                     movzx r15d, si
00ABA98E  BF 54 49 73 6E                  mov edi, 0x6e734954
00ABA993  41 BE 00 01 00 00               mov r14d, 0x100
00ABA999  44 8B C7                        mov r8d, edi
00ABA99C  41 8B CE                        mov ecx, r14d
00ABA99F  4B 8D 14 BF                     lea rdx, [r15 + r15*4]
00ABA9A3  48 C1 E2 04                     shl rdx, 4
00ABA9A7  E8 44 77 0C 00                  call 0x140b820f0
00ABA9AC  44 8B C7                        mov r8d, edi
00ABA9AF  BA 1A 02 00 00                  mov edx, 0x21a
00ABA9B4  41 8B CE                        mov ecx, r14d
00ABA9B7  48 8B D8                        mov rbx, rax
00ABA9BA  E8 31 77 0C 00                  call 0x140b820f0
00ABA9BF  33 C9                           xor ecx, ecx
00ABA9C1  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00ABA9C5  4C 8B E0                        mov r12, rax
00ABA9C8  48 85 DB                        test rbx, rbx
00ABA9CB  0F 84 5D 01 00 00               je 0x140abab2e
00ABA9D1  48 85 C0                        test rax, rax
00ABA9D4  0F 84 54 01 00 00               je 0x140abab2e
00ABA9DA  66 3B CE                        cmp cx, si
00ABA9DD  0F 83 DF 00 00 00               jae 0x140abaac2
00ABA9E3  48 8D BD 20 02 00 00            lea rdi, [rbp + 0x220]
00ABA9EA  4C 8D 73 10                     lea r14, [rbx + 0x10]
00ABA9EE  44 8D 69 01                     lea r13d, [rcx + 1]
00ABA9F2  48 8B 17                        mov rdx, qword ptr [rdi]
00ABA9F5  4D 8B CC                        mov r9, r12
00ABA9F8  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00ABA9FD  41 B8 02 00 00 00               mov r8d, 2
00ABAA03  48 83 C9 FF                     or rcx, 0xffffffffffffffff
00ABAA07  48 C7 44 24 20 18 02 00 00      mov qword ptr [rsp + 0x20], 0x218
00ABAA10  E8 1B 2B BF FF                  call 0x1406ad530
00ABAA15  33 C9                           xor ecx, ecx
00ABAA17  85 C0                           test eax, eax
00ABAA19  0F 88 8A 00 00 00               js 0x140abaaa9
00ABAA1F  41 0F B7 14 24                  movzx edx, word ptr [r12]
00ABAA24  66 41 3B D5                     cmp dx, r13w
00ABAA28  76 7F                           jbe 0x140abaaa9
00ABAA2A  66 D1 EA                        shr dx, 1
00ABAA2D  66 41 2B D5                     sub dx, r13w
00ABAA31  66 85 D2                        test dx, dx
00ABAA34  74 1D                           je 0x140abaa53
00ABAA36  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
00ABAA3B  0F B7 CA                        movzx ecx, dx
00ABAA3E  66 83 3C 48 5C                  cmp word ptr [rax + rcx*2], 0x5c
00ABAA43  74 0A                           je 0x140abaa4f
00ABAA45  B8 FF FF 00 00                  mov eax, 0xffff
00ABAA4A  66 03 D0                        add dx, ax
00ABAA4D  EB E2                           jmp 0x140abaa31
00ABAA4F  66 41 03 D5                     add dx, r13w
00ABAA53  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
00ABAA58  0F B7 CA                        movzx ecx, dx
00ABAA5B  BA 40 00 00 00                  mov edx, 0x40
00ABAA60  4C 8D 04 48                     lea r8, [rax + rcx*2]
00ABAA64  49 8B CE                        mov rcx, r14
00ABAA67  E8 A4 0E 98 FF                  call 0x14043b910
00ABAA6C  49 8D 4E F0                     lea rcx, [r14 - 0x10]
00ABAA70  49 8B D6                        mov rdx, r14
00ABAA73  E8 08 FD 96 FF                  call 0x14042a780
00ABAA78  48 8B 17                        mov rdx, qword ptr [rdi]
00ABAA7B  4C 8D 4D E8                     lea r9, [rbp - 0x18]
00ABAA7F  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00ABAA85  45 33 C0                        xor r8d, r8d
00ABAA88  48 83 C9 FF                     or rcx, 0xffffffffffffffff
00ABAA8C  48 C7 44 24 20 30 00 00 00      mov qword ptr [rsp + 0x20], 0x30
00ABAA95  E8 96 2A BF FF                  call 0x1406ad530
00ABAA9A  33 C9                           xor ecx, ecx
00ABAA9C  85 C0                           test eax, eax
00ABAA9E  78 09                           js 0x140abaaa9
00ABAAA0  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
00ABAAA4  48 29 07                        sub qword ptr [rdi], rax
00ABAAA7  EB 03                           jmp 0x140abaaac
00ABAAA9  48 89 0F                        mov qword ptr [rdi], rcx
00ABAAAC  49 83 C6 50                     add r14, 0x50
00ABAAB0  48 83 C7 08                     add rdi, 8
00ABAAB4  4D 2B FD                        sub r15, r13
00ABAAB7  0F 85 35 FF FF FF               jne 0x140aba9f2
00ABAABD  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
00ABAAC2  45 33 E4                        xor r12d, r12d
00ABAAC5  48 8D 0D 94 76 56 FF            lea rcx, [rip - 0xa9896c]
00ABAACC  0F 57 C0                        xorps xmm0, xmm0
00ABAACF  41 BF 01 00 00 00               mov r15d, 1
00ABAAD5  48 8D 05 64 62 56 FF            lea rax, [rip - 0xa99d9c]
00ABAADC  44 39 7C 24 40                  cmp dword ptr [rsp + 0x40], r15d
00ABAAE1  4C 8D 35 40 84 54 FF            lea r14, [rip - 0xab7bc0]
00ABAAE8  48 8D 55 88                     lea rdx, [rbp - 0x78]
00ABAAEC  48 0F 45 C1                     cmovne rax, rcx
00ABAAF0  49 8B CD                        mov rcx, r13
00ABAAF3  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00ABAAF8  49 8B 85 50 03 00 00            mov rax, qword ptr [r13 + 0x350]
00ABAAFF  48 85 C0                        test rax, rax
00ABAB02  0F 11 45 88                     movups xmmword ptr [rbp - 0x78], xmm0
00ABAB06  4C 0F 45 F0                     cmovne r14, rax
00ABAB0A  E8 11 B1 DE FF                  call 0x1408a5c20
00ABAB0F  0F B7 7D 88                     movzx edi, word ptr [rbp - 0x78]
00ABAB13  66 85 FF                        test di, di
00ABAB16  75 3A                           jne 0x140abab52
00ABAB18  48 8D 15 C1 3A 04 00            lea rdx, [rip + 0x43ac1]
00ABAB1F  48 8D 4D 88                     lea rcx, [rbp - 0x78]
00ABAB23  E8 58 FC 96 FF                  call 0x14042a780
00ABAB28  0F B7 7D 88                     movzx edi, word ptr [rbp - 0x78]
00ABAB2C  EB 29                           jmp 0x140abab57
00ABAB2E  45 33 E4                        xor r12d, r12d
00ABAB31  66 44 3B E6                     cmp r12w, si
00ABAB35  73 8E                           jae 0x140abaac5
00ABAB37  44 0F B7 C6                     movzx r8d, si
00ABAB3B  48 8D 8D 20 02 00 00            lea rcx, [rbp + 0x220]
00ABAB42  49 C1 E0 03                     shl r8, 3
00ABAB46  33 D2                           xor edx, edx
00ABAB48  E8 F3 C0 C0 FF                  call 0x1406c6c40
00ABAB4D  E9 73 FF FF FF                  jmp 0x140abaac5
00ABAB52  44 88 7C 24 30                  mov byte ptr [rsp + 0x30], r15b
00ABAB57  4C 8B 54 24 70                  mov r10, qword ptr [rsp + 0x70]
00ABAB5C  4D 85 D2                        test r10, r10
00ABAB5F  75 14                           jne 0x140abab75
00ABAB61  48 8D 15 78 3A 04 00            lea rdx, [rip + 0x43a78]
00ABAB68  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00ABAB6C  E8 0F FC 96 FF                  call 0x14042a780
00ABAB71  4C 8D 55 D8                     lea r10, [rbp - 0x28]
00ABAB75  4C 8D 1D 64 CB 04 00            lea r11, [rip + 0x4cb64]
00ABAB7C  41 B8 06 00 00 00               mov r8d, 6
00ABAB82  45 8D 48 06                     lea r9d, [r8 + 6]
00ABAB86  4D 85 F6                        test r14, r14
00ABAB89  74 32                           je 0x140ababbd
00ABAB8B  41 0F B7 06                     movzx eax, word ptr [r14]
00ABAB8F  66 85 C0                        test ax, ax
00ABAB92  74 29                           je 0x140ababbd
00ABAB94  66 D1 E8                        shr ax, 1
00ABAB97  66 89 44 24 34                  mov word ptr [rsp + 0x34], ax
00ABAB9C  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00ABABA1  48 89 85 A0 02 00 00            mov qword ptr [rbp + 0x2a0], rax
00ABABA8  48 C7 85 A8 02 00 00 02 00 00 00  mov qword ptr [rbp + 0x2a8], 2
00ABABB3  41 0F B7 06                     movzx eax, word ptr [r14]
00ABABB7  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
00ABABBB  EB 23                           jmp 0x140ababe0
00ABABBD  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00ABABC2  66 44 89 44 24 34               mov word ptr [rsp + 0x34], r8w
00ABABC8  48 89 85 A0 02 00 00            mov qword ptr [rbp + 0x2a0], rax
00ABABCF  49 8B CB                        mov rcx, r11
00ABABD2  41 8B C1                        mov eax, r9d
00ABABD5  48 C7 85 A8 02 00 00 02 00 00 00  mov qword ptr [rbp + 0x2a8], 2
00ABABE0  89 85 B8 02 00 00               mov dword ptr [rbp + 0x2b8], eax
00ABABE6  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
00ABABEA  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00ABABEF  48 89 8D B0 02 00 00            mov qword ptr [rbp + 0x2b0], rcx
00ABABF6  44 89 A5 BC 02 00 00            mov dword ptr [rbp + 0x2bc], r12d
00ABABFD  48 C7 85 C8 02 00 00 02 00 00 00  mov qword ptr [rbp + 0x2c8], 2
00ABAC08  66 85 FF                        test di, di
00ABAC0B  74 1B                           je 0x140abac28
00ABAC0D  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
00ABAC12  48 89 85 D0 02 00 00            mov qword ptr [rbp + 0x2d0], rax
00ABAC19  0F B7 C7                        movzx eax, di
00ABAC1C  48 89 8D C0 02 00 00            mov qword ptr [rbp + 0x2c0], rcx
00ABAC23  66 D1 EF                        shr di, 1
00ABAC26  EB 19                           jmp 0x140abac41
00ABAC28  48 8D 44 24 38                  lea rax, [rsp + 0x38]
00ABAC2D  4C 89 9D D0 02 00 00            mov qword ptr [rbp + 0x2d0], r11
00ABAC34  48 89 85 C0 02 00 00            mov qword ptr [rbp + 0x2c0], rax
00ABAC3B  41 8B F8                        mov edi, r8d
00ABAC3E  41 8B C1                        mov eax, r9d
00ABAC41  4C 8D 45 A0                     lea r8, [rbp - 0x60]
00ABAC45  66 89 7C 24 38                  mov word ptr [rsp + 0x38], di
00ABAC4A  49 8B D5                        mov rdx, r13
00ABAC4D  89 85 D8 02 00 00               mov dword ptr [rbp + 0x2d8], eax
00ABAC53  48 8D 8D E0 02 00 00            lea rcx, [rbp + 0x2e0]
00ABAC5A  44 89 A5 DC 02 00 00            mov dword ptr [rbp + 0x2dc], r12d
00ABAC61  E8 CA E2 8F FF                  call 0x1403b8f30
00ABAC66  41 BD 04 00 00 00               mov r13d, 4
00ABAC6C  42 8D 14 28                     lea edx, [rax + r13]
00ABAC70  8B CA                           mov ecx, edx
00ABAC72  48 8D 85 E0 05 00 00            lea rax, [rbp + 0x5e0]
00ABAC79  48 03 C9                        add rcx, rcx
00ABAC7C  44 8B C2                        mov r8d, edx
00ABAC7F  41 03 D7                        add edx, r15d
00ABAC82  48 89 84 CD A0 02 00 00         mov qword ptr [rbp + rcx*8 + 0x2a0], rax
00ABAC8A  4C 89 AC CD A8 02 00 00         mov qword ptr [rbp + rcx*8 + 0x2a8], r13
00ABAC92  4D 85 D2                        test r10, r10
00ABAC95  74 1C                           je 0x140abacb3
00ABAC97  41 0F B7 0A                     movzx ecx, word ptr [r10]
00ABAC9B  66 85 C9                        test cx, cx
00ABAC9E  74 13                           je 0x140abacb3
00ABACA0  4D 8B 7A 08                     mov r15, qword ptr [r10 + 8]
00ABACA4  44 8D 42 01                     lea r8d, [rdx + 1]
00ABACA8  0F B7 C1                        movzx eax, cx
00ABACAB  44 8B C9                        mov r9d, ecx
00ABACAE  66 D1 E8                        shr ax, 1
00ABACB1  EB 0C                           jmp 0x140abacbf
00ABACB3  B8 06 00 00 00                  mov eax, 6
00ABACB8  41 83 C0 02                     add r8d, 2
00ABACBC  4D 8B FB                        mov r15, r11
00ABACBF  66 89 44 24 3C                  mov word ptr [rsp + 0x3c], ax
00ABACC4  41 8D 48 01                     lea ecx, [r8 + 1]
00ABACC8  8B C2                           mov eax, edx
00ABACCA  4C 8D B5 A0 02 00 00            lea r14, [rbp + 0x2a0]
00ABACD1  48 C1 E0 04                     shl rax, 4
00ABACD5  4C 8D 9D A0 02 00 00            lea r11, [rbp + 0x2a0]
00ABACDC  48 8B F8                        mov rdi, rax
00ABACDF  41 8B D0                        mov edx, r8d
00ABACE2  48 C1 E2 04                     shl rdx, 4
00ABACE6  4C 8D 44 24 3C                  lea r8, [rsp + 0x3c]
00ABACEB  33 FF                           xor edi, edi
00ABACED  4C 8B D2                        mov r10, rdx
00ABACF0  4D 89 04 06                     mov qword ptr [r14 + rax], r8
00ABACF4  44 8D 51 01                     lea r10d, [rcx + 1]
00ABACF8  C7 84 05 A8 02 00 00 02 00 00 00  mov dword ptr [rbp + rax + 0x2a8], 2
00ABAD03  45 89 64 06 0C                  mov dword ptr [r14 + rax + 0xc], r12d
00ABAD08  44 0F B7 F7                     movzx r14d, di
00ABAD0C  4E 89 3C 1A                     mov qword ptr [rdx + r11], r15
00ABAD10  44 89 8C 15 A8 02 00 00         mov dword ptr [rbp + rdx + 0x2a8], r9d
00ABAD18  42 89 7C 1A 0C                  mov dword ptr [rdx + r11 + 0xc], edi
00ABAD1D  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00ABAD22  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00ABAD27  4C 8B DB                        mov r11, rbx
00ABAD2A  44 0F B7 64 24 50               movzx r12d, word ptr [rsp + 0x50]
00ABAD30  8B C1                           mov eax, ecx
00ABAD32  48 03 C0                        add rax, rax
00ABAD35  4C 89 AC C5 A8 02 00 00         mov qword ptr [rbp + rax*8 + 0x2a8], r13
00ABAD3D  4C 8D AD 20 02 00 00            lea r13, [rbp + 0x220]
00ABAD44  48 89 94 C5 A0 02 00 00         mov qword ptr [rbp + rax*8 + 0x2a0], rdx
00ABAD4C  0F B7 44 24 52                  movzx eax, word ptr [rsp + 0x52]
00ABAD51  66 89 44 24 32                  mov word ptr [rsp + 0x32], ax
00ABAD56  66 44 3B F6                     cmp r14w, si
00ABAD5A  73 68                           jae 0x140abadc4
00ABAD5C  48 85 DB                        test rbx, rbx
00ABAD5F  74 63                           je 0x140abadc4
00ABAD61  4D 85 DB                        test r11, r11
00ABAD64  74 2D                           je 0x140abad93
00ABAD66  4D 8B 4B 08                     mov r9, qword ptr [r11 + 8]
00ABAD6A  4D 85 C9                        test r9, r9
00ABAD6D  74 24                           je 0x140abad93
00ABAD6F  41 0F B7 03                     movzx eax, word ptr [r11]
00ABAD73  66 85 C0                        test ax, ax
00ABAD76  74 1B                           je 0x140abad93
00ABAD78  8B D0                           mov edx, eax
00ABAD7A  45 8B C2                        mov r8d, r10d
00ABAD7D  8D 48 01                        lea ecx, [rax + 1]
00ABAD80  49 C1 E0 04                     shl r8, 4
00ABAD84  41 0F B7 43 02                  movzx eax, word ptr [r11 + 2]
00ABAD89  3B C1                           cmp eax, ecx
00ABAD8B  8D 7A 02                        lea edi, [rdx + 2]
00ABAD8E  0F 46 FA                        cmovbe edi, edx
00ABAD91  EB 13                           jmp 0x140abada6
00ABAD93  45 8B C2                        mov r8d, r10d
00ABAD96  4C 8D 0D 43 C9 04 00            lea r9, [rip + 0x4c943]
00ABAD9D  49 C1 E0 04                     shl r8, 4
00ABADA1  BF 0E 00 00 00                  mov edi, 0xe
00ABADA6  49 8B C0                        mov rax, r8
00ABADA9  48 8D 8D A0 02 00 00            lea rcx, [rbp + 0x2a0]
00ABADB0  4C 89 0C 08                     mov qword ptr [rax + rcx], r9
00ABADB4  42 89 BC 05 A8 02 00 00         mov dword ptr [rbp + r8 + 0x2a8], edi
00ABADBC  33 FF                           xor edi, edi
00ABADBE  89 7C 08 0C                     mov dword ptr [rax + rcx + 0xc], edi
00ABADC2  EB 5F                           jmp 0x140abae23
00ABADC4  4D 85 FF                        test r15, r15
00ABADC7  74 39                           je 0x140abae02
00ABADC9  66 45 85 E4                     test r12w, r12w
00ABADCD  74 33                           je 0x140abae02
00ABADCF  45 8B CA                        mov r9d, r10d
00ABADD2  41 8D 4C 24 01                  lea ecx, [r12 + 1]
00ABADD7  4D 03 C9                        add r9, r9
00ABADDA  0F B7 C0                        movzx eax, ax
00ABADDD  3B C1                           cmp eax, ecx
00ABADDF  41 8D 54 24 02                  lea edx, [r12 + 2]
00ABADE4  41 0F 46 D4                     cmovbe edx, r12d
00ABADE8  42 89 94 CD A8 02 00 00         mov dword ptr [rbp + r9*8 + 0x2a8], edx
00ABADF0  4E 89 BC CD A0 02 00 00         mov qword ptr [rbp + r9*8 + 0x2a0], r15
00ABADF8  42 89 BC CD AC 02 00 00         mov dword ptr [rbp + r9*8 + 0x2ac], edi
00ABAE00  EB 21                           jmp 0x140abae23
00ABAE02  41 8B C2                        mov eax, r10d
00ABAE05  48 8D 0D D4 C8 04 00            lea rcx, [rip + 0x4c8d4]
00ABAE0C  48 03 C0                        add rax, rax
00ABAE0F  48 89 8C C5 A0 02 00 00         mov qword ptr [rbp + rax*8 + 0x2a0], rcx
00ABAE17  48 C7 84 C5 A8 02 00 00 0E 00 00 00  mov qword ptr [rbp + rax*8 + 0x2a8], 0xe
00ABAE23  B8 01 00 00 00                  mov eax, 1
00ABAE28  66 41 FF C6                     inc r14w
00ABAE2C  49 83 C3 50                     add r11, 0x50
00ABAE30  42 8D 0C 10                     lea ecx, [rax + r10]
00ABAE34  8B C1                           mov eax, ecx
00ABAE36  44 8D 51 01                     lea r10d, [rcx + 1]
00ABAE3A  48 03 C0                        add rax, rax
00ABAE3D  4C 89 AC C5 A0 02 00 00         mov qword ptr [rbp + rax*8 + 0x2a0], r13
00ABAE45  49 83 C5 08                     add r13, 8
00ABAE49  48 C7 84 C5 A8 02 00 00 08 00 00 00  mov qword ptr [rbp + rax*8 + 0x2a8], 8
00ABAE55  B8 10 00 00 00                  mov eax, 0x10
00ABAE5A  66 44 3B F0                     cmp r14w, ax
00ABAE5E  0F B7 44 24 32                  movzx eax, word ptr [rsp + 0x32]
00ABAE63  0F 82 ED FE FF FF               jb 0x140abad56
00ABAE69  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
00ABAE6E  48 8D 85 A0 02 00 00            lea rax, [rbp + 0x2a0]
00ABAE75  48 8B 0D AC 49 44 00            mov rcx, qword ptr [rip + 0x4449ac]
00ABAE7C  45 8B CA                        mov r9d, r10d
00ABAE7F  45 33 C0                        xor r8d, r8d
00ABAE82  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00ABAE87  E8 94 18 96 FF                  call 0x14041c720
00ABAE8C  41 B8 05 00 00 00               mov r8d, 5
00ABAE92  48 85 DB                        test rbx, rbx
00ABAE95  0F 84 30 03 00 00               je 0x140abb1cb
00ABAE9B  44 39 05 C6 E2 34 00            cmp dword ptr [rip + 0x34e2c6], r8d
00ABAEA2  0F 86 29 04 00 00               jbe 0x140abb2d1
00ABAEA8  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
00ABAEB2  48 8D 0D AF E2 34 00            lea rcx, [rip + 0x34e2af]
00ABAEB9  E8 E2 3B 97 FF                  call 0x14042eaa0
00ABAEBE  84 C0                           test al, al
00ABAEC0  0F 84 0B 04 00 00               je 0x140abb2d1
00ABAEC6  48 8D 45 A8                     lea rax, [rbp - 0x58]
00ABAECA  48 C7 45 A8 00 00 00 02         mov qword ptr [rbp - 0x58], 0x2000000
00ABAED2  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
00ABAED6  45 8D 50 FF                     lea r10d, [r8 - 1]
00ABAEDA  8B 85 E0 05 00 00               mov eax, dword ptr [rbp + 0x5e0]
00ABAEE0  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00ABAEE4  48 8D 44 24 44                  lea rax, [rsp + 0x44]
00ABAEE9  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
00ABAEED  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
00ABAEF1  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00ABAEF5  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00ABAEFA  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
00ABAEFE  8A 85 F0 05 00 00               mov al, byte ptr [rbp + 0x5f0]
00ABAF04  88 44 24 32                     mov byte ptr [rsp + 0x32], al
00ABAF08  48 8D 44 24 32                  lea rax, [rsp + 0x32]
00ABAF0D  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
00ABAF11  41 8D 40 FC                     lea eax, [r8 - 4]
00ABAF15  48 C7 45 48 08 00 00 00         mov qword ptr [rbp + 0x48], 8
00ABAF1D  4C 89 55 58                     mov qword ptr [rbp + 0x58], r10
00ABAF21  4C 89 55 68                     mov qword ptr [rbp + 0x68], r10
00ABAF25  48 89 45 78                     mov qword ptr [rbp + 0x78], rax
00ABAF29  66 3B F0                        cmp si, ax
00ABAF2C  76 0A                           jbe 0x140abaf38
00ABAF2E  48 8D 4B 50                     lea rcx, [rbx + 0x50]
00ABAF32  48 39 7B 58                     cmp qword ptr [rbx + 0x58], rdi
00ABAF36  75 05                           jne 0x140abaf3d
00ABAF38  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00ABAF3D  48 8D 85 98 00 00 00            lea rax, [rbp + 0x98]
00ABAF44  89 BD 9C 00 00 00               mov dword ptr [rbp + 0x9c], edi
00ABAF4A  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
00ABAF51  BA 02 00 00 00                  mov edx, 2
00ABAF56  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00ABAF5A  48 89 85 90 00 00 00            mov qword ptr [rbp + 0x90], rax
00ABAF61  0F B7 01                        movzx eax, word ptr [rcx]
00ABAF64  89 85 98 00 00 00               mov dword ptr [rbp + 0x98], eax
00ABAF6A  48 8B 85 28 02 00 00            mov rax, qword ptr [rbp + 0x228]
00ABAF71  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
00ABAF75  48 8D 45 B0                     lea rax, [rbp - 0x50]
00ABAF79  48 89 85 A0 00 00 00            mov qword ptr [rbp + 0xa0], rax
00ABAF80  48 89 95 88 00 00 00            mov qword ptr [rbp + 0x88], rdx
00ABAF87  48 C7 85 A8 00 00 00 08 00 00 00  mov qword ptr [rbp + 0xa8], 8
00ABAF92  66 3B F2                        cmp si, dx
00ABAF95  76 10                           jbe 0x140abafa7
00ABAF97  48 8D 8B A0 00 00 00            lea rcx, [rbx + 0xa0]
00ABAF9E  48 39 BB A8 00 00 00            cmp qword ptr [rbx + 0xa8], rdi
00ABAFA5  75 05                           jne 0x140abafac
00ABAFA7  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00ABAFAC  48 89 95 B8 00 00 00            mov qword ptr [rbp + 0xb8], rdx
00ABAFB3  48 8D 85 C8 00 00 00            lea rax, [rbp + 0xc8]
00ABAFBA  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
00ABAFC1  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00ABAFC5  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
00ABAFCC  0F B7 01                        movzx eax, word ptr [rcx]
00ABAFCF  89 85 C8 00 00 00               mov dword ptr [rbp + 0xc8], eax
00ABAFD5  48 8B 85 30 02 00 00            mov rax, qword ptr [rbp + 0x230]
00ABAFDC  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
00ABAFE0  48 8D 45 B8                     lea rax, [rbp - 0x48]
00ABAFE4  48 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], rax
00ABAFEB  89 BD CC 00 00 00               mov dword ptr [rbp + 0xcc], edi
00ABAFF1  48 C7 85 D8 00 00 00 08 00 00 00  mov qword ptr [rbp + 0xd8], 8
00ABAFFC  66 83 FE 03                     cmp si, 3
00ABB000  76 10                           jbe 0x140abb012
00ABB002  48 8D 8B F0 00 00 00            lea rcx, [rbx + 0xf0]
00ABB009  48 39 BB F8 00 00 00            cmp qword ptr [rbx + 0xf8], rdi
00ABB010  75 05                           jne 0x140abb017
00ABB012  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00ABB017  48 89 95 E8 00 00 00            mov qword ptr [rbp + 0xe8], rdx
00ABB01E  48 8D 85 F8 00 00 00            lea rax, [rbp + 0xf8]
00ABB025  48 89 85 E0 00 00 00            mov qword ptr [rbp + 0xe0], rax
00ABB02C  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00ABB030  48 89 85 F0 00 00 00            mov qword ptr [rbp + 0xf0], rax
00ABB037  0F B7 01                        movzx eax, word ptr [rcx]
00ABB03A  89 85 F8 00 00 00               mov dword ptr [rbp + 0xf8], eax
00ABB040  48 8B 85 38 02 00 00            mov rax, qword ptr [rbp + 0x238]
00ABB047  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00ABB04B  48 8D 45 C0                     lea rax, [rbp - 0x40]
00ABB04F  48 89 85 00 01 00 00            mov qword ptr [rbp + 0x100], rax
00ABB056  89 BD FC 00 00 00               mov dword ptr [rbp + 0xfc], edi
00ABB05C  48 C7 85 08 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x108], 8
00ABB067  66 41 3B F2                     cmp si, r10w
00ABB06B  76 10                           jbe 0x140abb07d
00ABB06D  48 8D 8B 40 01 00 00            lea rcx, [rbx + 0x140]
00ABB074  48 39 BB 48 01 00 00            cmp qword ptr [rbx + 0x148], rdi
00ABB07B  75 05                           jne 0x140abb082
00ABB07D  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00ABB082  48 89 95 18 01 00 00            mov qword ptr [rbp + 0x118], rdx
00ABB089  48 8D 85 28 01 00 00            lea rax, [rbp + 0x128]
00ABB090  48 89 85 10 01 00 00            mov qword ptr [rbp + 0x110], rax
00ABB097  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00ABB09B  48 89 85 20 01 00 00            mov qword ptr [rbp + 0x120], rax
00ABB0A2  0F B7 01                        movzx eax, word ptr [rcx]
00ABB0A5  89 85 28 01 00 00               mov dword ptr [rbp + 0x128], eax
00ABB0AB  48 8B 85 40 02 00 00            mov rax, qword ptr [rbp + 0x240]
00ABB0B2  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00ABB0B6  48 8D 45 C8                     lea rax, [rbp - 0x38]
00ABB0BA  48 89 85 30 01 00 00            mov qword ptr [rbp + 0x130], rax
00ABB0C1  89 BD 2C 01 00 00               mov dword ptr [rbp + 0x12c], edi
00ABB0C7  48 C7 85 38 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x138], 8
00ABB0D2  66 41 3B F0                     cmp si, r8w
00ABB0D6  76 10                           jbe 0x140abb0e8
00ABB0D8  48 8D 8B 90 01 00 00            lea rcx, [rbx + 0x190]
00ABB0DF  48 39 BB 98 01 00 00            cmp qword ptr [rbx + 0x198], rdi
00ABB0E6  75 05                           jne 0x140abb0ed
00ABB0E8  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00ABB0ED  48 8D 85 58 01 00 00            lea rax, [rbp + 0x158]
00ABB0F4  48 89 95 48 01 00 00            mov qword ptr [rbp + 0x148], rdx
00ABB0FB  48 89 85 40 01 00 00            mov qword ptr [rbp + 0x140], rax
00ABB102  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00ABB106  48 89 85 50 01 00 00            mov qword ptr [rbp + 0x150], rax
00ABB10D  0F B7 01                        movzx eax, word ptr [rcx]
00ABB110  89 85 58 01 00 00               mov dword ptr [rbp + 0x158], eax
00ABB116  48 8B 85 48 02 00 00            mov rax, qword ptr [rbp + 0x248]
00ABB11D  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00ABB121  48 8D 45 D0                     lea rax, [rbp - 0x30]
00ABB125  48 89 85 60 01 00 00            mov qword ptr [rbp + 0x160], rax
00ABB12C  B8 06 00 00 00                  mov eax, 6
00ABB131  89 BD 5C 01 00 00               mov dword ptr [rbp + 0x15c], edi
00ABB137  48 C7 85 68 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x168], 8
00ABB142  66 3B F0                        cmp si, ax
00ABB145  76 10                           jbe 0x140abb157
00ABB147  48 8D 8B E0 01 00 00            lea rcx, [rbx + 0x1e0]
00ABB14E  48 39 BB E8 01 00 00            cmp qword ptr [rbx + 0x1e8], rdi
00ABB155  75 05                           jne 0x140abb15c
00ABB157  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00ABB15C  48 8D 85 88 01 00 00            lea rax, [rbp + 0x188]
00ABB163  48 89 95 78 01 00 00            mov qword ptr [rbp + 0x178], rdx
00ABB16A  48 89 85 70 01 00 00            mov qword ptr [rbp + 0x170], rax
00ABB171  48 8D 15 18 9F 59 FF            lea rdx, [rip - 0xa660e8]
00ABB178  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00ABB17C  48 89 85 80 01 00 00            mov qword ptr [rbp + 0x180], rax
00ABB183  0F B7 01                        movzx eax, word ptr [rcx]
00ABB186  89 85 88 01 00 00               mov dword ptr [rbp + 0x188], eax
00ABB18C  48 8B 85 50 02 00 00            mov rax, qword ptr [rbp + 0x250]
00ABB193  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00ABB198  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00ABB19D  48 89 85 90 01 00 00            mov qword ptr [rbp + 0x190], rax
00ABB1A4  48 8D 45 20                     lea rax, [rbp + 0x20]
00ABB1A8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00ABB1AD  C7 44 24 20 18 00 00 00         mov dword ptr [rsp + 0x20], 0x18
00ABB1B5  89 BD 8C 01 00 00               mov dword ptr [rbp + 0x18c], edi
00ABB1BB  48 C7 85 98 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x198], 8
00ABB1C6  E9 F4 00 00 00                  jmp 0x140abb2bf
00ABB1CB  44 39 05 96 DF 34 00            cmp dword ptr [rip + 0x34df96], r8d
00ABB1D2  0F 86 F9 00 00 00               jbe 0x140abb2d1
00ABB1D8  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
00ABB1E2  48 8D 0D 7F DF 34 00            lea rcx, [rip + 0x34df7f]
00ABB1E9  E8 B2 38 97 FF                  call 0x14042eaa0
00ABB1EE  84 C0                           test al, al
00ABB1F0  0F 84 DB 00 00 00               je 0x140abb2d1
00ABB1F6  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00ABB1FB  48 C7 44 24 78 00 00 00 02      mov qword ptr [rsp + 0x78], 0x2000000
00ABB204  48 89 85 C0 01 00 00            mov qword ptr [rbp + 0x1c0], rax
00ABB20B  48 8D 15 A3 A1 59 FF            lea rdx, [rip - 0xa65e5d]
00ABB212  8B 85 E0 05 00 00               mov eax, dword ptr [rbp + 0x5e0]
00ABB218  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00ABB21C  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00ABB221  48 89 85 D0 01 00 00            mov qword ptr [rbp + 0x1d0], rax
00ABB228  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
00ABB22C  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00ABB230  48 8D 44 24 44                  lea rax, [rsp + 0x44]
00ABB235  48 89 85 E0 01 00 00            mov qword ptr [rbp + 0x1e0], rax
00ABB23C  8A 85 F0 05 00 00               mov al, byte ptr [rbp + 0x5f0]
00ABB242  88 44 24 32                     mov byte ptr [rsp + 0x32], al
00ABB246  48 8D 44 24 32                  lea rax, [rsp + 0x32]
00ABB24B  48 89 85 F0 01 00 00            mov qword ptr [rbp + 0x1f0], rax
00ABB252  48 8D 85 18 02 00 00            lea rax, [rbp + 0x218]
00ABB259  48 89 85 00 02 00 00            mov qword ptr [rbp + 0x200], rax
00ABB260  48 8D 85 A0 01 00 00            lea rax, [rbp + 0x1a0]
00ABB267  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00ABB26C  C7 44 24 20 08 00 00 00         mov dword ptr [rsp + 0x20], 8
00ABB274  48 C7 85 C8 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x1c8], 8
00ABB27F  48 C7 85 D8 01 00 00 04 00 00 00  mov qword ptr [rbp + 0x1d8], 4
00ABB28A  48 C7 85 E8 01 00 00 04 00 00 00  mov qword ptr [rbp + 0x1e8], 4
00ABB295  48 C7 85 F8 01 00 00 01 00 00 00  mov qword ptr [rbp + 0x1f8], 1
00ABB2A0  48 C7 85 08 02 00 00 02 00 00 00  mov qword ptr [rbp + 0x208], 2
00ABB2AB  4C 89 BD 10 02 00 00            mov qword ptr [rbp + 0x210], r15
00ABB2B2  44 89 A5 18 02 00 00            mov dword ptr [rbp + 0x218], r12d
00ABB2B9  89 BD 1C 02 00 00               mov dword ptr [rbp + 0x21c], edi
00ABB2BF  45 33 C9                        xor r9d, r9d
00ABB2C2  48 8D 0D 9F DE 34 00            lea rcx, [rip + 0x34de9f]
00ABB2C9  45 33 C0                        xor r8d, r8d
00ABB2CC  E8 0F AE 96 FF                  call 0x1404260e0
00ABB2D1  40 38 7C 24 30                  cmp byte ptr [rsp + 0x30], dil
00ABB2D6  74 0C                           je 0x140abb2e4
00ABB2D8  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00ABB2DD  33 D2                           xor edx, edx
00ABB2DF  E8 8C 75 0C 00                  call 0x140b82870
00ABB2E4  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00ABB2E8  48 85 C0                        test rax, rax
00ABB2EB  74 0A                           je 0x140abb2f7
00ABB2ED  33 D2                           xor edx, edx
00ABB2EF  48 8B C8                        mov rcx, rax
00ABB2F2  E8 79 75 0C 00                  call 0x140b82870
00ABB2F7  48 85 DB                        test rbx, rbx
00ABB2FA  74 0A                           je 0x140abb306
00ABB2FC  33 D2                           xor edx, edx
00ABB2FE  48 8B CB                        mov rcx, rbx
00ABB301  E8 6A 75 0C 00                  call 0x140b82870
00ABB306  48 8B 8D 80 05 00 00            mov rcx, qword ptr [rbp + 0x580]
00ABB30D  48 33 CC                        xor rcx, rsp
00ABB310  E8 2B 13 BF FF                  call 0x1406ac640
00ABB315  48 8B 9C 24 D0 06 00 00         mov rbx, qword ptr [rsp + 0x6d0]
00ABB31D  48 81 C4 90 06 00 00            add rsp, 0x690
00ABB324  41 5F                           pop r15
00ABB326  41 5E                           pop r14
00ABB328  41 5D                           pop r13
00ABB32A  41 5C                           pop r12
00ABB32C  5F                              pop rdi
00ABB32D  5E                              pop rsi
00ABB32E  5D                              pop rbp
00ABB32F  C3                              ret
00ABB330  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwTimLogRedirectionTrustPolicy(int a1, __int64 a2, int a3, __int64 a4, unsigned __int8 a5)
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
    unsigned __int64 v_stack_m2E8;
    unsigned int v_stack_m2EC;
    unsigned int v_stack_m2F0;
    unsigned __int64 v_stack_m2F8;
    unsigned __int64 v_stack_m300;
    unsigned __int64 v_stack_m308;
    unsigned int v_stack_m30C;
    unsigned int v_stack_m310;
    unsigned __int64 v_stack_m318;
    unsigned __int64 v_stack_m320;
    unsigned __int64 v_stack_m328;
    unsigned __int64 v_stack_m378;
    unsigned __int64 v_stack_m380;
    unsigned __int64 v_stack_m388;
    unsigned __int64 v_stack_m390;
    unsigned __int64 v_stack_m398;
    unsigned __int64 v_stack_m3A0;
    unsigned __int64 v_stack_m3A8;
    unsigned int v_stack_m3AC;
    unsigned __int64 v_stack_m3B0;
    unsigned __int64 v_stack_m3B8;
    unsigned __int64 v_stack_m3C0;
    unsigned __int64 v_stack_m3C8;
    unsigned __int64 v_stack_m3D0;
    unsigned __int64 v_stack_m3D8;
    unsigned __int64 v_stack_m3E0;
    unsigned __int64 v_stack_m3E8;
    unsigned __int64 v_stack_m3F0;
    unsigned __int64 v_stack_m3F8;
    unsigned __int64 v_stack_m400;
    unsigned __int64 v_stack_m408;
    unsigned __int64 v_stack_m428;
    unsigned __int64 v_stack_m430;
    unsigned __int64 v_stack_m438;
    unsigned int v_stack_m43C;
    unsigned __int64 v_stack_m440;
    unsigned __int64 v_stack_m448;
    unsigned __int64 v_stack_m450;
    unsigned __int64 v_stack_m458;
    unsigned __int64 v_stack_m460;
    unsigned __int64 v_stack_m468;
    unsigned int v_stack_m46C;
    unsigned __int64 v_stack_m470;
    unsigned __int64 v_stack_m478;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m480;
    unsigned __int64 v_stack_m488;
    unsigned __int64 v_stack_m490;
    unsigned __int64 v_stack_m498;
    unsigned int v_stack_m49C;
    unsigned __int64 v_stack_m4A0;
    unsigned __int64 v_stack_m4A8;
    unsigned __int64 v_stack_m4B0;
    unsigned __int64 v_stack_m4B8;
    unsigned __int64 v_stack_m4C0;
    unsigned __int64 v_stack_m4C8;
    unsigned int v_stack_m4CC;
    unsigned __int64 v_stack_m4D0;
    unsigned __int64 v_stack_m4D8;
    unsigned __int64 v_stack_m4E0;
    unsigned __int64 v_stack_m4E8;
    unsigned __int64 v_stack_m4F0;
    unsigned __int64 v_stack_m4F8;
    unsigned int v_stack_m4FC;
    unsigned __int64 v_stack_m500;
    unsigned __int64 v_stack_m508;
    unsigned __int64 v_stack_m510;
    unsigned __int64 v_stack_m518;
    unsigned __int64 v_stack_m520;
    unsigned __int64 v_stack_m528;
    unsigned int v_stack_m52C;
    unsigned __int64 v_stack_m530;
    unsigned __int64 v_stack_m538;
    unsigned __int64 v_stack_m540;
    unsigned __int64 v_stack_m548;
    unsigned __int64 v_stack_m550;
    unsigned __int64 v_stack_m558;
    unsigned __int64 v_stack_m560;
    unsigned __int64 v_stack_m568;
    unsigned __int64 v_stack_m570;
    unsigned __int64 v_stack_m578;
    unsigned __int64 v_stack_m580;
    unsigned __int64 v_stack_m588;
    unsigned __int64 v_stack_m5A8;
    unsigned __int64 v_stack_m5C0;
    unsigned __int64 v_stack_m5C8;
    unsigned __int64 v_stack_m5D0;
    unsigned __int64 v_stack_m5D8;
    unsigned __int64 v_stack_m5E0;
    unsigned __int64 v_stack_m5F0;
    unsigned __int64 v_stack_m5F8;
    unsigned __int64 v_stack_m600;
    unsigned __int64 v_stack_m608;
    unsigned __int64 v_stack_m610;
    unsigned __int64 v_stack_m618;
    unsigned __int64 v_stack_m620;
    unsigned __int64 v_stack_m628;
    unsigned __int64 v_stack_m638;
    unsigned __int64 v_stack_m640;
    unsigned __int64 v_stack_m648;
    unsigned __int64 v_stack_m650;
    unsigned __int64 v_stack_m658;
    unsigned __int64 v_stack_m660;
    unsigned int v_stack_m668;
    unsigned __int64 v_stack_m670;
    unsigned __int16 v_stack_m676;
    unsigned __int64 v_stack_m678;
    unsigned int v_stack_m680;
    unsigned int v_stack_m684;
    unsigned int v_stack_m688;
    unsigned __int16 v_stack_m68C;
    unsigned __int16 v_stack_m690;
    unsigned __int16 v_stack_m694;
    unsigned __int16 v_stack_m696;
    unsigned __int8 v_stack_m698;
    unsigned __int64 v_stack_m6A0;
    unsigned __int64 v_stack_m6A8;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (0x690ULL);
    result = (*(unsigned __int64 *)(v_rip + 3473205)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m660 = a2;
    v_rsi = 0;
    v_stack_m688 = a1;
    v_stack_m628 = 0;
    v_stack_m694 = 0;
    a2 = 0;
    v_stack_m690 = 0;
    v_stack_m68C = 0;
    v_stack_m658 = a4;
    v_stack_m5F0 = v_xmm0;
    v_stack_m678 = v_xmm1;
    v_stack_m5E0 = v_xmm0;
    v_stack_m5D0 = v_xmm0;
    v_stack_m5C0 = v_xmm0;
    result = memset(v_stack_m3A8, a2, 128, a4);
    v_stack_m668 = a5;
    v_stack_m698 = 0;
    v_stack_m648 = 0;
    result = RtlWalkFrameChain(v_stack_m3A8, v_rsi + 16, (unsigned int)((unsigned int)(v_rsi + 1)), a4);
loc_00ABA8B2:
    if (((unsigned __int16)((unsigned int)((unsigned int)(result)))) <= ((unsigned __int16)(0 + 7))) {
        a2 = (unsigned __int16)((unsigned int)((unsigned int)(result)));
    }
    if (((unsigned int)((unsigned __int16)((unsigned __int16)(0 + 1)))) >= ((unsigned int)(a2))) goto loc_00ABA8D5;
    v_rdi = (unsigned int)((0) + (*(unsigned int *)(v_stack_m5C8 + (unsigned __int16)((unsigned __int16)(0 + 1)) * 8 + 544)));
    a1 = (unsigned __int16)(((unsigned __int16)(0 + 1)) + ((unsigned __int16)(0 + 1)));
    goto loc_00ABA8B2;
loc_00ABA8D5:
    a2 = 0;
    if ((unsigned int)(v_rdi) == 0) { v_rdi = (unsigned int)(0 + 1); }
loc_00ABA8DD:
    if (*(unsigned __int64 *)(a2 + 1968) != 0) goto loc_00ABA926;
    result = ExAllocatePool2(256, *(unsigned __int64 *)(a2 + 1968) + 40, (unsigned int)(0x6E734954ULL), 0 + 7);
    a2 = 0;
    if (result == 0) goto loc_00ABB306;
    result = 0;
    if (condition_is_equal) goto loc_00ABA91D;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(0x6E734954ULL), 0 + 7);
    a2 = 0;
    goto loc_00ABA920;
loc_00ABA91D:
loc_00ABA920:
loc_00ABA926:
    if (0 >= 10) goto loc_00ABA948;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 0 * 4))) == 0) goto loc_00ABA944;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 0 * 4)))) == ((unsigned int)(v_rdi))) goto loc_00ABB306;
    v_r14 = (unsigned int)((0) + (1));
    goto loc_00ABA926;
loc_00ABA944:
loc_00ABA948:
    v_r12 = (unsigned __int8)(((unsigned __int8)(v_rsi + 1)) & (0));
    if (condition_is_equal) goto loc_00ABB306;
    result = 0;
    if (condition_is_equal) goto loc_00ABA96D;
    a2 = 0;
    goto loc_00ABA8DD;
loc_00ABA96D:
    result = RtlInitUnicodeString(v_stack_m678, v_rip + 277612, 1, 0 + 7);
    v_r12 = 0;
    if ((unsigned __int16)((unsigned int)((unsigned int)(result))) == 0) goto loc_00ABAAC5;
    a2 = ((unsigned __int16)((unsigned int)((unsigned int)(result))) + (unsigned __int16)((unsigned int)((unsigned int)(result))) * 4) << (4);
    result = ExAllocatePool2(256, a2, (unsigned int)((unsigned int)((unsigned int)(0x6E734954ULL))), 0 + 7);
    result = ExAllocatePool2(256, 538, (unsigned int)((unsigned int)((unsigned int)(0x6E734954ULL))), 0 + 7);
    a1 = 0;
    v_stack_m648 = result;
    if (result == 0) goto loc_00ABAB2E;
    if (result == 0) goto loc_00ABAB2E;
    if (0 >= ((unsigned __int16)((unsigned int)((unsigned int)(result))))) goto loc_00ABAAC2;
loc_00ABA9F2:
    v_stack_m6A0 = 0;
    a1 = (a1) | (-1);
    v_stack_m6A8 = 536;
    result = ZwQueryVirtualMemory(a1, *(unsigned __int64 *)(v_stack_m3A8), 2, result);
    a1 = 0;
    if (sign_flag) goto loc_00ABAAA9;
    if (((unsigned __int16)(*(unsigned __int16 *)(result))) <= ((unsigned __int16)(a1 + 1))) goto loc_00ABAAA9;
    a2 = (unsigned __int16)((*(unsigned __int16 *)(result)) >> (1));
    a2 = (unsigned __int16)((a2) - ((unsigned __int16)(a1 + 1)));
loc_00ABAA31:
    if ((unsigned __int16)(a2) == 0) goto loc_00ABAA53;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(result + 8) + (unsigned __int16)(a2) * 2)) == 92) goto loc_00ABAA4F;
    a2 = (unsigned __int16)((a2) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    goto loc_00ABAA31;
loc_00ABAA4F:
    a2 = (unsigned __int16)((a2) + ((unsigned __int16)(a1 + 1)));
loc_00ABAA53:
    result = RtlStringCbCopyW(result + 16, 64, *(unsigned __int64 *)(result + 8) + (unsigned __int16)(a2) * 2, result);
    result = RtlInitUnicodeString(result + 16 - 16, result + 16, *(unsigned __int64 *)(result + 8) + (unsigned __int16)(a2) * 2, result);
    a3 = 0;
    a1 = (result + 16 - 16) | (-1);
    v_stack_m6A8 = 48;
    result = ZwQueryVirtualMemory(a1, *(unsigned __int64 *)(v_stack_m3A8), a3, v_stack_m5E0);
    a1 = 0;
    if (sign_flag) goto loc_00ABAAA9;
    goto loc_00ABAAAC;
loc_00ABAAA9:
    *(unsigned __int64 *)(v_stack_m3A8) = 0;
loc_00ABAAAC:
    v_r14 = (result + 16) + (80);
    v_rdi = (v_stack_m3A8) + (8);
    v_r15 = ((unsigned __int16)((unsigned int)((unsigned int)(result)))) - (a1 + 1);
    if (condition_is_not_equal) goto loc_00ABA9F2;
loc_00ABAAC2:
    v_r12 = 0;
loc_00ABAAC5:
    result = v_rip - 11115932;
    if (v_stack_m688 != 1) { result = v_rip - 11110764; }
    v_stack_m660 = result;
    v_stack_m640 = v_xmm0;
    v_r14 = v_rip - 11238336;
    if (*(unsigned __int64 *)(v_stack_m660 + 848) != 0) { v_r14 = *(unsigned __int64 *)(v_stack_m660 + 848); }
    result = EtwpQueryProcessCommandLine(v_stack_m660, v_stack_m640, a3, v_stack_m5E0);
    if ((unsigned __int16)(v_stack_m640) != 0) goto loc_00ABAB52;
    result = RtlInitUnicodeString(v_stack_m640, v_rip + 277185, a3, v_stack_m5E0);
    goto loc_00ABAB57;
loc_00ABAB2E:
    v_r12 = 0;
    if (0 >= ((unsigned __int16)((unsigned int)((unsigned int)(result))))) goto loc_00ABAAC5;
    a3 = ((unsigned __int16)((unsigned int)((unsigned int)(result)))) << (3);
    a2 = 0;
    result = memset(v_stack_m3A8, a2, a3, v_stack_m5E0);
    goto loc_00ABAAC5;
loc_00ABAB52:
    v_stack_m698 = 1;
loc_00ABAB57:
    v_r10 = v_stack_m658;
    if (v_stack_m658 == 0) {
        a2 = v_rip + 277112;
        a1 = v_stack_m5F0;
        result = RtlInitUnicodeString(a1, a2, a3, v_stack_m5E0);
        v_r10 = v_stack_m5F0;
    }
    if (v_r14 == 0) goto loc_00ABABBD;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_r14)) == 0) goto loc_00ABABBD;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_r14)) >> (1));
    v_stack_m694 = (unsigned __int16)(result);
    v_stack_m328 = v_stack_m694;
    v_stack_m320 = 2;
    goto loc_00ABABE0;
loc_00ABABBD:
    v_stack_m694 = 6;
    v_stack_m328 = v_stack_m694;
    v_stack_m320 = 2;
loc_00ABABE0:
    v_stack_m310 = (unsigned int)((unsigned int)((unsigned int)(6 + 6)));
    v_stack_m658 = v_stack_m638;
    v_stack_m318 = v_rip + 314212;
    v_stack_m30C = 0;
    v_stack_m300 = 2;
    if ((unsigned __int16)(v_stack_m640) == 0) goto loc_00ABAC28;
    v_stack_m2F8 = v_stack_m638;
    v_stack_m308 = v_stack_m690;
    v_rdi = (unsigned __int16)((v_stack_m640) >> (1));
    goto loc_00ABAC41;
loc_00ABAC28:
    v_stack_m2F8 = v_rip + 314212;
    v_stack_m308 = v_stack_m690;
loc_00ABAC41:
    v_stack_m690 = 6;
    v_stack_m2F0 = (unsigned int)((unsigned int)((unsigned int)(6 + 6)));
    v_stack_m2EC = 0;
    result = EtwpTiFillProcessIdentity(v_stack_m2E8, v_stack_m660, v_stack_m628, 6 + 6);
    a1 = ((unsigned int)((unsigned int)(result + 4 * 1))) + ((unsigned int)((unsigned int)(result + 4 * 1)));
    a2 = (unsigned int)((result + 4 * 1) + (1));
    *(unsigned __int64 *)(v_stack_m5C8 + a1 * 8 + 672) = v_stack_p18;
    *(unsigned __int64 *)(v_stack_m5C8 + a1 * 8 + 680) = 4;
    if (v_r10 == 0) goto loc_00ABACB3;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_r10)) == 0) goto loc_00ABACB3;
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(v_r10))) >> (1));
    goto loc_00ABACBF;
loc_00ABACB3:
    a3 = (unsigned int)((a2 + 1) + (2));
loc_00ABACBF:
    v_stack_m68C = 6;
    result = ((unsigned int)((unsigned int)(a2))) << (4);
    a2 = ((unsigned int)(a3)) << (4);
    v_rdi = 0;
    *(unsigned __int64 *)(v_stack_m328 + result * 1) = v_stack_m68C;
    *(unsigned int *)(v_stack_m5C8 + result * 1 + 680) = 2;
    *(unsigned int *)(v_stack_m328 + result * 1 + 12) = 0;
    *(unsigned __int64 *)(a2 + v_stack_m328 * 1) = v_rip + 314212;
    *(unsigned int *)(v_stack_m5C8 + a2 * 1 + 680) = (unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_r10))));
    *(unsigned int *)(a2 + v_stack_m328 * 1 + 12) = 0;
    result = ((unsigned int)((unsigned int)(a3 + 1))) + ((unsigned int)((unsigned int)(a3 + 1)));
    *(unsigned __int64 *)(v_stack_m5C8 + result * 8 + 680) = 4;
    *(unsigned __int64 *)(v_stack_m5C8 + result * 8 + 672) = v_stack_m668;
    v_stack_m696 = (unsigned __int16)(v_stack_m676);
loc_00ABAD56:
    if (0 >= ((unsigned __int16)((unsigned int)((unsigned int)(result))))) goto loc_00ABADC4;
    if (result == 0) goto loc_00ABADC4;
    if (result == 0) goto loc_00ABAD93;
    if (*(unsigned __int64 *)(result + 8) == 0) goto loc_00ABAD93;
    if ((unsigned __int16)(*(unsigned __int16 *)(result)) == 0) goto loc_00ABAD93;
    a3 = ((unsigned int)((unsigned int)(a3 + 1 + 1))) << (4);
    v_rdi = (unsigned int)((unsigned int)(*(unsigned __int16 *)(result))) + 2;
    if (((unsigned int)(*(unsigned __int16 *)(result + 2))) <= ((unsigned int)(*(unsigned __int16 *)(result) + 1))) { v_rdi = (unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(result)))); }
    goto loc_00ABADA6;
loc_00ABAD93:
    a3 = ((unsigned int)((unsigned int)(a3 + 1 + 1))) << (4);
loc_00ABADA6:
    *(unsigned __int64 *)(a3 + v_stack_m328 * 1) = v_rip + 313667;
    *(unsigned int *)(v_stack_m5C8 + a3 * 1 + 680) = 14;
    v_rdi = 0;
    *(unsigned int *)(a3 + v_stack_m328 * 1 + 12) = 0;
    goto loc_00ABAE23;
loc_00ABADC4:
    if (v_stack_m670 == 0) goto loc_00ABAE02;
    if ((unsigned __int16)(v_stack_m678) == 0) goto loc_00ABAE02;
    a4 = ((unsigned int)((unsigned int)(a3 + 1 + 1))) + ((unsigned int)((unsigned int)(a3 + 1 + 1)));
    a2 = v_stack_m678 + 2;
    if (((unsigned int)((unsigned __int16)(a3))) <= ((unsigned int)(v_stack_m678 + 1))) { a2 = (unsigned int)(v_stack_m678); }
    *(unsigned int *)(v_stack_m5C8 + a4 * 8 + 680) = (unsigned int)(a2);
    *(unsigned __int64 *)(v_stack_m5C8 + a4 * 8 + 672) = v_stack_m670;
    *(unsigned int *)(v_stack_m5C8 + a4 * 8 + 684) = 0;
    goto loc_00ABAE23;
loc_00ABAE02:
    result = ((unsigned int)((unsigned int)(a3 + 1 + 1))) + ((unsigned int)((unsigned int)(a3 + 1 + 1)));
    *(unsigned __int64 *)(v_stack_m5C8 + result * 8 + 672) = v_rip + 313556;
    *(unsigned __int64 *)(v_stack_m5C8 + result * 8 + 680) = 14;
loc_00ABAE23:
    v_r14 = (unsigned __int16)((0) + 1);
    v_r11 = (result) + (80);
    result = ((unsigned int)((unsigned int)(1 + a3 + 1 + 1 * 1))) + ((unsigned int)((unsigned int)(1 + a3 + 1 + 1 * 1)));
    *(unsigned __int64 *)(v_stack_m5C8 + result * 8 + 672) = v_stack_m3A8;
    v_r13 = (v_stack_m3A8) + (8);
    *(unsigned __int64 *)(v_stack_m5C8 + result * 8 + 680) = 8;
    if (((unsigned __int16)(v_r14)) < 16) goto loc_00ABAD56;
    a3 = 0;
    v_stack_m6A8 = v_stack_m328;
    result = EtwWrite(*(unsigned __int64 *)(v_rip + 4475308), v_stack_m660, a3, (unsigned int)((unsigned int)(1 + a3 + 1 + 1 * 1 + 1)));
    if (result == 0) goto loc_00ABB1CB;
    if ((*(unsigned int *)(v_rip + 3465926)) <= 5) goto loc_00ABB2D1;
    result = tlgKeywordOn(v_rip + 3465903, v_stack_m660, 5, (unsigned int)((unsigned int)(1 + a3 + 1 + 1 * 1 + 1)));
    if ((unsigned __int8)(result) == 0) goto loc_00ABB2D1;
    v_stack_m620 = 0x2000000ULL;
    v_stack_m588 = v_stack_m620;
    v_stack_m684 = (unsigned int)((unsigned int)(v_stack_p18));
    v_stack_m578 = v_stack_m684;
    v_stack_m680 = (unsigned int)((unsigned int)(v_stack_m688));
    v_stack_m568 = v_stack_m680;
    v_stack_m696 = a5;
    v_stack_m558 = v_stack_m696;
    v_stack_m580 = 8;
    v_stack_m570 = 5 - 1;
    v_stack_m560 = 5 - 1;
    v_stack_m550 = 5 - 4;
    if (((unsigned __int16)((unsigned int)((unsigned int)(result)))) <= ((unsigned __int16)(5 - 4))) goto loc_00ABAF38;
    if ((*(unsigned __int64 *)(result + 88)) == 0) {
        a1 = v_stack_m678;
    }
    v_stack_m52C = 0;
    v_stack_m548 = v_stack_m530;
    v_stack_m538 = *(unsigned __int64 *)(a1 + 8);
    v_stack_m530 = (unsigned int)(*(unsigned __int16 *)(a1));
    v_stack_m618 = v_stack_m3A0;
    v_stack_m528 = v_stack_m618;
    v_stack_m540 = 2;
    v_stack_m520 = 8;
    if (((unsigned __int16)((unsigned int)((unsigned int)(result)))) <= 2) goto loc_00ABAFA7;
    if ((*(unsigned __int64 *)(result + 168)) == 0) {
        a1 = v_stack_m678;
    }
    v_stack_m510 = 2;
    v_stack_m518 = v_stack_m500;
    v_stack_m508 = *(unsigned __int64 *)(a1 + 8);
    v_stack_m500 = (unsigned int)(*(unsigned __int16 *)(a1));
    v_stack_m610 = v_stack_m398;
    v_stack_m4F8 = v_stack_m610;
    v_stack_m4FC = 0;
    v_stack_m4F0 = 8;
    if (((unsigned __int16)((unsigned int)((unsigned int)(result)))) <= 3) goto loc_00ABB012;
    if ((*(unsigned __int64 *)(result + 248)) == 0) {
        a1 = v_stack_m678;
    }
    v_stack_m4E0 = 2;
    v_stack_m4E8 = v_stack_m4D0;
    v_stack_m4D8 = *(unsigned __int64 *)(a1 + 8);
    v_stack_m4D0 = (unsigned int)(*(unsigned __int16 *)(a1));
    v_stack_m608 = v_stack_m390;
    v_stack_m4C8 = v_stack_m608;
    v_stack_m4CC = 0;
    v_stack_m4C0 = 8;
    if (((unsigned __int16)((unsigned int)((unsigned int)(result)))) <= ((unsigned __int16)(5 - 1))) goto loc_00ABB07D;
    if ((*(unsigned __int64 *)(result + 328)) == 0) {
        a1 = v_stack_m678;
    }
    v_stack_m4B0 = 2;
    v_stack_m4B8 = v_stack_m4A0;
    v_stack_m4A8 = *(unsigned __int64 *)(a1 + 8);
    v_stack_m4A0 = (unsigned int)(*(unsigned __int16 *)(a1));
    v_stack_m600 = v_stack_m388;
    v_stack_m498 = v_stack_m600;
    v_stack_m49C = 0;
    v_stack_m490 = 8;
    if (((unsigned __int16)((unsigned int)((unsigned int)(result)))) <= 5) goto loc_00ABB0E8;
    if ((*(unsigned __int64 *)(result + 408)) == 0) {
        a1 = v_stack_m678;
    }
    v_stack_m480 = 2;
    v_stack_m488 = v_stack_m470;
    v_stack_m478 = *(unsigned __int64 *)(a1 + 8);
    v_stack_m470 = (unsigned int)(*(unsigned __int16 *)(a1));
    v_stack_m5F8 = v_stack_m380;
    v_stack_m468 = v_stack_m5F8;
    v_stack_m46C = 0;
    v_stack_m460 = 8;
    if (((unsigned __int16)((unsigned int)((unsigned int)(result)))) <= 6) goto loc_00ABB157;
    if ((*(unsigned __int64 *)(result + 488)) == 0) {
        a1 = v_stack_m678;
    }
    v_stack_m450 = 2;
    v_stack_m458 = v_stack_m440;
    v_stack_m448 = *(unsigned __int64 *)(a1 + 8);
    v_stack_m440 = (unsigned int)(*(unsigned __int16 *)(a1));
    v_stack_m650 = v_stack_m378;
    v_stack_m438 = v_stack_m650;
    v_stack_m6A0 = v_stack_m5A8;
    v_stack_m6A8 = 24;
    v_stack_m43C = 0;
    v_stack_m430 = 8;
    goto loc_00ABB2BF;
loc_00ABB1CB:
    if ((*(unsigned int *)(v_rip + 3465110)) <= 5) goto loc_00ABB2D1;
    result = tlgKeywordOn(v_rip + 3465087, v_rip - 10903784, 5, (unsigned int)((unsigned int)(1 + a3 + 1 + 1 * 1 + 1)));
    if ((unsigned __int8)(result) == 0) goto loc_00ABB2D1;
    v_stack_m650 = 0x2000000ULL;
    v_stack_m408 = v_stack_m650;
    v_stack_m680 = (unsigned int)((unsigned int)(v_stack_p18));
    v_stack_m3F8 = v_stack_m680;
    v_stack_m684 = (unsigned int)((unsigned int)(v_stack_m688));
    v_stack_m3E8 = v_stack_m684;
    v_stack_m696 = a5;
    v_stack_m3D8 = v_stack_m696;
    v_stack_m3C8 = v_stack_m3B0;
    v_stack_m6A0 = v_stack_m428;
    v_stack_m6A8 = 8;
    v_stack_m400 = 8;
    v_stack_m3F0 = 4;
    v_stack_m3E0 = 4;
    v_stack_m3D0 = 1;
    v_stack_m3C0 = 2;
    v_stack_m3B8 = v_stack_m670;
    v_stack_m3B0 = (unsigned int)(v_stack_m678);
    v_stack_m3AC = 0;
loc_00ABB2BF:
    a4 = 0;
    a3 = 0;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 3464863, v_rip - 10903133, a3, a4);
loc_00ABB2D1:
    if (v_stack_m698 != 0) {
        a1 = v_stack_m658;
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    result = v_stack_m648;
    if (v_stack_m648 != 0) {
        a2 = 0;
        a1 = v_stack_m648;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (0x690ULL);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwTimLogRedirectionTrustPolicy(int32_t Arg1, void *Arg2, int32_t Arg3, int64_t Arg4, uint8_t Arg5)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

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
    uint64_t v_stack_m2E8;
    uint32_t v_stack_m2EC;
    uint32_t v_stack_m2F0;
    uint64_t v_stack_m2F8;
    uint64_t v_stack_m300;
    uint64_t v_stack_m308;
    uint32_t v_stack_m30C;
    uint32_t v_stack_m310;
    uint64_t v_stack_m318;
    uint64_t v_stack_m320;
    uint64_t v_stack_m328;
    uint64_t v_stack_m378;
    uint64_t v_stack_m380;
    uint64_t v_stack_m388;
    uint64_t v_stack_m390;
    uint64_t v_stack_m398;
    uint64_t v_stack_m3A0;
    uint64_t v_stack_m3A8;
    uint32_t v_stack_m3AC;
    uint64_t v_stack_m3B0;
    uint64_t v_stack_m3B8;
    uint64_t v_stack_m3C0;
    uint64_t v_stack_m3C8;
    uint64_t v_stack_m3D0;
    uint64_t v_stack_m3D8;
    uint64_t v_stack_m3E0;
    uint64_t v_stack_m3E8;
    uint64_t v_stack_m3F0;
    uint64_t v_stack_m3F8;
    uint64_t v_stack_m400;
    uint64_t v_stack_m408;
    uint64_t v_stack_m428;
    uint64_t v_stack_m430;
    uint64_t v_stack_m438;
    uint32_t v_stack_m43C;
    uint64_t v_stack_m440;
    uint64_t v_stack_m448;
    uint64_t v_stack_m450;
    uint64_t v_stack_m458;
    uint64_t v_stack_m460;
    uint64_t v_stack_m468;
    uint32_t v_stack_m46C;
    uint64_t v_stack_m470;
    uint64_t v_stack_m478;
    uint64_t v_stack_m48;
    uint64_t v_stack_m480;
    uint64_t v_stack_m488;
    uint64_t v_stack_m490;
    uint64_t v_stack_m498;
    uint32_t v_stack_m49C;
    uint64_t v_stack_m4A0;
    uint64_t v_stack_m4A8;
    uint64_t v_stack_m4B0;
    uint64_t v_stack_m4B8;
    uint64_t v_stack_m4C0;
    uint64_t v_stack_m4C8;
    uint32_t v_stack_m4CC;
    uint64_t v_stack_m4D0;
    uint64_t v_stack_m4D8;
    uint64_t v_stack_m4E0;
    uint64_t v_stack_m4E8;
    uint64_t v_stack_m4F0;
    uint64_t v_stack_m4F8;
    uint32_t v_stack_m4FC;
    uint64_t v_stack_m500;
    uint64_t v_stack_m508;
    uint64_t v_stack_m510;
    uint64_t v_stack_m518;
    uint64_t v_stack_m520;
    uint64_t v_stack_m528;
    uint32_t v_stack_m52C;
    uint64_t v_stack_m530;
    uint64_t v_stack_m538;
    uint64_t v_stack_m540;
    uint64_t v_stack_m548;
    uint64_t v_stack_m550;
    uint64_t v_stack_m558;
    uint64_t v_stack_m560;
    uint64_t v_stack_m568;
    uint64_t v_stack_m570;
    uint64_t v_stack_m578;
    uint64_t v_stack_m580;
    uint64_t v_stack_m588;
    uint64_t v_stack_m5A8;
    uint64_t v_stack_m5C0;
    uint64_t v_stack_m5C8;
    uint64_t v_stack_m5D0;
    uint64_t v_stack_m5D8;
    uint64_t v_stack_m5E0;
    uint64_t v_stack_m5F0;
    uint64_t v_stack_m5F8;
    uint64_t v_stack_m600;
    uint64_t v_stack_m608;
    uint64_t v_stack_m610;
    uint64_t v_stack_m618;
    uint64_t v_stack_m620;
    uint64_t v_stack_m628;
    uint64_t v_stack_m638;
    uint64_t v_stack_m640;
    uint64_t v_stack_m648;
    uint64_t v_stack_m650;
    uint64_t v_stack_m658;
    uint64_t v_stack_m660;
    uint32_t v_stack_m668;
    uint64_t v_stack_m670;
    uint16_t v_stack_m676;
    uint64_t v_stack_m678;
    uint32_t v_stack_m680;
    uint32_t v_stack_m684;
    uint32_t v_stack_m688;
    uint16_t v_stack_m68C;
    uint16_t v_stack_m690;
    uint16_t v_stack_m694;
    uint16_t v_stack_m696;
    uint8_t v_stack_m698;
    uint64_t v_stack_m6A0;
    uint64_t v_stack_m6A8;
    uint32_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (0x690ULL);
    result = (*(uint64_t *)(v_rip + 0x34FF35)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m660 = Arg2;
    local_rsi = 0;
    v_stack_m688 = Arg1;
    v_stack_m628 = 0;
    v_stack_m694 = 0;
    Arg2 = 0;
    v_stack_m690 = 0;
    v_stack_m68C = 0;
    v_stack_m658 = Arg4;
    v_stack_m5F0 = v_xmm0;
    v_stack_m678 = v_xmm1;
    v_stack_m5E0 = v_xmm0;
    v_stack_m5D0 = v_xmm0;
    v_stack_m5C0 = v_xmm0;
    result = memset(v_stack_m3A8, Arg2, 128, Arg4);
    v_stack_m668 = Arg5;
    v_stack_m698 = 0;
    v_stack_m648 = 0;
    result = RtlWalkFrameChain(v_stack_m3A8, local_rsi + 16, (uint32_t)((uint32_t)(local_rsi + 1)), Arg4);
loc_00ABA8B2:
    if (((uint16_t)((uint32_t)((uint32_t)(result)))) <= ((uint16_t)(0 + 7))) {
        Arg2 = (uint16_t)((uint32_t)((uint32_t)(result)));
    }
    if (((uint32_t)((uint16_t)((uint16_t)(0 + 1)))) >= ((uint32_t)(Arg2))) goto loc_00ABA8D5;
    local_rdi = (uint32_t)((0) + (*(uint32_t *)(v_stack_m5C8 + (uint16_t)((uint16_t)(0 + 0x1)) * 8 + 0x220)));
    Arg1 = (uint16_t)(((uint16_t)(0 + 1)) + ((uint16_t)(0 + 1)));
    goto loc_00ABA8B2;
loc_00ABA8D5:
    Arg2 = 0;
    if ((uint32_t)(local_rdi) == 0) { local_rdi = (uint32_t)(0 + 1); }
loc_00ABA8DD:
    if (*(uint64_t *)(arg2 + 0x7B0) != 0) goto loc_00ABA926;
    result = ExAllocatePool2(256, *(uint64_t *)(arg2 + 0x7B0) + 40, (uint32_t)(0x6E734954ULL), 0 + 7);
    Arg2 = 0;
    if (result == 0) goto loc_00ABB306;
    result = 0;
    if (condition_is_equal) goto loc_00ABA91D;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(0x6E734954ULL), 0 + 7);
    Arg2 = 0;
    goto loc_00ABA920;
loc_00ABA91D:
loc_00ABA920:
loc_00ABA926:
    if (0 >= 10) goto loc_00ABA948;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x0 * 4))) == 0) goto loc_00ABA944;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x0 * 4)))) == ((uint32_t)(local_rdi))) goto loc_00ABB306;
    local_r14 = (uint32_t)((0) + (1));
    goto loc_00ABA926;
loc_00ABA944:
loc_00ABA948:
    local_r12 = (uint8_t)(((uint8_t)(local_rsi + 1)) & (0));
    if (condition_is_equal) goto loc_00ABB306;
    result = 0;
    if (condition_is_equal) goto loc_00ABA96D;
    Arg2 = 0;
    goto loc_00ABA8DD;
loc_00ABA96D:
    result = RtlInitUnicodeString(v_stack_m678, v_rip + 277612, 1, 0 + 7);
    local_r12 = 0;
    if ((uint16_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_00ABAAC5;
    Arg2 = ((uint16_t)((uint32_t)((uint32_t)(result))) + (uint16_t)((uint32_t)((uint32_t)(result))) * 4) << (4);
    result = ExAllocatePool2(256, Arg2, (uint32_t)((uint32_t)((uint32_t)(0x6E734954ULL))), 0 + 7);
    result = ExAllocatePool2(256, 538, (uint32_t)((uint32_t)((uint32_t)(0x6E734954ULL))), 0 + 7);
    Arg1 = 0;
    v_stack_m648 = result;
    if (result == 0) goto loc_00ABAB2E;
    if (result == 0) goto loc_00ABAB2E;
    if (0 >= ((uint16_t)((uint32_t)((uint32_t)(result))))) goto loc_00ABAAC2;
loc_00ABA9F2:
    v_stack_m6A0 = 0;
    Arg1 = (Arg1) | (-1);
    v_stack_m6A8 = 536;
    result = ZwQueryVirtualMemory(Arg1, *(uint64_t *)(v_stack_m3A8), 2, result);
    Arg1 = 0;
    if (sign_flag) goto loc_00ABAAA9;
    if (((uint16_t)(*(uint16_t *)(result))) <= ((uint16_t)(Arg1 + 1))) goto loc_00ABAAA9;
    Arg2 = (uint16_t)((*(uint16_t *)(result)) >> (1));
    Arg2 = (uint16_t)((Arg2) - ((uint16_t)(Arg1 + 1)));
loc_00ABAA31:
    if ((uint16_t)(Arg2) == 0) goto loc_00ABAA53;
    if ((*(uint16_t *)(*(uint64_t *)(result + 0x8) + (uint16_t)(arg2) * 2)) == 92) goto loc_00ABAA4F;
    Arg2 = (uint16_t)((Arg2) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    goto loc_00ABAA31;
loc_00ABAA4F:
    Arg2 = (uint16_t)((Arg2) + ((uint16_t)(Arg1 + 1)));
loc_00ABAA53:
    result = RtlStringCbCopyW(result + 16, 64, *(uint64_t *)(result + 0x8) + (uint16_t)(Arg2) * 2, result);
    result = RtlInitUnicodeString(result + 16 - 16, result + 16, *(uint64_t *)(result + 0x8) + (uint16_t)(Arg2) * 2, result);
    Arg3 = 0;
    Arg1 = (result + 16 - 16) | (-1);
    v_stack_m6A8 = 48;
    result = ZwQueryVirtualMemory(Arg1, *(uint64_t *)(v_stack_m3A8), Arg3, v_stack_m5E0);
    Arg1 = 0;
    if (sign_flag) goto loc_00ABAAA9;
    goto loc_00ABAAAC;
loc_00ABAAA9:
    *(uint64_t *)(v_stack_m3A8) = 0;
loc_00ABAAAC:
    local_r14 = (result + 16) + (80);
    local_rdi = (v_stack_m3A8) + (8);
    local_r15 = ((uint16_t)((uint32_t)((uint32_t)(result)))) - (Arg1 + 1);
    if (condition_is_not_equal) goto loc_00ABA9F2;
loc_00ABAAC2:
    local_r12 = 0;
loc_00ABAAC5:
    result = v_rip - 11115932;
    if (v_stack_m688 != 1) { result = v_rip - 11110764; }
    v_stack_m660 = result;
    v_stack_m640 = v_xmm0;
    local_r14 = v_rip - 11238336;
    if (*(uint64_t *)(v_stack_m660 + 0x350) != 0) { local_r14 = *(uint64_t *)(v_stack_m660 + 0x350); }
    result = EtwpQueryProcessCommandLine(v_stack_m660, v_stack_m640, Arg3, v_stack_m5E0);
    if ((uint16_t)(v_stack_m640) != 0) goto loc_00ABAB52;
    result = RtlInitUnicodeString(v_stack_m640, v_rip + 277185, Arg3, v_stack_m5E0);
    goto loc_00ABAB57;
loc_00ABAB2E:
    local_r12 = 0;
    if (0 >= ((uint16_t)((uint32_t)((uint32_t)(result))))) goto loc_00ABAAC5;
    Arg3 = ((uint16_t)((uint32_t)((uint32_t)(result)))) << (3);
    Arg2 = 0;
    result = memset(v_stack_m3A8, Arg2, Arg3, v_stack_m5E0);
    goto loc_00ABAAC5;
loc_00ABAB52:
    v_stack_m698 = 1;
loc_00ABAB57:
    local_r10 = v_stack_m658;
    if (v_stack_m658 == 0) {
        Arg2 = v_rip + 277112;
        Arg1 = v_stack_m5F0;
        result = RtlInitUnicodeString(Arg1, Arg2, Arg3, v_stack_m5E0);
        local_r10 = v_stack_m5F0;
    }
    if (local_r14 == 0) goto loc_00ABABBD;
    if ((uint16_t)(*(uint16_t *)(local_r14)) == 0) goto loc_00ABABBD;
    result = (uint16_t)((*(uint16_t *)(local_r14)) >> (1));
    v_stack_m694 = (uint16_t)(result);
    v_stack_m328 = v_stack_m694;
    v_stack_m320 = 2;
    goto loc_00ABABE0;
loc_00ABABBD:
    v_stack_m694 = 6;
    v_stack_m328 = v_stack_m694;
    v_stack_m320 = 2;
loc_00ABABE0:
    v_stack_m310 = (uint32_t)((uint32_t)((uint32_t)(6 + 6)));
    v_stack_m658 = v_stack_m638;
    v_stack_m318 = v_rip + 314212;
    v_stack_m30C = 0;
    v_stack_m300 = 2;
    if ((uint16_t)(v_stack_m640) == 0) goto loc_00ABAC28;
    v_stack_m2F8 = v_stack_m638;
    v_stack_m308 = v_stack_m690;
    local_rdi = (uint16_t)((v_stack_m640) >> (1));
    goto loc_00ABAC41;
loc_00ABAC28:
    v_stack_m2F8 = v_rip + 314212;
    v_stack_m308 = v_stack_m690;
loc_00ABAC41:
    v_stack_m690 = 6;
    v_stack_m2F0 = (uint32_t)((uint32_t)((uint32_t)(6 + 6)));
    v_stack_m2EC = 0;
    result = EtwpTiFillProcessIdentity(v_stack_m2E8, v_stack_m660, v_stack_m628, 6 + 6);
    Arg1 = ((uint32_t)((uint32_t)(result + 4 * 1))) + ((uint32_t)((uint32_t)(result + 4 * 1)));
    Arg2 = (uint32_t)((result + 4 * 1) + (1));
    *(uint64_t *)(v_stack_m5C8 + Arg1 * 8 + 0x2A0) = v_stack_p18;
    *(uint64_t *)(v_stack_m5C8 + Arg1 * 8 + 0x2A8) = 4;
    if (local_r10 == 0) goto loc_00ABACB3;
    if ((uint16_t)(*(uint16_t *)(local_r10)) == 0) goto loc_00ABACB3;
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(local_r10))) >> (1));
    goto loc_00ABACBF;
loc_00ABACB3:
    Arg3 = (uint32_t)((Arg2 + 1) + (2));
loc_00ABACBF:
    v_stack_m68C = 6;
    result = ((uint32_t)((uint32_t)(Arg2))) << (4);
    Arg2 = ((uint32_t)(Arg3)) << (4);
    local_rdi = 0;
    *(uint64_t *)(v_stack_m328 + result * 1) = v_stack_m68C;
    *(uint32_t *)(v_stack_m5C8 + result * 1 + 0x2A8) = 2;
    *(uint32_t *)(v_stack_m328 + result * 1 + 0xC) = 0;
    *(uint64_t *)(arg2 + v_stack_m328 * 1) = v_rip + 314212;
    *(uint32_t *)(v_stack_m5C8 + arg2 * 1 + 0x2A8) = (uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(local_r10))));
    *(uint32_t *)(arg2 + v_stack_m328 * 1 + 0xC) = 0;
    result = ((uint32_t)((uint32_t)(Arg3 + 1))) + ((uint32_t)((uint32_t)(Arg3 + 1)));
    *(uint64_t *)(v_stack_m5C8 + result * 8 + 0x2A8) = 4;
    *(uint64_t *)(v_stack_m5C8 + result * 8 + 0x2A0) = v_stack_m668;
    v_stack_m696 = (uint16_t)(v_stack_m676);
loc_00ABAD56:
    if (0 >= ((uint16_t)((uint32_t)((uint32_t)(result))))) goto loc_00ABADC4;
    if (result == 0) goto loc_00ABADC4;
    if (result == 0) goto loc_00ABAD93;
    if (*(uint64_t *)(result + 0x8) == 0) goto loc_00ABAD93;
    if ((uint16_t)(*(uint16_t *)(result)) == 0) goto loc_00ABAD93;
    Arg3 = ((uint32_t)((uint32_t)(Arg3 + 1 + 1))) << (4);
    local_rdi = (uint32_t)((uint32_t)(*(uint16_t *)(result))) + 2;
    if (((uint32_t)(*(uint16_t *)(result + 0x2))) <= ((uint32_t)(*(uint16_t *)(result) + 1))) { local_rdi = (uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(result)))); }
    goto loc_00ABADA6;
loc_00ABAD93:
    Arg3 = ((uint32_t)((uint32_t)(Arg3 + 1 + 1))) << (4);
loc_00ABADA6:
    *(uint64_t *)(Arg3 + v_stack_m328 * 1) = v_rip + 313667;
    *(uint32_t *)(v_stack_m5C8 + Arg3 * 1 + 0x2A8) = 14;
    local_rdi = 0;
    *(uint32_t *)(Arg3 + v_stack_m328 * 1 + 0xC) = 0;
    goto loc_00ABAE23;
loc_00ABADC4:
    if (v_stack_m670 == 0) goto loc_00ABAE02;
    if ((uint16_t)(v_stack_m678) == 0) goto loc_00ABAE02;
    Arg4 = ((uint32_t)((uint32_t)(Arg3 + 1 + 1))) + ((uint32_t)((uint32_t)(Arg3 + 1 + 1)));
    Arg2 = v_stack_m678 + 2;
    if (((uint32_t)((uint16_t)(Arg3))) <= ((uint32_t)(v_stack_m678 + 1))) { Arg2 = (uint32_t)(v_stack_m678); }
    *(uint32_t *)(v_stack_m5C8 + Arg4 * 8 + 0x2A8) = (uint32_t)(Arg2);
    *(uint64_t *)(v_stack_m5C8 + Arg4 * 8 + 0x2A0) = v_stack_m670;
    *(uint32_t *)(v_stack_m5C8 + Arg4 * 8 + 0x2AC) = 0;
    goto loc_00ABAE23;
loc_00ABAE02:
    result = ((uint32_t)((uint32_t)(Arg3 + 1 + 1))) + ((uint32_t)((uint32_t)(Arg3 + 1 + 1)));
    *(uint64_t *)(v_stack_m5C8 + result * 8 + 0x2A0) = v_rip + 313556;
    *(uint64_t *)(v_stack_m5C8 + result * 8 + 0x2A8) = 14;
loc_00ABAE23:
    local_r14 = (uint16_t)((0) + 1);
    local_r11 = (result) + (80);
    result = ((uint32_t)((uint32_t)(1 + Arg3 + 1 + 1 * 1))) + ((uint32_t)((uint32_t)(1 + Arg3 + 1 + 1 * 1)));
    *(uint64_t *)(v_stack_m5C8 + result * 8 + 0x2A0) = v_stack_m3A8;
    local_r13 = (v_stack_m3A8) + (8);
    *(uint64_t *)(v_stack_m5C8 + result * 8 + 0x2A8) = 8;
    if (((uint16_t)(local_r14)) < 16) goto loc_00ABAD56;
    Arg3 = 0;
    v_stack_m6A8 = v_stack_m328;
    result = EtwWrite(*(uint64_t *)(v_rip + 0x4449AC), v_stack_m660, Arg3, (uint32_t)((uint32_t)(1 + Arg3 + 1 + 1 * 1 + 1)));
    if (result == 0) goto loc_00ABB1CB;
    if ((*(uint32_t *)(v_rip + 0x34E2C6)) <= 5) goto loc_00ABB2D1;
    result = tlgKeywordOn(v_rip + 3465903, v_stack_m660, 5, (uint32_t)((uint32_t)(1 + Arg3 + 1 + 1 * 1 + 1)));
    if ((uint8_t)(result) == 0) goto loc_00ABB2D1;
    v_stack_m620 = 0x2000000ULL;
    v_stack_m588 = v_stack_m620;
    v_stack_m684 = (uint32_t)((uint32_t)(v_stack_p18));
    v_stack_m578 = v_stack_m684;
    v_stack_m680 = (uint32_t)((uint32_t)(v_stack_m688));
    v_stack_m568 = v_stack_m680;
    v_stack_m696 = Arg5;
    v_stack_m558 = v_stack_m696;
    v_stack_m580 = 8;
    v_stack_m570 = 5 - 1;
    v_stack_m560 = 5 - 1;
    v_stack_m550 = 5 - 4;
    if (((uint16_t)((uint32_t)((uint32_t)(result)))) <= ((uint16_t)(5 - 4))) goto loc_00ABAF38;
    if ((*(uint64_t *)(result + 0x58)) == 0) {
        Arg1 = v_stack_m678;
    }
    v_stack_m52C = 0;
    v_stack_m548 = v_stack_m530;
    v_stack_m538 = *(uint64_t *)(Arg1 + 0x8);
    v_stack_m530 = (uint32_t)(*(uint16_t *)(Arg1));
    v_stack_m618 = v_stack_m3A0;
    v_stack_m528 = v_stack_m618;
    v_stack_m540 = 2;
    v_stack_m520 = 8;
    if (((uint16_t)((uint32_t)((uint32_t)(result)))) <= 2) goto loc_00ABAFA7;
    if ((*(uint64_t *)(result + 0xA8)) == 0) {
        Arg1 = v_stack_m678;
    }
    v_stack_m510 = 2;
    v_stack_m518 = v_stack_m500;
    v_stack_m508 = *(uint64_t *)(Arg1 + 0x8);
    v_stack_m500 = (uint32_t)(*(uint16_t *)(Arg1));
    v_stack_m610 = v_stack_m398;
    v_stack_m4F8 = v_stack_m610;
    v_stack_m4FC = 0;
    v_stack_m4F0 = 8;
    if (((uint16_t)((uint32_t)((uint32_t)(result)))) <= 3) goto loc_00ABB012;
    if ((*(uint64_t *)(result + 0xF8)) == 0) {
        Arg1 = v_stack_m678;
    }
    v_stack_m4E0 = 2;
    v_stack_m4E8 = v_stack_m4D0;
    v_stack_m4D8 = *(uint64_t *)(Arg1 + 0x8);
    v_stack_m4D0 = (uint32_t)(*(uint16_t *)(Arg1));
    v_stack_m608 = v_stack_m390;
    v_stack_m4C8 = v_stack_m608;
    v_stack_m4CC = 0;
    v_stack_m4C0 = 8;
    if (((uint16_t)((uint32_t)((uint32_t)(result)))) <= ((uint16_t)(5 - 1))) goto loc_00ABB07D;
    if ((*(uint64_t *)(result + 0x148)) == 0) {
        Arg1 = v_stack_m678;
    }
    v_stack_m4B0 = 2;
    v_stack_m4B8 = v_stack_m4A0;
    v_stack_m4A8 = *(uint64_t *)(Arg1 + 0x8);
    v_stack_m4A0 = (uint32_t)(*(uint16_t *)(Arg1));
    v_stack_m600 = v_stack_m388;
    v_stack_m498 = v_stack_m600;
    v_stack_m49C = 0;
    v_stack_m490 = 8;
    if (((uint16_t)((uint32_t)((uint32_t)(result)))) <= 5) goto loc_00ABB0E8;
    if ((*(uint64_t *)(result + 0x198)) == 0) {
        Arg1 = v_stack_m678;
    }
    v_stack_m480 = 2;
    v_stack_m488 = v_stack_m470;
    v_stack_m478 = *(uint64_t *)(Arg1 + 0x8);
    v_stack_m470 = (uint32_t)(*(uint16_t *)(Arg1));
    v_stack_m5F8 = v_stack_m380;
    v_stack_m468 = v_stack_m5F8;
    v_stack_m46C = 0;
    v_stack_m460 = 8;
    if (((uint16_t)((uint32_t)((uint32_t)(result)))) <= 6) goto loc_00ABB157;
    if ((*(uint64_t *)(result + 0x1E8)) == 0) {
        Arg1 = v_stack_m678;
    }
    v_stack_m450 = 2;
    v_stack_m458 = v_stack_m440;
    v_stack_m448 = *(uint64_t *)(Arg1 + 0x8);
    v_stack_m440 = (uint32_t)(*(uint16_t *)(Arg1));
    v_stack_m650 = v_stack_m378;
    v_stack_m438 = v_stack_m650;
    v_stack_m6A0 = v_stack_m5A8;
    v_stack_m6A8 = 24;
    v_stack_m43C = 0;
    v_stack_m430 = 8;
    goto loc_00ABB2BF;
loc_00ABB1CB:
    if ((*(uint32_t *)(v_rip + 0x34DF96)) <= 5) goto loc_00ABB2D1;
    result = tlgKeywordOn(v_rip + 3465087, v_rip - 10903784, 5, (uint32_t)((uint32_t)(1 + Arg3 + 1 + 1 * 1 + 1)));
    if ((uint8_t)(result) == 0) goto loc_00ABB2D1;
    v_stack_m650 = 0x2000000ULL;
    v_stack_m408 = v_stack_m650;
    v_stack_m680 = (uint32_t)((uint32_t)(v_stack_p18));
    v_stack_m3F8 = v_stack_m680;
    v_stack_m684 = (uint32_t)((uint32_t)(v_stack_m688));
    v_stack_m3E8 = v_stack_m684;
    v_stack_m696 = Arg5;
    v_stack_m3D8 = v_stack_m696;
    v_stack_m3C8 = v_stack_m3B0;
    v_stack_m6A0 = v_stack_m428;
    v_stack_m6A8 = 8;
    v_stack_m400 = 8;
    v_stack_m3F0 = 4;
    v_stack_m3E0 = 4;
    v_stack_m3D0 = 1;
    v_stack_m3C0 = 2;
    v_stack_m3B8 = v_stack_m670;
    v_stack_m3B0 = (uint32_t)(v_stack_m678);
    v_stack_m3AC = 0;
loc_00ABB2BF:
    Arg4 = 0;
    Arg3 = 0;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 3464863, v_rip - 10903133, Arg3, Arg4);
loc_00ABB2D1:
    if (v_stack_m698 != 0) {
        Arg1 = v_stack_m658;
        Arg2 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    result = v_stack_m648;
    if (v_stack_m648 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m648;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (0x690ULL);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x7B0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ABA7E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
