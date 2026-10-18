# MiBuildMappedCluster

- RVA: `0x00405F1C`–`0x00406987` (길이 `2,667` bytes)
- VA: `0x0000000140405F1C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009A8A0`
- 디코드: `591`개 명령, `2,667/2,667` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00406023` → [MiMapPageInHyperSpaceWorker](../33/MiMapPageInHyperSpaceWorker_function_00332B10.md) (function, `0x00332B10`)
- `0x00406220` → [MiUnmapPageInHyperSpaceWorker](../43/MiUnmapPageInHyperSpaceWorker_function_00432800.md) (function, `0x00432800`)
- `0x004062FC` → [MiUnmapPageInHyperSpaceWorker](../43/MiUnmapPageInHyperSpaceWorker_function_00432800.md) (function, `0x00432800`)
- `0x00406306` → [MiReferencePageForModifiedWrite](MiReferencePageForModifiedWrite_function_00405DAC.md) (function, `0x00405DAC`)
- `0x0040631C` → [MiMapPageInHyperSpaceWorker](../33/MiMapPageInHyperSpaceWorker_function_00332B10.md) (function, `0x00332B10`)
- `0x004063A3` → [MiReferencePageForModifiedWrite](MiReferencePageForModifiedWrite_function_00405DAC.md) (function, `0x00405DAC`)
- `0x004063D5` → [MiAllocatePool](../35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x0040642F` → [MiMapPageInHyperSpaceWorker](../33/MiMapPageInHyperSpaceWorker_function_00332B10.md) (function, `0x00332B10`)
- `0x00406563` → [MiUnmapPageInHyperSpaceWorker](../43/MiUnmapPageInHyperSpaceWorker_function_00432800.md) (function, `0x00432800`)
- `0x0040656D` → [MiReferencePageForModifiedWrite](MiReferencePageForModifiedWrite_function_00405DAC.md) (function, `0x00405DAC`)
- `0x00406589` → [MiMapPageInHyperSpaceWorker](../33/MiMapPageInHyperSpaceWorker_function_00332B10.md) (function, `0x00332B10`)
- `0x0040660D` → [MiUnmapPageInHyperSpaceWorker](../43/MiUnmapPageInHyperSpaceWorker_function_00432800.md) (function, `0x00432800`)
- `0x004066FA` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0040670C` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00406797` → [MiMapPageInHyperSpaceWorker](../33/MiMapPageInHyperSpaceWorker_function_00332B10.md) (function, `0x00332B10`)
- `0x004067B5` → [MiReferencePageForModifiedWrite](MiReferencePageForModifiedWrite_function_00405DAC.md) (function, `0x00405DAC`)
- `0x00406873` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00406886` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x004068EA` → [MiUnmapPageInHyperSpaceWorker](../43/MiUnmapPageInHyperSpaceWorker_function_00432800.md) (function, `0x00432800`)
- `0x00406960` → [MiUnmapPageInHyperSpaceWorker](../43/MiUnmapPageInHyperSpaceWorker_function_00432800.md) (function, `0x00432800`)

### Direct callers
- [MiGatherMappedPages](MiGatherMappedPages_function_00404E80.md) at `0x00405013`

