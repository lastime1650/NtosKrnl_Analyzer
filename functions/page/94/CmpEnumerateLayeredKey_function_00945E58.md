# CmpEnumerateLayeredKey

- RVA: `0x00945E58`–`0x00946483` (길이 `1,579` bytes)
- VA: `0x0000000140945E58`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00090968`
- 디코드: `395`개 명령, `1,579/1,579` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **38**; 고유 호출 대상: **32**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00945EC0` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00945EF6` → [CmpKeyEnumStackInitialize](CmpKeyEnumStackInitialize_function_00946D38.md) (function, `0x00946D38`)
- `0x00945F07` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x00945F15` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x00945F25` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (function, `0x0042A7F0`)
- `0x00945F42` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x00945F50` → [CmpStartKcbStackForTopLayerKcb](../84/CmpStartKcbStackForTopLayerKcb_function_00848390.md) (function, `0x00848390`)
- `0x00945F63` → [CmpLockKcbStackShared](CmpLockKcbStackShared_function_00948000.md) (function, `0x00948000`)
- `0x00945F72` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (function, `0x00BC97D0`)
- `0x00946019` → [CmpKeyEnumStackStartFromKcbStack](CmpKeyEnumStackStartFromKcbStack_function_00944F18.md) (function, `0x00944F18`)
- `0x00946038` → [CmpKeyEnumStackAdvance](CmpKeyEnumStackAdvance_function_0094668C.md) (function, `0x0094668C`)
- `0x0094604F` → [CmpIsRegistryLockContended](../../text/4F/CmpIsRegistryLockContended_function_004FB868.md) (function, `0x004FB868`)
- `0x00946062` → [CmpKeyEnumStackAdvance](CmpKeyEnumStackAdvance_function_0094668C.md) (function, `0x0094668C`)
- `0x00946098` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (function, `0x003CD504`)
- `0x009460FB` → [CmpReferenceKeyControlBlockUnsafe](../87/CmpReferenceKeyControlBlockUnsafe_function_00874DA0.md) (function, `0x00874DA0`)
- `0x0094617B` → [CmpQueryKeyDataFromKeyNodeStack](../../text/46/CmpQueryKeyDataFromKeyNodeStack_function_0046AC40.md) (function, `0x0046AC40`)
- `0x009461A0` → [CmpKeyEnumStackCleanup](CmpKeyEnumStackCleanup_function_00946868.md) (function, `0x00946868`)
- `0x009461C4` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x009461E4` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x009461F7` → [CmpUnlockKcbStack](../84/CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x00946205` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x00946235` → [CmpDereferenceKeyControlBlock](../85/CmpDereferenceKeyControlBlock_function_00851310.md) (function, `0x00851310`)
- `0x00946250` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x0094625B` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (function, `0x0041B9A0`)
- `0x00946260` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00946271` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009462B9` → [CmpGetKeyNodeForKcb](../85/CmpGetKeyNodeForKcb_function_00856480.md) (function, `0x00856480`)
- `0x009462D0` → [CmpFindSubKeyByNumber](../85/CmpFindSubKeyByNumber_function_0085C930.md) (function, `0x0085C930`)
- `0x00946308` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00946341` → [CmpQueryKeyDataFromNode](../84/CmpQueryKeyDataFromNode_function_0084EAE0.md) (function, `0x0084EAE0`)
- `0x00946354` → [CmpLockRegistryExclusive](../84/CmpLockRegistryExclusive_function_0084F9B4.md) (function, `0x0084F9B4`)
- `0x00946365` → [CmpKeyEnumStackVerifyResumeContext](CmpKeyEnumStackVerifyResumeContext_function_0094962C.md) (function, `0x0094962C`)
- `0x00946397` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x009463B0` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x009463FC` → [CmpKeyEnumStackCreateResumeContext](CmpKeyEnumStackCreateResumeContext_function_00948050.md) (function, `0x00948050`)
- `0x0094642A` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00946434` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00946479` → [CmpKeyEnumStackFreeResumeContext](../A6/CmpKeyEnumStackFreeResumeContext_function_00A6DDD8.md) (function, `0x00A6DDD8`)

### Direct callers
- [sub_0084E7D5](../84/Unknown_function_0084E7D5.md) at `0x0084E8C1`

### Static image references
- `0x00945E77` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **13**
  - `0x00945EC0` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00945F25` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (`PAGE` → `.text`)
  - `0x00945F42` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x00945F72` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (`PAGE` → `PAGECMRC`)
  - `0x0094604F` → [CmpIsRegistryLockContended](../../text/4F/CmpIsRegistryLockContended_function_004FB868.md) (`PAGE` → `.text`)
  - `0x00946098` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (`PAGE` → `.text`)
  - `0x0094617B` → [CmpQueryKeyDataFromKeyNodeStack](../../text/46/CmpQueryKeyDataFromKeyNodeStack_function_0046AC40.md) (`PAGE` → `.text`)
  - `0x00946205` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x00946250` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x0094625B` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (`PAGE` → `.text`)
  - `0x00946260` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x00946271` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00946397` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00945E58  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00945E5D  55                              push rbp
00945E5E  56                              push rsi
00945E5F  57                              push rdi
00945E60  41 54                           push r12
00945E62  41 55                           push r13
00945E64  41 56                           push r14
00945E66  41 57                           push r15
00945E68  48 8D AC 24 A0 FE FF FF         lea rbp, [rsp - 0x160]
00945E70  48 81 EC 60 02 00 00            sub rsp, 0x260
00945E77  48 8B 05 C2 48 4C 00            mov rax, qword ptr [rip + 0x4c48c2]
00945E7E  48 33 C4                        xor rax, rsp
00945E81  48 89 85 50 01 00 00            mov qword ptr [rbp + 0x150], rax
00945E88  48 8B 85 C8 01 00 00            mov rax, qword ptr [rbp + 0x1c8]
00945E8F  45 8B F0                        mov r14d, r8d
00945E92  48 8B BD D0 01 00 00            mov rdi, qword ptr [rbp + 0x1d0]
00945E99  44 8B EA                        mov r13d, edx
00945E9C  44 89 45 A0                     mov dword ptr [rbp - 0x60], r8d
00945EA0  4C 8B E1                        mov r12, rcx
00945EA3  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
00945EA7  33 D2                           xor edx, edx
00945EA9  41 B8 60 01 00 00               mov r8d, 0x160
00945EAF  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00945EB3  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00945EB7  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
00945EBC  4C 89 4D C8                     mov qword ptr [rbp - 0x38], r9
00945EC0  E8 7B 0D D8 FF                  call 0x1406c6c40
00945EC5  33 DB                           xor ebx, ebx
00945EC7  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00945ECB  0F 57 C9                        xorps xmm1, xmm1
00945ECE  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
00945ED3  0F 57 C0                        xorps xmm0, xmm0
00945ED6  89 5C 24 60                     mov dword ptr [rsp + 0x60], ebx
00945EDA  83 C8 FF                        or eax, 0xffffffff
00945EDD  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
00945EE2  0F 11 4D 80                     movups xmmword ptr [rbp - 0x80], xmm1
00945EE6  66 89 45 82                     mov word ptr [rbp - 0x7e], ax
00945EEA  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
00945EEE  88 5C 24 40                     mov byte ptr [rsp + 0x40], bl
00945EF2  0F 11 4D 90                     movups xmmword ptr [rbp - 0x70], xmm1
00945EF6  E8 3D 0E 00 00                  call 0x140946d38
00945EFB  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00945F00  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
00945F05  8B F3                           mov esi, ebx
00945F07  E8 04 00 F1 FF                  call 0x140855f10
00945F0C  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00945F11  48 89 5D B0                     mov qword ptr [rbp - 0x50], rbx
00945F15  E8 F6 FF F0 FF                  call 0x140855f10
00945F1A  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00945F1E  48 89 5D A8                     mov qword ptr [rbp - 0x58], rbx
00945F22  44 8B FB                        mov r15d, ebx
00945F25  E8 C6 48 AE FF                  call 0x14042a7f0
00945F2A  48 8B 1F                        mov rbx, qword ptr [rdi]
00945F2D  41 8D 47 02                     lea eax, [r15 + 2]
00945F31  4C 21 3F                        and qword ptr [rdi], r15
00945F34  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
00945F39  44 3B F0                        cmp r14d, eax
00945F3C  0F 84 12 04 00 00               je 0x140946354
00945F42  E8 ED 3B 28 00                  call 0x140bc9b34
00945F47  49 8B 54 24 08                  mov rdx, qword ptr [r12 + 8]
00945F4C  48 8D 4D 80                     lea rcx, [rbp - 0x80]
00945F50  E8 3B 24 F0 FF                  call 0x140848390
00945F55  8B F8                           mov edi, eax
00945F57  85 C0                           test eax, eax
00945F59  0F 88 30 04 00 00               js 0x14094638f
00945F5F  48 8D 4D 80                     lea rcx, [rbp - 0x80]
00945F63  E8 98 20 00 00                  call 0x140948000
00945F68  33 D2                           xor edx, edx
00945F6A  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
00945F6F  49 8B CC                        mov rcx, r12
00945F72  E8 59 38 28 00                  call 0x140bc97d0
00945F77  8B F8                           mov edi, eax
00945F79  85 C0                           test eax, eax
00945F7B  0F 88 0E 04 00 00               js 0x14094638f
00945F81  48 0F BF 4D 82                  movsx rcx, word ptr [rbp - 0x7e]
00945F86  40 8A D6                        mov dl, sil
00945F89  66 85 C9                        test cx, cx
00945F8C  0F 8E 18 03 00 00               jle 0x1409462aa
00945F92  4C 8B 4D 98                     mov r9, qword ptr [rbp - 0x68]
00945F96  48 8D 45 88                     lea rax, [rbp - 0x78]
00945F9A  4C 2B C8                        sub r9, rax
00945F9D  4C 8D 45 88                     lea r8, [rbp - 0x78]
00945FA1  41 83 CA FF                     or r10d, 0xffffffff
00945FA5  4D 8D 04 C8                     lea r8, [r8 + rcx*8]
00945FA9  45 8D 5A 03                     lea r11d, [r10 + 3]
00945FAD  66 41 3B CB                     cmp cx, r11w
00945FB1  0F 83 87 04 00 00               jae 0x14094643e
00945FB7  49 8B C0                        mov rax, r8
00945FBA  4C 8B 20                        mov r12, qword ptr [rax]
00945FBD  B8 01 00 00 00                  mov eax, 1
00945FC2  0F B6 D2                        movzx edx, dl
00945FC5  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
00945FCA  41 83 7C 24 28 FF               cmp dword ptr [r12 + 0x28], -1
00945FD0  0F 45 D0                        cmovne edx, eax
00945FD3  66 41 03 CA                     add cx, r10w
00945FD7  49 83 E8 08                     sub r8, 8
00945FDB  66 85 C9                        test cx, cx
00945FDE  7F CD                           jg 0x140945fad
00945FE0  4C 8B 65 B8                     mov r12, qword ptr [rbp - 0x48]
00945FE4  84 D2                           test dl, dl
00945FE6  0F 84 BE 02 00 00               je 0x1409462aa
00945FEC  48 85 DB                        test rbx, rbx
00945FEF  0F 85 69 03 00 00               jne 0x14094635e
00945FF5  48 8B DE                        mov rbx, rsi
00945FF8  49 87 5C 24 58                  xchg qword ptr [r12 + 0x58], rbx
00945FFD  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
00946002  48 85 DB                        test rbx, rbx
00946005  0F 85 53 03 00 00               jne 0x14094635e
0094600B  4C 8B CB                        mov r9, rbx
0094600E  48 8D 55 80                     lea rdx, [rbp - 0x80]
00946012  4D 8B C4                        mov r8, r12
00946015  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00946019  E8 FA EE FF FF                  call 0x140944f18
0094601E  8B F8                           mov edi, eax
00946020  85 C0                           test eax, eax
00946022  0F 88 64 01 00 00               js 0x14094618c
00946028  48 85 DB                        test rbx, rbx
0094602B  0F 85 61 02 00 00               jne 0x140946292
00946031  44 8B F6                        mov r14d, esi
00946034  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00946038  E8 4F 06 00 00                  call 0x14094668c
0094603D  8B F8                           mov edi, eax
0094603F  85 C0                           test eax, eax
00946041  0F 88 45 01 00 00               js 0x14094618c
00946047  41 8B F6                        mov esi, r14d
0094604A  41 3B F5                        cmp esi, r13d
0094604D  73 26                           jae 0x140946075
0094604F  E8 14 58 BB FF                  call 0x1404fb868
00946054  33 C9                           xor ecx, ecx
00946056  84 C0                           test al, al
00946058  0F 85 66 03 00 00               jne 0x1409463c4
0094605E  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00946062  E8 25 06 00 00                  call 0x14094668c
00946067  8B F8                           mov edi, eax
00946069  85 C0                           test eax, eax
0094606B  0F 88 1B 01 00 00               js 0x14094618c
00946071  FF C6                           inc esi
00946073  EB D5                           jmp 0x14094604a
00946075  4C 0F BF 6D 82                  movsx r13, word ptr [rbp - 0x7e]
0094607A  41 B8 43 4D 37 37               mov r8d, 0x37374d43
00946080  4A 8D 0C 6D 00 00 00 00         lea rcx, [r13*2]
00946088  49 03 CD                        add rcx, r13
0094608B  48 8D 14 CD 20 00 00 00         lea rdx, [rcx*8 + 0x20]
00946093  B9 00 01 00 00                  mov ecx, 0x100
00946098  E8 67 74 A8 FF                  call 0x1403cd504
0094609D  48 8B F8                        mov rdi, rax
009460A0  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
009460A4  33 C0                           xor eax, eax
009460A6  48 85 FF                        test rdi, rdi
009460A9  0F 84 B1 00 00 00               je 0x140946160
009460AF  89 77 04                        mov dword ptr [rdi + 4], esi
009460B2  44 0F B7 F0                     movzx r14d, ax
009460B6  66 44 89 2F                     mov word ptr [rdi], r13w
009460BA  88 47 02                        mov byte ptr [rdi + 2], al
009460BD  66 41 3B C5                     cmp ax, r13w
009460C1  0F 8F 91 00 00 00               jg 0x140946158
009460C7  48 8D 4D 88                     lea rcx, [rbp - 0x78]
009460CB  4C 8D 67 08                     lea r12, [rdi + 8]
009460CF  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
009460D4  48 8B 7D 98                     mov rdi, qword ptr [rbp - 0x68]
009460D8  44 8D 78 02                     lea r15d, [rax + 2]
009460DC  41 0F BF C6                     movsx eax, r14w
009460E0  66 45 3B F7                     cmp r14w, r15w
009460E4  0F 8D 60 03 00 00               jge 0x14094644a
009460EA  48 C1 E0 07                     shl rax, 7
009460EE  48 8D 75 48                     lea rsi, [rbp + 0x48]
009460F2  48 03 F0                        add rsi, rax
009460F5  48 8B 19                        mov rbx, qword ptr [rcx]
009460F8  48 8B CB                        mov rcx, rbx
009460FB  E8 A0 EC F2 FF                  call 0x140874da0
00946100  49 8D 4C 24 10                  lea rcx, [r12 + 0x10]
00946105  49 2B F4                        sub rsi, r12
00946108  48 89 59 F8                     mov qword ptr [rcx - 8], rbx
0094610C  49 8B D7                        mov rdx, r15
0094610F  48 8B 83 30 01 00 00            mov rax, qword ptr [rbx + 0x130]
00946116  41 BD 01 00 00 00               mov r13d, 1
0094611C  49 89 04 24                     mov qword ptr [r12], rax
00946120  8B 44 0E 08                     mov eax, dword ptr [rsi + rcx + 8]
00946124  89 01                           mov dword ptr [rcx], eax
00946126  48 8D 49 04                     lea rcx, [rcx + 4]
0094612A  49 2B D5                        sub rdx, r13
0094612D  75 F1                           jne 0x140946120
0094612F  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00946134  66 45 03 F5                     add r14w, r13w
00946138  48 83 C1 08                     add rcx, 8
0094613C  49 83 C4 18                     add r12, 0x18
00946140  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
00946145  66 44 3B 75 82                  cmp r14w, word ptr [rbp - 0x7e]
0094614A  7E 90                           jle 0x1409460dc
0094614C  48 8B 7D D0                     mov rdi, qword ptr [rbp - 0x30]
00946150  4C 8B 7D A8                     mov r15, qword ptr [rbp - 0x58]
00946154  4C 8B 65 B8                     mov r12, qword ptr [rbp - 0x48]
00946158  48 8B DF                        mov rbx, rdi
0094615B  49 87 5C 24 58                  xchg qword ptr [r12 + 0x58], rbx
00946160  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
00946164  48 8D 4D F8                     lea rcx, [rbp - 8]
00946168  44 8B 8D C0 01 00 00            mov r9d, dword ptr [rbp + 0x1c0]
0094616F  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
00946173  8B 55 A0                        mov edx, dword ptr [rbp - 0x60]
00946176  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0094617B  E8 C0 4A B2 FF                  call 0x14046ac40
00946180  8B F8                           mov edi, eax
00946182  33 C0                           xor eax, eax
00946184  85 FF                           test edi, edi
00946186  0F 89 15 02 00 00               jns 0x1409463a1
0094618C  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00946191  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
00946196  41 BD 01 00 00 00               mov r13d, 1
0094619C  48 8D 4D F0                     lea rcx, [rbp - 0x10]
009461A0  E8 C3 06 00 00                  call 0x140946868
009461A5  45 33 F6                        xor r14d, r14d
009461A8  4C 39 75 B0                     cmp qword ptr [rbp - 0x50], r14
009461AC  74 1B                           je 0x1409461c9
009461AE  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
009461B2  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
009461B7  44 84 A9 8C 00 00 00            test byte ptr [rcx + 0x8c], r13b
009461BE  0F 85 66 02 00 00               jne 0x14094642a
009461C4  E8 77 FD F0 FF                  call 0x140855f40
009461C9  4D 85 E4                        test r12, r12
009461CC  74 1B                           je 0x1409461e9
009461CE  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
009461D2  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
009461D7  44 84 A9 8C 00 00 00            test byte ptr [rcx + 0x8c], r13b
009461DE  0F 85 50 02 00 00               jne 0x140946434
009461E4  E8 57 FD F0 FF                  call 0x140855f40
009461E9  45 33 E4                        xor r12d, r12d
009461EC  44 38 64 24 40                  cmp byte ptr [rsp + 0x40], r12b
009461F1  74 09                           je 0x1409461fc
009461F3  48 8D 4D 80                     lea rcx, [rbp - 0x80]
009461F7  E8 64 22 F0 FF                  call 0x140848460
009461FC  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
00946200  48 85 C9                        test rcx, rcx
00946203  74 05                           je 0x14094620a
00946205  E8 76 FB B2 FF                  call 0x140475d80
0094620A  48 85 DB                        test rbx, rbx
0094620D  0F 85 5C 02 00 00               jne 0x14094646f
00946213  4D 85 FF                        test r15, r15
00946216  74 3D                           je 0x140946255
00946218  41 0F B7 07                     movzx eax, word ptr [r15]
0094621C  66 44 3B E0                     cmp r12w, ax
00946220  7F 21                           jg 0x140946243
00946222  66 41 03 C5                     add ax, r13w
00946226  49 8D 5F 10                     lea rbx, [r15 + 0x10]
0094622A  0F B7 F0                        movzx esi, ax
0094622D  48 8B 0B                        mov rcx, qword ptr [rbx]
00946230  48 85 C9                        test rcx, rcx
00946233  74 05                           je 0x14094623a
00946235  E8 D6 B0 F0 FF                  call 0x140851310
0094623A  48 83 C3 18                     add rbx, 0x18
0094623E  49 2B F5                        sub rsi, r13
00946241  75 EA                           jne 0x14094622d
00946243  49 8B CF                        mov rcx, r15
00946246  45 38 67 02                     cmp byte ptr [r15 + 2], r12b
0094624A  0F 85 47 01 00 00               jne 0x140946397
00946250  E8 2B FB B2 FF                  call 0x140475d80
00946255  33 D2                           xor edx, edx
00946257  48 8D 4D D8                     lea rcx, [rbp - 0x28]
0094625B  E8 40 57 AD FF                  call 0x14041b9a0
00946260  E8 1F 38 28 00                  call 0x140bc9a84
00946265  8B C7                           mov eax, edi
00946267  48 8B 8D 50 01 00 00            mov rcx, qword ptr [rbp + 0x150]
0094626E  48 33 CC                        xor rcx, rsp
00946271  E8 CA 63 D6 FF                  call 0x1406ac640
00946276  48 8B 9C 24 A8 02 00 00         mov rbx, qword ptr [rsp + 0x2a8]
0094627E  48 81 C4 60 02 00 00            add rsp, 0x260
00946285  41 5F                           pop r15
00946287  41 5E                           pop r14
00946289  41 5D                           pop r13
0094628B  41 5C                           pop r12
0094628D  5F                              pop rdi
0094628E  5E                              pop rsi
0094628F  5D                              pop rbp
00946290  C3                              ret
00946291  CC                              int3
00946292  44 8B 73 04                     mov r14d, dword ptr [rbx + 4]
00946296  4C 8B FB                        mov r15, rbx
00946299  48 89 5D A8                     mov qword ptr [rbp - 0x58], rbx
0094629D  48 8B DE                        mov rbx, rsi
009462A0  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
009462A5  E9 8A FD FF FF                  jmp 0x140946034
009462AA  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
009462AE  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
009462B3  48 8B CE                        mov rcx, rsi
009462B6  45 33 C0                        xor r8d, r8d
009462B9  E8 C2 01 F1 FF                  call 0x140856480
009462BE  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
009462C2  4C 8D 4C 24 60                  lea r9, [rsp + 0x60]
009462C7  45 8B C5                        mov r8d, r13d
009462CA  48 8B D0                        mov rdx, rax
009462CD  4C 8B E0                        mov r12, rax
009462D0  E8 5B 66 F1 FF                  call 0x14085c930
009462D5  8B F8                           mov edi, eax
009462D7  85 C0                           test eax, eax
009462D9  0F 88 B7 FE FF FF               js 0x140946196
009462DF  8B 54 24 60                     mov edx, dword ptr [rsp + 0x60]
009462E3  41 BD 01 00 00 00               mov r13d, 1
009462E9  83 FA FF                        cmp edx, -1
009462EC  0F 84 C8 00 00 00               je 0x1409463ba
009462F2  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
009462F6  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
009462FB  44 84 A9 8C 00 00 00            test byte ptr [rcx + 0x8c], r13b
00946302  0F 84 A8 00 00 00               je 0x1409463b0
00946308  E8 53 E9 F0 FF                  call 0x140854c60
0094630D  4C 8B 4D C8                     mov r9, qword ptr [rbp - 0x38]
00946311  48 8B C8                        mov rcx, rax
00946314  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
00946318  48 8B D1                        mov rdx, rcx
0094631B  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
0094631F  33 C0                           xor eax, eax
00946321  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00946326  45 8B C6                        mov r8d, r14d
00946329  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0094632E  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
00946332  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00946337  8B 85 C0 01 00 00               mov eax, dword ptr [rbp + 0x1c0]
0094633D  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00946341  E8 9A 87 F0 FF                  call 0x14084eae0
00946346  8B F8                           mov edi, eax
00946348  33 C0                           xor eax, eax
0094634A  85 FF                           test edi, edi
0094634C  0F 49 F8                        cmovns edi, eax
0094634F  E9 48 FE FF FF                  jmp 0x14094619c
00946354  E8 5B 96 F0 FF                  call 0x14084f9b4
00946359  E9 E9 FB FF FF                  jmp 0x140945f47
0094635E  48 8B D3                        mov rdx, rbx
00946361  48 8D 4D 80                     lea rcx, [rbp - 0x80]
00946365  E8 C2 32 00 00                  call 0x14094962c
0094636A  3D 59 00 00 C0                  cmp eax, 0xc0000059
0094636F  74 0A                           je 0x14094637b
00946371  44 39 6B 04                     cmp dword ptr [rbx + 4], r13d
00946375  0F 86 90 FC FF FF               jbe 0x14094600b
0094637B  4C 8B FB                        mov r15, rbx
0094637E  48 89 5D A8                     mov qword ptr [rbp - 0x58], rbx
00946382  48 8B DE                        mov rbx, rsi
00946385  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
0094638A  E9 7C FC FF FF                  jmp 0x14094600b
0094638F  4C 8B E6                        mov r12, rsi
00946392  E9 FF FD FF FF                  jmp 0x140946196
00946397  E8 E4 F9 B2 FF                  call 0x140475d80
0094639C  E9 B4 FE FF FF                  jmp 0x140946255
009463A1  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
009463A6  8B F8                           mov edi, eax
009463A8  4C 8B E0                        mov r12, rax
009463AB  E9 E6 FD FF FF                  jmp 0x140946196
009463B0  E8 FB E8 F0 FF                  call 0x140854cb0
009463B5  E9 53 FF FF FF                  jmp 0x14094630d
009463BA  BF 1A 00 00 80                  mov edi, 0x8000001a
009463BF  E9 D8 FD FF FF                  jmp 0x14094619c
009463C4  8B C6                           mov eax, esi
009463C6  41 2B C6                        sub eax, r14d
009463C9  83 F8 0A                        cmp eax, 0xa
009463CC  0F 82 8C FC FF FF               jb 0x14094605e
009463D2  38 8D D8 01 00 00               cmp byte ptr [rbp + 0x1d8], cl
009463D8  0F 84 80 FC FF FF               je 0x14094605e
009463DE  48 8D 44 24 50                  lea rax, [rsp + 0x50]
009463E3  41 BD 01 00 00 00               mov r13d, 1
009463E9  45 8A CD                        mov r9b, r13b
009463EC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009463F1  44 8B C6                        mov r8d, esi
009463F4  48 8D 55 F0                     lea rdx, [rbp - 0x10]
009463F8  48 8D 4D 80                     lea rcx, [rbp - 0x80]
009463FC  E8 4F 1C 00 00                  call 0x140948050
00946401  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00946406  33 D2                           xor edx, edx
00946408  8B F8                           mov edi, eax
0094640A  44 8B E2                        mov r12d, edx
0094640D  85 C0                           test eax, eax
0094640F  78 54                           js 0x140946465
00946411  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00946416  8B DA                           mov ebx, edx
00946418  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0094641D  BF 2D 02 00 C0                  mov edi, 0xc000022d
00946422  48 89 01                        mov qword ptr [rcx], rax
00946425  E9 72 FD FF FF                  jmp 0x14094619c
0094642A  E8 F1 67 F1 FF                  call 0x14085cc20
0094642F  E9 95 FD FF FF                  jmp 0x1409461c9
00946434  E8 E7 67 F1 FF                  call 0x14085cc20
00946439  E9 AB FD FF FF                  jmp 0x1409461e9
0094643E  49 8D 41 F0                     lea rax, [r9 - 0x10]
00946442  49 03 C0                        add rax, r8
00946445  E9 70 FB FF FF                  jmp 0x140945fba
0094644A  83 C0 FE                        add eax, -2
0094644D  8B F0                           mov esi, eax
0094644F  48 98                           cdqe
00946451  48 C1 E6 07                     shl rsi, 7
00946455  48 03 B5 48 01 00 00            add rsi, qword ptr [rbp + 0x148]
0094645C  48 8D 0C C7                     lea rcx, [rdi + rax*8]
00946460  E9 90 FC FF FF                  jmp 0x1409460f5
00946465  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0094646A  E9 2D FD FF FF                  jmp 0x14094619c
0094646F  45 33 C0                        xor r8d, r8d
00946472  48 8D 55 D8                     lea rdx, [rbp - 0x28]
00946476  48 8B CB                        mov rcx, rbx
00946479  E8 5A 79 12 00                  call 0x140a6ddd8
0094647E  E9 90 FD FF FF                  jmp 0x140946213
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpEnumerateLayeredKey(__int64 a1, int a2, int a3, __int64 a4, unsigned int a5, __int64 a6, __int64 a7, unsigned __int8 a8)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned int v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int16 v_stack_m216;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned int v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int8 v_stack_m258;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (608);
    result = (*(unsigned __int64 *)(v_rip + 4999362)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m1F8 = a3;
    v_stack_m1E0 = a1;
    a2 = 0;
    v_stack_m1D8 = a6;
    v_stack_m220 = a7;
    v_stack_m1D0 = a4;
    result = memset(v_stack_m1A8, a2, 352, a4);
    v_rbx = 0;
    v_stack_m228 = 0;
    v_stack_m238 = 0;
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    v_stack_m230 = 0;
    v_stack_m218 = v_xmm1;
    v_stack_m216 = (unsigned __int16)(result);
    v_stack_m1C0 = v_xmm0;
    v_stack_m258 = 0;
    v_stack_m208 = v_xmm1;
    result = CmpKeyEnumStackInitialize(v_stack_m1A8, a2, 352, a4);
    v_stack_m250 = 0;
    result = HvpGetCellContextInitialize(v_stack_m228, a2, 352, a4);
    v_stack_m1E8 = 0;
    result = HvpGetCellContextInitialize(v_stack_m230, a2, 352, a4);
    v_stack_m1F0 = 0;
    result = CmpInitializeDelayDerefContext(v_stack_m1C0, a2, 352, a4);
    v_stack_m248 = *(unsigned __int64 *)(a7);
    if (((unsigned int)((unsigned int)(a3))) == ((unsigned int)(0 + 2))) goto loc_00946354;
    result = CmpLockRegistry(v_stack_m1C0, a2, 352, a4);
loc_00945F47:
    result = CmpStartKcbStackForTopLayerKcb(v_stack_m218, *(unsigned __int64 *)(a1 + 8), 352, a4);
    if (sign_flag) goto loc_0094638F;
    result = CmpLockKcbStackShared(v_stack_m218, *(unsigned __int64 *)(a1 + 8), 352, a4);
    a2 = 0;
    v_stack_m258 = 1;
    result = CmpPerformKeyBodyDeletionCheck(a1, a2, 352, a4);
    if (sign_flag) goto loc_0094638F;
    if (condition_is_less_or_equal) goto loc_009462AA;
    a4 = (v_stack_m200) - (v_stack_m210);
    v_r10 = (unsigned int)((v_r10) | (0xFFFFFFFFULL));
loc_00945FAD:
    if (((unsigned __int16)((__int16)(v_stack_m216))) >= ((unsigned __int16)(v_r10 + 3))) goto loc_0094643E;
loc_00945FBA:
    v_stack_m240 = *(unsigned __int64 *)(v_stack_m210 + (__int16)(v_stack_m216) * 8);
    a2 = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m210 + (__int16)(v_stack_m216) * 8) + 40)) != -1) { a2 = 1; }
    a1 = (unsigned __int16)(((__int16)(v_stack_m216)) + ((unsigned __int16)(v_r10)));
    a3 = (v_stack_m210 + (__int16)(v_stack_m216) * 8) - (8);
    if (condition_is_greater) goto loc_00945FAD;
    if ((unsigned __int8)(a2) == 0) goto loc_009462AA;
    if (*(unsigned __int64 *)(a7) != 0) goto loc_0094635E;
    v_stack_m248 = 0;
    if (0 != 0) goto loc_0094635E;
