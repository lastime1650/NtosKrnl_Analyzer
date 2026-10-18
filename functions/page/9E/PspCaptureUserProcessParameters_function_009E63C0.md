# PspCaptureUserProcessParameters

- RVA: `0x009E63C0`–`0x009E6C22` (길이 `2,146` bytes)
- VA: `0x00000001409E63C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A46B8`
- 디코드: `489`개 명령, `2,146/2,146` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **25**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x009E64AD` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009E64F5` → [PsGetServerSiloGlobals](../../text/22/PsGetServerSiloGlobals_function_002250A0.md) (function, `0x002250A0`)
- `0x009E6557` → [PspCaptureAndValidateUnicodeString](PspCaptureAndValidateUnicodeString_function_009E6C28.md) (function, `0x009E6C28`)
- `0x009E6570` → [PspCaptureAndValidateUnicodeString](PspCaptureAndValidateUnicodeString_function_009E6C28.md) (function, `0x009E6C28`)
- `0x009E6589` → [PspCaptureAndValidateUnicodeString](PspCaptureAndValidateUnicodeString_function_009E6C28.md) (function, `0x009E6C28`)
- `0x009E65A5` → [PspCaptureAndValidateUnicodeString](PspCaptureAndValidateUnicodeString_function_009E6C28.md) (function, `0x009E6C28`)
- `0x009E65C1` → [PspCaptureAndValidateUnicodeString](PspCaptureAndValidateUnicodeString_function_009E6C28.md) (function, `0x009E6C28`)
- `0x009E65DD` → [PspCaptureAndValidateUnicodeString](PspCaptureAndValidateUnicodeString_function_009E6C28.md) (function, `0x009E6C28`)
- `0x009E6603` → [PspCaptureAndValidateUnicodeString](PspCaptureAndValidateUnicodeString_function_009E6C28.md) (function, `0x009E6C28`)
- `0x009E66D7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009E67AA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009E67FB` → [PspCopyUnicodeString](PspCopyUnicodeString_function_009E6C94.md) (function, `0x009E6C94`)
- `0x009E6818` → [PspCopyUnicodeString](PspCopyUnicodeString_function_009E6C94.md) (function, `0x009E6C94`)
- `0x009E6835` → [PspCopyUnicodeString](PspCopyUnicodeString_function_009E6C94.md) (function, `0x009E6C94`)
- `0x009E6856` → [PspCopyUnicodeString](PspCopyUnicodeString_function_009E6C94.md) (function, `0x009E6C94`)
- `0x009E687A` → [PspCopyUnicodeString](PspCopyUnicodeString_function_009E6C94.md) (function, `0x009E6C94`)
- `0x009E689E` → [PspCopyUnicodeString](PspCopyUnicodeString_function_009E6C94.md) (function, `0x009E6C94`)
- `0x009E68C2` → [PspCopyUnicodeString](PspCopyUnicodeString_function_009E6C94.md) (function, `0x009E6C94`)
- `0x009E68E3` → [PspCopyUnicodeString](PspCopyUnicodeString_function_009E6C94.md) (function, `0x009E6C94`)
- `0x009E6943` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009E697B` → [PspValidateEnvironmentBlock](PspValidateEnvironmentBlock_function_009E6D10.md) (function, `0x009E6D10`)
- `0x009E69D6` → [PspCaptureAndValidateUnicodeString](PspCaptureAndValidateUnicodeString_function_009E6C28.md) (function, `0x009E6C28`)
- `0x009E6A56` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009E6B40` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009E6C04` → [PspCopyUnicodeString](PspCopyUnicodeString_function_009E6C94.md) (function, `0x009E6C94`)

### Direct callers
- [PsCaptureUserProcessParameters](PsCaptureUserProcessParameters_function_009E6310.md) at `0x009E6339`
- [PspCaptureProcessParameters](PspCaptureProcessParameters_function_009E6350.md) at `0x009E638A`

### Static image references
- `0x009E6507` → RVA `0x00B4BEE8` (`PspProtectedRuntimeData`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x009E64F5` → [PsGetServerSiloGlobals](../../text/22/PsGetServerSiloGlobals_function_002250A0.md) (`PAGE` → `.text`)
  - `0x009E66D7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009E67AA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009E6943` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009E6A56` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009E6B40` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x009E6921` → [sub_00B306B6](../B3/Unknown_function_00B306B6.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009E63C0  48 8B C4                        mov rax, rsp
009E63C3  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
009E63C7  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
009E63CB  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
009E63CF  48 89 48 08                     mov qword ptr [rax + 8], rcx
009E63D3  53                              push rbx
009E63D4  56                              push rsi
009E63D5  57                              push rdi
009E63D6  41 54                           push r12
009E63D8  41 55                           push r13
009E63DA  41 56                           push r14
009E63DC  41 57                           push r15
009E63DE  48 81 EC 10 01 00 00            sub rsp, 0x110
009E63E5  0F 29 70 B8                     movaps xmmword ptr [rax - 0x48], xmm6
009E63E9  4D 8B F8                        mov r15, r8
009E63EC  48 8B F2                        mov rsi, rdx
009E63EF  4D 8B E8                        mov r13, r8
009E63F2  4C 89 44 24 50                  mov qword ptr [rsp + 0x50], r8
009E63F7  0F 57 C0                        xorps xmm0, xmm0
009E63FA  0F 11 80 60 FF FF FF            movups xmmword ptr [rax - 0xa0], xmm0
009E6401  0F 57 C9                        xorps xmm1, xmm1
009E6404  0F 11 4C 24 68                  movups xmmword ptr [rsp + 0x68], xmm1
009E6409  0F 11 40 80                     movups xmmword ptr [rax - 0x80], xmm0
009E640D  0F 11 88 40 FF FF FF            movups xmmword ptr [rax - 0xc0], xmm1
009E6414  33 DB                           xor ebx, ebx
009E6416  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
009E641B  0F 11 80 50 FF FF FF            movups xmmword ptr [rax - 0xb0], xmm0
009E6422  0F 11 4C 24 78                  movups xmmword ptr [rsp + 0x78], xmm1
009E6427  0F 11 40 90                     movups xmmword ptr [rax - 0x70], xmm0
009E642B  0F 11 88 70 FF FF FF            movups xmmword ptr [rax - 0x90], xmm1
009E6432  40 F6 C6 03                     test sil, 3
009E6436  75 75                           jne 0x1409e64ad
009E6438  49 B8 00 00 FF FF FF 7F 00 00   movabs r8, 0x7fffffff0000
009E6442  49 8B C0                        mov rax, r8
009E6445  49 3B D0                        cmp rdx, r8
009E6448  48 0F 42 C2                     cmovb rax, rdx
009E644C  90                              nop
009E644D  8A 00                           mov al, byte ptr [rax]
009E644F  8B 7A 08                        mov edi, dword ptr [rdx + 8]
009E6452  0F BA F7 0E                     btr edi, 0xe
009E6456  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
009E645A  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
009E645E  8B C7                           mov eax, edi
009E6460  83 F0 01                        xor eax, 1
009E6463  A9 11 0E 01 F4                  test eax, 0xf4010e11
009E6468  75 49                           jne 0x1409e64b3
009E646A  8B C7                           mov eax, edi
009E646C  25 60 00 00 FF                  and eax, 0xff000060
009E6471  FF C8                           dec eax
009E6473  23 C7                           and eax, edi
009E6475  A9 60 00 00 01                  test eax, 0x1000060
009E647A  75 41                           jne 0x1409e64bd
009E647C  48 8B 8A 80 00 00 00            mov rcx, qword ptr [rdx + 0x80]
009E6483  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
009E6488  48 8B 82 F0 03 00 00            mov rax, qword ptr [rdx + 0x3f0]
009E648F  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
009E6494  48 85 C0                        test rax, rax
009E6497  74 3B                           je 0x1409e64d4
009E6499  A8 01                           test al, 1
009E649B  75 37                           jne 0x1409e64d4
009E649D  48 8D 14 08                     lea rdx, [rax + rcx]
009E64A1  49 3B D0                        cmp rdx, r8
009E64A4  77 21                           ja 0x1409e64c7
009E64A6  48 3B D1                        cmp rdx, rcx
009E64A9  72 1C                           jb 0x1409e64c7
009E64AB  EB 36                           jmp 0x1409e64e3
009E64AD  E8 1E 3B EB FF                  call 0x140899fd0
009E64B2  CC                              int3
009E64B3  B8 0D 00 00 C0                  mov eax, 0xc000000d
009E64B8  E9 F5 02 00 00                  jmp 0x1409e67b2
009E64BD  B8 0D 00 00 C0                  mov eax, 0xc000000d
009E64C2  E9 EB 02 00 00                  jmp 0x1409e67b2
009E64C7  41 8A 00                        mov al, byte ptr [r8]
009E64CA  8B 7C 24 28                     mov edi, dword ptr [rsp + 0x28]
009E64CE  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
009E64D2  EB D7                           jmp 0x1409e64ab
009E64D4  B8 0D 00 00 C0                  mov eax, 0xc000000d
009E64D9  E9 D4 02 00 00                  jmp 0x1409e67b2
009E64DE  E9 CF 02 00 00                  jmp 0x1409e67b2
009E64E3  41 F6 C1 01                     test r9b, 1
009E64E7  0F 84 E0 04 00 00               je 0x1409e69cd
009E64ED  48 8B 8C 24 70 01 00 00         mov rcx, qword ptr [rsp + 0x170]
009E64F5  E8 A6 EB 83 FF                  call 0x1402250a0
009E64FA  0F 10 80 C8 03 00 00            movups xmm0, xmmword ptr [rax + 0x3c8]
009E6501  F3 0F 7F 44 24 68               movdqu xmmword ptr [rsp + 0x68], xmm0
009E6507  0F 10 35 DA 59 16 00            movups xmm6, xmmword ptr [rip + 0x1659da]
009E650E  0F 11 74 24 30                  movups xmmword ptr [rsp + 0x30], xmm6
009E6513  66 0F 6F C6                     movdqa xmm0, xmm6
009E6517  66 44 0F C5 F6 01               pextrw r14d, xmm6, 1
009E651D  66 41 0F 7E F4                  movd r12d, xmm6
009E6522  66 0F 73 D8 08                  psrldq xmm0, 8
009E6527  41 F6 C1 02                     test r9b, 2
009E652B  75 18                           jne 0x1409e6545
009E652D  48 8B 88 E0 03 00 00            mov rcx, qword ptr [rax + 0x3e0]
009E6534  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
009E6539  0F B7 80 DA 03 00 00            movzx eax, word ptr [rax + 0x3da]
009E6540  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
009E6545  66 0F D6 44 24 40               movq qword ptr [rsp + 0x40], xmm0
009E654B  48 8D 4E 50                     lea rcx, [rsi + 0x50]
009E654F  48 8D 94 24 88 00 00 00         lea rdx, [rsp + 0x88]
009E6557  E8 CC 06 00 00                  call 0x1409e6c28
009E655C  85 C0                           test eax, eax
009E655E  0F 88 4E 02 00 00               js 0x1409e67b2
009E6564  48 8D 4E 60                     lea rcx, [rsi + 0x60]
009E6568  48 8D 94 24 98 00 00 00         lea rdx, [rsp + 0x98]
009E6570  E8 B3 06 00 00                  call 0x1409e6c28
009E6575  85 C0                           test eax, eax
009E6577  0F 88 35 02 00 00               js 0x1409e67b2
009E657D  48 8D 4E 70                     lea rcx, [rsi + 0x70]
009E6581  48 8D 94 24 A8 00 00 00         lea rdx, [rsp + 0xa8]
009E6589  E8 9A 06 00 00                  call 0x1409e6c28
009E658E  85 C0                           test eax, eax
009E6590  0F 88 1C 02 00 00               js 0x1409e67b2
009E6596  48 8D 8E B0 00 00 00            lea rcx, [rsi + 0xb0]
009E659D  48 8D 94 24 B8 00 00 00         lea rdx, [rsp + 0xb8]
009E65A5  E8 7E 06 00 00                  call 0x1409e6c28
009E65AA  85 C0                           test eax, eax
009E65AC  0F 88 00 02 00 00               js 0x1409e67b2
009E65B2  48 8D 8E C0 00 00 00            lea rcx, [rsi + 0xc0]
009E65B9  48 8D 94 24 C8 00 00 00         lea rdx, [rsp + 0xc8]
009E65C1  E8 62 06 00 00                  call 0x1409e6c28
009E65C6  85 C0                           test eax, eax
009E65C8  0F 88 E4 01 00 00               js 0x1409e67b2
009E65CE  48 8D 8E D0 00 00 00            lea rcx, [rsi + 0xd0]
009E65D5  48 8D 94 24 D8 00 00 00         lea rdx, [rsp + 0xd8]
009E65DD  E8 46 06 00 00                  call 0x1409e6c28
009E65E2  85 C0                           test eax, eax
009E65E4  0F 88 C8 01 00 00               js 0x1409e67b2
009E65EA  4D 85 FF                        test r15, r15
009E65ED  0F 85 68 05 00 00               jne 0x1409e6b5b
009E65F3  49 8D 7D 04                     lea rdi, [r13 + 4]
009E65F7  48 8D 8E 10 04 00 00            lea rcx, [rsi + 0x410]
009E65FE  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
009E6603  E8 20 06 00 00                  call 0x1409e6c28
009E6608  85 C0                           test eax, eax
009E660A  0F 88 A2 01 00 00               js 0x1409e67b2
009E6610  4D 85 FF                        test r15, r15
009E6613  0F 85 60 05 00 00               jne 0x1409e6b79
009E6619  0F 57 C0                        xorps xmm0, xmm0
009E661C  0F 11 84 24 E8 00 00 00         movups xmmword ptr [rsp + 0xe8], xmm0
009E6624  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
009E662C  48 C1 E8 10                     shr rax, 0x10
009E6630  0F B7 C8                        movzx ecx, ax
009E6633  0F B7 44 24 7A                  movzx eax, word ptr [rsp + 0x7a]
009E6638  48 03 C8                        add rcx, rax
009E663B  0F B7 84 24 DA 00 00 00         movzx eax, word ptr [rsp + 0xda]
009E6643  48 03 C8                        add rcx, rax
009E6646  0F B7 84 24 CA 00 00 00         movzx eax, word ptr [rsp + 0xca]
009E664E  48 03 C8                        add rcx, rax
009E6651  0F B7 84 24 BA 00 00 00         movzx eax, word ptr [rsp + 0xba]
009E6659  48 03 C8                        add rcx, rax
009E665C  0F B7 84 24 AA 00 00 00         movzx eax, word ptr [rsp + 0xaa]
009E6664  48 03 C8                        add rcx, rax
009E6667  0F B7 84 24 9A 00 00 00         movzx eax, word ptr [rsp + 0x9a]
009E666F  48 03 C8                        add rcx, rax
009E6672  0F B7 84 24 8A 00 00 00         movzx eax, word ptr [rsp + 0x8a]
009E667A  48 03 C8                        add rcx, rax
009E667D  41 0F B7 C6                     movzx eax, r14w
009E6681  48 03 C8                        add rcx, rax
009E6684  44 0F B7 6C 24 6A               movzx r13d, word ptr [rsp + 0x6a]
009E668A  49 81 C5 51 04 00 00            add r13, 0x451
009E6691  4C 03 E9                        add r13, rcx
009E6694  49 83 E5 FE                     and r13, 0xfffffffffffffffe
009E6698  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
009E669D  4D 85 FF                        test r15, r15
009E66A0  0F 85 F0 04 00 00               jne 0x1409e6b96
009E66A6  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
009E66AB  49 03 CD                        add rcx, r13
009E66AE  48 83 CA FF                     or rdx, 0xffffffffffffffff
009E66B2  49 3B CD                        cmp rcx, r13
009E66B5  48 0F 43 D1                     cmovae rdx, rcx
009E66B9  45 1B F6                        sbb r14d, r14d
009E66BC  41 81 E6 95 00 00 C0            and r14d, 0xc0000095
009E66C3  49 3B CD                        cmp rcx, r13
009E66C6  0F 82 4C 05 00 00               jb 0x1409e6c18
009E66CC  B9 41 00 00 00                  mov ecx, 0x41
009E66D1  41 B8 50 73 50 62               mov r8d, 0x62507350
009E66D7  E8 14 BA 19 00                  call 0x140b820f0
009E66DC  48 8B F8                        mov rdi, rax
009E66DF  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
009E66E4  48 85 C0                        test rax, rax
009E66E7  0F 84 D2 04 00 00               je 0x1409e6bbf
009E66ED  B9 08 00 00 00                  mov ecx, 8
009E66F2  8D 51 78                        lea edx, [rcx + 0x78]
009E66F5  0F 10 06                        movups xmm0, xmmword ptr [rsi]
009E66F8  0F 11 00                        movups xmmword ptr [rax], xmm0
009E66FB  0F 10 4E 10                     movups xmm1, xmmword ptr [rsi + 0x10]
009E66FF  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
009E6703  0F 10 46 20                     movups xmm0, xmmword ptr [rsi + 0x20]
009E6707  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
009E670B  0F 10 4E 30                     movups xmm1, xmmword ptr [rsi + 0x30]
009E670F  0F 11 48 30                     movups xmmword ptr [rax + 0x30], xmm1
009E6713  0F 10 46 40                     movups xmm0, xmmword ptr [rsi + 0x40]
009E6717  0F 11 40 40                     movups xmmword ptr [rax + 0x40], xmm0
009E671B  0F 10 4E 50                     movups xmm1, xmmword ptr [rsi + 0x50]
009E671F  0F 11 48 50                     movups xmmword ptr [rax + 0x50], xmm1
009E6723  0F 10 46 60                     movups xmm0, xmmword ptr [rsi + 0x60]
009E6727  0F 11 40 60                     movups xmmword ptr [rax + 0x60], xmm0
009E672B  48 03 C2                        add rax, rdx
009E672E  0F 10 4E 70                     movups xmm1, xmmword ptr [rsi + 0x70]
009E6732  0F 11 48 F0                     movups xmmword ptr [rax - 0x10], xmm1
009E6736  48 03 F2                        add rsi, rdx
009E6739  48 83 E9 01                     sub rcx, 1
009E673D  75 B6                           jne 0x1409e66f5
009E673F  0F 10 06                        movups xmm0, xmmword ptr [rsi]
009E6742  0F 11 00                        movups xmmword ptr [rax], xmm0
009E6745  0F 10 4E 10                     movups xmm1, xmmword ptr [rsi + 0x10]
009E6749  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
009E674D  0F 10 46 20                     movups xmm0, xmmword ptr [rsi + 0x20]
009E6751  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
009E6755  0F 10 4E 30                     movups xmm1, xmmword ptr [rsi + 0x30]
009E6759  0F 11 48 30                     movups xmmword ptr [rax + 0x30], xmm1
009E675D  0F 10 46 40                     movups xmm0, xmmword ptr [rsi + 0x40]
009E6761  0F 11 40 40                     movups xmmword ptr [rax + 0x40], xmm0
009E6765  8B 44 24 20                     mov eax, dword ptr [rsp + 0x20]
009E6769  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
009E676E  EB 30                           jmp 0x1409e67a0
009E6770  44 8B F0                        mov r14d, eax
009E6773  33 DB                           xor ebx, ebx
009E6775  4C 8B BC 24 60 01 00 00         mov r15, qword ptr [rsp + 0x160]
009E677D  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
009E6782  8B 44 24 28                     mov eax, dword ptr [rsp + 0x28]
009E6786  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
009E678B  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
009E6790  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
009E6795  44 0F B7 64 24 30               movzx r12d, word ptr [rsp + 0x30]
009E679B  0F 10 74 24 30                  movups xmm6, xmmword ptr [rsp + 0x30]
009E67A0  45 85 F6                        test r14d, r14d
009E67A3  79 29                           jns 0x1409e67ce
009E67A5  33 D2                           xor edx, edx
009E67A7  48 8B CF                        mov rcx, rdi
009E67AA  E8 C1 C0 19 00                  call 0x140b82870
009E67AF  41 8B C6                        mov eax, r14d
009E67B2  0F 28 B4 24 00 01 00 00         movaps xmm6, xmmword ptr [rsp + 0x100]
009E67BA  48 81 C4 10 01 00 00            add rsp, 0x110
009E67C1  41 5F                           pop r15
009E67C3  41 5E                           pop r14
009E67C5  41 5D                           pop r13
009E67C7  41 5C                           pop r12
009E67C9  5F                              pop rdi
009E67CA  5E                              pop rsi
009E67CB  5B                              pop rbx
009E67CC  C3                              ret
009E67CD  CC                              int3
009E67CE  89 47 08                        mov dword ptr [rdi + 8], eax
009E67D1  44 89 6F 04                     mov dword ptr [rdi + 4], r13d
009E67D5  44 89 2F                        mov dword ptr [rdi], r13d
009E67D8  48 8D 87 50 04 00 00            lea rax, [rdi + 0x450]
009E67DF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009E67E4  4D 85 FF                        test r15, r15
009E67E7  0F 85 DC 03 00 00               jne 0x1409e6bc9
009E67ED  48 8D 57 38                     lea rdx, [rdi + 0x38]
009E67F1  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
009E67F6  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
009E67FB  E8 94 04 00 00                  call 0x1409e6c94
009E6800  44 8B F0                        mov r14d, eax
009E6803  85 C0                           test eax, eax
009E6805  78 9E                           js 0x1409e67a5
009E6807  48 8D 57 50                     lea rdx, [rdi + 0x50]
009E680B  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
009E6810  48 8D 8C 24 88 00 00 00         lea rcx, [rsp + 0x88]
009E6818  E8 77 04 00 00                  call 0x1409e6c94
009E681D  44 8B F0                        mov r14d, eax
009E6820  85 C0                           test eax, eax
009E6822  78 81                           js 0x1409e67a5
009E6824  48 8D 57 60                     lea rdx, [rdi + 0x60]
009E6828  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
009E682D  48 8D 8C 24 98 00 00 00         lea rcx, [rsp + 0x98]
009E6835  E8 5A 04 00 00                  call 0x1409e6c94
009E683A  44 8B F0                        mov r14d, eax
009E683D  85 C0                           test eax, eax
009E683F  0F 88 60 FF FF FF               js 0x1409e67a5
009E6845  48 8D 57 70                     lea rdx, [rdi + 0x70]
009E6849  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
009E684E  48 8D 8C 24 A8 00 00 00         lea rcx, [rsp + 0xa8]
009E6856  E8 39 04 00 00                  call 0x1409e6c94
009E685B  44 8B F0                        mov r14d, eax
009E685E  85 C0                           test eax, eax
009E6860  0F 88 3F FF FF FF               js 0x1409e67a5
009E6866  48 8D 97 B0 00 00 00            lea rdx, [rdi + 0xb0]
009E686D  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
009E6872  48 8D 8C 24 B8 00 00 00         lea rcx, [rsp + 0xb8]
009E687A  E8 15 04 00 00                  call 0x1409e6c94
009E687F  44 8B F0                        mov r14d, eax
009E6882  85 C0                           test eax, eax
009E6884  0F 88 1B FF FF FF               js 0x1409e67a5
009E688A  48 8D 97 C0 00 00 00            lea rdx, [rdi + 0xc0]
009E6891  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
009E6896  48 8D 8C 24 C8 00 00 00         lea rcx, [rsp + 0xc8]
009E689E  E8 F1 03 00 00                  call 0x1409e6c94
009E68A3  44 8B F0                        mov r14d, eax
009E68A6  85 C0                           test eax, eax
009E68A8  0F 88 F7 FE FF FF               js 0x1409e67a5
009E68AE  48 8D 97 D0 00 00 00            lea rdx, [rdi + 0xd0]
009E68B5  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
009E68BA  48 8D 8C 24 D8 00 00 00         lea rcx, [rsp + 0xd8]
009E68C2  E8 CD 03 00 00                  call 0x1409e6c94
009E68C7  44 8B F0                        mov r14d, eax
009E68CA  85 C0                           test eax, eax
009E68CC  0F 88 D3 FE FF FF               js 0x1409e67a5
009E68D2  48 8D 97 10 04 00 00            lea rdx, [rdi + 0x410]
009E68D9  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
009E68DE  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
009E68E3  E8 AC 03 00 00                  call 0x1409e6c94
009E68E8  4D 85 FF                        test r15, r15
009E68EB  0F 85 F3 02 00 00               jne 0x1409e6be4
009E68F1  0F 57 C0                        xorps xmm0, xmm0
009E68F4  0F 11 87 20 04 00 00            movups xmmword ptr [rdi + 0x420], xmm0
009E68FB  F3 0F 7F B7 E0 00 00 00         movdqu xmmword ptr [rdi + 0xe0], xmm6
009E6903  48 85 F6                        test rsi, rsi
009E6906  48 8B 74 24 20                  mov rsi, qword ptr [rsp + 0x20]
009E690B  0F 85 32 01 00 00               jne 0x1409e6a43
009E6911  48 89 9F 30 04 00 00            mov qword ptr [rdi + 0x430], rbx
009E6918  89 9F 38 04 00 00               mov dword ptr [rdi + 0x438], ebx
009E691E  4D 85 FF                        test r15, r15
009E6921  0F 85 8F 9D 14 00               jne 0x140b306b6
009E6927  48 8B C7                        mov rax, rdi
009E692A  48 2B C6                        sub rax, rsi
009E692D  4C 03 E8                        add r13, rax
009E6930  0F 85 02 02 00 00               jne 0x1409e6b38
009E6936  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
009E693B  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
009E6940  48 8B CE                        mov rcx, rsi
009E6943  E8 F8 FE CD FF                  call 0x1406c6840
009E6948  EB 0F                           jmp 0x1409e6959
009E694A  44 8B F0                        mov r14d, eax
009E694D  33 DB                           xor ebx, ebx
009E694F  48 8B 74 24 20                  mov rsi, qword ptr [rsp + 0x20]
009E6954  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
009E6959  45 85 F6                        test r14d, r14d
009E695C  0F 88 43 FE FF FF               js 0x1409e67a5
009E6962  44 8B BC 24 68 01 00 00         mov r15d, dword ptr [rsp + 0x168]
009E696A  41 8B C7                        mov eax, r15d
009E696D  24 03                           and al, 3
009E696F  3C 01                           cmp al, 1
009E6971  74 18                           je 0x1409e698b
009E6973  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
009E6978  48 8B CE                        mov rcx, rsi
009E697B  E8 90 03 00 00                  call 0x1409e6d10
009E6980  44 8B F0                        mov r14d, eax
009E6983  85 C0                           test eax, eax
009E6985  0F 88 1A FE FF FF               js 0x1409e67a5
009E698B  41 F6 C7 01                     test r15b, 1
009E698F  74 10                           je 0x1409e69a1
009E6991  48 89 5F 10                     mov qword ptr [rdi + 0x10], rbx
009E6995  48 89 5F 20                     mov qword ptr [rdi + 0x20], rbx
009E6999  48 89 5F 28                     mov qword ptr [rdi + 0x28], rbx
009E699D  48 89 5F 30                     mov qword ptr [rdi + 0x30], rbx
009E69A1  48 89 B7 80 00 00 00            mov qword ptr [rdi + 0x80], rsi
009E69A8  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
009E69AD  48 89 87 F0 03 00 00            mov qword ptr [rdi + 0x3f0], rax
009E69B4  48 89 9F F8 03 00 00            mov qword ptr [rdi + 0x3f8], rbx
009E69BB  48 8B 84 24 50 01 00 00         mov rax, qword ptr [rsp + 0x150]
009E69C3  48 89 38                        mov qword ptr [rax], rdi
009E69C6  33 C0                           xor eax, eax
009E69C8  E9 E5 FD FF FF                  jmp 0x1409e67b2
009E69CD  48 8D 4E 38                     lea rcx, [rsi + 0x38]
009E69D1  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
009E69D6  E8 4D 02 00 00                  call 0x1409e6c28
009E69DB  8B C8                           mov ecx, eax
009E69DD  85 C0                           test eax, eax
009E69DF  0F 88 CD FD FF FF               js 0x1409e67b2
009E69E5  B8 08 02 00 00                  mov eax, 0x208
009E69EA  66 39 44 24 68                  cmp word ptr [rsp + 0x68], ax
009E69EF  0F 83 23 02 00 00               jae 0x1409e6c18
009E69F5  66 89 44 24 6A                  mov word ptr [rsp + 0x6a], ax
009E69FA  0F 10 86 E0 00 00 00            movups xmm0, xmmword ptr [rsi + 0xe0]
009E6A01  F3 0F 7F 44 24 30               movdqu xmmword ptr [rsp + 0x30], xmm0
009E6A07  EB 05                           jmp 0x1409e6a0e
009E6A09  E9 A4 FD FF FF                  jmp 0x1409e67b2
009E6A0E  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
009E6A13  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
009E6A18  48 85 FF                        test rdi, rdi
009E6A1B  0F 85 81 00 00 00               jne 0x1409e6aa2
009E6A21  44 0F B7 64 24 30               movzx r12d, word ptr [rsp + 0x30]
009E6A27  66 45 85 E4                     test r12w, r12w
009E6A2B  0F 85 E7 01 00 00               jne 0x1409e6c18
009E6A31  44 8B F3                        mov r14d, ebx
009E6A34  66 89 5C 24 32                  mov word ptr [rsp + 0x32], bx
009E6A39  0F 10 74 24 30                  movups xmm6, xmmword ptr [rsp + 0x30]
009E6A3E  E9 08 FB FF FF                  jmp 0x1409e654b
009E6A43  48 89 B7 E8 00 00 00            mov qword ptr [rdi + 0xe8], rsi
009E6A4A  45 0F B7 C4                     movzx r8d, r12w
009E6A4E  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
009E6A53  48 8B CE                        mov rcx, rsi
009E6A56  E8 E5 FD CD FF                  call 0x1406c6840
009E6A5B  EB 22                           jmp 0x1409e6a7f
009E6A5D  44 8B F0                        mov r14d, eax
009E6A60  33 DB                           xor ebx, ebx
009E6A62  4C 8B BC 24 60 01 00 00         mov r15, qword ptr [rsp + 0x160]
009E6A6A  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
009E6A6F  48 8B 74 24 20                  mov rsi, qword ptr [rsp + 0x20]
009E6A74  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
009E6A79  44 0F B7 64 24 30               movzx r12d, word ptr [rsp + 0x30]
009E6A7F  45 85 F6                        test r14d, r14d
009E6A82  0F 88 1D FD FF FF               js 0x1409e67a5
009E6A88  48 85 F6                        test rsi, rsi
009E6A8B  0F 84 80 FE FF FF               je 0x1409e6911
009E6A91  41 0F B7 C4                     movzx eax, r12w
009E6A95  48 03 F0                        add rsi, rax
009E6A98  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
009E6A9D  E9 6F FE FF FF                  jmp 0x1409e6911
009E6AA2  44 0F B7 64 24 30               movzx r12d, word ptr [rsp + 0x30]
009E6AA8  45 0F B7 F4                     movzx r14d, r12w
009E6AAC  66 44 89 64 24 32               mov word ptr [rsp + 0x32], r12w
009E6AB2  66 45 85 E4                     test r12w, r12w
009E6AB6  74 38                           je 0x1409e6af0
009E6AB8  4A 8D 14 27                     lea rdx, [rdi + r12]
009E6ABC  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
009E6AC6  48 3B D0                        cmp rdx, rax
009E6AC9  77 05                           ja 0x1409e6ad0
009E6ACB  48 3B D7                        cmp rdx, rdi
009E6ACE  73 20                           jae 0x1409e6af0
009E6AD0  8A 00                           mov al, byte ptr [rax]
009E6AD2  8B 44 24 28                     mov eax, dword ptr [rsp + 0x28]
009E6AD6  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
009E6ADA  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
009E6ADF  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
009E6AE4  44 0F B7 74 24 32               movzx r14d, word ptr [rsp + 0x32]
009E6AEA  44 0F B7 64 24 30               movzx r12d, word ptr [rsp + 0x30]
009E6AF0  EB 37                           jmp 0x1409e6b29
009E6AF2  8B C8                           mov ecx, eax
009E6AF4  33 DB                           xor ebx, ebx
009E6AF6  4C 8B BC 24 60 01 00 00         mov r15, qword ptr [rsp + 0x160]
009E6AFE  48 8B B4 24 58 01 00 00         mov rsi, qword ptr [rsp + 0x158]
009E6B06  8B 44 24 28                     mov eax, dword ptr [rsp + 0x28]
009E6B0A  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
009E6B0E  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
009E6B13  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
009E6B18  44 0F B7 74 24 32               movzx r14d, word ptr [rsp + 0x32]
009E6B1E  44 0F B7 64 24 30               movzx r12d, word ptr [rsp + 0x30]
009E6B24  4C 8B 6C 24 50                  mov r13, qword ptr [rsp + 0x50]
009E6B29  85 C9                           test ecx, ecx
009E6B2B  0F 89 08 FF FF FF               jns 0x1409e6a39
009E6B31  8B C1                           mov eax, ecx
009E6B33  E9 7A FC FF FF                  jmp 0x1409e67b2
009E6B38  4D 8B C5                        mov r8, r13
009E6B3B  33 D2                           xor edx, edx
009E6B3D  48 8B CE                        mov rcx, rsi
009E6B40  E8 FB 00 CE FF                  call 0x1406c6c40
009E6B45  48 85 F6                        test rsi, rsi
009E6B48  0F 84 E8 FD FF FF               je 0x1409e6936
009E6B4E  49 03 F5                        add rsi, r13
009E6B51  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
009E6B56  E9 DB FD FF FF                  jmp 0x1409e6936
009E6B5B  49 8D 7F 04                     lea rdi, [r15 + 4]
009E6B5F  8B 07                           mov eax, dword ptr [rdi]
009E6B61  A8 02                           test al, 2
009E6B63  0F 84 8E FA FF FF               je 0x1409e65f7
009E6B69  41 0F 10 47 08                  movups xmm0, xmmword ptr [r15 + 8]
009E6B6E  F3 0F 7F 44 24 78               movdqu xmmword ptr [rsp + 0x78], xmm0
009E6B74  E9 97 FA FF FF                  jmp 0x1409e6610
009E6B79  8B 07                           mov eax, dword ptr [rdi]
009E6B7B  A8 04                           test al, 4
009E6B7D  0F 84 96 FA FF FF               je 0x1409e6619
009E6B83  41 0F 10 47 18                  movups xmm0, xmmword ptr [r15 + 0x18]
009E6B88  F3 0F 7F 84 24 E8 00 00 00      movdqu xmmword ptr [rsp + 0xe8], xmm0
009E6B91  E9 8E FA FF FF                  jmp 0x1409e6624
009E6B96  8B 07                           mov eax, dword ptr [rdi]
009E6B98  A8 01                           test al, 1
009E6B9A  0F 84 06 FB FF FF               je 0x1409e66a6
009E6BA0  41 8B 4F 30                     mov ecx, dword ptr [r15 + 0x30]
009E6BA4  49 8D 45 03                     lea rax, [r13 + 3]
009E6BA8  48 83 E0 FC                     and rax, 0xfffffffffffffffc
009E6BAC  4C 8D 2C C8                     lea r13, [rax + rcx*8]
009E6BB0  4C 3B E8                        cmp r13, rax
009E6BB3  72 63                           jb 0x1409e6c18
009E6BB5  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
009E6BBA  E9 E7 FA FF FF                  jmp 0x1409e66a6
009E6BBF  B8 9A 00 00 C0                  mov eax, 0xc000009a
009E6BC4  E9 E9 FB FF FF                  jmp 0x1409e67b2
009E6BC9  41 8B 47 04                     mov eax, dword ptr [r15 + 4]
009E6BCD  A8 08                           test al, 8
009E6BCF  0F 84 18 FC FF FF               je 0x1409e67ed
009E6BD5  41 8B 47 34                     mov eax, dword ptr [r15 + 0x34]
009E6BD9  89 87 3C 04 00 00               mov dword ptr [rdi + 0x43c], eax
009E6BDF  E9 09 FC FF FF                  jmp 0x1409e67ed
009E6BE4  41 8B 47 04                     mov eax, dword ptr [r15 + 4]
009E6BE8  A8 04                           test al, 4
009E6BEA  0F 84 01 FD FF FF               je 0x1409e68f1
009E6BF0  48 8D 97 20 04 00 00            lea rdx, [rdi + 0x420]
009E6BF7  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
009E6BFC  48 8D 8C 24 E8 00 00 00         lea rcx, [rsp + 0xe8]
009E6C04  E8 8B 00 00 00                  call 0x1409e6c94
009E6C09  41 8B 47 38                     mov eax, dword ptr [r15 + 0x38]
009E6C0D  89 87 40 04 00 00               mov dword ptr [rdi + 0x440], eax
009E6C13  E9 E3 FC FF FF                  jmp 0x1409e68fb
009E6C18  B8 0D 00 00 C0                  mov eax, 0xc000000d
009E6C1D  E9 90 FB FF FF                  jmp 0x1409e67b2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspCaptureUserProcessParameters(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m120;
    unsigned int v_stack_m128;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m60;
    unsigned __int16 v_stack_m6E;
    unsigned __int64 v_stack_m70;
    unsigned __int16 v_stack_m7E;
    unsigned __int64 v_stack_m80;
    unsigned __int16 v_stack_m8E;
    unsigned __int64 v_stack_m90;
    unsigned __int16 v_stack_m9E;
    unsigned __int64 v_stack_mA0;
    unsigned __int16 v_stack_mAE;
    unsigned __int64 v_stack_mB0;
    unsigned __int16 v_stack_mBE;
    unsigned __int64 v_stack_mC0;
    unsigned __int16 v_stack_mCE;
    unsigned __int64 v_stack_mD0;
    unsigned __int16 v_stack_mDE;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p150;
    unsigned __int64 v_stack_p158;
    unsigned __int64 v_stack_p160;
    unsigned int v_stack_p168;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int16 v_stack_p32;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int16 v_stack_p6A;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pD8;
    unsigned __int64 v_stack_pE8;

    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (272);
    *(unsigned __int64 *)(v_rsp - 72) = v_xmm6;
    v_stack_mF8 = a3;
    *(unsigned __int64 *)(v_rsp - 160) = v_xmm0;
    v_stack_mE0 = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 128) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 192) = v_xmm1;
    v_rbx = 0;
    v_stack_mE8 = 0;
    *(unsigned __int64 *)(v_rsp - 176) = v_xmm0;
    v_stack_mD0 = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 112) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 144) = v_xmm1;
    if ((((unsigned __int8)(a2)) & (3)) != 0) goto loc_009E64AD;
    if (a2 < a3) { a3 = a2; }
    v_stack_m128 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8)));
    v_stack_m120 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8)));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8))))) ^ (1));
    if ((((unsigned int)(result)) & (0xF4010E11ULL)) != 0) goto loc_009E64B3;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8))))) & (0xFF000060ULL));
    result = (unsigned int)((result) - 1);
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8)))));
    if ((((unsigned int)(result)) & (0x1000060ULL)) != 0) goto loc_009E64BD;
    v_stack_mE8 = *(unsigned __int64 *)(a2 + 128);
    v_stack_m100 = *(unsigned __int64 *)(a2 + 1008);
    if (*(unsigned __int64 *)(a2 + 1008) == 0) goto loc_009E64D4;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2 + 1008))) & (1)) != 0) goto loc_009E64D4;
    if ((*(unsigned __int64 *)(a2 + 1008) + *(unsigned __int64 *)(a2 + 128) * 1) > a3) goto loc_009E64C7;
    if ((*(unsigned __int64 *)(a2 + 1008) + *(unsigned __int64 *)(a2 + 128) * 1) < (*(unsigned __int64 *)(a2 + 128))) goto loc_009E64C7;
loc_009E64AB:
    goto loc_009E64E3;
loc_009E64AD:
    result = ExRaiseDatatypeMisalignment(*(unsigned __int64 *)(a2 + 128), *(unsigned __int64 *)(a2 + 1008) + *(unsigned __int64 *)(a2 + 128) * 1, a3, a4);
loc_009E64B3:
    goto loc_009E67B2;
loc_009E64BD:
    goto loc_009E67B2;
loc_009E64C7:
    v_stack_m128 = (unsigned int)((unsigned int)(v_stack_m120));
    goto loc_009E64AB;
loc_009E64D4:
    goto loc_009E67B2;
loc_009E64E3:
    if ((((unsigned __int8)(a4)) & (1)) == 0) goto loc_009E69CD;
    result = PsGetServerSiloGlobals(a5, *(unsigned __int64 *)(a2 + 1008) + *(unsigned __int64 *)(a2 + 128) * 1, a3, a4);
    v_stack_mE0 = v_xmm0;
    v_stack_m118 = v_xmm6;
    if ((((unsigned __int8)(a4)) & (2)) == 0) {
        a1 = *(unsigned __int64 *)(result + 992);
        v_stack_mE8 = a1;
        result = *(unsigned __int16 *)(result + 986);
        v_stack_m100 = result;
    }
    v_stack_m108 = v_xmm0;
loc_009E654B:
    result = PspCaptureAndValidateUnicodeString(a2 + 80, v_stack_mC0, a3, a4);
    if (sign_flag) goto loc_009E67B2;
    result = PspCaptureAndValidateUnicodeString(a2 + 96, v_stack_mB0, a3, a4);
    if (sign_flag) goto loc_009E67B2;
    result = PspCaptureAndValidateUnicodeString(a2 + 112, v_stack_mA0, a3, a4);
    if (sign_flag) goto loc_009E67B2;
    result = PspCaptureAndValidateUnicodeString(a2 + 176, v_stack_m90, a3, a4);
    if (sign_flag) goto loc_009E67B2;
    result = PspCaptureAndValidateUnicodeString(a2 + 192, v_stack_m80, a3, a4);
    if (sign_flag) goto loc_009E67B2;
    result = PspCaptureAndValidateUnicodeString(a2 + 208, v_stack_m70, a3, a4);
    if (sign_flag) goto loc_009E67B2;
    if (a3 != 0) goto loc_009E6B5B;
loc_009E65F7:
    result = PspCaptureAndValidateUnicodeString(a2 + 1040, v_stack_mD0, a3, a4);
    if (sign_flag) goto loc_009E67B2;
loc_009E6610:
    if (a3 != 0) goto loc_009E6B79;
loc_009E6619:
    v_stack_m60 = v_xmm0;
loc_009E6624:
    result = (v_stack_m60) >> (16);
    a1 = ((unsigned __int16)(result)) + (v_stack_mCE);
    a1 = (a1) + (v_stack_m6E);
    a1 = (a1) + (v_stack_m7E);
    a1 = (a1) + (v_stack_m8E);
    a1 = (a1) + (v_stack_m9E);
    a1 = (a1) + (v_stack_mAE);
    a1 = (a1) + (v_stack_mBE);
    a1 = (a1) + ((unsigned __int16)(v_r14));
    v_r13 = (v_stack_mDE) + (0x451ULL);
    v_r13 = (v_r13) + (a1);
    v_r13 = (v_r13) & (-2);
    v_stack_mF0 = v_r13;
    if (a3 != 0) goto loc_009E6B96;
loc_009E66A6:
    a1 = (v_stack_m100) + (v_r13);
    a2 = (v_stack_mD0) | (-1);
    if (a1 >= v_r13) { a2 = a1; }
    v_r14 = (unsigned int)((v_r14) & (0xC0000095ULL));
    if (a1 < v_r13) goto loc_009E6C18;
    result = ExAllocatePool2(65, a2, (unsigned int)(0x62507350ULL), a4);
    v_stack_mF8 = result;
    if (result == 0) goto loc_009E6BBF;
loc_009E66F5:
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm1;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    *(unsigned __int64 *)(result + 48) = v_xmm1;
    *(unsigned __int64 *)(result + 64) = v_xmm0;
    *(unsigned __int64 *)(result + 80) = v_xmm1;
    *(unsigned __int64 *)(result + 96) = v_xmm0;
    result = (result) + (8 + 120);
    *(unsigned __int64 *)(result - 16) = v_xmm1;
    v_rsi = (a2) + (8 + 120);
    a1 = (8) - (1);
    if (condition_is_not_equal) goto loc_009E66F5;
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm1;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    *(unsigned __int64 *)(result + 48) = v_xmm1;
    *(unsigned __int64 *)(result + 64) = v_xmm0;
    goto loc_009E67A0;
loc_009E67A0:
    if (!sign_flag) goto loc_009E67CE;
loc_009E67A5:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(0x62507350ULL), a4);
loc_009E67B2:
    v_rsp = (v_rsp) + (272);
    return (unsigned int)((unsigned int)(v_r14));
loc_009E67CE:
    *(unsigned int *)(result + 8) = (unsigned int)((unsigned int)((unsigned int)(v_r14)));
    *(unsigned int *)(result + 4) = (unsigned int)(v_r13);
    *(unsigned int *)(result) = (unsigned int)(v_r13);
    v_stack_p20 = result + 1104;
    if (a3 != 0) goto loc_009E6BC9;
loc_009E67ED:
    result = PspCopyUnicodeString(v_stack_p68, result + 56, v_stack_p20, a4);
    if (sign_flag) goto loc_009E67A5;
    result = PspCopyUnicodeString(v_stack_p88, result + 80, v_stack_p20, a4);
    if (sign_flag) goto loc_009E67A5;
    result = PspCopyUnicodeString(v_stack_p98, result + 96, v_stack_p20, a4);
    if (sign_flag) goto loc_009E67A5;
    result = PspCopyUnicodeString(v_stack_pA8, result + 112, v_stack_p20, a4);
    if (sign_flag) goto loc_009E67A5;
    result = PspCopyUnicodeString(v_stack_pB8, result + 176, v_stack_p20, a4);
    if (sign_flag) goto loc_009E67A5;
    result = PspCopyUnicodeString(v_stack_pC8, result + 192, v_stack_p20, a4);
    if (sign_flag) goto loc_009E67A5;
    result = PspCopyUnicodeString(v_stack_pD8, result + 208, v_stack_p20, a4);
    if (sign_flag) goto loc_009E67A5;
    result = PspCopyUnicodeString(v_stack_p78, result + 1040, v_stack_p20, a4);
    if (a3 != 0) goto loc_009E6BE4;
loc_009E68F1:
    *(unsigned __int64 *)(result + 1056) = v_xmm0;
loc_009E68FB:
    *(unsigned __int64 *)(result + 224) = v_xmm6;
    if (v_stack_m108 != 0) goto loc_009E6A43;
loc_009E6911:
    *(unsigned __int64 *)(result + 1072) = 0;
    *(unsigned int *)(result + 1080) = 0;
    result = (result) - (v_stack_p20);
    v_r13 = (v_r13) + (result);
    if (condition_is_not_equal) goto loc_009E6B38;
loc_009E6936:
    result = memcpy(v_stack_p20, v_stack_p60, v_stack_p48, a4);
    goto loc_009E6959;
loc_009E6959:
    if (sign_flag) goto loc_009E67A5;
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p168)))) & (3));
    if (((unsigned __int8)(result)) == 1) goto loc_009E698B;
    result = PspValidateEnvironmentBlock(v_stack_p20, v_stack_p48, v_stack_p48, a4);
    if (sign_flag) goto loc_009E67A5;
loc_009E698B:
    if ((((unsigned __int8)((unsigned int)(v_stack_p168))) & (1)) != 0) {
        *(unsigned __int64 *)(result + 16) = 0;
        *(unsigned __int64 *)(result + 32) = 0;
        *(unsigned __int64 *)(result + 40) = 0;
        *(unsigned __int64 *)(result + 48) = 0;
    }
    *(unsigned __int64 *)(result + 128) = v_stack_p20;
    *(unsigned __int64 *)(result + 1008) = v_stack_p48;
    *(unsigned __int64 *)(result + 1016) = 0;
    *(unsigned __int64 *)(v_stack_p150) = result;
    result = 0;
    goto loc_009E67B2;
loc_009E69CD:
    result = PspCaptureAndValidateUnicodeString(v_stack_p20 + 56, v_stack_p68, v_stack_p48, a4);
    if (sign_flag) goto loc_009E67B2;
    if (v_stack_p68 >= 520) goto loc_009E6C18;
    v_stack_p6A = 520;
    v_stack_p30 = v_xmm0;
    goto loc_009E6A0E;
loc_009E6A0E:
    v_stack_p40 = v_stack_p38;
    if (v_stack_p38 != 0) goto loc_009E6AA2;
    if ((unsigned __int16)(v_stack_p30) != 0) goto loc_009E6C18;
    v_stack_p32 = 0;
loc_009E6A39:
    goto loc_009E654B;
loc_009E6A43:
    *(unsigned __int64 *)(v_stack_p38 + 232) = v_stack_p20;
    result = memcpy(v_stack_p20, v_stack_p40, (unsigned __int16)(v_stack_p30), a4);
    goto loc_009E6A7F;
loc_009E6A7F:
    if (sign_flag) goto loc_009E67A5;
    if (v_stack_p20 == 0) goto loc_009E6911;
    v_rsi = (v_stack_p20) + ((unsigned __int16)(v_stack_p30));
    v_stack_p20 = v_rsi;
    goto loc_009E6911;
loc_009E6AA2:
    v_stack_p32 = (unsigned __int16)(v_stack_p30);
    if ((unsigned __int16)(v_stack_p30) == 0) goto loc_009E6AF0;
    if ((v_stack_p38 + v_stack_p30 * 1) > ((unsigned __int16)(v_stack_p30))) goto loc_009E6AD0;
    result = (unsigned __int16)(v_stack_p30);
    v_r12 = v_stack_p30;
    v_r14 = (unsigned __int16)(v_stack_p30);
    if ((v_stack_p38 + v_stack_p30 * 1) < v_stack_p38) {
        result = *(unsigned __int8 *)((unsigned __int16)(v_stack_p30));
        result = v_stack_p28;
        v_stack_p20 = (unsigned int)(result);
        result = v_stack_p38;
        v_stack_p40 = result;
        v_r14 = v_stack_p32;
        v_r12 = v_stack_p30;
    }
    goto loc_009E6B29;
loc_009E6B29:
    if (!sign_flag) goto loc_009E6A39;
    goto loc_009E67B2;
loc_009E6B38:
    a2 = 0;
    result = memset(v_rsi, a2, v_r13, a4);
    if (v_rsi == 0) goto loc_009E6936;
    v_rsi = (v_rsi) + (v_r13);
    v_stack_p20 = v_rsi;
    goto loc_009E6936;
loc_009E6B5B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p168) + 4)))) & (2)) == 0) goto loc_009E65F7;
    v_stack_p78 = v_xmm0;
    goto loc_009E6610;
loc_009E6B79:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p168) + 4)))) & (4)) == 0) goto loc_009E6619;
    v_stack_pE8 = v_xmm0;
    goto loc_009E6624;
loc_009E6B96:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p168) + 4)))) & (1)) == 0) goto loc_009E66A6;
    result = (v_r13 + 3) & (-4);
    if ((result + (unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p168) + 48)) * 8) < result) goto loc_009E6C18;
    v_stack_p58 = result + (unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p168) + 48)) * 8;
    goto loc_009E66A6;
loc_009E6BBF:
    goto loc_009E67B2;
loc_009E6BC9:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p168) + 4)))) & (8)) == 0) goto loc_009E67ED;
    *(unsigned int *)((unsigned int)(v_stack_p168) + 4 + 1084) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p168) + 52)));
    goto loc_009E67ED;
loc_009E6BE4:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p168) + 4)))) & (4)) == 0) goto loc_009E68F1;
    result = PspCopyUnicodeString(v_stack_pE8, (unsigned int)(v_stack_p168) + 4 + 1056, v_stack_p20, a4);
    *(unsigned int *)((unsigned int)(v_stack_p168) + 4 + 1088) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p168) + 56)));
    goto loc_009E68FB;
loc_009E6C18:
    goto loc_009E67B2;
}
```

