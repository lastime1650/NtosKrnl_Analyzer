# MiProcessLargeCoalesceCandidates

- RVA: `0x00379DF4`–`0x0037A3DD` (길이 `1,513` bytes)
- VA: `0x0000000140379DF4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007B000`
- 디코드: `357`개 명령, `1,513/1,513` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00379E64` → [MiReferencePageRuns](MiReferencePageRuns_function_00379540.md) (function, `0x00379540`)
- `0x0037A1EB` → [MiProcessLargeCoalesceBitmapCandidates](MiProcessLargeCoalesceBitmapCandidates_function_0037A3F0.md) (function, `0x0037A3F0`)
- `0x0037A237` → [MiAccumulateTimeBoundTime](../4D/MiAccumulateTimeBoundTime_function_004D5FAC.md) (function, `0x004D5FAC`)
- `0x0037A3D3` → [MiDereferencePageRuns](../3B/MiDereferencePageRuns_function_003BD388.md) (function, `0x003BD388`)

### Direct callers
- [MiPerformOnDemandLargePageCoalesce](MiPerformOnDemandLargePageCoalesce_function_00379678.md) at `0x0037977B`
- [MiRebuildLargePagesThread](MiRebuildLargePagesThread_function_00379AC0.md) at `0x00379CF3`
- [sub_006E43FC](../6E/Unknown_function_006E43FC.md) at `0x006E4406`

### Static image references
- `0x00379E7F` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00379EDC` → RVA `0x00E3CCF8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00379F08` → [sub_006E4446](../6E/Unknown_function_006E4446.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00379DF4  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
00379DF8  53                              push rbx
00379DF9  55                              push rbp
00379DFA  56                              push rsi
00379DFB  57                              push rdi
00379DFC  41 54                           push r12
00379DFE  41 55                           push r13
00379E00  41 56                           push r14
00379E02  41 57                           push r15
00379E04  48 81 EC D8 00 00 00            sub rsp, 0xd8
00379E0B  49 8B F0                        mov rsi, r8
00379E0E  44 8B E2                        mov r12d, edx
00379E11  4C 8B E9                        mov r13, rcx
00379E14  44 0F 20 C0                     mov rax, cr8
00379E18  48 83 A4 24 88 00 00 00 00      and qword ptr [rsp + 0x88], 0
00379E21  4B 8D 2C 64                     lea rbp, [r12 + r12*2]
00379E25  48 C1 E5 04                     shl rbp, 4
00379E29  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00379E31  33 C0                           xor eax, eax
00379E33  89 84 24 20 01 00 00            mov dword ptr [rsp + 0x120], eax
00379E3A  44 8B F2                        mov r14d, edx
00379E3D  48 89 6C 24 68                  mov qword ptr [rsp + 0x68], rbp
00379E42  8D 78 01                        lea edi, [rax + 1]
00379E45  4D 85 C0                        test r8, r8
00379E48  0F 84 6D 04 00 00               je 0x14037a2bb
00379E4E  49 8B 40 18                     mov rax, qword ptr [r8 + 0x18]
00379E52  8B D7                           mov edx, edi
00379E54  4A 8B 84 E0 30 DF 00 00         mov rax, qword ptr [rax + r12*8 + 0xdf30]
00379E5C  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
00379E64  E8 D7 F6 FF FF                  call 0x140379540
00379E69  4C 8B C0                        mov r8, rax
00379E6C  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00379E71  44 8B 08                        mov r9d, dword ptr [rax]
00379E74  4A 8D 14 0F                     lea rdx, [rdi + r9]
00379E78  48 C1 E2 04                     shl rdx, 4
00379E7C  48 03 D0                        add rdx, rax
00379E7F  4C 8D 1D 7A 61 C8 FF            lea r11, [rip - 0x379e86]
00379E86  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
00379E8B  43 8B 84 A3 E8 35 01 00         mov eax, dword ptr [r11 + r12*4 + 0x135e8]
00379E93  4C 8B D7                        mov r10, rdi
00379E96  43 8A 8C E3 28 11 01 00         mov cl, byte ptr [r11 + r12*8 + 0x11128]
00379E9E  4B 8B 9C E3 60 1C 01 00         mov rbx, qword ptr [r11 + r12*8 + 0x11c60]
00379EA6  2A C8                           sub cl, al
00379EA8  49 D3 E2                        shl r10, cl
00379EAB  49 8B C6                        mov rax, r14
00379EAE  48 C1 E0 04                     shl rax, 4
00379EB2  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
00379EB7  4C 89 94 24 38 01 00 00         mov qword ptr [rsp + 0x138], r10
00379EBF  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00379EC4  45 85 E4                        test r12d, r12d
00379EC7  0F 84 30 04 00 00               je 0x14037a2fd
00379ECD  41 BF 02 00 00 00               mov r15d, 2
00379ED3  44 3B E7                        cmp r12d, edi
00379ED6  0F 84 EE 03 00 00               je 0x14037a2ca
00379EDC  48 8B 2D 15 2E AC 00            mov rbp, qword ptr [rip + 0xac2e15]
00379EE3  48 83 64 24 78 00               and qword ptr [rsp + 0x78], 0
00379EE9  48 89 6C 24 50                  mov qword ptr [rsp + 0x50], rbp
00379EEE  4A 8B AC 28 10 40 00 00         mov rbp, qword ptr [rax + r13 + 0x4010]
00379EF6  48 89 6C 24 60                  mov qword ptr [rsp + 0x60], rbp
00379EFB  45 85 C9                        test r9d, r9d
00379EFE  75 46                           jne 0x140379f46
00379F00  BB 05 01 00 00                  mov ebx, 0x105
00379F05  48 85 F6                        test rsi, rsi
00379F08  0F 85 38 A5 36 00               jne 0x1406e4446
00379F0E  8B AC 24 20 01 00 00            mov ebp, dword ptr [rsp + 0x120]
00379F15  41 BC 2D 02 00 C0               mov r12d, 0xc000022d
00379F1B  85 ED                           test ebp, ebp
00379F1D  41 0F 45 DC                     cmovne ebx, r12d
00379F21  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00379F26  48 85 C9                        test rcx, rcx
00379F29  0F 85 A4 04 00 00               jne 0x14037a3d3
00379F2F  8B C3                           mov eax, ebx
00379F31  48 81 C4 D8 00 00 00            add rsp, 0xd8
00379F38  41 5F                           pop r15
00379F3A  41 5E                           pop r14
00379F3C  41 5D                           pop r13
00379F3E  41 5C                           pop r12
00379F40  5F                              pop rdi
00379F41  5E                              pop rsi
00379F42  5D                              pop rbp
00379F43  5B                              pop rbx
00379F44  C3                              ret
00379F45  CC                              int3
00379F46  41 FF C9                        dec r9d
00379F49  4C 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], r9
00379F51  48 85 F6                        test rsi, rsi
00379F54  0F 85 BF 03 00 00               jne 0x14037a319
00379F5A  4D 8B 9D 48 48 00 00            mov r11, qword ptr [r13 + 0x4848]
00379F61  33 D2                           xor edx, edx
00379F63  4C 03 DF                        add r11, rdi
00379F66  4C 8D 52 FF                     lea r10, [rdx - 1]
00379F6A  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
00379F6F  4C 03 D3                        add r10, rbx
00379F72  48 8D 43 FF                     lea rax, [rbx - 1]
00379F76  48 F7 D0                        not rax
00379F79  4C 23 D0                        and r10, rax
00379F7C  4C 23 D8                        and r11, rax
00379F7F  4C 89 94 24 98 00 00 00         mov qword ptr [rsp + 0x98], r10
00379F87  4D 3B D3                        cmp r10, r11
00379F8A  0F 83 1E 03 00 00               jae 0x14037a2ae
00379F90  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00379F95  48 8D 0D 64 60 C8 FF            lea rcx, [rip - 0x379f9c]
00379F9C  4A 8B 8C F1 28 11 01 00         mov rcx, qword ptr [rcx + r14*8 + 0x11128]
00379FA4  4C 2B DF                        sub r11, rdi
00379FA7  49 8B DA                        mov rbx, r10
00379FAA  4C 89 9C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r11
00379FB2  48 D3 EB                        shr rbx, cl
00379FB5  49 8B D3                        mov rdx, r11
00379FB8  4A 8B 84 28 08 40 00 00         mov rax, qword ptr [rax + r13 + 0x4008]
00379FC0  48 D3 EA                        shr rdx, cl
00379FC3  48 FF C8                        dec rax
00379FC6  48 3B D0                        cmp rdx, rax
00379FC9  48 0F 42 C2                     cmovb rax, rdx
00379FCD  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
00379FD5  4C 8D 60 01                     lea r12, [rax + 1]
00379FD9  4C 89 A4 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], r12
00379FE1  83 A4 24 30 01 00 00 00         and dword ptr [rsp + 0x130], 0
00379FE9  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
00379FEE  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
00379FF3  4C 8B 8C 24 80 00 00 00         mov r9, qword ptr [rsp + 0x80]
00379FFB  4C 3B E3                        cmp r12, rbx
00379FFE  0F 86 A5 02 00 00               jbe 0x14037a2a9
0037A004  48 C1 E8 06                     shr rax, 6
0037A008  8A CB                           mov cl, bl
0037A00A  80 E1 3F                        and cl, 0x3f
0037A00D  45 33 C0                        xor r8d, r8d
0037A010  4C 8D 14 C5 00 00 00 00         lea r10, [rax*8]
0037A018  48 8B C3                        mov rax, rbx
0037A01B  48 C1 E8 06                     shr rax, 6
0037A01F  4C 03 D5                        add r10, rbp
0037A022  4C 8D 0C C5 00 00 00 00         lea r9, [rax*8]
0037A02A  48 8B C7                        mov rax, rdi
0037A02D  48 D3 E0                        shl rax, cl
0037A030  4C 03 CD                        add r9, rbp
0037A033  48 2B C7                        sub rax, rdi
0037A036  48 F7 D0                        not rax
0037A039  49 8B 11                        mov rdx, qword ptr [r9]
0037A03C  48 23 D0                        and rdx, rax
0037A03F  49 8D 41 08                     lea rax, [r9 + 8]
0037A043  48 85 D2                        test rdx, rdx
0037A046  0F 84 9C 02 00 00               je 0x14037a2e8
0037A04C  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0037A051  49 8B E9                        mov rbp, r9
0037A054  48 2B EB                        sub rbp, rbx
0037A057  48 0F BC CA                     bsf rcx, rdx
0037A05B  48 C1 FD 03                     sar rbp, 3
0037A05F  48 C1 E5 06                     shl rbp, 6
0037A063  8B C1                           mov eax, ecx
0037A065  48 03 E8                        add rbp, rax
0037A068  89 8C 24 30 01 00 00            mov dword ptr [rsp + 0x130], ecx
0037A06F  49 3B EC                        cmp rbp, r12
0037A072  0F 87 D0 02 00 00               ja 0x14037a348
0037A078  48 8B C7                        mov rax, rdi
0037A07B  48 D3 E0                        shl rax, cl
0037A07E  48 2B C7                        sub rax, rdi
0037A081  48 0B D0                        or rdx, rax
0037A084  48 F7 D2                        not rdx
0037A087  48 85 D2                        test rdx, rdx
0037A08A  75 15                           jne 0x14037a0a1
0037A08C  49 8D 41 08                     lea rax, [r9 + 8]
0037A090  49 3B C2                        cmp rax, r10
0037A093  0F 87 76 02 00 00               ja 0x14037a30f
0037A099  48 8B 10                        mov rdx, qword ptr [rax]
0037A09C  4C 8B C8                        mov r9, rax
0037A09F  EB E3                           jmp 0x14037a084
0037A0A1  48 0F BC C2                     bsf rax, rdx
0037A0A5  4D 8B C1                        mov r8, r9
0037A0A8  89 84 24 30 01 00 00            mov dword ptr [rsp + 0x130], eax
0037A0AF  4C 2B C3                        sub r8, rbx
0037A0B2  49 C1 F8 03                     sar r8, 3
0037A0B6  49 C1 E0 06                     shl r8, 6
0037A0BA  4C 03 C0                        add r8, rax
0037A0BD  4D 3B C4                        cmp r8, r12
0037A0C0  4D 0F 47 C4                     cmova r8, r12
0037A0C4  4C 2B C5                        sub r8, rbp
0037A0C7  4D 85 C0                        test r8, r8
0037A0CA  0F 84 C2 01 00 00               je 0x14037a292
0037A0D0  48 8B 84 24 38 01 00 00         mov rax, qword ptr [rsp + 0x138]
0037A0D8  49 8D 1C 28                     lea rbx, [r8 + rbp]
0037A0DC  49 0F AF C7                     imul rax, r15
0037A0E0  4C 8B E5                        mov r12, rbp
0037A0E3  48 89 9C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rbx
0037A0EB  4C 0F AF A4 24 38 01 00 00      imul r12, qword ptr [rsp + 0x138]
0037A0F4  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
0037A0FC  4D 0F AF E7                     imul r12, r15
0037A100  4C 03 64 24 50                  add r12, qword ptr [rsp + 0x50]
0037A105  48 3B EB                        cmp rbp, rbx
0037A108  0F 83 3C 01 00 00               jae 0x14037a24a
0037A10E  48 85 F6                        test rsi, rsi
0037A111  75 4A                           jne 0x14037a15d
0037A113  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0037A118  4C 8B D5                        mov r10, rbp
0037A11B  41 83 E2 1F                     and r10d, 0x1f
0037A11F  48 8B CD                        mov rcx, rbp
0037A122  48 C1 E9 05                     shr rcx, 5
0037A126  4C 8B CF                        mov r9, rdi
0037A129  4A 89 AC 28 78 40 00 00         mov qword ptr [rax + r13 + 0x4078], rbp
0037A131  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0037A136  4A 8B 84 28 10 40 00 00         mov rax, qword ptr [rax + r13 + 0x4010]
0037A13E  4C 8D 04 88                     lea r8, [rax + rcx*4]
0037A142  49 8D 42 01                     lea rax, [r10 + 1]
0037A146  48 83 F8 20                     cmp rax, 0x20
0037A14A  0F 87 86 01 00 00               ja 0x14037a2d6
0037A150  41 8B CA                        mov ecx, r10d
0037A153  8B C7                           mov eax, edi
0037A155  D3 E0                           shl eax, cl
0037A157  F7 D0                           not eax
0037A159  F0 41 21 00                     lock and dword ptr [r8], eax
0037A15D  48 8D 05 9C 5E C8 FF            lea rax, [rip - 0x37a164]
0037A164  4C 8B D5                        mov r10, rbp
0037A167  4A 8B 8C F0 28 11 01 00         mov rcx, qword ptr [rax + r14*8 + 0x11128]
0037A16F  4D 8B CC                        mov r9, r12
0037A172  49 D3 E2                        shl r10, cl
0037A175  48 8D 45 01                     lea rax, [rbp + 1]
0037A179  48 8B E8                        mov rbp, rax
0037A17C  48 D3 E0                        shl rax, cl
0037A17F  48 8B 8C 24 38 01 00 00         mov rcx, qword ptr [rsp + 0x138]
0037A187  48 2B C7                        sub rax, rdi
0037A18A  48 FF C9                        dec rcx
0037A18D  49 0F AF CF                     imul rcx, r15
0037A191  49 03 CC                        add rcx, r12
0037A194  49 3B C3                        cmp rax, r11
0037A197  0F 86 A1 01 00 00               jbe 0x14037a33e
0037A19D  49 2B C3                        sub rax, r11
0037A1A0  33 D2                           xor edx, edx
0037A1A2  4C 8B 5C 24 48                  mov r11, qword ptr [rsp + 0x48]
0037A1A7  49 F7 F3                        div r11
0037A1AA  49 0F AF C7                     imul rax, r15
0037A1AE  48 2B C8                        sub rcx, rax
0037A1B1  4C 8B 84 24 98 00 00 00         mov r8, qword ptr [rsp + 0x98]
0037A1B9  4D 3B D0                        cmp r10, r8
0037A1BC  0F 82 E8 01 00 00               jb 0x14037a3aa
0037A1C2  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
0037A1CA  49 8B D2                        mov rdx, r10
0037A1CD  44 8B 84 24 28 01 00 00         mov r8d, dword ptr [rsp + 0x128]
0037A1D5  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
0037A1DA  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0037A1DE  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
0037A1E3  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0037A1E8  49 8B CD                        mov rcx, r13
0037A1EB  E8 00 02 00 00                  call 0x14037a3f0
0037A1F0  8B D8                           mov ebx, eax
0037A1F2  48 85 F6                        test rsi, rsi
0037A1F5  74 6D                           je 0x14037a264
0037A1F7  3D 2D 02 00 C0                  cmp eax, 0xc000022d
0037A1FC  0F 84 C5 01 00 00               je 0x14037a3c7
0037A202  8B 84 24 20 01 00 00            mov eax, dword ptr [rsp + 0x120]
0037A209  89 84 24 20 01 00 00            mov dword ptr [rsp + 0x120], eax
0037A210  81 FB 05 01 00 00               cmp ebx, 0x105
0037A216  0F 85 05 FD FF FF               jne 0x140379f21
0037A21C  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0037A221  48 03 C7                        add rax, rdi
0037A224  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0037A229  A8 1F                           test al, 0x1f
0037A22B  75 48                           jne 0x14037a275
0037A22D  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
0037A231  33 D2                           xor edx, edx
0037A233  48 83 C1 28                     add rcx, 0x28
0037A237  E8 70 BD 15 00                  call 0x1404d5fac
0037A23C  85 C0                           test eax, eax
0037A23E  74 35                           je 0x14037a275
0037A240  BB 02 01 00 00                  mov ebx, 0x102
0037A245  E9 D7 FC FF FF                  jmp 0x140379f21
0037A24A  4C 8B A4 24 B8 00 00 00         mov r12, qword ptr [rsp + 0xb8]
0037A252  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
0037A25A  48 8B 6C 24 60                  mov rbp, qword ptr [rsp + 0x60]
0037A25F  E9 7D FD FF FF                  jmp 0x140379fe1
0037A264  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0037A269  4A C7 84 28 78 40 00 00 FE FF FF FF  mov qword ptr [rax + r13 + 0x4078], 0xfffffffffffffffe
0037A275  4C 03 A4 24 A0 00 00 00         add r12, qword ptr [rsp + 0xa0]
0037A27D  4C 8B 9C 24 A8 00 00 00         mov r11, qword ptr [rsp + 0xa8]
0037A285  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
0037A28D  E9 73 FE FF FF                  jmp 0x14037a105
0037A292  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
0037A297  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
0037A29C  4C 8B 8C 24 80 00 00 00         mov r9, qword ptr [rsp + 0x80]
0037A2A4  48 8B 6C 24 60                  mov rbp, qword ptr [rsp + 0x60]
0037A2A9  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
0037A2AE  4C 8B 94 24 38 01 00 00         mov r10, qword ptr [rsp + 0x138]
0037A2B6  E9 40 FC FF FF                  jmp 0x140379efb
0037A2BB  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
0037A2C0  33 D2                           xor edx, edx
0037A2C2  44 8B CF                        mov r9d, edi
0037A2C5  E9 B5 FB FF FF                  jmp 0x140379e7f
0037A2CA  49 8B AD 00 40 00 00            mov rbp, qword ptr [r13 + 0x4000]
0037A2D1  E9 0D FC FF FF                  jmp 0x140379ee3
0037A2D6  4D 85 D2                        test r10, r10
0037A2D9  75 75                           jne 0x14037a350
0037A2DB  49 8B C9                        mov rcx, r9
0037A2DE  83 C8 FF                        or eax, 0xffffffff
0037A2E1  D3 E0                           shl eax, cl
0037A2E3  E9 71 FE FF FF                  jmp 0x14037a159
0037A2E8  49 3B C2                        cmp rax, r10
0037A2EB  77 5B                           ja 0x14037a348
0037A2ED  49 83 C1 08                     add r9, 8
0037A2F1  48 83 C0 08                     add rax, 8
0037A2F5  49 8B 11                        mov rdx, qword ptr [r9]
0037A2F8  E9 46 FD FF FF                  jmp 0x14037a043
0037A2FD  49 8B AD 38 40 00 00            mov rbp, qword ptr [r13 + 0x4038]
0037A304  41 BF 04 00 00 00               mov r15d, 4
0037A30A  E9 D4 FB FF FF                  jmp 0x140379ee3
0037A30F  B8 40 00 00 00                  mov eax, 0x40
0037A314  E9 8C FD FF FF                  jmp 0x14037a0a5
0037A319  8B 46 0C                        mov eax, dword ptr [rsi + 0xc]
0037A31C  41 8B C9                        mov ecx, r9d
0037A31F  42 39 04 CA                     cmp dword ptr [rdx + r9*8], eax
0037A323  0F 85 D2 FB FF FF               jne 0x140379efb
0037A329  48 03 C9                        add rcx, rcx
0037A32C  49 8B 54 C8 10                  mov rdx, qword ptr [r8 + rcx*8 + 0x10]
0037A331  4D 8B 5C C8 18                  mov r11, qword ptr [r8 + rcx*8 + 0x18]
0037A336  4C 03 DA                        add r11, rdx
0037A339  E9 28 FC FF FF                  jmp 0x140379f66
0037A33E  4C 8B 5C 24 48                  mov r11, qword ptr [rsp + 0x48]
0037A343  E9 69 FE FF FF                  jmp 0x14037a1b1
0037A348  49 8B EC                        mov rbp, r12
0037A34B  E9 77 FD FF FF                  jmp 0x14037a0c7
0037A350  8B C5                           mov eax, ebp
0037A352  BA 20 00 00 00                  mov edx, 0x20
0037A357  83 E0 1F                        and eax, 0x1f
0037A35A  2B D0                           sub edx, eax
0037A35C  8B C7                           mov eax, edi
0037A35E  8B CA                           mov ecx, edx
0037A360  D3 E0                           shl eax, cl
0037A362  49 8B CA                        mov rcx, r10
0037A365  2B C7                           sub eax, edi
0037A367  D3 E0                           shl eax, cl
0037A369  F7 D0                           not eax
0037A36B  F0 41 21 00                     lock and dword ptr [r8], eax
0037A36F  8B C2                           mov eax, edx
0037A371  49 83 C0 04                     add r8, 4
0037A375  4C 2B C8                        sub r9, rax
0037A378  49 83 F9 20                     cmp r9, 0x20
0037A37C  72 1E                           jb 0x14037a39c
0037A37E  49 8B D1                        mov rdx, r9
0037A381  48 C1 EA 05                     shr rdx, 5
0037A385  48 6B C2 E0                     imul rax, rdx, -0x20
0037A389  4C 03 C8                        add r9, rax
0037A38C  41 C7 00 00 00 00 00            mov dword ptr [r8], 0
0037A393  49 83 C0 04                     add r8, 4
0037A397  48 2B D7                        sub rdx, rdi
0037A39A  75 F0                           jne 0x14037a38c
0037A39C  4D 85 C9                        test r9, r9
0037A39F  0F 84 B8 FD FF FF               je 0x14037a15d
0037A3A5  E9 31 FF FF FF                  jmp 0x14037a2db
0037A3AA  33 D2                           xor edx, edx
0037A3AC  49 8B C0                        mov rax, r8
0037A3AF  49 2B C2                        sub rax, r10
0037A3B2  4D 8B D0                        mov r10, r8
0037A3B5  49 F7 F3                        div r11
0037A3B8  4C 8B C8                        mov r9, rax
0037A3BB  4D 0F AF CF                     imul r9, r15
0037A3BF  4D 03 CC                        add r9, r12
0037A3C2  E9 FB FD FF FF                  jmp 0x14037a1c2
0037A3C7  89 BC 24 20 01 00 00            mov dword ptr [rsp + 0x120], edi
0037A3CE  E9 49 FE FF FF                  jmp 0x14037a21c
0037A3D3  E8 B0 2F 04 00                  call 0x1403bd388
0037A3D8  E9 52 FB FF FF                  jmp 0x140379f2f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiProcessLargeCoalesceCandidates(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_p10;
    unsigned int v_stack_p120;
    unsigned int v_stack_p128;
    unsigned int v_stack_p130;
    unsigned __int64 v_stack_p138;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned int v_stack_p8;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pC0;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (216);
    v_rbp = ((unsigned int)(a2) + (unsigned int)(a2) * 2) << (4);
    v_stack_m88 = v_cr8;
    result = 0;
    v_stack_p8 = 0;
    v_stack_mB0 = v_rbp;
    if (a3 == 0) goto loc_0037A2BB;
    v_stack_m90 = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 24) + (unsigned int)(a2) * 8 + 57136);
    result = MiReferencePageRuns(a1, (unsigned int)((unsigned int)(result + 1)), a3, a4);
    v_stack_mC0 = result;
    a2 = (result + 1 + (unsigned int)(*(unsigned int *)(result)) * 1) << (4);
    a2 = (a2) + (result);
