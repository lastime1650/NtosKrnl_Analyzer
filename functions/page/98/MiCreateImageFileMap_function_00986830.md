# MiCreateImageFileMap

- RVA: `0x00986830`–`0x009870D3` (길이 `2,211` bytes)
- VA: `0x0000000140986830`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00097CC8`
- 디코드: `518`개 명령, `2,211/2,211` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **27**; 고유 호출 대상: **23**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x009868C1` → [FsRtlGetFileSize](FsRtlGetFileSize_function_00985150.md) (function, `0x00985150`)
- `0x00986906` → [MiCreateMdl](MiCreateMdl_function_009883A8.md) (function, `0x009883A8`)
- `0x00986926` → [CcZeroEndOfLastPage](../../text/45/CcZeroEndOfLastPage_function_00453584.md) (function, `0x00453584`)
- `0x00986933` → [MiFlushDataSection](../../text/48/MiFlushDataSection_function_0048ED88.md) (function, `0x0048ED88`)
- `0x00986963` → [PsIsCurrentThreadPrefetching](../../text/45/PsIsCurrentThreadPrefetching_function_004511B0.md) (function, `0x004511B0`)
- `0x00986987` → [MiCopyHeaderIfResident](../../text/48/MiCopyHeaderIfResident_function_00482184.md) (function, `0x00482184`)
- `0x00986A21` → [MiVerifyImageHeader](MiVerifyImageHeader_function_009870DC.md) (function, `0x009870DC`)
- `0x00986B11` → [MiBuildImageControlArea](MiBuildImageControlArea_function_009878A4.md) (function, `0x009878A4`)
- `0x00986BB9` → [IoIsDeviceEjectable](../../text/49/IoIsDeviceEjectable_function_0049C644.md) (function, `0x0049C644`)
- `0x00986C0C` → [MiInitializeImageProtos](../../text/2A/MiInitializeImageProtos_function_002ABDAC.md) (function, `0x002ABDAC`)
- `0x00986C26` → [MiInitializeImageHeaderPage](../../text/43/MiInitializeImageHeaderPage_function_0043231C.md) (function, `0x0043231C`)
- `0x00986CAD` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00986D2C` → [MiReadImageHeaders](MiReadImageHeaders_function_00987DAC.md) (function, `0x00987DAC`)
- `0x00986DBA` → [MiCreateMdl](MiCreateMdl_function_009883A8.md) (function, `0x009883A8`)
- `0x00986DD7` → [MiDeleteImageCreationMdls](MiDeleteImageCreationMdls_function_009884FC.md) (function, `0x009884FC`)
- `0x00986DF6` → [MiChargeCommit](../../text/28/MiChargeCommit_function_00286EB0.md) (function, `0x00286EB0`)
- `0x00986E34` → [MiDeleteImageCreationMdls](MiDeleteImageCreationMdls_function_009884FC.md) (function, `0x009884FC`)
- `0x00986E59` → [MiUpdateSystemProtoPtesTree](../../text/29/MiUpdateSystemProtoPtesTree_function_00295F0C.md) (function, `0x00295F0C`)
- `0x00986E64` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00986E6E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00986E78` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00986ECB` → [MiAllocateEntireImageFileExtents](../80/MiAllocateEntireImageFileExtents_function_008008DC.md) (function, `0x008008DC`)
- `0x00986F8A` → [MiLogCreateImageFileMapFailure](../7F/MiLogCreateImageFileMapFailure_function_007FCCDC.md) (function, `0x007FCCDC`)
- `0x00986FAE` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0098707D` → [MiEnableImageDirectMap](../../text/68/MiEnableImageDirectMap_function_00680A78.md) (function, `0x00680A78`)
- `0x009870B3` → [MiReturnCommit](../../text/24/MiReturnCommit_function_00248410.md) (function, `0x00248410`)
- `0x009870C9` → [MiDeleteFileExtentList](../80/MiDeleteFileExtentList_function_00800F6C.md) (function, `0x00800F6C`)

### Direct callers
- [MiCreateNewSection](MiCreateNewSection_function_00985DB0.md) at `0x00985FC0`

