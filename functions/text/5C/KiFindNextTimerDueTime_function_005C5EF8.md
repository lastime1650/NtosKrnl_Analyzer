# KiFindNextTimerDueTime

- RVA: `0x005C5EF8`–`0x005C6446` (길이 `1,358` bytes)
- VA: `0x00000001405C5EF8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CAAC8`
- 디코드: `377`개 명령, `1,358/1,358` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KePrepareClockTimerForIdle](../5B/KePrepareClockTimerForIdle_function_005BA49C.md) at `0x005BA56A`
- [KePrepareClockTimerForIdle](../5B/KePrepareClockTimerForIdle_function_005BA49C.md) at `0x005BA5DD`
- [KiGetNextTimerExpirationDueTime](../5B/KiGetNextTimerExpirationDueTime_function_005BCF60.md) at `0x005BCFF4`

### Static image references
- `0x005C5F2E` → RVA `0x00FC6C48` (`ALMOSTRO`; read)
- `0x005C5F47` → RVA `0x00FC6BB8` (`ALMOSTRO`; read)
- `0x005C5F4D` → RVA `0x00FC6AA0` (`ALMOSTRO`; read)
- `0x005C5F6F` → RVA `0x00FC8520` (`ALMOSTRO`; read)
- `0x005C5F8E` → RVA `0x00FC5030` (`ALMOSTRO`; read)
- `0x005C5FA6` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x005C5FF2` → RVA `0x00FC8528` (`ALMOSTRO`; read)
- `0x005C6288` → RVA `0x00FC5018` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005C5EF8  48 8B C4                        mov rax, rsp
005C5EFB  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
005C5EFF  44 88 40 18                     mov byte ptr [rax + 0x18], r8b
005C5F03  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
005C5F07  48 89 48 08                     mov qword ptr [rax + 8], rcx
005C5F0B  53                              push rbx
005C5F0C  55                              push rbp
005C5F0D  56                              push rsi
005C5F0E  57                              push rdi
005C5F0F  41 54                           push r12
005C5F11  41 55                           push r13
005C5F13  41 56                           push r14
005C5F15  41 57                           push r15
005C5F17  48 83 EC 28                     sub rsp, 0x28
005C5F1B  41 83 CE FF                     or r14d, 0xffffffff
005C5F1F  49 8B F1                        mov rsi, r9
005C5F22  4C 8B C9                        mov r9, rcx
005C5F25  4C 8B EA                        mov r13, rdx
005C5F28  48 83 C9 FF                     or rcx, 0xffffffffffffffff
005C5F2C  33 ED                           xor ebp, ebp
005C5F2E  39 2D 14 0D A0 00               cmp dword ptr [rip + 0xa00d14], ebp
005C5F34  41 8B D6                        mov edx, r14d
005C5F37  41 8A F8                        mov dil, r8b
005C5F3A  48 89 4C 24 10                  mov qword ptr [rsp + 0x10], rcx
005C5F3F  45 8B D6                        mov r10d, r14d
005C5F42  89 14 24                        mov dword ptr [rsp], edx
005C5F45  75 1B                           jne 0x1405c5f62
005C5F47  8B 05 6B 0C A0 00               mov eax, dword ptr [rip + 0xa00c6b]
005C5F4D  3B 05 4D 0B A0 00               cmp eax, dword ptr [rip + 0xa00b4d]
005C5F53  75 0D                           jne 0x1405c5f62
005C5F55  09 4C 24 08                     or dword ptr [rsp + 8], ecx
005C5F59  44 8D 59 02                     lea r11d, [rcx + 2]
005C5F5D  41 8B DB                        mov ebx, r11d
005C5F60  EB 0D                           jmp 0x1405c5f6f
005C5F62  41 BB 01 00 00 00               mov r11d, 1
005C5F68  8B DD                           mov ebx, ebp
005C5F6A  44 89 5C 24 08                  mov dword ptr [rsp + 8], r11d
005C5F6F  4C 8D 3D AA 25 A0 00            lea r15, [rip + 0xa025aa]
005C5F76  89 5C 24 04                     mov dword ptr [rsp + 4], ebx
005C5F7A  83 FB 02                        cmp ebx, 2
005C5F7D  0F 83 AE 04 00 00               jae 0x1405c6431
005C5F83  49 8B C5                        mov rax, r13
005C5F86  49 83 C8 FF                     or r8, 0xffffffffffffffff
005C5F8A  48 C1 E8 12                     shr rax, 0x12
005C5F8E  39 2D 9C F0 9F 00               cmp dword ptr [rip + 0x9ff09c], ebp
005C5F94  0F B6 D8                        movzx ebx, al
005C5F97  0F 84 F7 01 00 00               je 0x1405c6194
005C5F9D  40 84 FF                        test dil, dil
005C5FA0  0F 84 D5 01 00 00               je 0x1405c617b
005C5FA6  48 8B 0D 93 2C A0 00            mov rcx, qword ptr [rip + 0xa02c93]
005C5FAD  8B 7C 24 04                     mov edi, dword ptr [rsp + 4]
005C5FB1  8B 94 B9 10 83 00 00            mov edx, dword ptr [rcx + rdi*4 + 0x8310]
005C5FB8  2B DA                           sub ebx, edx
005C5FBA  0F B6 C3                        movzx eax, bl
005C5FBD  41 3B C3                        cmp eax, r11d
005C5FC0  0F 87 68 04 00 00               ja 0x1405c642e
005C5FC6  44 8B D5                        mov r10d, ebp
005C5FC9  48 C1 E7 0D                     shl rdi, 0xd
005C5FCD  C1 E0 12                        shl eax, 0x12
005C5FD0  49 8B ED                        mov rbp, r13
005C5FD3  48 81 E5 00 00 FC FF            and rbp, 0xfffffffffffc0000
005C5FDA  44 0F B6 E2                     movzx r12d, dl
005C5FDE  48 2B E8                        sub rbp, rax
005C5FE1  48 03 F9                        add rdi, rcx
005C5FE4  48 81 C5 00 00 00 04            add rbp, 0x4000000
005C5FEB  48 8B 35 2E 25 A0 00            mov rsi, qword ptr [rip + 0xa0252e]
005C5FF2  4C 8B 2D 2F 25 A0 00            mov r13, qword ptr [rip + 0xa0252f]
005C5FF9  45 8B F4                        mov r14d, r12d
005C5FFC  4C 3B F6                        cmp r14, rsi
005C5FFF  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
005C6004  4C 8D 4E FF                     lea r9, [rsi - 1]
005C6008  48 1B DB                        sbb rbx, rbx
005C600B  49 23 DE                        and rbx, r14
005C600E  83 64 24 0C 00                  and dword ptr [rsp + 0xc], 0
005C6013  49 8B C1                        mov rax, r9
005C6016  48 2B C3                        sub rax, rbx
005C6019  49 03 C3                        add rax, r11
005C601C  49 3B C3                        cmp rax, r11
005C601F  73 06                           jae 0x1405c6027
005C6021  48 83 C9 FF                     or rcx, 0xffffffffffffffff
005C6025  EB 79                           jmp 0x1405c60a0
005C6027  8A CB                           mov cl, bl
005C6029  49 8B C1                        mov rax, r9
005C602C  48 C1 E8 06                     shr rax, 6
005C6030  80 E1 3F                        and cl, 0x3f
005C6033  49 8B D3                        mov rdx, r11
005C6036  48 D3 E2                        shl rdx, cl
005C6039  49 2B D3                        sub rdx, r11
005C603C  4C 8D 3C C5 00 00 00 00         lea r15, [rax*8]
005C6044  48 8B C3                        mov rax, rbx
005C6047  48 C1 E8 06                     shr rax, 6
005C604B  4D 03 FD                        add r15, r13
005C604E  48 8D 0C C5 00 00 00 00         lea rcx, [rax*8]
005C6056  49 03 CD                        add rcx, r13
005C6059  48 8B 01                        mov rax, qword ptr [rcx]
005C605C  48 F7 D0                        not rax
005C605F  48 0B C2                        or rax, rdx
005C6062  48 83 CA FF                     or rdx, 0xffffffffffffffff
005C6066  48 3B C2                        cmp rax, rdx
005C6069  75 16                           jne 0x1405c6081
005C606B  48 83 C1 08                     add rcx, 8
005C606F  49 3B CF                        cmp rcx, r15
005C6072  77 08                           ja 0x1405c607c
005C6074  48 8B 01                        mov rax, qword ptr [rcx]
005C6077  48 F7 D0                        not rax
005C607A  EB EA                           jmp 0x1405c6066
005C607C  48 8B CA                        mov rcx, rdx
005C607F  EB 1F                           jmp 0x1405c60a0
005C6081  49 2B CD                        sub rcx, r13
005C6084  48 F7 D0                        not rax
005C6087  48 C1 F9 03                     sar rcx, 3
005C608B  48 0F BC C0                     bsf rax, rax
005C608F  48 C1 E1 06                     shl rcx, 6
005C6093  48 03 C8                        add rcx, rax
005C6096  49 3B C9                        cmp rcx, r9
005C6099  77 E1                           ja 0x1405c607c
005C609B  48 3B CA                        cmp rcx, rdx
005C609E  75 1B                           jne 0x1405c60bb
005C60A0  48 85 DB                        test rbx, rbx
005C60A3  74 16                           je 0x1405c60bb
005C60A5  4D 8D 4C 24 01                  lea r9, [r12 + 1]
005C60AA  4C 3B CE                        cmp r9, rsi
005C60AD  4C 0F 47 CE                     cmova r9, rsi
005C60B1  4D 2B CB                        sub r9, r11
005C60B4  33 DB                           xor ebx, ebx
005C60B6  E9 53 FF FF FF                  jmp 0x1405c600e
005C60BB  8B 14 24                        mov edx, dword ptr [rsp]
005C60BE  41 83 CE FF                     or r14d, 0xffffffff
005C60C2  41 3B CE                        cmp ecx, r14d
005C60C5  0F 84 88 00 00 00               je 0x1405c6153
005C60CB  8B C1                           mov eax, ecx
005C60CD  41 2B C4                        sub eax, r12d
005C60D0  41 03 C3                        add eax, r11d
005C60D3  0F B6 C0                        movzx eax, al
005C60D6  44 03 D0                        add r10d, eax
005C60D9  41 81 FA 00 01 00 00            cmp r10d, 0x100
005C60E0  77 71                           ja 0x1405c6153
005C60E2  44 3B D2                        cmp r10d, edx
005C60E5  77 6C                           ja 0x1405c6153
005C60E7  8B C1                           mov eax, ecx
005C60E9  48 C1 E0 05                     shl rax, 5
005C60ED  48 8B 94 38 18 43 00 00         mov rdx, qword ptr [rax + rdi + 0x4318]
005C60F5  49 3B D0                        cmp rdx, r8
005C60F8  73 47                           jae 0x1405c6141
005C60FA  44 39 B4 38 1C 43 00 00         cmp dword ptr [rax + rdi + 0x431c], r14d
005C6102  74 3D                           je 0x1405c6141
005C6104  48 3B D5                        cmp rdx, rbp
005C6107  73 35                           jae 0x1405c613e
005C6109  48 8B C2                        mov rax, rdx
005C610C  48 C1 E8 12                     shr rax, 0x12
005C6110  44 0F B6 C0                     movzx r8d, al
005C6114  44 3B C1                        cmp r8d, ecx
005C6117  74 34                           je 0x1405c614d
005C6119  8B C1                           mov eax, ecx
005C611B  48 81 E2 00 00 FC FF            and rdx, 0xfffffffffffc0000
005C6122  41 2B C0                        sub eax, r8d
005C6125  C1 E0 12                        shl eax, 0x12
005C6128  25 00 00 FC 03                  and eax, 0x3fc0000
005C612D  4C 8D 04 10                     lea r8, [rax + rdx]
005C6131  4C 3B 44 24 18                  cmp r8, qword ptr [rsp + 0x18]
005C6136  4C 0F 43 44 24 18               cmovae r8, qword ptr [rsp + 0x18]
005C613C  EB 03                           jmp 0x1405c6141
005C613E  4C 8B C2                        mov r8, rdx
005C6141  8D 41 01                        lea eax, [rcx + 1]
005C6144  44 0F B6 E0                     movzx r12d, al
005C6148  E9 9E FE FF FF                  jmp 0x1405c5feb
005C614D  4C 8B C2                        mov r8, rdx
005C6150  8B 14 24                        mov edx, dword ptr [rsp]
005C6153  4C 8B 6C 24 78                  mov r13, qword ptr [rsp + 0x78]
005C6158  4C 8D 3D C1 23 A0 00            lea r15, [rip + 0xa023c1]
005C615F  4C 8B 4C 24 70                  mov r9, qword ptr [rsp + 0x70]
005C6164  33 ED                           xor ebp, ebp
005C6166  40 8A BC 24 80 00 00 00         mov dil, byte ptr [rsp + 0x80]
005C616E  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
005C6176  48 8B 4C 24 10                  mov rcx, qword ptr [rsp + 0x10]
005C617B  8B 5C 24 04                     mov ebx, dword ptr [rsp + 4]
005C617F  85 DB                           test ebx, ebx
005C6181  0F 85 89 02 00 00               jne 0x1405c6410
005C6187  49 8B C8                        mov rcx, r8
005C618A  48 89 4C 24 10                  mov qword ptr [rsp + 0x10], rcx
005C618F  E9 7F 02 00 00                  jmp 0x1405c6413
005C6194  8B 44 24 04                     mov eax, dword ptr [rsp + 4]
005C6198  41 8B 8C 81 10 83 00 00         mov ecx, dword ptr [r9 + rax*4 + 0x8310]
005C61A0  0F B6 C1                        movzx eax, cl
005C61A3  3B D8                           cmp ebx, eax
005C61A5  0F 85 83 02 00 00               jne 0x1405c642e
005C61AB  40 84 FF                        test dil, dil
005C61AE  0F 84 2A 01 00 00               je 0x1405c62de
005C61B4  44 8B FB                        mov r15d, ebx
005C61B7  4C 8D 25 62 23 A0 00            lea r12, [rip + 0xa02362]
005C61BE  41 C1 E7 09                     shl r15d, 9
005C61C2  45 8B D6                        mov r10d, r14d
005C61C5  0F B7 FD                        movzx edi, bp
005C61C8  0F B7 C7                        movzx eax, di
005C61CB  48 03 C0                        add rax, rax
005C61CE  49 8B 34 C4                     mov rsi, qword ptr [r12 + rax*8]
005C61D2  4D 8B 74 C4 08                  mov r14, qword ptr [r12 + rax*8 + 8]
005C61D7  4C 3B FE                        cmp r15, rsi
005C61DA  4D 1B C9                        sbb r9, r9
005C61DD  4D 23 CF                        and r9, r15
005C61E0  48 8D 56 FF                     lea rdx, [rsi - 1]
005C61E4  48 8B C2                        mov rax, rdx
005C61E7  89 6C 24 0C                     mov dword ptr [rsp + 0xc], ebp
005C61EB  49 2B C1                        sub rax, r9
005C61EE  49 03 C3                        add rax, r11
005C61F1  49 3B C3                        cmp rax, r11
005C61F4  73 06                           jae 0x1405c61fc
005C61F6  48 83 C9 FF                     or rcx, 0xffffffffffffffff
005C61FA  EB 53                           jmp 0x1405c624f
005C61FC  48 8B C2                        mov rax, rdx
005C61FF  48 C1 E8 06                     shr rax, 6
005C6203  49 8D 2C C6                     lea rbp, [r14 + rax*8]
005C6207  49 8B C1                        mov rax, r9
005C620A  48 C1 E8 06                     shr rax, 6
005C620E  49 8D 0C C6                     lea rcx, [r14 + rax*8]
005C6212  48 8B 01                        mov rax, qword ptr [rcx]
005C6215  48 F7 D0                        not rax
005C6218  48 83 F8 FF                     cmp rax, -1
005C621C  75 0F                           jne 0x1405c622d
005C621E  48 83 C1 08                     add rcx, 8
005C6222  48 3B CD                        cmp rcx, rbp
005C6225  76 EB                           jbe 0x1405c6212
005C6227  48 83 C9 FF                     or rcx, 0xffffffffffffffff
005C622B  EB 20                           jmp 0x1405c624d
005C622D  49 2B CE                        sub rcx, r14
005C6230  48 F7 D0                        not rax
005C6233  48 C1 F9 03                     sar rcx, 3
005C6237  48 0F BC C0                     bsf rax, rax
005C623B  48 C1 E1 06                     shl rcx, 6
005C623F  48 03 C8                        add rcx, rax
005C6242  48 3B CA                        cmp rcx, rdx
005C6245  77 E0                           ja 0x1405c6227
005C6247  48 83 F9 FF                     cmp rcx, -1
005C624B  75 1D                           jne 0x1405c626a
005C624D  33 ED                           xor ebp, ebp
005C624F  4D 85 C9                        test r9, r9
005C6252  74 18                           je 0x1405c626c
005C6254  49 8D 57 01                     lea rdx, [r15 + 1]
005C6258  4C 8B CD                        mov r9, rbp
005C625B  48 3B D6                        cmp rdx, rsi
005C625E  48 0F 47 D6                     cmova rdx, rsi
005C6262  49 2B D3                        sub rdx, r11
005C6265  E9 7A FF FF FF                  jmp 0x1405c61e4
005C626A  33 ED                           xor ebp, ebp
005C626C  41 83 CE FF                     or r14d, 0xffffffff
005C6270  41 3B CE                        cmp ecx, r14d
005C6273  74 0F                           je 0x1405c6284
005C6275  C1 E9 09                        shr ecx, 9
005C6278  2B CB                           sub ecx, ebx
005C627A  0F B6 C1                        movzx eax, cl
005C627D  41 3B C2                        cmp eax, r10d
005C6280  44 0F 42 D0                     cmovb r10d, eax
005C6284  66 41 03 FB                     add di, r11w
005C6288  66 3B 3D 89 ED 9F 00            cmp di, word ptr [rip + 0x9fed89]
005C628F  0F 82 33 FF FF FF               jb 0x1405c61c8
005C6295  8B 14 24                        mov edx, dword ptr [rsp]
005C6298  4C 8D 3D 81 22 A0 00            lea r15, [rip + 0xa02281]
005C629F  4C 8B 4C 24 70                  mov r9, qword ptr [rsp + 0x70]
005C62A4  40 8A BC 24 80 00 00 00         mov dil, byte ptr [rsp + 0x80]
005C62AC  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
005C62B4  45 3B D6                        cmp r10d, r14d
005C62B7  0F 84 B9 FE FF FF               je 0x1405c6176
005C62BD  8B 0D F5 08 A0 00               mov ecx, dword ptr [rip + 0xa008f5]
005C62C3  45 8B C2                        mov r8d, r10d
005C62C6  41 C1 E0 12                     shl r8d, 0x12
005C62CA  49 8B C5                        mov rax, r13
005C62CD  48 25 00 00 FC FF               and rax, 0xfffffffffffc0000
005C62D3  4C 03 C0                        add r8, rax
005C62D6  4C 03 C1                        add r8, rcx
005C62D9  E9 98 FE FF FF                  jmp 0x1405c6176
005C62DE  41 0F B6 B1 D0 00 00 00         movzx esi, byte ptr [r9 + 0xd0]
005C62E6  44 8B D5                        mov r10d, ebp
005C62E9  4D 8B A1 C8 00 00 00            mov r12, qword ptr [r9 + 0xc8]
005C62F0  48 03 F6                        add rsi, rsi
005C62F3  4C 89 64 24 18                  mov qword ptr [rsp + 0x18], r12
005C62F8  4D 8B 6C F7 08                  mov r13, qword ptr [r15 + rsi*8 + 8]
005C62FD  49 8B 2C F7                     mov rbp, qword ptr [r15 + rsi*8]
005C6301  4D 8B 7C F7 08                  mov r15, qword ptr [r15 + rsi*8 + 8]
005C6306  8B FB                           mov edi, ebx
005C6308  48 C1 E7 09                     shl rdi, 9
005C630C  48 3B FD                        cmp rdi, rbp
005C630F  48 8D 55 FF                     lea rdx, [rbp - 1]
005C6313  4D 1B C9                        sbb r9, r9
005C6316  4C 23 CF                        and r9, rdi
005C6319  45 33 E4                        xor r12d, r12d
005C631C  48 8B C2                        mov rax, rdx
005C631F  44 89 64 24 0C                  mov dword ptr [rsp + 0xc], r12d
005C6324  49 2B C1                        sub rax, r9
005C6327  49 03 C3                        add rax, r11
005C632A  49 3B C3                        cmp rax, r11
005C632D  73 06                           jae 0x1405c6335
005C632F  48 83 C9 FF                     or rcx, 0xffffffffffffffff
005C6333  EB 4D                           jmp 0x1405c6382
005C6335  48 8B C2                        mov rax, rdx
005C6338  48 C1 E8 06                     shr rax, 6
005C633C  4D 8D 34 C7                     lea r14, [r15 + rax*8]
005C6340  49 8B C1                        mov rax, r9
005C6343  48 C1 E8 06                     shr rax, 6
005C6347  49 8D 0C C7                     lea rcx, [r15 + rax*8]
005C634B  48 8B 01                        mov rax, qword ptr [rcx]
005C634E  48 F7 D0                        not rax
005C6351  48 83 F8 FF                     cmp rax, -1
005C6355  75 0B                           jne 0x1405c6362
005C6357  48 83 C1 08                     add rcx, 8
005C635B  49 3B CE                        cmp rcx, r14
005C635E  76 EB                           jbe 0x1405c634b
005C6360  EB CD                           jmp 0x1405c632f
005C6362  49 2B CF                        sub rcx, r15
005C6365  48 F7 D0                        not rax
005C6368  48 C1 F9 03                     sar rcx, 3
005C636C  48 0F BC C0                     bsf rax, rax
005C6370  48 C1 E1 06                     shl rcx, 6
005C6374  48 03 C8                        add rcx, rax
005C6377  48 3B CA                        cmp rcx, rdx
005C637A  77 B3                           ja 0x1405c632f
005C637C  48 83 F9 FF                     cmp rcx, -1
005C6380  75 18                           jne 0x1405c639a
005C6382  4D 85 C9                        test r9, r9
005C6385  74 13                           je 0x1405c639a
005C6387  48 8D 57 01                     lea rdx, [rdi + 1]
005C638B  4D 8B CC                        mov r9, r12
005C638E  48 3B D5                        cmp rdx, rbp
005C6391  48 0F 47 D5                     cmova rdx, rbp
005C6395  49 2B D3                        sub rdx, r11
005C6398  EB 82                           jmp 0x1405c631c
005C639A  4C 8B 64 24 18                  mov r12, qword ptr [rsp + 0x18]
005C639F  41 83 CE FF                     or r14d, 0xffffffff
005C63A3  41 3B CE                        cmp ecx, r14d
005C63A6  0F 84 A4 FD FF FF               je 0x1405c6150
005C63AC  C1 E9 09                        shr ecx, 9
005C63AF  8B C1                           mov eax, ecx
005C63B1  2B C3                           sub eax, ebx
005C63B3  0F B6 C0                        movzx eax, al
005C63B6  44 03 D0                        add r10d, eax
005C63B9  41 81 FA 00 01 00 00            cmp r10d, 0x100
005C63C0  0F 87 8A FD FF FF               ja 0x1405c6150
005C63C6  8B C1                           mov eax, ecx
005C63C8  4C 8D 3D 51 21 A0 00            lea r15, [rip + 0xa02151]
005C63CF  48 C1 E0 06                     shl rax, 6
005C63D3  4E 85 24 28                     test qword ptr [rax + r13], r12
005C63D7  75 0E                           jne 0x1405c63e7
005C63D9  8D 41 01                        lea eax, [rcx + 1]
005C63DC  45 03 D3                        add r10d, r11d
005C63DF  0F B6 D8                        movzx ebx, al
005C63E2  E9 16 FF FF FF                  jmp 0x1405c62fd
005C63E7  4C 8B 6C 24 78                  mov r13, qword ptr [rsp + 0x78]
005C63EC  45 8B C2                        mov r8d, r10d
005C63EF  8B 0D C3 07 A0 00               mov ecx, dword ptr [rip + 0xa007c3]
005C63F5  49 8B C5                        mov rax, r13
005C63F8  8B 14 24                        mov edx, dword ptr [rsp]
005C63FB  48 25 00 00 FC FF               and rax, 0xfffffffffffc0000
005C6401  41 C1 E0 12                     shl r8d, 0x12
005C6405  4C 03 C0                        add r8, rax
005C6408  4C 03 C1                        add r8, rcx
005C640B  E9 4F FD FF FF                  jmp 0x1405c615f
005C6410  4C 89 06                        mov qword ptr [rsi], r8
005C6413  49 83 F8 FF                     cmp r8, -1
005C6417  74 0C                           je 0x1405c6425
005C6419  41 8D 42 01                     lea eax, [r10 + 1]
005C641D  3B D0                           cmp edx, eax
005C641F  0F 43 D0                        cmovae edx, eax
005C6422  89 14 24                        mov dword ptr [rsp], edx
005C6425  03 5C 24 08                     add ebx, dword ptr [rsp + 8]
005C6429  E9 48 FB FF FF                  jmp 0x1405c5f76
005C642E  48 8B CD                        mov rcx, rbp
005C6431  48 8B C1                        mov rax, rcx
005C6434  48 83 C4 28                     add rsp, 0x28
005C6438  41 5F                           pop r15
005C643A  41 5E                           pop r14
005C643C  41 5D                           pop r13
005C643E  41 5C                           pop r12
005C6440  5F                              pop rdi
005C6441  5E                              pop rsi
005C6442  5D                              pop rbp
005C6443  5B                              pop rbx
005C6444  C3                              ret
005C6445  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiFindNextTimerDueTime(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int8 *)(v_rsp + 24) = (unsigned __int8)(a3);
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (40);
    v_r14 = (unsigned int)((v_r14) | (0xFFFFFFFFULL));
    a1 = (a1) | (-1);
    v_rbp = 0;
    v_stack_m58 = a1;
    v_stack_m68 = (unsigned int)((unsigned int)((unsigned int)(v_r14)));
    if ((*(unsigned int *)(v_rip + 10489108)) != 0) goto loc_005C5F62;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10488939)))) != (*(unsigned int *)(v_rip + 10488653))) goto loc_005C5F62;
    goto loc_005C5F6F;
loc_005C5F62:
    v_stack_m60 = 1;
loc_005C5F6F:
loc_005C5F76:
    v_stack_m64 = 0;
    if (0 >= 2) goto loc_005C6431;
    a3 = (a3) | (-1);
    result = (a2) >> (18);
    if ((*(unsigned int *)(v_rip + 10481820)) == 0) goto loc_005C6194;
    if ((unsigned __int8)((unsigned __int8)(a3)) == 0) goto loc_005C617B;
    v_rbx = (unsigned int)(((unsigned __int8)(result)) - ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10497171) + (unsigned int)(v_stack_m64) * 4 + 33552)))));
    if (((unsigned int)((unsigned __int8)(v_rbx))) > 1) goto loc_005C642E;
    v_rdi = ((unsigned int)(v_stack_m64)) << (13);
    result = (unsigned int)(((unsigned __int8)(v_rbx)) << (18));
    v_rbp = (a2) & (0xFFFFFFFFFFFC0000ULL);
    v_rbp = (v_rbp) - (result);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_rip + 10497171));
    v_rbp = (v_rbp) + (0x4000000ULL);
loc_005C5FEB:
    v_stack_m50 = a3;
    v_rbx = (v_rbx) & ((unsigned int)((unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10497171) + (unsigned int)(v_stack_m64) * 4 + 33552))))));
loc_005C600E:
    result = (*(unsigned __int64 *)(v_rip + 10495278) - 1) - (v_rbx);
    result = (result) + (1);
    if (result >= 1) goto loc_005C6027;
    a1 = (*(unsigned __int64 *)(v_rip + 10497171)) | (-1);
    goto loc_005C60A0;
loc_005C6027:
    result = (*(unsigned __int64 *)(v_rip + 10495278) - 1) >> (6);
    a1 = (unsigned __int8)(((unsigned __int8)(v_rbx)) & (63));
    a2 = (1) << ((unsigned __int8)(a1));
    a2 = (a2) - (1);
    result = (v_rbx) >> (6);
    v_r15 = (result * 8) + (*(unsigned __int64 *)(v_rip + 10495279));
    a1 = (result * 8) + (*(unsigned __int64 *)(v_rip + 10495279));
    result = ~(*(unsigned __int64 *)(a1));
    result = (result) | (a2);
    a2 = (a2) | (-1);
loc_005C6066:
    if (result != a2) goto loc_005C6081;
    a1 = (a1) + (8);
    if (a1 > v_r15) goto loc_005C607C;
    result = ~(*(unsigned __int64 *)(a1));
    goto loc_005C6066;
loc_005C607C:
    goto loc_005C60A0;
loc_005C6081:
    a1 = (a2) - (*(unsigned __int64 *)(v_rip + 10495279));
    result = ~(result);
    a1 = (a1) >> (3);
    a1 = (a1) << (6);
    a1 = (a1) + (result);
    if (a1 > (*(unsigned __int64 *)(v_rip + 10495278) - 1)) goto loc_005C607C;
    if (a1 != a2) goto loc_005C60BB;
loc_005C60A0:
    if (v_rbx == 0) goto loc_005C60BB;
    a4 = (unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10497171) + (unsigned int)(v_stack_m64) * 4 + 33552))) + 1;
    if (((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10497171) + (unsigned int)(v_stack_m64) * 4 + 33552))) + 1) > (*(unsigned __int64 *)(v_rip + 10495278))) { a4 = *(unsigned __int64 *)(v_rip + 10495278); }
    a4 = (a4) - (1);
    v_rbx = 0;
    goto loc_005C600E;
loc_005C60BB:
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10497171) + (unsigned int)(v_stack_m64) * 4 + 33552)))))) | (0xFFFFFFFFULL));
    if (((unsigned int)(a1)) == ((unsigned int)(v_r14))) goto loc_005C6153;
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) - ((unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10497171) + (unsigned int)(v_stack_m64) * 4 + 33552))))));
    result = (unsigned int)((result) + (1));
    v_r10 = (unsigned int)((0) + ((unsigned int)((unsigned __int8)(result))));
    if (((unsigned int)(v_r10)) > 256) goto loc_005C6153;
    if (((unsigned int)(v_r10)) > ((unsigned int)((unsigned int)(v_stack_m68)))) goto loc_005C6153;
    result = ((unsigned int)((unsigned int)(a1))) << (5);
    if ((*(unsigned __int64 *)(result + v_rdi * 1 + 17176)) >= a3) goto loc_005C6141;
    if ((*(unsigned int *)(result + v_rdi * 1 + 17180)) == ((unsigned int)(v_r14))) goto loc_005C6141;
    if ((*(unsigned __int64 *)(result + v_rdi * 1 + 17176)) >= v_rbp) goto loc_005C613E;
    result = (*(unsigned __int64 *)(result + v_rdi * 1 + 17176)) >> (18);
    if (((unsigned int)((unsigned __int8)(result))) == ((unsigned int)(a1))) goto loc_005C614D;
    a2 = (*(unsigned __int64 *)(result + v_rdi * 1 + 17176)) & (0xFFFFFFFFFFFC0000ULL);
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) - ((unsigned int)((unsigned __int8)(result))));
    result = (unsigned int)((result) << (18));
    result = (unsigned int)((result) & (0x3FC0000ULL));
    a3 = result + a2 * 1;
    if ((result + a2 * 1) >= v_stack_m50) { a3 = v_stack_m50; }
    goto loc_005C6141;
loc_005C613E:
loc_005C6141:
    goto loc_005C5FEB;
loc_005C614D:
loc_005C6150:
loc_005C6153:
loc_005C615F:
    v_rbp = 0;
loc_005C6176:
loc_005C617B:
    if ((unsigned int)((unsigned int)(v_stack_m64)) != 0) goto loc_005C6410;
    v_stack_m58 = a2;
    goto loc_005C6413;
loc_005C6194:
    if (((unsigned int)((unsigned int)(v_stack_m64))) != ((unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + (unsigned int)(v_stack_m64) * 4 + 33552)))))) goto loc_005C642E;
    if ((unsigned __int8)(v_stack_p18) == 0) goto loc_005C62DE;
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m64)))) << (9));
loc_005C61C8:
    result = (0) + (0);
    a4 = (v_stack_p8) & (v_r15);
loc_005C61E4:
    v_stack_m5C = 0;
    result = (*(unsigned __int64 *)(v_rip + 10494818 + result * 8) - 1) - (a4);
    result = (result) + (1);
    if (result >= 1) goto loc_005C61FC;
    a1 = ((unsigned int)(*(unsigned int *)(v_stack_p8 + (unsigned int)(v_stack_m64) * 4 + 33552))) | (-1);
    goto loc_005C624F;
loc_005C61FC:
    result = (*(unsigned __int64 *)(v_rip + 10494818 + result * 8) - 1) >> (6);
    result = (a4) >> (6);
loc_005C6212:
    result = ~(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10494818 + result * 8 + 8) + result * 8));
    if (result != -1) goto loc_005C622D;
    a1 = (*(unsigned __int64 *)(v_rip + 10494818 + result * 8 + 8) + result * 8) + (8);
    if (a1 <= (*(unsigned __int64 *)(v_rip + 10494818 + result * 8 + 8) + result * 8)) goto loc_005C6212;
loc_005C6227:
    a1 = (a1) | (-1);
    goto loc_005C624D;
loc_005C622D:
    a1 = (a1) - (*(unsigned __int64 *)(v_rip + 10494818 + result * 8 + 8));
    result = ~(result);
    a1 = (a1) >> (3);
    a1 = (a1) << (6);
    a1 = (a1) + (result);
    if (a1 > (*(unsigned __int64 *)(v_rip + 10494818 + result * 8) - 1)) goto loc_005C6227;
    if (a1 != -1) goto loc_005C626A;
loc_005C624D:
    v_rbp = 0;
loc_005C624F:
    if (a4 == 0) goto loc_005C626C;
    a2 = v_r15 + 1;
    if ((v_r15 + 1) > (*(unsigned __int64 *)(v_rip + 10494818 + result * 8))) { a2 = *(unsigned __int64 *)(v_rip + 10494818 + result * 8); }
    a2 = (a2) - (1);
    goto loc_005C61E4;
loc_005C626A:
    v_rbp = 0;
loc_005C626C:
    v_r14 = (unsigned int)((*(unsigned __int64 *)(v_rip + 10494818 + result * 8 + 8)) | (0xFFFFFFFFULL));
    v_r10 = (unsigned int)((unsigned int)(v_r14));
    if (((unsigned int)(a1)) != ((unsigned int)(v_r14))) {
        a1 = (unsigned int)((a1) >> (9));
        a1 = (unsigned int)((a1) - ((unsigned int)((unsigned int)(v_stack_m64))));
        result = (unsigned __int8)(a1);
        v_r10 = (unsigned int)((unsigned int)(v_r14));
        if (((unsigned int)(result)) < ((unsigned int)((unsigned int)((unsigned int)(v_r14))))) { v_r10 = (unsigned int)(result); }
    }
    v_rdi = (unsigned __int16)((0) + (1));
    if (((unsigned __int16)(v_rdi)) < (*(unsigned __int16 *)(v_rip + 10481033))) goto loc_005C61C8;
    if (((unsigned int)(v_r10)) == ((unsigned int)(v_r14))) goto loc_005C6176;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) << (18));
    result = (v_stack_p10) & (0xFFFFFFFFFFFC0000ULL);
    a3 = (a3) + (result);
    a3 = (a3) + ((unsigned int)(*(unsigned int *)(v_rip + 10488053)));
    goto loc_005C6176;
loc_005C62DE:
    v_rsi = (*(unsigned __int8 *)(v_stack_p8 + 208)) + (*(unsigned __int8 *)(v_stack_p8 + 208));
    v_stack_m50 = *(unsigned __int64 *)(v_stack_p8 + 200);
loc_005C62FD:
    v_rdi = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m64)))) << (9);
    a4 = (v_stack_p8) & (v_rdi);
    v_r12 = 0;
loc_005C631C:
    v_stack_m5C = 0;
    result = (*(unsigned __int64 *)(v_rip + 10494593 + v_rsi * 8) - 1) - (a4);
    result = (result) + (1);
    if (result >= 1) goto loc_005C6335;
loc_005C632F:
    a1 = ((unsigned int)(*(unsigned int *)(v_rip + 10488053))) | (-1);
    goto loc_005C6382;
loc_005C6335:
    result = (*(unsigned __int64 *)(v_rip + 10494593 + v_rsi * 8) - 1) >> (6);
    result = (a4) >> (6);
loc_005C634B:
    result = ~(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10494593 + v_rsi * 8 + 8) + result * 8));
    if (result != -1) goto loc_005C6362;
    a1 = (*(unsigned __int64 *)(v_rip + 10494593 + v_rsi * 8 + 8) + result * 8) + (8);
    if (a1 <= (*(unsigned __int64 *)(v_rip + 10494593 + v_rsi * 8 + 8) + result * 8)) goto loc_005C634B;
    goto loc_005C632F;
loc_005C6362:
    a1 = (a1) - (*(unsigned __int64 *)(v_rip + 10494593 + v_rsi * 8 + 8));
    result = ~(result);
    a1 = (a1) >> (3);
    a1 = (a1) << (6);
    a1 = (a1) + (result);
    if (a1 > (*(unsigned __int64 *)(v_rip + 10494593 + v_rsi * 8) - 1)) goto loc_005C632F;
    if (a1 != -1) goto loc_005C639A;
loc_005C6382:
    if (a4 == 0) goto loc_005C639A;
    a2 = v_rdi + 1;
    if ((v_rdi + 1) > (*(unsigned __int64 *)(v_rip + 10494593 + v_rsi * 8))) { a2 = *(unsigned __int64 *)(v_rip + 10494593 + v_rsi * 8); }
    a2 = (a2) - (1);
    goto loc_005C631C;
loc_005C639A:
    v_r14 = (unsigned int)((*(unsigned __int64 *)(v_rip + 10494593 + v_rsi * 8 + 8) + result * 8) | (0xFFFFFFFFULL));
    if (((unsigned int)(a1)) == ((unsigned int)(v_r14))) goto loc_005C6150;
    a1 = (unsigned int)((a1) >> (9));
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) - ((unsigned int)((unsigned int)(v_stack_m64))));
    v_r10 = (unsigned int)((0) + ((unsigned int)((unsigned __int8)(result))));
    if (((unsigned int)(v_r10)) > 256) goto loc_005C6150;
    result = ((unsigned int)((unsigned int)(a1))) << (6);
    if (((*(unsigned __int64 *)(result + *(unsigned __int64 *)(v_rip + 10494593 + v_rsi * 8 + 8) * 1)) & (v_stack_m50)) != 0) goto loc_005C63E7;
    v_r10 = (unsigned int)((v_r10) + (1));
    goto loc_005C62FD;
loc_005C63E7:
    result = (v_stack_p10) & (0xFFFFFFFFFFFC0000ULL);
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) << (18));
    a3 = (a3) + (result);
    a3 = (a3) + ((unsigned int)(*(unsigned int *)(v_rip + 10487747)));
    goto loc_005C615F;
loc_005C6410:
    *(unsigned __int64 *)(v_rsi) = a3;
loc_005C6413:
    if (a3 != -1) {
        result = v_r10 + 1;
        a2 = (unsigned int)(v_stack_m68);
        if (((unsigned int)((unsigned int)(v_stack_m68))) >= ((unsigned int)(result))) { a2 = (unsigned int)(result); }
        v_stack_m68 = (unsigned int)(a2);
    }
    v_rbx = (unsigned int)(((unsigned __int8)(a1 + 1)) + (v_stack_m60));
    goto loc_005C5F76;
loc_005C642E:
loc_005C6431:
    v_rsp = (v_rsp) + (40);
    return *(unsigned __int64 *)(v_rip + 10494593 + v_rsi * 8);
}
```