loc_0094600B:
    result = CmpKeyEnumStackStartFromKcbStack(v_stack_m1A8, v_stack_m218, v_stack_m1E0, 0);
    if (sign_flag) goto loc_0094618C;
    if (0 != 0) goto loc_00946292;
loc_00946034:
    result = CmpKeyEnumStackAdvance(v_stack_m1A8, v_stack_m218, v_stack_m1E0, 0);
    if (sign_flag) goto loc_0094618C;
loc_0094604A:
    if (0 >= ((unsigned int)((unsigned int)(a2)))) goto loc_00946075;
    result = CmpIsRegistryLockContended(v_stack_m1A8, v_stack_m218, v_stack_m1E0, 0);
    a1 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_009463C4;
loc_0094605E:
    result = CmpKeyEnumStackAdvance(v_stack_m1A8, v_stack_m218, v_stack_m1E0, 0);
    if (sign_flag) goto loc_0094618C;
    v_rsi = (unsigned int)((0) + 1);
    goto loc_0094604A;
loc_00946075:
    a1 = ((__int16)(v_stack_m216) * 2) + ((__int16)(v_stack_m216));
    result = CmpAllocatePool(256, a1 * 8 + 32, (unsigned int)(0x37374D43ULL), 0);
    v_stack_m1C8 = result;
    result = 0;
    if (0 == 0) goto loc_00946160;
    *(unsigned int *)(result + 4) = (unsigned int)(v_rsi);
    *(unsigned __int16 *)(result) = (unsigned __int16)((__int16)(v_stack_m216));
    *(unsigned __int8 *)(result + 2) = 0;
    if (0 > ((unsigned __int16)((__int16)(v_stack_m216)))) goto loc_00946158;
    v_stack_m220 = v_stack_m210;