### Static image references
- `0x00405F9E` → RVA `0x00E30088` (`.data`; read)
- `0x00405FBE` → RVA `0x00E2DC80` (`.data`; read)
- `0x00406121` → RVA `0x00E2DCE0` (`.data`; read)
- `0x004062A1` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x004066EC` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x004066C0` → [sub_006EC446 + 0x65](../6E/Unknown_function_006EC446.md) (`tail-transfer`)
  - `0x004066CD` → [sub_006EC446 + 0x52](../6E/Unknown_function_006EC446.md) (`tail-transfer`)
  - `0x004066E7` → [sub_006EC446](../6E/Unknown_function_006EC446.md) (`tail-transfer`)
  - `0x00406972` → [sub_006EC446 + 0x123](../6E/Unknown_function_006EC446.md) (`tail-transfer`)
  - `0x00406982` → [sub_006EC446 + 0xDB](../6E/Unknown_function_006EC446.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00405F1C  48 8B C4                        mov rax, rsp
00405F1F  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00405F23  48 89 48 08                     mov qword ptr [rax + 8], rcx
00405F27  53                              push rbx
00405F28  55                              push rbp
00405F29  56                              push rsi
00405F2A  57                              push rdi
00405F2B  41 54                           push r12
00405F2D  41 55                           push r13
00405F2F  41 56                           push r14
00405F31  41 57                           push r15
00405F33  48 81 EC 88 00 00 00            sub rsp, 0x88
00405F3A  41 8B E8                        mov ebp, r8d
00405F3D  4C 8B FA                        mov r15, rdx
00405F40  45 33 C0                        xor r8d, r8d
00405F43  48 8B D1                        mov rdx, rcx
00405F46  44 88 40 18                     mov byte ptr [rax + 0x18], r8b
00405F4A  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00405F54  48 8B C0                        mov rax, rax
00405F57  4C 8B 6A 08                     mov r13, qword ptr [rdx + 8]
00405F5B  48 2B C8                        sub rcx, rax
00405F5E  48 C1 F9 04                     sar rcx, 4
00405F62  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00405F6C  48 0F AF C8                     imul rcx, rax
00405F70  49 8D 47 30                     lea rax, [r15 + 0x30]
00405F74  49 C7 C4 00 F0 FF FF            mov r12, 0xfffffffffffff000
00405F7B  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00405F80  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00405F85  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
00405F8F  4C 0B E8                        or r13, rax
00405F92  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
00405F97  48 8B 42 28                     mov rax, qword ptr [rdx + 0x28]
00405F9B  49 8B FD                        mov rdi, r13
00405F9E  48 8B 0D E3 A0 A2 00            mov rcx, qword ptr [rip + 0xa2a0e3]
00405FA5  49 23 FC                        and rdi, r12
00405FA8  48 8B 5A 10                     mov rbx, qword ptr [rdx + 0x10]
00405FAC  48 C1 E8 2B                     shr rax, 0x2b
00405FB0  25 FF 03 00 00                  and eax, 0x3ff
00405FB5  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
00405FBA  4C 8B 34 C1                     mov r14, qword ptr [rcx + rax*8]
00405FBE  48 8B 05 BB 7C A2 00            mov rax, qword ptr [rip + 0xa27cbb]
00405FC5  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
00405FCA  48 85 C0                        test rax, rax
00405FCD  74 0B                           je 0x140405fda
00405FCF  F6 C3 10                        test bl, 0x10
00405FD2  75 06                           jne 0x140405fda
00405FD4  48 F7 D0                        not rax
00405FD7  48 23 D8                        and rbx, rax
00405FDA  48 C1 FB 10                     sar rbx, 0x10
00405FDE  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00405FE8  41 B8 00 00 00 80               mov r8d, 0x80000000
00405FEE  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
00405FF3  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00405FF7  48 3B F8                        cmp rdi, rax
00405FFA  48 0F 42 F8                     cmovb rdi, rax
00405FFE  49 8D 45 88                     lea rax, [r13 - 0x78]
00406002  48 3B F8                        cmp rdi, rax
00406005  48 8B F7                        mov rsi, rdi
00406008  48 0F 42 F0                     cmovb rsi, rax
0040600C  48 8B 42 28                     mov rax, qword ptr [rdx + 0x28]
00406010  48 23 C1                        and rax, rcx
00406013  48 8D 94 24 E0 00 00 00         lea rdx, [rsp + 0xe0]
0040601B  48 8B C8                        mov rcx, rax
0040601E  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00406023  E8 E8 CA F2 FF                  call 0x140332b10
00406028  4D 8B C5                        mov r8, r13
0040602B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00406030  41 81 E0 FF 0F 00 00            and r8d, 0xfff
00406037  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0040603C  4C 03 C0                        add r8, rax
0040603F  45 33 DB                        xor r11d, r11d
00406042  4C 8B D0                        mov r10, rax
00406045  85 ED                           test ebp, ebp
00406047  0F 85 7C 07 00 00               jne 0x1404067c9
0040604D  49 8B F5                        mov rsi, r13
00406050  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00406054  4D 23 C4                        and r8, r12
00406057  8B 4B 2C                        mov ecx, dword ptr [rbx + 0x2c]
0040605A  4C 8B F6                        mov r14, rsi
0040605D  41 81 E6 FF 0F 00 00            and r14d, 0xfff
00406064  4C 8B E6                        mov r12, rsi
00406067  49 81 E4 00 F0 FF FF            and r12, 0xfffffffffffff000
0040606E  4D 03 F0                        add r14, r8
00406071  49 81 C4 00 10 00 00            add r12, 0x1000
00406078  48 8D 14 C8                     lea rdx, [rax + rcx*8]
0040607C  4C 3B E2                        cmp r12, rdx
0040607F  48 8D 86 80 00 00 00            lea rax, [rsi + 0x80]
00406086  4C 0F 47 E2                     cmova r12, rdx
0040608A  4C 3B E0                        cmp r12, rax
0040608D  49 8B D4                        mov rdx, r12
00406090  48 0F 47 D0                     cmova rdx, rax
00406094  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
00406099  85 ED                           test ebp, ebp
0040609B  75 0C                           jne 0x1404060a9
0040609D  48 8D 56 08                     lea rdx, [rsi + 8]
004060A1  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
004060A6  4C 8B E2                        mov r12, rdx
004060A9  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
004060AE  BF 81 00 00 00                  mov edi, 0x81
004060B3  48 8B EE                        mov rbp, rsi
004060B6  8D 4F 80                        lea ecx, [rdi - 0x80]
004060B9  89 8C 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], ecx
004060C0  49 3B F4                        cmp rsi, r12
004060C3  0F 83 42 01 00 00               jae 0x14040620b
004060C9  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
004060CE  48 3B E8                        cmp rbp, rax
004060D1  0F 84 E7 01 00 00               je 0x1404062be
004060D7  83 F9 03                        cmp ecx, 3
004060DA  0F 84 14 08 00 00               je 0x1404068f4
004060E0  49 8B 1E                        mov rbx, qword ptr [r14]
004060E3  48 8B C3                        mov rax, rbx
004060E6  25 01 0C 00 00                  and eax, 0xc01
004060EB  48 3D 00 08 00 00               cmp rax, 0x800
004060F1  0F 85 97 05 00 00               jne 0x14040668e
004060F7  48 8B 05 82 7B A2 00            mov rax, qword ptr [rip + 0xa27b82]
004060FE  48 8B CB                        mov rcx, rbx
00406101  48 C1 E9 0C                     shr rcx, 0xc
00406105  48 F7 D0                        not rax
00406108  48 C1 E8 0C                     shr rax, 0xc
0040610C  48 23 C1                        and rax, rcx
0040610F  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
00406114  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
0040611E  48 23 C1                        and rax, rcx
00406121  48 3B 05 B8 7B A2 00            cmp rax, qword ptr [rip + 0xa27bb8]
00406128  0F 87 AB 01 00 00               ja 0x1404062d9
0040612E  48 8D 0C 40                     lea rcx, [rax + rax*2]
00406132  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
0040613C  48 03 C9                        add rcx, rcx
0040613F  48 8B C0                        mov rax, rax
00406142  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
00406146  48 C1 E8 36                     shr rax, 0x36
0040614A  0F BA E0 00                     bt eax, 0
0040614E  0F 83 85 01 00 00               jae 0x1404062d9
00406154  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0040615E  48 8B C0                        mov rax, rax
00406161  48 8D 34 C8                     lea rsi, [rax + rcx*8]
00406165  41 8B EB                        mov ebp, r11d
00406168  F0 48 0F BA 6E 18 3F            lock bts qword ptr [rsi + 0x18], 0x3f
0040616F  0F 82 2A 01 00 00               jb 0x14040629f
00406175  49 8B 06                        mov rax, qword ptr [r14]
00406178  48 3B D8                        cmp rbx, rax
0040617B  0F 85 F7 01 00 00               jne 0x140406378
00406181  F6 46 22 10                     test byte ptr [rsi + 0x22], 0x10
00406185  0F 84 E5 04 00 00               je 0x140406670
0040618B  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
0040618E  66 85 C0                        test ax, ax
00406191  0F 85 D9 04 00 00               jne 0x140406670
00406197  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
0040619B  48 8B 0D E6 9E A2 00            mov rcx, qword ptr [rip + 0xa29ee6]
004061A2  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
004061A7  48 C1 E8 2B                     shr rax, 0x2b
004061AB  25 FF 03 00 00                  and eax, 0x3ff
004061B0  48 3B 14 C1                     cmp rdx, qword ptr [rcx + rax*8]
004061B4  0F 85 B6 04 00 00               jne 0x140406670
004061BA  48 8B 6C 24 40                  mov rbp, qword ptr [rsp + 0x40]
004061BF  4C 8B 54 24 28                  mov r10, qword ptr [rsp + 0x28]
004061C4  48 3B 6C 24 48                  cmp rbp, qword ptr [rsp + 0x48]
004061C9  0F 82 17 01 00 00               jb 0x1404062e6
004061CF  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
004061D9  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
004061DE  48 8B 74 24 20                  mov rsi, qword ptr [rsp + 0x20]
004061E3  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
004061E8  8B 8C 24 E8 00 00 00            mov ecx, dword ptr [rsp + 0xe8]
004061EF  48 83 C5 08                     add rbp, 8
004061F3  49 83 C6 08                     add r14, 8
004061F7  48 89 6C 24 40                  mov qword ptr [rsp + 0x40], rbp
004061FC  41 BB 00 00 00 00               mov r11d, 0
00406202  49 3B EC                        cmp rbp, r12
00406205  0F 82 C3 FE FF FF               jb 0x1404060ce
0040620B  4D 85 D2                        test r10, r10
0040620E  74 15                           je 0x140406225
00406210  8A 94 24 E0 00 00 00            mov dl, byte ptr [rsp + 0xe0]
00406217  41 B8 00 00 00 80               mov r8d, 0x80000000
0040621D  49 8B CA                        mov rcx, r10
00406220  E8 DB C5 02 00                  call 0x140432800
00406225  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0040622A  48 3B E9                        cmp rbp, rcx
0040622D  4C 8B F1                        mov r14, rcx
00406230  4C 0F 46 F5                     cmovbe r14, rbp
00406234  4C 2B F6                        sub r14, rsi
00406237  49 C1 FE 03                     sar r14, 3
0040623B  83 BC 24 E8 00 00 00 03         cmp dword ptr [rsp + 0xe8], 3
00406243  74 12                           je 0x140406257
00406245  48 3B E9                        cmp rbp, rcx
00406248  0F 87 6A 01 00 00               ja 0x1404063b8
0040624E  4C 3B EE                        cmp r13, rsi
00406251  0F 82 61 01 00 00               jb 0x1404063b8
00406257  33 DB                           xor ebx, ebx
00406259  49 C1 E6 0C                     shl r14, 0xc
0040625D  49 8B C6                        mov rax, r14
00406260  49 89 1F                        mov qword ptr [r15], rbx
00406263  48 C1 E8 0C                     shr rax, 0xc
00406267  66 83 C0 06                     add ax, 6
0040626B  49 89 5F 20                     mov qword ptr [r15 + 0x20], rbx
0040626F  66 C1 E0 03                     shl ax, 3
00406273  66 41 89 47 08                  mov word ptr [r15 + 8], ax
00406278  49 8B C7                        mov rax, r15
0040627B  41 89 5F 2C                     mov dword ptr [r15 + 0x2c], ebx
0040627F  45 89 77 28                     mov dword ptr [r15 + 0x28], r14d
00406283  66 41 C7 47 0A 02 00            mov word ptr [r15 + 0xa], 2
0040628A  48 81 C4 88 00 00 00            add rsp, 0x88
00406291  41 5F                           pop r15
00406293  41 5E                           pop r14
00406295  41 5D                           pop r13
00406297  41 5C                           pop r12
00406299  5F                              pop rdi
0040629A  5E                              pop rsi
0040629B  5D                              pop rbp
0040629C  5B                              pop rbx
0040629D  C3                              ret
0040629E  CC                              int3
0040629F  FF C5                           inc ebp
004062A1  85 2D 05 F0 BB 00               test dword ptr [rip + 0xbbf005], ebp
004062A7  0F 84 3F 04 00 00               je 0x1404066ec
004062AD  F3 90                           pause
004062AF  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
004062B3  48 85 C0                        test rax, rax
004062B6  0F 89 AC FE FF FF               jns 0x140406168
004062BC  EB E1                           jmp 0x14040629f
004062BE  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
004062C3  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
004062C8  48 89 13                        mov qword ptr [rbx], rdx
004062CB  48 83 C3 08                     add rbx, 8
004062CF  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
004062D4  E9 16 FF FF FF                  jmp 0x1404061ef
004062D9  49 83 EE 08                     sub r14, 8
004062DD  48 83 ED 08                     sub rbp, 8
004062E1  E9 FD FE FF FF                  jmp 0x1404061e3
004062E6  4D 85 D2                        test r10, r10
004062E9  0F 84 AF 00 00 00               je 0x14040639e
004062EF  BB 00 00 00 80                  mov ebx, 0x80000000
004062F4  B2 02                           mov dl, 2
004062F6  44 8B C3                        mov r8d, ebx
004062F9  49 8B CA                        mov rcx, r10
004062FC  E8 FF C4 02 00                  call 0x140432800
00406301  33 D2                           xor edx, edx
00406303  48 8B CE                        mov rcx, rsi
00406306  E8 A1 FA FF FF                  call 0x140405dac
0040630B  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00406310  44 8B C3                        mov r8d, ebx
00406313  33 D2                           xor edx, edx
00406315  89 84 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], eax
0040631C  E8 EF C7 F2 FF                  call 0x140332b10
00406321  8B 8C 24 E8 00 00 00            mov ecx, dword ptr [rsp + 0xe8]
00406328  41 81 E6 FF 0F 00 00            and r14d, 0xfff
0040632F  4C 03 F0                        add r14, rax
00406332  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00406337  4C 8B D0                        mov r10, rax
0040633A  85 C9                           test ecx, ecx
0040633C  0F 84 D6 05 00 00               je 0x140406918
00406342  48 8B 05 37 79 A2 00            mov rax, qword ptr [rip + 0xa27937]
00406349  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00406353  48 F7 D0                        not rax
00406356  48 C1 E8 0C                     shr rax, 0xc
0040635A  48 23 44 24 50                  and rax, qword ptr [rsp + 0x50]
0040635F  48 23 C1                        and rax, rcx
00406362  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00406367  48 89 01                        mov qword ptr [rcx], rax
0040636A  48 83 C1 08                     add rcx, 8
0040636E  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00406373  E9 57 FE FF FF                  jmp 0x1404061cf
00406378  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00406382  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
00406387  48 8B 6C 24 40                  mov rbp, qword ptr [rsp + 0x40]
0040638C  49 83 EE 08                     sub r14, 8
00406390  4C 8B 54 24 28                  mov r10, qword ptr [rsp + 0x28]
00406395  48 83 ED 08                     sub rbp, 8
00406399  E9 40 FE FF FF                  jmp 0x1404061de
0040639E  33 D2                           xor edx, edx
004063A0  48 8B CE                        mov rcx, rsi
004063A3  E8 04 FA FF FF                  call 0x140405dac
004063A8  4C 8B 54 24 28                  mov r10, qword ptr [rsp + 0x28]
004063AD  8B C8                           mov ecx, eax
004063AF  89 84 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], eax
004063B6  EB 82                           jmp 0x14040633a
004063B8  48 8B D5                        mov rdx, rbp
004063BB  B9 40 00 00 00                  mov ecx, 0x40
004063C0  49 2B D5                        sub rdx, r13
004063C3  41 B8 4D 6D 57 65               mov r8d, 0x65576d4d
004063C9  48 C1 FA 03                     sar rdx, 3
004063CD  48 8D 14 D5 30 00 00 00         lea rdx, [rdx*8 + 0x30]
004063D5  E8 66 51 F5 FF                  call 0x14035b540
004063DA  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
004063DF  48 8B D8                        mov rbx, rax
004063E2  48 85 C0                        test rax, rax
004063E5  0F 84 6C FE FF FF               je 0x140406257
004063EB  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
004063F3  49 8D 47 30                     lea rax, [r15 + 0x30]
004063F7  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004063FC  4C 8D 73 30                     lea r14, [rbx + 0x30]
00406400  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
0040640A  4C 89 74 24 68                  mov qword ptr [rsp + 0x68], r14
0040640F  41 B8 00 00 00 80               mov r8d, 0x80000000
00406415  C7 84 24 D8 00 00 00 01 00 00 00  mov dword ptr [rsp + 0xd8], 1
00406420  48 8B 49 28                     mov rcx, qword ptr [rcx + 0x28]
00406424  48 8D 94 24 E0 00 00 00         lea rdx, [rsp + 0xe0]
0040642C  48 23 C8                        and rcx, rax
0040642F  E8 DC C6 F2 FF                  call 0x140332b10
00406434  49 8B ED                        mov rbp, r13
00406437  4C 8B E0                        mov r12, rax
0040643A  81 E5 FF 0F 00 00               and ebp, 0xfff
00406440  48 03 E8                        add rbp, rax
00406443  4C 3B 6C 24 40                  cmp r13, qword ptr [rsp + 0x40]
00406448  0F 83 AA 01 00 00               jae 0x1404065f8
0040644E  49 8D 47 30                     lea rax, [r15 + 0x30]
00406452  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00406457  4C 3B 6C 24 48                  cmp r13, qword ptr [rsp + 0x48]
0040645C  73 09                           jae 0x140406467
0040645E  4C 3B EE                        cmp r13, rsi
00406461  0F 83 BE 01 00 00               jae 0x140406625
00406467  83 BC 24 D8 00 00 00 03         cmp dword ptr [rsp + 0xd8], 3
0040646F  0F 84 BC 04 00 00               je 0x140406931
00406475  48 8B 5D 00                     mov rbx, qword ptr [rbp]
00406479  48 8B C3                        mov rax, rbx
0040647C  25 01 0C 00 00                  and eax, 0xc01
00406481  48 3D 00 08 00 00               cmp rax, 0x800
00406487  0F 85 A0 02 00 00               jne 0x14040672d
0040648D  48 8B 0D EC 77 A2 00            mov rcx, qword ptr [rip + 0xa277ec]
00406494  48 8B C3                        mov rax, rbx
00406497  48 F7 D1                        not rcx
0040649A  48 C1 E8 0C                     shr rax, 0xc
0040649E  48 C1 E9 0C                     shr rcx, 0xc
004064A2  48 23 C8                        and rcx, rax
004064A5  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
004064AF  48 23 C8                        and rcx, rax
004064B2  48 3B 0D 27 78 A2 00            cmp rcx, qword ptr [rip + 0xa27827]
004064B9  0F 87 24 01 00 00               ja 0x1404065e3
004064BF  48 8D 14 49                     lea rdx, [rcx + rcx*2]
004064C3  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
004064CD  48 03 D2                        add rdx, rdx
004064D0  48 8B C0                        mov rax, rax
004064D3  48 8B 04 D0                     mov rax, qword ptr [rax + rdx*8]
004064D7  48 C1 E8 36                     shr rax, 0x36
004064DB  0F BA E0 00                     bt eax, 0
004064DF  0F 83 FE 00 00 00               jae 0x1404065e3
004064E5  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
004064EF  48 8B C0                        mov rax, rax
004064F2  45 33 C0                        xor r8d, r8d
004064F5  48 8D 34 D0                     lea rsi, [rax + rdx*8]
004064F9  45 8B F8                        mov r15d, r8d
004064FC  F0 48 0F BA 6E 18 3F            lock bts qword ptr [rsi + 0x18], 0x3f
00406503  0F 82 32 01 00 00               jb 0x14040663b
00406509  48 8B 45 00                     mov rax, qword ptr [rbp]
0040650D  48 3B D8                        cmp rbx, rax
00406510  0F 85 46 01 00 00               jne 0x14040665c
00406516  F6 46 22 10                     test byte ptr [rsi + 0x22], 0x10
0040651A  0F 84 F9 01 00 00               je 0x140406719
00406520  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
00406523  66 85 C0                        test ax, ax
00406526  0F 85 ED 01 00 00               jne 0x140406719
0040652C  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00406530  48 8B 0D 51 9B A2 00            mov rcx, qword ptr [rip + 0xa29b51]
00406537  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0040653C  48 C1 E8 2B                     shr rax, 0x2b
00406540  25 FF 03 00 00                  and eax, 0x3ff
00406545  48 3B 14 C1                     cmp rdx, qword ptr [rcx + rax*8]
00406549  0F 85 CA 01 00 00               jne 0x140406719
0040654F  4D 85 E4                        test r12, r12
00406552  0F 84 58 02 00 00               je 0x1404067b0
00406558  41 B8 00 00 00 80               mov r8d, 0x80000000
0040655E  B2 02                           mov dl, 2
00406560  49 8B CC                        mov rcx, r12
00406563  E8 98 C2 02 00                  call 0x140432800
00406568  33 D2                           xor edx, edx
0040656A  48 8B CE                        mov rcx, rsi
0040656D  E8 3A F8 FF FF                  call 0x140405dac
00406572  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00406577  33 D2                           xor edx, edx
00406579  41 B8 00 00 00 80               mov r8d, 0x80000000
0040657F  89 84 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], eax
00406586  44 8B F8                        mov r15d, eax
00406589  E8 82 C5 F2 FF                  call 0x140332b10
0040658E  81 E5 FF 0F 00 00               and ebp, 0xfff
00406594  4C 8B E0                        mov r12, rax
00406597  48 03 E8                        add rbp, rax
0040659A  45 85 FF                        test r15d, r15d
0040659D  0F 84 76 01 00 00               je 0x140406719
004065A3  48 8B 05 D6 76 A2 00            mov rax, qword ptr [rip + 0xa276d6]
004065AA  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
004065B4  48 F7 D0                        not rax
004065B7  48 C1 EB 0C                     shr rbx, 0xc
004065BB  48 C1 E8 0C                     shr rax, 0xc
004065BF  48 23 C3                        and rax, rbx
004065C2  48 23 C1                        and rax, rcx
004065C5  49 89 06                        mov qword ptr [r14], rax
004065C8  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
004065D2  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
004065D7  48 83 C5 08                     add rbp, 8
004065DB  49 83 C5 08                     add r13, 8
004065DF  49 83 C6 08                     add r14, 8
004065E3  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
004065E8  48 8B 74 24 20                  mov rsi, qword ptr [rsp + 0x20]
004065ED  4C 3B 6C 24 40                  cmp r13, qword ptr [rsp + 0x40]
004065F2  0F 82 5F FE FF FF               jb 0x140406457
004065F8  4D 85 E4                        test r12, r12
004065FB  74 15                           je 0x140406612
004065FD  8A 94 24 E0 00 00 00            mov dl, byte ptr [rsp + 0xe0]
00406604  41 B8 00 00 00 80               mov r8d, 0x80000000
0040660A  49 8B CC                        mov rcx, r12
0040660D  E8 EE C1 02 00                  call 0x140432800
00406612  4C 2B F3                        sub r14, rbx
00406615  4C 8B FB                        mov r15, rbx
00406618  49 83 EE 30                     sub r14, 0x30
0040661C  49 C1 FE 03                     sar r14, 3
00406620  E9 32 FC FF FF                  jmp 0x140406257
00406625  48 8B 4C 24 28                  mov rcx, qword ptr [rsp + 0x28]
0040662A  48 8B 01                        mov rax, qword ptr [rcx]
0040662D  48 83 C1 08                     add rcx, 8
00406631  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00406636  49 89 06                        mov qword ptr [r14], rax
00406639  EB 9C                           jmp 0x1404065d7
0040663B  41 FF C7                        inc r15d
0040663E  44 85 3D 67 EC BB 00            test dword ptr [rip + 0xbbec67], r15d
00406645  0F 84 1A 02 00 00               je 0x140406865
0040664B  F3 90                           pause
0040664D  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
00406651  48 85 C0                        test rax, rax
00406654  0F 89 A2 FE FF FF               jns 0x1404064fc
0040665A  EB DF                           jmp 0x14040663b
0040665C  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00406666  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
0040666B  E9 73 FF FF FF                  jmp 0x1404065e3
00406670  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0040667A  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
0040667F  48 8B 6C 24 40                  mov rbp, qword ptr [rsp + 0x40]
00406684  48 8B 74 24 20                  mov rsi, qword ptr [rsp + 0x20]
00406689  4C 8B 54 24 28                  mov r10, qword ptr [rsp + 0x28]
0040668E  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
00406693  4D 85 D2                        test r10, r10
00406696  0F 85 3E 02 00 00               jne 0x1404068da
0040669C  4C 8B 74 24 30                  mov r14, qword ptr [rsp + 0x30]
004066A1  49 3B EE                        cmp rbp, r14
004066A4  0F 83 7B FB FF FF               jae 0x140406225
004066AA  48 8B EB                        mov rbp, rbx
004066AD  49 2B EF                        sub rbp, r15
004066B0  48 83 ED 30                     sub rbp, 0x30
004066B4  48 C1 FD 03                     sar rbp, 3
004066B8  48 89 6C 24 50                  mov qword ptr [rsp + 0x50], rbp
004066BD  48 85 ED                        test rbp, rbp
004066C0  0F 84 E5 5D 2E 00               je 0x1406ec4ab
004066C6  49 8D 47 30                     lea rax, [r15 + 0x30]
004066CA  48 3B D8                        cmp rbx, rax
004066CD  0F 86 C5 5D 2E 00               jbe 0x1406ec498
004066D3  4C 8B 7C 24 38                  mov r15, qword ptr [rsp + 0x38]
004066D8  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
004066DD  48 BD 00 00 00 00 00 DE FF FF   movabs rbp, 0xffffde0000000000
004066E7  E9 5A 5D 2E 00                  jmp 0x1406ec446
004066EC  8B 05 C6 03 BC 00               mov eax, dword ptr [rip + 0xbc03c6]
004066F2  A8 40                           test al, 0x40
004066F4  0F 84 B3 FB FF FF               je 0x1404062ad
004066FA  E8 91 8D F0 FF                  call 0x14030f490
004066FF  45 33 DB                        xor r11d, r11d
00406702  84 C0                           test al, al
00406704  0F 84 A3 FB FF FF               je 0x1404062ad
0040670A  8B CD                           mov ecx, ebp
0040670C  E8 4F 8D F0 FF                  call 0x14030f460
00406711  45 33 DB                        xor r11d, r11d
00406714  E9 96 FB FF FF                  jmp 0x1404062af
00406719  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00406723  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
00406728  48 8B 74 24 20                  mov rsi, qword ptr [rsp + 0x20]
0040672D  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00406732  4D 85 E4                        test r12, r12
00406735  0F 85 15 02 00 00               jne 0x140406950
0040673B  4C 3B EE                        cmp r13, rsi
0040673E  0F 83 CE FE FF FF               jae 0x140406612
00406744  49 8B EE                        mov rbp, r14
00406747  48 2B EB                        sub rbp, rbx
0040674A  48 83 ED 30                     sub rbp, 0x30
0040674E  48 C1 FD 03                     sar rbp, 3
00406752  48 89 AC 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rbp
0040675A  48 85 ED                        test rbp, rbp
0040675D  0F 85 07 02 00 00               jne 0x14040696a
00406763  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00406768  48 8D 94 24 E0 00 00 00         lea rdx, [rsp + 0xe0]
00406770  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00406775  41 B8 00 00 00 80               mov r8d, 0x80000000
0040677B  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
00406783  4C 8B EE                        mov r13, rsi
00406786  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
0040678A  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
00406794  48 23 C8                        and rcx, rax
00406797  E8 74 C3 F2 FF                  call 0x140332b10
0040679C  48 8B EE                        mov rbp, rsi
0040679F  4C 8B E0                        mov r12, rax
004067A2  81 E5 FF 0F 00 00               and ebp, 0xfff
004067A8  48 03 E8                        add rbp, rax
004067AB  E9 33 FE FF FF                  jmp 0x1404065e3
004067B0  33 D2                           xor edx, edx
004067B2  48 8B CE                        mov rcx, rsi
004067B5  E8 F2 F5 FF FF                  call 0x140405dac
004067BA  44 8B F8                        mov r15d, eax
004067BD  89 84 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], eax
004067C4  E9 D1 FD FF FF                  jmp 0x14040659a
004067C9  4D 8B CD                        mov r9, r13
004067CC  4C 3B EF                        cmp r13, rdi
004067CF  77 08                           ja 0x1404067d9
004067D1  49 8B F1                        mov rsi, r9
004067D4  E9 77 F8 FF FF                  jmp 0x140406050
004067D9  49 BF FF FF FF FF FF 00 00 00   movabs r15, 0xffffffffff
004067E3  49 BA 00 00 00 00 00 DE FF FF   movabs r10, 0xffffde0000000000
004067ED  48 BB 28 00 00 00 00 DE FF FF   movabs rbx, 0xffffde0000000028
004067F7  49 83 E8 08                     sub r8, 8
004067FB  49 8B 00                        mov rax, qword ptr [r8]
004067FE  48 8B C8                        mov rcx, rax
00406801  81 E1 01 0C 00 00               and ecx, 0xc01
00406807  48 81 F9 00 08 00 00            cmp rcx, 0x800
0040680E  75 39                           jne 0x140406849
00406810  48 8B 0D 69 74 A2 00            mov rcx, qword ptr [rip + 0xa27469]
00406817  48 F7 D1                        not rcx
0040681A  48 C1 E8 0C                     shr rax, 0xc
0040681E  48 C1 E9 0C                     shr rcx, 0xc
00406822  48 23 C8                        and rcx, rax
00406825  49 23 CF                        and rcx, r15
00406828  48 3B 0D B1 74 A2 00            cmp rcx, qword ptr [rip + 0xa274b1]
0040682F  77 18                           ja 0x140406849
00406831  48 8D 14 49                     lea rdx, [rcx + rcx*2]
00406835  48 03 D2                        add rdx, rdx
00406838  48 8B C3                        mov rax, rbx
0040683B  48 8B 04 D0                     mov rax, qword ptr [rax + rdx*8]
0040683F  48 C1 E8 36                     shr rax, 0x36
00406843  0F BA E0 00                     bt eax, 0
00406847  72 4A                           jb 0x140406893
00406849  4C 8B BC 24 D8 00 00 00         mov r15, qword ptr [rsp + 0xd8]
00406851  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00406856  4C 8B 54 24 28                  mov r10, qword ptr [rsp + 0x28]
0040685B  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00406860  E9 6C FF FF FF                  jmp 0x1404067d1
00406865  8B 05 4D 02 BC 00               mov eax, dword ptr [rip + 0xbc024d]
0040686B  A8 40                           test al, 0x40
0040686D  0F 84 D8 FD FF FF               je 0x14040664b
00406873  E8 18 8C F0 FF                  call 0x14030f490
00406878  45 33 C0                        xor r8d, r8d
0040687B  84 C0                           test al, al
0040687D  0F 84 C8 FD FF FF               je 0x14040664b
00406883  41 8B CF                        mov ecx, r15d
00406886  E8 D5 8B F0 FF                  call 0x14030f460
0040688B  45 33 C0                        xor r8d, r8d
0040688E  E9 BA FD FF FF                  jmp 0x14040664d
00406893  49 8B CA                        mov rcx, r10
00406896  F6 44 D1 22 10                  test byte ptr [rcx + rdx*8 + 0x22], 0x10
0040689B  74 AC                           je 0x140406849
0040689D  8B 44 D1 20                     mov eax, dword ptr [rcx + rdx*8 + 0x20]
004068A1  66 85 C0                        test ax, ax
004068A4  75 A3                           jne 0x140406849
004068A6  48 8B 44 D1 28                  mov rax, qword ptr [rcx + rdx*8 + 0x28]
004068AB  48 8B 0D D6 97 A2 00            mov rcx, qword ptr [rip + 0xa297d6]
004068B2  48 C1 E8 2B                     shr rax, 0x2b
004068B6  25 FF 03 00 00                  and eax, 0x3ff
004068BB  4C 3B 34 C1                     cmp r14, qword ptr [rcx + rax*8]
004068BF  75 88                           jne 0x140406849
004068C1  49 83 ED 08                     sub r13, 8
004068C5  4C 3B EE                        cmp r13, rsi
004068C8  4D 0F 43 CD                     cmovae r9, r13
004068CC  4C 3B EF                        cmp r13, rdi
004068CF  0F 87 22 FF FF FF               ja 0x1404067f7
004068D5  E9 6F FF FF FF                  jmp 0x140406849
004068DA  8A 94 24 E0 00 00 00            mov dl, byte ptr [rsp + 0xe0]
004068E1  41 B8 00 00 00 80               mov r8d, 0x80000000
004068E7  49 8B CA                        mov rcx, r10
004068EA  E8 11 BF 02 00                  call 0x140432800
004068EF  E9 A8 FD FF FF                  jmp 0x14040669c
004068F4  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
004068F9  48 8B C3                        mov rax, rbx
004068FC  49 2B C7                        sub rax, r15
004068FF  48 83 E8 30                     sub rax, 0x30
00406903  48 83 E0 F8                     and rax, 0xfffffffffffffff8
00406907  48 3D 80 00 00 00               cmp rax, 0x80
0040690D  0F 8D 80 FD FF FF               jge 0x140406693
00406913  E9 C8 F7 FF FF                  jmp 0x1404060e0
00406918  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00406922  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
00406927  48 8B 74 24 20                  mov rsi, qword ptr [rsp + 0x20]
0040692C  E9 5D FD FF FF                  jmp 0x14040668e
00406931  49 8B C6                        mov rax, r14
00406934  48 2B C3                        sub rax, rbx
00406937  48 83 E8 30                     sub rax, 0x30
0040693B  48 83 E0 F8                     and rax, 0xfffffffffffffff8
0040693F  48 3D 80 00 00 00               cmp rax, 0x80
00406945  0F 8D E7 FD FF FF               jge 0x140406732
0040694B  E9 25 FB FF FF                  jmp 0x140406475
00406950  8A 94 24 E0 00 00 00            mov dl, byte ptr [rsp + 0xe0]
00406957  41 B8 00 00 00 80               mov r8d, 0x80000000
0040695D  49 8B CC                        mov rcx, r12
00406960  E8 9B BE 02 00                  call 0x140432800
00406965  E9 D1 FD FF FF                  jmp 0x14040673b
0040696A  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
0040696F  4D 3B F7                        cmp r14, r15
00406972  0F 86 F1 5B 2E 00               jbe 0x1406ec569
00406978  48 BD 00 00 00 00 00 DE FF FF   movabs rbp, 0xffffde0000000000
00406982  E9 9A 5B 2E 00                  jmp 0x1406ec521
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiBuildMappedCluster(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_pD0;
    unsigned int v_stack_pD8;
    unsigned __int64 v_stack_pE0;
    unsigned int v_stack_pE8;

    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (136);
    a3 = 0;
    *(unsigned __int8 *)(v_rsp + 24) = 0;
    a1 = (a1) - (v_rsp);
    a1 = (a1) >> (4);
    a1 = (a1) * (v_rsp);
    v_stack_m60 = a2 + 48;
    v_stack_m90 = a2 + 48;
    v_r13 = (*(unsigned __int64 *)(a1 + 8)) | (a2 + 48);
    v_stack_m50 = a1;
    v_rdi = (v_r13) & (0xFFFFFFFFFFFFF000ULL);
    result = (*(unsigned __int64 *)(a1 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_stack_m98 = v_r13;
    v_stack_m70 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10658019) + result * 8);
    if (*(unsigned __int64 *)(v_rip + 10648763) == 0) goto loc_00405FDA;
    result = *(unsigned __int64 *)(v_rip + 10648763);
    v_rbx = *(unsigned __int64 *)(a1 + 16);
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 16))) & (16)) == 0) {
        result = ~(*(unsigned __int64 *)(v_rip + 10648763));
        v_rbx = (*(unsigned __int64 *)(a1 + 16)) & (result);
    }
    v_rbx = (v_rbx) >> (16);
    v_stack_m88 = v_rbx;
    if (v_rdi < (*(unsigned __int64 *)(v_rbx + 8))) { v_rdi = *(unsigned __int64 *)(v_rbx + 8); }
    v_rsi = v_rdi;
    if (v_rdi < (v_r13 - 120)) { v_rsi = v_r13 - 120; }
    result = (*(unsigned __int64 *)(a1 + 40)) & (*(unsigned __int64 *)(v_rip + 10658019));
    v_stack_m68 = result;
    result = MiMapPageInHyperSpaceWorker(result, v_stack_p18, (unsigned int)(0x80000000ULL), a4);
    v_stack_mA0 = result;
    a3 = (unsigned int)((v_r13) & (0xFFFULL));
    v_stack_mA8 = v_r13;
    a3 = (a3) + (result);
    v_r11 = 0;
    if ((unsigned int)((unsigned int)(a3)) != 0) goto loc_004067C9;