## 5. (Beta) C Style

```c
int64_t PspCaptureUserProcessParameters(int64_t Arg1, int64_t Arg2, void *Arg3, int32_t Arg4, int64_t Arg5)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint32_t v_stack_m120;
    uint32_t v_stack_m128;
    uint64_t v_stack_m48;
    uint64_t v_stack_m60;
    uint16_t v_stack_m6E;
    uint64_t v_stack_m70;
    uint16_t v_stack_m7E;
    uint64_t v_stack_m80;
    uint16_t v_stack_m8E;
    uint64_t v_stack_m90;
    uint16_t v_stack_m9E;
    uint64_t v_stack_mA0;
    uint16_t v_stack_mAE;
    uint64_t v_stack_mB0;
    uint16_t v_stack_mBE;
    uint64_t v_stack_mC0;
    uint16_t v_stack_mCE;
    uint64_t v_stack_mD0;
    uint16_t v_stack_mDE;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p150;
    uint64_t v_stack_p158;
    uint64_t v_stack_p160;
    uint32_t v_stack_p168;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint16_t v_stack_p32;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint16_t v_stack_p6A;
    uint64_t v_stack_p78;
    uint64_t v_stack_p88;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pD8;
    uint64_t v_stack_pE8;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(void **)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (272);
    *(uint64_t *)(local_rsp - 0x48) = v_xmm6;
    v_stack_mF8 = Arg3;
    *(uint64_t *)(local_rsp - 0xA0) = v_xmm0;
    v_stack_mE0 = v_xmm1;
    *(uint64_t *)(local_rsp - 0x80) = v_xmm0;
    *(uint64_t *)(local_rsp - 0xC0) = v_xmm1;
    local_rbx = 0;
    v_stack_mE8 = 0;
    *(uint64_t *)(local_rsp - 0xB0) = v_xmm0;
    v_stack_mD0 = v_xmm1;
    *(uint64_t *)(local_rsp - 0x70) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x90) = v_xmm1;
    if ((((uint8_t)(Arg2)) & (3)) != 0) goto loc_009E64AD;
    if (Arg2 < Arg3) { Arg3 = Arg2; }
    v_stack_m128 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x8)));
    v_stack_m120 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x8)));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x8))))) ^ (1));
    if ((((uint32_t)(result)) & (0xF4010E11ULL)) != 0) goto loc_009E64B3;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x8))))) & (0xFF000060ULL));
    result = (uint32_t)((result) - 1);
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x8)))));
    if ((((uint32_t)(result)) & (0x1000060ULL)) != 0) goto loc_009E64BD;
    v_stack_mE8 = *(uint64_t *)(Arg2 + 0x80);
    v_stack_m100 = *(uint64_t *)(Arg2 + 0x3F0);
    if (*(uint64_t *)(Arg2 + 0x3F0) == 0) goto loc_009E64D4;
    if ((((uint8_t)(*(uint64_t *)(Arg2 + 0x3F0))) & (1)) != 0) goto loc_009E64D4;
    if ((*(uint64_t *)(Arg2 + 0x3F0) + *(uint64_t *)(Arg2 + 0x80) * 1) > Arg3) goto loc_009E64C7;
    if ((*(uint64_t *)(Arg2 + 0x3F0) + *(uint64_t *)(Arg2 + 0x80) * 1) < (*(uint64_t *)(Arg2 + 0x80))) goto loc_009E64C7;
loc_009E64AB:
    goto loc_009E64E3;
loc_009E64AD:
    result = ExRaiseDatatypeMisalignment(*(uint64_t *)(Arg2 + 0x80), *(uint64_t *)(Arg2 + 0x3F0) + *(uint64_t *)(Arg2 + 0x80) * 1, Arg3, Arg4);
loc_009E64B3:
    goto loc_009E67B2;
loc_009E64BD:
    goto loc_009E67B2;
loc_009E64C7:
    v_stack_m128 = (uint32_t)((uint32_t)(v_stack_m120));
    goto loc_009E64AB;
loc_009E64D4:
    goto loc_009E67B2;
loc_009E64E3:
    if ((((uint8_t)(Arg4)) & (1)) == 0) goto loc_009E69CD;
    result = PsGetServerSiloGlobals(Arg5, *(uint64_t *)(Arg2 + 0x3F0) + *(uint64_t *)(Arg2 + 0x80) * 1, Arg3, Arg4);
    v_stack_mE0 = v_xmm0;
    v_stack_m118 = v_xmm6;
    if ((((uint8_t)(Arg4)) & (2)) == 0) {
        Arg1 = *(uint64_t *)(result + 0x3E0);
        v_stack_mE8 = Arg1;
        result = *(uint16_t *)(result + 0x3DA);
        v_stack_m100 = result;
    }
    v_stack_m108 = v_xmm0;
loc_009E654B:
    result = PspCaptureAndValidateUnicodeString(Arg2 + 80, v_stack_mC0, Arg3, Arg4);
    if (sign_flag) goto loc_009E67B2;
    result = PspCaptureAndValidateUnicodeString(Arg2 + 96, v_stack_mB0, Arg3, Arg4);
    if (sign_flag) goto loc_009E67B2;
    result = PspCaptureAndValidateUnicodeString(Arg2 + 112, v_stack_mA0, Arg3, Arg4);
    if (sign_flag) goto loc_009E67B2;
    result = PspCaptureAndValidateUnicodeString(Arg2 + 176, v_stack_m90, Arg3, Arg4);
    if (sign_flag) goto loc_009E67B2;
    result = PspCaptureAndValidateUnicodeString(Arg2 + 192, v_stack_m80, Arg3, Arg4);
    if (sign_flag) goto loc_009E67B2;
    result = PspCaptureAndValidateUnicodeString(Arg2 + 208, v_stack_m70, Arg3, Arg4);
    if (sign_flag) goto loc_009E67B2;
    if (Arg3 != NULL) goto loc_009E6B5B;
loc_009E65F7:
    result = PspCaptureAndValidateUnicodeString(Arg2 + 1040, v_stack_mD0, Arg3, Arg4);
    if (sign_flag) goto loc_009E67B2;
loc_009E6610:
    if (Arg3 != NULL) goto loc_009E6B79;
loc_009E6619:
    v_stack_m60 = v_xmm0;
loc_009E6624:
    result = (v_stack_m60) >> (16);
    Arg1 = ((uint16_t)(result)) + (v_stack_mCE);
    Arg1 = (Arg1) + (v_stack_m6E);
    Arg1 = (Arg1) + (v_stack_m7E);
    Arg1 = (Arg1) + (v_stack_m8E);
    Arg1 = (Arg1) + (v_stack_m9E);
    Arg1 = (Arg1) + (v_stack_mAE);
    Arg1 = (Arg1) + (v_stack_mBE);
    Arg1 = (Arg1) + ((uint16_t)(local_r14));
    local_r13 = (v_stack_mDE) + (0x451ULL);
    local_r13 = (local_r13) + (Arg1);
    local_r13 = (local_r13) & (-2);
    v_stack_mF0 = local_r13;
    if (Arg3 != NULL) goto loc_009E6B96;
loc_009E66A6:
    Arg1 = (v_stack_m100) + (local_r13);
    Arg2 = (v_stack_mD0) | (-1);
    if (Arg1 >= local_r13) { Arg2 = Arg1; }
    local_r14 = (uint32_t)((local_r14) & (0xC0000095ULL));
    if (Arg1 < local_r13) goto loc_009E6C18;
    result = ExAllocatePool2(65, Arg2, (uint32_t)(0x62507350ULL), Arg4);
    v_stack_mF8 = result;
    if (result == 0) goto loc_009E6BBF;
loc_009E66F5:
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm1;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    *(uint64_t *)(result + 0x30) = v_xmm1;
    *(uint64_t *)(result + 0x40) = v_xmm0;
    *(uint64_t *)(result + 0x50) = v_xmm1;
    *(uint64_t *)(result + 0x60) = v_xmm0;
    result = (result) + (8 + 120);
    *(uint64_t *)(result - 0x10) = v_xmm1;
    local_rsi = (Arg2) + (8 + 120);
    Arg1 = (8) - (1);
    if (condition_is_not_equal) goto loc_009E66F5;
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm1;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    *(uint64_t *)(result + 0x30) = v_xmm1;
    *(uint64_t *)(result + 0x40) = v_xmm0;
    goto loc_009E67A0;
loc_009E67A0:
    if (!sign_flag) goto loc_009E67CE;
loc_009E67A5:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(0x62507350ULL), Arg4);
loc_009E67B2:
    local_rsp = (local_rsp) + (272);
    return (uint32_t)((uint32_t)(local_r14));
loc_009E67CE:
    *(uint32_t *)(result + 0x8) = (uint32_t)((uint32_t)((uint32_t)(local_r14)));
    *(uint32_t *)(result + 0x4) = (uint32_t)(local_r13);
    *(uint32_t *)(result) = (uint32_t)(local_r13);
    v_stack_p20 = result + 1104;
    if (Arg3 != NULL) goto loc_009E6BC9;
loc_009E67ED:
    result = PspCopyUnicodeString(v_stack_p68, result + 56, v_stack_p20, Arg4);
    if (sign_flag) goto loc_009E67A5;
    result = PspCopyUnicodeString(v_stack_p88, result + 80, v_stack_p20, Arg4);
    if (sign_flag) goto loc_009E67A5;
    result = PspCopyUnicodeString(v_stack_p98, result + 96, v_stack_p20, Arg4);
    if (sign_flag) goto loc_009E67A5;
    result = PspCopyUnicodeString(v_stack_pA8, result + 112, v_stack_p20, Arg4);
    if (sign_flag) goto loc_009E67A5;
    result = PspCopyUnicodeString(v_stack_pB8, result + 176, v_stack_p20, Arg4);
    if (sign_flag) goto loc_009E67A5;
    result = PspCopyUnicodeString(v_stack_pC8, result + 192, v_stack_p20, Arg4);
    if (sign_flag) goto loc_009E67A5;
    result = PspCopyUnicodeString(v_stack_pD8, result + 208, v_stack_p20, Arg4);
    if (sign_flag) goto loc_009E67A5;
    result = PspCopyUnicodeString(v_stack_p78, result + 1040, v_stack_p20, Arg4);
    if (Arg3 != NULL) goto loc_009E6BE4;
loc_009E68F1:
    *(uint64_t *)(result + 0x420) = v_xmm0;
loc_009E68FB:
    *(uint64_t *)(result + 0xE0) = v_xmm6;
    if (v_stack_m108 != 0) goto loc_009E6A43;
loc_009E6911:
    *(uint64_t *)(result + 0x430) = 0;
    *(uint32_t *)(result + 0x438) = 0;
    result = (result) - (v_stack_p20);
    local_r13 = (local_r13) + (result);
    if (condition_is_not_equal) goto loc_009E6B38;
loc_009E6936:
    result = memcpy(v_stack_p20, v_stack_p60, v_stack_p48, Arg4);
    goto loc_009E6959;
loc_009E6959:
    if (sign_flag) goto loc_009E67A5;
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p168)))) & (3));
    if (((uint8_t)(result)) == 1) goto loc_009E698B;
    result = PspValidateEnvironmentBlock(v_stack_p20, v_stack_p48, v_stack_p48, Arg4);
    if (sign_flag) goto loc_009E67A5;
loc_009E698B:
    if ((((uint8_t)((uint32_t)(v_stack_p168))) & (1)) != 0) {
        *(uint64_t *)(result + 0x10) = 0;
        *(uint64_t *)(result + 0x20) = 0;
        *(uint64_t *)(result + 0x28) = 0;
        *(uint64_t *)(result + 0x30) = 0;
    }
    *(uint64_t *)(result + 0x80) = v_stack_p20;
    *(uint64_t *)(result + 0x3F0) = v_stack_p48;
    *(uint64_t *)(result + 0x3F8) = 0;
    *(uint64_t *)(v_stack_p150) = result;
    result = 0;
    goto loc_009E67B2;
loc_009E69CD:
    result = PspCaptureAndValidateUnicodeString(v_stack_p20 + 56, v_stack_p68, v_stack_p48, Arg4);
    if (sign_flag) goto loc_009E67B2;
    if (v_stack_p68 >= 520) goto loc_009E6C18;
    v_stack_p6A = 520;
    v_stack_p30 = v_xmm0;
    goto loc_009E6A0E;
loc_009E6A0E:
    v_stack_p40 = v_stack_p38;
    if (v_stack_p38 != 0) goto loc_009E6AA2;
    if ((uint16_t)(v_stack_p30) != 0) goto loc_009E6C18;
    v_stack_p32 = 0;
loc_009E6A39:
    goto loc_009E654B;
loc_009E6A43:
    *(uint64_t *)(v_stack_p38 + 0xE8) = v_stack_p20;
    result = memcpy(v_stack_p20, v_stack_p40, (uint16_t)(v_stack_p30), Arg4);
    goto loc_009E6A7F;
loc_009E6A7F:
    if (sign_flag) goto loc_009E67A5;
    if (v_stack_p20 == 0) goto loc_009E6911;
    local_rsi = (v_stack_p20) + ((uint16_t)(v_stack_p30));
    v_stack_p20 = local_rsi;
    goto loc_009E6911;
loc_009E6AA2:
    v_stack_p32 = (uint16_t)(v_stack_p30);
    if ((uint16_t)(v_stack_p30) == 0) goto loc_009E6AF0;
    if ((v_stack_p38 + v_stack_p30 * 1) > ((uint16_t)(v_stack_p30))) goto loc_009E6AD0;
    result = (uint16_t)(v_stack_p30);
    local_r12 = v_stack_p30;
    local_r14 = (uint16_t)(v_stack_p30);
    if ((v_stack_p38 + v_stack_p30 * 1) < v_stack_p38) {
        result = *(uint8_t *)((uint16_t)(v_stack_p30));
        result = v_stack_p28;
        v_stack_p20 = (uint32_t)(result);
        result = v_stack_p38;
        v_stack_p40 = result;
        local_r14 = v_stack_p32;
        local_r12 = v_stack_p30;
    }
    goto loc_009E6B29;
loc_009E6B29:
    if (!sign_flag) goto loc_009E6A39;
    goto loc_009E67B2;
loc_009E6B38:
    Arg2 = 0;
    result = memset(local_rsi, Arg2, local_r13, Arg4);
    if (local_rsi == 0) goto loc_009E6936;
    local_rsi = (local_rsi) + (local_r13);
    v_stack_p20 = local_rsi;
    goto loc_009E6936;
loc_009E6B5B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p168) + 0x4)))) & (2)) == 0) goto loc_009E65F7;
    v_stack_p78 = v_xmm0;
    goto loc_009E6610;
loc_009E6B79:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p168) + 0x4)))) & (4)) == 0) goto loc_009E6619;
    v_stack_pE8 = v_xmm0;
    goto loc_009E6624;
loc_009E6B96:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p168) + 0x4)))) & (1)) == 0) goto loc_009E66A6;
    result = (local_r13 + 3) & (-4);
    if ((result + (uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p168) + 0x30)) * 8) < result) goto loc_009E6C18;
    v_stack_p58 = result + (uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p168) + 0x30)) * 8;
    goto loc_009E66A6;
loc_009E6BBF:
    goto loc_009E67B2;
loc_009E6BC9:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p168) + 0x4)))) & (8)) == 0) goto loc_009E67ED;
    *(uint32_t *)((uint32_t)(v_stack_p168) + 0x4 + 0x43C) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p168) + 0x34)));
    goto loc_009E67ED;
loc_009E6BE4:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p168) + 0x4)))) & (4)) == 0) goto loc_009E68F1;
    result = PspCopyUnicodeString(v_stack_pE8, (uint32_t)(v_stack_p168) + 4 + 1056, v_stack_p20, Arg4);
    *(uint32_t *)((uint32_t)(v_stack_p168) + 0x4 + 0x440) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p168) + 0x38)));
    goto loc_009E68FB;
loc_009E6C18:
    goto loc_009E67B2;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x4` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009E63C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
