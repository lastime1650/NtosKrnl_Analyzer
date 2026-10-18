# RtlValidAcl

- RVA: `0x0092A7A0`–`0x0092AB3C` (길이 `924` bytes)
- VA: `0x000000014092A7A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008DB20`
- 디코드: `234`개 명령, `924/924` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **26**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0092A993` → [RtlpValidRelativeAttribute](../A6/RtlpValidRelativeAttribute_function_00A68428.md) (function, `0x00A68428`)

### Direct callers
- [RtlAddAccessFilterAce](../78/RtlAddAccessFilterAce_function_0078D210.md) at `0x0078D264`
- [RtlAddMandatoryAccessAllowedAce](../78/RtlAddMandatoryAccessAllowedAce_function_0078D530.md) at `0x0078D565`
- [RtlAddMandatoryAppAccessAllowedAce](../78/RtlAddMandatoryAppAccessAllowedAce_function_0078D670.md) at `0x0078D6F4`
- [RtlAddResourceAttributeAce](../78/RtlAddResourceAttributeAce_function_0078D7F0.md) at `0x0078D9DF`
- [RtlpAddKnownObjectAce](../78/RtlpAddKnownObjectAce_function_0078DBB4.md) at `0x0078DC4F`
- [SddlAddAccessFilterAce](../7A/SddlAddAccessFilterAce_function_007A4D58.md) at `0x007A4DB1`
- [SddlAddProcessTrustLabelAce](../7A/SddlAddProcessTrustLabelAce_function_007A4F94.md) at `0x007A4FD7`
- [SddlAddScopedPolicyIDAce](../7A/SddlAddScopedPolicyIDAce_function_007A50F4.md) at `0x007A51A2`
- [CMFCreateSecurityDescriptor](../7D/CMFCreateSecurityDescriptor_function_007D2B10.md) at `0x007D3002`
- [SepAppendAceToTokenObjectAcl](../8B/SepAppendAceToTokenObjectAcl_function_008B6430.md) at `0x008B66D6`
- [SepAppendAceToTokenObjectAcl](../8B/SepAppendAceToTokenObjectAcl_function_008B6430.md) at `0x008B67E6`
- [SepCreateImpersonationTokenDacl](../8B/SepCreateImpersonationTokenDacl_function_008B8140.md) at `0x008B8272`
- [SepCreateImpersonationTokenDacl](../8B/SepCreateImpersonationTokenDacl_function_008B8140.md) at `0x008B82F8`
- [SepCreateImpersonationTokenDacl](../8B/SepCreateImpersonationTokenDacl_function_008B8140.md) at `0x008B837B`
- [SepCreateImpersonationTokenDacl](../8B/SepCreateImpersonationTokenDacl_function_008B8140.md) at `0x008B840E`
- [SepCreateImpersonationTokenDacl](../8B/SepCreateImpersonationTokenDacl_function_008B8140.md) at `0x008B84C1`
- [SepCreateImpersonationTokenDacl](../8B/SepCreateImpersonationTokenDacl_function_008B8140.md) at `0x008B8537`
- [RtlValidSecurityDescriptor](../8B/RtlValidSecurityDescriptor_function_008BD3F0.md) at `0x008BD485`
- [RtlValidSecurityDescriptor](../8B/RtlValidSecurityDescriptor_function_008BD3F0.md) at `0x008BD4B6`
- [RtlValidRelativeSecurityDescriptor](../8B/RtlValidRelativeSecurityDescriptor_function_008BDC70.md) at `0x008BDD5F`
- [RtlValidRelativeSecurityDescriptor](../8B/RtlValidRelativeSecurityDescriptor_function_008BDC70.md) at `0x008BDDC0`
- [SeValidSecurityDescriptor](../8B/SeValidSecurityDescriptor_function_008BED60.md) at `0x008BEED6`
- [SeValidSecurityDescriptor](../8B/SeValidSecurityDescriptor_function_008BED60.md) at `0x008BEF58`
- [RtlAddAccessAllowedAceEx](RtlAddAccessAllowedAceEx_function_009279D0.md) at `0x00927A61`
- [LocalGetAclForString](LocalGetAclForString_function_00927F30.md) at `0x009284B8`
- [RtlAddProcessTrustLabelAce](RtlAddProcessTrustLabelAce_function_00929740.md) at `0x0092976F`
- [sub_00929936](Unknown_function_00929936.md) at `0x00929944`
- [sub_00929A97](Unknown_function_00929A97.md) at `0x00929AB6`
- [RtlAddMandatoryAce](RtlAddMandatoryAce_function_00929BA0.md) at `0x00929C76`
- [RtlAddAce](RtlAddAce_function_00929D70.md) at `0x00929D98`
- [SeCaptureSecurityDescriptor](SeCaptureSecurityDescriptor_function_00929F40.md) at `0x0092A342`
- [SeCaptureSecurityDescriptor](SeCaptureSecurityDescriptor_function_00929F40.md) at `0x0092A564`
- [SepCheckAcl](SepCheckAcl_function_0092A770.md) at `0x0092A781`
- [RtlpNewSecurityObject](RtlpNewSecurityObject_function_0092AB50.md) at `0x0092B9A3`
- [SddlAddMandatoryAce](../9A/SddlAddMandatoryAce_function_009A98AC.md) at `0x009A9957`
- [RtlDeleteAce](../A7/RtlDeleteAce_function_00A76040.md) at `0x00A76054`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0092A7A0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0092A7A5  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0092A7AA  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0092A7AF  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0092A7B4  41 54                           push r12
0092A7B6  41 56                           push r14
0092A7B8  41 57                           push r15
0092A7BA  48 83 EC 20                     sub rsp, 0x20
0092A7BE  0F B6 01                        movzx eax, byte ptr [rcx]
0092A7C1  48 8B F9                        mov rdi, rcx
0092A7C4  2C 02                           sub al, 2
0092A7C6  3C 02                           cmp al, 2
0092A7C8  0F 87 D2 01 00 00               ja 0x14092a9a0
0092A7CE  48 8D 41 03                     lea rax, [rcx + 3]
0092A7D2  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0092A7D6  4C 8D 71 02                     lea r14, [rcx + 2]
0092A7DA  49 3B C6                        cmp rax, r14
0092A7DD  0F 85 BD 01 00 00               jne 0x14092a9a0
0092A7E3  66 41 83 3E 08                  cmp word ptr [r14], 8
0092A7E8  0F 82 B2 01 00 00               jb 0x14092a9a0
0092A7EE  33 ED                           xor ebp, ebp
0092A7F0  48 8D 59 08                     lea rbx, [rcx + 8]
0092A7F4  66 3B 69 04                     cmp bp, word ptr [rcx + 4]
0092A7F8  0F 83 37 03 00 00               jae 0x14092ab35
0092A7FE  41 BF 0F 66 9A 00               mov r15d, 0x9a660f
0092A804  44 8D 65 0C                     lea r12d, [rbp + 0xc]
0092A808  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
0092A810  41 0F B7 16                     movzx edx, word ptr [r14]
0092A814  48 8D 43 04                     lea rax, [rbx + 4]
0092A818  48 03 D7                        add rdx, rdi
0092A81B  48 3B C2                        cmp rax, rdx
0092A81E  0F 87 7C 01 00 00               ja 0x14092a9a0
0092A824  48 8D 43 03                     lea rax, [rbx + 3]
0092A828  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0092A82C  48 8D 73 02                     lea rsi, [rbx + 2]
0092A830  48 3B C6                        cmp rax, rsi
0092A833  0F 85 67 01 00 00               jne 0x14092a9a0
0092A839  0F B7 06                        movzx eax, word ptr [rsi]
0092A83C  48 8D 0C 18                     lea rcx, [rax + rbx]
0092A840  48 3B CA                        cmp rcx, rdx
0092A843  0F 87 57 01 00 00               ja 0x14092a9a0
0092A849  0F B6 13                        movzx edx, byte ptr [rbx]
0092A84C  80 FA 17                        cmp dl, 0x17
0092A84F  77 47                           ja 0x14092a898
0092A851  41 0F A3 D7                     bt r15d, edx
0092A855  73 41                           jae 0x14092a898
0092A857  48 8D 48 03                     lea rcx, [rax + 3]
0092A85B  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
0092A85F  48 3B C8                        cmp rcx, rax
0092A862  0F 85 38 01 00 00               jne 0x14092a9a0
0092A868  83 F8 10                        cmp eax, 0x10
0092A86B  0F 82 2F 01 00 00               jb 0x14092a9a0
0092A871  80 7B 08 01                     cmp byte ptr [rbx + 8], 1
0092A875  0F 85 25 01 00 00               jne 0x14092a9a0
0092A87B  0F B6 4B 09                     movzx ecx, byte ptr [rbx + 9]
0092A87F  80 F9 0F                        cmp cl, 0xf
0092A882  0F 87 18 01 00 00               ja 0x14092a9a0
0092A888  48 8D 0C 8D 10 00 00 00         lea rcx, [rcx*4 + 0x10]
0092A890  48 3B C1                        cmp rax, rcx
0092A893  E9 83 02 00 00                  jmp 0x14092ab1b
0092A898  80 FA 04                        cmp dl, 4
0092A89B  0F 85 80 00 00 00               jne 0x14092a921
0092A8A1  80 3F 03                        cmp byte ptr [rdi], 3
0092A8A4  0F 82 F6 00 00 00               jb 0x14092a9a0
0092A8AA  48 8D 48 03                     lea rcx, [rax + 3]
0092A8AE  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
0092A8B2  48 3B C8                        cmp rcx, rax
0092A8B5  0F 85 E5 00 00 00               jne 0x14092a9a0
0092A8BB  83 F8 18                        cmp eax, 0x18
0092A8BE  0F 82 DC 00 00 00               jb 0x14092a9a0
0092A8C4  66 83 7B 08 01                  cmp word ptr [rbx + 8], 1
0092A8C9  0F 85 D1 00 00 00               jne 0x14092a9a0
0092A8CF  80 7B 0C 01                     cmp byte ptr [rbx + 0xc], 1
0092A8D3  0F 85 C7 00 00 00               jne 0x14092a9a0
0092A8D9  0F B6 4B 0D                     movzx ecx, byte ptr [rbx + 0xd]
0092A8DD  80 F9 0F                        cmp cl, 0xf
0092A8E0  0F 87 BA 00 00 00               ja 0x14092a9a0
0092A8E6  48 8D 14 8D 08 00 00 00         lea rdx, [rcx*4 + 8]
0092A8EE  48 8D 4A 18                     lea rcx, [rdx + 0x18]
0092A8F2  48 3B C1                        cmp rax, rcx
0092A8F5  0F 82 A5 00 00 00               jb 0x14092a9a0
0092A8FB  80 7C 1A 0C 01                  cmp byte ptr [rdx + rbx + 0xc], 1
0092A900  0F 85 9A 00 00 00               jne 0x14092a9a0
0092A906  0F B6 4C 1A 0D                  movzx ecx, byte ptr [rdx + rbx + 0xd]
0092A90B  80 F9 0F                        cmp cl, 0xf
0092A90E  0F 87 8C 00 00 00               ja 0x14092a9a0
0092A914  48 8D 14 8A                     lea rdx, [rdx + rcx*4]
0092A918  48 83 C2 14                     add rdx, 0x14
0092A91C  E9 F7 01 00 00                  jmp 0x14092ab18
0092A921  8D 4A FB                        lea ecx, [rdx - 5]
0092A924  80 F9 03                        cmp cl, 3
0092A927  0F 86 68 01 00 00               jbe 0x14092aa95
0092A92D  8D 4A F5                        lea ecx, [rdx - 0xb]
0092A930  80 F9 01                        cmp cl, 1
0092A933  0F 86 5C 01 00 00               jbe 0x14092aa95
0092A939  8D 4A F1                        lea ecx, [rdx - 0xf]
0092A93C  80 F9 01                        cmp cl, 1
0092A93F  0F 86 50 01 00 00               jbe 0x14092aa95
0092A945  80 FA 12                        cmp dl, 0x12
0092A948  75 78                           jne 0x14092a9c2
0092A94A  48 8D 48 03                     lea rcx, [rax + 3]
0092A94E  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
0092A952  48 3B C8                        cmp rcx, rax
0092A955  75 49                           jne 0x14092a9a0
0092A957  83 F8 10                        cmp eax, 0x10
0092A95A  72 44                           jb 0x14092a9a0
0092A95C  80 7B 08 01                     cmp byte ptr [rbx + 8], 1
0092A960  4C 8D 43 08                     lea r8, [rbx + 8]
0092A964  75 3A                           jne 0x14092a9a0
0092A966  41 0F B6 48 01                  movzx ecx, byte ptr [r8 + 1]
0092A96B  80 F9 0F                        cmp cl, 0xf
0092A96E  77 30                           ja 0x14092a9a0
0092A970  44 8D 0C 8D 08 00 00 00         lea r9d, [rcx*4 + 8]
0092A978  41 8D 51 08                     lea edx, [r9 + 8]
0092A97C  48 83 C2 14                     add rdx, 0x14
0092A980  48 3B C2                        cmp rax, rdx
0092A983  72 1B                           jb 0x14092a9a0
0092A985  8B D0                           mov edx, eax
0092A987  41 8B C9                        mov ecx, r9d
0092A98A  41 2B D1                        sub edx, r9d
0092A98D  49 03 C8                        add rcx, r8
0092A990  83 EA 08                        sub edx, 8
0092A993  E8 90 DA 13 00                  call 0x140a68428
0092A998  84 C0                           test al, al
0092A99A  0F 85 81 01 00 00               jne 0x14092ab21
0092A9A0  32 C0                           xor al, al
0092A9A2  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0092A9A7  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
0092A9AC  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0092A9B1  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
0092A9B6  48 83 C4 20                     add rsp, 0x20
0092A9BA  41 5F                           pop r15
0092A9BC  41 5E                           pop r14
0092A9BE  41 5C                           pop r12
0092A9C0  C3                              ret
0092A9C1  CC                              int3
0092A9C2  80 FA 15                        cmp dl, 0x15
0092A9C5  75 49                           jne 0x14092aa10
0092A9C7  48 8D 48 03                     lea rcx, [rax + 3]
0092A9CB  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
0092A9CF  48 3B C8                        cmp rcx, rax
0092A9D2  75 CC                           jne 0x14092a9a0
0092A9D4  83 F8 10                        cmp eax, 0x10
0092A9D7  72 C7                           jb 0x14092a9a0
0092A9D9  80 7B 08 01                     cmp byte ptr [rbx + 8], 1
0092A9DD  75 C1                           jne 0x14092a9a0
0092A9DF  0F B6 4B 09                     movzx ecx, byte ptr [rbx + 9]
0092A9E3  80 F9 0F                        cmp cl, 0xf
0092A9E6  77 B8                           ja 0x14092a9a0
0092A9E8  8D 51 02                        lea edx, [rcx + 2]
0092A9EB  8B C8                           mov ecx, eax
0092A9ED  66 C1 E2 02                     shl dx, 2
0092A9F1  0F B7 C2                        movzx eax, dx
0092A9F4  2B C8                           sub ecx, eax
0092A9F6  83 E9 08                        sub ecx, 8
0092A9F9  83 F9 06                        cmp ecx, 6
0092A9FC  7C A2                           jl 0x14092a9a0
0092A9FE  0F B7 C2                        movzx eax, dx
0092AA01  81 7C 18 08 61 72 74 78         cmp dword ptr [rax + rbx + 8], 0x78747261
0092AA09  75 95                           jne 0x14092a9a0
0092AA0B  E9 11 01 00 00                  jmp 0x14092ab21
0092AA10  80 FA 16                        cmp dl, 0x16
0092AA13  75 78                           jne 0x14092aa8d
0092AA15  48 8D 48 03                     lea rcx, [rax + 3]
0092AA19  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
0092AA1D  48 3B C8                        cmp rcx, rax
0092AA20  0F 85 7A FF FF FF               jne 0x14092a9a0
0092AA26  83 F8 14                        cmp eax, 0x14
0092AA29  0F 82 71 FF FF FF               jb 0x14092a9a0
0092AA2F  80 7B 08 01                     cmp byte ptr [rbx + 8], 1
0092AA33  0F 85 67 FF FF FF               jne 0x14092a9a0
0092AA39  0F B6 4B 09                     movzx ecx, byte ptr [rbx + 9]
0092AA3D  80 F9 0F                        cmp cl, 0xf
0092AA40  0F 87 5A FF FF FF               ja 0x14092a9a0
0092AA46  8D 14 8D 10 00 00 00            lea edx, [rcx*4 + 0x10]
0092AA4D  44 8B C9                        mov r9d, ecx
0092AA50  49 03 D4                        add rdx, r12
0092AA53  48 3B C2                        cmp rax, rdx
0092AA56  0F 82 44 FF FF FF               jb 0x14092a9a0
0092AA5C  8D 0C 8D 08 00 00 00            lea ecx, [rcx*4 + 8]
0092AA63  80 7C 19 08 01                  cmp byte ptr [rcx + rbx + 8], 1
0092AA68  0F 85 32 FF FF FF               jne 0x14092a9a0
0092AA6E  0F B6 4C 19 09                  movzx ecx, byte ptr [rcx + rbx + 9]
0092AA73  80 F9 0F                        cmp cl, 0xf
0092AA76  0F 87 24 FF FF FF               ja 0x14092a9a0
0092AA7C  41 03 C9                        add ecx, r9d
0092AA7F  8D 14 8D 18 00 00 00            lea edx, [rcx*4 + 0x18]
0092AA86  3B C2                           cmp eax, edx
0092AA88  E9 8E 00 00 00                  jmp 0x14092ab1b
0092AA8D  83 F8 04                        cmp eax, 4
0092AA90  E9 86 00 00 00                  jmp 0x14092ab1b
0092AA95  80 3F 04                        cmp byte ptr [rdi], 4
0092AA98  0F 82 02 FF FF FF               jb 0x14092a9a0
0092AA9E  48 8D 48 03                     lea rcx, [rax + 3]
0092AAA2  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
0092AAA6  48 3B C8                        cmp rcx, rax
0092AAA9  0F 85 F1 FE FF FF               jne 0x14092a9a0
0092AAAF  41 3B C4                        cmp eax, r12d
0092AAB2  0F 82 E8 FE FF FF               jb 0x14092a9a0
0092AAB8  44 8B 43 08                     mov r8d, dword ptr [rbx + 8]
0092AABC  45 8B C8                        mov r9d, r8d
0092AABF  41 83 E1 01                     and r9d, 1
0092AAC3  41 8B D1                        mov edx, r9d
0092AAC6  C1 E2 04                        shl edx, 4
0092AAC9  41 83 E0 02                     and r8d, 2
0092AACD  8D 4A 10                        lea ecx, [rdx + 0x10]
0092AAD0  0F 44 CA                        cmove ecx, edx
0092AAD3  44 8B D1                        mov r10d, ecx
0092AAD6  48 83 C1 18                     add rcx, 0x18
0092AADA  48 3B C1                        cmp rax, rcx
0092AADD  0F 82 BD FE FF FF               jb 0x14092a9a0
0092AAE3  45 85 C0                        test r8d, r8d
0092AAE6  41 8B D1                        mov edx, r9d
0092AAE9  B9 1C 00 00 00                  mov ecx, 0x1c
0092AAEE  49 0F 44 CC                     cmove rcx, r12
0092AAF2  48 03 D2                        add rdx, rdx
0092AAF5  48 03 CB                        add rcx, rbx
0092AAF8  80 3C D1 01                     cmp byte ptr [rcx + rdx*8], 1
0092AAFC  0F 85 9E FE FF FF               jne 0x14092a9a0
0092AB02  0F B6 4C D1 01                  movzx ecx, byte ptr [rcx + rdx*8 + 1]
0092AB07  80 F9 0F                        cmp cl, 0xf
0092AB0A  0F 87 90 FE FF FF               ja 0x14092a9a0
0092AB10  48 8D 51 05                     lea rdx, [rcx + 5]
0092AB14  49 8D 14 92                     lea rdx, [r10 + rdx*4]
0092AB18  48 3B C2                        cmp rax, rdx
0092AB1B  0F 82 7F FE FF FF               jb 0x14092a9a0
0092AB21  0F B7 06                        movzx eax, word ptr [rsi]
0092AB24  FF C5                           inc ebp
0092AB26  48 03 D8                        add rbx, rax
0092AB29  0F B7 47 04                     movzx eax, word ptr [rdi + 4]
0092AB2D  3B E8                           cmp ebp, eax
0092AB2F  0F 82 DB FC FF FF               jb 0x14092a810
0092AB35  B0 01                           mov al, 1
0092AB37  E9 66 FE FF FF                  jmp 0x14092a9a2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlValidAcl(__int64 a1)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_stack_p20 = v_rdi;
    v_rsp = (v_rsp) - (32);
    result = (unsigned __int8)((*(unsigned __int8 *)(a1)) - (2));
    if (((unsigned __int8)(result)) > 2) goto loc_0092A9A0;
    result = (a1 + 3) & (-2);
    if (result != (a1 + 2)) goto loc_0092A9A0;
    if ((*(unsigned __int16 *)(a1 + 2)) < 8) goto loc_0092A9A0;
    v_rbp = 0;
    if (0 >= (*(unsigned __int16 *)(a1 + 4))) goto loc_0092AB35;
loc_0092A810:
    a2 = (*(unsigned __int16 *)(a1 + 2)) + (a1);
    if ((a1 + 8 + 4) > a2) goto loc_0092A9A0;
    result = (a1 + 8 + 3) & (-2);
    if (result != (a1 + 8 + 2)) goto loc_0092A9A0;
    if ((*(unsigned __int16 *)(a1 + 8 + 2) + a1 + 8 * 1) > a2) goto loc_0092A9A0;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 8))) > 23) goto loc_0092A898;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 8))) >= 23) goto loc_0092A898;
    a1 = (*(unsigned __int16 *)(a1 + 8 + 2) + 3) & (-4);
    if (a1 != (*(unsigned __int16 *)(a1 + 8 + 2))) goto loc_0092A9A0;
    if (((unsigned int)(*(unsigned __int16 *)(a1 + 8 + 2))) < 16) goto loc_0092A9A0;
    if ((*(unsigned __int8 *)(a1 + 8 + 8)) != 1) goto loc_0092A9A0;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 8 + 9))) > 15) goto loc_0092A9A0;
    goto loc_0092AB1B;
loc_0092A898:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 8))) != 4) goto loc_0092A921;
    if ((*(unsigned __int8 *)(a1)) < 3) goto loc_0092A9A0;
    a1 = (*(unsigned __int16 *)(a1 + 8 + 2) + 3) & (-4);
    if (a1 != (*(unsigned __int16 *)(a1 + 8 + 2))) goto loc_0092A9A0;
    if (((unsigned int)(*(unsigned __int16 *)(a1 + 8 + 2))) < 24) goto loc_0092A9A0;
    if ((*(unsigned __int16 *)(a1 + 8 + 8)) != 1) goto loc_0092A9A0;
    if ((*(unsigned __int8 *)(a1 + 8 + 12)) != 1) goto loc_0092A9A0;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 8 + 13))) > 15) goto loc_0092A9A0;
    if ((*(unsigned __int16 *)(a1 + 8 + 2)) < (*(unsigned __int8 *)(a1 + 8 + 13) * 4 + 8 + 24)) goto loc_0092A9A0;
    if ((*(unsigned __int8 *)(*(unsigned __int8 *)(a1 + 8 + 13) * 4 + 8 + a1 + 8 * 1 + 12)) != 1) goto loc_0092A9A0;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(a1 + 8 + 13) * 4 + 8 + a1 + 8 * 1 + 13))) > 15) goto loc_0092A9A0;
    a2 = (*(unsigned __int8 *)(a1 + 8 + 13) * 4 + 8 + *(unsigned __int8 *)(*(unsigned __int8 *)(a1 + 8 + 13) * 4 + 8 + a1 + 8 * 1 + 13) * 4) + (20);
    goto loc_0092AB18;
loc_0092A921:
    if (((unsigned __int8)(a2 - 5)) <= 3) goto loc_0092AA95;
    if (((unsigned __int8)(a2 - 11)) <= 1) goto loc_0092AA95;
    if (((unsigned __int8)(a2 - 15)) <= 1) goto loc_0092AA95;
    if (((unsigned __int8)(a2)) != 18) goto loc_0092A9C2;
    a1 = (*(unsigned __int16 *)(a1 + 8 + 2) + 3) & (-4);
    if (a1 != (*(unsigned __int16 *)(a1 + 8 + 2))) goto loc_0092A9A0;
    if (((unsigned int)(*(unsigned __int16 *)(a1 + 8 + 2))) < 16) goto loc_0092A9A0;
    if ((*(unsigned __int8 *)(a1 + 8 + 8)) != 1) goto loc_0092A9A0;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 8 + 8 + 1))) > 15) goto loc_0092A9A0;
    a2 = (*(unsigned __int8 *)(a1 + 8 + 8 + 1) * 4 + 8 + 8) + (20);
    if ((*(unsigned __int16 *)(a1 + 8 + 2)) < a2) goto loc_0092A9A0;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(a1 + 8 + 2)))) - ((unsigned int)(*(unsigned __int8 *)(a1 + 8 + 8 + 1) * 4 + 8)));
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 8 + 8 + 1) * 4 + 8))) + (a1 + 8 + 8);
    a2 = (unsigned int)((a2) - (8));
    result = RtlpValidRelativeAttribute(a1, a2, a1 + 8 + 8, *(unsigned __int8 *)(a1 + 8 + 8 + 1) * 4 + 8);
    if ((unsigned __int8)(result) != 0) goto loc_0092AB21;
loc_0092A9A0:
    result = 0;
loc_0092A9A2:
    v_rsp = (v_rsp) + (32);
    return result;
loc_0092A9C2:
    if (((unsigned __int8)(a2)) != 21) goto loc_0092AA10;
    a1 = (result + 3) & (-4);
    if (a1 != 0) goto loc_0092A9A0;
    if (0 < 16) goto loc_0092A9A0;
    if ((*(unsigned __int8 *)(v_stack_p8 + 8)) != 1) goto loc_0092A9A0;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 9))) > 15) goto loc_0092A9A0;
    a2 = (unsigned __int16)((*(unsigned __int8 *)(v_stack_p8 + 9) + 2) << (2));
    a1 = (unsigned int)((0) - ((unsigned int)((unsigned __int16)(a2))));
    a1 = (unsigned int)((a1) - (8));
    if (((unsigned int)(a1)) < 6) goto loc_0092A9A0;
    if ((*(unsigned int *)((unsigned __int16)(a2) + v_stack_p8 * 1 + 8)) != 0x78747261ULL) goto loc_0092A9A0;
    goto loc_0092AB21;
loc_0092AA10:
    if (((unsigned __int8)(a2)) != 22) goto loc_0092AA8D;
    a1 = ((unsigned __int16)(a2) + 3) & (-4);
    if (a1 != ((unsigned __int16)(a2))) goto loc_0092A9A0;
    if (((unsigned int)((unsigned __int16)(a2))) < 20) goto loc_0092A9A0;
    if ((*(unsigned __int8 *)(v_stack_p8 + 8)) != 1) goto loc_0092A9A0;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 9))) > 15) goto loc_0092A9A0;
    a2 = (*(unsigned __int8 *)(v_stack_p8 + 9) * 4 + 16) + (v_rbp + 12);
    if (((unsigned __int16)(a2)) < a2) goto loc_0092A9A0;
    if ((*(unsigned __int8 *)(*(unsigned __int8 *)(v_stack_p8 + 9) * 4 + 8 + v_stack_p8 * 1 + 8)) != 1) goto loc_0092A9A0;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(v_stack_p8 + 9) * 4 + 8 + v_stack_p8 * 1 + 9))) > 15) goto loc_0092A9A0;
    a1 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int8 *)(v_stack_p8 + 9) * 4 + 8 + v_stack_p8 * 1 + 9)) + ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_stack_p8 + 9))))));
    goto loc_0092AB1B;
loc_0092AA8D:
    goto loc_0092AB1B;
loc_0092AA95:
    if ((*(unsigned __int8 *)(v_stack_p20)) < 4) goto loc_0092A9A0;
    a1 = ((unsigned __int16)(a2) + 3) & (-4);
    if (a1 != ((unsigned __int16)(a2))) goto loc_0092A9A0;
    if (((unsigned int)((unsigned __int16)(a2))) < ((unsigned int)(v_rbp + 12))) goto loc_0092A9A0;
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 8))))) & (1));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a4))) << (4));
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 8))) & (2));
    a1 = a2 + 16;
    if (condition_is_equal) { a1 = (unsigned int)(a2); }
    a1 = (a1) + (24);
    if (((unsigned __int16)(a2)) < a1) goto loc_0092A9A0;
    a1 = 28;
    if ((unsigned int)(a3) == 0) { a1 = v_rbp + 12; }
    a2 = ((unsigned int)((unsigned int)(a4))) + ((unsigned int)((unsigned int)(a4)));
    a1 = (a1) + (v_stack_p8);
    if ((*(unsigned __int8 *)(a1 + a2 * 8)) != 1) goto loc_0092A9A0;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + a2 * 8 + 1))) > 15) goto loc_0092A9A0;
loc_0092AB18:
loc_0092AB1B:
    if (((unsigned __int16)(a2)) < ((unsigned int)((unsigned int)(a1)) + *(unsigned __int8 *)(a1 + a2 * 8 + 1) + 5 * 4)) goto loc_0092A9A0;
loc_0092AB21:
    v_rbp = (unsigned int)((v_stack_p10) + 1);
    v_rbx = (v_stack_p8) + (*(unsigned __int16 *)(v_stack_p18));
    if (((unsigned int)(v_rbp)) < ((unsigned int)(*(unsigned __int16 *)(v_stack_p20 + 4)))) goto loc_0092A810;
loc_0092AB35:
    goto loc_0092A9A2;
}
```