loc_009460DC:
    if (0 >= ((unsigned __int16)(result + 2))) goto loc_0094644A;
    result = ((__int16)(0)) << (7);
    v_rsi = (v_stack_m150) + (result);
loc_009460F5:
    result = CmpReferenceKeyControlBlockUnsafe(*(unsigned __int64 *)(v_stack_m210), a1 * 8 + 32, (unsigned int)(0x37374D43ULL), 0);
    v_rsi = (v_rsi) - (result + 8);
    *(unsigned __int64 *)(result + 8 + 16 - 8) = *(unsigned __int64 *)(v_stack_m210);
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m210) + 304);
loc_00946120:
    *(unsigned int *)(result + 8 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + result + 8 + 16 * 1 + 8)));
    a2 = (result + 2) - (1);
    if (condition_is_not_equal) goto loc_00946120;
    v_r14 = (unsigned __int16)((0) + (1));
    a1 = (v_stack_m220) + (8);
    v_r12 = (result + 8) + (24);
    v_stack_m220 = a1;
    if (((unsigned __int16)(v_r14)) <= v_stack_m216) goto loc_009460DC;
loc_00946158:
loc_00946160:
    v_stack_m278 = v_stack_m1D8;
    result = CmpQueryKeyDataFromKeyNodeStack(v_stack_m1A0, (unsigned int)(v_stack_m1F8), v_stack_m1D0, (unsigned int)(a5));
    result = 0;
    if (!sign_flag) goto loc_009463A1;