loc_00379E7F:
    v_stack_mD8 = a2;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_rip - 3645062 + (unsigned int)(a2) * 8 + 69928)) - ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip - 3645062 + (unsigned int)(a2) * 4 + 79336)))));
    v_r10 = (result + 1) << ((unsigned __int8)(a1));
    result = ((unsigned int)(a2)) << (4);
    v_stack_mD0 = *(unsigned __int64 *)(v_rip - 3645062 + (unsigned int)(a2) * 8 + 72800);
    v_stack_p20 = v_r10;
    v_stack_mA8 = result;
    if ((unsigned int)((unsigned int)(a2)) == 0) goto loc_0037A2FD;
    if (((unsigned int)((unsigned int)(a2))) == ((unsigned int)(result + 1))) goto loc_0037A2CA;
loc_00379EE3:
    v_stack_mC8 = *(unsigned __int64 *)(v_rip + 11283989);
    v_stack_mB8 = *(unsigned __int64 *)(result + a1 * 1 + 16400);
loc_00379EFB:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result))) != 0) goto loc_00379F46;
    v_rbx = 261;
    if ((unsigned int)((unsigned int)(v_stack_p8)) != 0) { v_rbx = (unsigned int)((unsigned int)(0xC000022DULL)); }
loc_00379F21:
    if (v_stack_mC0 != 0) goto loc_0037A3D3;