loc_00406050:
    a3 = (a3) & (0xFFFFFFFFFFFFF000ULL);
    v_r14 = (unsigned int)((v_r13) & (0xFFFULL));
    v_r12 = (v_r13) & (0xFFFFFFFFFFFFF000ULL);
    v_r14 = (v_r14) + (a3);
    v_r12 = (v_r12) + (0x1000ULL);
    if (v_r12 > (*(unsigned __int64 *)(v_rbx + 8) + (unsigned int)(*(unsigned int *)(v_rbx + 44)) * 8)) { v_r12 = *(unsigned __int64 *)(v_rbx + 8) + (unsigned int)(*(unsigned int *)(v_rbx + 44)) * 8; }
    a2 = v_r12;
    if (v_r12 > (v_r13 + 128)) { a2 = v_r13 + 128; }
    v_stack_m80 = a2;
    if ((unsigned int)((unsigned int)(a3)) == 0) {
        a2 = v_r13 + 8;
        v_stack_m80 = a2;
        v_r12 = a2;
    }
    v_stack_m88 = v_r13;
    v_stack_p20 = (unsigned int)(129 - 128);
    if (v_r13 >= v_r12) goto loc_0040620B;
loc_004060CE:
    if (v_r13 == v_stack_m98) goto loc_004062BE;
    if (((unsigned int)(129 - 128)) == 3) goto loc_004068F4;