loc_0094618C:
loc_00946196:
loc_0094619C:
    result = CmpKeyEnumStackCleanup(v_stack_m1A8, (unsigned int)(v_stack_m1F8), v_stack_m1D0, (unsigned int)(a5));
    v_r14 = 0;
    if (v_stack_m1E8 == 0) goto loc_009461C9;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m240 + 32) + 140)) & (1)) != 0) goto loc_0094642A;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(v_stack_m240 + 32), v_stack_m230, v_stack_m1D0, (unsigned int)(a5));
loc_009461C9:
    if (v_stack_m250 == 0) goto loc_009461E9;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m240 + 32) + 140)) & (1)) != 0) goto loc_00946434;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(v_stack_m240 + 32), v_stack_m228, v_stack_m1D0, (unsigned int)(a5));
loc_009461E9:
    v_r12 = 0;
    if (v_stack_m258 != 0) {
        a1 = v_stack_m218;
        result = CmpUnlockKcbStack(a1, v_stack_m228, v_stack_m1D0, (unsigned int)(a5));
    }
    if (v_stack_m200 != 0) {
        result = CmSiFreeMemory(v_stack_m200, v_stack_m228, v_stack_m1D0, (unsigned int)(a5));
    }
    if (v_stack_m1C8 != 0) goto loc_0094646F;