### Static image references
- `0x00986849` → RVA `0x00E0A740` (`.data`; read)
- `0x00986C78` → RVA `0x00E2D7F8` (`.data`; write)
- `0x00986F8F` → RVA `0x00F04F18` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **16**
  - `0x00986926` → [CcZeroEndOfLastPage](../../text/45/CcZeroEndOfLastPage_function_00453584.md) (`PAGE` → `.text`)
  - `0x00986933` → [MiFlushDataSection](../../text/48/MiFlushDataSection_function_0048ED88.md) (`PAGE` → `.text`)
  - `0x00986963` → [PsIsCurrentThreadPrefetching](../../text/45/PsIsCurrentThreadPrefetching_function_004511B0.md) (`PAGE` → `.text`)
  - `0x00986987` → [MiCopyHeaderIfResident](../../text/48/MiCopyHeaderIfResident_function_00482184.md) (`PAGE` → `.text`)
  - `0x00986BB9` → [IoIsDeviceEjectable](../../text/49/IoIsDeviceEjectable_function_0049C644.md) (`PAGE` → `.text`)
  - `0x00986C0C` → [MiInitializeImageProtos](../../text/2A/MiInitializeImageProtos_function_002ABDAC.md) (`PAGE` → `.text`)
  - `0x00986C26` → [MiInitializeImageHeaderPage](../../text/43/MiInitializeImageHeaderPage_function_0043231C.md) (`PAGE` → `.text`)
  - `0x00986CAD` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00986DF6` → [MiChargeCommit](../../text/28/MiChargeCommit_function_00286EB0.md) (`PAGE` → `.text`)
  - `0x00986E59` → [MiUpdateSystemProtoPtesTree](../../text/29/MiUpdateSystemProtoPtesTree_function_00295F0C.md) (`PAGE` → `.text`)
  - `0x00986E64` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00986E6E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00986E78` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00986FAE` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0098707D` → [MiEnableImageDirectMap](../../text/68/MiEnableImageDirectMap_function_00680A78.md) (`PAGE` → `.text`)
  - `0x009870B3` → [MiReturnCommit](../../text/24/MiReturnCommit_function_00248410.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **10**
  - `0x0098696A` → [sub_00B2B0A8](../B2/Unknown_function_00B2B0A8.md) (`tail-transfer`)
  - `0x00986A00` → [sub_00B2B0A8 + 0x18](../B2/Unknown_function_00B2B0A8.md) (`tail-transfer`)
  - `0x00986ACF` → [sub_00B2B0A8 + 0x16A](../B2/Unknown_function_00B2B0A8.md) (`tail-transfer`)
  - `0x00986EA5` → [sub_00B2B0A8 + 0x10](../B2/Unknown_function_00B2B0A8.md) (`tail-transfer`)
  - `0x00986F73` → [sub_00B2B0A8 + 0x291](../B2/Unknown_function_00B2B0A8.md) (`tail-transfer`)
  - `0x00986F99` → [sub_00B2B0A8 + 0x282](../B2/Unknown_function_00B2B0A8.md) (`tail-transfer`)
  - `0x00986FB4` → [sub_00B2B0A8 + 0x282](../B2/Unknown_function_00B2B0A8.md) (`tail-transfer`)
  - `0x00987041` → [sub_00B2B0A8 + 0x2BC](../B2/Unknown_function_00B2B0A8.md) (`tail-transfer`)
  - `0x0098704F` → [sub_00B2B0A8 + 0x2BC](../B2/Unknown_function_00B2B0A8.md) (`tail-transfer`)
  - `0x00987087` → [sub_00B2B0A8 + 0x35C](../B2/Unknown_function_00B2B0A8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00986830  40 55                           push rbp
00986832  53                              push rbx
00986833  56                              push rsi
00986834  57                              push rdi
00986835  41 54                           push r12
00986837  41 55                           push r13
00986839  41 56                           push r14
0098683B  41 57                           push r15
0098683D  48 8D 6C 24 C8                  lea rbp, [rsp - 0x38]
00986842  48 81 EC 38 01 00 00            sub rsp, 0x138
00986849  48 8B 05 F0 3E 48 00            mov rax, qword ptr [rip + 0x483ef0]
00986850  48 33 C4                        xor rax, rsp
00986853  48 89 45 28                     mov qword ptr [rbp + 0x28], rax
00986857  48 8B 85 A0 00 00 00            mov rax, qword ptr [rbp + 0xa0]
0098685E  0F 57 C0                        xorps xmm0, xmm0
00986861  48 89 45 08                     mov qword ptr [rbp + 8], rax
00986865  4C 8B EA                        mov r13, rdx
00986868  48 8B 85 A8 00 00 00            mov rax, qword ptr [rbp + 0xa8]
0098686F  45 33 E4                        xor r12d, r12d
00986872  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
00986876  0F 57 C9                        xorps xmm1, xmm1
00986879  48 8B 85 B0 00 00 00            mov rax, qword ptr [rbp + 0xb0]
00986880  41 8B D9                        mov ebx, r9d
00986883  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00986888  41 8B F0                        mov esi, r8d
0098688B  48 8B 85 B8 00 00 00            mov rax, qword ptr [rbp + 0xb8]
00986892  4C 8B F1                        mov r14, rcx
00986895  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
00986899  33 C0                           xor eax, eax
0098689B  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
009868A0  48 8D 55 80                     lea rdx, [rbp - 0x80]
009868A4  89 45 E0                        mov dword ptr [rbp - 0x20], eax
009868A7  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
009868AC  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
009868B0  44 89 64 24 70                  mov dword ptr [rsp + 0x70], r12d
009868B5  0F 11 45 A0                     movups xmmword ptr [rbp - 0x60], xmm0
009868B9  4C 89 65 80                     mov qword ptr [rbp - 0x80], r12
009868BD  0F 11 4D F8                     movups xmmword ptr [rbp - 8], xmm1
009868C1  E8 8A E8 FF FF                  call 0x140985150
009868C6  85 C0                           test eax, eax
009868C8  0F 88 0A 04 00 00               js 0x140986cd8
009868CE  44 39 65 84                     cmp dword ptr [rbp - 0x7c], r12d
009868D2  0F 85 A0 03 00 00               jne 0x140986c78
009868D8  4C 21 65 C0                     and qword ptr [rbp - 0x40], r12
009868DC  41 8D 4C 24 01                  lea ecx, [r12 + 1]
009868E1  8B F9                           mov edi, ecx
009868E3  4C 89 65 88                     mov qword ptr [rbp - 0x78], r12
009868E7  44 8B C9                        mov r9d, ecx
009868EA  4C 89 65 90                     mov qword ptr [rbp - 0x70], r12
009868EE  49 8B CD                        mov rcx, r13
009868F1  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
009868F6  41 B8 00 10 00 00               mov r8d, 0x1000
009868FC  4C 89 64 24 68                  mov qword ptr [rsp + 0x68], r12
00986901  8B D6                           mov edx, esi
00986903  45 8B FC                        mov r15d, r12d
00986906  E8 9D 1A 00 00                  call 0x1409883a8
0098690B  4C 8B E8                        mov r13, rax
0098690E  48 85 C0                        test rax, rax
00986911  0F 84 B0 03 00 00               je 0x140986cc7
00986917  4C 21 60 10                     and qword ptr [rax + 0x10], r12
0098691B  49 8B CE                        mov rcx, r14
0098691E  48 8B 40 30                     mov rax, qword ptr [rax + 0x30]
00986922  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00986926  E8 59 CC AC FF                  call 0x140453584
0098692B  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
00986930  49 8B CE                        mov rcx, r14
00986933  E8 50 84 B0 FF                  call 0x14048ed88
00986938  44 8B F0                        mov r14d, eax
0098693B  3D 54 00 00 C0                  cmp eax, 0xc0000054
00986940  0F 84 55 05 00 00               je 0x140986e9b
00986946  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
0098694B  44 39 64 24 70                  cmp dword ptr [rsp + 0x70], r12d
00986950  0F 85 54 05 00 00               jne 0x140986eaa
00986956  F7 C3 40 00 08 00               test ebx, 0x80040
0098695C  74 12                           je 0x140986970
0098695E  40 88 7C 24 40                  mov byte ptr [rsp + 0x40], dil
00986963  E8 48 A8 AC FF                  call 0x1404511b0
00986968  84 C0                           test al, al
0098696A  0F 85 38 47 1A 00               jne 0x140b2b0a8
00986970  4C 8B 75 80                     mov r14, qword ptr [rbp - 0x80]
00986974  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00986979  0F BA E3 0E                     bt ebx, 0xe
0098697D  0F 82 30 05 00 00               jb 0x140986eb3
00986983  48 8B 55 F0                     mov rdx, qword ptr [rbp - 0x10]
00986987  E8 F8 B7 AF FF                  call 0x140482184
0098698C  85 C0                           test eax, eax
0098698E  0F 84 5D 03 00 00               je 0x140986cf1
00986994  B8 00 10 00 00                  mov eax, 0x1000
00986999  44 8B C8                        mov r9d, eax
0098699C  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
009869A0  41 F6 45 0A 04                  test byte ptr [r13 + 0xa], 4
009869A5  0F 85 C4 03 00 00               jne 0x140986d6f
009869AB  49 8B 55 18                     mov rdx, qword ptr [r13 + 0x18]
009869AF  B8 4D 5A 00 00                  mov eax, 0x5a4d
009869B4  48 89 55 98                     mov qword ptr [rbp - 0x68], rdx
009869B8  66 39 02                        cmp word ptr [rdx], ax
009869BB  0F 85 2B 05 00 00               jne 0x140986eec
009869C1  8B 4A 3C                        mov ecx, dword ptr [rdx + 0x3c]
009869C4  89 4C 24 74                     mov dword ptr [rsp + 0x74], ecx
009869C8  8D 81 08 01 00 00               lea eax, [rcx + 0x108]
009869CE  3B C1                           cmp eax, ecx
009869D0  0F 86 1E 05 00 00               jbe 0x140986ef4
009869D6  48 8D 81 08 01 00 00            lea rax, [rcx + 0x108]
009869DD  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
009869E2  44 8B F1                        mov r14d, ecx
009869E5  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
009869E9  48 3B C1                        cmp rax, rcx
009869EC  0F 87 14 05 00 00               ja 0x140986f06
009869F2  48 C1 E7 0C                     shl rdi, 0xc
009869F6  49 C7 C0 00 F0 FF FF            mov r8, 0xfffffffffffff000
009869FD  48 3B C7                        cmp rax, rdi
00986A00  0F 87 BA 46 1A 00               ja 0x140b2b0c0
00986A06  49 3B C1                        cmp rax, r9
00986A09  0F 87 0C 05 00 00               ja 0x140986f1b
00986A0F  49 8D 3C 16                     lea rdi, [r14 + rdx]
00986A13  4D 2B CE                        sub r9, r14
00986A16  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00986A1B  4C 8B C2                        mov r8, rdx
00986A1E  48 8B D7                        mov rdx, rdi
00986A21  E8 B6 06 00 00                  call 0x1409870dc
00986A26  44 8B F0                        mov r14d, eax
00986A29  85 C0                           test eax, eax
00986A2B  0F 85 58 02 00 00               jne 0x140986c89
00986A31  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
00986A35  41 8B CF                        mov ecx, r15d
00986A38  4C 8B 5C 24 60                  mov r11, qword ptr [rsp + 0x60]
00986A3D  44 8B 4C 24 74                  mov r9d, dword ptr [rsp + 0x74]
00986A42  44 89 08                        mov dword ptr [rax], r9d
00986A45  45 8B 43 10                     mov r8d, dword ptr [r11 + 0x10]
00986A49  41 F7 C0 FF 0F 00 00            test r8d, 0xfff
00986A50  41 8B C0                        mov eax, r8d
00986A53  0F 95 C1                        setne cl
00986A56  C1 E8 0C                        shr eax, 0xc
00986A59  03 C8                           add ecx, eax
00986A5B  0F 84 CF 04 00 00               je 0x140986f30
00986A61  8B 47 14                        mov eax, dword ptr [rdi + 0x14]
00986A64  0F 10 47 04                     movups xmm0, xmmword ptr [rdi + 4]
00986A68  0F B7 D0                        movzx edx, ax
00986A6B  89 45 E0                        mov dword ptr [rbp - 0x20], eax
00986A6E  83 C2 18                        add edx, 0x18
00986A71  66 48 0F 7E C0                  movq rax, xmm0
00986A76  89 55 B0                        mov dword ptr [rbp - 0x50], edx
00986A79  48 C1 E8 10                     shr rax, 0x10
00986A7D  44 0F B7 D0                     movzx r10d, ax
00986A81  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00986A85  43 8D 04 92                     lea eax, [r10 + r10*4]
00986A89  8D 0C C2                        lea ecx, [rdx + rax*8]
00986A8C  41 03 C9                        add ecx, r9d
00986A8F  41 3B C9                        cmp ecx, r9d
00986A92  0F 86 AD 04 00 00               jbe 0x140986f45
00986A98  4B 8D 0C 92                     lea rcx, [r10 + r10*4]
00986A9C  42 8D 04 0A                     lea eax, [rdx + r9]
00986AA0  4C 8D 0C CD 00 00 00 00         lea r9, [rcx*8]
00986AA8  44 8B F0                        mov r14d, eax
00986AAB  49 8D 0C 01                     lea rcx, [r9 + rax]
00986AAF  41 8B 43 18                     mov eax, dword ptr [r11 + 0x18]
00986AB3  48 3B C1                        cmp rax, rcx
00986AB6  44 8B D1                        mov r10d, ecx
00986AB9  44 0F 43 D0                     cmovae r10d, eax
00986ABD  44 89 54 24 78                  mov dword ptr [rsp + 0x78], r10d
00986AC2  45 3B D0                        cmp r10d, r8d
00986AC5  0F 87 8F 04 00 00               ja 0x140986f5a
00986ACB  48 3B 4D A8                     cmp rcx, qword ptr [rbp - 0x58]
00986ACF  0F 87 3D 47 1A 00               ja 0x140b2b212
00986AD5  44 8B D2                        mov r10d, edx
00986AD8  4C 03 D7                        add r10, rdi
00986ADB  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00986AE0  B8 00 10 00 00                  mov eax, 0x1000
00986AE5  41 39 43 0C                     cmp dword ptr [r11 + 0xc], eax
00986AE9  0F 82 80 04 00 00               jb 0x140986f6f
00986AEF  48 8D 45 90                     lea rax, [rbp - 0x70]
00986AF3  4D 8B C3                        mov r8, r11
00986AF6  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00986AFB  4C 8D 4D D0                     lea r9, [rbp - 0x30]
00986AFF  48 8D 45 80                     lea rax, [rbp - 0x80]
00986B03  49 8B D2                        mov rdx, r10
00986B06  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00986B0B  8B CE                           mov ecx, esi
00986B0D  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00986B11  E8 8E 0D 00 00                  call 0x1409878a4
00986B16  4C 8B 7D 90                     mov r15, qword ptr [rbp - 0x70]
00986B1A  44 8B F0                        mov r14d, eax
00986B1D  85 C0                           test eax, eax
00986B1F  0F 88 FD 02 00 00               js 0x140986e22
00986B25  49 8B 07                        mov rax, qword ptr [r15]
00986B28  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
00986B2D  48 8B 48 38                     mov rcx, qword ptr [rax + 0x38]
00986B31  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
00986B35  89 41 40                        mov dword ptr [rcx + 0x40], eax
00986B38  41 0F B7 47 3C                  movzx eax, word ptr [r15 + 0x3c]
00986B3D  0F B7 C8                        movzx ecx, ax
00986B40  66 33 0A                        xor cx, word ptr [rdx]
00986B43  BA FF 03 00 00                  mov edx, 0x3ff
00986B48  66 23 CA                        and cx, dx
00986B4B  66 33 C8                        xor cx, ax
00986B4E  66 41 89 4F 3C                  mov word ptr [r15 + 0x3c], cx
00986B53  0F BA E3 08                     bt ebx, 8
00986B57  0F 82 5C 04 00 00               jb 0x140986fb9
00986B5D  4D 8B 07                        mov r8, qword ptr [r15]
00986B60  40 32 FF                        xor dil, dil
00986B63  48 83 7D C0 00                  cmp qword ptr [rbp - 0x40], 0
00986B68  4C 89 44 24 50                  mov qword ptr [rsp + 0x50], r8
00986B6D  0F 85 05 02 00 00               jne 0x140986d78
00986B73  49 83 7D 00 00                  cmp qword ptr [r13], 0
00986B78  0F 85 FA 01 00 00               jne 0x140986d78
00986B7E  41 B9 01 00 00 00               mov r9d, 1
00986B84  F7 C3 00 40 10 00               test ebx, 0x104000
00986B8A  75 15                           jne 0x140986ba1
00986B8C  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00986B91  B8 00 10 00 00                  mov eax, 0x1000
00986B96  40 0F B6 FF                     movzx edi, dil
00986B9A  39 41 18                        cmp dword ptr [rcx + 0x18], eax
00986B9D  41 0F 42 F9                     cmovb edi, r9d
00986BA1  80 7C 24 40 00                  cmp byte ptr [rsp + 0x40], 0
00986BA6  44 0F B7 75 E2                  movzx r14d, word ptr [rbp - 0x1e]
00986BAB  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00986BB0  75 2C                           jne 0x140986bde
00986BB2  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
00986BB6  48 8B CA                        mov rcx, rdx
00986BB9  E8 86 5A B1 FF                  call 0x14049c644
00986BBE  84 C0                           test al, al
00986BC0  0F 85 1B 04 00 00               jne 0x140986fe1
00986BC6  66 41 0F BA E6 0A               bt r14w, 0xa
00986BCC  0F 82 F7 03 00 00               jb 0x140986fc9
00986BD2  66 41 0F BA E6 0B               bt r14w, 0xb
00986BD8  0F 82 F8 03 00 00               jb 0x140986fd6
00986BDE  49 8B 40 10                     mov rax, qword ptr [r8 + 0x10]
00986BE2  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00986BE6  48 85 C0                        test rax, rax
00986BE9  0F 85 F9 01 00 00               jne 0x140986de8
00986BEF  41 8B 4F 38                     mov ecx, dword ptr [r15 + 0x38]
00986BF3  0F BA E1 11                     bt ecx, 0x11
00986BF7  0F 82 09 04 00 00               jb 0x140987006
00986BFD  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
00986C01  48 85 C0                        test rax, rax
00986C04  74 0B                           je 0x140986c11
00986C06  48 8B D0                        mov rdx, rax
00986C09  49 8B CF                        mov rcx, r15
00986C0C  E8 9B 51 92 FF                  call 0x1402abdac
00986C11  40 84 FF                        test dil, dil
00986C14  74 15                           je 0x140986c2b
00986C16  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00986C1B  49 8B CF                        mov rcx, r15
00986C1E  48 8B 55 F0                     mov rdx, qword ptr [rbp - 0x10]
00986C22  44 8B 40 18                     mov r8d, dword ptr [rax + 0x18]
00986C26  E8 F1 B6 AA FF                  call 0x14043231c
00986C2B  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
00986C30  B8 0B 01 00 00                  mov eax, 0x10b
00986C35  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
00986C3A  66 39 42 30                     cmp word ptr [rdx + 0x30], ax
00986C3E  75 09                           jne 0x140986c49
00986C40  B8 00 80 00 00                  mov eax, 0x8000
00986C45  66 09 47 0C                     or word ptr [rdi + 0xc], ax
00986C49  8A 44 24 40                     mov al, byte ptr [rsp + 0x40]
00986C4D  84 C0                           test al, al
00986C4F  0F 85 DA 03 00 00               jne 0x14098702f
00986C55  41 BE 01 00 00 00               mov r14d, 1
00986C5B  0F BA E3 0E                     bt ebx, 0xe
00986C5F  0F 82 EF 03 00 00               jb 0x140987054
00986C65  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
00986C69  45 33 F6                        xor r14d, r14d
00986C6C  48 89 38                        mov qword ptr [rax], rdi
00986C6F  48 8B 45 10                     mov rax, qword ptr [rbp + 0x10]
00986C73  4C 89 28                        mov qword ptr [rax], r13
00986C76  EB 22                           jmp 0x140986c9a
00986C78  C7 05 76 6B 4A 00 22 00 00 00   mov dword ptr [rip + 0x4a6b76], 0x22
00986C82  B8 20 00 00 C0                  mov eax, 0xc0000020
00986C87  EB 1D                           jmp 0x140986ca6
00986C89  33 C0                           xor eax, eax
00986C8B  33 DB                           xor ebx, ebx
00986C8D  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00986C91  45 85 F6                        test r14d, r14d
00986C94  0F 88 8D 01 00 00               js 0x140986e27
00986C9A  4D 85 E4                        test r12, r12
00986C9D  0F 85 23 04 00 00               jne 0x1409870c6
00986CA3  41 8B C6                        mov eax, r14d
00986CA6  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00986CAA  48 33 CC                        xor rcx, rsp
00986CAD  E8 8E 59 D2 FF                  call 0x1406ac640
00986CB2  48 81 C4 38 01 00 00            add rsp, 0x138
00986CB9  41 5F                           pop r15
00986CBB  41 5E                           pop r14
00986CBD  41 5D                           pop r13
00986CBF  41 5C                           pop r12
00986CC1  5F                              pop rdi
00986CC2  5E                              pop rsi
00986CC3  5B                              pop rbx
00986CC4  5D                              pop rbp
00986CC5  C3                              ret
00986CC6  CC                              int3
00986CC7  C7 05 27 6B 4A 00 23 00 00 00   mov dword ptr [rip + 0x4a6b27], 0x23
00986CD1  B8 9A 00 00 C0                  mov eax, 0xc000009a
00986CD6  EB CE                           jmp 0x140986ca6
00986CD8  3D BA 00 00 C0                  cmp eax, 0xc00000ba
00986CDD  C7 05 11 6B 4A 00 21 00 00 00   mov dword ptr [rip + 0x4a6b11], 0x21
00986CE7  B9 20 00 00 C0                  mov ecx, 0xc0000020
00986CEC  0F 44 C1                        cmove eax, ecx
00986CEF  EB B5                           jmp 0x140986ca6
00986CF1  44 38 64 24 40                  cmp byte ptr [rsp + 0x40], r12b
00986CF6  75 18                           jne 0x140986d10
00986CF8  F6 C3 20                        test bl, 0x20
00986CFB  0F 85 82 00 00 00               jne 0x140986d83
00986D01  0F BA E3 09                     bt ebx, 9
00986D05  73 09                           jae 0x140986d10
00986D07  41 81 FE 00 00 02 00            cmp r14d, 0x20000
00986D0E  76 73                           jbe 0x140986d83
00986D10  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00986D15  4C 8B 4D A8                     mov r9, qword ptr [rbp - 0x58]
00986D19  4D 85 C9                        test r9, r9
00986D1C  0F 85 7E FC FF FF               jne 0x1409869a0
00986D22  4C 8D 4D A0                     lea r9, [rbp - 0x60]
00986D26  4D 8B C5                        mov r8, r13
00986D29  49 8B D4                        mov rdx, r12
00986D2C  E8 7B 10 00 00                  call 0x140987dac
00986D31  44 8B F0                        mov r14d, eax
00986D34  85 C0                           test eax, eax
00986D36  0F 88 50 01 00 00               js 0x140986e8c
00986D3C  4C 8B 4D A8                     mov r9, qword ptr [rbp - 0x58]
00986D40  48 8B C7                        mov rax, rdi
00986D43  48 C1 E0 0C                     shl rax, 0xc
00986D47  4C 3B C8                        cmp r9, rax
00986D4A  0F 84 50 FC FF FF               je 0x1409869a0
00986D50  49 83 F9 40                     cmp r9, 0x40
00986D54  0F 83 46 FC FF FF               jae 0x1409869a0
00986D5A  41 BE 2F 01 00 C0               mov r14d, 0xc000012f
00986D60  C7 05 8E 6A 4A 00 29 00 00 00   mov dword ptr [rip + 0x4a6a8e], 0x29
00986D6A  E9 27 01 00 00                  jmp 0x140986e96
00986D6F  49 8B 55 20                     mov rdx, qword ptr [r13 + 0x20]
00986D73  E9 37 FC FF FF                  jmp 0x1409869af
00986D78  41 B9 01 00 00 00               mov r9d, 1
00986D7E  E9 1E FE FF FF                  jmp 0x140986ba1
00986D83  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00986D88  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
00986D8C  4C 39 20                        cmp qword ptr [rax], r12
00986D8F  75 84                           jne 0x140986d15
00986D91  41 8B FE                        mov edi, r14d
00986D94  48 81 C7 FF 0F 00 00            add rdi, 0xfff
00986D9B  48 C1 EF 0C                     shr rdi, 0xc
00986D9F  48 83 FF 01                     cmp rdi, 1
00986DA3  0F 86 6C FF FF FF               jbe 0x140986d15
00986DA9  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00986DAE  4C 8B C7                        mov r8, rdi
00986DB1  49 C1 E0 0C                     shl r8, 0xc
00986DB5  45 33 C9                        xor r9d, r9d
00986DB8  8B D6                           mov edx, esi
00986DBA  E8 E9 15 00 00                  call 0x1409883a8
00986DBF  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00986DC3  4C 8B F0                        mov r14, rax
00986DC6  48 85 C0                        test rax, rax
00986DC9  0F 84 B3 00 00 00               je 0x140986e82
00986DCF  BA 01 00 00 00                  mov edx, 1
00986DD4  49 8B CD                        mov rcx, r13
00986DD7  E8 20 17 00 00                  call 0x1409884fc
00986DDC  4D 21 66 10                     and qword ptr [r14 + 0x10], r12
00986DE0  4D 8B EE                        mov r13, r14
00986DE3  E9 28 FF FF FF                  jmp 0x140986d10
00986DE8  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
00986DED  45 33 C0                        xor r8d, r8d
00986DF0  49 8B CE                        mov rcx, r14
00986DF3  48 8B D0                        mov rdx, rax
00986DF6  E8 B5 00 90 FF                  call 0x140286eb0
00986DFB  85 C0                           test eax, eax
00986DFD  0F 84 E8 01 00 00               je 0x140986feb
00986E03  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
00986E07  F0 49 01 86 B8 4C 00 00         lock add qword ptr [r14 + 0x4cb8], rax
00986E0F  4C 8B 7D 90                     mov r15, qword ptr [rbp - 0x70]
00986E13  44 0F B7 75 E2                  movzx r14d, word ptr [rbp - 0x1e]
00986E18  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
00986E1D  E9 CD FD FF FF                  jmp 0x140986bef
00986E22  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00986E27  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
00986E2C  BA 01 00 00 00                  mov edx, 1
00986E31  49 8B CD                        mov rcx, r13
00986E34  E8 C3 16 00 00                  call 0x1409884fc
00986E39  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
00986E3D  48 85 C9                        test rcx, rcx
00986E40  0F 85 56 02 00 00               jne 0x14098709c
00986E46  4D 85 FF                        test r15, r15
00986E49  0F 84 4B FE FF FF               je 0x140986c9a
00986E4F  49 8B 4F 60                     mov rcx, qword ptr [r15 + 0x60]
00986E53  33 D2                           xor edx, edx
00986E55  48 83 E1 F8                     and rcx, 0xfffffffffffffff8
00986E59  E8 AE F0 90 FF                  call 0x140295f0c
00986E5E  48 8B 4B 40                     mov rcx, qword ptr [rbx + 0x40]
00986E62  33 D2                           xor edx, edx
00986E64  E8 07 BA 1F 00                  call 0x140b82870
00986E69  33 D2                           xor edx, edx
00986E6B  48 8B CB                        mov rcx, rbx
00986E6E  E8 FD B9 1F 00                  call 0x140b82870
00986E73  33 D2                           xor edx, edx
00986E75  49 8B CF                        mov rcx, r15
00986E78  E8 F3 B9 1F 00                  call 0x140b82870
00986E7D  E9 18 FE FF FF                  jmp 0x140986c9a
00986E82  BF 01 00 00 00                  mov edi, 1
00986E87  E9 84 FE FF FF                  jmp 0x140986d10
00986E8C  C7 05 62 69 4A 00 28 00 00 00   mov dword ptr [rip + 0x4a6962], 0x28
00986E96  49 8B DF                        mov rbx, r15
00986E99  EB 8C                           jmp 0x140986e27
00986E9B  C7 05 53 69 4A 00 24 00 00 00   mov dword ptr [rip + 0x4a6953], 0x24
00986EA5  E9 0E 42 1A 00                  jmp 0x140b2b0b8
00986EAA  0F BA EB 13                     bts ebx, 0x13
00986EAE  E9 A3 FA FF FF                  jmp 0x140986956
00986EB3  B8 00 10 00 00                  mov eax, 0x1000
00986EB8  4C 8D 4C 24 68                  lea r9, [rsp + 0x68]
00986EBD  0F BA E3 11                     bt ebx, 0x11
00986EC1  49 8B D6                        mov rdx, r14
00986EC4  48 0F 42 D0                     cmovb rdx, rax
00986EC8  45 33 C0                        xor r8d, r8d
00986ECB  E8 0C 9A E7 FF                  call 0x1408008dc
00986ED0  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
00986ED5  44 8B F0                        mov r14d, eax
00986ED8  85 C0                           test eax, eax
00986EDA  0F 89 30 FE FF FF               jns 0x140986d10
00986EE0  C7 05 0E 69 4A 00 26 00 00 00   mov dword ptr [rip + 0x4a690e], 0x26
00986EEA  EB AA                           jmp 0x140986e96
00986EEC  41 BE 2F 01 00 C0               mov r14d, 0xc000012f
00986EF2  EB A2                           jmp 0x140986e96
00986EF4  41 BE 30 01 00 C0               mov r14d, 0xc0000130
00986EFA  C7 05 F4 68 4A 00 2A 00 00 00   mov dword ptr [rip + 0x4a68f4], 0x2a
00986F04  EB 90                           jmp 0x140986e96
00986F06  41 BE 30 01 00 C0               mov r14d, 0xc0000130
00986F0C  C7 05 E2 68 4A 00 2B 00 00 00   mov dword ptr [rip + 0x4a68e2], 0x2b
00986F16  E9 7B FF FF FF                  jmp 0x140986e96
00986F1B  41 BE 30 01 00 C0               mov r14d, 0xc0000130
00986F21  C7 05 CD 68 4A 00 2F 00 00 00   mov dword ptr [rip + 0x4a68cd], 0x2f
00986F2B  E9 66 FF FF FF                  jmp 0x140986e96
00986F30  41 BE 7B 00 00 C0               mov r14d, 0xc000007b
00986F36  C7 05 B8 68 4A 00 31 00 00 00   mov dword ptr [rip + 0x4a68b8], 0x31
00986F40  E9 51 FF FF FF                  jmp 0x140986e96
00986F45  41 BE 7B 00 00 C0               mov r14d, 0xc000007b
00986F4B  C7 05 A3 68 4A 00 32 00 00 00   mov dword ptr [rip + 0x4a68a3], 0x32
00986F55  E9 3C FF FF FF                  jmp 0x140986e96
00986F5A  41 BE 7B 00 00 C0               mov r14d, 0xc000007b
00986F60  C7 05 8E 68 4A 00 30 00 00 00   mov dword ptr [rip + 0x4a688e], 0x30
00986F6A  E9 27 FF FF FF                  jmp 0x140986e96
00986F6F  0F BA E3 12                     bt ebx, 0x12
00986F73  0F 83 C0 43 1A 00               jae 0x140b2b339
00986F79  44 8B 4D D4                     mov r9d, dword ptr [rbp - 0x2c]
00986F7D  48 8B D7                        mov rdx, rdi
00986F80  45 8B 43 40                     mov r8d, dword ptr [r11 + 0x40]
00986F84  41 BE 7B 00 00 C0               mov r14d, 0xc000007b
00986F8A  E8 4D 5D E7 FF                  call 0x1407fccdc
00986F8F  48 8B 05 82 DF 57 00            mov rax, qword ptr [rip + 0x57df82]
00986F96  48 85 C0                        test rax, rax
00986F99  0F 84 8B 43 1A 00               je 0x140b2b32a
00986F9F  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00986FA4  44 8B 45 D4                     mov r8d, dword ptr [rbp - 0x2c]
00986FA8  8B 51 40                        mov edx, dword ptr [rcx + 0x40]
00986FAB  48 8B CF                        mov rcx, rdi
00986FAE  E8 1D 3B D3 FF                  call 0x1406baad0
00986FB3  90                              nop
00986FB4  E9 71 43 1A 00                  jmp 0x140b2b32a
00986FB9  49 8B 07                        mov rax, qword ptr [r15]
00986FBC  48 8B 48 38                     mov rcx, qword ptr [rax + 0x38]
00986FC0  80 49 33 10                     or byte ptr [rcx + 0x33], 0x10
00986FC4  E9 94 FB FF FF                  jmp 0x140986b5d
00986FC9  8B 42 34                        mov eax, dword ptr [rdx + 0x34]
00986FCC  41 84 C1                        test r9b, al
00986FCF  75 10                           jne 0x140986fe1
00986FD1  E9 FC FB FF FF                  jmp 0x140986bd2
00986FD6  8B 42 34                        mov eax, dword ptr [rdx + 0x34]
00986FD9  A8 10                           test al, 0x10
00986FDB  0F 84 FD FB FF FF               je 0x140986bde
00986FE1  44 88 4C 24 40                  mov byte ptr [rsp + 0x40], r9b
00986FE6  E9 F3 FB FF FF                  jmp 0x140986bde
00986FEB  33 C0                           xor eax, eax
00986FED  C7 05 01 68 4A 00 39 00 00 00   mov dword ptr [rip + 0x4a6801], 0x39
00986FF7  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00986FFB  41 BE 2D 01 00 C0               mov r14d, 0xc000012d
00987001  E9 1C FE FF FF                  jmp 0x140986e22
00987006  0F BA E3 14                     bt ebx, 0x14
0098700A  0F 82 ED FB FF FF               jb 0x140986bfd
00987010  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00987015  F7 40 14 00 00 00 01            test dword ptr [rax + 0x14], 0x1000000
0098701C  0F 85 DB FB FF FF               jne 0x140986bfd
00987022  0F BA E9 1B                     bts ecx, 0x1b
00987026  41 89 4F 38                     mov dword ptr [r15 + 0x38], ecx
0098702A  E9 CE FB FF FF                  jmp 0x140986bfd
0098702F  41 8B 47 38                     mov eax, dword ptr [r15 + 0x38]
00987033  0F BA E8 0B                     bts eax, 0xb
00987037  41 89 47 38                     mov dword ptr [r15 + 0x38], eax
0098703B  F7 C3 40 00 08 00               test ebx, 0x80040
00987041  0F 84 1D 43 1A 00               je 0x140b2b364
00987047  0F BA E8 12                     bts eax, 0x12
0098704B  41 89 47 38                     mov dword ptr [r15 + 0x38], eax
0098704F  E9 10 43 1A 00                  jmp 0x140b2b364
00987054  8B CB                           mov ecx, ebx
00987056  0F B6 C0                        movzx eax, al
00987059  C1 E9 11                        shr ecx, 0x11
0098705C  4C 8B C2                        mov r8, rdx
0098705F  41 23 CE                        and ecx, r14d
00987062  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00987066  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
0098706A  4D 8B CC                        mov r9, r12
0098706D  C1 EB 10                        shr ebx, 0x10
00987070  48 8B CE                        mov rcx, rsi
00987073  41 23 DE                        and ebx, r14d
00987076  49 8B D7                        mov rdx, r15
00987079  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0098707D  E8 F6 99 CF FF                  call 0x140680a78
00987082  44 8B F0                        mov r14d, eax
00987085  85 C0                           test eax, eax
00987087  0F 89 77 43 1A 00               jns 0x140b2b404
0098708D  C7 05 61 67 4A 00 3A 00 00 00   mov dword ptr [rip + 0x4a6761], 0x3a
00987097  E9 86 FD FF FF                  jmp 0x140986e22
0098709C  48 8B C1                        mov rax, rcx
0098709F  48 F7 D8                        neg rax
009870A2  F0 48 01 87 B8 4C 00 00         lock add qword ptr [rdi + 0x4cb8], rax
009870AA  48 8B D1                        mov rdx, rcx
009870AD  45 33 C0                        xor r8d, r8d
009870B0  48 8B CF                        mov rcx, rdi
009870B3  E8 58 13 8C FF                  call 0x140248410
009870B8  4C 8B 7D 90                     mov r15, qword ptr [rbp - 0x70]
009870BC  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
009870C1  E9 80 FD FF FF                  jmp 0x140986e46
009870C6  49 8B CC                        mov rcx, r12
009870C9  E8 9E 9E E7 FF                  call 0x140800f6c
009870CE  E9 D0 FB FF FF                  jmp 0x140986ca3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCreateImageFileMap(__int64 a1, __int64 a2, int a3, int a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m104;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int8 v_stack_m138;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned int v_stack_m158;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int16 v_stack_m96;
    unsigned int v_stack_m98;
    unsigned int v_stack_mA4;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF4;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int8 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;

    v_rsp = (v_rsp) - (312);
    result = (*(unsigned __int64 *)(v_rip + 4734704)) ^ (v_rsp);
    v_stack_m50 = result;
    v_stack_m70 = a5;
    v_r12 = 0;
    v_stack_m68 = a6;
    v_stack_m118 = a7;
    v_stack_m60 = a8;
    result = 0;
    v_stack_m130 = a2;
    v_stack_m98 = 0;
    v_stack_m120 = a1;
    v_stack_mA8 = v_xmm0;
    v_stack_m108 = 0;
    v_stack_mD8 = v_xmm0;
    v_stack_mF8 = 0;
    v_stack_m80 = v_xmm1;
    result = FsRtlGetFileSize(a1, v_stack_mF8, a3, a4);
    if (sign_flag) goto loc_00986CD8;
    if (v_stack_mF4 != 0) goto loc_00986C78;
    v_stack_mF0 = 0;
    v_stack_mE8 = 0;
    v_stack_m128 = 0;
    v_stack_m110 = 0;
    result = MiCreateMdl(a2, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)(0x1000ULL), (unsigned int)((unsigned int)(v_r12 + 1)));
    if (result == 0) goto loc_00986CC7;
    v_stack_m88 = *(unsigned __int64 *)(result + 48);
    result = CcZeroEndOfLastPage(a1, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)(0x1000ULL), (unsigned int)((unsigned int)(v_r12 + 1)));
    result = MiFlushDataSection(a1, v_stack_m108, (unsigned int)(0x1000ULL), (unsigned int)((unsigned int)(v_r12 + 1)));
    if (((unsigned int)(result)) == 0xC0000054ULL) goto loc_00986E9B;
    v_stack_m138 = 0;
    if (v_stack_m108 != 0) goto loc_00986EAA;
loc_00986956:
    if ((((unsigned int)((unsigned int)(a4))) & (0x80040ULL)) == 0) goto loc_00986970;
    v_stack_m138 = (unsigned __int8)((unsigned int)((unsigned int)(v_r12 + 1)));
    result = PsIsCurrentThreadPrefetching(a1, v_stack_m108, (unsigned int)(0x1000ULL), (unsigned int)((unsigned int)(v_r12 + 1)));
loc_00986970:
    if (condition_is_below) goto loc_00986EB3;
    result = MiCopyHeaderIfResident(v_stack_m120, v_stack_m88, (unsigned int)(0x1000ULL), (unsigned int)((unsigned int)(v_r12 + 1)));
    if ((unsigned int)(result) == 0) goto loc_00986CF1;
    v_stack_mD0 = (unsigned int)(0x1000ULL);
loc_009869A0:
    if (((*(unsigned __int8 *)(result + 10)) & (4)) != 0) goto loc_00986D6F;
loc_009869AF:
    v_stack_mE0 = *(unsigned __int64 *)(result + 24);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(result + 24))) != ((unsigned __int16)((unsigned int)(0x5A4DULL)))) goto loc_00986EEC;
    v_stack_m104 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 24) + 60)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 24) + 60)) + 264)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 24) + 60))))) goto loc_00986EF4;
    v_stack_m100 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 24) + 60));
    if (((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 24) + 60)) + 264) > v_stack_mF8) goto loc_00986F06;
    v_rdi = ((unsigned int)((unsigned int)(v_r12 + 1))) << (12);
    if (((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 24) + 60)) + 264) > ((unsigned int)((unsigned int)((unsigned int)(0x1000ULL))))) goto loc_00986F1B;
    a4 = ((unsigned int)((unsigned int)((unsigned int)(0x1000ULL)))) - ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 24) + 60)))));
    result = MiVerifyImageHeader(v_stack_m118, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 24) + 60)))) + *(unsigned __int64 *)(result + 24) * 1, *(unsigned __int64 *)(result + 24), a4);
    if ((unsigned int)(result) != 0) goto loc_00986C89;
    *(unsigned int *)(v_stack_m60) = (unsigned int)((unsigned int)(v_stack_m104));
    a1 = ((((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m118 + 16)))) & (0xFFFULL)) != 0) ? 1 : 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m118 + 16))))) >> (12));
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    if (condition_is_equal) goto loc_00986F30;
    v_stack_m98 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 24) + 60)))) + *(unsigned __int64 *)(result + 24) * 1 + 20)));
    a2 = (unsigned int)(((unsigned __int16)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 24) + 60)))) + *(unsigned __int64 *)(result + 24) * 1 + 20)))) + (24));
    v_stack_mC8 = (unsigned int)(a2);
    result = ((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 24) + 60)))) + *(unsigned __int64 *)(result + 24) * 1 + 20))) >> (16);
    v_stack_mA8 = v_xmm0;
    a1 = (unsigned int)((a2 + (unsigned __int16)(result) + (unsigned __int16)(result) * 4 * 8) + ((unsigned int)((unsigned int)(v_stack_m104))));
    if (((unsigned int)(a1)) <= ((unsigned int)((unsigned int)(v_stack_m104)))) goto loc_00986F45;
    v_r10 = (unsigned int)((unsigned int)((unsigned __int16)(result) + (unsigned __int16)(result) * 4 * 8 + a2 + (unsigned int)(v_stack_m104) * 1 * 1));
    if (((unsigned int)(*(unsigned int *)(v_stack_m118 + 24))) >= ((unsigned __int16)(result) + (unsigned __int16)(result) * 4 * 8 + a2 + (unsigned int)(v_stack_m104) * 1 * 1)) { v_r10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m118 + 24))); }
    v_stack_m100 = (unsigned int)(v_r10);
    if (((unsigned int)(v_r10)) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m118 + 16))))) goto loc_00986F5A;
    v_r10 = ((unsigned int)((unsigned int)(a2))) + ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 24) + 60)))) + *(unsigned __int64 *)(result + 24) * 1);
    if ((*(unsigned int *)(v_stack_m118 + 12)) < ((unsigned int)((unsigned int)(0x1000ULL)))) goto loc_00986F6F;
    v_stack_m148 = v_stack_mE8;
    v_stack_m150 = v_stack_mF8;
    v_stack_m158 = (unsigned int)((unsigned int)(a4));
    result = MiBuildImageControlArea((unsigned int)((unsigned int)((unsigned int)(a3))), v_r10, v_stack_m118, v_stack_mA8);
    if (sign_flag) goto loc_00986E22;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mE8) + 56) + 64) = (unsigned int)((unsigned int)(v_stack_m100));
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(v_stack_mE8 + 60))) ^ (*(unsigned __int16 *)(v_stack_m130)));
    a1 = (unsigned __int16)((a1) & ((unsigned __int16)((unsigned int)(0x3FFULL))));
    a1 = (unsigned __int16)((a1) ^ ((unsigned __int16)(*(unsigned __int16 *)(v_stack_mE8 + 60))));
    *(unsigned __int16 *)(v_stack_mE8 + 60) = (unsigned __int16)(a1);
    if (condition_is_below) goto loc_00986FB9;