loc_004060E0:
    result = (unsigned int)((*(unsigned __int64 *)(v_r14)) & (0xC01ULL));
    if (result != 0x800ULL) goto loc_0040668E;
    a1 = (*(unsigned __int64 *)(v_r14)) >> (12);
    result = ~(*(unsigned __int64 *)(v_rip + 10648450));
    result = (result) >> (12);
    result = (result) & (a1);
    v_stack_m78 = a1;
    result = (result) & (a1);
    if (result > (*(unsigned __int64 *)(v_rip + 10648504))) goto loc_004062D9;
    a1 = (result + result * 2) + (result + result * 2);
    result = (*(unsigned __int64 *)(result + a1 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_004062D9;
loc_00406168:
    if (condition_is_below) goto loc_0040629F;
    if ((*(unsigned __int64 *)(v_r14)) != (*(unsigned __int64 *)(v_r14))) goto loc_00406378;
    if (((*(unsigned __int8 *)(result + a1 * 8 + 34)) & (16)) == 0) goto loc_00406670;
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(result + a1 * 8 + 32))) != 0) goto loc_00406670;
    result = (*(unsigned __int64 *)(result + a1 * 8 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if (v_stack_m70 != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10657510) + result * 8))) goto loc_00406670;
    if (v_stack_m88 < v_stack_m80) goto loc_004062E6;