loc_00946213:
    if (v_stack_m1F0 == 0) goto loc_00946255;
    if (0 > ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m1F0)))) goto loc_00946243;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m1F0)) + (1));
loc_0094622D:
    if (*(unsigned __int64 *)(v_stack_m1F0 + 16) != 0) {
        result = CmpDereferenceKeyControlBlock(*(unsigned __int64 *)(v_stack_m1F0 + 16), v_stack_m228, v_stack_m1D0, (unsigned int)(a5));
    }
    v_rbx = (v_stack_m1F0 + 16) + (24);
    v_rsi = ((unsigned __int16)(result)) - (1);
    if (condition_is_not_equal) goto loc_0094622D;
loc_00946243:
    if ((*(unsigned __int8 *)(v_stack_m1F0 + 2)) != 0) goto loc_00946397;
    result = CmSiFreeMemory(v_stack_m1F0, v_stack_m228, v_stack_m1D0, (unsigned int)(a5));
loc_00946255:
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m1C0, a2, v_stack_m1D0, (unsigned int)(a5));
    result = CmpUnlockRegistry(v_stack_m1C0, a2, v_stack_m1D0, (unsigned int)(a5));
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_m1D0, (unsigned int)(a5));
    v_rsp = (v_rsp) + (608);
    return result;