loc_00379F2F:
    v_rsp = (v_rsp) + (216);
    return (unsigned int)((unsigned int)(v_rbx));
loc_00379F46:
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(result))) - 1);
    v_stack_p80 = a4;
    if (a3 != 0) goto loc_0037A319;
    a2 = 0;
    v_r11 = (*(unsigned __int64 *)(a1 + 18504)) + (result + 1);
loc_00379F66:
    v_r10 = (a2 - 1) + (v_rbx);
    result = ~(v_rbx - 1);
    v_r10 = (v_r10) & (result);
    v_r11 = (v_r11) & (result);
    v_stack_p98 = v_r10;
    if (v_r10 >= v_r11) goto loc_0037A2AE;
    v_r11 = (v_r11) - (result + 1);
    v_stack_pA8 = v_r11;
    v_rbx = (v_r10) >> ((unsigned __int8)(*(unsigned __int64 *)(v_rip - 3645340 + (unsigned int)(a2) * 8 + 69928)));
    a2 = (v_r11) >> ((unsigned __int8)(*(unsigned __int64 *)(v_rip - 3645340 + (unsigned int)(a2) * 8 + 69928)));
    result = (*(unsigned __int64 *)(v_stack_p70 + a1 * 1 + 16392)) - 1;
    if (a2 < result) { result = a2; }
    v_stack_pC0 = result;
    v_stack_pB8 = result + 1;