loc_00986B5D:
    v_rdi = 0;
    v_stack_m128 = *(unsigned __int64 *)(v_stack_mE8);
    if (v_stack_mB8 != 0) goto loc_00986D78;
    if ((*(unsigned __int64 *)(result)) != 0) goto loc_00986D78;
    result = *(unsigned __int16 *)(v_stack_mE8 + 60);
    if ((((unsigned int)((unsigned int)(a4))) & (0x104000ULL)) == 0) {
        a1 = v_stack_m118;
        result = 0x1000ULL;
        v_rdi = 0;
        if ((*(unsigned int *)(a1 + 24)) < ((unsigned int)(result))) { v_rdi = 1; }
    }
    if (v_stack_m138 != 0) goto loc_00986BDE;
    result = IoIsDeviceEjectable(*(unsigned __int64 *)(v_stack_m120 + 8), *(unsigned __int64 *)(v_stack_m120 + 8), *(unsigned __int64 *)(v_stack_mE8), 1);
    if ((unsigned __int8)(result) != 0) goto loc_00986FE1;
    if (condition_is_below) goto loc_00986FC9;
loc_00986BD2:
    if (condition_is_below) goto loc_00986FD6;
loc_00986BDE:
    v_stack_mF0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mE8) + 16);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mE8) + 16) != 0) goto loc_00986DE8;