loc_00946292:
    v_stack_m1F0 = v_stack_p10;
    v_stack_p50 = v_rsi;
    goto loc_00946034;
loc_009462AA:
    a3 = 0;
    result = CmpGetKeyNodeForKcb(v_stack_m210, v_stack_p70, a3, (unsigned int)(a5));
    result = CmpFindSubKeyByNumber(*(unsigned __int64 *)(v_stack_m210 + 32), result, 1, v_stack_p60);
    if (sign_flag) goto loc_00946196;
    if (((unsigned int)((unsigned int)(v_stack_p60))) == -1) goto loc_009463BA;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m210 + 32) + 140)) & (1)) == 0) goto loc_009463B0;
    result = HvpGetCellFlat(*(unsigned __int64 *)(v_stack_m210 + 32), (unsigned int)(v_stack_p60), v_stack_p68, v_stack_p60);
loc_0094630D:
    v_stack_m1E8 = result;
    result = 0;
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = v_stack_m1D8;
    v_stack_p20 = (unsigned int)((unsigned int)(a5));
    result = CmpQueryKeyDataFromNode(*(unsigned __int64 *)(v_stack_m210 + 32), result, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 4)))), v_stack_m1D0);
    result = 0;
    v_rdi = (unsigned int)((unsigned int)(result));
    if (!sign_flag) { v_rdi = 0; }
    goto loc_0094619C;
loc_00946354:
    result = CmpLockRegistryExclusive(*(unsigned __int64 *)(v_stack_m210 + 32), result, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 4)))), v_stack_m1D0);
    goto loc_00945F47;
loc_0094635E:
    result = CmpKeyEnumStackVerifyResumeContext(v_stack_m218, v_rsi, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 4)))), v_stack_m1D0);
    if (((unsigned int)(result)) == 0xC0000059ULL) goto loc_0094637B;
    if ((*(unsigned int *)(v_rsi + 4)) <= 1) goto loc_0094600B;
loc_0094637B:
    v_stack_m1F0 = v_rsi;
    v_stack_p50 = v_stack_m210;
    goto loc_0094600B;
loc_0094638F:
    goto loc_00946196;
loc_00946397:
    result = CmSiFreeMemory(v_stack_m218, v_rsi, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 4)))), v_stack_m1D0);
    goto loc_00946255;
loc_009463A1:
    goto loc_00946196;
loc_009463B0:
    result = HvpGetCellPaged(v_stack_m218, v_rsi, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 4)))), v_stack_m1D0);
    goto loc_0094630D;
loc_009463BA:
    goto loc_0094619C;
loc_009463C4:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p58))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 4)))));
    if (((unsigned int)(result)) < 10) goto loc_0094605E;
    if (a8 == ((unsigned __int8)(v_stack_m218))) goto loc_0094605E;
    v_stack_p20 = v_stack_p50;
    result = CmpKeyEnumStackCreateResumeContext(v_stack_m218, v_stack_m1A8, (unsigned int)((unsigned int)(v_stack_p58)), 1);
    a2 = 0;
    if (sign_flag) goto loc_00946465;
    *(unsigned __int64 *)(v_stack_p78) = v_stack_p50;
    goto loc_0094619C;
loc_0094642A:
    result = HvpReleaseCellFlat(v_stack_p78, a2, (unsigned int)((unsigned int)(v_stack_p58)), 1);
    goto loc_009461C9;
loc_00946434:
    result = HvpReleaseCellFlat(v_stack_p78, a2, (unsigned int)((unsigned int)(v_stack_p58)), 1);
    goto loc_009461E9;
loc_0094643E:
    result = (1 - 16) + ((unsigned int)((unsigned int)(v_stack_p58)));
    goto loc_00945FBA;
loc_0094644A:
    result = (unsigned int)((result) + (-2));
    v_rsi = ((unsigned int)((unsigned int)(result))) << (7);
    v_rsi = (v_rsi) + (v_stack_m50);
    goto loc_009460F5;
loc_00946465:
    goto loc_0094619C;