loc_00379FE1:
    if ((result + 1) <= v_rbx) goto loc_0037A2A9;
    result = (result) >> (6);
    a1 = (unsigned __int8)(((unsigned __int8)(v_rbx)) & (63));
    a3 = 0;
    result = (v_rbx) >> (6);
    v_r10 = (result * 8) + ((unsigned int)(v_stack_p8));
    result = (result + 1) << ((unsigned __int8)(a1));
    a4 = (result * 8) + ((unsigned int)(v_stack_p8));
    result = (result) - (result + 1);
    result = ~(result);
    a2 = (*(unsigned __int64 *)(a4)) & (result);
loc_0037A043:
    if (a2 == 0) goto loc_0037A2E8;
    v_rbp = (a4) - (v_stack_p60);
    v_rbp = (v_rbp) >> (3);
    v_rbp = (v_rbp) << (6);
    v_rbp = (v_rbp) + ((unsigned int)((unsigned int)(a1)));
    v_stack_p130 = (unsigned int)(a1);
    if (v_rbp > (result + 1)) goto loc_0037A348;
    result = (result + 1) << ((unsigned __int8)(a1));
    result = (result) - (result + 1);
    a2 = (a2) | (result);
loc_0037A084:
    a2 = ~(a2);
    if (a2 != 0) goto loc_0037A0A1;
    if ((a4 + 8) > v_r10) goto loc_0037A30F;
    goto loc_0037A084;