loc_00986BEF:
    if (condition_is_below) goto loc_00987006;
loc_00986BFD:
    result = v_stack_mB8;
    if (v_stack_mB8 != 0) {
        a2 = v_stack_mB8;
        a1 = v_stack_mE8;
        result = MiInitializeImageProtos(a1, a2, *(unsigned __int64 *)(v_stack_mE8), 1);
    }
    if ((unsigned __int8)(v_rdi) != 0) {
        result = v_stack_m118;
        a1 = v_stack_mE8;
        a2 = v_stack_m88;
        a3 = *(unsigned int *)(result + 24);
        result = MiInitializeImageHeaderPage(a1, a2, a3, 1);
    }
    result = 267;
    if ((*(unsigned __int16 *)(v_stack_m118 + 48)) == 267) {
        result = 0x8000ULL;
    }
    if ((unsigned __int8)(v_stack_m138) != 0) goto loc_0098702F;
    if (condition_is_below) goto loc_00987054;
    v_r14 = 0;
    *(unsigned __int64 *)(v_stack_m70) = v_stack_m128;
    *(unsigned __int64 *)(v_stack_m68) = result;
    goto loc_00986C9A;
loc_00986C78:
    *(unsigned int *)(v_rip + 4877174) = 34;
    goto loc_00986CA6;
