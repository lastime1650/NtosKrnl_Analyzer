# EtwpTraceFileIo

- RVA: `0x00223BB0`–`0x00224038` (길이 `1,160` bytes)
- VA: `0x0000000140223BB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005F838`
- 디코드: `279`개 명령, `1,160/1,160` bytes 표시
- 미해석 바이트: `5` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **26**

### Outgoing calls
- `0x00223D11` → [EtwpLogKernelEvent](../25/EtwpLogKernelEvent_function_0025CC00.md) (function, `0x0025CC00`)
- `0x00223D99` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x00223F1A` → [PsGetServerSiloGlobals](PsGetServerSiloGlobals_function_002250A0.md) (function, `0x002250A0`)
- `0x00223F8A` → [EtwpLogKernelEvent](../25/EtwpLogKernelEvent_function_0025CC00.md) (function, `0x0025CC00`)
- `0x00223FA9` → [PsIsServerSilo](PsIsServerSilo_function_00225828.md) (function, `0x00225828`)
- `0x00223FC0` → [PsIsServerSilo](PsIsServerSilo_function_00225828.md) (function, `0x00225828`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00223BFB` → RVA `0x00FC6AA8` (`ALMOSTRO`; read)
- `0x00223C40` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00223C59` → RVA `0x00010430` (`.rdata`; read)
- `0x00223C62` → RVA `0x00010410` (`.rdata`; read)
- `0x00223C6F` → RVA `0x00EFF838` (`.data`; read)
- `0x00223DA3` → RVA `0x00010420` (`.rdata`; read)
- `0x00223E03` → RVA `0x00010440` (`.rdata`; read)
- `0x00223E0F` → RVA `0x00010450` (`.rdata`; read)
- `0x00223E1B` → RVA `0x00010460` (`.rdata`; read)
- `0x00223E27` → RVA `0x00010470` (`.rdata`; read)
- `0x00223E40` → RVA `0x00010480` (`.rdata`; read)
- `0x00223E4C` → RVA `0x00010490` (`.rdata`; read)
- `0x00223E58` → RVA `0x000104A0` (`.rdata`; read)
- `0x00223E64` → RVA `0x000104B0` (`.rdata`; read)
- `0x00223E7E` → RVA `0x000104C0` (`.rdata`; read)
- `0x00223E97` → RVA `0x000104D0` (`.rdata`; read)
- `0x00223EA3` → RVA `0x000104E0` (`.rdata`; read)
- `0x00223EAF` → RVA `0x000104F0` (`.rdata`; read)
- `0x00223EBB` → RVA `0x00010500` (`.rdata`; read)
- `0x00223EC7` → RVA `0x00010510` (`.rdata`; read)
- `0x00223ED3` → RVA `0x00010520` (`.rdata`; read)
- `0x00223EE7` → RVA `0x00010530` (`.rdata`; read)
- `0x00223EF3` → RVA `0x00010540` (`.rdata`; read)
- `0x00223EFF` → RVA `0x00010550` (`.rdata`; read)
- `0x00223F0B` → RVA `0x000105B0` (`.rdata`; read)
- `0x00223FCE` → RVA `0x000231E8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00224034` → [UpcaseUnicodeToSingleByteNHelper + 0x34](UpcaseUnicodeToSingleByteNHelper_function_00224040.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00223BB0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00223BB5  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00223BBA  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00223BBF  57                              push rdi
00223BC0  41 56                           push r14
00223BC2  41 57                           push r15
00223BC4  48 83 EC 40                     sub rsp, 0x40
00223BC8  33 DB                           xor ebx, ebx
00223BCA  41 8B F1                        mov esi, r9d
00223BCD  45 8B F0                        mov r14d, r8d
00223BD0  4C 8B FA                        mov r15, rdx
00223BD3  48 85 C9                        test rcx, rcx
00223BD6  0F 84 03 03 00 00               je 0x140223edf
00223BDC  48 8B A9 98 06 00 00            mov rbp, qword ptr [rcx + 0x698]
00223BE3  48 83 FD FD                     cmp rbp, -3
00223BE7  0F 85 AC 03 00 00               jne 0x140223f99
00223BED  48 8B 81 20 02 00 00            mov rax, qword ptr [rcx + 0x220]
00223BF4  48 8B A8 F0 05 00 00            mov rbp, qword ptr [rax + 0x5f0]
00223BFB  48 8B 05 A6 2E DA 00            mov rax, qword ptr [rip + 0xda2ea6]
00223C02  0F B7 BC 24 80 00 00 00         movzx edi, word ptr [rsp + 0x80]
00223C0A  48 05 CC 12 00 00               add rax, 0x12cc
00223C10  0F 84 82 00 00 00               je 0x140223c98
00223C16  F7 00 00 00 00 06               test dword ptr [rax], 0x6000000
00223C1C  74 7A                           je 0x140223c98
00223C1E  44 8B CB                        mov r9d, ebx
00223C21  8B C7                           mov eax, edi
00223C23  81 FF 4C 04 00 00               cmp edi, 0x44c
00223C29  74 37                           je 0x140223c62
00223C2B  3D 43 04 00 00                  cmp eax, 0x443
00223C30  0F 84 6D 01 00 00               je 0x140223da3
00223C36  05 C0 FB FF FF                  add eax, 0xfffffbc0
00223C3B  83 F8 16                        cmp eax, 0x16
00223C3E  77 58                           ja 0x140223c98
00223C40  48 8D 15 B9 C3 DD FF            lea rdx, [rip - 0x223c47]
00223C47  48 98                           cdqe
00223C49  8B 8C 82 DC 3F 22 00            mov ecx, dword ptr [rdx + rax*4 + 0x223fdc]
00223C50  48 03 CA                        add rcx, rdx
00223C53  FF E1                           jmp rcx
00223C55  CC                              int3
00223C56  CC                              int3
00223C57  CC                              int3
00223C58  CC                              int3
00223C59  4C 8D 15 D0 C7 DE FF            lea r10, [rip - 0x213830]
00223C60  EB 0D                           jmp 0x140223c6f
00223C62  4C 8D 15 A7 C7 DE FF            lea r10, [rip - 0x213859]
00223C69  41 B9 01 00 00 00               mov r9d, 1
00223C6F  48 8B 15 C2 BB CD 00            mov rdx, qword ptr [rip + 0xcdbbc2]
00223C76  48 85 D2                        test rdx, rdx
00223C79  74 1D                           je 0x140223c98
00223C7B  48 8B 4A 20                     mov rcx, qword ptr [rdx + 0x20]
00223C7F  4D 8B 42 08                     mov r8, qword ptr [r10 + 8]
00223C83  83 79 60 00                     cmp dword ptr [rcx + 0x60], 0
00223C87  0F 85 B1 00 00 00               jne 0x140223d3e
00223C8D  66 83 7A 66 00                  cmp word ptr [rdx + 0x66], 0
00223C92  0F 85 1E 01 00 00               jne 0x140223db6
00223C98  B8 4E 04 00 00                  mov eax, 0x44e
00223C9D  66 3B F8                        cmp di, ax
00223CA0  0F 84 7E 00 00 00               je 0x140223d24
00223CA6  48 8B 1D FB 2D DA 00            mov rbx, qword ptr [rip + 0xda2dfb]
00223CAD  8B 9B A8 11 00 00               mov ebx, dword ptr [rbx + 0x11a8]
00223CB3  0F BC CB                        bsf ecx, ebx
00223CB6  74 63                           je 0x140223d1b
00223CB8  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
00223CC0  48 8B 15 E1 2D DA 00            mov rdx, qword ptr [rip + 0xda2de1]
00223CC7  8D 43 FF                        lea eax, [rbx - 1]
00223CCA  23 D8                           and ebx, eax
00223CCC  44 8B C1                        mov r8d, ecx
00223CCF  8B C1                           mov eax, ecx
00223CD1  48 C1 E0 05                     shl rax, 5
00223CD5  48 8D 8A CC 11 00 00            lea rcx, [rdx + 0x11cc]
00223CDC  48 03 C8                        add rcx, rax
00223CDF  74 35                           je 0x140223d16
00223CE1  48 8B C6                        mov rax, rsi
00223CE4  48 C1 E8 1D                     shr rax, 0x1d
00223CE8  8B 0C 81                        mov ecx, dword ptr [rcx + rax*4]
00223CEB  23 CE                           and ecx, esi
00223CED  F7 C1 FF FF FF 1F               test ecx, 0x1fffffff
00223CF3  74 21                           je 0x140223d16
00223CF5  46 0F B6 84 42 98 11 00 00      movzx r8d, byte ptr [rdx + r8*2 + 0x1198]
00223CFE  45 8B CE                        mov r9d, r14d
00223D01  C7 44 24 28 03 19 60 00         mov dword ptr [rsp + 0x28], 0x601903
00223D09  49 8B CF                        mov rcx, r15
00223D0C  66 89 7C 24 20                  mov word ptr [rsp + 0x20], di
00223D11  E8 EA 8E 03 00                  call 0x14025cc00
00223D16  0F BC CB                        bsf ecx, ebx
00223D19  75 A5                           jne 0x140223cc0
00223D1B  48 85 ED                        test rbp, rbp
00223D1E  0F 85 F3 01 00 00               jne 0x140223f17
00223D24  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00223D29  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00223D2E  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00223D33  48 83 C4 40                     add rsp, 0x40
00223D37  41 5F                           pop r15
00223D39  41 5E                           pop r14
00223D3B  5F                              pop rdi
00223D3C  C3                              ret
00223D3D  CC                              int3
00223D3E  0F B6 41 64                     movzx eax, byte ptr [rcx + 0x64]
00223D42  41 38 42 04                     cmp byte ptr [r10 + 4], al
00223D46  0F 87 E7 00 00 00               ja 0x140223e33
00223D4C  8B 41 68                        mov eax, dword ptr [rcx + 0x68]
00223D4F  A8 40                           test al, 0x40
00223D51  75 5C                           jne 0x140223daf
00223D53  4C 85 41 70                     test qword ptr [rcx + 0x70], r8
00223D57  0F 84 30 FF FF FF               je 0x140223c8d
00223D5D  48 8B 49 78                     mov rcx, qword ptr [rcx + 0x78]
00223D61  48 8B C1                        mov rax, rcx
00223D64  49 23 C0                        and rax, r8
00223D67  48 3B C1                        cmp rax, rcx
00223D6A  0F 85 1D FF FF FF               jne 0x140223c8d
00223D70  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00223D78  45 33 C0                        xor r8d, r8d
00223D7B  48 8B 0D B6 BA CD 00            mov rcx, qword ptr [rip + 0xcdbab6]
00223D82  49 8B D2                        mov rdx, r10
00223D85  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
00223D8A  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
00223D8F  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00223D94  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00223D99  E8 32 B3 03 00                  call 0x14025f0d0
00223D9E  E9 F5 FE FF FF                  jmp 0x140223c98
00223DA3  4C 8D 15 76 C6 DE FF            lea r10, [rip - 0x21398a]
00223DAA  E9 BA FE FF FF                  jmp 0x140223c69
00223DAF  4D 85 C0                        test r8, r8
00223DB2  75 9F                           jne 0x140223d53
00223DB4  EB BA                           jmp 0x140223d70
00223DB6  48 8B 4A 28                     mov rcx, qword ptr [rdx + 0x28]
00223DBA  4D 8B 42 08                     mov r8, qword ptr [r10 + 8]
00223DBE  83 79 60 00                     cmp dword ptr [rcx + 0x60], 0
00223DC2  0F 84 D0 FE FF FF               je 0x140223c98
00223DC8  0F B6 41 64                     movzx eax, byte ptr [rcx + 0x64]
00223DCC  41 38 42 04                     cmp byte ptr [r10 + 4], al
00223DD0  0F 87 B4 00 00 00               ja 0x140223e8a
00223DD6  8B 41 68                        mov eax, dword ptr [rcx + 0x68]
00223DD9  A8 40                           test al, 0x40
00223DDB  0F 85 8F 00 00 00               jne 0x140223e70
00223DE1  4C 85 41 70                     test qword ptr [rcx + 0x70], r8
00223DE5  0F 84 AD FE FF FF               je 0x140223c98
00223DEB  48 8B 49 78                     mov rcx, qword ptr [rcx + 0x78]
00223DEF  48 8B C1                        mov rax, rcx
00223DF2  49 23 C0                        and rax, r8
00223DF5  48 3B C1                        cmp rax, rcx
00223DF8  0F 85 9A FE FF FF               jne 0x140223c98
00223DFE  E9 6D FF FF FF                  jmp 0x140223d70
00223E03  4C 8D 15 36 C6 DE FF            lea r10, [rip - 0x2139ca]
00223E0A  E9 60 FE FF FF                  jmp 0x140223c6f
00223E0F  4C 8D 15 3A C6 DE FF            lea r10, [rip - 0x2139c6]
00223E16  E9 4E FE FF FF                  jmp 0x140223c69
00223E1B  4C 8D 15 3E C6 DE FF            lea r10, [rip - 0x2139c2]
00223E22  E9 48 FE FF FF                  jmp 0x140223c6f
00223E27  4C 8D 15 42 C6 DE FF            lea r10, [rip - 0x2139be]
00223E2E  E9 3C FE FF FF                  jmp 0x140223c6f
00223E33  84 C0                           test al, al
00223E35  0F 84 11 FF FF FF               je 0x140223d4c
00223E3B  E9 4D FE FF FF                  jmp 0x140223c8d
00223E40  4C 8D 15 39 C6 DE FF            lea r10, [rip - 0x2139c7]
00223E47  E9 23 FE FF FF                  jmp 0x140223c6f
00223E4C  4C 8D 15 3D C6 DE FF            lea r10, [rip - 0x2139c3]
00223E53  E9 17 FE FF FF                  jmp 0x140223c6f
00223E58  4C 8D 15 41 C6 DE FF            lea r10, [rip - 0x2139bf]
00223E5F  E9 0B FE FF FF                  jmp 0x140223c6f
00223E64  4C 8D 15 45 C6 DE FF            lea r10, [rip - 0x2139bb]
00223E6B  E9 FF FD FF FF                  jmp 0x140223c6f
00223E70  4D 85 C0                        test r8, r8
00223E73  0F 85 68 FF FF FF               jne 0x140223de1
00223E79  E9 F2 FE FF FF                  jmp 0x140223d70
00223E7E  4C 8D 15 3B C6 DE FF            lea r10, [rip - 0x2139c5]
00223E85  E9 E5 FD FF FF                  jmp 0x140223c6f
00223E8A  84 C0                           test al, al
00223E8C  0F 84 44 FF FF FF               je 0x140223dd6
00223E92  E9 01 FE FF FF                  jmp 0x140223c98
00223E97  4C 8D 15 32 C6 DE FF            lea r10, [rip - 0x2139ce]
00223E9E  E9 CC FD FF FF                  jmp 0x140223c6f
00223EA3  4C 8D 15 36 C6 DE FF            lea r10, [rip - 0x2139ca]
00223EAA  E9 C0 FD FF FF                  jmp 0x140223c6f
00223EAF  4C 8D 15 3A C6 DE FF            lea r10, [rip - 0x2139c6]
00223EB6  E9 B4 FD FF FF                  jmp 0x140223c6f
00223EBB  4C 8D 15 3E C6 DE FF            lea r10, [rip - 0x2139c2]
00223EC2  E9 A8 FD FF FF                  jmp 0x140223c6f
00223EC7  4C 8D 15 42 C6 DE FF            lea r10, [rip - 0x2139be]
00223ECE  E9 9C FD FF FF                  jmp 0x140223c6f
00223ED3  4C 8D 15 46 C6 DE FF            lea r10, [rip - 0x2139ba]
00223EDA  E9 90 FD FF FF                  jmp 0x140223c6f
00223EDF  48 8B EB                        mov rbp, rbx
00223EE2  E9 14 FD FF FF                  jmp 0x140223bfb
00223EE7  4C 8D 15 42 C6 DE FF            lea r10, [rip - 0x2139be]
00223EEE  E9 7C FD FF FF                  jmp 0x140223c6f
00223EF3  4C 8D 15 46 C6 DE FF            lea r10, [rip - 0x2139ba]
00223EFA  E9 70 FD FF FF                  jmp 0x140223c6f
00223EFF  4C 8D 15 4A C6 DE FF            lea r10, [rip - 0x2139b6]
00223F06  E9 64 FD FF FF                  jmp 0x140223c6f
00223F0B  4C 8D 15 9E C6 DE FF            lea r10, [rip - 0x213962]
00223F12  E9 58 FD FF FF                  jmp 0x140223c6f
00223F17  48 8B CD                        mov rcx, rbp
00223F1A  E8 81 11 00 00                  call 0x1402250a0
00223F1F  48 8B A8 40 03 00 00            mov rbp, qword ptr [rax + 0x340]
00223F26  48 85 ED                        test rbp, rbp
00223F29  0F 84 F5 FD FF FF               je 0x140223d24
00223F2F  8B 9D A8 11 00 00               mov ebx, dword ptr [rbp + 0x11a8]
00223F35  0F BC CB                        bsf ecx, ebx
00223F38  0F 84 E6 FD FF FF               je 0x140223d24
00223F3E  66 90                           nop
00223F40  8B D1                           mov edx, ecx
00223F42  8D 43 FF                        lea eax, [rbx - 1]
00223F45  48 C1 E1 05                     shl rcx, 5
00223F49  23 D8                           and ebx, eax
00223F4B  48 81 C1 CC 11 00 00            add rcx, 0x11cc
00223F52  48 03 CD                        add rcx, rbp
00223F55  74 38                           je 0x140223f8f
00223F57  48 8B C6                        mov rax, rsi
00223F5A  48 C1 E8 1D                     shr rax, 0x1d
00223F5E  8B 0C 81                        mov ecx, dword ptr [rcx + rax*4]
00223F61  23 CE                           and ecx, esi
00223F63  F7 C1 FF FF FF 1F               test ecx, 0x1fffffff
00223F69  74 24                           je 0x140223f8f
00223F6B  44 0F B6 84 55 98 11 00 00      movzx r8d, byte ptr [rbp + rdx*2 + 0x1198]
00223F74  45 8B CE                        mov r9d, r14d
00223F77  48 8B D5                        mov rdx, rbp
00223F7A  C7 44 24 28 03 19 60 00         mov dword ptr [rsp + 0x28], 0x601903
00223F82  49 8B CF                        mov rcx, r15
00223F85  66 89 7C 24 20                  mov word ptr [rsp + 0x20], di
00223F8A  E8 71 8C 03 00                  call 0x14025cc00
00223F8F  0F BC CB                        bsf ecx, ebx
00223F92  75 AC                           jne 0x140223f40
00223F94  E9 8B FD FF FF                  jmp 0x140223d24
00223F99  48 85 ED                        test rbp, rbp
00223F9C  75 08                           jne 0x140223fa6
00223F9E  48 8B EB                        mov rbp, rbx
00223FA1  E9 55 FC FF FF                  jmp 0x140223bfb
00223FA6  48 8B CD                        mov rcx, rbp
00223FA9  E8 7A 18 00 00                  call 0x140225828
00223FAE  84 C0                           test al, al
00223FB0  0F 85 45 FC FF FF               jne 0x140223bfb
00223FB6  48 8B AD 18 05 00 00            mov rbp, qword ptr [rbp + 0x518]
00223FBD  48 8B CD                        mov rcx, rbp
00223FC0  E8 63 18 00 00                  call 0x140225828
00223FC5  84 C0                           test al, al
00223FC7  74 ED                           je 0x140223fb6
00223FC9  E9 2D FC FF FF                  jmp 0x140223bfb
00223FCE  4C 8D 15 13 F2 DF FF            lea r10, [rip - 0x200ded]
00223FD5  E9 95 FC FF FF                  jmp 0x140223c6f
00223FDA  66 90                           nop
00223FDC  03 3E                           add edi, dword ptr [rsi]
00223FDE  22 00                           and al, byte ptr [rax]
00223FE0  1B 3E                           sbb edi, dword ptr [rsi]
00223FE2  22 00                           and al, byte ptr [rax]
00223FE4  27                              .byte 0x27
00223FE5  3E 22 00                        and al, byte ptr ds:[rax]
00223FE8  98                              cwde
00223FE9  3C 22                           cmp al, 0x22
00223FEB  00 0F                           add byte ptr [rdi], cl
00223FED  3E 22 00                        and al, byte ptr ds:[rax]
00223FF0  64 3E 22 00                     and al, byte ptr ds:[rax]
00223FF4  C7                              .byte 0xc7
00223FF5  3E 22 00                        and al, byte ptr ds:[rax]
00223FF8  F3 3E 22 00                     and al, byte ptr ds:[rax]
00223FFC  40 3E 22 00                     and al, byte ptr ds:[rax]
00224000  A3 3E 22 00 59 3C 22 00 4C      movabs dword ptr [0x4c00223c5900223e], eax
00224009  3E 22 00                        and al, byte ptr ds:[rax]
0022400C  98                              cwde
0022400D  3C 22                           cmp al, 0x22
0022400F  00 BB 3E 22 00 AF               add byte ptr [rbx - 0x50ffddc2], bh
00224015  3E 22 00                        and al, byte ptr ds:[rax]
00224018  D3 3E                           sar dword ptr [rsi], cl
0022401A  22 00                           and al, byte ptr [rax]
0022401C  E7 3E                           out 0x3e, eax
0022401E  22 00                           and al, byte ptr [rax]
00224020  0B 3F                           or edi, dword ptr [rdi]
00224022  22 00                           and al, byte ptr [rax]
00224024  CE                              .byte 0xce
00224025  3F                              .byte 0x3f
00224026  22 00                           and al, byte ptr [rax]
00224028  97                              xchg edi, eax
00224029  3E 22 00                        and al, byte ptr ds:[rax]
0022402C  58                              pop rax
0022402D  3E 22 00                        and al, byte ptr ds:[rax]
00224030  FF                              .byte 0xff
00224031  3E 22 00                        and al, byte ptr ds:[rax]
00224034  7E 3E                           jle 0x140224074
00224036  22 00                           and al, byte ptr [rax]
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpTraceFileIo(__int64 a1, __int64 a2, int a3, int a4, unsigned __int16 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned int v_stack_m30;
    unsigned __int16 v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (64);
    v_rbx = 0;
    if (a1 == 0) goto loc_00223EDF;
    if ((*(unsigned __int64 *)(a1 + 1688)) != -3) goto loc_00223F99;
loc_00223BFB:
    result = (*(unsigned __int64 *)(v_rip + 14298790)) + (0x12CCULL);
    if (condition_is_equal) goto loc_00223C98;
    if (((*(unsigned int *)(result)) & (0x6000000ULL)) == 0) goto loc_00223C98;
    if (a5 == 0x44CULL) goto loc_00223C62;
    if (((unsigned int)((unsigned int)(a5))) == 0x443ULL) goto loc_00223DA3;
    result = (unsigned int)(((unsigned int)(a5)) + (0xFFFFFBC0ULL));
    if (((unsigned int)(result)) > 22) goto loc_00223C98;
    a1 = ((unsigned int)(*(unsigned int *)(v_rip - 2243655 + result * 4 + 2244572))) + (v_rip - 2243655);
loc_00223C62:
loc_00223C69:
loc_00223C6F:
    if (*(unsigned __int64 *)(v_rip + 13482946) == 0) goto loc_00223C98;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13482946) + 32) + 96)) != 0) goto loc_00223D3E;
loc_00223C8D:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 13482946) + 102)) != 0) goto loc_00223DB6;
loc_00223C98:
    if (a5 == ((unsigned __int16)((unsigned int)(0x44EULL)))) goto loc_00223D24;
    if (a5 == ((unsigned __int16)((unsigned int)(0x44EULL)))) goto loc_00223D1B;
loc_00223CC0:
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 14298619) + 4520))) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 14298619) + 4520)) - 1)));
    result = ((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13482946) + 32)))) << (5);
    a1 = (*(unsigned __int64 *)(v_rip + 14298593) + 4556) + (result);
    if (condition_is_equal) goto loc_00223D16;
    result = ((unsigned int)(a4)) >> (29);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + result * 4))) & ((unsigned int)((unsigned int)(a4))));
    if ((((unsigned int)(a1)) & (0x1FFFFFFFULL)) != 0) {
        a3 = *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 14298593) + (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13482946) + 32))) * 2 + 4504);
        a4 = (unsigned int)((unsigned int)(a3));
        v_stack_m30 = 0x601903ULL;
        a1 = a2;
        v_stack_m38 = a5;
        result = EtwpLogKernelEvent(a1, *(unsigned __int64 *)(v_rip + 14298593), a3, a4);
    }
    if ((((unsigned int)(a1)) & (0x1FFFFFFFULL)) != 0) goto loc_00223CC0;
loc_00223D1B:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1520) != 0) goto loc_00223F17;
loc_00223D24:
    v_rsp = (v_rsp) + (64);
    return result;
loc_00223D3E:
    if ((*(unsigned __int8 *)(v_rip - 2177113 + 4)) > ((unsigned __int8)(*(unsigned __int8 *)(a1 + 100)))) goto loc_00223E33;
loc_00223D4C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 104)))) & (64)) != 0) goto loc_00223DAF;
loc_00223D53:
    if (((*(unsigned __int64 *)(a1 + 112)) & (a3)) == 0) goto loc_00223C8D;
    result = (*(unsigned __int64 *)(a1 + 120)) & (a3);
    if (result != (*(unsigned __int64 *)(a1 + 120))) goto loc_00223C8D;
loc_00223D70:
    a3 = 0;
    v_stack_p38 = a2;
    v_stack_p30 = (unsigned int)((unsigned int)(a3));
    v_stack_p28 = v_stack_p8;
    v_stack_p20 = a6;
    result = EtwWriteEx(*(unsigned __int64 *)(v_rip + 13482678), v_rip - 2177113, a3, a4);
    goto loc_00223C98;
loc_00223DA3:
    goto loc_00223C69;
loc_00223DAF:
    if (0 != 0) goto loc_00223D53;
    goto loc_00223D70;
loc_00223DB6:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip - 2177113 + 40) + 96)) == 0) goto loc_00223C98;
    if ((*(unsigned __int8 *)(v_rip - 2177418 + 4)) > ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 2177113 + 40) + 100)))) goto loc_00223E8A;
loc_00223DD6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 2177113 + 40) + 104)))) & (64)) != 0) goto loc_00223E70;
loc_00223DE1:
    if (((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 2177113 + 40) + 112)) & (*(unsigned __int64 *)(v_rip - 2177418 + 8))) == 0) goto loc_00223C98;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 2177113 + 40) + 120)) & (*(unsigned __int64 *)(v_rip - 2177418 + 8));
    if (result != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 2177113 + 40) + 120))) goto loc_00223C98;
    goto loc_00223D70;
loc_00223E33:
    if ((unsigned __int8)(result) == 0) goto loc_00223D4C;
    goto loc_00223C8D;
loc_00223E70:
    if (*(unsigned __int64 *)(v_rip - 2177418 + 8) != 0) goto loc_00223DE1;
    goto loc_00223D70;
loc_00223E8A:
    if ((unsigned __int8)(result) == 0) goto loc_00223DD6;
    goto loc_00223C98;
loc_00223EDF:
    goto loc_00223BFB;
loc_00223F17:
    result = PsGetServerSiloGlobals(v_stack_p8, v_rip - 2177113, *(unsigned __int64 *)(v_rip - 2177418 + 8), a4);
    if (*(unsigned __int64 *)(result + 832) == 0) goto loc_00223D24;
    if (*(unsigned __int64 *)(result + 832) == 0) goto loc_00223D24;
loc_00223F40:
    a1 = (v_stack_p8) << (5);
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 832) + 4520))) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 832) + 4520)) - 1)));
    a1 = (a1) + (0x11CCULL);
    a1 = (a1) + (*(unsigned __int64 *)(result + 832));
    if (condition_is_equal) goto loc_00223F8F;
    result = (v_stack_p18) >> (29);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + result * 4))) & ((unsigned int)(v_stack_p18)));
    if ((((unsigned int)(a1)) & (0x1FFFFFFFULL)) != 0) {
        a3 = *(unsigned __int8 *)(*(unsigned __int64 *)(result + 832) + (unsigned int)((unsigned int)(v_stack_p8)) * 2 + 4504);
        a4 = (unsigned int)((unsigned int)(a3));
        a2 = *(unsigned __int64 *)(result + 832);
        v_stack_p28 = 0x601903ULL;
        a1 = a2;
        v_stack_p20 = a5;
        result = EtwpLogKernelEvent(a1, a2, a3, a4);
    }
    if ((((unsigned int)(a1)) & (0x1FFFFFFFULL)) != 0) goto loc_00223F40;
    goto loc_00223D24;
loc_00223F99:
    if (*(unsigned __int64 *)(result + 832) != 0) goto loc_00223FA6;
    goto loc_00223BFB;
loc_00223FA6:
    result = PsIsServerSilo(v_rbx, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00223BFB;
loc_00223FB6:
    result = PsIsServerSilo(*(unsigned __int64 *)(v_rbx + 1304), a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00223FB6;
    goto loc_00223BFB;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpTraceFileIo(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, uint16_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint32_t v_stack_m30;
    uint16_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (64);
    local_rbx = 0;
    if (Arg1 == 0) goto loc_00223EDF;
    if ((*(uint64_t *)(Arg1 + 0x698)) != -3) goto loc_00223F99;
loc_00223BFB:
    result = (*(uint64_t *)(v_rip + 0xDA2EA6)) + (0x12CCULL);
    if (condition_is_equal) goto loc_00223C98;
    if (((*(uint32_t *)(result)) & (0x6000000ULL)) == 0) goto loc_00223C98;
    if (Arg5 == 0x44CULL) goto loc_00223C62;
    if (((uint32_t)((uint32_t)(Arg5))) == 0x443ULL) goto loc_00223DA3;
    result = (uint32_t)(((uint32_t)(Arg5)) + (0xFFFFFBC0ULL));
    if (((uint32_t)(result)) > 22) goto loc_00223C98;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip - 0x223C47 + result * 4 + 0x223FDC))) + (v_rip - 2243655);
loc_00223C62:
loc_00223C69:
loc_00223C6F:
    if (*(uint64_t *)(v_rip + 0xCDBBC2) == 0) goto loc_00223C98;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xCDBBC2) + 0x20) + 0x60)) != 0) goto loc_00223D3E;
loc_00223C8D:
    if ((*(uint16_t *)(*(uint64_t *)(v_rip + 0xCDBBC2) + 0x66)) != 0) goto loc_00223DB6;
loc_00223C98:
    if (Arg5 == ((uint16_t)((uint32_t)(0x44EULL)))) goto loc_00223D24;
    if (Arg5 == ((uint16_t)((uint32_t)(0x44EULL)))) goto loc_00223D1B;
loc_00223CC0:
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xDA2DFB) + 0x11A8))) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xDA2DFB) + 0x11A8)) - 1)));
    result = ((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xCDBBC2) + 0x20)))) << (5);
    Arg1 = (*(uint64_t *)(v_rip + 0xDA2DE1) + 4556) + (result);
    if (condition_is_equal) goto loc_00223D16;
    result = ((uint32_t)(Arg4)) >> (29);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg1 + result * 4))) & ((uint32_t)((uint32_t)(Arg4))));
    if ((((uint32_t)(Arg1)) & (0x1FFFFFFFULL)) != 0) {
        Arg3 = *(uint8_t *)(*(uint64_t *)(v_rip + 0xDA2DE1) + (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xCDBBC2) + 0x20))) * 2 + 0x1198);
        Arg4 = (uint32_t)((uint32_t)(Arg3));
        v_stack_m30 = 0x601903ULL;
        Arg1 = Arg2;
        v_stack_m38 = Arg5;
        result = EtwpLogKernelEvent(Arg1, *(uint64_t *)(v_rip + 0xDA2DE1), Arg3, Arg4);
    }
    if ((((uint32_t)(Arg1)) & (0x1FFFFFFFULL)) != 0) goto loc_00223CC0;
loc_00223D1B:
    if (*(uint64_t *)(*(uint64_t *)(Arg1 + 0x220) + 0x5F0) != 0) goto loc_00223F17;
loc_00223D24:
    local_rsp = (local_rsp) + (64);
    return result;
loc_00223D3E:
    if ((*(uint8_t *)(v_rip - 0x213859 + 0x4)) > ((uint8_t)(*(uint8_t *)(Arg1 + 0x64)))) goto loc_00223E33;
loc_00223D4C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x68)))) & (64)) != 0) goto loc_00223DAF;
loc_00223D53:
    if (((*(uint64_t *)(Arg1 + 0x70)) & (Arg3)) == 0) goto loc_00223C8D;
    result = (*(uint64_t *)(Arg1 + 0x78)) & (Arg3);
    if (result != (*(uint64_t *)(Arg1 + 0x78))) goto loc_00223C8D;
loc_00223D70:
    Arg3 = 0;
    v_stack_p38 = Arg2;
    v_stack_p30 = (uint32_t)((uint32_t)(Arg3));
    v_stack_p28 = v_stack_p8;
    v_stack_p20 = Arg6;
    result = EtwWriteEx(*(uint64_t *)(v_rip + 0xCDBAB6), v_rip - 2177113, Arg3, Arg4);
    goto loc_00223C98;
loc_00223DA3:
    goto loc_00223C69;
loc_00223DAF:
    if (0 != 0) goto loc_00223D53;
    goto loc_00223D70;
loc_00223DB6:
    if ((*(uint32_t *)(*(uint64_t *)(v_rip - 0x213859 + 0x28) + 0x60)) == 0) goto loc_00223C98;
    if ((*(uint8_t *)(v_rip - 0x21398A + 0x4)) > ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip - 0x213859 + 0x28) + 0x64)))) goto loc_00223E8A;
loc_00223DD6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0x213859 + 0x28) + 0x68)))) & (64)) != 0) goto loc_00223E70;
loc_00223DE1:
    if (((*(uint64_t *)(*(uint64_t *)(v_rip - 0x213859 + 0x28) + 0x70)) & (*(uint64_t *)(v_rip - 0x21398A + 0x8))) == 0) goto loc_00223C98;
    result = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x213859 + 0x28) + 0x78)) & (*(uint64_t *)(v_rip - 0x21398A + 0x8));
    if (result != (*(uint64_t *)(*(uint64_t *)(v_rip - 0x213859 + 0x28) + 0x78))) goto loc_00223C98;
    goto loc_00223D70;
loc_00223E33:
    if ((uint8_t)(result) == 0) goto loc_00223D4C;
    goto loc_00223C8D;
loc_00223E70:
    if (*(uint64_t *)(v_rip - 0x21398A + 0x8) != 0) goto loc_00223DE1;
    goto loc_00223D70;
loc_00223E8A:
    if ((uint8_t)(result) == 0) goto loc_00223DD6;
    goto loc_00223C98;
loc_00223EDF:
    goto loc_00223BFB;
loc_00223F17:
    result = PsGetServerSiloGlobals(v_stack_p8, v_rip - 2177113, *(uint64_t *)(v_rip - 0x21398A + 0x8), Arg4);
    if (*(uint64_t *)(result + 0x340) == 0) goto loc_00223D24;
    if (*(uint64_t *)(result + 0x340) == 0) goto loc_00223D24;
loc_00223F40:
    Arg1 = (v_stack_p8) << (5);
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x340) + 0x11A8))) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x340) + 0x11A8)) - 1)));
    Arg1 = (Arg1) + (0x11CCULL);
    Arg1 = (Arg1) + (*(uint64_t *)(result + 0x340));
    if (condition_is_equal) goto loc_00223F8F;
    result = (v_stack_p18) >> (29);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg1 + result * 4))) & ((uint32_t)(v_stack_p18)));
    if ((((uint32_t)(Arg1)) & (0x1FFFFFFFULL)) != 0) {
        Arg3 = *(uint8_t *)(*(uint64_t *)(result + 0x340) + (uint32_t)((uint32_t)(v_stack_p8)) * 2 + 0x1198);
        Arg4 = (uint32_t)((uint32_t)(Arg3));
        Arg2 = *(uint64_t *)(result + 0x340);
        v_stack_p28 = 0x601903ULL;
        Arg1 = Arg2;
        v_stack_p20 = Arg5;
        result = EtwpLogKernelEvent(Arg1, Arg2, Arg3, Arg4);
    }
    if ((((uint32_t)(Arg1)) & (0x1FFFFFFFULL)) != 0) goto loc_00223F40;
    goto loc_00223D24;
loc_00223F99:
    if (*(uint64_t *)(result + 0x340) != 0) goto loc_00223FA6;
    goto loc_00223BFB;
loc_00223FA6:
    result = PsIsServerSilo(local_rbx, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00223BFB;
loc_00223FB6:
    result = PsIsServerSilo(*(uint64_t *)(local_rbx + 0x518), Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00223FB6;
    goto loc_00223BFB;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00223BB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