loc_004061CF:
loc_004061DE:
loc_004061E3:
loc_004061EF:
    v_rbp = (v_stack_m88) + (8);
    v_r14 = (v_r14) + (8);
    v_stack_m88 = v_rbp;
    if (v_rbp < v_r12) goto loc_004060CE;
loc_0040620B:
    result = v_stack_m98;
    if (v_stack_mA0 != 0) {
        a2 = v_stack_p18;
        a3 = 0x80000000ULL;
        a1 = v_stack_mA0;
        result = MiUnmapPageInHyperSpaceWorker(a1, a2, a3, a4);
    }
    v_r14 = v_stack_m80;
    if (v_rbp <= v_stack_m80) { v_r14 = v_rbp; }
    v_r14 = (v_r14) - (v_stack_mA8);
    v_r14 = (v_r14) >> (3);
    if (v_stack_p20 == 3) goto loc_00406257;
    if (v_rbp > v_stack_m80) goto loc_004063B8;
    if (v_r13 < v_stack_mA8) goto loc_004063B8;
loc_00406257:
    v_rbx = 0;
    v_r14 = (v_r14) << (12);
    *(unsigned __int64 *)(a2) = 0;
    result = (v_r14) >> (12);
    result = (unsigned __int16)((result) + (6));
    *(unsigned __int64 *)(a2 + 32) = 0;
    result = (unsigned __int16)((result) << (3));
    *(unsigned __int16 *)(a2 + 8) = (unsigned __int16)(result);
    *(unsigned int *)(a2 + 44) = 0;
    *(unsigned int *)(a2 + 40) = (unsigned int)(v_r14);
    *(unsigned __int16 *)(a2 + 10) = 2;
    v_rsp = (v_rsp) + (136);
    return a2;
loc_0040629F:
    v_rbp = (unsigned int)((v_rbp) + 1);
    if (((*(unsigned int *)(v_rip + 12316677)) & ((unsigned int)(v_rbp))) == 0) goto loc_004066EC;
loc_004062AD:
loc_004062AF:
    if (!sign_flag) goto loc_00406168;
    goto loc_0040629F;
loc_004062BE:
    *(unsigned __int64 *)(v_stack_p38) = v_stack_p78;
    v_rbx = (v_stack_p38) + (8);
    v_stack_p38 = v_rbx;
    goto loc_004061EF;
loc_004062D9:
    v_r14 = (v_r14) - (8);
    v_rbp = (v_rbp) - (8);
    goto loc_004061E3;
loc_004062E6:
    if (v_stack_mA0 == 0) goto loc_0040639E;
    result = MiUnmapPageInHyperSpaceWorker(v_stack_mA0, 2, (unsigned int)((unsigned int)((unsigned int)(0x80000000ULL))), a4);
    a2 = 0;
    result = MiReferencePageForModifiedWrite(v_stack_mA8, a2, (unsigned int)((unsigned int)((unsigned int)(0x80000000ULL))), a4);
    a2 = 0;
    v_stack_pE8 = (unsigned int)(result);
    result = MiMapPageInHyperSpaceWorker(v_stack_p60, a2, (unsigned int)((unsigned int)((unsigned int)(0x80000000ULL))), a4);
    v_r14 = (unsigned int)((v_r14) & (0xFFFULL));
    v_r14 = (v_r14) + (result);
    v_stack_p28 = result;
loc_0040633A:
    if ((unsigned int)((unsigned int)(v_stack_pE8)) == 0) goto loc_00406918;
    result = ~(*(unsigned __int64 *)(v_rip + 10647863));
    result = (result) >> (12);
    result = (result) & (v_stack_p50);
    result = (result) & ((unsigned int)(v_stack_pE8));
    *(unsigned __int64 *)(v_stack_p38) = result;
    a1 = (v_stack_p38) + (8);
    v_stack_p38 = a1;
    goto loc_004061CF;
loc_00406378:
    v_r14 = (v_r14) - (8);
    v_rbp = (v_stack_p40) - (8);
    goto loc_004061DE;