loc_00986C89:
    result = 0;
    v_rbx = 0;
    v_stack_mF0 = 0;
    if (sign_flag) goto loc_00986E27;
loc_00986C9A:
    if (0 != 0) goto loc_009870C6;
loc_00986CA3:
loc_00986CA6:
    a1 = (v_stack_m50) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m118, a3, 1);
    v_rsp = (v_rsp) + (312);
    return result;
loc_00986CC7:
    *(unsigned int *)(v_rip + 4877095) = 35;
    goto loc_00986CA6;
loc_00986CD8:
    *(unsigned int *)(v_rip + 4877073) = 33;
    result = (unsigned int)(0xC000009AULL);
    if (((unsigned int)((unsigned int)(0xC000009AULL))) == 0xC00000BAULL) { result = (unsigned int)((unsigned int)(0xC0000020ULL)); }
    goto loc_00986CA6;
loc_00986CF1:
    if (v_stack_p40 != 0) goto loc_00986D10;
    if (((0) & (32)) != 0) goto loc_00986D83;
    if (condition_is_above_or_equal) goto loc_00986D10;
    if (0 <= 0x20000ULL) goto loc_00986D83;
loc_00986D10:
loc_00986D15:
    if (v_stack_mD0 != 0) goto loc_009869A0;
    result = MiReadImageHeaders(v_stack_p58, 0, result, v_stack_mD8);
    if (sign_flag) goto loc_00986E8C;
    result = (v_stack_m128) << (12);
    if (v_stack_mD0 == result) goto loc_009869A0;
    if (v_stack_mD0 >= 64) goto loc_009869A0;
    *(unsigned int *)(v_rip + 4876942) = 41;
    goto loc_00986E96;