loc_0037A0A1:
loc_0037A0A5:
    v_stack_p130 = (unsigned int)(a4 + 8);
    a3 = (a4 + 8) - (v_stack_p60);
    a3 = (a3) >> (3);
    a3 = (a3) << (6);
    a3 = (a3) + (a4 + 8);
    if (a3 > (result + 1)) { a3 = result + 1; }
    a3 = (a3) - (v_rbp);
loc_0037A0C7:
    if (a3 == 0) goto loc_0037A292;
    result = (v_stack_p138) * (2);
    v_stack_pB0 = a3 + v_rbp * 1;
    v_r12 = (v_rbp) * (v_stack_p138);
    v_stack_pA0 = result;
    v_r12 = (v_r12) * (2);
    v_r12 = (v_r12) + (v_stack_p50);
loc_0037A105:
    if (v_rbp >= (a3 + v_rbp * 1)) goto loc_0037A24A;
    if (a3 != 0) goto loc_0037A15D;
    v_r10 = (unsigned int)((v_rbp) & (31));
    a1 = (v_rbp) >> (5);
    *(unsigned __int64 *)(v_stack_p68 + a1 * 1 + 16504) = v_rbp;
    if ((v_r10 + 1) > 32) goto loc_0037A2D6;
    result = (unsigned int)(((unsigned int)((unsigned int)(result + 1))) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r10)))));
    result = (unsigned int)(~(result));