## 5. (Beta) C Style

```c
int64_t RtlValidAcl(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    v_stack_p20 = local_rdi;
    local_rsp = (local_rsp) - (32);
    result = (uint8_t)((*(uint8_t *)(arg1)) - (2));
    if (((uint8_t)(result)) > 2) goto loc_0092A9A0;
    result = (Arg1 + 3) & (-2);
    if (result != (Arg1 + 2)) goto loc_0092A9A0;
    if ((*(uint16_t *)(arg1 + 0x2)) < 8) goto loc_0092A9A0;
    local_rbp = 0;
    if (0 >= (*(uint16_t *)(arg1 + 0x4))) goto loc_0092AB35;
loc_0092A810:
    a2 = (*(uint16_t *)(arg1 + 0x2)) + (Arg1);
    if ((Arg1 + 8 + 4) > a2) goto loc_0092A9A0;
    result = (Arg1 + 8 + 3) & (-2);
    if (result != (Arg1 + 8 + 2)) goto loc_0092A9A0;
    if ((*(uint16_t *)(arg1 + 0x8 + 0x2) + Arg1 + 8 * 1) > a2) goto loc_0092A9A0;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x8))) > 23) goto loc_0092A898;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x8))) >= 23) goto loc_0092A898;
    Arg1 = (*(uint16_t *)(arg1 + 0x8 + 0x2) + 3) & (-4);
    if (Arg1 != (*(uint16_t *)(arg1 + 0x8 + 0x2))) goto loc_0092A9A0;
    if (((uint32_t)(*(uint16_t *)(arg1 + 0x8 + 0x2))) < 16) goto loc_0092A9A0;
    if ((*(uint8_t *)(arg1 + 0x8 + 0x8)) != 1) goto loc_0092A9A0;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x8 + 0x9))) > 15) goto loc_0092A9A0;
    goto loc_0092AB1B;
loc_0092A898:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x8))) != 4) goto loc_0092A921;
    if ((*(uint8_t *)(arg1)) < 3) goto loc_0092A9A0;
    Arg1 = (*(uint16_t *)(arg1 + 0x8 + 0x2) + 3) & (-4);
    if (Arg1 != (*(uint16_t *)(arg1 + 0x8 + 0x2))) goto loc_0092A9A0;
    if (((uint32_t)(*(uint16_t *)(arg1 + 0x8 + 0x2))) < 24) goto loc_0092A9A0;
    if ((*(uint16_t *)(arg1 + 0x8 + 0x8)) != 1) goto loc_0092A9A0;
    if ((*(uint8_t *)(arg1 + 0x8 + 0xC)) != 1) goto loc_0092A9A0;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x8 + 0xD))) > 15) goto loc_0092A9A0;
    if ((*(uint16_t *)(arg1 + 0x8 + 0x2)) < (*(uint8_t *)(arg1 + 0x8 + 0xD) * 4 + 8 + 24)) goto loc_0092A9A0;
    if ((*(uint8_t *)(*(uint8_t *)(arg1 + 0x8 + 0xD) * 4 + 0x8 + arg1 + 0x8 * 1 + 0xC)) != 1) goto loc_0092A9A0;
    if (((uint8_t)(*(uint8_t *)(*(uint8_t *)(arg1 + 0x8 + 0xD) * 4 + 0x8 + arg1 + 0x8 * 1 + 0xD))) > 15) goto loc_0092A9A0;
    a2 = (*(uint8_t *)(arg1 + 0x8 + 0xD) * 4 + 8 + *(uint8_t *)(*(uint8_t *)(arg1 + 0x8 + 0xD) * 4 + 0x8 + arg1 + 0x8 * 1 + 0xD) * 4) + (20);
    goto loc_0092AB18;
loc_0092A921:
    if (((uint8_t)(a2 - 5)) <= 3) goto loc_0092AA95;
    if (((uint8_t)(a2 - 11)) <= 1) goto loc_0092AA95;
    if (((uint8_t)(a2 - 15)) <= 1) goto loc_0092AA95;
    if (((uint8_t)(a2)) != 18) goto loc_0092A9C2;
    Arg1 = (*(uint16_t *)(arg1 + 0x8 + 0x2) + 3) & (-4);
    if (Arg1 != (*(uint16_t *)(arg1 + 0x8 + 0x2))) goto loc_0092A9A0;
    if (((uint32_t)(*(uint16_t *)(arg1 + 0x8 + 0x2))) < 16) goto loc_0092A9A0;
    if ((*(uint8_t *)(arg1 + 0x8 + 0x8)) != 1) goto loc_0092A9A0;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x8 + 0x8 + 0x1))) > 15) goto loc_0092A9A0;
    a2 = (*(uint8_t *)(arg1 + 0x8 + 0x8 + 0x1) * 4 + 8 + 8) + (20);
    if ((*(uint16_t *)(arg1 + 0x8 + 0x2)) < a2) goto loc_0092A9A0;
    a2 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(arg1 + 0x8 + 0x2)))) - ((uint32_t)(*(uint8_t *)(arg1 + 0x8 + 0x8 + 0x1) * 4 + 8)));
    Arg1 = ((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0x8 + 0x8 + 0x1) * 4 + 8))) + (Arg1 + 8 + 8);
    a2 = (uint32_t)((a2) - (8));
    result = RtlpValidRelativeAttribute(Arg1, a2, Arg1 + 8 + 8, *(uint8_t *)(arg1 + 0x8 + 0x8 + 0x1) * 4 + 8);
    if ((uint8_t)(result) != 0) goto loc_0092AB21;
loc_0092A9A0:
    result = 0;
loc_0092A9A2:
    local_rsp = (local_rsp) + (32);
    return result;
loc_0092A9C2:
    if (((uint8_t)(a2)) != 21) goto loc_0092AA10;
    Arg1 = (result + 3) & (-4);
    if (Arg1 != NULL) goto loc_0092A9A0;
    if (0 < 16) goto loc_0092A9A0;
    if ((*(uint8_t *)(v_stack_p8 + 0x8)) != 1) goto loc_0092A9A0;
    if (((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x9))) > 15) goto loc_0092A9A0;
    a2 = (uint16_t)((*(uint8_t *)(v_stack_p8 + 0x9) + 2) << (2));
    Arg1 = (uint32_t)((0) - ((uint32_t)((uint16_t)(a2))));
    Arg1 = (uint32_t)((Arg1) - (8));
    if (((uint32_t)(Arg1)) < 6) goto loc_0092A9A0;
    if ((*(uint32_t *)((uint16_t)(a2) + v_stack_p8 * 1 + 0x8)) != 0x78747261ULL) goto loc_0092A9A0;
    goto loc_0092AB21;
loc_0092AA10:
    if (((uint8_t)(a2)) != 22) goto loc_0092AA8D;
    Arg1 = ((uint16_t)(a2) + 3) & (-4);
    if (Arg1 != ((uint16_t)(a2))) goto loc_0092A9A0;
    if (((uint32_t)((uint16_t)(a2))) < 20) goto loc_0092A9A0;
    if ((*(uint8_t *)(v_stack_p8 + 0x8)) != 1) goto loc_0092A9A0;
    if (((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x9))) > 15) goto loc_0092A9A0;
    a2 = (*(uint8_t *)(v_stack_p8 + 0x9) * 4 + 16) + (local_rbp + 12);
    if (((uint16_t)(a2)) < a2) goto loc_0092A9A0;
    if ((*(uint8_t *)(*(uint8_t *)(v_stack_p8 + 0x9) * 4 + 0x8 + v_stack_p8 * 1 + 0x8)) != 1) goto loc_0092A9A0;
    if (((uint8_t)(*(uint8_t *)(*(uint8_t *)(v_stack_p8 + 0x9) * 4 + 0x8 + v_stack_p8 * 1 + 0x9))) > 15) goto loc_0092A9A0;
    Arg1 = (uint32_t)((*(uint8_t *)(*(uint8_t *)(v_stack_p8 + 0x9) * 4 + 0x8 + v_stack_p8 * 1 + 0x9)) + ((uint32_t)((uint32_t)((uint32_t)(*(uint8_t *)(v_stack_p8 + 0x9))))));
    goto loc_0092AB1B;
loc_0092AA8D:
    goto loc_0092AB1B;
loc_0092AA95:
    if ((*(uint8_t *)(v_stack_p20)) < 4) goto loc_0092A9A0;
    Arg1 = ((uint16_t)(a2) + 3) & (-4);
    if (Arg1 != ((uint16_t)(a2))) goto loc_0092A9A0;
    if (((uint32_t)((uint16_t)(a2))) < ((uint32_t)(local_rbp + 12))) goto loc_0092A9A0;
    a4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x8))))) & (1));
    a2 = (uint32_t)(((uint32_t)((uint32_t)(a4))) << (4));
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x8))) & (2));
    Arg1 = a2 + 16;
    if (condition_is_equal) { Arg1 = (uint32_t)(a2); }
    Arg1 = (Arg1) + (24);
    if (((uint16_t)(a2)) < Arg1) goto loc_0092A9A0;
    Arg1 = 28;
    if ((uint32_t)(a3) == 0) { Arg1 = local_rbp + 12; }
    a2 = ((uint32_t)((uint32_t)(a4))) + ((uint32_t)((uint32_t)(a4)));
    Arg1 = (Arg1) + (v_stack_p8);
    if ((*(uint8_t *)(arg1 + a2 * 8)) != 1) goto loc_0092A9A0;
    if (((uint8_t)(*(uint8_t *)(arg1 + a2 * 8 + 0x1))) > 15) goto loc_0092A9A0;
loc_0092AB18:
loc_0092AB1B:
    if (((uint16_t)(a2)) < ((uint32_t)((uint32_t)(Arg1)) + *(uint8_t *)(arg1 + a2 * 8 + 0x1) + 5 * 4)) goto loc_0092A9A0;
loc_0092AB21:
    local_rbp = (uint32_t)((v_stack_p10) + 1);
    local_rbx = (v_stack_p8) + (*(uint16_t *)(v_stack_p18));
    if (((uint32_t)(local_rbp)) < ((uint32_t)(*(uint16_t *)(v_stack_p20 + 0x4)))) goto loc_0092A810;
loc_0092AB35:
    goto loc_0092A9A2;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x1` | `8` | `R` |
| `Arg1` | `+ 0x2` | `64` | `R` |
| `Arg1` | `+ 0x3` | `64` | `R` |
| `Arg1` | `+ 0x4` | `16` | `R` |
| `Arg1` | `+ 0x4` | `64` | `R` |
| `Arg1` | `+ 0x8` | `8` | `R` |
| `Arg1` | `+ 0x8` | `16` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x9` | `8` | `R` |
| `Arg1` | `+ 0xC` | `8` | `R` |
| `Arg1` | `+ 0xD` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0092A7A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