loc_00986D6F:
    goto loc_009869AF;
loc_00986D78:
    goto loc_00986BA1;
loc_00986D83:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58 + 40))) != 0) goto loc_00986D15;
    v_rdi = ((unsigned int)((unsigned int)((unsigned int)(0xC000012FULL)))) + (0xFFFULL);
    v_rdi = (v_rdi) >> (12);
    if (v_rdi <= 1) goto loc_00986D15;
    a3 = (v_rdi) << (12);
    a4 = 0;
    result = MiCreateMdl(v_stack_p48, (unsigned int)((unsigned int)(v_stack_m120)), a3, a4);
    v_stack_mB8 = result;
    if (result == 0) goto loc_00986E82;
    result = MiDeleteImageCreationMdls(result, 1, a3, a4);
    goto loc_00986D10;
loc_00986DE8:
    a3 = 0;
    result = MiChargeCommit(v_stack_p48, result, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00986FEB;
    goto loc_00986BEF;
loc_00986E22:
loc_00986E27:
    result = MiDeleteImageCreationMdls(result, 1, a3, a4);
    if (v_stack_mF0 != 0) goto loc_0098709C;
loc_00986E46:
    if (v_stack_mE8 == 0) goto loc_00986C9A;
    a2 = 0;
    a1 = (*(unsigned __int64 *)(v_stack_mE8 + 96)) & (-8);
    result = MiUpdateSystemProtoPtesTree(a1, a2, a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_p50 + 64), a2, a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p50, a2, a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_mE8, a2, a3, a4);
    goto loc_00986C9A;
loc_00986E82:
    goto loc_00986D10;
loc_00986E8C:
    *(unsigned int *)(v_rip + 4876642) = 40;
loc_00986E96:
    goto loc_00986E27;
loc_00986E9B:
    *(unsigned int *)(v_rip + 4876627) = 36;
loc_00986EAA:
    goto loc_00986956;
loc_00986EB3:
    a2 = v_stack_m96;
    if (condition_is_below) { a2 = (unsigned int)(0x1000ULL); }
    a3 = 0;
    result = MiAllocateEntireImageFileExtents(v_stack_mE8, a2, a3, v_stack_p68);
    if (!sign_flag) goto loc_00986D10;
    *(unsigned int *)(v_rip + 4876558) = 38;
    goto loc_00986E96;
loc_00986EEC:
    goto loc_00986E96;
loc_00986EF4:
    *(unsigned int *)(v_rip + 4876532) = 42;
    goto loc_00986E96;
loc_00986F06:
    *(unsigned int *)(v_rip + 4876514) = 43;
    goto loc_00986E96;
loc_00986F1B:
    *(unsigned int *)(v_rip + 4876493) = 47;
    goto loc_00986E96;
loc_00986F30:
    *(unsigned int *)(v_rip + 4876472) = 49;
    goto loc_00986E96;
loc_00986F45:
    *(unsigned int *)(v_rip + 4876451) = 50;
    goto loc_00986E96;
loc_00986F5A:
    *(unsigned int *)(v_rip + 4876430) = 48;
    goto loc_00986E96;
loc_00986F6F:
    result = MiLogCreateImageFileMapFailure(v_stack_mE8, 1, (unsigned int)(*(unsigned int *)(v_stack_m118 + 64)), (unsigned int)(v_stack_mA4));
    result = guard_dispatch_icall(1, (unsigned int)(*(unsigned int *)(v_stack_p60 + 64)), (unsigned int)(v_stack_mA4), (unsigned int)(v_stack_mA4));
loc_00986FB9:
    goto loc_00986B5D;
loc_00986FC9:
    if ((((unsigned __int8)((unsigned int)(v_stack_mA4))) & ((unsigned __int8)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_p60 + 64)) + 52))))) != 0) goto loc_00986FE1;
    goto loc_00986BD2;
loc_00986FD6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_p60 + 64)) + 52)))) & (16)) == 0) goto loc_00986BDE;
loc_00986FE1:
    v_stack_p40 = (unsigned __int8)((unsigned int)(v_stack_mA4));
    goto loc_00986BDE;
loc_00986FEB:
    result = 0;
    *(unsigned int *)(v_rip + 4876289) = 57;
    v_stack_mF0 = 0;
    goto loc_00986E22;
loc_00987006:
    if (condition_is_below) goto loc_00986BFD;
    if (((*(unsigned int *)(v_stack_p60 + 20)) & (0x1000000ULL)) != 0) goto loc_00986BFD;
    *(unsigned int *)(v_stack_mE8 + 56) = (unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mE8) + 56));
    goto loc_00986BFD;
loc_0098702F:
    *(unsigned int *)(v_stack_mE8 + 56) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mE8 + 56)));
    *(unsigned int *)(v_stack_mE8 + 56) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mE8 + 56)));