loc_0094646F:
    a3 = 0;
    result = CmpKeyEnumStackFreeResumeContext(v_stack_p50, v_stack_m1C0, a3, 1);
    goto loc_00946213;
}
```

## 5. (Beta) C Style

```c
int64_t CmpEnumerateLayeredKey(void *Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6, void *Arg7, uint8_t Arg8)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m150;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint32_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint16_t v_stack_m216;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint64_t v_stack_m230;
    uint32_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint8_t v_stack_m258;
    uint64_t v_stack_m278;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_p10;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (608);
    result = (*(uint64_t *)(v_rip + 0x4C48C2)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m1F8 = Arg3;
    v_stack_m1E0 = Arg1;
    Arg2 = 0;
    v_stack_m1D8 = Arg6;
    v_stack_m220 = Arg7;
    v_stack_m1D0 = Arg4;
    result = memset(v_stack_m1A8, Arg2, 352, Arg4);
    local_rbx = 0;
    v_stack_m228 = 0;
    v_stack_m238 = 0;
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    v_stack_m230 = 0;
    v_stack_m218 = v_xmm1;
    v_stack_m216 = (uint16_t)(result);
    v_stack_m1C0 = v_xmm0;
    v_stack_m258 = 0;
    v_stack_m208 = v_xmm1;
    result = CmpKeyEnumStackInitialize(v_stack_m1A8, Arg2, 352, Arg4);
    v_stack_m250 = 0;
    result = HvpGetCellContextInitialize(v_stack_m228, Arg2, 352, Arg4);
    v_stack_m1E8 = 0;
    result = HvpGetCellContextInitialize(v_stack_m230, Arg2, 352, Arg4);
    v_stack_m1F0 = 0;
    result = CmpInitializeDelayDerefContext(v_stack_m1C0, Arg2, 352, Arg4);
    v_stack_m248 = *(uint64_t *)(arg7);
    if (((uint32_t)((uint32_t)(Arg3))) == ((uint32_t)(0 + 2))) goto loc_00946354;
    result = CmpLockRegistry(v_stack_m1C0, Arg2, 352, Arg4);
loc_00945F47:
    result = CmpStartKcbStackForTopLayerKcb(v_stack_m218, *(uint64_t *)(arg1 + 0x8), 352, Arg4);
    if (sign_flag) goto loc_0094638F;
    result = CmpLockKcbStackShared(v_stack_m218, *(uint64_t *)(arg1 + 0x8), 352, Arg4);
    Arg2 = 0;
    v_stack_m258 = 1;
    result = CmpPerformKeyBodyDeletionCheck(Arg1, Arg2, 352, Arg4);
    if (sign_flag) goto loc_0094638F;
    if (condition_is_less_or_equal) goto loc_009462AA;
    Arg4 = (v_stack_m200) - (v_stack_m210);
    local_r10 = (uint32_t)((local_r10) | (0xFFFFFFFFULL));
loc_00945FAD:
    if (((uint16_t)((int16_t)(v_stack_m216))) >= ((uint16_t)(local_r10 + 3))) goto loc_0094643E;
loc_00945FBA:
    v_stack_m240 = *(uint64_t *)(v_stack_m210 + (int16_t)(v_stack_m216) * 8);
    Arg2 = 0;
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m210 + (int16_t)(v_stack_m216) * 8) + 0x28)) != -1) { Arg2 = 1; }
    Arg1 = (uint16_t)(((int16_t)(v_stack_m216)) + ((uint16_t)(local_r10)));
    Arg3 = (v_stack_m210 + (int16_t)(v_stack_m216) * 8) - (8);
    if (condition_is_greater) goto loc_00945FAD;
    if ((uint8_t)(Arg2) == 0) goto loc_009462AA;
    if (*(uint64_t *)(arg7) != 0) goto loc_0094635E;
    v_stack_m248 = 0;
    if (0 != 0) goto loc_0094635E;
loc_0094600B:
    result = CmpKeyEnumStackStartFromKcbStack(v_stack_m1A8, v_stack_m218, v_stack_m1E0, 0);
    if (sign_flag) goto loc_0094618C;
    if (0 != 0) goto loc_00946292;
loc_00946034:
    result = CmpKeyEnumStackAdvance(v_stack_m1A8, v_stack_m218, v_stack_m1E0, 0);
    if (sign_flag) goto loc_0094618C;
loc_0094604A:
    if (0 >= ((uint32_t)((uint32_t)(Arg2)))) goto loc_00946075;
    result = CmpIsRegistryLockContended(v_stack_m1A8, v_stack_m218, v_stack_m1E0, 0);
    Arg1 = 0;
    if ((uint8_t)(result) != 0) goto loc_009463C4;
loc_0094605E:
    result = CmpKeyEnumStackAdvance(v_stack_m1A8, v_stack_m218, v_stack_m1E0, 0);
    if (sign_flag) goto loc_0094618C;
    local_rsi = (uint32_t)((0) + 1);
    goto loc_0094604A;
loc_00946075:
    Arg1 = ((int16_t)(v_stack_m216) * 2) + ((int16_t)(v_stack_m216));
    result = CmpAllocatePool(256, Arg1 * 8 + 32, (uint32_t)(0x37374D43ULL), 0);
    v_stack_m1C8 = result;
    result = 0;
    if (0 == 0) goto loc_00946160;
    *(uint32_t *)(result + 0x4) = (uint32_t)(local_rsi);
    *(uint16_t *)(result) = (uint16_t)((int16_t)(v_stack_m216));
    *(uint8_t *)(result + 0x2) = 0;
    if (0 > ((uint16_t)((int16_t)(v_stack_m216)))) goto loc_00946158;
    v_stack_m220 = v_stack_m210;
loc_009460DC:
    if (0 >= ((uint16_t)(result + 2))) goto loc_0094644A;
    result = ((int16_t)(0)) << (7);
    local_rsi = (v_stack_m150) + (result);
loc_009460F5:
    result = CmpReferenceKeyControlBlockUnsafe(*(uint64_t *)(v_stack_m210), Arg1 * 8 + 32, (uint32_t)(0x37374D43ULL), 0);
    local_rsi = (local_rsi) - (result + 8);
    *(uint64_t *)(result + 0x8 + 0x10 - 0x8) = *(uint64_t *)(v_stack_m210);
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(*(uint64_t *)(v_stack_m210) + 0x130);
loc_00946120:
    *(uint32_t *)(result + 0x8 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + result + 0x8 + 0x10 * 1 + 0x8)));
    Arg2 = (result + 2) - (1);
    if (condition_is_not_equal) goto loc_00946120;
    local_r14 = (uint16_t)((0) + (1));
    Arg1 = (v_stack_m220) + (8);
    local_r12 = (result + 8) + (24);
    v_stack_m220 = Arg1;
    if (((uint16_t)(local_r14)) <= v_stack_m216) goto loc_009460DC;
loc_00946158:
loc_00946160:
    v_stack_m278 = v_stack_m1D8;
    result = CmpQueryKeyDataFromKeyNodeStack(v_stack_m1A0, (uint32_t)(v_stack_m1F8), v_stack_m1D0, (uint32_t)(Arg5));
    result = 0;
    if (!sign_flag) goto loc_009463A1;