loc_0040639E:
    a2 = 0;
    result = MiReferencePageForModifiedWrite(v_stack_mA8, a2, (unsigned int)((unsigned int)((unsigned int)(0x80000000ULL))), a4);
    v_stack_pE8 = (unsigned int)(result);
    goto loc_0040633A;
loc_004063B8:
    a2 = (v_rbp) - (v_r13);
    a2 = (a2) >> (3);
    result = MiAllocatePool(64, a2 * 8 + 48, (unsigned int)(0x65576D4DULL), a4);
    v_stack_p30 = result;
    if (result == 0) goto loc_00406257;
    v_stack_p28 = a2 + 48;
    v_stack_p68 = result + 48;
    v_stack_pD8 = 1;
    a1 = (*(unsigned __int64 *)(v_stack_pD0 + 40)) & (a2 + 48);
    result = MiMapPageInHyperSpaceWorker(a1, v_stack_pE0, (unsigned int)(0x80000000ULL), a4);
    v_rbp = (unsigned int)((v_r13) & (0xFFFULL));
    v_rbp = (v_rbp) + (result);
    if (v_r13 >= v_stack_p40) goto loc_004065F8;
    v_stack_p50 = a2 + 48;
loc_00406457:
    if (v_r13 >= v_stack_p48) goto loc_00406467;
    if (v_r13 >= v_stack_mA8) goto loc_00406625;
loc_00406467:
    if (v_stack_pD8 == 3) goto loc_00406931;
loc_00406475:
    result = (unsigned int)((*(unsigned __int64 *)(v_rbp)) & (0xC01ULL));
    if (result != 0x800ULL) goto loc_0040672D;
    a1 = ~(*(unsigned __int64 *)(v_rip + 10647532));
    result = (*(unsigned __int64 *)(v_rbp)) >> (12);
    a1 = (a1) >> (12);
    a1 = (a1) & (result);
    a1 = (a1) & (result);
    if (a1 > (*(unsigned __int64 *)(v_rip + 10647591))) goto loc_004065E3;
    a2 = (a1 + a1 * 2) + (a1 + a1 * 2);
    result = (*(unsigned __int64 *)(result + a2 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_004065E3;
    a3 = 0;
loc_004064FC:
    if (condition_is_below) goto loc_0040663B;
    if ((*(unsigned __int64 *)(v_rbp)) != (*(unsigned __int64 *)(v_rbp))) goto loc_0040665C;
    if (((*(unsigned __int8 *)(result + a2 * 8 + 34)) & (16)) == 0) goto loc_00406719;
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(result + a2 * 8 + 32))) != 0) goto loc_00406719;
    result = (*(unsigned __int64 *)(result + a2 * 8 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if (v_stack_p58 != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10656593) + result * 8))) goto loc_00406719;
    if (result == 0) goto loc_004067B0;
    result = MiUnmapPageInHyperSpaceWorker(result, 2, (unsigned int)(0x80000000ULL), a4);
    a2 = 0;
    result = MiReferencePageForModifiedWrite(result + a2 * 8, a2, (unsigned int)(0x80000000ULL), a4);
    a2 = 0;
    v_stack_pD8 = (unsigned int)(result);
    result = MiMapPageInHyperSpaceWorker(v_stack_p60, a2, (unsigned int)(0x80000000ULL), a4);
    v_rbp = (unsigned int)((v_rbp) & (0xFFFULL));
    v_rbp = (v_rbp) + (result);
loc_0040659A:
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_00406719;
    result = ~(*(unsigned __int64 *)(v_rip + 10647254));
    v_rbx = (*(unsigned __int64 *)(v_rbp)) >> (12);
    result = (result) >> (12);
    result = (result) & (v_rbx);
    result = (result) & (v_stack_p60);
    *(unsigned __int64 *)(result + 48) = result;
loc_004065D7:
    v_rbp = (v_rbp) + (8);
    v_r13 = (v_r13) + (8);
    v_r14 = (result + 48) + (8);
loc_004065E3:
    if (v_r13 < v_stack_p40) goto loc_00406457;
loc_004065F8:
    if (result != 0) {
        a2 = v_stack_pE0;
        a3 = 0x80000000ULL;
        a1 = result;
        result = MiUnmapPageInHyperSpaceWorker(a1, a2, a3, a4);
    }
    v_r14 = (v_r14) - (v_stack_p30);
    v_r14 = (v_r14) - (48);
    v_r14 = (v_r14) >> (3);
    goto loc_00406257;
loc_00406625:
    a1 = (v_stack_p28) + (8);
    v_stack_p28 = a1;
    *(unsigned __int64 *)(v_r14) = *(unsigned __int64 *)(v_stack_p28);
    goto loc_004065D7;
loc_0040663B:
    v_r15 = (unsigned int)((v_stack_p30) + 1);
    if (((*(unsigned int *)(v_rip + 12315751)) & ((unsigned int)(v_r15))) == 0) goto loc_00406865;
loc_0040664B:
loc_0040664D:
    if (!sign_flag) goto loc_004064FC;
    goto loc_0040663B;
loc_0040665C:
    goto loc_004065E3;
loc_00406670:
loc_0040668E:
loc_00406693:
    if (v_stack_p28 != 0) goto loc_004068DA;
loc_0040669C:
    if (v_stack_p40 >= v_stack_p30) goto loc_00406225;
    v_rbp = (v_stack_p38) - (v_r15);
    v_rbp = (v_rbp) - (48);
    v_rbp = (v_rbp) >> (3);
    v_stack_p50 = v_rbp;
loc_004066EC:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12321734)))) & (64)) == 0) goto loc_004062AD;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, a2, a3, a4);
    v_r11 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_004062AD;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbp)), a2, a3, a4);
    v_r11 = 0;
    goto loc_004062AF;
loc_00406719:
loc_0040672D:
loc_00406732:
    if (result != 0) goto loc_00406950;
loc_0040673B:
    if (v_r13 >= v_stack_p20) goto loc_00406612;
    v_rbp = (v_stack_p68) - (v_stack_p30);
    v_rbp = (v_rbp) - (48);
    v_rbp = (v_rbp) >> (3);
    v_stack_pE8 = v_rbp;
    if (v_rbp != 0) goto loc_0040696A;
    v_stack_p28 = v_stack_p50;
    a1 = (*(unsigned __int64 *)(v_stack_pD0 + 40)) & (v_stack_pD0);
    result = MiMapPageInHyperSpaceWorker(a1, v_stack_pE0, (unsigned int)(0x80000000ULL), a4);
    v_rbp = (unsigned int)((v_stack_p20) & (0xFFFULL));
    v_rbp = (v_rbp) + (result);
    goto loc_004065E3;
loc_004067B0:
    a2 = 0;
    result = MiReferencePageForModifiedWrite(v_stack_p20, a2, (unsigned int)(0x80000000ULL), a4);
    v_stack_pD8 = (unsigned int)(result);
    goto loc_0040659A;
loc_004067C9:
    if (v_stack_p20 > 129) goto loc_004067D9;
loc_004067D1:
    goto loc_00406050;
loc_004067D9:
loc_004067F7:
    a3 = ((unsigned int)(0x80000000ULL)) - (8);
    a1 = (unsigned int)((*(unsigned __int64 *)(a3)) & (0xC01ULL));
    if (a1 != 0x800ULL) goto loc_00406849;
    a1 = ~(*(unsigned __int64 *)(v_rip + 10646633));
    result = (*(unsigned __int64 *)(a3)) >> (12);
    a1 = (a1) >> (12);
    a1 = (a1) & (result);
    a1 = (a1) & ((unsigned int)((unsigned int)(result)));
    if (a1 > (*(unsigned __int64 *)(v_rip + 10646705))) goto loc_00406849;
    a2 = (a1 + a1 * 2) + (a1 + a1 * 2);
    result = (*(unsigned __int64 *)(v_stack_p30 + a2 * 8)) >> (54);
    if (condition_is_below) goto loc_00406893;
loc_00406849:
    v_stack_p20 = v_stack_p20;
    goto loc_004067D1;
loc_00406865:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12321357)))) & (64)) == 0) goto loc_0040664B;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, a2, a3, v_stack_p20);
    a3 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_0040664B;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_pD8)), a2, a3, v_stack_p20);
    a3 = 0;
    goto loc_0040664D;
loc_00406893:
    if (((*(unsigned __int8 *)(v_stack_p28 + a2 * 8 + 34)) & (16)) == 0) goto loc_00406849;
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p28 + a2 * 8 + 32))) != 0) goto loc_00406849;
    result = (*(unsigned __int64 *)(v_stack_p28 + a2 * 8 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if (v_stack_p68 != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10655702) + result * 8))) goto loc_00406849;
    v_r13 = (v_stack_p20) - (8);
    a4 = v_stack_p20;
    if (v_r13 >= v_stack_p20) { a4 = v_r13; }
    if (v_r13 > 129) goto loc_004067F7;
    goto loc_00406849;
loc_004068DA:
    result = MiUnmapPageInHyperSpaceWorker(v_stack_p28, v_stack_pE0, (unsigned int)(0x80000000ULL), a4);
    goto loc_0040669C;
loc_004068F4:
    result = (v_stack_p38) - (v_stack_pD8);
    result = (result) - (48);
    result = (result) & (-8);
    if (result >= 128) goto loc_00406693;
    goto loc_004060E0;
loc_00406918:
    goto loc_0040668E;
loc_00406931:
    result = (v_stack_p68) - (v_stack_p38);
    result = (result) - (48);
    result = (result) & (-8);
    if (result >= 128) goto loc_00406732;
    goto loc_00406475;
loc_00406950:
    result = MiUnmapPageInHyperSpaceWorker(result, v_stack_pE0, (unsigned int)(0x80000000ULL), a4);
    goto loc_0040673B;