loc_00987054:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_mE8))) >> (17));
    a1 = (unsigned int)((a1) & ((unsigned int)((unsigned int)(0xC000012DULL))));
    v_stack_p30 = (unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mE8 + 56))));
    v_stack_p28 = (unsigned int)(a1);
    v_rbx = (unsigned int)((v_stack_mE8) >> (16));
    v_rbx = (unsigned int)((v_rbx) & ((unsigned int)((unsigned int)(0xC000012DULL))));
    v_stack_p20 = (unsigned int)(v_rbx);
    result = MiEnableImageDirectMap(v_stack_m120, v_stack_mE8, (unsigned int)(*(unsigned int *)(v_stack_p60 + 64)), v_stack_p68);
    *(unsigned int *)(v_rip + 4876129) = 58;
    goto loc_00986E22;
loc_0098709C:
    result = -(v_stack_m120);
    a3 = 0;
    result = MiReturnCommit(1, v_stack_m120, a3, v_stack_p68);
    goto loc_00986E46;
loc_009870C6:
    result = MiDeleteFileExtentList(v_stack_p68, v_stack_m120, a3, v_stack_p68);
    goto loc_00986CA3;
}
```

## 5. (Beta) C Style

```c
int64_t MiCreateImageFileMap(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m104;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint8_t v_stack_m138;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint32_t v_stack_m158;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint16_t v_stack_m96;
    uint32_t v_stack_m98;
    uint32_t v_stack_mA4;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF4;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint8_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;

    local_rsp = (local_rsp) - (312);
    result = (*(uint64_t *)(v_rip + 0x483EF0)) ^ (local_rsp);
    v_stack_m50 = result;
    v_stack_m70 = Arg5;
    local_r12 = 0;
    v_stack_m68 = Arg6;
    v_stack_m118 = Arg7;
    v_stack_m60 = Arg8;
    result = 0;
    v_stack_m130 = Arg2;
    v_stack_m98 = 0;
    v_stack_m120 = Arg1;
    v_stack_mA8 = v_xmm0;
    v_stack_m108 = 0;
    v_stack_mD8 = v_xmm0;
    v_stack_mF8 = 0;
    v_stack_m80 = v_xmm1;
    result = FsRtlGetFileSize(Arg1, v_stack_mF8, Arg3, Arg4);
    if (sign_flag) goto loc_00986CD8;
    if (v_stack_mF4 != 0) goto loc_00986C78;
    v_stack_mF0 = 0;
    v_stack_mE8 = 0;
    v_stack_m128 = 0;
    v_stack_m110 = 0;
    result = MiCreateMdl(Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)(0x1000ULL), (uint32_t)((uint32_t)(local_r12 + 1)));
    if (result == 0) goto loc_00986CC7;
    v_stack_m88 = *(uint64_t *)(result + 0x30);
    result = CcZeroEndOfLastPage(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)(0x1000ULL), (uint32_t)((uint32_t)(local_r12 + 1)));
    result = MiFlushDataSection(Arg1, v_stack_m108, (uint32_t)(0x1000ULL), (uint32_t)((uint32_t)(local_r12 + 1)));
    if (((uint32_t)(result)) == 0xC0000054ULL) goto loc_00986E9B;
    v_stack_m138 = 0;
    if (v_stack_m108 != 0) goto loc_00986EAA;
loc_00986956:
    if ((((uint32_t)((uint32_t)(Arg4))) & (0x80040ULL)) == 0) goto loc_00986970;
    v_stack_m138 = (uint8_t)((uint32_t)((uint32_t)(local_r12 + 1)));
    result = PsIsCurrentThreadPrefetching(Arg1, v_stack_m108, (uint32_t)(0x1000ULL), (uint32_t)((uint32_t)(local_r12 + 1)));
loc_00986970:
    if (condition_is_below) goto loc_00986EB3;
    result = MiCopyHeaderIfResident(v_stack_m120, v_stack_m88, (uint32_t)(0x1000ULL), (uint32_t)((uint32_t)(local_r12 + 1)));
    if ((uint32_t)(result) == 0) goto loc_00986CF1;
    v_stack_mD0 = (uint32_t)(0x1000ULL);
loc_009869A0:
    if (((*(uint8_t *)(result + 0xA)) & (4)) != 0) goto loc_00986D6F;
loc_009869AF:
    v_stack_mE0 = *(uint64_t *)(result + 0x18);
    if ((*(uint16_t *)(*(uint64_t *)(result + 0x18))) != ((uint16_t)((uint32_t)(0x5A4DULL)))) goto loc_00986EEC;
    v_stack_m104 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x18) + 0x3C)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x18) + 0x3C)) + 264)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x18) + 0x3C))))) goto loc_00986EF4;
    v_stack_m100 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x18) + 0x3C));
    if (((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x18) + 0x3C)) + 264) > v_stack_mF8) goto loc_00986F06;
    local_rdi = ((uint32_t)((uint32_t)(local_r12 + 1))) << (12);
    if (((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x18) + 0x3C)) + 264) > ((uint32_t)((uint32_t)((uint32_t)(0x1000ULL))))) goto loc_00986F1B;
    Arg4 = ((uint32_t)((uint32_t)((uint32_t)(0x1000ULL)))) - ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x18) + 0x3C)))));
    result = MiVerifyImageHeader(v_stack_m118, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x18) + 0x3C)))) + *(uint64_t *)(result + 0x18) * 1, *(uint64_t *)(result + 0x18), Arg4);
    if ((uint32_t)(result) != 0) goto loc_00986C89;
    *(uint32_t *)(v_stack_m60) = (uint32_t)((uint32_t)(v_stack_m104));
    Arg1 = ((((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m118 + 0x10)))) & (0xFFFULL)) != 0) ? 1 : 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m118 + 0x10))))) >> (12));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    if (condition_is_equal) goto loc_00986F30;
    v_stack_m98 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x18) + 0x3C)))) + *(uint64_t *)(result + 0x18) * 1 + 0x14)));
    Arg2 = (uint32_t)(((uint16_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x18) + 0x3C)))) + *(uint64_t *)(result + 0x18) * 1 + 0x14)))) + (24));
    v_stack_mC8 = (uint32_t)(Arg2);
    result = ((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x18) + 0x3C)))) + *(uint64_t *)(result + 0x18) * 1 + 0x14))) >> (16);
    v_stack_mA8 = v_xmm0;
    Arg1 = (uint32_t)((Arg2 + (uint16_t)(result) + (uint16_t)(result) * 4 * 8) + ((uint32_t)((uint32_t)(v_stack_m104))));
    if (((uint32_t)(Arg1)) <= ((uint32_t)((uint32_t)(v_stack_m104)))) goto loc_00986F45;
    local_r10 = (uint32_t)((uint32_t)((uint16_t)(result) + (uint16_t)(result) * 4 * 8 + Arg2 + (uint32_t)(v_stack_m104) * 1 * 1));
    if (((uint32_t)(*(uint32_t *)(v_stack_m118 + 0x18))) >= ((uint16_t)(result) + (uint16_t)(result) * 4 * 8 + Arg2 + (uint32_t)(v_stack_m104) * 1 * 1)) { local_r10 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m118 + 0x18))); }
    v_stack_m100 = (uint32_t)(local_r10);
    if (((uint32_t)(local_r10)) > ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m118 + 0x10))))) goto loc_00986F5A;
    local_r10 = ((uint32_t)((uint32_t)(Arg2))) + ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x18) + 0x3C)))) + *(uint64_t *)(result + 0x18) * 1);
    if ((*(uint32_t *)(v_stack_m118 + 0xC)) < ((uint32_t)((uint32_t)(0x1000ULL)))) goto loc_00986F6F;
    v_stack_m148 = v_stack_mE8;
    v_stack_m150 = v_stack_mF8;
    v_stack_m158 = (uint32_t)((uint32_t)(Arg4));
    result = MiBuildImageControlArea((uint32_t)((uint32_t)((uint32_t)(Arg3))), local_r10, v_stack_m118, v_stack_mA8);
    if (sign_flag) goto loc_00986E22;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mE8) + 0x38) + 0x40) = (uint32_t)((uint32_t)(v_stack_m100));
    Arg1 = (uint16_t)(((uint16_t)(*(uint16_t *)(v_stack_mE8 + 0x3C))) ^ (*(uint16_t *)(v_stack_m130)));
    Arg1 = (uint16_t)((Arg1) & ((uint16_t)((uint32_t)(0x3FFULL))));
    Arg1 = (uint16_t)((Arg1) ^ ((uint16_t)(*(uint16_t *)(v_stack_mE8 + 0x3C))));
    *(uint16_t *)(v_stack_mE8 + 0x3C) = (uint16_t)(Arg1);
    if (condition_is_below) goto loc_00986FB9;
loc_00986B5D:
    local_rdi = 0;
    v_stack_m128 = *(uint64_t *)(v_stack_mE8);
    if (v_stack_mB8 != 0) goto loc_00986D78;
    if ((*(uint64_t *)(result)) != 0) goto loc_00986D78;
    result = *(uint16_t *)(v_stack_mE8 + 0x3C);
    if ((((uint32_t)((uint32_t)(Arg4))) & (0x104000ULL)) == 0) {
        Arg1 = v_stack_m118;
        result = 0x1000ULL;
        local_rdi = 0;
        if ((*(uint32_t *)(Arg1 + 0x18)) < ((uint32_t)(result))) { local_rdi = 1; }
    }
    if (v_stack_m138 != 0) goto loc_00986BDE;
    result = IoIsDeviceEjectable(*(uint64_t *)(v_stack_m120 + 0x8), *(uint64_t *)(v_stack_m120 + 0x8), *(uint64_t *)(v_stack_mE8), 1);
    if ((uint8_t)(result) != 0) goto loc_00986FE1;
    if (condition_is_below) goto loc_00986FC9;