loc_0094618C:
loc_00946196:
loc_0094619C:
    result = CmpKeyEnumStackCleanup(v_stack_m1A8, (uint32_t)(v_stack_m1F8), v_stack_m1D0, (uint32_t)(Arg5));
    local_r14 = 0;
    if (v_stack_m1E8 == 0) goto loc_009461C9;
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m240 + 0x20) + 0x8C)) & (1)) != 0) goto loc_0094642A;
    result = HvpReleaseCellPaged(*(uint64_t *)(v_stack_m240 + 0x20), v_stack_m230, v_stack_m1D0, (uint32_t)(Arg5));
loc_009461C9:
    if (v_stack_m250 == 0) goto loc_009461E9;
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m240 + 0x20) + 0x8C)) & (1)) != 0) goto loc_00946434;
    result = HvpReleaseCellPaged(*(uint64_t *)(v_stack_m240 + 0x20), v_stack_m228, v_stack_m1D0, (uint32_t)(Arg5));
loc_009461E9:
    local_r12 = 0;
    if (v_stack_m258 != 0) {
        Arg1 = v_stack_m218;
        result = CmpUnlockKcbStack(Arg1, v_stack_m228, v_stack_m1D0, (uint32_t)(Arg5));
    }
    if (v_stack_m200 != 0) {
        result = CmSiFreeMemory(v_stack_m200, v_stack_m228, v_stack_m1D0, (uint32_t)(Arg5));
    }
    if (v_stack_m1C8 != 0) goto loc_0094646F;
loc_00946213:
    if (v_stack_m1F0 == 0) goto loc_00946255;
    if (0 > ((uint16_t)(*(uint16_t *)(v_stack_m1F0)))) goto loc_00946243;
    result = (uint16_t)((*(uint16_t *)(v_stack_m1F0)) + (1));
loc_0094622D:
    if (*(uint64_t *)(v_stack_m1F0 + 0x10) != 0) {
        result = CmpDereferenceKeyControlBlock(*(uint64_t *)(v_stack_m1F0 + 0x10), v_stack_m228, v_stack_m1D0, (uint32_t)(Arg5));
    }
    local_rbx = (v_stack_m1F0 + 16) + (24);
    local_rsi = ((uint16_t)(result)) - (1);
    if (condition_is_not_equal) goto loc_0094622D;
loc_00946243:
    if ((*(uint8_t *)(v_stack_m1F0 + 0x2)) != 0) goto loc_00946397;
    result = CmSiFreeMemory(v_stack_m1F0, v_stack_m228, v_stack_m1D0, (uint32_t)(Arg5));
loc_00946255:
    Arg2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m1C0, Arg2, v_stack_m1D0, (uint32_t)(Arg5));
    result = CmpUnlockRegistry(v_stack_m1C0, Arg2, v_stack_m1D0, (uint32_t)(Arg5));
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_m1D0, (uint32_t)(Arg5));
    local_rsp = (local_rsp) + (608);
    return result;
loc_00946292:
    v_stack_m1F0 = v_stack_p10;
    v_stack_p50 = local_rsi;
    goto loc_00946034;
loc_009462AA:
    Arg3 = 0;
    result = CmpGetKeyNodeForKcb(v_stack_m210, v_stack_p70, Arg3, (uint32_t)(Arg5));
    result = CmpFindSubKeyByNumber(*(uint64_t *)(v_stack_m210 + 0x20), result, 1, v_stack_p60);
    if (sign_flag) goto loc_00946196;
    if (((uint32_t)((uint32_t)(v_stack_p60))) == -1) goto loc_009463BA;
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m210 + 0x20) + 0x8C)) & (1)) == 0) goto loc_009463B0;
    result = HvpGetCellFlat(*(uint64_t *)(v_stack_m210 + 0x20), (uint32_t)(v_stack_p60), v_stack_p68, v_stack_p60);
loc_0094630D:
    v_stack_m1E8 = result;
    result = 0;
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = v_stack_m1D8;
    v_stack_p20 = (uint32_t)((uint32_t)(Arg5));
    result = CmpQueryKeyDataFromNode(*(uint64_t *)(v_stack_m210 + 0x20), result, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x4)))), v_stack_m1D0);
    result = 0;
    local_rdi = (uint32_t)((uint32_t)(result));
    if (!sign_flag) { local_rdi = 0; }
    goto loc_0094619C;
loc_00946354:
    result = CmpLockRegistryExclusive(*(uint64_t *)(v_stack_m210 + 0x20), result, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x4)))), v_stack_m1D0);
    goto loc_00945F47;
loc_0094635E:
    result = CmpKeyEnumStackVerifyResumeContext(v_stack_m218, local_rsi, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x4)))), v_stack_m1D0);
    if (((uint32_t)(result)) == 0xC0000059ULL) goto loc_0094637B;
    if ((*(uint32_t *)(local_rsi + 0x4)) <= 1) goto loc_0094600B;
loc_0094637B:
    v_stack_m1F0 = local_rsi;
    v_stack_p50 = v_stack_m210;
    goto loc_0094600B;
loc_0094638F:
    goto loc_00946196;
loc_00946397:
    result = CmSiFreeMemory(v_stack_m218, local_rsi, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x4)))), v_stack_m1D0);
    goto loc_00946255;
loc_009463A1:
    goto loc_00946196;
loc_009463B0:
    result = HvpGetCellPaged(v_stack_m218, local_rsi, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x4)))), v_stack_m1D0);
    goto loc_0094630D;
loc_009463BA:
    goto loc_0094619C;
loc_009463C4:
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p58))) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x4)))));
    if (((uint32_t)(result)) < 10) goto loc_0094605E;
    if (Arg8 == ((uint8_t)(v_stack_m218))) goto loc_0094605E;
    v_stack_p20 = v_stack_p50;
    result = CmpKeyEnumStackCreateResumeContext(v_stack_m218, v_stack_m1A8, (uint32_t)((uint32_t)(v_stack_p58)), 1);
    Arg2 = 0;
    if (sign_flag) goto loc_00946465;
    *(uint64_t *)(v_stack_p78) = v_stack_p50;
    goto loc_0094619C;
loc_0094642A:
    result = HvpReleaseCellFlat(v_stack_p78, Arg2, (uint32_t)((uint32_t)(v_stack_p58)), 1);
    goto loc_009461C9;
loc_00946434:
    result = HvpReleaseCellFlat(v_stack_p78, Arg2, (uint32_t)((uint32_t)(v_stack_p58)), 1);
    goto loc_009461E9;
loc_0094643E:
    result = (1 - 16) + ((uint32_t)((uint32_t)(v_stack_p58)));
    goto loc_00945FBA;
loc_0094644A:
    result = (uint32_t)((result) + (-2));
    local_rsi = ((uint32_t)((uint32_t)(result))) << (7);
    local_rsi = (local_rsi) + (v_stack_m50);
    goto loc_009460F5;
loc_00946465:
    goto loc_0094619C;
loc_0094646F:
    Arg3 = 0;
    result = CmpKeyEnumStackFreeResumeContext(v_stack_p50, v_stack_m1C0, Arg3, 1);
    goto loc_00946213;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg7` | `+ 0x0` | `64` | `R` |
| `Arg7` | `+ 0x0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00945E58&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