loc_0037A159:
loc_0037A15D:
    v_r10 = (v_rbp) << ((unsigned __int8)(*(unsigned __int64 *)(v_rip - 3645796 + (unsigned int)(a2) * 8 + 69928)));
    result = (v_rbp + 1) << ((unsigned __int8)(*(unsigned __int64 *)(v_rip - 3645796 + (unsigned int)(a2) * 8 + 69928)));
    result = (result) - (result + 1);
    a1 = (v_stack_p138) - 1;
    a1 = (a1) * (2);
    a1 = (a1) + (v_r12);
    if (result <= v_r11) goto loc_0037A33E;
    result = (result) - (v_r11);
    a2 = 0;
    result = (result) * (2);
    a1 = (a1) - (result);
loc_0037A1B1:
    if (v_r10 < v_stack_p98) goto loc_0037A3AA;
loc_0037A1C2:
    v_stack_p38 = a3;
    v_stack_p30 = (unsigned __int8)(v_stack_p90);
    v_stack_p28 = 2;
    v_stack_p20 = a1;
    result = MiProcessLargeCoalesceBitmapCandidates(a1, v_r10, (unsigned int)(v_stack_p128), v_r12);
    if (a3 == 0) goto loc_0037A264;
    if (((unsigned int)(result)) == 0xC000022DULL) goto loc_0037A3C7;
    v_stack_p120 = (unsigned int)((unsigned int)(v_stack_p120));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 261) goto loc_00379F21;
loc_0037A21C:
    result = (v_stack_p78) + (result + 1);
    v_stack_p78 = result;
    if ((((unsigned __int8)(result)) & (31)) != 0) goto loc_0037A275;
    a2 = 0;
    a1 = (*(unsigned __int64 *)(a3 + 32)) + (40);
    result = MiAccumulateTimeBoundTime(a1, a2, (unsigned int)(v_stack_p128), v_r12);
    if ((unsigned int)(result) == 0) goto loc_0037A275;
    goto loc_00379F21;
loc_0037A24A:
    goto loc_00379FE1;
loc_0037A264:
    *(unsigned __int64 *)(v_stack_p68 + a1 * 1 + 16504) = -2;
loc_0037A275:
    v_r12 = (v_stack_pB8) + (v_stack_pA0);
    goto loc_0037A105;
loc_0037A292:
loc_0037A2A9:
loc_0037A2AE:
    goto loc_00379EFB;
loc_0037A2BB:
    v_stack_p58 = v_stack_p58;
    a2 = 0;
    goto loc_00379E7F;
loc_0037A2CA:
    goto loc_00379EE3;
loc_0037A2D6:
    if (v_stack_p138 != 0) goto loc_0037A350;
loc_0037A2DB:
    result = (unsigned int)((v_stack_p68) | (0xFFFFFFFFULL));
    result = (unsigned int)((result) << ((unsigned __int8)((unsigned int)((unsigned int)(result + 1)))));
    goto loc_0037A159;
loc_0037A2E8:
    if (result > v_stack_p138) goto loc_0037A348;
    a4 = ((unsigned int)((unsigned int)(result + 1))) + (8);
    result = (result) + (8);
    goto loc_0037A043;
loc_0037A2FD:
    goto loc_00379EE3;
loc_0037A30F:
    goto loc_0037A0A5;
loc_0037A319:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a4) + a4 * 8)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12))))) goto loc_00379EFB;
    a1 = ((unsigned int)((unsigned int)(a4))) + ((unsigned int)((unsigned int)(a4)));
    v_r11 = (*(unsigned __int64 *)(v_stack_p58 + a1 * 8 + 24)) + (*(unsigned __int64 *)(v_stack_p58 + a1 * 8 + 16));
    goto loc_00379F66;
loc_0037A33E:
    goto loc_0037A1B1;
loc_0037A348:
    goto loc_0037A0C7;
loc_0037A350:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) & (31));
    a2 = (unsigned int)((32) - ((unsigned int)(result)));
    result = (unsigned int)(((unsigned int)((unsigned int)(result + 1))) << ((unsigned __int8)((unsigned int)(a2))));
    result = (unsigned int)((result) - ((unsigned int)(result + 1)));
    result = (unsigned int)((result) << ((unsigned __int8)(v_stack_p138)));
    result = (unsigned int)(~(result));
    a3 = (v_stack_p58) + (4);
    a4 = (a4) - ((unsigned int)(a2));
    if (a4 < 32) goto loc_0037A39C;
    a2 = (a4) >> (5);
    result = ((unsigned int)(a2)) * (a2);
    a4 = (a4) + (result);
loc_0037A38C:
    *(unsigned int *)(a3) = 0;
    a3 = (a3) + (4);
    a2 = (a2) - (result + 1);
    if (condition_is_not_equal) goto loc_0037A38C;
loc_0037A39C:
    if (a4 == 0) goto loc_0037A15D;
    goto loc_0037A2DB;
loc_0037A3AA:
    a2 = 0;
    result = (a3) - (v_stack_p138);
    a4 = (result) * (4);
    a4 = (a4) + (v_r12);
    goto loc_0037A1C2;
loc_0037A3C7:
    v_stack_p120 = (unsigned int)(result + 1);
    goto loc_0037A21C;