loc_00986BD2:
    if (condition_is_below) goto loc_00986FD6;
loc_00986BDE:
    v_stack_mF0 = *(uint64_t *)(*(uint64_t *)(v_stack_mE8) + 0x10);
    if (*(uint64_t *)(*(uint64_t *)(v_stack_mE8) + 0x10) != 0) goto loc_00986DE8;
loc_00986BEF:
    if (condition_is_below) goto loc_00987006;
loc_00986BFD:
    result = v_stack_mB8;
    if (v_stack_mB8 != 0) {
        Arg2 = v_stack_mB8;
        Arg1 = v_stack_mE8;
        result = MiInitializeImageProtos(Arg1, Arg2, *(uint64_t *)(v_stack_mE8), 1);
    }
    if ((uint8_t)(local_rdi) != 0) {
        result = v_stack_m118;
        Arg1 = v_stack_mE8;
        Arg2 = v_stack_m88;
        Arg3 = *(uint32_t *)(result + 0x18);
        result = MiInitializeImageHeaderPage(Arg1, Arg2, Arg3, 1);
    }
    result = 267;
    if ((*(uint16_t *)(v_stack_m118 + 0x30)) == 267) {
        result = 0x8000ULL;
    }
    if ((uint8_t)(v_stack_m138) != 0) goto loc_0098702F;
    if (condition_is_below) goto loc_00987054;
    local_r14 = 0;
    *(uint64_t *)(v_stack_m70) = v_stack_m128;
    *(uint64_t *)(v_stack_m68) = result;
    goto loc_00986C9A;
loc_00986C78:
    *(uint32_t *)(v_rip + 0x4A6B76) = 34;
    goto loc_00986CA6;
loc_00986C89:
    result = 0;
    local_rbx = 0;
    v_stack_mF0 = 0;
    if (sign_flag) goto loc_00986E27;
loc_00986C9A:
    if (0 != 0) goto loc_009870C6;
loc_00986CA3:
loc_00986CA6:
    Arg1 = (v_stack_m50) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m118, Arg3, 1);
    local_rsp = (local_rsp) + (312);
    return result;
loc_00986CC7:
    *(uint32_t *)(v_rip + 0x4A6B27) = 35;
    goto loc_00986CA6;
loc_00986CD8:
    *(uint32_t *)(v_rip + 0x4A6B11) = 33;
    result = (uint32_t)(0xC000009AULL);
    if (((uint32_t)((uint32_t)(0xC000009AULL))) == 0xC00000BAULL) { result = (uint32_t)((uint32_t)(0xC0000020ULL)); }
    goto loc_00986CA6;
loc_00986CF1:
    if (v_stack_p40 != 0) goto loc_00986D10;
    if (((0) & (32)) != 0) goto loc_00986D83;
    if (condition_is_above_or_equal) goto loc_00986D10;
    if (0 <= 0x20000ULL) goto loc_00986D83;
loc_00986D10:
loc_00986D15:
    if (v_stack_mD0 != 0) goto loc_009869A0;
    result = MiReadImageHeaders(v_stack_p58, 0, result, v_stack_mD8);
    if (sign_flag) goto loc_00986E8C;
    result = (v_stack_m128) << (12);
    if (v_stack_mD0 == result) goto loc_009869A0;
    if (v_stack_mD0 >= 64) goto loc_009869A0;
    *(uint32_t *)(v_rip + 0x4A6A8E) = 41;
    goto loc_00986E96;
loc_00986D6F:
    goto loc_009869AF;
loc_00986D78:
    goto loc_00986BA1;
loc_00986D83:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p58 + 0x28))) != 0) goto loc_00986D15;
    local_rdi = ((uint32_t)((uint32_t)((uint32_t)(0xC000012FULL)))) + (0xFFFULL);
    local_rdi = (local_rdi) >> (12);
    if (local_rdi <= 1) goto loc_00986D15;
    Arg3 = (local_rdi) << (12);
    Arg4 = 0;
    result = MiCreateMdl(v_stack_p48, (uint32_t)((uint32_t)(v_stack_m120)), Arg3, Arg4);
    v_stack_mB8 = result;
    if (result == 0) goto loc_00986E82;
    result = MiDeleteImageCreationMdls(result, 1, Arg3, Arg4);
    goto loc_00986D10;
loc_00986DE8:
    Arg3 = 0;
    result = MiChargeCommit(v_stack_p48, result, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00986FEB;
    goto loc_00986BEF;
loc_00986E22:
loc_00986E27:
    result = MiDeleteImageCreationMdls(result, 1, Arg3, Arg4);
    if (v_stack_mF0 != 0) goto loc_0098709C;
loc_00986E46:
    if (v_stack_mE8 == 0) goto loc_00986C9A;
    Arg2 = 0;
    Arg1 = (*(uint64_t *)(v_stack_mE8 + 0x60)) & (-8);
    result = MiUpdateSystemProtoPtesTree(Arg1, Arg2, Arg3, Arg4);
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_p50 + 0x40), Arg2, Arg3, Arg4);
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p50, Arg2, Arg3, Arg4);
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_mE8, Arg2, Arg3, Arg4);
    goto loc_00986C9A;
loc_00986E82:
    goto loc_00986D10;
loc_00986E8C:
    *(uint32_t *)(v_rip + 0x4A6962) = 40;
loc_00986E96:
    goto loc_00986E27;
loc_00986E9B:
    *(uint32_t *)(v_rip + 0x4A6953) = 36;
loc_00986EAA:
    goto loc_00986956;
loc_00986EB3:
    Arg2 = v_stack_m96;
    if (condition_is_below) { Arg2 = (uint32_t)(0x1000ULL); }
    Arg3 = 0;
    result = MiAllocateEntireImageFileExtents(v_stack_mE8, Arg2, Arg3, v_stack_p68);
    if (!sign_flag) goto loc_00986D10;
    *(uint32_t *)(v_rip + 0x4A690E) = 38;
    goto loc_00986E96;
loc_00986EEC:
    goto loc_00986E96;
loc_00986EF4:
    *(uint32_t *)(v_rip + 0x4A68F4) = 42;
    goto loc_00986E96;
loc_00986F06:
    *(uint32_t *)(v_rip + 0x4A68E2) = 43;
    goto loc_00986E96;
loc_00986F1B:
    *(uint32_t *)(v_rip + 0x4A68CD) = 47;
    goto loc_00986E96;
loc_00986F30:
    *(uint32_t *)(v_rip + 0x4A68B8) = 49;
    goto loc_00986E96;
loc_00986F45:
    *(uint32_t *)(v_rip + 0x4A68A3) = 50;
    goto loc_00986E96;
loc_00986F5A:
    *(uint32_t *)(v_rip + 0x4A688E) = 48;
    goto loc_00986E96;
loc_00986F6F:
    result = MiLogCreateImageFileMapFailure(v_stack_mE8, 1, (uint32_t)(*(uint32_t *)(v_stack_m118 + 0x40)), (uint32_t)(v_stack_mA4));
    result = guard_dispatch_icall(1, (uint32_t)(*(uint32_t *)(v_stack_p60 + 0x40)), (uint32_t)(v_stack_mA4), (uint32_t)(v_stack_mA4));
loc_00986FB9:
    goto loc_00986B5D;
loc_00986FC9:
    if ((((uint8_t)((uint32_t)(v_stack_mA4))) & ((uint8_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_p60 + 0x40)) + 0x34))))) != 0) goto loc_00986FE1;
    goto loc_00986BD2;
loc_00986FD6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_p60 + 0x40)) + 0x34)))) & (16)) == 0) goto loc_00986BDE;
loc_00986FE1:
    v_stack_p40 = (uint8_t)((uint32_t)(v_stack_mA4));
    goto loc_00986BDE;
loc_00986FEB:
    result = 0;
    *(uint32_t *)(v_rip + 0x4A6801) = 57;
    v_stack_mF0 = 0;
    goto loc_00986E22;
loc_00987006:
    if (condition_is_below) goto loc_00986BFD;
    if (((*(uint32_t *)(v_stack_p60 + 0x14)) & (0x1000000ULL)) != 0) goto loc_00986BFD;
    *(uint32_t *)(v_stack_mE8 + 0x38) = (uint32_t)(*(uint64_t *)(*(uint64_t *)(v_stack_mE8) + 0x38));
    goto loc_00986BFD;
loc_0098702F:
    *(uint32_t *)(v_stack_mE8 + 0x38) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mE8 + 0x38)));
    *(uint32_t *)(v_stack_mE8 + 0x38) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mE8 + 0x38)));
loc_00987054:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_mE8))) >> (17));
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)((uint32_t)(0xC000012DULL))));
    v_stack_p30 = (uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mE8 + 0x38))));
    v_stack_p28 = (uint32_t)(Arg1);
    local_rbx = (uint32_t)((v_stack_mE8) >> (16));
    local_rbx = (uint32_t)((local_rbx) & ((uint32_t)((uint32_t)(0xC000012DULL))));
    v_stack_p20 = (uint32_t)(local_rbx);
    result = MiEnableImageDirectMap(v_stack_m120, v_stack_mE8, (uint32_t)(*(uint32_t *)(v_stack_p60 + 0x40)), v_stack_p68);
    *(uint32_t *)(v_rip + 0x4A6761) = 58;
    goto loc_00986E22;
loc_0098709C:
    result = -(v_stack_m120);
    Arg3 = 0;
    result = MiReturnCommit(1, v_stack_m120, Arg3, v_stack_p68);
    goto loc_00986E46;
loc_009870C6:
    result = MiDeleteFileExtentList(v_stack_p68, v_stack_m120, Arg3, v_stack_p68);
    goto loc_00986CA3;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00986830&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
