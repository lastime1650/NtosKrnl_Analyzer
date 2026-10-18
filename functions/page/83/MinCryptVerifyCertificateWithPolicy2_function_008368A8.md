# MinCryptVerifyCertificateWithPolicy2

- RVA: `0x008368A8`–`0x00837513` (길이 `3,179` bytes)
- VA: `0x00000001408368A8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DADA0`
- 디코드: `772`개 명령, `3,179/3,179` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **25**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0083696A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008369D0` → [I_MinCryptGetCertificateEKUs](I_MinCryptGetCertificateEKUs_function_008367D0.md) (function, `0x008367D0`)
- `0x00836AD8` → [I_MinCryptCheckEKURequirements](I_MinCryptCheckEKURequirements_function_00839218.md) (function, `0x00839218`)
- `0x00836B0C` → [I_MinCryptGetCertValidityPeriod](I_MinCryptGetCertValidityPeriod_function_00836770.md) (function, `0x00836770`)
- `0x00836B1F` → [I_MinCryptCheckEKU](I_MinCryptCheckEKU_function_008364C4.md) (function, `0x008364C4`)
- `0x00836B79` → [I_MinCryptCheckEKU](I_MinCryptCheckEKU_function_008364C4.md) (function, `0x008364C4`)
- `0x00836C32` → [MinCryptDecodeHashAlgorithmIdentifier](MinCryptDecodeHashAlgorithmIdentifier_function_008361A0.md) (function, `0x008361A0`)
- `0x00836C5A` → [MinCryptHashMemory](../../text/6A/MinCryptHashMemory_function_006A5F04.md) (function, `0x006A5F04`)
- `0x00836D5E` → [I_MinCryptGetCommonName](I_MinCryptGetCommonName_function_0083685C.md) (function, `0x0083685C`)
- `0x00836DD7` → [I_MinCryptGetCommonName](I_MinCryptGetCommonName_function_0083685C.md) (function, `0x0083685C`)
- `0x00836E98` → [I_MinCryptIsCertificateHashRevokedV2](../../text/6A/I_MinCryptIsCertificateHashRevokedV2_function_006A5F24.md) (function, `0x006A5F24`)
- `0x00836F10` → [I_MinCryptGetCertificateEKUs](I_MinCryptGetCertificateEKUs_function_008367D0.md) (function, `0x008367D0`)
- `0x00836F30` → [I_MinCryptCheckEKURequirements](I_MinCryptCheckEKURequirements_function_00839218.md) (function, `0x00839218`)
- `0x00836F6B` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x00836FA5` → [MincryptValidateBasicConstraints](MincryptValidateBasicConstraints_function_00837B84.md) (function, `0x00837B84`)
- `0x00836FCB` → [I_MinCryptFindRootByKey](I_MinCryptFindRootByKey_function_00836620.md) (function, `0x00836620`)
- `0x0083701D` → [MinCryptIsCertPresent](../../text/6A/MinCryptIsCertPresent_function_006A631C.md) (function, `0x006A631C`)
- `0x00837031` → [MinCryptIsKeyPresent](../../text/6A/MinCryptIsKeyPresent_function_006A638C.md) (function, `0x006A638C`)
- `0x0083713C` → [MinCryptVerifySignedHash2](MinCryptVerifySignedHash2_function_008362A0.md) (function, `0x008362A0`)
- `0x00837246` → [I_MinCryptFindRootByName](I_MinCryptFindRootByName_function_00836694.md) (function, `0x00836694`)
- `0x0083733F` → [I_MinCryptFindIssuerCertificateByName](I_MinCryptFindIssuerCertificateByName_function_00836530.md) (function, `0x00836530`)
- `0x00837358` → [MinCryptDecodeHashAlgorithmIdentifier](MinCryptDecodeHashAlgorithmIdentifier_function_008361A0.md) (function, `0x008361A0`)
- `0x008373B2` → [MinCryptCheckCertsAndKeys](../../text/6A/MinCryptCheckCertsAndKeys_function_006A61F8.md) (function, `0x006A61F8`)
- `0x008374D4` → [I_MincryptAddChainInfo](I_MincryptAddChainInfo_function_00839314.md) (function, `0x00839314`)
- `0x008374E8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [MincrypK_ParseCertificateChainWithPolicy2](MincrypK_ParseCertificateChainWithPolicy2_function_00837534.md) at `0x00837678`
- [I_MinCryptVerifyAuthenticodeTimeStamp](I_MinCryptVerifyAuthenticodeTimeStamp_function_00838090.md) at `0x0083818B`
- [MinCrypK_VerifySignedDataKModeEx](MinCrypK_VerifySignedDataKModeEx_function_00838568.md) at `0x0083876C`

### Static image references
- `0x00836B18` → RVA `0x00B4BC88` (`PAGE`; read)
- `0x00836B2C` → RVA `0x00FD8288` (`PAGEDATA`; read)
- `0x00836B5E` → RVA `0x00E11CC8` (`.data`; read)
- `0x00836B72` → RVA `0x00B4BC78` (`PAGE`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **8**
  - `0x0083696A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00836C5A` → [MinCryptHashMemory](../../text/6A/MinCryptHashMemory_function_006A5F04.md) (`PAGE` → `.text`)
  - `0x00836E98` → [I_MinCryptIsCertificateHashRevokedV2](../../text/6A/I_MinCryptIsCertificateHashRevokedV2_function_006A5F24.md) (`PAGE` → `.text`)
  - `0x00836F6B` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0083701D` → [MinCryptIsCertPresent](../../text/6A/MinCryptIsCertPresent_function_006A631C.md) (`PAGE` → `.text`)
  - `0x00837031` → [MinCryptIsKeyPresent](../../text/6A/MinCryptIsKeyPresent_function_006A638C.md) (`PAGE` → `.text`)
  - `0x008373B2` → [MinCryptCheckCertsAndKeys](../../text/6A/MinCryptCheckCertsAndKeys_function_006A61F8.md) (`PAGE` → `.text`)
  - `0x008374E8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008368A8  4C 8B DC                        mov r11, rsp
008368AB  4D 89 43 18                     mov qword ptr [r11 + 0x18], r8
008368AF  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
008368B3  49 89 4B 08                     mov qword ptr [r11 + 8], rcx
008368B7  53                              push rbx
008368B8  56                              push rsi
008368B9  57                              push rdi
008368BA  41 54                           push r12
008368BC  41 55                           push r13
008368BE  41 56                           push r14
008368C0  41 57                           push r15
008368C2  48 81 EC 10 01 00 00            sub rsp, 0x110
008368C9  4D 8B E9                        mov r13, r9
008368CC  4C 8B F1                        mov r14, rcx
008368CF  45 33 FF                        xor r15d, r15d
008368D2  44 89 7C 24 50                  mov dword ptr [rsp + 0x50], r15d
008368D7  45 89 BB 48 FF FF FF            mov dword ptr [r11 - 0xb8], r15d
008368DE  C7 44 24 78 32 00 00 00         mov dword ptr [rsp + 0x78], 0x32
008368E6  45 89 BB 3C FF FF FF            mov dword ptr [r11 - 0xc4], r15d
008368ED  44 89 7C 24 7C                  mov dword ptr [rsp + 0x7c], r15d
008368F2  44 89 7C 24 58                  mov dword ptr [rsp + 0x58], r15d
008368F7  44 89 7C 24 54                  mov dword ptr [rsp + 0x54], r15d
008368FC  41 8B FF                        mov edi, r15d
008368FF  44 89 7C 24 5C                  mov dword ptr [rsp + 0x5c], r15d
00836904  45 89 BB 38 FF FF FF            mov dword ptr [r11 - 0xc8], r15d
0083690B  4D 89 BB 78 FF FF FF            mov qword ptr [r11 - 0x88], r15
00836912  45 89 BB 40 FF FF FF            mov dword ptr [r11 - 0xc0], r15d
00836919  4D 89 7B 90                     mov qword ptr [r11 - 0x70], r15
0083691D  44 89 7C 24 74                  mov dword ptr [rsp + 0x74], r15d
00836922  4D 89 BB 50 FF FF FF            mov qword ptr [r11 - 0xb0], r15
00836929  4C 89 7C 24 68                  mov qword ptr [rsp + 0x68], r15
0083692E  4D 89 BB 68 FF FF FF            mov qword ptr [r11 - 0x98], r15
00836935  4D 89 BB 58 FF FF FF            mov qword ptr [r11 - 0xa8], r15
0083693C  4D 89 BB 60 FF FF FF            mov qword ptr [r11 - 0xa0], r15
00836943  44 88 7C 24 60                  mov byte ptr [rsp + 0x60], r15b
00836948  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00836952  49 89 43 80                     mov qword ptr [r11 - 0x80], rax
00836956  49 89 4B B0                     mov qword ptr [r11 - 0x50], rcx
0083695A  BA A0 0B 00 00                  mov edx, 0xba0
0083695F  B9 02 01 00 00                  mov ecx, 0x102
00836964  41 B8 43 49 63 72               mov r8d, 0x72634943
0083696A  E8 81 B7 34 00                  call 0x140b820f0
0083696F  48 8B F0                        mov rsi, rax
00836972  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00836977  48 85 C0                        test rax, rax
0083697A  75 14                           jne 0x140836990
0083697C  BB 17 00 00 C0                  mov ebx, 0xc0000017
00836981  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00836985  41 BC 03 06 00 C0               mov r12d, 0xc0000603
0083698B  E9 A0 0A 00 00                  jmp 0x140837430
00836990  48 05 20 03 00 00               add rax, 0x320
00836996  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
0083699E  48 8D B0 B0 00 00 00            lea rsi, [rax + 0xb0]
008369A5  48 89 B4 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rsi
008369AD  48 8D 86 20 03 00 00            lea rax, [rsi + 0x320]
008369B4  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
008369BC  49 8D 8E E0 00 00 00            lea rcx, [r14 + 0xe0]
008369C3  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
008369C8  4C 8B C6                        mov r8, rsi
008369CB  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
008369D0  E8 FB FD FF FF                  call 0x1408367d0
008369D5  8B D8                           mov ebx, eax
008369D7  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008369DB  85 C0                           test eax, eax
008369DD  78 A6                           js 0x140836985
008369DF  41 8B D7                        mov edx, r15d
008369E2  41 BA FC FF FF FF               mov r10d, 0xfffffffc
008369E8  41 B9 95 00 00 C0               mov r9d, 0xc0000095
008369EE  41 83 C8 FF                     or r8d, 0xffffffff
008369F2  41 BC 01 00 00 00               mov r12d, 1
008369F8  89 94 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], edx
008369FF  3B 54 24 78                     cmp edx, dword ptr [rsp + 0x78]
00836A03  73 79                           jae 0x140836a7e
00836A05  8B C2                           mov eax, edx
00836A07  48 03 C0                        add rax, rax
00836A0A  8B 0C C6                        mov ecx, dword ptr [rsi + rax*8]
00836A0D  8D 41 03                        lea eax, [rcx + 3]
00836A10  41 23 C2                        and eax, r10d
00836A13  3B C1                           cmp eax, ecx
00836A15  73 08                           jae 0x140836a1f
00836A17  41 8B D9                        mov ebx, r9d
00836A1A  E9 62 FF FF FF                  jmp 0x140836981
00836A1F  03 C7                           add eax, edi
00836A21  3B C7                           cmp eax, edi
00836A23  72 0D                           jb 0x140836a32
00836A25  8B F8                           mov edi, eax
00836A27  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
00836A2B  41 8B DF                        mov ebx, r15d
00836A2E  8B C8                           mov ecx, eax
00836A30  EB 11                           jmp 0x140836a43
00836A32  41 8B F8                        mov edi, r8d
00836A35  44 89 44 24 5C                  mov dword ptr [rsp + 0x5c], r8d
00836A3A  41 8B D9                        mov ebx, r9d
00836A3D  41 8B C0                        mov eax, r8d
00836A40  41 8B C8                        mov ecx, r8d
00836A43  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00836A47  85 DB                           test ebx, ebx
00836A49  0F 88 36 FF FF FF               js 0x140836985
00836A4F  8D 78 10                        lea edi, [rax + 0x10]
00836A52  3B F9                           cmp edi, ecx
00836A54  72 09                           jb 0x140836a5f
00836A56  89 7C 24 5C                     mov dword ptr [rsp + 0x5c], edi
00836A5A  41 8B DF                        mov ebx, r15d
00836A5D  EB 0B                           jmp 0x140836a6a
00836A5F  41 8B F8                        mov edi, r8d
00836A62  44 89 44 24 5C                  mov dword ptr [rsp + 0x5c], r8d
00836A67  41 8B D9                        mov ebx, r9d
00836A6A  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00836A6E  85 DB                           test ebx, ebx
00836A70  0F 88 0F FF FF FF               js 0x140836985
00836A76  41 03 D4                        add edx, r12d
00836A79  E9 7A FF FF FF                  jmp 0x1408369f8
00836A7E  48 8B 84 24 78 01 00 00         mov rax, qword ptr [rsp + 0x178]
00836A86  48 85 C0                        test rax, rax
00836A89  74 35                           je 0x140836ac0
00836A8B  8B 00                           mov eax, dword ptr [rax]
00836A8D  8D 48 03                        lea ecx, [rax + 3]
00836A90  41 23 CA                        and ecx, r10d
00836A93  3B C8                           cmp ecx, eax
00836A95  72 80                           jb 0x140836a17
00836A97  8D 04 39                        lea eax, [rcx + rdi]
00836A9A  3B C7                           cmp eax, edi
00836A9C  72 0B                           jb 0x140836aa9
00836A9E  8B F8                           mov edi, eax
00836AA0  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
00836AA4  41 8B DF                        mov ebx, r15d
00836AA7  EB 0B                           jmp 0x140836ab4
00836AA9  41 8B F8                        mov edi, r8d
00836AAC  44 89 44 24 5C                  mov dword ptr [rsp + 0x5c], r8d
00836AB1  41 8B D9                        mov ebx, r9d
00836AB4  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00836AB8  85 DB                           test ebx, ebx
00836ABA  0F 88 C5 FE FF FF               js 0x140836985
00836AC0  4D 85 ED                        test r13, r13
00836AC3  74 2C                           je 0x140836af1
00836AC5  41 8B 45 04                     mov eax, dword ptr [r13 + 4]
00836AC9  41 84 C4                        test r12b, al
00836ACC  75 23                           jne 0x140836af1
00836ACE  4D 8B C5                        mov r8, r13
00836AD1  48 8B D6                        mov rdx, rsi
00836AD4  8B 4C 24 78                     mov ecx, dword ptr [rsp + 0x78]
00836AD8  E8 3B 27 00 00                  call 0x140839218
00836ADD  84 C0                           test al, al
00836ADF  75 10                           jne 0x140836af1
00836AE1  0F BA 6C 24 58 13               bts dword ptr [rsp + 0x58], 0x13
00836AE7  BB 28 04 00 C0                  mov ebx, 0xc0000428
00836AEC  E9 90 FE FF FF                  jmp 0x140836981
00836AF1  4C 8D 84 24 A8 00 00 00         lea r8, [rsp + 0xa8]
00836AF9  48 8D 94 24 A0 00 00 00         lea rdx, [rsp + 0xa0]
00836B01  4C 8B B4 24 50 01 00 00         mov r14, qword ptr [rsp + 0x150]
00836B09  49 8B CE                        mov rcx, r14
00836B0C  E8 5F FC FF FF                  call 0x140836770
00836B11  4C 8B C6                        mov r8, rsi
00836B14  8B 54 24 78                     mov edx, dword ptr [rsp + 0x78]
00836B18  48 8D 0D 69 51 31 00            lea rcx, [rip + 0x315169]
00836B1F  E8 A0 F9 FF FF                  call 0x1408364c4
00836B24  88 44 24 71                     mov byte ptr [rsp + 0x71], al
00836B28  84 C0                           test al, al
00836B2A  74 32                           je 0x140836b5e
00836B2C  48 8B 05 55 17 7A 00            mov rax, qword ptr [rip + 0x7a1755]
00836B33  48 85 C0                        test rax, rax
00836B36  7E 26                           jle 0x140836b5e
00836B38  41 0F B6 CF                     movzx ecx, r15b
00836B3C  48 39 84 24 A0 00 00 00         cmp qword ptr [rsp + 0xa0], rax
00836B44  41 0F 4C CC                     cmovl ecx, r12d
00836B48  84 C9                           test cl, cl
00836B4A  74 12                           je 0x140836b5e
00836B4C  81 4C 24 58 00 00 60 00         or dword ptr [rsp + 0x58], 0x600000
00836B54  BB 05 06 00 C0                  mov ebx, 0xc0000605
00836B59  E9 23 FE FF FF                  jmp 0x140836981
00836B5E  80 3D 63 B1 5D 00 00            cmp byte ptr [rip + 0x5db163], 0
00836B65  0F 85 85 00 00 00               jne 0x140836bf0
00836B6B  4C 8B C6                        mov r8, rsi
00836B6E  8B 54 24 78                     mov edx, dword ptr [rsp + 0x78]
00836B72  48 8D 0D FF 50 31 00            lea rcx, [rip + 0x3150ff]
00836B79  E8 46 F9 FF FF                  call 0x1408364c4
00836B7E  84 C0                           test al, al
00836B80  74 6E                           je 0x140836bf0
00836B82  41 8A CF                        mov cl, r15b
00836B85  88 4C 24 70                     mov byte ptr [rsp + 0x70], cl
00836B89  48 B8 14 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000014
00836B93  48 8B 00                        mov rax, qword ptr [rax]
00836B96  44 38 7C 24 71                  cmp byte ptr [rsp + 0x71], r15b
00836B9B  75 0A                           jne 0x140836ba7
00836B9D  48 3B 84 24 A0 00 00 00         cmp rax, qword ptr [rsp + 0xa0]
00836BA5  7C 0A                           jl 0x140836bb1
00836BA7  48 3B 84 24 A8 00 00 00         cmp rax, qword ptr [rsp + 0xa8]
00836BAF  7E 07                           jle 0x140836bb8
00836BB1  41 8A CC                        mov cl, r12b
00836BB4  88 4C 24 70                     mov byte ptr [rsp + 0x70], cl
00836BB8  84 C9                           test cl, cl
00836BBA  74 1C                           je 0x140836bd8
00836BBC  0F BA 6C 24 58 16               bts dword ptr [rsp + 0x58], 0x16
00836BC2  BB 05 06 00 C0                  mov ebx, 0xc0000605
00836BC7  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00836BCB  44 8D 63 FE                     lea r12d, [rbx - 2]
00836BCF  8B 7C 24 5C                     mov edi, dword ptr [rsp + 0x5c]
00836BD3  E9 53 08 00 00                  jmp 0x14083742b
00836BD8  8B 5C 24 50                     mov ebx, dword ptr [rsp + 0x50]
00836BDC  4C 8B B4 24 F8 00 00 00         mov r14, qword ptr [rsp + 0xf8]
00836BE4  4C 89 B4 24 50 01 00 00         mov qword ptr [rsp + 0x150], r14
00836BEC  8B 7C 24 5C                     mov edi, dword ptr [rsp + 0x5c]
00836BF0  41 BC 03 06 00 C0               mov r12d, 0xc0000603
00836BF6  44 39 BC 24 84 00 00 00         cmp dword ptr [rsp + 0x84], r15d
00836BFE  0F 85 27 08 00 00               jne 0x14083742b
00836C04  8B 84 24 80 00 00 00            mov eax, dword ptr [rsp + 0x80]
00836C0B  48 6B F0 78                     imul rsi, rax, 0x78
00836C0F  48 89 B4 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rsi
00836C17  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
00836C1F  48 83 C3 08                     add rbx, 8
00836C23  48 03 DE                        add rbx, rsi
00836C26  48 89 9C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rbx
00836C2E  49 8D 4E 30                     lea rcx, [r14 + 0x30]
00836C32  E8 69 F5 FF FF                  call 0x1408361a0
00836C37  44 8B F8                        mov r15d, eax
00836C3A  89 84 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], eax
00836C41  4D 8D 46 20                     lea r8, [r14 + 0x20]
00836C45  48 8D 44 24 7C                  lea rax, [rsp + 0x7c]
00836C4A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00836C4F  4C 8B CB                        mov r9, rbx
00836C52  BA 01 00 00 00                  mov edx, 1
00836C57  41 8B CF                        mov ecx, r15d
00836C5A  E8 A5 F2 E6 FF                  call 0x1406a5f04
00836C5F  8B D8                           mov ebx, eax
00836C61  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00836C65  85 C0                           test eax, eax
00836C67  79 0E                           jns 0x140836c77
00836C69  0F BA 6C 24 58 12               bts dword ptr [rsp + 0x58], 0x12
00836C6F  45 33 FF                        xor r15d, r15d
00836C72  E9 B4 07 00 00                  jmp 0x14083742b
00836C77  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
00836C7F  44 89 3C 16                     mov dword ptr [rsi + rdx], r15d
00836C83  44 8B 54 24 7C                  mov r10d, dword ptr [rsp + 0x7c]
00836C88  44 89 54 16 04                  mov dword ptr [rsi + rdx + 4], r10d
00836C8D  41 0F 10 46 10                  movups xmm0, xmmword ptr [r14 + 0x10]
00836C92  F3 0F 7F 44 16 68               movdqu xmmword ptr [rsi + rdx + 0x68], xmm0
00836C98  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
00836C9C  8D 48 03                        lea ecx, [rax + 3]
00836C9F  83 E1 FC                        and ecx, 0xfffffffc
00836CA2  3B C8                           cmp ecx, eax
00836CA4  73 0B                           jae 0x140836cb1
00836CA6  BB 95 00 00 C0                  mov ebx, 0xc0000095
00836CAB  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00836CAF  EB BE                           jmp 0x140836c6f
00836CB1  44 8D 34 39                     lea r14d, [rcx + rdi]
00836CB5  44 3B F7                        cmp r14d, edi
00836CB8  72 20                           jb 0x140836cda
00836CBA  41 8B FE                        mov edi, r14d
00836CBD  44 89 74 24 5C                  mov dword ptr [rsp + 0x5c], r14d
00836CC2  33 DB                           xor ebx, ebx
00836CC4  44 89 B4 24 B8 00 00 00         mov dword ptr [rsp + 0xb8], r14d
00836CCC  41 8B C6                        mov eax, r14d
00836CCF  41 8B F6                        mov esi, r14d
00836CD2  41 8B CE                        mov ecx, r14d
00836CD5  45 8B FE                        mov r15d, r14d
00836CD8  EB 28                           jmp 0x140836d02
00836CDA  41 83 C8 FF                     or r8d, 0xffffffff
00836CDE  41 8B F8                        mov edi, r8d
00836CE1  44 89 44 24 5C                  mov dword ptr [rsp + 0x5c], r8d
00836CE6  BB 95 00 00 C0                  mov ebx, 0xc0000095
00836CEB  45 8B F0                        mov r14d, r8d
00836CEE  44 89 84 24 B8 00 00 00         mov dword ptr [rsp + 0xb8], r8d
00836CF6  41 8B C0                        mov eax, r8d
00836CF9  41 8B F0                        mov esi, r8d
00836CFC  41 8B C8                        mov ecx, r8d
00836CFF  45 8B F8                        mov r15d, r8d
00836D02  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00836D06  85 DB                           test ebx, ebx
00836D08  0F 88 11 07 00 00               js 0x14083741f
00836D0E  48 8B 9C 24 E8 00 00 00         mov rbx, qword ptr [rsp + 0xe8]
00836D16  4C 8D 04 13                     lea r8, [rbx + rdx]
00836D1A  0F 57 C0                        xorps xmm0, xmm0
00836D1D  41 0F 11 40 48                  movups xmmword ptr [r8 + 0x48], xmm0
00836D22  48 83 C2 58                     add rdx, 0x58
00836D26  48 03 D3                        add rdx, rbx
00836D29  48 89 94 24 00 01 00 00         mov qword ptr [rsp + 0x100], rdx
00836D31  0F 57 C9                        xorps xmm1, xmm1
00836D34  0F 11 0A                        movups xmmword ptr [rdx], xmm1
00836D37  48 83 BC 24 70 01 00 00 00      cmp qword ptr [rsp + 0x170], 0
00836D40  0F 84 09 01 00 00               je 0x140836e4f
00836D46  8B F0                           mov esi, eax
00836D48  44 8B F9                        mov r15d, ecx
00836D4B  48 8B 8C 24 50 01 00 00         mov rcx, qword ptr [rsp + 0x150]
00836D53  48 81 C1 A0 00 00 00            add rcx, 0xa0
00836D5A  49 8D 50 48                     lea rdx, [r8 + 0x48]
00836D5E  E8 F9 FA FF FF                  call 0x14083685c
00836D63  84 C0                           test al, al
00836D65  74 5C                           je 0x140836dc3
00836D67  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00836D6F  0F B7 44 03 50                  movzx eax, word ptr [rbx + rax + 0x50]
00836D74  8D 48 03                        lea ecx, [rax + 3]
00836D77  83 E1 FC                        and ecx, 0xfffffffc
00836D7A  3B C8                           cmp ecx, eax
00836D7C  0F 82 24 FF FF FF               jb 0x140836ca6
00836D82  41 8D 3C 0E                     lea edi, [r14 + rcx]
00836D86  3B BC 24 B8 00 00 00            cmp edi, dword ptr [rsp + 0xb8]
00836D8D  72 0D                           jb 0x140836d9c
00836D8F  89 7C 24 5C                     mov dword ptr [rsp + 0x5c], edi
00836D93  33 DB                           xor ebx, ebx
00836D95  8B F7                           mov esi, edi
00836D97  44 8B FF                        mov r15d, edi
00836D9A  EB 13                           jmp 0x140836daf
00836D9C  83 C8 FF                        or eax, 0xffffffff
00836D9F  8B F8                           mov edi, eax
00836DA1  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
00836DA5  BB 95 00 00 C0                  mov ebx, 0xc0000095
00836DAA  8B F0                           mov esi, eax
00836DAC  44 8B F8                        mov r15d, eax
00836DAF  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00836DB3  85 DB                           test ebx, ebx
00836DB5  0F 88 B4 FE FF FF               js 0x140836c6f
00836DBB  48 8B 9C 24 E8 00 00 00         mov rbx, qword ptr [rsp + 0xe8]
00836DC3  4C 8B B4 24 50 01 00 00         mov r14, qword ptr [rsp + 0x150]
00836DCB  49 8D 4E 70                     lea rcx, [r14 + 0x70]
00836DCF  48 8B 94 24 00 01 00 00         mov rdx, qword ptr [rsp + 0x100]
00836DD7  E8 80 FA FF FF                  call 0x14083685c
00836DDC  84 C0                           test al, al
00836DDE  74 4E                           je 0x140836e2e
00836DE0  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00836DE8  0F B7 44 03 60                  movzx eax, word ptr [rbx + rax + 0x60]
00836DED  8D 48 03                        lea ecx, [rax + 3]
00836DF0  83 E1 FC                        and ecx, 0xfffffffc
00836DF3  3B C8                           cmp ecx, eax
00836DF5  0F 82 AB FE FF FF               jb 0x140836ca6
00836DFB  8D 34 39                        lea esi, [rcx + rdi]
00836DFE  3B F7                           cmp esi, edi
00836E00  72 0D                           jb 0x140836e0f
00836E02  8B FE                           mov edi, esi
00836E04  89 74 24 5C                     mov dword ptr [rsp + 0x5c], esi
00836E08  33 DB                           xor ebx, ebx
00836E0A  44 8B FE                        mov r15d, esi
00836E0D  EB 13                           jmp 0x140836e22
00836E0F  83 C8 FF                        or eax, 0xffffffff
00836E12  8B F8                           mov edi, eax
00836E14  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
00836E18  BB 95 00 00 C0                  mov ebx, 0xc0000095
00836E1D  8B F0                           mov esi, eax
00836E1F  44 8B F8                        mov r15d, eax
00836E22  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00836E26  85 DB                           test ebx, ebx
00836E28  0F 88 41 FE FF FF               js 0x140836c6f
00836E2E  44 8B 54 24 7C                  mov r10d, dword ptr [rsp + 0x7c]
00836E33  B8 01 00 00 00                  mov eax, 1
00836E38  01 84 24 80 00 00 00            add dword ptr [rsp + 0x80], eax
00836E3F  8D 7E 78                        lea edi, [rsi + 0x78]
00836E42  41 3B FF                        cmp edi, r15d
00836E45  72 12                           jb 0x140836e59
00836E47  45 33 FF                        xor r15d, r15d
00836E4A  41 8B DF                        mov ebx, r15d
00836E4D  EB 15                           jmp 0x140836e64
00836E4F  4C 8B B4 24 50 01 00 00         mov r14, qword ptr [rsp + 0x150]
00836E57  EB DA                           jmp 0x140836e33
00836E59  83 CF FF                        or edi, 0xffffffff
00836E5C  BB 95 00 00 C0                  mov ebx, 0xc0000095
00836E61  45 33 FF                        xor r15d, r15d
00836E64  89 7C 24 5C                     mov dword ptr [rsp + 0x5c], edi
00836E68  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00836E6C  85 DB                           test ebx, ebx
00836E6E  0F 88 B7 05 00 00               js 0x14083742b
00836E74  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
00836E79  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00836E7E  4C 8D 8C 24 D8 00 00 00         lea r9, [rsp + 0xd8]
00836E86  45 8B C2                        mov r8d, r10d
00836E89  48 8B 94 24 E0 00 00 00         mov rdx, qword ptr [rsp + 0xe0]
00836E91  8B 8C 24 8C 00 00 00            mov ecx, dword ptr [rsp + 0x8c]
00836E98  E8 87 F0 E6 FF                  call 0x1406a5f24
00836E9D  B9 01 00 00 00                  mov ecx, 1
00836EA2  84 C0                           test al, al
00836EA4  74 33                           je 0x140836ed9
00836EA6  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00836EAB  89 8C 24 88 00 00 00            mov dword ptr [rsp + 0x88], ecx
00836EB2  0F BA 6C 24 58 15               bts dword ptr [rsp + 0x58], 0x15
00836EB8  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
00836EC0  48 39 84 24 D8 00 00 00         cmp qword ptr [rsp + 0xd8], rax
00836EC8  48 0F 4C 84 24 D8 00 00 00      cmovl rax, qword ptr [rsp + 0xd8]
00836ED1  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
00836ED9  44 89 7C 24 50                  mov dword ptr [rsp + 0x50], r15d
00836EDE  4D 85 ED                        test r13, r13
00836EE1  74 6A                           je 0x140836f4d
00836EE3  41 8B 45 04                     mov eax, dword ptr [r13 + 4]
00836EE7  84 C1                           test cl, al
00836EE9  74 62                           je 0x140836f4d
00836EEB  C7 84 24 BC 00 00 00 32 00 00 00  mov dword ptr [rsp + 0xbc], 0x32
00836EF6  49 8D 8E E0 00 00 00            lea rcx, [r14 + 0xe0]
00836EFD  48 8B B4 24 F0 00 00 00         mov rsi, qword ptr [rsp + 0xf0]
00836F05  4C 8B C6                        mov r8, rsi
00836F08  48 8D 94 24 BC 00 00 00         lea rdx, [rsp + 0xbc]
00836F10  E8 BB F8 FF FF                  call 0x1408367d0
00836F15  8B D8                           mov ebx, eax
00836F17  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00836F1B  85 C0                           test eax, eax
00836F1D  0F 88 08 05 00 00               js 0x14083742b
00836F23  4D 8B C5                        mov r8, r13
00836F26  48 8B D6                        mov rdx, rsi
00836F29  8B 8C 24 BC 00 00 00            mov ecx, dword ptr [rsp + 0xbc]
00836F30  E8 E3 22 00 00                  call 0x140839218
00836F35  84 C0                           test al, al
00836F37  75 14                           jne 0x140836f4d
00836F39  0F BA 6C 24 58 13               bts dword ptr [rsp + 0x58], 0x13
00836F3F  BB 28 04 00 C0                  mov ebx, 0xc0000428
00836F44  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00836F48  E9 DE 04 00 00                  jmp 0x14083742b
00836F4D  4D 8D 7E 70                     lea r15, [r14 + 0x70]
00836F51  41 8B 07                        mov eax, dword ptr [r15]
00836F54  41 3B 86 A0 00 00 00            cmp eax, dword ptr [r14 + 0xa0]
00836F5B  75 2D                           jne 0x140836f8a
00836F5D  44 8B C0                        mov r8d, eax
00836F60  49 8B 96 A8 00 00 00            mov rdx, qword ptr [r14 + 0xa8]
00836F67  49 8B 4E 78                     mov rcx, qword ptr [r14 + 0x78]
00836F6B  E8 A0 FB E8 FF                  call 0x1406c6b10
00836F70  33 C9                           xor ecx, ecx
00836F72  85 C0                           test eax, eax
00836F74  0F 94 C1                        sete cl
00836F77  0F B6 44 24 60                  movzx eax, byte ptr [rsp + 0x60]
00836F7C  85 C9                           test ecx, ecx
00836F7E  B9 01 00 00 00                  mov ecx, 1
00836F83  0F 45 C1                        cmovne eax, ecx
00836F86  88 44 24 60                     mov byte ptr [rsp + 0x60], al
00836F8A  49 8D 8E E0 00 00 00            lea rcx, [r14 + 0xe0]
00836F91  4C 8D 4C 24 58                  lea r9, [rsp + 0x58]
00836F96  40 8A 74 24 60                  mov sil, byte ptr [rsp + 0x60]
00836F9B  44 8A C6                        mov r8b, sil
00836F9E  8B 94 24 90 00 00 00            mov edx, dword ptr [rsp + 0x90]
00836FA5  E8 DA 0B 00 00                  call 0x140837b84
00836FAA  8B D8                           mov ebx, eax
00836FAC  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00836FB0  85 C0                           test eax, eax
00836FB2  0F 88 5E 04 00 00               js 0x140837416
00836FB8  40 84 F6                        test sil, sil
00836FBB  0F 84 C6 01 00 00               je 0x140837187
00836FC1  49 8D B6 B0 00 00 00            lea rsi, [r14 + 0xb0]
00836FC8  48 8B CE                        mov rcx, rsi
00836FCB  E8 50 F6 FF FF                  call 0x140836620
00836FD0  48 8B C8                        mov rcx, rax
00836FD3  45 33 FF                        xor r15d, r15d
00836FD6  48 85 C0                        test rax, rax
00836FD9  0F 85 B6 00 00 00               jne 0x140837095
00836FDF  4C 39 BC 24 70 01 00 00         cmp qword ptr [rsp + 0x170], r15
00836FE7  0F 84 52 FF FF FF               je 0x140836f3f
00836FED  8B 5C 24 58                     mov ebx, dword ptr [rsp + 0x58]
00836FF1  44 8D 48 01                     lea r9d, [rax + 1]
00836FF5  41 0B D9                        or ebx, r9d
00836FF8  89 5C 24 58                     mov dword ptr [rsp + 0x58], ebx
00836FFC  C7 44 24 74 02 00 00 00         mov dword ptr [rsp + 0x74], 2
00837004  4D 85 ED                        test r13, r13
00837007  74 3F                           je 0x140837048
00837009  41 8B 45 04                     mov eax, dword ptr [r13 + 4]
0083700D  A8 20                           test al, 0x20
0083700F  74 37                           je 0x140837048
00837011  45 8B 45 70                     mov r8d, dword ptr [r13 + 0x70]
00837015  49 8B 55 78                     mov rdx, qword ptr [r13 + 0x78]
00837019  49 8D 4E 10                     lea rcx, [r14 + 0x10]
0083701D  E8 FA F2 E6 FF                  call 0x1406a631c
00837022  85 C0                           test eax, eax
00837024  75 14                           jne 0x14083703a
00837026  45 8B 45 60                     mov r8d, dword ptr [r13 + 0x60]
0083702A  49 8B 55 68                     mov rdx, qword ptr [r13 + 0x68]
0083702E  48 8B CE                        mov rcx, rsi
00837031  E8 56 F3 E6 FF                  call 0x1406a638c
00837036  85 C0                           test eax, eax
00837038  74 08                           je 0x140837042
0083703A  0F BA EB 0E                     bts ebx, 0xe
0083703E  89 5C 24 58                     mov dword ptr [rsp + 0x58], ebx
00837042  41 B9 01 00 00 00               mov r9d, 1
00837048  4C 39 BC 24 70 01 00 00         cmp qword ptr [rsp + 0x170], r15
00837050  0F 84 B4 00 00 00               je 0x14083710a
00837056  8B 54 24 54                     mov edx, dword ptr [rsp + 0x54]
0083705A  8B CA                           mov ecx, edx
0083705C  48 03 C9                        add rcx, rcx
0083705F  0F 10 06                        movups xmm0, xmmword ptr [rsi]
00837062  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
0083706A  F3 0F 7F 04 C8                  movdqu xmmword ptr [rax + rcx*8], xmm0
0083706F  41 03 D1                        add edx, r9d
00837072  89 54 24 54                     mov dword ptr [rsp + 0x54], edx
00837076  8B 06                           mov eax, dword ptr [rsi]
00837078  8D 48 03                        lea ecx, [rax + 3]
0083707B  83 E1 FC                        and ecx, 0xfffffffc
0083707E  3B C8                           cmp ecx, eax
00837080  73 30                           jae 0x1408370b2
00837082  BB 95 00 00 C0                  mov ebx, 0xc0000095
00837087  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
0083708B  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00837090  E9 9F 03 00 00                  jmp 0x140837434
00837095  48 8D 70 10                     lea rsi, [rax + 0x10]
00837099  8B 40 20                        mov eax, dword ptr [rax + 0x20]
0083709C  41 B9 01 00 00 00               mov r9d, 1
008370A2  41 0B C1                        or eax, r9d
008370A5  09 44 24 58                     or dword ptr [rsp + 0x58], eax
008370A9  8B 41 24                        mov eax, dword ptr [rcx + 0x24]
008370AC  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
008370B0  EB 96                           jmp 0x140837048
008370B2  8D 04 39                        lea eax, [rcx + rdi]
008370B5  41 83 C8 FF                     or r8d, 0xffffffff
008370B9  3B C7                           cmp eax, edi
008370BB  72 0D                           jb 0x1408370ca
008370BD  8B F8                           mov edi, eax
008370BF  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
008370C3  41 8B DF                        mov ebx, r15d
008370C6  8B C8                           mov ecx, eax
008370C8  EB 13                           jmp 0x1408370dd
008370CA  41 8B F8                        mov edi, r8d
008370CD  44 89 44 24 5C                  mov dword ptr [rsp + 0x5c], r8d
008370D2  BB 95 00 00 C0                  mov ebx, 0xc0000095
008370D7  41 8B C0                        mov eax, r8d
008370DA  41 8B C8                        mov ecx, r8d
008370DD  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
008370E1  85 DB                           test ebx, ebx
008370E3  78 A6                           js 0x14083708b
008370E5  8D 78 10                        lea edi, [rax + 0x10]
008370E8  3B F9                           cmp edi, ecx
008370EA  72 09                           jb 0x1408370f5
008370EC  89 7C 24 5C                     mov dword ptr [rsp + 0x5c], edi
008370F0  41 8B DF                        mov ebx, r15d
008370F3  EB 0D                           jmp 0x140837102
008370F5  41 8B F8                        mov edi, r8d
008370F8  44 89 44 24 5C                  mov dword ptr [rsp + 0x5c], r8d
008370FD  BB 95 00 00 C0                  mov ebx, 0xc0000095
00837102  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00837106  85 DB                           test ebx, ebx
00837108  78 81                           js 0x14083708b
0083710A  44 89 8C 24 84 00 00 00         mov dword ptr [rsp + 0x84], r9d
00837112  4C 8B BC 24 C0 00 00 00         mov r15, qword ptr [rsp + 0xc0]
0083711A  4D 8D 4E 40                     lea r9, [r14 + 0x40]
0083711E  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
00837123  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00837128  44 8B 44 24 7C                  mov r8d, dword ptr [rsp + 0x7c]
0083712D  48 8B 94 24 E0 00 00 00         mov rdx, qword ptr [rsp + 0xe0]
00837135  8B 8C 24 8C 00 00 00            mov ecx, dword ptr [rsp + 0x8c]
0083713C  E8 5F F1 FF FF                  call 0x1408362a0
00837141  8B D8                           mov ebx, eax
00837143  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00837147  85 C0                           test eax, eax
00837149  0F 88 1A FB FF FF               js 0x140836c69
0083714F  83 BC 24 84 00 00 00 00         cmp dword ptr [rsp + 0x84], 0
00837157  0F 85 B1 02 00 00               jne 0x14083740e
0083715D  8B 84 24 90 00 00 00            mov eax, dword ptr [rsp + 0x90]
00837164  B9 01 00 00 00                  mov ecx, 1
00837169  03 C1                           add eax, ecx
0083716B  89 84 24 90 00 00 00            mov dword ptr [rsp + 0x90], eax
00837172  83 F8 0A                        cmp eax, 0xa
00837175  0F 82 80 02 00 00               jb 0x1408373fb
0083717B  89 4C 24 74                     mov dword ptr [rsp + 0x74], ecx
0083717F  45 33 FF                        xor r15d, r15d
00837182  E9 46 02 00 00                  jmp 0x1408373cd
00837187  BE 01 00 00 00                  mov esi, 1
0083718C  48 83 BC 24 70 01 00 00 00      cmp qword ptr [rsp + 0x170], 0
00837195  0F 84 A5 00 00 00               je 0x140837240
0083719B  8B 54 24 54                     mov edx, dword ptr [rsp + 0x54]
0083719F  8B CA                           mov ecx, edx
008371A1  48 03 C9                        add rcx, rcx
008371A4  41 0F 10 86 B0 00 00 00         movups xmm0, xmmword ptr [r14 + 0xb0]
008371AC  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
008371B4  F3 0F 7F 04 C8                  movdqu xmmword ptr [rax + rcx*8], xmm0
008371B9  03 D6                           add edx, esi
008371BB  89 54 24 54                     mov dword ptr [rsp + 0x54], edx
008371BF  41 8B 86 B0 00 00 00            mov eax, dword ptr [r14 + 0xb0]
008371C6  8D 48 03                        lea ecx, [rax + 3]
008371C9  83 E1 FC                        and ecx, 0xfffffffc
008371CC  3B C8                           cmp ecx, eax
008371CE  73 16                           jae 0x1408371e6
008371D0  BB 95 00 00 C0                  mov ebx, 0xc0000095
008371D5  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
008371D9  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
008371DE  45 33 FF                        xor r15d, r15d
008371E1  E9 4E 02 00 00                  jmp 0x140837434
008371E6  8D 04 39                        lea eax, [rcx + rdi]
008371E9  3B C7                           cmp eax, edi
008371EB  72 10                           jb 0x1408371fd
008371ED  8B F8                           mov edi, eax
008371EF  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
008371F3  33 DB                           xor ebx, ebx
008371F5  8B C8                           mov ecx, eax
008371F7  41 83 C8 FF                     or r8d, 0xffffffff
008371FB  EB 17                           jmp 0x140837214
008371FD  41 83 C8 FF                     or r8d, 0xffffffff
00837201  41 8B F8                        mov edi, r8d
00837204  44 89 44 24 5C                  mov dword ptr [rsp + 0x5c], r8d
00837209  BB 95 00 00 C0                  mov ebx, 0xc0000095
0083720E  41 8B C0                        mov eax, r8d
00837211  41 8B C8                        mov ecx, r8d
00837214  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00837218  85 DB                           test ebx, ebx
0083721A  78 BD                           js 0x1408371d9
0083721C  8D 78 10                        lea edi, [rax + 0x10]
0083721F  3B F9                           cmp edi, ecx
00837221  72 08                           jb 0x14083722b
00837223  89 7C 24 5C                     mov dword ptr [rsp + 0x5c], edi
00837227  33 DB                           xor ebx, ebx
00837229  EB 0D                           jmp 0x140837238
0083722B  41 8B F8                        mov edi, r8d
0083722E  44 89 44 24 5C                  mov dword ptr [rsp + 0x5c], r8d
00837233  BB 95 00 00 C0                  mov ebx, 0xc0000095
00837238  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
0083723C  85 DB                           test ebx, ebx
0083723E  78 99                           js 0x1408371d9
00837240  49 8B D5                        mov rdx, r13
00837243  49 8B CF                        mov rcx, r15
00837246  E8 49 F4 FF FF                  call 0x140836694
0083724B  48 8B C8                        mov rcx, rax
0083724E  48 85 C0                        test rax, rax
00837251  0F 84 C6 00 00 00               je 0x14083731d
00837257  48 8D 70 10                     lea rsi, [rax + 0x10]
0083725B  8B 40 20                        mov eax, dword ptr [rax + 0x20]
0083725E  09 44 24 58                     or dword ptr [rsp + 0x58], eax
00837262  8B 41 24                        mov eax, dword ptr [rcx + 0x24]
00837265  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
00837269  41 B8 01 00 00 00               mov r8d, 1
0083726F  44 89 84 24 84 00 00 00         mov dword ptr [rsp + 0x84], r8d
00837277  45 33 FF                        xor r15d, r15d
0083727A  4C 39 BC 24 70 01 00 00         cmp qword ptr [rsp + 0x170], r15
00837282  0F 84 8A FE FF FF               je 0x140837112
00837288  8B 54 24 54                     mov edx, dword ptr [rsp + 0x54]
0083728C  8B CA                           mov ecx, edx
0083728E  48 03 C9                        add rcx, rcx
00837291  0F 10 06                        movups xmm0, xmmword ptr [rsi]
00837294  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
0083729C  F3 0F 7F 04 C8                  movdqu xmmword ptr [rax + rcx*8], xmm0
008372A1  41 03 D0                        add edx, r8d
008372A4  89 54 24 54                     mov dword ptr [rsp + 0x54], edx
008372A8  8B 06                           mov eax, dword ptr [rsi]
008372AA  8D 48 03                        lea ecx, [rax + 3]
008372AD  83 E1 FC                        and ecx, 0xfffffffc
008372B0  3B C8                           cmp ecx, eax
008372B2  0F 82 CA FD FF FF               jb 0x140837082
008372B8  8D 04 39                        lea eax, [rcx + rdi]
008372BB  41 83 C8 FF                     or r8d, 0xffffffff
008372BF  3B C7                           cmp eax, edi
008372C1  72 0D                           jb 0x1408372d0
008372C3  8B F8                           mov edi, eax
008372C5  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
008372C9  41 8B DF                        mov ebx, r15d
008372CC  8B C8                           mov ecx, eax
008372CE  EB 13                           jmp 0x1408372e3
008372D0  41 8B F8                        mov edi, r8d
008372D3  44 89 44 24 5C                  mov dword ptr [rsp + 0x5c], r8d
008372D8  BB 95 00 00 C0                  mov ebx, 0xc0000095
008372DD  41 8B C0                        mov eax, r8d
008372E0  41 8B C8                        mov ecx, r8d
008372E3  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
008372E7  85 DB                           test ebx, ebx
008372E9  0F 88 9C FD FF FF               js 0x14083708b
008372EF  8D 78 10                        lea edi, [rax + 0x10]
008372F2  3B F9                           cmp edi, ecx
008372F4  72 09                           jb 0x1408372ff
008372F6  89 7C 24 5C                     mov dword ptr [rsp + 0x5c], edi
008372FA  41 8B DF                        mov ebx, r15d
008372FD  EB 0D                           jmp 0x14083730c
008372FF  41 8B F8                        mov edi, r8d
00837302  44 89 44 24 5C                  mov dword ptr [rsp + 0x5c], r8d
00837307  BB 95 00 00 C0                  mov ebx, 0xc0000095
0083730C  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00837310  85 DB                           test ebx, ebx
00837312  0F 88 73 FD FF FF               js 0x14083708b
00837318  E9 F5 FD FF FF                  jmp 0x140837112
0083731D  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
00837325  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0083732A  4D 8B CD                        mov r9, r13
0083732D  4C 8B 84 24 60 01 00 00         mov r8, qword ptr [rsp + 0x160]
00837335  8B 94 24 58 01 00 00            mov edx, dword ptr [rsp + 0x158]
0083733C  49 8B CF                        mov rcx, r15
0083733F  E8 EC F1 FF FF                  call 0x140836530
00837344  4C 8B F8                        mov r15, rax
00837347  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
0083734F  48 85 C0                        test rax, rax
00837352  74 1C                           je 0x140837370
00837354  48 8D 48 30                     lea rcx, [rax + 0x30]
00837358  E8 43 EE FF FF                  call 0x1408361a0
0083735D  F7 D8                           neg eax
0083735F  48 1B C9                        sbb rcx, rcx
00837362  49 23 CF                        and rcx, r15
00837365  4C 8B F9                        mov r15, rcx
00837368  48 89 8C 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rcx
00837370  4D 85 FF                        test r15, r15
00837373  75 7A                           jne 0x1408373ef
00837375  4D 85 ED                        test r13, r13
00837378  74 4F                           je 0x1408373c9
0083737A  41 8B 45 04                     mov eax, dword ptr [r13 + 4]
0083737E  A8 20                           test al, 0x20
00837380  74 47                           je 0x1408373c9
00837382  41 8B 45 60                     mov eax, dword ptr [r13 + 0x60]
00837386  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0083738A  41 8B 45 70                     mov eax, dword ptr [r13 + 0x70]
0083738E  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00837392  49 8B 45 78                     mov rax, qword ptr [r13 + 0x78]
00837396  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0083739B  4D 8B CE                        mov r9, r14
0083739E  44 8B 44 24 7C                  mov r8d, dword ptr [rsp + 0x7c]
008373A3  48 8B 94 24 E0 00 00 00         mov rdx, qword ptr [rsp + 0xe0]
008373AB  8B 8C 24 8C 00 00 00            mov ecx, dword ptr [rsp + 0x8c]
008373B2  E8 41 EE E6 FF                  call 0x1406a61f8
008373B7  8B D8                           mov ebx, eax
008373B9  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008373BD  85 C0                           test eax, eax
008373BF  78 08                           js 0x1408373c9
008373C1  0F BA 6C 24 58 0E               bts dword ptr [rsp + 0x58], 0xe
008373C7  EB 62                           jmp 0x14083742b
008373C9  89 74 24 74                     mov dword ptr [rsp + 0x74], esi
008373CD  4C 39 BC 24 70 01 00 00         cmp qword ptr [rsp + 0x170], r15
008373D5  74 0D                           je 0x1408373e4
008373D7  83 4C 24 58 10                  or dword ptr [rsp + 0x58], 0x10
008373DC  41 8B DF                        mov ebx, r15d
008373DF  E9 60 FB FF FF                  jmp 0x140836f44
008373E4  0F BA 6C 24 58 11               bts dword ptr [rsp + 0x58], 0x11
008373EA  E9 50 FB FF FF                  jmp 0x140836f3f
008373EF  49 8D B7 B0 00 00 00            lea rsi, [r15 + 0xb0]
008373F6  E9 1F FD FF FF                  jmp 0x14083711a
008373FB  4D 8B F7                        mov r14, r15
008373FE  4C 89 BC 24 50 01 00 00         mov qword ptr [rsp + 0x150], r15
00837406  4C 89 BC 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], r15
0083740E  45 33 FF                        xor r15d, r15d
00837411  E9 E0 F7 FF FF                  jmp 0x140836bf6
00837416  8B 54 24 54                     mov edx, dword ptr [rsp + 0x54]
0083741A  E9 BA FD FF FF                  jmp 0x1408371d9
0083741F  8B 54 24 54                     mov edx, dword ptr [rsp + 0x54]
00837423  45 33 FF                        xor r15d, r15d
00837426  E9 60 FC FF FF                  jmp 0x14083708b
0083742B  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00837430  8B 54 24 54                     mov edx, dword ptr [rsp + 0x54]
00837434  48 8B 8C 24 70 01 00 00         mov rcx, qword ptr [rsp + 0x170]
0083743C  48 85 C9                        test rcx, rcx
0083743F  0F 84 96 00 00 00               je 0x1408374db
00837445  C7 01 30 00 00 00               mov dword ptr [rcx], 0x30
0083744B  89 59 04                        mov dword ptr [rcx + 4], ebx
0083744E  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
00837452  89 41 08                        mov dword ptr [rcx + 8], eax
00837455  4C 89 79 10                     mov qword ptr [rcx + 0x10], r15
00837459  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
00837461  48 89 41 20                     mov qword ptr [rcx + 0x20], rax
00837465  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
0083746D  48 89 41 28                     mov qword ptr [rcx + 0x28], rax
00837471  44 39 BC 24 88 00 00 00         cmp dword ptr [rsp + 0x88], r15d
00837479  74 0C                           je 0x140837487
0083747B  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
00837483  48 89 41 18                     mov qword ptr [rcx + 0x18], rax
00837487  85 DB                           test ebx, ebx
00837489  78 50                           js 0x1408374db
0083748B  48 8B 84 24 78 01 00 00         mov rax, qword ptr [rsp + 0x178]
00837493  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00837498  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
008374A0  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008374A5  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
008374AD  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008374B2  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
008374B7  8B 44 24 74                     mov eax, dword ptr [rsp + 0x74]
008374BB  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
008374BF  8B 84 24 80 00 00 00            mov eax, dword ptr [rsp + 0x80]
008374C6  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008374CA  44 8B CA                        mov r9d, edx
008374CD  44 8B 44 24 78                  mov r8d, dword ptr [rsp + 0x78]
008374D2  8B D7                           mov edx, edi
008374D4  E8 3B 1E 00 00                  call 0x140839314
008374D9  8B D8                           mov ebx, eax
008374DB  48 85 F6                        test rsi, rsi
008374DE  74 0D                           je 0x1408374ed
008374E0  BA 43 49 63 72                  mov edx, 0x72634943
008374E5  48 8B CE                        mov rcx, rsi
008374E8  E8 83 B3 34 00                  call 0x140b82870
008374ED  85 DB                           test ebx, ebx
008374EF  78 0C                           js 0x1408374fd
008374F1  44 39 BC 24 88 00 00 00         cmp dword ptr [rsp + 0x88], r15d
008374F9  41 0F 45 DC                     cmovne ebx, r12d
008374FD  8B C3                           mov eax, ebx
008374FF  48 81 C4 10 01 00 00            add rsp, 0x110
00837506  41 5F                           pop r15
00837508  41 5E                           pop r14
0083750A  41 5D                           pop r13
0083750C  41 5C                           pop r12
0083750E  5F                              pop rdi
0083750F  5E                              pop rsi
00837510  5B                              pop rbx
00837511  C3                              ret
00837512  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MinCryptVerifyCertificateWithPolicy2(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned int v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned int v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned int v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned __int8 v_stack_mD7;
    unsigned __int8 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int8 v_stack_mE8;
    unsigned int v_stack_mEC;
    unsigned int v_stack_mF0;
    unsigned int v_stack_mF4;
    unsigned int v_stack_mF8;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 24) = a3;
    v_stack_p10 = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (272);
    v_r15 = 0;
    v_stack_mF8 = 0;
    *(unsigned int *)(v_rsp - 184) = 0;
    v_stack_mD0 = 50;
    *(unsigned int *)(v_rsp - 196) = 0;
    v_stack_mCC = 0;
    v_stack_mF0 = 0;
    v_stack_mF4 = 0;
    v_stack_mEC = 0;
    *(unsigned int *)(v_rsp - 200) = 0;
    *(unsigned __int64 *)(v_rsp - 136) = 0;
    *(unsigned int *)(v_rsp - 192) = 0;
    *(unsigned __int64 *)(v_rsp - 112) = 0;
    v_stack_mD4 = 0;
    *(unsigned __int64 *)(v_rsp - 176) = 0;
    v_stack_mE0 = 0;
    *(unsigned __int64 *)(v_rsp - 152) = 0;
    *(unsigned __int64 *)(v_rsp - 168) = 0;
    *(unsigned __int64 *)(v_rsp - 160) = 0;
    v_stack_mE8 = 0;
    *(unsigned __int64 *)(v_rsp - 128) = result;
    *(unsigned __int64 *)(v_rsp - 80) = a1;
    result = ExAllocatePool2(258, (unsigned int)(0xBA0ULL), (unsigned int)(0x72634943ULL), a4);
    v_stack_mE0 = result;
    if (result != 0) goto loc_00836990;
loc_00836981:
    v_stack_mF8 = (unsigned int)((unsigned int)(0xC0000017ULL));
loc_00836985:
    goto loc_00837430;
loc_00836990:
    result = (result) + (800);
    v_stack_m98 = result;
    v_stack_m58 = result + 176;
    v_stack_mB0 = result + 176 + 800;
    result = I_MinCryptGetCertificateEKUs(a1 + 224, v_stack_mD0, v_stack_mE0, a4);
    v_stack_mF8 = (unsigned int)(result);
    if (sign_flag) goto loc_00836985;
    a3 = (unsigned int)((v_stack_mE0) | (0xFFFFFFFFULL));
loc_008369F8:
    v_stack_m78 = 0;
    if (0 >= v_stack_mD0) goto loc_00836A7E;
    result = (0) + (0);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mE0 + result * 8)) + 3) & ((unsigned int)((unsigned int)(0xFFFFFFFCULL))));
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mE0 + result * 8))))) goto loc_00836A1F;
loc_00836A17:
    goto loc_00836981;
loc_00836A1F:
    result = (unsigned int)((result) + (0));
    if (((unsigned int)(result)) < 0) goto loc_00836A32;
    v_stack_mEC = (unsigned int)(result);
    goto loc_00836A43;
loc_00836A32:
    v_stack_mEC = (unsigned int)(a3);
loc_00836A43:
    v_stack_mF8 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))));
    if (sign_flag) goto loc_00836985;
    if (((unsigned int)((unsigned int)((unsigned int)(a3)) + 16)) < ((unsigned int)((unsigned int)((unsigned int)(a3))))) goto loc_00836A5F;
    v_stack_mEC = (unsigned int)((unsigned int)((unsigned int)(a3)) + 16);
    goto loc_00836A6A;
loc_00836A5F:
    v_stack_mEC = (unsigned int)(a3);
loc_00836A6A:
    v_stack_mF8 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))));
    if (sign_flag) goto loc_00836985;
    a2 = (unsigned int)((0) + (1));
    goto loc_008369F8;
loc_00836A7E:
    if (a6 == 0) goto loc_00836AC0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a6)) + 3) & ((unsigned int)((unsigned int)(0xFFFFFFFCULL))));
    if (((unsigned int)(a1)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a6))))) goto loc_00836A17;
    if (((unsigned int)(a1 + (unsigned int)((unsigned int)(a3)) * 1)) < ((unsigned int)((unsigned int)((unsigned int)(a3))))) goto loc_00836AA9;
    v_stack_mEC = (unsigned int)(a1 + (unsigned int)((unsigned int)(a3)) * 1);
    goto loc_00836AB4;
loc_00836AA9:
    v_stack_mEC = (unsigned int)(a3);
loc_00836AB4:
    v_stack_mF8 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))));
    if (sign_flag) goto loc_00836985;
loc_00836AC0:
    if (a4 == 0) goto loc_00836AF1;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a4 + 4))))) != 0) goto loc_00836AF1;
    result = I_MinCryptCheckEKURequirements((unsigned int)(v_stack_mD0), v_stack_mE0, a4, (unsigned int)(0xC0000095ULL));
    if ((unsigned __int8)(result) != 0) goto loc_00836AF1;
    goto loc_00836981;
loc_00836AF1:
    result = I_MinCryptGetCertValidityPeriod(v_stack_p8, v_stack_mA8, v_stack_mA0, (unsigned int)(0xC0000095ULL));
    result = I_MinCryptCheckEKU(v_rip + 3232105, (unsigned int)(v_stack_mD0), v_stack_mE0, (unsigned int)(0xC0000095ULL));
    v_stack_mD7 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) goto loc_00836B5E;
    if (condition_is_less_or_equal) goto loc_00836B5E;
    a1 = 0;
    if (v_stack_mA8 < (*(unsigned __int64 *)(v_rip + 8001365))) { a1 = 1; }
    if ((unsigned __int8)(a1) == 0) goto loc_00836B5E;
    goto loc_00836981;
loc_00836B5E:
    if ((*(unsigned __int8 *)(v_rip + 6140259)) != 0) goto loc_00836BF0;
    result = I_MinCryptCheckEKU(v_rip + 3231999, (unsigned int)(v_stack_mD0), v_stack_mE0, (unsigned int)(0xC0000095ULL));
    if ((unsigned __int8)(result) == 0) goto loc_00836BF0;
    v_stack_mD8 = 0;
    if (v_stack_mD7 != 0) goto loc_00836BA7;
    if ((*(unsigned __int64 *)(result)) < v_stack_mA8) goto loc_00836BB1;
loc_00836BA7:
    if ((*(unsigned __int64 *)(result)) >= = v_stack_mA0) {
        a1 = 1;
        v_stack_mD8 = (unsigned __int8)(a1);
    }
    if ((unsigned __int8)(a1) == 0) goto loc_00836BD8;
    v_stack_mF8 = (unsigned int)((unsigned int)(0xC0000605ULL));
    goto loc_0083742B;
loc_00836BD8:
    v_stack_p8 = v_stack_m50;
loc_00836BF0:
loc_00836BF6:
    if (v_stack_mC4 != 0) goto loc_0083742B;
    v_rsi = (v_stack_mE0) * ((unsigned int)(v_stack_mC8));
    v_stack_m60 = v_rsi;
    v_rbx = (v_stack_mB0) + (8);
    v_rbx = (v_rbx) + (v_rsi);
    v_stack_m68 = v_rbx;
    result = MinCryptDecodeHashAlgorithmIdentifier(v_stack_m50 + 48, (unsigned int)(v_stack_mD0), v_stack_mE0, (unsigned int)(0xC0000095ULL));
    v_stack_mBC = (unsigned int)(result);
    v_stack_m128 = v_stack_mCC;
    result = MinCryptHashMemory((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), 1, v_stack_m50 + 32, v_rbx);
    v_stack_mF8 = (unsigned int)(result);
    if (!sign_flag) goto loc_00836C77;
loc_00836C69:
loc_00836C6F:
    v_r15 = 0;
    goto loc_0083742B;
loc_00836C77:
    *(unsigned int *)(v_rsi + v_stack_mB0 * 1) = 0;
    *(unsigned int *)(v_rsi + v_stack_mB0 * 1 + 4) = (unsigned int)((unsigned int)(v_stack_mCC));
    *(unsigned __int64 *)(v_rsi + v_stack_mB0 * 1 + 104) = v_xmm0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m50 + 16)) + 3) & (0xFFFFFFFCULL));
    if (((unsigned int)(a1)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m50 + 16))))) goto loc_00836CB1;
loc_00836CA6:
    v_stack_mF8 = (unsigned int)((unsigned int)(0xC0000095ULL));
    goto loc_00836C6F;
loc_00836CB1:
    if (((unsigned int)(a1 + (unsigned int)(v_stack_mEC) * 1)) < ((unsigned int)((unsigned int)(v_stack_mEC)))) goto loc_00836CDA;
    v_stack_mEC = (unsigned int)(a1 + (unsigned int)(v_stack_mEC) * 1);
    v_rbx = 0;
    v_stack_m90 = (unsigned int)(a1 + (unsigned int)(v_stack_mEC) * 1);
    goto loc_00836D02;
loc_00836CDA:
    a3 = (unsigned int)((v_stack_m50 + 32) | (0xFFFFFFFFULL));
    v_stack_mEC = (unsigned int)(a3);
    v_stack_m90 = (unsigned int)(a3);
loc_00836D02:
    v_stack_mF8 = (unsigned int)((unsigned int)(0xC0000095ULL));
    if (sign_flag) goto loc_0083741F;
    *(unsigned __int64 *)(v_stack_m60 + v_stack_mB0 * 1 + 72) = v_xmm0;
    a2 = (v_stack_mB0) + (88);
    a2 = (a2) + (v_stack_m60);
    v_stack_m48 = a2;
    *(unsigned __int64 *)(a2) = v_xmm1;
    if (a5 == 0) goto loc_00836E4F;
    a1 = (v_stack_p8) + (160);
    result = I_MinCryptGetCommonName(a1, v_stack_m60 + v_stack_mB0 * 1 + 72, v_stack_m60 + v_stack_mB0 * 1, v_rbx);
    if ((unsigned __int8)(result) == 0) goto loc_00836DC3;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_m60 + v_stack_mB0 * 1 + 80) + 3) & (0xFFFFFFFCULL));
    if (((unsigned int)(a1)) < ((unsigned int)(*(unsigned __int16 *)(v_stack_m60 + v_stack_mB0 * 1 + 80)))) goto loc_00836CA6;
    if (((unsigned int)((unsigned int)((unsigned int)(a3)) + a1 * 1)) < v_stack_m90) goto loc_00836D9C;
    v_stack_mEC = (unsigned int)((unsigned int)((unsigned int)(a3)) + a1 * 1);
    v_rbx = 0;
    goto loc_00836DAF;
loc_00836D9C:
    result = (unsigned int)((*(unsigned __int16 *)(v_stack_m60 + v_stack_mB0 * 1 + 80)) | (0xFFFFFFFFULL));
    v_stack_mEC = (unsigned int)(result);
loc_00836DAF:
    v_stack_mF8 = (unsigned int)((unsigned int)(0xC0000095ULL));
    if (sign_flag) goto loc_00836C6F;
loc_00836DC3:
    result = I_MinCryptGetCommonName(v_stack_p8 + 112, v_stack_m48, v_stack_m60 + v_stack_mB0 * 1, v_rbx);
    if ((unsigned __int8)(result) == 0) goto loc_00836E2E;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_m60 + v_stack_mB0 * 1 + 96) + 3) & (0xFFFFFFFCULL));
    if (((unsigned int)(a1)) < ((unsigned int)(*(unsigned __int16 *)(v_stack_m60 + v_stack_mB0 * 1 + 96)))) goto loc_00836CA6;
    if (((unsigned int)(a1 + (unsigned int)((unsigned int)(result)) * 1)) < ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_00836E0F;
    v_stack_mEC = (unsigned int)(a1 + (unsigned int)((unsigned int)(result)) * 1);
    v_rbx = 0;
    goto loc_00836E22;
loc_00836E0F:
    result = (unsigned int)((*(unsigned __int16 *)(v_stack_m60 + v_stack_mB0 * 1 + 96)) | (0xFFFFFFFFULL));
    v_stack_mEC = (unsigned int)(result);
loc_00836E22:
    v_stack_mF8 = (unsigned int)((unsigned int)(0xC0000095ULL));
    if (sign_flag) goto loc_00836C6F;
loc_00836E2E:
loc_00836E33:
    if (((unsigned int)((unsigned int)((unsigned int)(result)) + 120)) < ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_00836E59;
    v_r15 = 0;
    goto loc_00836E64;
loc_00836E4F:
    goto loc_00836E33;
loc_00836E59:
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(result)) + 120) | (0xFFFFFFFFULL));
    v_r15 = 0;
loc_00836E64:
    v_stack_mEC = (unsigned int)(v_rdi);
    v_stack_mF8 = (unsigned int)((unsigned int)(0xC0000095ULL));
    if (sign_flag) goto loc_0083742B;
    v_stack_m120 = 0;
    v_stack_m128 = 0;
    result = I_MinCryptIsCertificateHashRevokedV2((unsigned int)(v_stack_mBC), v_stack_m68, (unsigned int)((unsigned int)((unsigned int)(v_stack_mCC))), v_stack_m70);
    if ((unsigned __int8)(result) != 0) {
        v_stack_mF8 = (unsigned int)((unsigned int)(0xC0000603ULL));
        v_stack_mC0 = 1;
        result = v_stack_m80;
        if (v_stack_m70 < result) { result = v_stack_m70; }
        v_stack_m80 = result;
    }
    v_stack_mF8 = 0;
    if (a4 == 0) goto loc_00836F4D;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a4 + 4))))) == 0) goto loc_00836F4D;
    v_stack_m8C = 50;
    result = I_MinCryptGetCertificateEKUs(v_stack_p8 + 224, v_stack_m8C, v_stack_m58, v_stack_m70);
    v_stack_mF8 = (unsigned int)(result);
    if (sign_flag) goto loc_0083742B;
    result = I_MinCryptCheckEKURequirements((unsigned int)(v_stack_m8C), v_stack_m58, a4, v_stack_m70);
    if ((unsigned __int8)(result) != 0) goto loc_00836F4D;
loc_00836F3F:
loc_00836F44:
    v_stack_mF8 = (unsigned int)((unsigned int)(0xC0000428ULL));
    goto loc_0083742B;
loc_00836F4D:
    result = (unsigned int)(*(unsigned int *)(v_stack_p8 + 112));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 112)))) == (*(unsigned int *)(v_stack_p8 + 160))) {
        a3 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 112)));
        a2 = *(unsigned __int64 *)(v_stack_p8 + 168);
        a1 = *(unsigned __int64 *)(v_stack_p8 + 120);
        result = memcmp(a1, a2, a3, v_stack_m70);
        a1 = 0;
        a1 = ((unsigned int)(result) == 0) ? 1 : 0;
        result = v_stack_mE8;
        a1 = 1;
        if ((unsigned int)(a1) != 0) { result = (unsigned int)(a1); }
        v_stack_mE8 = (unsigned __int8)(result);
    }
    result = MincryptValidateBasicConstraints(v_stack_p8 + 224, (unsigned int)(v_stack_mB8), (unsigned __int8)(v_stack_mE8), v_stack_mF0);
    v_stack_mF8 = (unsigned int)(result);
    if (sign_flag) goto loc_00837416;
    if ((unsigned __int8)(v_stack_mE8) == 0) goto loc_00837187;
    result = I_MinCryptFindRootByKey(v_stack_p8 + 176, (unsigned int)(v_stack_mB8), (unsigned __int8)(v_stack_mE8), v_stack_mF0);
    v_r15 = 0;
    if (result != 0) goto loc_00837095;
    if (a5 == 0) goto loc_00836F3F;
    v_rbx = (unsigned int)(((unsigned int)(v_stack_mF0)) | ((unsigned int)(result + 1)));
    v_stack_mF0 = (unsigned int)(v_rbx);
    v_stack_mD4 = 2;
    if (a4 == 0) goto loc_00837048;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a4 + 4)))) & (32)) == 0) goto loc_00837048;
    result = MinCryptIsCertPresent(v_stack_p8 + 16, *(unsigned __int64 *)(a4 + 120), (unsigned int)(*(unsigned int *)(a4 + 112)), result + 1);
    if ((unsigned int)(result) != 0) goto loc_0083703A;
    result = MinCryptIsKeyPresent(v_stack_p8 + 176, *(unsigned __int64 *)(a4 + 104), (unsigned int)(*(unsigned int *)(a4 + 96)), result + 1);
    if ((unsigned int)(result) != 0) {
        v_stack_mF0 = (unsigned int)(v_rbx);
    }
loc_00837048:
    if (a5 == 0) goto loc_0083710A;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_mF4)))) + ((unsigned int)((unsigned int)((unsigned int)(v_stack_mF4))));
    *(unsigned __int64 *)(v_stack_m98 + a1 * 8) = v_xmm0;
    a2 = (unsigned int)(((unsigned int)(v_stack_mF4)) + (1));
    v_stack_mF4 = a2;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 176)) + 3) & (0xFFFFFFFCULL));
    if (((unsigned int)(a1)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 176))))) goto loc_008370B2;
loc_00837082:
    v_stack_mF8 = (unsigned int)((unsigned int)(0xC0000095ULL));
loc_0083708B:
    goto loc_00837434;
loc_00837095:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_p8 + 176)) + 32))) | (1));
    v_stack_mD4 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 36)));
    goto loc_00837048;
loc_008370B2:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + 96))) | (0xFFFFFFFFULL));
    if (((unsigned int)(a1 + v_rdi * 1)) < ((unsigned int)(v_rdi))) goto loc_008370CA;
    v_stack_mEC = (unsigned int)(a1 + v_rdi * 1);
    goto loc_008370DD;
loc_008370CA:
    v_stack_mEC = (unsigned int)(a3);
loc_008370DD:
    v_stack_mF8 = (unsigned int)((unsigned int)(0xC0000095ULL));
    if (sign_flag) goto loc_0083708B;
    if (((unsigned int)((unsigned int)((unsigned int)(a3)) + 16)) < ((unsigned int)((unsigned int)((unsigned int)(a3))))) goto loc_008370F5;
    v_stack_mEC = (unsigned int)((unsigned int)((unsigned int)(a3)) + 16);
    goto loc_00837102;
loc_008370F5:
    v_stack_mEC = (unsigned int)(a3);
loc_00837102:
    v_stack_mF8 = (unsigned int)((unsigned int)(0xC0000095ULL));
    if (sign_flag) goto loc_0083708B;
loc_0083710A:
    v_stack_mC4 = 1;
loc_00837112:
loc_0083711A:
    v_stack_m120 = a4;
    v_stack_m128 = (unsigned int)(*(unsigned int *)(v_stack_p8 + 176)) + 16;
    result = MinCryptVerifySignedHash2((unsigned int)(v_stack_mBC), v_stack_m68, (unsigned int)(v_stack_mCC), v_stack_p8 + 64);
    v_stack_mF8 = (unsigned int)(result);
    if (sign_flag) goto loc_00836C69;
    if (v_stack_mC4 != 0) goto loc_0083740E;
    result = (unsigned int)(((unsigned int)(v_stack_mB8)) + (1));
    v_stack_mB8 = (unsigned int)(result);
    if (((unsigned int)(result)) < 10) goto loc_008373FB;
    v_stack_mD4 = 1;
    v_r15 = 0;
    goto loc_008373CD;
loc_00837187:
    if (a5 == 0) goto loc_00837240;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_mF4)))) + ((unsigned int)((unsigned int)((unsigned int)(v_stack_mF4))));
    *(unsigned __int64 *)(v_stack_m98 + a1 * 8) = v_xmm0;
    a2 = (unsigned int)(((unsigned int)(v_stack_mF4)) + (1));
    v_stack_mF4 = a2;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 176)) + 3) & (0xFFFFFFFCULL));
    if (((unsigned int)(a1)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 176))))) goto loc_008371E6;
    v_stack_mF8 = (unsigned int)((unsigned int)(0xC0000095ULL));
loc_008371D9:
    v_r15 = 0;
    goto loc_00837434;
loc_008371E6:
    if (((unsigned int)(a1 + (unsigned int)((unsigned int)(a3)) * 1)) < ((unsigned int)((unsigned int)((unsigned int)(a3))))) goto loc_008371FD;
    v_stack_mEC = (unsigned int)(a1 + (unsigned int)((unsigned int)(a3)) * 1);
    v_rbx = 0;
    a3 = (unsigned int)(((unsigned int)(v_stack_mCC)) | (0xFFFFFFFFULL));
    goto loc_00837214;
loc_008371FD:
    a3 = (unsigned int)((a3) | (0xFFFFFFFFULL));
    v_stack_mEC = (unsigned int)(a3);
loc_00837214:
    v_stack_mF8 = (unsigned int)((unsigned int)(0xC0000095ULL));
    if (sign_flag) goto loc_008371D9;
    if (((unsigned int)((unsigned int)((unsigned int)(a3)) + 16)) < ((unsigned int)((unsigned int)((unsigned int)(a3))))) goto loc_0083722B;
    v_stack_mEC = (unsigned int)((unsigned int)((unsigned int)(a3)) + 16);
    v_rbx = 0;
    goto loc_00837238;
loc_0083722B:
    v_stack_mEC = (unsigned int)(a3);
loc_00837238:
    v_stack_mF8 = (unsigned int)((unsigned int)(0xC0000095ULL));
    if (sign_flag) goto loc_008371D9;
loc_00837240:
    result = I_MinCryptFindRootByName(0, a4, a3, v_stack_p8 + 64);
    if (result == 0) goto loc_0083731D;
    v_stack_mD4 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 36)));
    v_stack_mC4 = 1;
    v_r15 = 0;
    if (a5 == 0) goto loc_00837112;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_mF4)))) + ((unsigned int)((unsigned int)((unsigned int)(v_stack_mF4))));
    *(unsigned __int64 *)(v_stack_m98 + a1 * 8) = v_xmm0;
    a2 = (unsigned int)(((unsigned int)(v_stack_mF4)) + (1));
    v_stack_mF4 = a2;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 16)) + 3) & (0xFFFFFFFCULL));
    if (((unsigned int)(a1)) < ((unsigned int)((unsigned int)(*(unsigned int *)(result + 16))))) goto loc_00837082;
    a3 = (unsigned int)((1) | (0xFFFFFFFFULL));
    if (((unsigned int)(a1 + (unsigned int)((unsigned int)(a3)) * 1)) < ((unsigned int)((unsigned int)((unsigned int)(a3))))) goto loc_008372D0;
    v_stack_mEC = (unsigned int)(a1 + (unsigned int)((unsigned int)(a3)) * 1);
    goto loc_008372E3;
loc_008372D0:
    v_stack_mEC = (unsigned int)(a3);
loc_008372E3:
    v_stack_mF8 = (unsigned int)((unsigned int)(0xC0000095ULL));
    if (sign_flag) goto loc_0083708B;
    if (((unsigned int)((unsigned int)((unsigned int)(a3)) + 16)) < ((unsigned int)((unsigned int)((unsigned int)(a3))))) goto loc_008372FF;
    v_stack_mEC = (unsigned int)((unsigned int)((unsigned int)(a3)) + 16);
    goto loc_0083730C;
loc_008372FF:
    v_stack_mEC = (unsigned int)(a3);
loc_0083730C:
    v_stack_mF8 = (unsigned int)((unsigned int)(0xC0000095ULL));
    if (sign_flag) goto loc_0083708B;
    goto loc_00837112;
loc_0083731D:
    v_stack_m128 = v_stack_m58;
    result = I_MinCryptFindIssuerCertificateByName(0, (unsigned int)(v_stack_p10), v_stack_p18, a4);
    v_stack_m88 = result;
    v_r15 = result;
    if (result != 0) {
        a1 = result + 48;
        result = MinCryptDecodeHashAlgorithmIdentifier(a1, (unsigned int)(v_stack_p10), v_stack_p18, a4);
        result = (unsigned int)(-(result));
        a1 = (a1) & (result);
        v_r15 = a1;
        v_stack_m88 = a1;
    }
    if (v_r15 != 0) goto loc_008373EF;
    if (a4 == 0) goto loc_008373C9;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a4 + 4)))) & (32)) == 0) goto loc_008373C9;
    v_stack_m110 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 96)));
    v_stack_m120 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 112)));
    v_stack_m128 = *(unsigned __int64 *)(a4 + 120);
    result = MinCryptCheckCertsAndKeys((unsigned int)(v_stack_mBC), v_stack_m68, (unsigned int)(v_stack_mCC), v_stack_p8);
    v_stack_mF8 = (unsigned int)(result);
    if (sign_flag) goto loc_008373C9;
    goto loc_0083742B;
loc_008373C9:
    v_stack_mD4 = (unsigned int)(result + 16);
loc_008373CD:
    if (a5 == v_r15) goto loc_008373E4;
    goto loc_00836F44;
loc_008373E4:
    goto loc_00836F3F;
loc_008373EF:
    goto loc_0083711A;
loc_008373FB:
    v_stack_p8 = v_r15;
    v_stack_m50 = v_r15;
loc_0083740E:
    v_r15 = 0;
    goto loc_00836BF6;
loc_00837416:
    goto loc_008371D9;
loc_0083741F:
    v_r15 = 0;
    goto loc_0083708B;
loc_0083742B:
loc_00837430:
loc_00837434:
    if (a5 == 0) goto loc_008374DB;
    *(unsigned int *)(a5) = 48;
    *(unsigned int *)(a5 + 4) = (unsigned int)((unsigned int)((unsigned int)(v_r15)));
    *(unsigned int *)(a5 + 8) = (unsigned int)((unsigned int)(v_stack_mF0));
    *(unsigned __int64 *)(a5 + 16) = 0;
    *(unsigned __int64 *)(a5 + 32) = v_stack_mA8;
    *(unsigned __int64 *)(a5 + 40) = v_stack_mA0;
    result = v_stack_mA0;
    if (v_stack_mC0 != 0) {
        result = v_stack_m80;
        *(unsigned __int64 *)(a5 + 24) = result;
    }
    v_rbx = (unsigned int)((unsigned int)(v_r15));
    if (!(sign_flag)) {
        result = a6;
        v_stack_m100 = result;
        result = v_stack_mB0;
        v_stack_m108 = result;
        result = v_stack_m98;
        v_stack_m110 = result;
        v_stack_m118 = v_stack_mE0;
        result = v_stack_mD4;
        v_stack_m120 = (unsigned int)(result);
        result = v_stack_mC8;
        v_stack_m128 = (unsigned int)(result);
        a4 = (unsigned int)((unsigned int)(v_stack_mF4));
        a3 = v_stack_mD0;
        a2 = (unsigned int)((unsigned int)((unsigned int)(a3)));
        result = I_MincryptAddChainInfo(a5, a2, a3, a4);
        v_rbx = (unsigned int)(result);
    }
    if (v_stack_mE0 != 0) {
        a2 = 0x72634943ULL;
        a1 = v_stack_mE0;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (!(sign_flag)) {
        if (v_stack_mC0 != 0) { v_rbx = (unsigned int)((unsigned int)(0xC0000603ULL)); }
    }
    v_rsp = (v_rsp) + (272);
    return (unsigned int)((unsigned int)(v_rbx));
}
```