loc_0037A3D3:
    result = MiDereferencePageRuns(v_stack_p138, a2, a3, a4);
    goto loc_00379F2F;
}
```

## 5. (Beta) C Style

```c
int64_t MiProcessLargeCoalesceCandidates(void *Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_p10;
    uint32_t v_stack_p120;
    uint32_t v_stack_p128;
    uint32_t v_stack_p130;
    uint64_t v_stack_p138;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint8_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint32_t v_stack_p8;
    uint64_t v_stack_p80;
    uint64_t v_stack_p90;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pC0;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (216);
    local_rbp = ((uint32_t)(Arg2) + (uint32_t)(Arg2) * 2) << (4);
    v_stack_m88 = v_cr8;
    result = 0;
    v_stack_p8 = 0;
    v_stack_mB0 = local_rbp;
    if (Arg3 == 0) goto loc_0037A2BB;
    v_stack_m90 = *(uint64_t *)(*(uint64_t *)(Arg3 + 0x18) + (uint32_t)(arg2) * 8 + 0xDF30);
    result = MiReferencePageRuns(Arg1, (uint32_t)((uint32_t)(result + 1)), Arg3, a4);
    v_stack_mC0 = result;
    Arg2 = (result + 1 + (uint32_t)(*(uint32_t *)(result)) * 1) << (4);
    Arg2 = (Arg2) + (result);
loc_00379E7F:
    v_stack_mD8 = Arg2;
    Arg1 = (uint8_t)((*(uint8_t *)(v_rip - 0x379E86 + (uint32_t)(arg2) * 8 + 0x11128)) - ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip - 0x379E86 + (uint32_t)(arg2) * 4 + 0x135E8)))));
    local_r10 = (result + 1) << ((uint8_t)(Arg1));
    result = ((uint32_t)(Arg2)) << (4);
    v_stack_mD0 = *(uint64_t *)(v_rip - 0x379E86 + (uint32_t)(arg2) * 8 + 0x11C60);
    v_stack_p20 = local_r10;
    v_stack_mA8 = result;
    if ((uint32_t)((uint32_t)(Arg2)) == 0) goto loc_0037A2FD;
    if (((uint32_t)((uint32_t)(Arg2))) == ((uint32_t)(result + 1))) goto loc_0037A2CA;
loc_00379EE3:
    v_stack_mC8 = *(uint64_t *)(v_rip + 0xAC2E15);
    v_stack_mB8 = *(uint64_t *)(result + arg1 * 1 + 0x4010);
loc_00379EFB:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result))) != 0) goto loc_00379F46;
    local_rbx = 261;
    if ((uint32_t)((uint32_t)(v_stack_p8)) != 0) { local_rbx = (uint32_t)((uint32_t)(0xC000022DULL)); }
loc_00379F21:
    if (v_stack_mC0 != 0) goto loc_0037A3D3;
loc_00379F2F:
    local_rsp = (local_rsp) + (216);
    return (uint32_t)((uint32_t)(local_rbx));
loc_00379F46:
    a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(result))) - 1);
    v_stack_p80 = a4;
    if (Arg3 != 0) goto loc_0037A319;
    Arg2 = 0;
    local_r11 = (*(uint64_t *)(arg1 + 0x4848)) + (result + 1);
loc_00379F66:
    local_r10 = (Arg2 - 1) + (local_rbx);
    result = ~(local_rbx - 1);
    local_r10 = (local_r10) & (result);
    local_r11 = (local_r11) & (result);
    v_stack_p98 = local_r10;
    if (local_r10 >= local_r11) goto loc_0037A2AE;
    local_r11 = (local_r11) - (result + 1);
    v_stack_pA8 = local_r11;
    local_rbx = (local_r10) >> ((uint8_t)(*(uint64_t *)(v_rip - 0x379F9C + (uint32_t)(arg2) * 8 + 0x11128)));
    Arg2 = (local_r11) >> ((uint8_t)(*(uint64_t *)(v_rip - 0x379F9C + (uint32_t)(arg2) * 8 + 0x11128)));
    result = (*(uint64_t *)(v_stack_p70 + arg1 * 1 + 0x4008)) - 1;
    if (Arg2 < result) { result = Arg2; }
    v_stack_pC0 = result;
    v_stack_pB8 = result + 1;
loc_00379FE1:
    if ((result + 1) <= local_rbx) goto loc_0037A2A9;
    result = (result) >> (6);
    Arg1 = (uint8_t)(((uint8_t)(local_rbx)) & (63));
    Arg3 = 0;
    result = (local_rbx) >> (6);
    local_r10 = (result * 8) + ((uint32_t)(v_stack_p8));
    result = (result + 1) << ((uint8_t)(Arg1));
    a4 = (result * 8) + ((uint32_t)(v_stack_p8));
    result = (result) - (result + 1);
    result = ~(result);
    Arg2 = (*(uint64_t *)(a4)) & (result);
loc_0037A043:
    if (Arg2 == NULL) goto loc_0037A2E8;
    local_rbp = (a4) - (v_stack_p60);
    local_rbp = (local_rbp) >> (3);
    local_rbp = (local_rbp) << (6);
    local_rbp = (local_rbp) + ((uint32_t)((uint32_t)(Arg1)));
    v_stack_p130 = (uint32_t)(Arg1);
    if (local_rbp > (result + 1)) goto loc_0037A348;
    result = (result + 1) << ((uint8_t)(Arg1));
    result = (result) - (result + 1);
    Arg2 = (Arg2) | (result);
loc_0037A084:
    Arg2 = ~(Arg2);
    if (Arg2 != NULL) goto loc_0037A0A1;
    if ((a4 + 8) > local_r10) goto loc_0037A30F;
    goto loc_0037A084;
loc_0037A0A1:
loc_0037A0A5:
    v_stack_p130 = (uint32_t)(a4 + 8);
    Arg3 = (a4 + 8) - (v_stack_p60);
    Arg3 = (Arg3) >> (3);
    Arg3 = (Arg3) << (6);
    Arg3 = (Arg3) + (a4 + 8);
    if (Arg3 > (result + 1)) { Arg3 = result + 1; }
    Arg3 = (Arg3) - (local_rbp);
loc_0037A0C7:
    if (Arg3 == 0) goto loc_0037A292;
    result = (v_stack_p138) * (2);
    v_stack_pB0 = Arg3 + local_rbp * 1;
    local_r12 = (local_rbp) * (v_stack_p138);
    v_stack_pA0 = result;
    local_r12 = (local_r12) * (2);
    local_r12 = (local_r12) + (v_stack_p50);