loc_0040696A:
}
```

## 5. (Beta) C Style

```c
void *MiBuildMappedCluster(void *Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p78;
    uint64_t v_stack_pD0;
    uint32_t v_stack_pD8;
    uint64_t v_stack_pE0;
    uint32_t v_stack_pE8;

    *(void **)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (136);
    Arg3 = 0;
    *(uint8_t *)(local_rsp + 0x18) = 0;
    Arg1 = (Arg1) - (local_rsp);
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * (local_rsp);
    v_stack_m60 = Arg2 + 48;
    v_stack_m90 = Arg2 + 48;
    local_r13 = (*(uint64_t *)(arg1 + 0x8)) | (Arg2 + 48);
    v_stack_m50 = Arg1;
    local_rdi = (local_r13) & (0xFFFFFFFFFFFFF000ULL);
    result = (*(uint64_t *)(arg1 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    v_stack_m98 = local_r13;
    v_stack_m70 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xA2A0E3) + result * 8);
    if (*(uint64_t *)(v_rip + 0xA27CBB) == 0) goto loc_00405FDA;
    result = *(uint64_t *)(v_rip + 0xA27CBB);
    local_rbx = *(uint64_t *)(arg1 + 0x10);
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x10))) & (16)) == 0) {
        result = ~(*(uint64_t *)(v_rip + 0xA27CBB));
        local_rbx = (*(uint64_t *)(arg1 + 0x10)) & (result);
    }
    local_rbx = (local_rbx) >> (16);
    v_stack_m88 = local_rbx;
    if (local_rdi < (*(uint64_t *)(local_rbx + 0x8))) { local_rdi = *(uint64_t *)(local_rbx + 0x8); }
    local_rsi = local_rdi;
    if (local_rdi < (local_r13 - 120)) { local_rsi = local_r13 - 120; }
    result = (*(uint64_t *)(arg1 + 0x28)) & (*(uint64_t *)(v_rip + 0xA2A0E3));
    v_stack_m68 = result;
    result = MiMapPageInHyperSpaceWorker(result, v_stack_p18, (uint32_t)(0x80000000ULL), a4);
    v_stack_mA0 = result;
    Arg3 = (uint32_t)((local_r13) & (0xFFFULL));
    v_stack_mA8 = local_r13;
    Arg3 = (Arg3) + (result);
    local_r11 = 0;
    if ((uint32_t)((uint32_t)(Arg3)) != 0) goto loc_004067C9;
loc_00406050:
    Arg3 = (Arg3) & (0xFFFFFFFFFFFFF000ULL);
    local_r14 = (uint32_t)((local_r13) & (0xFFFULL));
    local_r12 = (local_r13) & (0xFFFFFFFFFFFFF000ULL);
    local_r14 = (local_r14) + (Arg3);
    local_r12 = (local_r12) + (0x1000ULL);
    if (local_r12 > (*(uint64_t *)(local_rbx + 0x8) + (uint32_t)(*(uint32_t *)(local_rbx + 0x2C)) * 8)) { local_r12 = *(uint64_t *)(local_rbx + 0x8) + (uint32_t)(*(uint32_t *)(local_rbx + 0x2C)) * 8; }
    Arg2 = local_r12;
    if (local_r12 > (local_r13 + 128)) { Arg2 = local_r13 + 128; }
    v_stack_m80 = Arg2;
    if ((uint32_t)((uint32_t)(Arg3)) == 0) {
        Arg2 = local_r13 + 8;
        v_stack_m80 = Arg2;
        local_r12 = Arg2;
    }
    v_stack_m88 = local_r13;
    v_stack_p20 = (uint32_t)(129 - 128);
    if (local_r13 >= local_r12) goto loc_0040620B;
loc_004060CE:
    if (local_r13 == v_stack_m98) goto loc_004062BE;
    if (((uint32_t)(129 - 128)) == 3) goto loc_004068F4;
loc_004060E0:
    result = (uint32_t)((*(uint64_t *)(local_r14)) & (0xC01ULL));
    if (result != 0x800ULL) goto loc_0040668E;
    Arg1 = (*(uint64_t *)(local_r14)) >> (12);
    result = ~(*(uint64_t *)(v_rip + 0xA27B82));
    result = (result) >> (12);
    result = (result) & (Arg1);
    v_stack_m78 = Arg1;
    result = (result) & (Arg1);
    if (result > (*(uint64_t *)(v_rip + 0xA27BB8))) goto loc_004062D9;
    Arg1 = (result + result * 2) + (result + result * 2);
    result = (*(uint64_t *)(result + arg1 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_004062D9;
loc_00406168:
    if (condition_is_below) goto loc_0040629F;
    if ((*(uint64_t *)(local_r14)) != (*(uint64_t *)(local_r14))) goto loc_00406378;
    if (((*(uint8_t *)(result + arg1 * 8 + 0x22)) & (16)) == 0) goto loc_00406670;
    if ((uint16_t)((uint32_t)(*(uint32_t *)(result + arg1 * 8 + 0x20))) != 0) goto loc_00406670;
    result = (*(uint64_t *)(result + arg1 * 8 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if (v_stack_m70 != (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA29EE6) + result * 8))) goto loc_00406670;
    if (v_stack_m88 < v_stack_m80) goto loc_004062E6;
loc_004061CF:
loc_004061DE:
loc_004061E3:
loc_004061EF:
    local_rbp = (v_stack_m88) + (8);
    local_r14 = (local_r14) + (8);
    v_stack_m88 = local_rbp;
    if (local_rbp < local_r12) goto loc_004060CE;
loc_0040620B:
    result = v_stack_m98;
    if (v_stack_mA0 != 0) {
        Arg2 = v_stack_p18;
        Arg3 = 0x80000000ULL;
        Arg1 = v_stack_mA0;
        result = MiUnmapPageInHyperSpaceWorker(Arg1, Arg2, Arg3, a4);
    }
    local_r14 = v_stack_m80;
    if (local_rbp <= v_stack_m80) { local_r14 = local_rbp; }
    local_r14 = (local_r14) - (v_stack_mA8);
    local_r14 = (local_r14) >> (3);
    if (v_stack_p20 == 3) goto loc_00406257;
    if (local_rbp > v_stack_m80) goto loc_004063B8;
    if (local_r13 < v_stack_mA8) goto loc_004063B8;
loc_00406257:
    local_rbx = 0;
    local_r14 = (local_r14) << (12);
    *(uint64_t *)(arg2) = 0;
    result = (local_r14) >> (12);
    result = (uint16_t)((result) + (6));
    *(uint64_t *)(arg2 + 0x20) = 0;
    result = (uint16_t)((result) << (3));
    *(uint16_t *)(arg2 + 0x8) = (uint16_t)(result);
    *(uint32_t *)(arg2 + 0x2C) = 0;
    *(uint32_t *)(arg2 + 0x28) = (uint32_t)(local_r14);
    *(uint16_t *)(arg2 + 0xA) = 2;
    local_rsp = (local_rsp) + (136);
    return Arg2;
loc_0040629F:
    local_rbp = (uint32_t)((local_rbp) + 1);
    if (((*(uint32_t *)(v_rip + 0xBBF005)) & ((uint32_t)(local_rbp))) == 0) goto loc_004066EC;
loc_004062AD:
loc_004062AF:
    if (!sign_flag) goto loc_00406168;
    goto loc_0040629F;
loc_004062BE:
    *(uint64_t *)(v_stack_p38) = v_stack_p78;
    local_rbx = (v_stack_p38) + (8);
    v_stack_p38 = local_rbx;
    goto loc_004061EF;
loc_004062D9:
    local_r14 = (local_r14) - (8);
    local_rbp = (local_rbp) - (8);
    goto loc_004061E3;
loc_004062E6:
    if (v_stack_mA0 == 0) goto loc_0040639E;
    result = MiUnmapPageInHyperSpaceWorker(v_stack_mA0, 2, (uint32_t)((uint32_t)((uint32_t)(0x80000000ULL))), a4);
    Arg2 = 0;
    result = MiReferencePageForModifiedWrite(v_stack_mA8, Arg2, (uint32_t)((uint32_t)((uint32_t)(0x80000000ULL))), a4);
    Arg2 = 0;
    v_stack_pE8 = (uint32_t)(result);
    result = MiMapPageInHyperSpaceWorker(v_stack_p60, Arg2, (uint32_t)((uint32_t)((uint32_t)(0x80000000ULL))), a4);
    local_r14 = (uint32_t)((local_r14) & (0xFFFULL));
    local_r14 = (local_r14) + (result);
    v_stack_p28 = result;
loc_0040633A:
    if ((uint32_t)((uint32_t)(v_stack_pE8)) == 0) goto loc_00406918;
    result = ~(*(uint64_t *)(v_rip + 0xA27937));
    result = (result) >> (12);
    result = (result) & (v_stack_p50);
    result = (result) & ((uint32_t)(v_stack_pE8));
    *(uint64_t *)(v_stack_p38) = result;
    Arg1 = (v_stack_p38) + (8);
    v_stack_p38 = Arg1;
    goto loc_004061CF;
loc_00406378:
    local_r14 = (local_r14) - (8);
    local_rbp = (v_stack_p40) - (8);
    goto loc_004061DE;
loc_0040639E:
    Arg2 = 0;
    result = MiReferencePageForModifiedWrite(v_stack_mA8, Arg2, (uint32_t)((uint32_t)((uint32_t)(0x80000000ULL))), a4);
    v_stack_pE8 = (uint32_t)(result);
    goto loc_0040633A;
loc_004063B8:
    Arg2 = (local_rbp) - (local_r13);
    Arg2 = (Arg2) >> (3);
    result = MiAllocatePool(64, Arg2 * 8 + 48, (uint32_t)(0x65576D4DULL), a4);
    v_stack_p30 = result;
    if (result == 0) goto loc_00406257;
    v_stack_p28 = Arg2 + 48;
    v_stack_p68 = result + 48;
    v_stack_pD8 = 1;
    Arg1 = (*(uint64_t *)(v_stack_pD0 + 0x28)) & (Arg2 + 48);
    result = MiMapPageInHyperSpaceWorker(Arg1, v_stack_pE0, (uint32_t)(0x80000000ULL), a4);
    local_rbp = (uint32_t)((local_r13) & (0xFFFULL));
    local_rbp = (local_rbp) + (result);
    if (local_r13 >= v_stack_p40) goto loc_004065F8;
    v_stack_p50 = Arg2 + 48;
loc_00406457:
    if (local_r13 >= v_stack_p48) goto loc_00406467;
    if (local_r13 >= v_stack_mA8) goto loc_00406625;
loc_00406467:
    if (v_stack_pD8 == 3) goto loc_00406931;
loc_00406475:
    result = (uint32_t)((*(uint64_t *)(local_rbp)) & (0xC01ULL));
    if (result != 0x800ULL) goto loc_0040672D;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xA277EC));
    result = (*(uint64_t *)(local_rbp)) >> (12);
    Arg1 = (Arg1) >> (12);
    Arg1 = (Arg1) & (result);
    Arg1 = (Arg1) & (result);
    if (Arg1 > (*(uint64_t *)(v_rip + 0xA27827))) goto loc_004065E3;
    Arg2 = (Arg1 + Arg1 * 2) + (Arg1 + Arg1 * 2);
    result = (*(uint64_t *)(result + arg2 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_004065E3;
    Arg3 = 0;
loc_004064FC:
    if (condition_is_below) goto loc_0040663B;
    if ((*(uint64_t *)(local_rbp)) != (*(uint64_t *)(local_rbp))) goto loc_0040665C;
    if (((*(uint8_t *)(result + arg2 * 8 + 0x22)) & (16)) == 0) goto loc_00406719;
    if ((uint16_t)((uint32_t)(*(uint32_t *)(result + arg2 * 8 + 0x20))) != 0) goto loc_00406719;
    result = (*(uint64_t *)(result + arg2 * 8 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if (v_stack_p58 != (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA29B51) + result * 8))) goto loc_00406719;
    if (result == 0) goto loc_004067B0;
    result = MiUnmapPageInHyperSpaceWorker(result, 2, (uint32_t)(0x80000000ULL), a4);
    Arg2 = 0;
    result = MiReferencePageForModifiedWrite(result + Arg2 * 8, Arg2, (uint32_t)(0x80000000ULL), a4);
    Arg2 = 0;
    v_stack_pD8 = (uint32_t)(result);
    result = MiMapPageInHyperSpaceWorker(v_stack_p60, Arg2, (uint32_t)(0x80000000ULL), a4);
    local_rbp = (uint32_t)((local_rbp) & (0xFFFULL));
    local_rbp = (local_rbp) + (result);
loc_0040659A:
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_00406719;
    result = ~(*(uint64_t *)(v_rip + 0xA276D6));
    local_rbx = (*(uint64_t *)(local_rbp)) >> (12);
    result = (result) >> (12);
    result = (result) & (local_rbx);
    result = (result) & (v_stack_p60);
    *(uint64_t *)(result + 0x30) = result;
loc_004065D7:
    local_rbp = (local_rbp) + (8);
    local_r13 = (local_r13) + (8);
    local_r14 = (result + 48) + (8);
loc_004065E3:
    if (local_r13 < v_stack_p40) goto loc_00406457;
loc_004065F8:
    if (result != 0) {
        Arg2 = v_stack_pE0;
        Arg3 = 0x80000000ULL;
        Arg1 = result;
        result = MiUnmapPageInHyperSpaceWorker(Arg1, Arg2, Arg3, a4);
    }
    local_r14 = (local_r14) - (v_stack_p30);
    local_r14 = (local_r14) - (48);
    local_r14 = (local_r14) >> (3);
    goto loc_00406257;
loc_00406625:
    Arg1 = (v_stack_p28) + (8);
    v_stack_p28 = Arg1;
    *(uint64_t *)(local_r14) = *(uint64_t *)(v_stack_p28);
    goto loc_004065D7;
loc_0040663B:
    local_r15 = (uint32_t)((v_stack_p30) + 1);
    if (((*(uint32_t *)(v_rip + 0xBBEC67)) & ((uint32_t)(local_r15))) == 0) goto loc_00406865;
loc_0040664B:
loc_0040664D:
    if (!sign_flag) goto loc_004064FC;
    goto loc_0040663B;
loc_0040665C:
    goto loc_004065E3;
loc_00406670:
loc_0040668E:
loc_00406693:
    if (v_stack_p28 != 0) goto loc_004068DA;
loc_0040669C:
    if (v_stack_p40 >= v_stack_p30) goto loc_00406225;
    local_rbp = (v_stack_p38) - (local_r15);
    local_rbp = (local_rbp) - (48);
    local_rbp = (local_rbp) >> (3);
    v_stack_p50 = local_rbp;
loc_004066EC:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBC03C6)))) & (64)) == 0) goto loc_004062AD;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, Arg2, Arg3, a4);
    local_r11 = 0;
    if ((uint8_t)(result) == 0) goto loc_004062AD;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbp)), Arg2, Arg3, a4);
    local_r11 = 0;
    goto loc_004062AF;