## 5. (Beta) C Style

```c
int64_t MinCryptVerifyCertificateWithPolicy2(void *Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint32_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint32_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint32_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint8_t v_stack_mD7;
    uint8_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint8_t v_stack_mE8;
    uint32_t v_stack_mEC;
    uint32_t v_stack_mF0;
    uint32_t v_stack_mF4;
    uint32_t v_stack_mF8;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    v_stack_p10 = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (272);
    local_r15 = 0;
    v_stack_mF8 = 0;
    *(uint32_t *)(local_rsp - 0xB8) = 0;
    v_stack_mD0 = 50;
    *(uint32_t *)(local_rsp - 0xC4) = 0;
    v_stack_mCC = 0;
    v_stack_mF0 = 0;
    v_stack_mF4 = 0;
    v_stack_mEC = 0;
    *(uint32_t *)(local_rsp - 0xC8) = 0;
    *(uint64_t *)(local_rsp - 0x88) = 0;
    *(uint32_t *)(local_rsp - 0xC0) = 0;
    *(uint64_t *)(local_rsp - 0x70) = 0;
    v_stack_mD4 = 0;
    *(uint64_t *)(local_rsp - 0xB0) = 0;
    v_stack_mE0 = 0;
    *(uint64_t *)(local_rsp - 0x98) = 0;
    *(uint64_t *)(local_rsp - 0xA8) = 0;
    *(uint64_t *)(local_rsp - 0xA0) = 0;
    v_stack_mE8 = 0;
    *(uint64_t *)(local_rsp - 0x80) = result;
    *(void **)(local_rsp - 0x50) = Arg1;
    result = ExAllocatePool2(258, (uint32_t)(0xBA0ULL), (uint32_t)(0x72634943ULL), Arg4);
    v_stack_mE0 = result;
    if (result != 0) goto loc_00836990;
loc_00836981:
    v_stack_mF8 = (uint32_t)((uint32_t)(0xC0000017ULL));
loc_00836985:
    goto loc_00837430;
loc_00836990:
    result = (result) + (800);
    v_stack_m98 = result;
    v_stack_m58 = result + 176;
    v_stack_mB0 = result + 176 + 800;
    result = I_MinCryptGetCertificateEKUs(Arg1 + 224, v_stack_mD0, v_stack_mE0, Arg4);
    v_stack_mF8 = (uint32_t)(result);
    if (sign_flag) goto loc_00836985;
    Arg3 = (uint32_t)((v_stack_mE0) | (0xFFFFFFFFULL));
loc_008369F8:
    v_stack_m78 = 0;
    if (0 >= v_stack_mD0) goto loc_00836A7E;
    result = (0) + (0);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mE0 + result * 8)) + 3) & ((uint32_t)((uint32_t)(0xFFFFFFFCULL))));
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mE0 + result * 8))))) goto loc_00836A1F;
loc_00836A17:
    goto loc_00836981;
loc_00836A1F:
    result = (uint32_t)((result) + (0));
    if (((uint32_t)(result)) < 0) goto loc_00836A32;
    v_stack_mEC = (uint32_t)(result);
    goto loc_00836A43;
loc_00836A32:
    v_stack_mEC = (uint32_t)(Arg3);
loc_00836A43:
    v_stack_mF8 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))));
    if (sign_flag) goto loc_00836985;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg3)) + 16)) < ((uint32_t)((uint32_t)((uint32_t)(Arg3))))) goto loc_00836A5F;
    v_stack_mEC = (uint32_t)((uint32_t)((uint32_t)(Arg3)) + 16);
    goto loc_00836A6A;
loc_00836A5F:
    v_stack_mEC = (uint32_t)(Arg3);
loc_00836A6A:
    v_stack_mF8 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))));
    if (sign_flag) goto loc_00836985;
    Arg2 = (uint32_t)((0) + (1));
    goto loc_008369F8;
loc_00836A7E:
    if (Arg6 == 0) goto loc_00836AC0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg6)) + 3) & ((uint32_t)((uint32_t)(0xFFFFFFFCULL))));
    if (((uint32_t)(Arg1)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg6))))) goto loc_00836A17;
    if (((uint32_t)(Arg1 + (uint32_t)((uint32_t)(Arg3)) * 1)) < ((uint32_t)((uint32_t)((uint32_t)(Arg3))))) goto loc_00836AA9;
    v_stack_mEC = (uint32_t)(Arg1 + (uint32_t)((uint32_t)(Arg3)) * 1);
    goto loc_00836AB4;
loc_00836AA9:
    v_stack_mEC = (uint32_t)(Arg3);
loc_00836AB4:
    v_stack_mF8 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))));
    if (sign_flag) goto loc_00836985;
loc_00836AC0:
    if (Arg4 == 0) goto loc_00836AF1;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) != 0) goto loc_00836AF1;
    result = I_MinCryptCheckEKURequirements((uint32_t)(v_stack_mD0), v_stack_mE0, Arg4, (uint32_t)(0xC0000095ULL));
    if ((uint8_t)(result) != 0) goto loc_00836AF1;
    goto loc_00836981;
loc_00836AF1:
    result = I_MinCryptGetCertValidityPeriod(v_stack_p8, v_stack_mA8, v_stack_mA0, (uint32_t)(0xC0000095ULL));
    result = I_MinCryptCheckEKU(v_rip + 3232105, (uint32_t)(v_stack_mD0), v_stack_mE0, (uint32_t)(0xC0000095ULL));
    v_stack_mD7 = (uint8_t)(result);
    if ((uint8_t)(result) == 0) goto loc_00836B5E;
    if (condition_is_less_or_equal) goto loc_00836B5E;
    Arg1 = 0;
    if (v_stack_mA8 < (*(uint64_t *)(v_rip + 0x7A1755))) { Arg1 = 1; }
    if ((uint8_t)(Arg1) == 0) goto loc_00836B5E;
    goto loc_00836981;
loc_00836B5E:
    if ((*(uint8_t *)(v_rip + 0x5DB163)) != 0) goto loc_00836BF0;
    result = I_MinCryptCheckEKU(v_rip + 3231999, (uint32_t)(v_stack_mD0), v_stack_mE0, (uint32_t)(0xC0000095ULL));
    if ((uint8_t)(result) == 0) goto loc_00836BF0;
    v_stack_mD8 = 0;
    if (v_stack_mD7 != 0) goto loc_00836BA7;
    if ((*(uint64_t *)(result)) < v_stack_mA8) goto loc_00836BB1;
loc_00836BA7:
    if ((*(uint64_t *)(result)) >= = v_stack_mA0) {
        Arg1 = 1;
        v_stack_mD8 = (uint8_t)(Arg1);
    }
    if ((uint8_t)(Arg1) == 0) goto loc_00836BD8;
    v_stack_mF8 = (uint32_t)((uint32_t)(0xC0000605ULL));
    goto loc_0083742B;
loc_00836BD8:
    v_stack_p8 = v_stack_m50;
loc_00836BF0:
loc_00836BF6:
    if (v_stack_mC4 != 0) goto loc_0083742B;
    local_rsi = (v_stack_mE0) * ((uint32_t)(v_stack_mC8));
    v_stack_m60 = local_rsi;
    local_rbx = (v_stack_mB0) + (8);
    local_rbx = (local_rbx) + (local_rsi);
    v_stack_m68 = local_rbx;
    result = MinCryptDecodeHashAlgorithmIdentifier(v_stack_m50 + 48, (uint32_t)(v_stack_mD0), v_stack_mE0, (uint32_t)(0xC0000095ULL));
    v_stack_mBC = (uint32_t)(result);
    v_stack_m128 = v_stack_mCC;
    result = MinCryptHashMemory((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), 1, v_stack_m50 + 32, local_rbx);
    v_stack_mF8 = (uint32_t)(result);
    if (!sign_flag) goto loc_00836C77;
loc_00836C69:
loc_00836C6F:
    local_r15 = 0;
    goto loc_0083742B;
loc_00836C77:
    *(uint32_t *)(local_rsi + v_stack_mB0 * 1) = 0;
    *(uint32_t *)(local_rsi + v_stack_mB0 * 1 + 0x4) = (uint32_t)((uint32_t)(v_stack_mCC));
    *(uint64_t *)(local_rsi + v_stack_mB0 * 1 + 0x68) = v_xmm0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m50 + 0x10)) + 3) & (0xFFFFFFFCULL));
    if (((uint32_t)(Arg1)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m50 + 0x10))))) goto loc_00836CB1;
loc_00836CA6:
    v_stack_mF8 = (uint32_t)((uint32_t)(0xC0000095ULL));
    goto loc_00836C6F;
loc_00836CB1:
    if (((uint32_t)(Arg1 + (uint32_t)(v_stack_mEC) * 1)) < ((uint32_t)((uint32_t)(v_stack_mEC)))) goto loc_00836CDA;
    v_stack_mEC = (uint32_t)(Arg1 + (uint32_t)(v_stack_mEC) * 1);
    local_rbx = 0;
    v_stack_m90 = (uint32_t)(Arg1 + (uint32_t)(v_stack_mEC) * 1);
    goto loc_00836D02;
loc_00836CDA:
    Arg3 = (uint32_t)((v_stack_m50 + 32) | (0xFFFFFFFFULL));
    v_stack_mEC = (uint32_t)(Arg3);
    v_stack_m90 = (uint32_t)(Arg3);
loc_00836D02:
    v_stack_mF8 = (uint32_t)((uint32_t)(0xC0000095ULL));
    if (sign_flag) goto loc_0083741F;
    *(uint64_t *)(v_stack_m60 + v_stack_mB0 * 1 + 0x48) = v_xmm0;
    Arg2 = (v_stack_mB0) + (88);
    Arg2 = (Arg2) + (v_stack_m60);
    v_stack_m48 = Arg2;
    *(uint64_t *)(Arg2) = v_xmm1;
    if (Arg5 == 0) goto loc_00836E4F;
    Arg1 = (v_stack_p8) + (160);
    result = I_MinCryptGetCommonName(Arg1, v_stack_m60 + v_stack_mB0 * 1 + 72, v_stack_m60 + v_stack_mB0 * 1, local_rbx);
    if ((uint8_t)(result) == 0) goto loc_00836DC3;
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_m60 + v_stack_mB0 * 1 + 0x50) + 3) & (0xFFFFFFFCULL));
    if (((uint32_t)(Arg1)) < ((uint32_t)(*(uint16_t *)(v_stack_m60 + v_stack_mB0 * 1 + 0x50)))) goto loc_00836CA6;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg3)) + Arg1 * 1)) < v_stack_m90) goto loc_00836D9C;
    v_stack_mEC = (uint32_t)((uint32_t)((uint32_t)(Arg3)) + Arg1 * 1);
    local_rbx = 0;
    goto loc_00836DAF;
loc_00836D9C:
    result = (uint32_t)((*(uint16_t *)(v_stack_m60 + v_stack_mB0 * 1 + 0x50)) | (0xFFFFFFFFULL));
    v_stack_mEC = (uint32_t)(result);
loc_00836DAF:
    v_stack_mF8 = (uint32_t)((uint32_t)(0xC0000095ULL));
    if (sign_flag) goto loc_00836C6F;
loc_00836DC3:
    result = I_MinCryptGetCommonName(v_stack_p8 + 112, v_stack_m48, v_stack_m60 + v_stack_mB0 * 1, local_rbx);
    if ((uint8_t)(result) == 0) goto loc_00836E2E;
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_m60 + v_stack_mB0 * 1 + 0x60) + 3) & (0xFFFFFFFCULL));
    if (((uint32_t)(Arg1)) < ((uint32_t)(*(uint16_t *)(v_stack_m60 + v_stack_mB0 * 1 + 0x60)))) goto loc_00836CA6;
    if (((uint32_t)(Arg1 + (uint32_t)((uint32_t)(result)) * 1)) < ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_00836E0F;
    v_stack_mEC = (uint32_t)(Arg1 + (uint32_t)((uint32_t)(result)) * 1);
    local_rbx = 0;
    goto loc_00836E22;
loc_00836E0F:
    result = (uint32_t)((*(uint16_t *)(v_stack_m60 + v_stack_mB0 * 1 + 0x60)) | (0xFFFFFFFFULL));
    v_stack_mEC = (uint32_t)(result);
loc_00836E22:
    v_stack_mF8 = (uint32_t)((uint32_t)(0xC0000095ULL));
    if (sign_flag) goto loc_00836C6F;
loc_00836E2E:
loc_00836E33:
    if (((uint32_t)((uint32_t)((uint32_t)(result)) + 120)) < ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_00836E59;
    local_r15 = 0;
    goto loc_00836E64;
loc_00836E4F:
    goto loc_00836E33;
loc_00836E59:
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(result)) + 120) | (0xFFFFFFFFULL));
    local_r15 = 0;
loc_00836E64:
    v_stack_mEC = (uint32_t)(local_rdi);
    v_stack_mF8 = (uint32_t)((uint32_t)(0xC0000095ULL));
    if (sign_flag) goto loc_0083742B;
    v_stack_m120 = 0;
    v_stack_m128 = 0;
    result = I_MinCryptIsCertificateHashRevokedV2((uint32_t)(v_stack_mBC), v_stack_m68, (uint32_t)((uint32_t)((uint32_t)(v_stack_mCC))), v_stack_m70);
    if ((uint8_t)(result) != 0) {
        v_stack_mF8 = (uint32_t)((uint32_t)(0xC0000603ULL));
        v_stack_mC0 = 1;
        result = v_stack_m80;
        if (v_stack_m70 < result) { result = v_stack_m70; }
        v_stack_m80 = result;
    }
    v_stack_mF8 = 0;
    if (Arg4 == 0) goto loc_00836F4D;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) == 0) goto loc_00836F4D;
    v_stack_m8C = 50;
    result = I_MinCryptGetCertificateEKUs(v_stack_p8 + 224, v_stack_m8C, v_stack_m58, v_stack_m70);
    v_stack_mF8 = (uint32_t)(result);
    if (sign_flag) goto loc_0083742B;
    result = I_MinCryptCheckEKURequirements((uint32_t)(v_stack_m8C), v_stack_m58, Arg4, v_stack_m70);
    if ((uint8_t)(result) != 0) goto loc_00836F4D;
loc_00836F3F:
loc_00836F44:
    v_stack_mF8 = (uint32_t)((uint32_t)(0xC0000428ULL));
    goto loc_0083742B;
loc_00836F4D:
    result = (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x70));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x70)))) == (*(uint32_t *)(v_stack_p8 + 0xA0))) {
        Arg3 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x70)));
        Arg2 = *(uint64_t *)(v_stack_p8 + 0xA8);
        Arg1 = *(uint64_t *)(v_stack_p8 + 0x78);
        result = memcmp(Arg1, Arg2, Arg3, v_stack_m70);
        Arg1 = 0;
        Arg1 = ((uint32_t)(result) == 0) ? 1 : 0;
        result = v_stack_mE8;
        Arg1 = 1;
        if ((uint32_t)(Arg1) != 0) { result = (uint32_t)(Arg1); }
        v_stack_mE8 = (uint8_t)(result);
    }
    result = MincryptValidateBasicConstraints(v_stack_p8 + 224, (uint32_t)(v_stack_mB8), (uint8_t)(v_stack_mE8), v_stack_mF0);
    v_stack_mF8 = (uint32_t)(result);
    if (sign_flag) goto loc_00837416;
    if ((uint8_t)(v_stack_mE8) == 0) goto loc_00837187;
    result = I_MinCryptFindRootByKey(v_stack_p8 + 176, (uint32_t)(v_stack_mB8), (uint8_t)(v_stack_mE8), v_stack_mF0);
    local_r15 = 0;
    if (result != 0) goto loc_00837095;
    if (Arg5 == 0) goto loc_00836F3F;
    local_rbx = (uint32_t)(((uint32_t)(v_stack_mF0)) | ((uint32_t)(result + 1)));
    v_stack_mF0 = (uint32_t)(local_rbx);
    v_stack_mD4 = 2;
    if (Arg4 == 0) goto loc_00837048;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)))) & (32)) == 0) goto loc_00837048;
    result = MinCryptIsCertPresent(v_stack_p8 + 16, *(uint64_t *)(Arg4 + 0x78), (uint32_t)(*(uint32_t *)(Arg4 + 0x70)), result + 1);
    if ((uint32_t)(result) != 0) goto loc_0083703A;
    result = MinCryptIsKeyPresent(v_stack_p8 + 176, *(uint64_t *)(Arg4 + 0x68), (uint32_t)(*(uint32_t *)(Arg4 + 0x60)), result + 1);
    if ((uint32_t)(result) != 0) {
        v_stack_mF0 = (uint32_t)(local_rbx);
    }
loc_00837048:
    if (Arg5 == 0) goto loc_0083710A;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_mF4)))) + ((uint32_t)((uint32_t)((uint32_t)(v_stack_mF4))));
    *(uint64_t *)(v_stack_m98 + arg1 * 8) = v_xmm0;
    Arg2 = (uint32_t)(((uint32_t)(v_stack_mF4)) + (1));
    v_stack_mF4 = Arg2;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xB0)) + 3) & (0xFFFFFFFCULL));
    if (((uint32_t)(Arg1)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xB0))))) goto loc_008370B2;
loc_00837082:
    v_stack_mF8 = (uint32_t)((uint32_t)(0xC0000095ULL));
loc_0083708B:
    goto loc_00837434;
loc_00837095:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xB0)) + 0x20))) | (1));
    v_stack_mD4 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x24)));
    goto loc_00837048;
loc_008370B2:
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg4 + 0x60))) | (0xFFFFFFFFULL));
    if (((uint32_t)(Arg1 + local_rdi * 1)) < ((uint32_t)(local_rdi))) goto loc_008370CA;
    v_stack_mEC = (uint32_t)(Arg1 + local_rdi * 1);
    goto loc_008370DD;
loc_008370CA:
    v_stack_mEC = (uint32_t)(Arg3);
loc_008370DD:
    v_stack_mF8 = (uint32_t)((uint32_t)(0xC0000095ULL));
    if (sign_flag) goto loc_0083708B;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg3)) + 16)) < ((uint32_t)((uint32_t)((uint32_t)(Arg3))))) goto loc_008370F5;
    v_stack_mEC = (uint32_t)((uint32_t)((uint32_t)(Arg3)) + 16);
    goto loc_00837102;
loc_008370F5:
    v_stack_mEC = (uint32_t)(Arg3);
loc_00837102:
    v_stack_mF8 = (uint32_t)((uint32_t)(0xC0000095ULL));
    if (sign_flag) goto loc_0083708B;
loc_0083710A:
    v_stack_mC4 = 1;
loc_00837112:
loc_0083711A:
    v_stack_m120 = Arg4;
    v_stack_m128 = (uint32_t)(*(uint32_t *)(v_stack_p8 + 0xB0)) + 16;
    result = MinCryptVerifySignedHash2((uint32_t)(v_stack_mBC), v_stack_m68, (uint32_t)(v_stack_mCC), v_stack_p8 + 64);
    v_stack_mF8 = (uint32_t)(result);
    if (sign_flag) goto loc_00836C69;
    if (v_stack_mC4 != 0) goto loc_0083740E;
    result = (uint32_t)(((uint32_t)(v_stack_mB8)) + (1));
    v_stack_mB8 = (uint32_t)(result);
    if (((uint32_t)(result)) < 10) goto loc_008373FB;
    v_stack_mD4 = 1;
    local_r15 = 0;
    goto loc_008373CD;
loc_00837187:
    if (Arg5 == 0) goto loc_00837240;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_mF4)))) + ((uint32_t)((uint32_t)((uint32_t)(v_stack_mF4))));
    *(uint64_t *)(v_stack_m98 + arg1 * 8) = v_xmm0;
    Arg2 = (uint32_t)(((uint32_t)(v_stack_mF4)) + (1));
    v_stack_mF4 = Arg2;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xB0)) + 3) & (0xFFFFFFFCULL));
    if (((uint32_t)(Arg1)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xB0))))) goto loc_008371E6;
    v_stack_mF8 = (uint32_t)((uint32_t)(0xC0000095ULL));
loc_008371D9:
    local_r15 = 0;
    goto loc_00837434;
loc_008371E6:
    if (((uint32_t)(Arg1 + (uint32_t)((uint32_t)(Arg3)) * 1)) < ((uint32_t)((uint32_t)((uint32_t)(Arg3))))) goto loc_008371FD;
    v_stack_mEC = (uint32_t)(Arg1 + (uint32_t)((uint32_t)(Arg3)) * 1);
    local_rbx = 0;
    Arg3 = (uint32_t)(((uint32_t)(v_stack_mCC)) | (0xFFFFFFFFULL));
    goto loc_00837214;
loc_008371FD:
    Arg3 = (uint32_t)((Arg3) | (0xFFFFFFFFULL));
    v_stack_mEC = (uint32_t)(Arg3);
loc_00837214:
    v_stack_mF8 = (uint32_t)((uint32_t)(0xC0000095ULL));
    if (sign_flag) goto loc_008371D9;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg3)) + 16)) < ((uint32_t)((uint32_t)((uint32_t)(Arg3))))) goto loc_0083722B;
    v_stack_mEC = (uint32_t)((uint32_t)((uint32_t)(Arg3)) + 16);
    local_rbx = 0;
    goto loc_00837238;
loc_0083722B:
    v_stack_mEC = (uint32_t)(Arg3);
loc_00837238:
    v_stack_mF8 = (uint32_t)((uint32_t)(0xC0000095ULL));
    if (sign_flag) goto loc_008371D9;
loc_00837240:
    result = I_MinCryptFindRootByName(0, Arg4, Arg3, v_stack_p8 + 64);
    if (result == 0) goto loc_0083731D;
    v_stack_mD4 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x24)));
    v_stack_mC4 = 1;
    local_r15 = 0;
    if (Arg5 == 0) goto loc_00837112;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_mF4)))) + ((uint32_t)((uint32_t)((uint32_t)(v_stack_mF4))));
    *(uint64_t *)(v_stack_m98 + arg1 * 8) = v_xmm0;
    Arg2 = (uint32_t)(((uint32_t)(v_stack_mF4)) + (1));
    v_stack_mF4 = Arg2;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x10)) + 3) & (0xFFFFFFFCULL));
    if (((uint32_t)(Arg1)) < ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10))))) goto loc_00837082;
    Arg3 = (uint32_t)((1) | (0xFFFFFFFFULL));
    if (((uint32_t)(Arg1 + (uint32_t)((uint32_t)(Arg3)) * 1)) < ((uint32_t)((uint32_t)((uint32_t)(Arg3))))) goto loc_008372D0;
    v_stack_mEC = (uint32_t)(Arg1 + (uint32_t)((uint32_t)(Arg3)) * 1);
    goto loc_008372E3;
loc_008372D0:
    v_stack_mEC = (uint32_t)(Arg3);
loc_008372E3:
    v_stack_mF8 = (uint32_t)((uint32_t)(0xC0000095ULL));
    if (sign_flag) goto loc_0083708B;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg3)) + 16)) < ((uint32_t)((uint32_t)((uint32_t)(Arg3))))) goto loc_008372FF;
    v_stack_mEC = (uint32_t)((uint32_t)((uint32_t)(Arg3)) + 16);
    goto loc_0083730C;
loc_008372FF:
    v_stack_mEC = (uint32_t)(Arg3);
loc_0083730C:
    v_stack_mF8 = (uint32_t)((uint32_t)(0xC0000095ULL));
    if (sign_flag) goto loc_0083708B;
    goto loc_00837112;
loc_0083731D:
    v_stack_m128 = v_stack_m58;
    result = I_MinCryptFindIssuerCertificateByName(0, (uint32_t)(v_stack_p10), v_stack_p18, Arg4);
    v_stack_m88 = result;
    local_r15 = result;
    if (result != 0) {
        Arg1 = result + 48;
        result = MinCryptDecodeHashAlgorithmIdentifier(Arg1, (uint32_t)(v_stack_p10), v_stack_p18, Arg4);
        result = (uint32_t)(-(result));
        Arg1 = (Arg1) & (result);
        local_r15 = Arg1;
        v_stack_m88 = Arg1;
    }
    if (local_r15 != 0) goto loc_008373EF;
    if (Arg4 == 0) goto loc_008373C9;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)))) & (32)) == 0) goto loc_008373C9;
    v_stack_m110 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x60)));
    v_stack_m120 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x70)));
    v_stack_m128 = *(uint64_t *)(Arg4 + 0x78);
    result = MinCryptCheckCertsAndKeys((uint32_t)(v_stack_mBC), v_stack_m68, (uint32_t)(v_stack_mCC), v_stack_p8);
    v_stack_mF8 = (uint32_t)(result);
    if (sign_flag) goto loc_008373C9;
    goto loc_0083742B;
loc_008373C9:
    v_stack_mD4 = (uint32_t)(result + 16);
loc_008373CD:
    if (Arg5 == local_r15) goto loc_008373E4;
    goto loc_00836F44;
loc_008373E4:
    goto loc_00836F3F;
loc_008373EF:
    goto loc_0083711A;
loc_008373FB:
    v_stack_p8 = local_r15;
    v_stack_m50 = local_r15;
loc_0083740E:
    local_r15 = 0;
    goto loc_00836BF6;
loc_00837416:
    goto loc_008371D9;
loc_0083741F:
    local_r15 = 0;
    goto loc_0083708B;
loc_0083742B:
loc_00837430:
loc_00837434:
    if (Arg5 == 0) goto loc_008374DB;
    *(uint32_t *)(Arg5) = 48;
    *(uint32_t *)(Arg5 + 0x4) = (uint32_t)((uint32_t)((uint32_t)(local_r15)));
    *(uint32_t *)(Arg5 + 0x8) = (uint32_t)((uint32_t)(v_stack_mF0));
    *(uint64_t *)(Arg5 + 0x10) = 0;
    *(uint64_t *)(Arg5 + 0x20) = v_stack_mA8;
    *(uint64_t *)(Arg5 + 0x28) = v_stack_mA0;
    result = v_stack_mA0;
    if (v_stack_mC0 != 0) {
        result = v_stack_m80;
        *(uint64_t *)(Arg5 + 0x18) = result;
    }
    local_rbx = (uint32_t)((uint32_t)(local_r15));
    if (!(sign_flag)) {
        result = Arg6;
        v_stack_m100 = result;
        result = v_stack_mB0;
        v_stack_m108 = result;
        result = v_stack_m98;
        v_stack_m110 = result;
        v_stack_m118 = v_stack_mE0;
        result = v_stack_mD4;
        v_stack_m120 = (uint32_t)(result);
        result = v_stack_mC8;
        v_stack_m128 = (uint32_t)(result);
        Arg4 = (uint32_t)((uint32_t)(v_stack_mF4));
        Arg3 = v_stack_mD0;
        Arg2 = (uint32_t)((uint32_t)((uint32_t)(Arg3)));
        result = I_MincryptAddChainInfo(Arg5, Arg2, Arg3, Arg4);
        local_rbx = (uint32_t)(result);
    }
    if (v_stack_mE0 != 0) {
        Arg2 = 0x72634943ULL;
        Arg1 = v_stack_mE0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    if (!(sign_flag)) {
        if (v_stack_mC0 != 0) { local_rbx = (uint32_t)((uint32_t)(0xC0000603ULL)); }
    }
    local_rsp = (local_rsp) + (272);
    return (uint32_t)((uint32_t)(local_rbx));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xE0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008368A8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