loc_0037A105:
    if (local_rbp >= (Arg3 + local_rbp * 1)) goto loc_0037A24A;
    if (Arg3 != 0) goto loc_0037A15D;
    local_r10 = (uint32_t)((local_rbp) & (31));
    Arg1 = (local_rbp) >> (5);
    *(uint64_t *)(v_stack_p68 + arg1 * 1 + 0x4078) = local_rbp;
    if ((local_r10 + 1) > 32) goto loc_0037A2D6;
    result = (uint32_t)(((uint32_t)((uint32_t)(result + 1))) << ((uint8_t)((uint32_t)((uint32_t)(local_r10)))));
    result = (uint32_t)(~(result));
loc_0037A159:
loc_0037A15D:
    local_r10 = (local_rbp) << ((uint8_t)(*(uint64_t *)(v_rip - 0x37A164 + (uint32_t)(arg2) * 8 + 0x11128)));
    result = (local_rbp + 1) << ((uint8_t)(*(uint64_t *)(v_rip - 0x37A164 + (uint32_t)(arg2) * 8 + 0x11128)));
    result = (result) - (result + 1);
    Arg1 = (v_stack_p138) - 1;
    Arg1 = (Arg1) * (2);
    Arg1 = (Arg1) + (local_r12);
    if (result <= local_r11) goto loc_0037A33E;
    result = (result) - (local_r11);
    Arg2 = 0;
    result = (result) * (2);
    Arg1 = (Arg1) - (result);
loc_0037A1B1:
    if (local_r10 < v_stack_p98) goto loc_0037A3AA;
loc_0037A1C2:
    v_stack_p38 = Arg3;
    v_stack_p30 = (uint8_t)(v_stack_p90);
    v_stack_p28 = 2;
    v_stack_p20 = Arg1;
    result = MiProcessLargeCoalesceBitmapCandidates(Arg1, local_r10, (uint32_t)(v_stack_p128), local_r12);
    if (Arg3 == 0) goto loc_0037A264;
    if (((uint32_t)(result)) == 0xC000022DULL) goto loc_0037A3C7;
    v_stack_p120 = (uint32_t)((uint32_t)(v_stack_p120));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 261) goto loc_00379F21;
loc_0037A21C:
    result = (v_stack_p78) + (result + 1);
    v_stack_p78 = result;
    if ((((uint8_t)(result)) & (31)) != 0) goto loc_0037A275;
    Arg2 = 0;
    Arg1 = (*(uint64_t *)(Arg3 + 0x20)) + (40);
    result = MiAccumulateTimeBoundTime(Arg1, Arg2, (uint32_t)(v_stack_p128), local_r12);
    if ((uint32_t)(result) == 0) goto loc_0037A275;
    goto loc_00379F21;
loc_0037A24A:
    goto loc_00379FE1;
loc_0037A264:
    *(uint64_t *)(v_stack_p68 + arg1 * 1 + 0x4078) = -2;
loc_0037A275:
    local_r12 = (v_stack_pB8) + (v_stack_pA0);
    goto loc_0037A105;
loc_0037A292:
loc_0037A2A9:
loc_0037A2AE:
    goto loc_00379EFB;
loc_0037A2BB:
    v_stack_p58 = v_stack_p58;
    Arg2 = 0;
    goto loc_00379E7F;
loc_0037A2CA:
    goto loc_00379EE3;
loc_0037A2D6:
    if (v_stack_p138 != 0) goto loc_0037A350;
loc_0037A2DB:
    result = (uint32_t)((v_stack_p68) | (0xFFFFFFFFULL));
    result = (uint32_t)((result) << ((uint8_t)((uint32_t)((uint32_t)(result + 1)))));
    goto loc_0037A159;
loc_0037A2E8:
    if (result > v_stack_p138) goto loc_0037A348;
    a4 = ((uint32_t)((uint32_t)(result + 1))) + (8);
    result = (result) + (8);
    goto loc_0037A043;
loc_0037A2FD:
    goto loc_00379EE3;
loc_0037A30F:
    goto loc_0037A0A5;
loc_0037A319:
    if ((*(uint32_t *)(*(uint64_t *)(a4) + a4 * 8)) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0xC))))) goto loc_00379EFB;
    Arg1 = ((uint32_t)((uint32_t)(a4))) + ((uint32_t)((uint32_t)(a4)));
    local_r11 = (*(uint64_t *)(v_stack_p58 + arg1 * 8 + 0x18)) + (*(uint64_t *)(v_stack_p58 + arg1 * 8 + 0x10));
    goto loc_00379F66;
loc_0037A33E:
    goto loc_0037A1B1;
loc_0037A348:
    goto loc_0037A0C7;
loc_0037A350:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) & (31));
    Arg2 = (uint32_t)((32) - ((uint32_t)(result)));
    result = (uint32_t)(((uint32_t)((uint32_t)(result + 1))) << ((uint8_t)((uint32_t)(Arg2))));
    result = (uint32_t)((result) - ((uint32_t)(result + 1)));
    result = (uint32_t)((result) << ((uint8_t)(v_stack_p138)));
    result = (uint32_t)(~(result));
    Arg3 = (v_stack_p58) + (4);
    a4 = (a4) - ((uint32_t)(Arg2));
    if (a4 < 32) goto loc_0037A39C;
    Arg2 = (a4) >> (5);
    result = ((uint32_t)(Arg2)) * (Arg2);
    a4 = (a4) + (result);
loc_0037A38C:
    *(uint32_t *)(Arg3) = 0;
    Arg3 = (Arg3) + (4);
    Arg2 = (Arg2) - (result + 1);
    if (condition_is_not_equal) goto loc_0037A38C;
loc_0037A39C:
    if (a4 == 0) goto loc_0037A15D;
    goto loc_0037A2DB;
loc_0037A3AA:
    Arg2 = 0;
    result = (Arg3) - (v_stack_p138);
    a4 = (result) * (4);
    a4 = (a4) + (local_r12);
    goto loc_0037A1C2;
loc_0037A3C7:
    v_stack_p120 = (uint32_t)(result + 1);
    goto loc_0037A21C;
loc_0037A3D3:
    result = MiDereferencePageRuns(v_stack_p138, Arg2, Arg3, a4);
    goto loc_00379F2F;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4000` | `64` | `R` |
| `Arg1` | `+ 0x4038` | `64` | `R` |
| `Arg1` | `+ 0x4848` | `64` | `R` |
| `Arg2` | `+ 0x0 + r12*2` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00379DF4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