## 5. (Beta) C Style

```c
int64_t KiFindNextTimerDueTime(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint64_t v_stack_p10;
    uint8_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint8_t *)(local_rsp + 0x18) = (uint8_t)(Arg3);
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (40);
    local_r14 = (uint32_t)((local_r14) | (0xFFFFFFFFULL));
    Arg1 = (Arg1) | (-1);
    local_rbp = 0;
    v_stack_m58 = Arg1;
    v_stack_m68 = (uint32_t)((uint32_t)((uint32_t)(local_r14)));
    if ((*(uint32_t *)(v_rip + 0xA00D14)) != 0) goto loc_005C5F62;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA00C6B)))) != (*(uint32_t *)(v_rip + 0xA00B4D))) goto loc_005C5F62;
    goto loc_005C5F6F;
loc_005C5F62:
    v_stack_m60 = 1;
loc_005C5F6F:
loc_005C5F76:
    v_stack_m64 = 0;
    if (0 >= 2) goto loc_005C6431;
    Arg3 = (Arg3) | (-1);
    result = (Arg2) >> (18);
    if ((*(uint32_t *)(v_rip + 0x9FF09C)) == 0) goto loc_005C6194;
    if ((uint8_t)((uint8_t)(Arg3)) == 0) goto loc_005C617B;
    local_rbx = (uint32_t)(((uint8_t)(result)) - ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA02C93) + (uint32_t)(v_stack_m64) * 4 + 0x8310)))));
    if (((uint32_t)((uint8_t)(local_rbx))) > 1) goto loc_005C642E;
    local_rdi = ((uint32_t)(v_stack_m64)) << (13);
    result = (uint32_t)(((uint8_t)(local_rbx)) << (18));
    local_rbp = (Arg2) & (0xFFFFFFFFFFFC0000ULL);
    local_rbp = (local_rbp) - (result);
    local_rdi = (local_rdi) + (*(uint64_t *)(v_rip + 0xA02C93));
    local_rbp = (local_rbp) + (0x4000000ULL);
loc_005C5FEB:
    v_stack_m50 = Arg3;
    local_rbx = (local_rbx) & ((uint32_t)((uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA02C93) + (uint32_t)(v_stack_m64) * 4 + 0x8310))))));
loc_005C600E:
    result = (*(uint64_t *)(v_rip + 0xA0252E) - 1) - (local_rbx);
    result = (result) + (1);
    if (result >= 1) goto loc_005C6027;
    Arg1 = (*(uint64_t *)(v_rip + 0xA02C93)) | (-1);
    goto loc_005C60A0;
loc_005C6027:
    result = (*(uint64_t *)(v_rip + 0xA0252E) - 1) >> (6);
    Arg1 = (uint8_t)(((uint8_t)(local_rbx)) & (63));
    Arg2 = (1) << ((uint8_t)(Arg1));
    Arg2 = (Arg2) - (1);
    result = (local_rbx) >> (6);
    local_r15 = (result * 8) + (*(uint64_t *)(v_rip + 0xA0252F));
    Arg1 = (result * 8) + (*(uint64_t *)(v_rip + 0xA0252F));
    result = ~(*(uint64_t *)(arg1));
    result = (result) | (Arg2);
    Arg2 = (Arg2) | (-1);
loc_005C6066:
    if (result != Arg2) goto loc_005C6081;
    Arg1 = (Arg1) + (8);
    if (Arg1 > local_r15) goto loc_005C607C;
    result = ~(*(uint64_t *)(arg1));
    goto loc_005C6066;
loc_005C607C:
    goto loc_005C60A0;
loc_005C6081:
    Arg1 = (Arg2) - (*(uint64_t *)(v_rip + 0xA0252F));
    result = ~(result);
    Arg1 = (Arg1) >> (3);
    Arg1 = (Arg1) << (6);
    Arg1 = (Arg1) + (result);
    if (Arg1 > (*(uint64_t *)(v_rip + 0xA0252E) - 1)) goto loc_005C607C;
    if (Arg1 != Arg2) goto loc_005C60BB;
loc_005C60A0:
    if (local_rbx == 0) goto loc_005C60BB;
    Arg4 = (uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA02C93) + (uint32_t)(v_stack_m64) * 4 + 0x8310))) + 1;
    if (((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA02C93) + (uint32_t)(v_stack_m64) * 4 + 0x8310))) + 1) > (*(uint64_t *)(v_rip + 0xA0252E))) { Arg4 = *(uint64_t *)(v_rip + 0xA0252E); }
    Arg4 = (Arg4) - (1);
    local_rbx = 0;
    goto loc_005C600E;
loc_005C60BB:
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA02C93) + (uint32_t)(v_stack_m64) * 4 + 0x8310)))))) | (0xFFFFFFFFULL));
    if (((uint32_t)(Arg1)) == ((uint32_t)(local_r14))) goto loc_005C6153;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) - ((uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA02C93) + (uint32_t)(v_stack_m64) * 4 + 0x8310))))));
    result = (uint32_t)((result) + (1));
    local_r10 = (uint32_t)((0) + ((uint32_t)((uint8_t)(result))));
    if (((uint32_t)(local_r10)) > 256) goto loc_005C6153;
    if (((uint32_t)(local_r10)) > ((uint32_t)((uint32_t)(v_stack_m68)))) goto loc_005C6153;
    result = ((uint32_t)((uint32_t)(Arg1))) << (5);
    if ((*(uint64_t *)(result + local_rdi * 1 + 0x4318)) >= Arg3) goto loc_005C6141;
    if ((*(uint32_t *)(result + local_rdi * 1 + 0x431C)) == ((uint32_t)(local_r14))) goto loc_005C6141;
    if ((*(uint64_t *)(result + local_rdi * 1 + 0x4318)) >= local_rbp) goto loc_005C613E;
    result = (*(uint64_t *)(result + local_rdi * 1 + 0x4318)) >> (18);
    if (((uint32_t)((uint8_t)(result))) == ((uint32_t)(Arg1))) goto loc_005C614D;
    Arg2 = (*(uint64_t *)(result + local_rdi * 1 + 0x4318)) & (0xFFFFFFFFFFFC0000ULL);
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) - ((uint32_t)((uint8_t)(result))));
    result = (uint32_t)((result) << (18));
    result = (uint32_t)((result) & (0x3FC0000ULL));
    Arg3 = result + Arg2 * 1;
    if ((result + Arg2 * 1) >= v_stack_m50) { Arg3 = v_stack_m50; }
    goto loc_005C6141;
loc_005C613E:
loc_005C6141:
    goto loc_005C5FEB;
loc_005C614D:
loc_005C6150:
loc_005C6153:
loc_005C615F:
    local_rbp = 0;
loc_005C6176:
loc_005C617B:
    if ((uint32_t)((uint32_t)(v_stack_m64)) != 0) goto loc_005C6410;
    v_stack_m58 = Arg2;
    goto loc_005C6413;
loc_005C6194:
    if (((uint32_t)((uint32_t)(v_stack_m64))) != ((uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + (uint32_t)(v_stack_m64) * 4 + 0x8310)))))) goto loc_005C642E;
    if ((uint8_t)(v_stack_p18) == 0) goto loc_005C62DE;
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m64)))) << (9));
loc_005C61C8:
    result = (0) + (0);
    Arg4 = (v_stack_p8) & (local_r15);
loc_005C61E4:
    v_stack_m5C = 0;
    result = (*(uint64_t *)(v_rip + 0xA02362 + result * 8) - 1) - (Arg4);
    result = (result) + (1);
    if (result >= 1) goto loc_005C61FC;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_stack_p8 + (uint32_t)(v_stack_m64) * 4 + 0x8310))) | (-1);
    goto loc_005C624F;
loc_005C61FC:
    result = (*(uint64_t *)(v_rip + 0xA02362 + result * 8) - 1) >> (6);
    result = (Arg4) >> (6);
loc_005C6212:
    result = ~(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA02362 + result * 8 + 0x8) + result * 8));
    if (result != -1) goto loc_005C622D;
    Arg1 = (*(uint64_t *)(v_rip + 0xA02362 + result * 8 + 0x8) + result * 8) + (8);
    if (Arg1 <= (*(uint64_t *)(v_rip + 0xA02362 + result * 8 + 0x8) + result * 8)) goto loc_005C6212;
loc_005C6227:
    Arg1 = (Arg1) | (-1);
    goto loc_005C624D;
loc_005C622D:
    Arg1 = (Arg1) - (*(uint64_t *)(v_rip + 0xA02362 + result * 8 + 0x8));
    result = ~(result);
    Arg1 = (Arg1) >> (3);
    Arg1 = (Arg1) << (6);
    Arg1 = (Arg1) + (result);
    if (Arg1 > (*(uint64_t *)(v_rip + 0xA02362 + result * 8) - 1)) goto loc_005C6227;
    if (Arg1 != -1) goto loc_005C626A;
loc_005C624D:
    local_rbp = 0;
loc_005C624F:
    if (Arg4 == 0) goto loc_005C626C;
    Arg2 = local_r15 + 1;
    if ((local_r15 + 1) > (*(uint64_t *)(v_rip + 0xA02362 + result * 8))) { Arg2 = *(uint64_t *)(v_rip + 0xA02362 + result * 8); }
    Arg2 = (Arg2) - (1);
    goto loc_005C61E4;
loc_005C626A:
    local_rbp = 0;
loc_005C626C:
    local_r14 = (uint32_t)((*(uint64_t *)(v_rip + 0xA02362 + result * 8 + 0x8)) | (0xFFFFFFFFULL));
    local_r10 = (uint32_t)((uint32_t)(local_r14));
    if (((uint32_t)(Arg1)) != ((uint32_t)(local_r14))) {
        Arg1 = (uint32_t)((Arg1) >> (9));
        Arg1 = (uint32_t)((Arg1) - ((uint32_t)((uint32_t)(v_stack_m64))));
        result = (uint8_t)(Arg1);
        local_r10 = (uint32_t)((uint32_t)(local_r14));
        if (((uint32_t)(result)) < ((uint32_t)((uint32_t)((uint32_t)(local_r14))))) { local_r10 = (uint32_t)(result); }
    }
    local_rdi = (uint16_t)((0) + (1));
    if (((uint16_t)(local_rdi)) < (*(uint16_t *)(v_rip + 0x9FED89))) goto loc_005C61C8;
    if (((uint32_t)(local_r10)) == ((uint32_t)(local_r14))) goto loc_005C6176;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) << (18));
    result = (v_stack_p10) & (0xFFFFFFFFFFFC0000ULL);
    Arg3 = (Arg3) + (result);
    Arg3 = (Arg3) + ((uint32_t)(*(uint32_t *)(v_rip + 0xA008F5)));
    goto loc_005C6176;
loc_005C62DE:
    local_rsi = (*(uint8_t *)(v_stack_p8 + 0xD0)) + (*(uint8_t *)(v_stack_p8 + 0xD0));
    v_stack_m50 = *(uint64_t *)(v_stack_p8 + 0xC8);
loc_005C62FD:
    local_rdi = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m64)))) << (9);
    Arg4 = (v_stack_p8) & (local_rdi);
    local_r12 = 0;
loc_005C631C:
    v_stack_m5C = 0;
    result = (*(uint64_t *)(v_rip + 0xA02281 + local_rsi * 8) - 1) - (Arg4);
    result = (result) + (1);
    if (result >= 1) goto loc_005C6335;
loc_005C632F:
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip + 0xA008F5))) | (-1);
    goto loc_005C6382;
loc_005C6335:
    result = (*(uint64_t *)(v_rip + 0xA02281 + local_rsi * 8) - 1) >> (6);
    result = (Arg4) >> (6);
loc_005C634B:
    result = ~(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA02281 + local_rsi * 8 + 0x8) + result * 8));
    if (result != -1) goto loc_005C6362;
    Arg1 = (*(uint64_t *)(v_rip + 0xA02281 + local_rsi * 8 + 0x8) + result * 8) + (8);
    if (Arg1 <= (*(uint64_t *)(v_rip + 0xA02281 + local_rsi * 8 + 0x8) + result * 8)) goto loc_005C634B;
    goto loc_005C632F;
loc_005C6362:
    Arg1 = (Arg1) - (*(uint64_t *)(v_rip + 0xA02281 + local_rsi * 8 + 0x8));
    result = ~(result);
    Arg1 = (Arg1) >> (3);
    Arg1 = (Arg1) << (6);
    Arg1 = (Arg1) + (result);
    if (Arg1 > (*(uint64_t *)(v_rip + 0xA02281 + local_rsi * 8) - 1)) goto loc_005C632F;
    if (Arg1 != -1) goto loc_005C639A;
loc_005C6382:
    if (Arg4 == 0) goto loc_005C639A;
    Arg2 = local_rdi + 1;
    if ((local_rdi + 1) > (*(uint64_t *)(v_rip + 0xA02281 + local_rsi * 8))) { Arg2 = *(uint64_t *)(v_rip + 0xA02281 + local_rsi * 8); }
    Arg2 = (Arg2) - (1);
    goto loc_005C631C;
loc_005C639A:
    local_r14 = (uint32_t)((*(uint64_t *)(v_rip + 0xA02281 + local_rsi * 8 + 0x8) + result * 8) | (0xFFFFFFFFULL));
    if (((uint32_t)(Arg1)) == ((uint32_t)(local_r14))) goto loc_005C6150;
    Arg1 = (uint32_t)((Arg1) >> (9));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) - ((uint32_t)((uint32_t)(v_stack_m64))));
    local_r10 = (uint32_t)((0) + ((uint32_t)((uint8_t)(result))));
    if (((uint32_t)(local_r10)) > 256) goto loc_005C6150;
    result = ((uint32_t)((uint32_t)(Arg1))) << (6);
    if (((*(uint64_t *)(result + *(uint64_t *)(v_rip + 0xA02281 + local_rsi * 8 + 0x8) * 1)) & (v_stack_m50)) != 0) goto loc_005C63E7;
    local_r10 = (uint32_t)((local_r10) + (1));
    goto loc_005C62FD;
loc_005C63E7:
    result = (v_stack_p10) & (0xFFFFFFFFFFFC0000ULL);
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) << (18));
    Arg3 = (Arg3) + (result);
    Arg3 = (Arg3) + ((uint32_t)(*(uint32_t *)(v_rip + 0xA007C3)));
    goto loc_005C615F;
loc_005C6410:
    *(uint64_t *)(local_rsi) = Arg3;
loc_005C6413:
    if (Arg3 != -1) {
        result = local_r10 + 1;
        Arg2 = (uint32_t)(v_stack_m68);
        if (((uint32_t)((uint32_t)(v_stack_m68))) >= ((uint32_t)(result))) { Arg2 = (uint32_t)(result); }
        v_stack_m68 = (uint32_t)(Arg2);
    }
    local_rbx = (uint32_t)(((uint8_t)(Arg1 + 1)) + (v_stack_m60));
    goto loc_005C5F76;
loc_005C642E:
loc_005C6431:
    local_rsp = (local_rsp) + (40);
    return *(uint64_t *)(v_rip + 0xA02281 + local_rsi * 8);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005C5EF8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