loc_00406719:
loc_0040672D:
loc_00406732:
    if (result != 0) goto loc_00406950;
loc_0040673B:
    if (local_r13 >= v_stack_p20) goto loc_00406612;
    local_rbp = (v_stack_p68) - (v_stack_p30);
    local_rbp = (local_rbp) - (48);
    local_rbp = (local_rbp) >> (3);
    v_stack_pE8 = local_rbp;
    if (local_rbp != 0) goto loc_0040696A;
    v_stack_p28 = v_stack_p50;
    Arg1 = (*(uint64_t *)(v_stack_pD0 + 0x28)) & (v_stack_pD0);
    result = MiMapPageInHyperSpaceWorker(Arg1, v_stack_pE0, (uint32_t)(0x80000000ULL), a4);
    local_rbp = (uint32_t)((v_stack_p20) & (0xFFFULL));
    local_rbp = (local_rbp) + (result);
    goto loc_004065E3;
loc_004067B0:
    Arg2 = 0;
    result = MiReferencePageForModifiedWrite(v_stack_p20, Arg2, (uint32_t)(0x80000000ULL), a4);
    v_stack_pD8 = (uint32_t)(result);
    goto loc_0040659A;
loc_004067C9:
    if (v_stack_p20 > 129) goto loc_004067D9;
loc_004067D1:
    goto loc_00406050;
loc_004067D9:
loc_004067F7:
    Arg3 = ((uint32_t)(0x80000000ULL)) - (8);
    Arg1 = (uint32_t)((*(uint64_t *)(Arg3)) & (0xC01ULL));
    if (Arg1 != 0x800ULL) goto loc_00406849;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xA27469));
    result = (*(uint64_t *)(Arg3)) >> (12);
    Arg1 = (Arg1) >> (12);
    Arg1 = (Arg1) & (result);
    Arg1 = (Arg1) & ((uint32_t)((uint32_t)(result)));
    if (Arg1 > (*(uint64_t *)(v_rip + 0xA274B1))) goto loc_00406849;
    Arg2 = (Arg1 + Arg1 * 2) + (Arg1 + Arg1 * 2);
    result = (*(uint64_t *)(v_stack_p30 + arg2 * 8)) >> (54);
    if (condition_is_below) goto loc_00406893;
loc_00406849:
    v_stack_p20 = v_stack_p20;
    goto loc_004067D1;
loc_00406865:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBC024D)))) & (64)) == 0) goto loc_0040664B;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, Arg2, Arg3, v_stack_p20);
    Arg3 = 0;
    if ((uint8_t)(result) == 0) goto loc_0040664B;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_pD8)), Arg2, Arg3, v_stack_p20);
    Arg3 = 0;
    goto loc_0040664D;
loc_00406893:
    if (((*(uint8_t *)(v_stack_p28 + arg2 * 8 + 0x22)) & (16)) == 0) goto loc_00406849;
    if ((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p28 + arg2 * 8 + 0x20))) != 0) goto loc_00406849;
    result = (*(uint64_t *)(v_stack_p28 + arg2 * 8 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if (v_stack_p68 != (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA297D6) + result * 8))) goto loc_00406849;
    local_r13 = (v_stack_p20) - (8);
    a4 = v_stack_p20;
    if (local_r13 >= v_stack_p20) { a4 = local_r13; }
    if (local_r13 > 129) goto loc_004067F7;
    goto loc_00406849;
loc_004068DA:
    result = MiUnmapPageInHyperSpaceWorker(v_stack_p28, v_stack_pE0, (uint32_t)(0x80000000ULL), a4);
    goto loc_0040669C;
loc_004068F4:
    result = (v_stack_p38) - (v_stack_pD8);
    result = (result) - (48);
    result = (result) & (-8);
    if (result >= 128) goto loc_00406693;
    goto loc_004060E0;
loc_00406918:
    goto loc_0040668E;
loc_00406931:
    result = (v_stack_p68) - (v_stack_p38);
    result = (result) - (48);
    result = (result) & (-8);
    if (result >= 128) goto loc_00406732;
    goto loc_00406475;
loc_00406950:
    result = MiUnmapPageInHyperSpaceWorker(result, v_stack_pE0, (uint32_t)(0x80000000ULL), a4);
    goto loc_0040673B;
loc_0040696A:
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg2` | `+ 0x30` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00405F1C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
