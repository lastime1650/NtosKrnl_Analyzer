# MiDbgCopyMemory

- RVA: `0x00684A18`–`0x00684E63` (길이 `1,099` bytes)
- VA: `0x0000000140684A18`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D875C`
- 디코드: `284`개 명령, `1,099/1,099` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00684AD6` → [KeIsUserVaAccessAllowed](../21/KeIsUserVaAccessAllowed_function_0021D740.md) (function, `0x0021D740`)
- `0x00684B0B` → [MiDbgTranslatePhysicalAddress](MiDbgTranslatePhysicalAddress_function_00685760.md) (function, `0x00685760`)
- `0x00684B64` → [ProbeForWrite](../../page/8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x00684B74` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00684BCC` → [KeGenericCallDpc](../49/KeGenericCallDpc_function_0049F980.md) (function, `0x0049F980`)
- `0x00684BE3` → [MmIsAddressValidEx](../27/MmIsAddressValidEx_function_0027FDD0.md) (function, `0x0027FDD0`)
- `0x00684BFE` → [MiDbgPteWriteInProgress](MiDbgPteWriteInProgress_function_00685528.md) (function, `0x00685528`)
- `0x00684C34` → [MmGetPhysicalAddress](../23/MmGetPhysicalAddress_function_0023A500.md) (function, `0x0023A500`)
- `0x00684C7D` → [MiDbgPatchIdentity](MiDbgPatchIdentity_function_00685470.md) (function, `0x00685470`)
- `0x00684C92` → [MmGetPhysicalAddress](../23/MmGetPhysicalAddress_function_0023A500.md) (function, `0x0023A500`)
- `0x00684CA4` → [MiDbgTranslatePhysicalAddress](MiDbgTranslatePhysicalAddress_function_00685760.md) (function, `0x00685760`)
- `0x00684D1F` → [MiDbgWriteCheck](MiDbgWriteCheck_function_00685BE4.md) (function, `0x00685BE4`)
- `0x00684D5E` → [MiAllocateDbgPatches](MiAllocateDbgPatches_function_00684358.md) (function, `0x00684358`)
- `0x00684D7E` → [MiFillDbgPatches](MiFillDbgPatches_function_00685F3C.md) (function, `0x00685F3C`)
- `0x00684DAC` → [MiCopyToUntrustedMemory](MiCopyToUntrustedMemory_function_00684894.md) (function, `0x00684894`)
- `0x00684DD5` → [MiFillDbgPatches](MiFillDbgPatches_function_00685F3C.md) (function, `0x00685F3C`)
- `0x00684DF5` → [MiCopyFromUntrustedMemory](MiCopyFromUntrustedMemory_function_00684744.md) (function, `0x00684744`)
- `0x00684E25` → [MiDbgReleaseAddress](MiDbgReleaseAddress_function_00685630.md) (function, `0x00685630`)
- `0x00684E38` → [MiDbgUnTranslatePhysicalAddress](MiDbgUnTranslatePhysicalAddress_function_00685AF8.md) (function, `0x00685AF8`)
- `0x00684E4A` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [MmDbgCopyMemory](MmDbgCopyMemory_function_006861E8.md) at `0x00686260`

### Static image references
- `0x00684A2D` → RVA `0x00E0A740` (`.data`; read)
- `0x00684BC5` → RVA `0x00684E70` (`MiDbgCopyMemoryTarget`; read)
- `0x00684C24` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00684C44` → RVA `0x00E2DCE0` (`.data`; read)
- `0x00684CC8` → RVA `0x00FC6BF0` (`ALMOSTRO`; read)
- `0x00684DDC` → RVA `0x00E0EBC8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00684B64` → [ProbeForWrite](../../page/8E/ProbeForWrite_function_008E91C0.md) (`.text` → `PAGE`)
  - `0x00684B74` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00684A18  4C 8B DC                        mov r11, rsp
00684A1B  53                              push rbx
00684A1C  56                              push rsi
00684A1D  57                              push rdi
00684A1E  41 54                           push r12
00684A20  41 55                           push r13
00684A22  41 56                           push r14
00684A24  41 57                           push r15
00684A26  48 81 EC F0 00 00 00            sub rsp, 0xf0
00684A2D  48 8B 05 0C 5D 78 00            mov rax, qword ptr [rip + 0x785d0c]
00684A34  48 33 C4                        xor rax, rsp
00684A37  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
00684A3F  44 89 4C 24 40                  mov dword ptr [rsp + 0x40], r9d
00684A44  45 8B E8                        mov r13d, r8d
00684A47  4C 8B E2                        mov r12, rdx
00684A4A  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
00684A4F  4C 8B F1                        mov r14, rcx
00684A52  8B BC 24 50 01 00 00            mov edi, dword ptr [rsp + 0x150]
00684A59  33 F6                           xor esi, esi
00684A5B  48 89 74 24 50                  mov qword ptr [rsp + 0x50], rsi
00684A60  0F 57 C0                        xorps xmm0, xmm0
00684A63  33 C0                           xor eax, eax
00684A65  0F 11 84 24 80 00 00 00         movups xmmword ptr [rsp + 0x80], xmm0
00684A6D  0F 11 84 24 90 00 00 00         movups xmmword ptr [rsp + 0x90], xmm0
00684A75  0F 11 84 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm0
00684A7D  49 89 43 88                     mov qword ptr [r11 - 0x78], rax
00684A81  89 74 24 7C                     mov dword ptr [rsp + 0x7c], esi
00684A85  41 0F 11 43 90                  movups xmmword ptr [r11 - 0x70], xmm0
00684A8A  0F 57 C9                        xorps xmm1, xmm1
00684A8D  41 0F 11 4B A0                  movups xmmword ptr [r11 - 0x60], xmm1
00684A92  49 89 43 B0                     mov qword ptr [r11 - 0x50], rax
00684A96  45 85 C0                        test r8d, r8d
00684A99  75 0A                           jne 0x140684aa5
00684A9B  B8 F1 00 00 C0                  mov eax, 0xc00000f1
00684AA0  E9 9A 03 00 00                  jmp 0x140684e3f
00684AA5  40 F6 C7 40                     test dil, 0x40
00684AA9  74 1D                           je 0x140684ac8
00684AAB  40 F6 C7 02                     test dil, 2
00684AAF  0F 85 82 00 00 00               jne 0x140684b37
00684AB5  41 BF 01 00 00 00               mov r15d, 1
00684ABB  41 84 FF                        test r15b, dil
00684ABE  74 77                           je 0x140684b37
00684AC0  40 F6 C7 04                     test dil, 4
00684AC4  74 71                           je 0x140684b37
00684AC6  EB 06                           jmp 0x140684ace
00684AC8  41 BF 01 00 00 00               mov r15d, 1
00684ACE  48 83 4C 24 48 FF               or qword ptr [rsp + 0x48], 0xffffffffffffffff
00684AD4  33 C9                           xor ecx, ecx
00684AD6  E8 65 8C B9 FF                  call 0x14021d740
00684ADB  F6 D8                           neg al
00684ADD  1B DB                           sbb ebx, ebx
00684ADF  83 E3 02                        and ebx, 2
00684AE2  0F BA EF 1F                     bts edi, 0x1f
00684AE6  8B C7                           mov eax, edi
00684AE8  83 E0 04                        and eax, 4
00684AEB  40 F6 C7 02                     test dil, 2
00684AEF  74 35                           je 0x140684b26
00684AF1  85 C0                           test eax, eax
00684AF3  75 09                           jne 0x140684afe
00684AF5  44 0F 20 C0                     mov rax, cr8
00684AF9  41 3A C7                        cmp al, r15b
00684AFC  77 39                           ja 0x140684b37
00684AFE  4C 8D 84 24 80 00 00 00         lea r8, [rsp + 0x80]
00684B06  8B D7                           mov edx, edi
00684B08  49 8B CE                        mov rcx, r14
00684B0B  E8 50 0C 00 00                  call 0x140685760
00684B10  4C 8B F0                        mov r14, rax
00684B13  48 85 C0                        test rax, rax
00684B16  0F 85 A2 01 00 00               jne 0x140684cbe
00684B1C  B8 01 00 00 C0                  mov eax, 0xc0000001
00684B21  E9 19 03 00 00                  jmp 0x140684e3f
00684B26  85 C0                           test eax, eax
00684B28  0F 85 AC 00 00 00               jne 0x140684bda
00684B2E  44 0F 20 C0                     mov rax, cr8
00684B32  41 3A C7                        cmp al, r15b
00684B35  76 0A                           jbe 0x140684b41
00684B37  B8 F2 00 00 C0                  mov eax, 0xc00000f2
00684B3C  E9 FE 02 00 00                  jmp 0x140684e3f
00684B41  0F BA F7 1F                     btr edi, 0x1f
00684B45  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
00684B4F  4C 3B F0                        cmp r14, rax
00684B52  73 54                           jae 0x140684ba8
00684B54  8B F7                           mov esi, edi
00684B56  41 23 F7                        and esi, r15d
00684B59  74 10                           je 0x140684b6b
00684B5B  49 8B D5                        mov rdx, r13
00684B5E  45 8B C5                        mov r8d, r13d
00684B61  49 8B CE                        mov rcx, r14
00684B64  E8 57 46 26 00                  call 0x1408e91c0
00684B69  EB 28                           jmp 0x140684b93
00684B6B  41 8D 4D FF                     lea ecx, [r13 - 1]
00684B6F  49 85 CE                        test r14, rcx
00684B72  74 05                           je 0x140684b79
00684B74  E8 57 54 21 00                  call 0x140899fd0
00684B79  4B 8D 0C 2E                     lea rcx, [r14 + r13]
00684B7D  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
00684B87  48 3B C8                        cmp rcx, rax
00684B8A  77 05                           ja 0x140684b91
00684B8C  49 3B CE                        cmp rcx, r14
00684B8F  73 02                           jae 0x140684b93
00684B91  8A 00                           mov al, byte ptr [rax]
00684B93  85 F6                           test esi, esi
00684B95  0F 84 4C 02 00 00               je 0x140684de7
00684B9B  45 8B E7                        mov r12d, r15d
00684B9E  E9 E0 01 00 00                  jmp 0x140684d83
00684BA3  E9 97 02 00 00                  jmp 0x140684e3f
00684BA8  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
00684BAD  44 89 6C 24 70                  mov dword ptr [rsp + 0x70], r13d
00684BB2  4C 89 64 24 68                  mov qword ptr [rsp + 0x68], r12
00684BB7  44 89 4C 24 74                  mov dword ptr [rsp + 0x74], r9d
00684BBC  89 7C 24 78                     mov dword ptr [rsp + 0x78], edi
00684BC0  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00684BC5  48 8D 0D A4 02 00 00            lea rcx, [rip + 0x2a4]
00684BCC  E8 AF AD E1 FF                  call 0x14049f980
00684BD1  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
00684BD5  E9 65 02 00 00                  jmp 0x140684e3f
00684BDA  0F BA EF 1E                     bts edi, 0x1e
00684BDE  33 D2                           xor edx, edx
00684BE0  49 8B CE                        mov rcx, r14
00684BE3  E8 E8 B1 BF FF                  call 0x14027fdd0
00684BE8  84 C0                           test al, al
00684BEA  75 32                           jne 0x140684c1e
00684BEC  40 84 FF                        test dil, dil
00684BEF  79 17                           jns 0x140684c08
00684BF1  4C 8D 84 24 80 00 00 00         lea r8, [rsp + 0x80]
00684BF9  8B D7                           mov edx, edi
00684BFB  49 8B CE                        mov rcx, r14
00684BFE  E8 25 09 00 00                  call 0x140685528
00684C03  4C 8B F0                        mov r14, rax
00684C06  EB 03                           jmp 0x140684c0b
00684C08  4C 8B F6                        mov r14, rsi
00684C0B  4D 85 F6                        test r14, r14
00684C0E  0F 85 A7 00 00 00               jne 0x140684cbb
00684C14  BE EF 00 00 C0                  mov esi, 0xc00000ef
00684C19  E9 1F 02 00 00                  jmp 0x140684e3d
00684C1E  40 F6 C7 41                     test dil, 0x41
00684C22  74 65                           je 0x140684c89
00684C24  48 F7 05 59 1E 94 00 00 00 00 10  test qword ptr [rip + 0x941e59], 0x10000000
00684C2F  74 58                           je 0x140684c89
00684C31  49 8B CE                        mov rcx, r14
00684C34  E8 C7 58 BB FF                  call 0x14023a500
00684C39  48 C1 E8 0C                     shr rax, 0xc
00684C3D  48 8D 14 40                     lea rdx, [rax + rax*2]
00684C41  48 03 D2                        add rdx, rdx
00684C44  48 3B 05 95 90 7A 00            cmp rax, qword ptr [rip + 0x7a9095]
00684C4B  76 04                           jbe 0x140684c51
00684C4D  8B C6                           mov eax, esi
00684C4F  EB 15                           jmp 0x140684c66
00684C51  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
00684C5B  48 8B 04 D0                     mov rax, qword ptr [rax + rdx*8]
00684C5F  48 C1 E8 36                     shr rax, 0x36
00684C63  41 23 C7                        and eax, r15d
00684C66  85 C0                           test eax, eax
00684C68  74 1F                           je 0x140684c89
00684C6A  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00684C74  48 8D 0C D0                     lea rcx, [rax + rdx*8]
00684C78  45 33 C0                        xor r8d, r8d
00684C7B  33 D2                           xor edx, edx
00684C7D  E8 EE 07 00 00                  call 0x140685470
00684C82  85 C0                           test eax, eax
00684C84  74 03                           je 0x140684c89
00684C86  83 CF 40                        or edi, 0x40
00684C89  40 F6 C7 40                     test dil, 0x40
00684C8D  74 2F                           je 0x140684cbe
00684C8F  49 8B CE                        mov rcx, r14
00684C92  E8 69 58 BB FF                  call 0x14023a500
00684C97  4C 8D 84 24 80 00 00 00         lea r8, [rsp + 0x80]
00684C9F  8B D7                           mov edx, edi
00684CA1  48 8B C8                        mov rcx, rax
00684CA4  E8 B7 0A 00 00                  call 0x140685760
00684CA9  4C 8B F0                        mov r14, rax
00684CAC  48 85 C0                        test rax, rax
00684CAF  75 0A                           jne 0x140684cbb
00684CB1  BE 01 00 00 C0                  mov esi, 0xc0000001
00684CB6  E9 82 01 00 00                  jmp 0x140684e3d
00684CBB  83 CF 02                        or edi, 2
00684CBE  8B CF                           mov ecx, edi
00684CC0  83 E1 06                        and ecx, 6
00684CC3  83 F9 04                        cmp ecx, 4
00684CC6  75 0B                           jne 0x140684cd3
00684CC8  39 35 22 1F 94 00               cmp dword ptr [rip + 0x941f22], esi
00684CCE  74 03                           je 0x140684cd3
00684CD0  0F 01 CB                        stac
00684CD3  41 84 FF                        test r15b, dil
00684CD6  0F 84 0B 01 00 00               je 0x140684de7
00684CDC  83 F9 02                        cmp ecx, 2
00684CDF  75 14                           jne 0x140684cf5
00684CE1  48 39 B4 24 A8 00 00 00         cmp qword ptr [rsp + 0xa8], rsi
00684CE9  74 0A                           je 0x140684cf5
00684CEB  BE 01 00 00 C0                  mov esi, 0xc0000001
00684CF0  E9 07 01 00 00                  jmp 0x140684dfc
00684CF5  48 8D 84 24 B8 00 00 00         lea rax, [rsp + 0xb8]
00684CFD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00684D02  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00684D07  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00684D0C  44 8B 8C 24 80 00 00 00         mov r9d, dword ptr [rsp + 0x80]
00684D14  44 8B C7                        mov r8d, edi
00684D17  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
00684D1C  49 8B CE                        mov rcx, r14
00684D1F  E8 C0 0E 00 00                  call 0x140685be4
00684D24  44 8B E0                        mov r12d, eax
00684D27  85 C0                           test eax, eax
00684D29  75 0A                           jne 0x140684d35
00684D2B  BE EF 00 00 C0                  mov esi, 0xc00000ef
00684D30  E9 C7 00 00 00                  jmp 0x140684dfc
00684D35  41 0B DF                        or ebx, r15d
00684D38  40 F6 C7 02                     test dil, 2
00684D3C  74 45                           je 0x140684d83
00684D3E  48 39 B4 24 A8 00 00 00         cmp qword ptr [rsp + 0xa8], rsi
00684D46  74 3B                           je 0x140684d83
00684D48  4C 8D 8C 24 C8 00 00 00         lea r9, [rsp + 0xc8]
00684D50  4C 8D 84 24 80 00 00 00         lea r8, [rsp + 0x80]
00684D58  41 8B D5                        mov edx, r13d
00684D5B  49 8B CE                        mov rcx, r14
00684D5E  E8 F5 F5 FF FF                  call 0x140684358
00684D63  8B F0                           mov esi, eax
00684D65  85 C0                           test eax, eax
00684D67  0F 88 8F 00 00 00               js 0x140684dfc
00684D6D  45 8B CF                        mov r9d, r15d
00684D70  4C 8D 84 24 C8 00 00 00         lea r8, [rsp + 0xc8]
00684D78  41 8B D5                        mov edx, r13d
00684D7B  49 8B CE                        mov rcx, r14
00684D7E  E8 B9 11 00 00                  call 0x140685f3c
00684D83  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
00684D88  44 8B 4C 24 40                  mov r9d, dword ptr [rsp + 0x40]
00684D8D  44 89 4C 24 28                  mov dword ptr [rsp + 0x28], r9d
00684D92  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
00684D97  4C 8B 4C 24 58                  mov r9, qword ptr [rsp + 0x58]
00684D9C  4C 8D 84 24 B8 00 00 00         lea r8, [rsp + 0xb8]
00684DA4  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
00684DA9  49 8B CE                        mov rcx, r14
00684DAC  E8 E3 FA FF FF                  call 0x140684894
00684DB1  8B F0                           mov esi, eax
00684DB3  40 F6 C7 02                     test dil, 2
00684DB7  74 43                           je 0x140684dfc
00684DB9  48 83 BC 24 A8 00 00 00 00      cmp qword ptr [rsp + 0xa8], 0
00684DC2  74 38                           je 0x140684dfc
00684DC4  45 33 C9                        xor r9d, r9d
00684DC7  4C 8D 84 24 C8 00 00 00         lea r8, [rsp + 0xc8]
00684DCF  41 8B D5                        mov edx, r13d
00684DD2  49 8B CE                        mov rcx, r14
00684DD5  E8 62 11 00 00                  call 0x140685f3c
00684DDA  33 C0                           xor eax, eax
00684DDC  F0 44 0F B1 3D E3 9D 78 00      lock cmpxchg dword ptr [rip + 0x789de3], r15d
00684DE5  EB 15                           jmp 0x140684dfc
00684DE7  44 8B 4C 24 40                  mov r9d, dword ptr [rsp + 0x40]
00684DEC  45 8B C5                        mov r8d, r13d
00684DEF  49 8B D6                        mov rdx, r14
00684DF2  49 8B CC                        mov rcx, r12
00684DF5  E8 4A F9 FF FF                  call 0x140684744
00684DFA  8B F0                           mov esi, eax
00684DFC  8B C7                           mov eax, edi
00684DFE  24 06                           and al, 6
00684E00  3C 04                           cmp al, 4
00684E02  75 11                           jne 0x140684e15
00684E04  83 FB 02                        cmp ebx, 2
00684E07  73 0C                           jae 0x140684e15
00684E09  83 3D E0 1D 94 00 00            cmp dword ptr [rip + 0x941de0], 0
00684E10  74 03                           je 0x140684e15
00684E12  0F 01 CA                        clac
00684E15  41 84 DF                        test r15b, bl
00684E18  74 10                           je 0x140684e2a
00684E1A  44 8B C7                        mov r8d, edi
00684E1D  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
00684E22  49 8B CE                        mov rcx, r14
00684E25  E8 06 08 00 00                  call 0x140685630
00684E2A  40 F6 C7 02                     test dil, 2
00684E2E  74 0D                           je 0x140684e3d
00684E30  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
00684E38  E8 BB 0C 00 00                  call 0x140685af8
00684E3D  8B C6                           mov eax, esi
00684E3F  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
00684E47  48 33 CC                        xor rcx, rsp
00684E4A  E8 F1 77 02 00                  call 0x1406ac640
00684E4F  48 81 C4 F0 00 00 00            add rsp, 0xf0
00684E56  41 5F                           pop r15
00684E58  41 5E                           pop r14
00684E5A  41 5D                           pop r13
00684E5C  41 5C                           pop r12
00684E5E  5F                              pop rdi
00684E5F  5E                              pop rsi
00684E60  5B                              pop rbx
00684E61  C3                              ret
00684E62  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDbgCopyMemory(__int64 a1, __int64 a2, int a3, int a4, unsigned int a5)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mAC;
    unsigned int v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE8;
    unsigned int v_stack_mF0;

    v_rsp = (v_rsp) - (240);
    result = (*(unsigned __int64 *)(v_rip + 7888140)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_mE8 = a4;
    v_stack_mD0 = a2;
    v_rsi = 0;
    v_stack_mD8 = 0;
    result = 0;
    v_stack_mA8 = v_xmm0;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 120) = 0;
    v_stack_mAC = 0;
    *(unsigned __int64 *)(v_rsp - 112) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 96) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 80) = 0;
    if (a3 != 0) goto loc_00684AA5;
    goto loc_00684E3F;
loc_00684AA5:
    if ((((unsigned __int8)((unsigned int)(a5))) & (64)) == 0) goto loc_00684AC8;
    if ((((unsigned __int8)((unsigned int)(a5))) & (2)) != 0) goto loc_00684B37;
    if (((1) & ((unsigned __int8)((unsigned int)(a5)))) == 0) goto loc_00684B37;
    if ((((unsigned __int8)((unsigned int)(a5))) & (4)) == 0) goto loc_00684B37;
    goto loc_00684ACE;
loc_00684AC8:
loc_00684ACE:
    a1 = 0;
    result = KeIsUserVaAccessAllowed(a1, a2, a3, a4);
    result = (unsigned __int8)(-(result));
    v_rbx = (unsigned int)((v_rbx) & (2));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (4));
    if ((((unsigned __int8)((unsigned int)(a5))) & (2)) == 0) goto loc_00684B26;
    if ((unsigned int)(result) != 0) goto loc_00684AFE;
    if (((unsigned __int8)(v_cr8)) > 1) goto loc_00684B37;
loc_00684AFE:
    result = MiDbgTranslatePhysicalAddress(0, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_mA8, a4);
    if (result != 0) goto loc_00684CBE;
    goto loc_00684E3F;
loc_00684B26:
    if ((unsigned int)((unsigned int)(0xC0000001ULL)) != 0) goto loc_00684BDA;
    if (((unsigned __int8)(v_cr8)) <= 1) goto loc_00684B41;
loc_00684B37:
    goto loc_00684E3F;
loc_00684B41:
    if (result >= ((unsigned int)(0xC00000F2ULL))) goto loc_00684BA8;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (1));
    if (condition_is_equal) goto loc_00684B6B;
    result = ProbeForWrite(result, (unsigned int)(a3), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    goto loc_00684B93;
loc_00684B6B:
    if (((result) & ((unsigned int)(a3) - 1)) != 0) {
        result = ExRaiseDatatypeMisalignment((unsigned int)(a3) - 1, (unsigned int)(a3), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
    if ((result + (unsigned int)(a3) * 1) > result) goto loc_00684B91;
    if ((result + (unsigned int)(a3) * 1) < result) {
        result = *(unsigned __int8 *)(result);
    }
    if ((unsigned int)(v_rsi) == 0) goto loc_00684DE7;
    goto loc_00684D83;
loc_00684BA8:
    v_stack_mC8 = result;
    v_stack_mB8 = (unsigned int)((unsigned int)(a3));
    v_stack_mC0 = 1;
    v_stack_mB4 = a4;
    v_stack_mB0 = (unsigned int)((unsigned int)(a5));
    result = KeGenericCallDpc(v_rip + 676, v_stack_mC8, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    goto loc_00684E3F;
loc_00684BDA:
    a2 = 0;
    result = MmIsAddressValidEx(result, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) != 0) goto loc_00684C1E;
    if (!sign_flag) goto loc_00684C08;
    result = MiDbgPteWriteInProgress(result, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_mA8, a4);
    goto loc_00684C0B;
loc_00684C08:
loc_00684C0B:
    if (v_rsi != 0) goto loc_00684CBB;
    goto loc_00684E3D;
loc_00684C1E:
    if ((((unsigned __int8)((unsigned int)(a5))) & (65)) == 0) goto loc_00684C89;
    if (((*(unsigned __int64 *)(v_rip + 9707097)) & (0x10000000ULL)) == 0) goto loc_00684C89;
    result = MmGetPhysicalAddress(v_rsi, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_mA8, a4);
    result = (result) >> (12);
    a2 = (result + result * 2) + (result + result * 2);
    if (result <= (*(unsigned __int64 *)(v_rip + 8032405))) goto loc_00684C51;
    goto loc_00684C66;
loc_00684C51:
    result = (*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(0xC00000EFULL))) + a2 * 8)) >> (54);
    result = (unsigned int)((result) & (1));
loc_00684C66:
    if ((unsigned int)(result) == 0) goto loc_00684C89;
    a3 = 0;
    a2 = 0;
    result = MiDbgPatchIdentity(result + a2 * 8, a2, a3, a4);
    v_rdi = (unsigned int)(a5);
    if ((unsigned int)(result) != 0) {
        v_rdi = (unsigned int)(((unsigned int)(a5)) | (64));
    }
    if ((((unsigned __int8)(v_rdi)) & (64)) == 0) goto loc_00684CBE;
    result = MmGetPhysicalAddress(v_rsi, a2, a3, a4);
    result = MiDbgTranslatePhysicalAddress(result, (unsigned int)((unsigned int)(v_rdi)), v_stack_mA8, a4);
    if (result != 0) goto loc_00684CBB;
    goto loc_00684E3D;
loc_00684CBB:
    v_rdi = (unsigned int)((v_rdi) | (2));
loc_00684CBE:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (6));
    if (((unsigned int)(a1)) != 4) goto loc_00684CD3;
    if ((*(unsigned int *)(v_rip + 9707298)) != ((unsigned int)((unsigned int)(0xC0000001ULL)))) {
    }
    if (((1) & ((unsigned __int8)(v_rdi))) == 0) goto loc_00684DE7;
    if (((unsigned int)(a1)) != 2) goto loc_00684CF5;
    if (v_stack_m80 == ((unsigned int)(0xC0000001ULL))) goto loc_00684CF5;
    goto loc_00684DFC;
loc_00684CF5:
    v_stack_m100 = v_stack_m70;
    v_stack_m108 = v_stack_mE0;
    result = MiDbgWriteCheck(result, v_stack_mD8, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(v_stack_mA8));
    if ((unsigned int)(result) != 0) goto loc_00684D35;
    goto loc_00684DFC;
loc_00684D35:
    v_rbx = (unsigned int)((v_rbx) | (1));
    if ((((unsigned __int8)(v_rdi)) & (2)) == 0) goto loc_00684D83;
    if (v_stack_m80 == ((unsigned int)(0xC00000EFULL))) goto loc_00684D83;
    result = MiAllocateDbgPatches(result, (unsigned int)((unsigned int)((unsigned int)(a3))), v_stack_mA8, v_stack_m60);
    if (sign_flag) goto loc_00684DFC;
    result = MiFillDbgPatches(result, (unsigned int)((unsigned int)((unsigned int)(a3))), v_stack_m60, 1);
loc_00684D83:
    v_stack_mF0 = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_stack_m100 = (unsigned int)((unsigned int)(v_stack_mE8));
    v_stack_m108 = (unsigned int)((unsigned int)(a3));
    result = MiCopyToUntrustedMemory(result, v_stack_mE0, v_stack_m70, v_stack_mD0);
    if ((((unsigned __int8)(v_rdi)) & (2)) == 0) goto loc_00684DFC;
    if (v_stack_m80 == 0) goto loc_00684DFC;
    a4 = 0;
    result = MiFillDbgPatches(result, (unsigned int)((unsigned int)((unsigned int)(a3))), v_stack_m60, a4);
    result = 0;
    goto loc_00684DFC;
loc_00684DE7:
    result = MiCopyFromUntrustedMemory((unsigned int)((unsigned int)(result)), 0, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)(v_stack_mE8));
loc_00684DFC:
    result = (unsigned __int8)(((unsigned int)((unsigned int)(v_rdi))) & (6));
    if (((unsigned __int8)(result)) != 4) goto loc_00684E15;
    if (((unsigned int)(v_rbx)) >= 2) goto loc_00684E15;
    if ((*(unsigned int *)(v_rip + 9706976)) != 0) {
    }
    if (((1) & ((unsigned __int8)(v_rbx))) != 0) {
        a3 = (unsigned int)(v_rdi);
        a2 = v_stack_mD8;
        a1 = result;
        result = MiDbgReleaseAddress(a1, a2, a3, (unsigned int)(v_stack_mE8));
    }
    if ((((unsigned __int8)(v_rdi)) & (2)) != 0) {
        a1 = v_stack_mA8;
        result = MiDbgUnTranslatePhysicalAddress(a1, a2, a3, (unsigned int)(v_stack_mE8));
    }
loc_00684E3F:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, (unsigned int)(v_stack_mE8));
    v_rsp = (v_rsp) + (240);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiDbgCopyMemory(int64_t Arg1, int64_t Arg2, void *Arg3, int32_t Arg4, uint32_t Arg5)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m48;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mAC;
    uint32_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE8;
    uint32_t v_stack_mF0;

    local_rsp = (local_rsp) - (240);
    result = (*(uint64_t *)(v_rip + 0x785D0C)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_mE8 = Arg4;
    v_stack_mD0 = Arg2;
    local_rsi = 0;
    v_stack_mD8 = 0;
    result = 0;
    v_stack_mA8 = v_xmm0;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x78) = 0;
    v_stack_mAC = 0;
    *(uint64_t *)(local_rsp - 0x70) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x60) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x50) = 0;
    if (Arg3 != NULL) goto loc_00684AA5;
    goto loc_00684E3F;
loc_00684AA5:
    if ((((uint8_t)((uint32_t)(Arg5))) & (64)) == 0) goto loc_00684AC8;
    if ((((uint8_t)((uint32_t)(Arg5))) & (2)) != 0) goto loc_00684B37;
    if (((1) & ((uint8_t)((uint32_t)(Arg5)))) == 0) goto loc_00684B37;
    if ((((uint8_t)((uint32_t)(Arg5))) & (4)) == 0) goto loc_00684B37;
    goto loc_00684ACE;
loc_00684AC8:
loc_00684ACE:
    Arg1 = 0;
    result = KeIsUserVaAccessAllowed(Arg1, Arg2, Arg3, Arg4);
    result = (uint8_t)(-(result));
    local_rbx = (uint32_t)((local_rbx) & (2));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (4));
    if ((((uint8_t)((uint32_t)(Arg5))) & (2)) == 0) goto loc_00684B26;
    if ((uint32_t)(result) != 0) goto loc_00684AFE;
    if (((uint8_t)(v_cr8)) > 1) goto loc_00684B37;
loc_00684AFE:
    result = MiDbgTranslatePhysicalAddress(0, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_mA8, Arg4);
    if (result != 0) goto loc_00684CBE;
    goto loc_00684E3F;
loc_00684B26:
    if ((uint32_t)((uint32_t)(0xC0000001ULL)) != 0) goto loc_00684BDA;
    if (((uint8_t)(v_cr8)) <= 1) goto loc_00684B41;
loc_00684B37:
    goto loc_00684E3F;
loc_00684B41:
    if (result >= ((uint32_t)(0xC00000F2ULL))) goto loc_00684BA8;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (1));
    if (condition_is_equal) goto loc_00684B6B;
    result = ProbeForWrite(result, (uint32_t)(Arg3), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    goto loc_00684B93;
loc_00684B6B:
    if (((result) & ((uint32_t)(Arg3) - 1)) != 0) {
        result = ExRaiseDatatypeMisalignment((uint32_t)(Arg3) - 1, (uint32_t)(Arg3), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
    if ((result + (uint32_t)(Arg3) * 1) > result) goto loc_00684B91;
    if ((result + (uint32_t)(Arg3) * 1) < result) {
        result = *(uint8_t *)(result);
    }
    if ((uint32_t)(local_rsi) == 0) goto loc_00684DE7;
    goto loc_00684D83;
loc_00684BA8:
    v_stack_mC8 = result;
    v_stack_mB8 = (uint32_t)((uint32_t)(Arg3));
    v_stack_mC0 = 1;
    v_stack_mB4 = Arg4;
    v_stack_mB0 = (uint32_t)((uint32_t)(Arg5));
    result = KeGenericCallDpc(v_rip + 676, v_stack_mC8, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    goto loc_00684E3F;
loc_00684BDA:
    Arg2 = 0;
    result = MmIsAddressValidEx(result, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    if ((uint8_t)(result) != 0) goto loc_00684C1E;
    if (!sign_flag) goto loc_00684C08;
    result = MiDbgPteWriteInProgress(result, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_mA8, Arg4);
    goto loc_00684C0B;
loc_00684C08:
loc_00684C0B:
    if (local_rsi != 0) goto loc_00684CBB;
    goto loc_00684E3D;
loc_00684C1E:
    if ((((uint8_t)((uint32_t)(Arg5))) & (65)) == 0) goto loc_00684C89;
    if (((*(uint64_t *)(v_rip + 0x941E59)) & (0x10000000ULL)) == 0) goto loc_00684C89;
    result = MmGetPhysicalAddress(local_rsi, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_mA8, Arg4);
    result = (result) >> (12);
    Arg2 = (result + result * 2) + (result + result * 2);
    if (result <= (*(uint64_t *)(v_rip + 0x7A9095))) goto loc_00684C51;
    goto loc_00684C66;
loc_00684C51:
    result = (*(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(0xC00000EFULL))) + Arg2 * 8)) >> (54);
    result = (uint32_t)((result) & (1));
loc_00684C66:
    if ((uint32_t)(result) == 0) goto loc_00684C89;
    Arg3 = 0;
    Arg2 = 0;
    result = MiDbgPatchIdentity(result + Arg2 * 8, Arg2, Arg3, Arg4);
    local_rdi = (uint32_t)(Arg5);
    if ((uint32_t)(result) != 0) {
        local_rdi = (uint32_t)(((uint32_t)(Arg5)) | (64));
    }
    if ((((uint8_t)(local_rdi)) & (64)) == 0) goto loc_00684CBE;
    result = MmGetPhysicalAddress(local_rsi, Arg2, Arg3, Arg4);
    result = MiDbgTranslatePhysicalAddress(result, (uint32_t)((uint32_t)(local_rdi)), v_stack_mA8, Arg4);
    if (result != 0) goto loc_00684CBB;
    goto loc_00684E3D;
loc_00684CBB:
    local_rdi = (uint32_t)((local_rdi) | (2));
loc_00684CBE:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (6));
    if (((uint32_t)(Arg1)) != 4) goto loc_00684CD3;
    if ((*(uint32_t *)(v_rip + 0x941F22)) != ((uint32_t)((uint32_t)(0xC0000001ULL)))) {
    }
    if (((1) & ((uint8_t)(local_rdi))) == 0) goto loc_00684DE7;
    if (((uint32_t)(Arg1)) != 2) goto loc_00684CF5;
    if (v_stack_m80 == ((uint32_t)(0xC0000001ULL))) goto loc_00684CF5;
    goto loc_00684DFC;
loc_00684CF5:
    v_stack_m100 = v_stack_m70;
    v_stack_m108 = v_stack_mE0;
    result = MiDbgWriteCheck(result, v_stack_mD8, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(v_stack_mA8));
    if ((uint32_t)(result) != 0) goto loc_00684D35;
    goto loc_00684DFC;
loc_00684D35:
    local_rbx = (uint32_t)((local_rbx) | (1));
    if ((((uint8_t)(local_rdi)) & (2)) == 0) goto loc_00684D83;
    if (v_stack_m80 == ((uint32_t)(0xC00000EFULL))) goto loc_00684D83;
    result = MiAllocateDbgPatches(result, (uint32_t)((uint32_t)((uint32_t)(Arg3))), v_stack_mA8, v_stack_m60);
    if (sign_flag) goto loc_00684DFC;
    result = MiFillDbgPatches(result, (uint32_t)((uint32_t)((uint32_t)(Arg3))), v_stack_m60, 1);
loc_00684D83:
    v_stack_mF0 = (uint32_t)((uint32_t)((uint32_t)(result)));
    v_stack_m100 = (uint32_t)((uint32_t)(v_stack_mE8));
    v_stack_m108 = (uint32_t)((uint32_t)(Arg3));
    result = MiCopyToUntrustedMemory(result, v_stack_mE0, v_stack_m70, v_stack_mD0);
    if ((((uint8_t)(local_rdi)) & (2)) == 0) goto loc_00684DFC;
    if (v_stack_m80 == 0) goto loc_00684DFC;
    Arg4 = 0;
    result = MiFillDbgPatches(result, (uint32_t)((uint32_t)((uint32_t)(Arg3))), v_stack_m60, Arg4);
    result = 0;
    goto loc_00684DFC;
loc_00684DE7:
    result = MiCopyFromUntrustedMemory((uint32_t)((uint32_t)(result)), 0, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)(v_stack_mE8));
loc_00684DFC:
    result = (uint8_t)(((uint32_t)((uint32_t)(local_rdi))) & (6));
    if (((uint8_t)(result)) != 4) goto loc_00684E15;
    if (((uint32_t)(local_rbx)) >= 2) goto loc_00684E15;
    if ((*(uint32_t *)(v_rip + 0x941DE0)) != 0) {
    }
    if (((1) & ((uint8_t)(local_rbx))) != 0) {
        Arg3 = (uint32_t)(local_rdi);
        Arg2 = v_stack_mD8;
        Arg1 = result;
        result = MiDbgReleaseAddress(Arg1, Arg2, Arg3, (uint32_t)(v_stack_mE8));
    }
    if ((((uint8_t)(local_rdi)) & (2)) != 0) {
        Arg1 = v_stack_mA8;
        result = MiDbgUnTranslatePhysicalAddress(Arg1, Arg2, Arg3, (uint32_t)(v_stack_mE8));
    }
loc_00684E3F:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, (uint32_t)(v_stack_mE8));
    local_rsp = (local_rsp) + (240);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `- 0x1` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00684A18&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
