# HvlpSelectVpSet

- RVA: `0x0058616C`–`0x005867C4` (길이 `1,624` bytes)
- VA: `0x000000014058616C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C659C`
- 디코드: `441`개 명령, `1,624/1,624` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **18**

### Outgoing calls
- `0x005861BC` → [HviGetImplementationLimits](../66/HviGetImplementationLimits_function_00666708.md) (function, `0x00666708`)
- `0x005861F1` → [HvlpComputeLpComparisonMetrics](HvlpComputeLpComparisonMetrics_function_005852E4.md) (function, `0x005852E4`)
- `0x005862F7` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00586392` → [HvlIsSingleGroupRequired](HvlIsSingleGroupRequired_function_00583BA4.md) (function, `0x00583BA4`)
- `0x0058648E` → [HvlIsSingleGroupRequired](HvlIsSingleGroupRequired_function_00583BA4.md) (function, `0x00583BA4`)
- `0x00586658` → [HvlpComputeLpComparisonMetrics](HvlpComputeLpComparisonMetrics_function_005852E4.md) (function, `0x005852E4`)
- `0x0058669E` → [HvlpLpComparison](HvlpLpComparison_function_00585AF8.md) (function, `0x00585AF8`)
- `0x005866F8` → [HvlpComputeLpComparisonMetrics](HvlpComputeLpComparisonMetrics_function_005852E4.md) (function, `0x005852E4`)
- `0x0058679D` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [HvlStartBootLogicalProcessors](HvlStartBootLogicalProcessors_function_00584E18.md) at `0x00585074`

### Static image references
- `0x0058618B` → RVA `0x00E0A740` (`.data`; read)
- `0x005861B2` → RVA `0x00FC6ABD` (`ALMOSTRO`; write)
- `0x005861C1` → RVA `0x00FC6A90` (`ALMOSTRO`; read)
- `0x005861CD` → RVA `0x00FC6AD8` (`ALMOSTRO`; read)
- `0x00586242` → RVA `0x00FCCC40` (`ALMOSTRO`; read)
- `0x00586249` → RVA `0x00FC7690` (`ALMOSTRO`; read)
- `0x00586259` → RVA `0x00FC6C90` (`ALMOSTRO`; read)
- `0x00586263` → RVA `0x00FC6C90` (`ALMOSTRO`; write)
- `0x00586271` → RVA `0x00FC6C8C` (`ALMOSTRO`; read)
- `0x0058627B` → RVA `0x00FC6C8C` (`ALMOSTRO`; write)
- `0x00586289` → RVA `0x00FC6BC0` (`ALMOSTRO`; read)
- `0x0058629C` → RVA `0x00FC6BC0` (`ALMOSTRO`; write)
- `0x005862A2` → RVA `0x00FC6B90` (`ALMOSTRO`; read)
- `0x005862CC` → RVA `0x00FC6B90` (`ALMOSTRO`; write)
- `0x00586303` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x005863C0` → RVA `0x00FC7690` (`ALMOSTRO`; write)
- `0x005863E8` → RVA `0x00FC6AA7` (`ALMOSTRO`; read)
- `0x005864B3` → RVA `0x00FC6AA7` (`ALMOSTRO`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0058616C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00586171  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
00586176  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0058617B  57                              push rdi
0058617C  41 54                           push r12
0058617E  41 55                           push r13
00586180  41 56                           push r14
00586182  41 57                           push r15
00586184  48 81 EC 90 00 00 00            sub rsp, 0x90
0058618B  48 8B 05 AE 45 88 00            mov rax, qword ptr [rip + 0x8845ae]
00586192  48 33 C4                        xor rax, rsp
00586195  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
0058619D  8B F9                           mov edi, ecx
0058619F  0F 57 C0                        xorps xmm0, xmm0
005861A2  45 33 ED                        xor r13d, r13d
005861A5  48 8D 4C 24 28                  lea rcx, [rsp + 0x28]
005861AA  0F 11 44 24 28                  movups xmmword ptr [rsp + 0x28], xmm0
005861AF  45 8A FD                        mov r15b, r13b
005861B2  44 88 2D 04 09 A4 00            mov byte ptr [rip + 0xa40904], r13b
005861B9  48 8B DA                        mov rbx, rdx
005861BC  E8 47 05 0E 00                  call 0x140666708
005861C1  F7 05 C5 08 A4 00 00 00 80 00   test dword ptr [rip + 0xa408c5], 0x800000
005861CB  74 3E                           je 0x14058620b
005861CD  F7 05 01 09 A4 00 00 08 00 00   test dword ptr [rip + 0xa40901], 0x800
005861D7  75 32                           jne 0x14058620b
005861D9  41 B7 01                        mov r15b, 1
005861DC  41 8B F5                        mov esi, r13d
005861DF  3B F7                           cmp esi, edi
005861E1  73 28                           jae 0x14058620b
005861E3  8B C6                           mov eax, esi
005861E5  44 8B C6                        mov r8d, esi
005861E8  48 8B D3                        mov rdx, rbx
005861EB  8B CF                           mov ecx, edi
005861ED  48 8D 2C 80                     lea rbp, [rax + rax*4]
005861F1  E8 EE F0 FF FF                  call 0x1405852e4
005861F6  44 38 6C EB 02                  cmp byte ptr [rbx + rbp*8 + 2], r13b
005861FB  74 07                           je 0x140586204
005861FD  44 39 6C EB 1C                  cmp dword ptr [rbx + rbp*8 + 0x1c], r13d
00586202  74 04                           je 0x140586208
00586204  FF C6                           inc esi
00586206  EB D7                           jmp 0x1405861df
00586208  45 8A FD                        mov r15b, r13b
0058620B  85 FF                           test edi, edi
0058620D  74 33                           je 0x140586242
0058620F  48 8D 4B 08                     lea rcx, [rbx + 8]
00586213  48 8B D7                        mov rdx, rdi
00586216  0F B7 01                        movzx eax, word ptr [rcx]
00586219  66 89 41 04                     mov word ptr [rcx + 4], ax
0058621D  41 8A C5                        mov al, r13b
00586220  66 C7 41 F8 01 00               mov word ptr [rcx - 8], 1
00586226  F7 05 A8 08 A4 00 00 08 00 00   test dword ptr [rip + 0xa408a8], 0x800
00586230  75 03                           jne 0x140586235
00586232  8A 41 FA                        mov al, byte ptr [rcx - 6]
00586235  88 41 FB                        mov byte ptr [rcx - 5], al
00586238  48 83 C1 28                     add rcx, 0x28
0058623C  48 83 EA 01                     sub rdx, 1
00586240  75 D4                           jne 0x140586216
00586242  4C 8D 05 F7 69 A4 00            lea r8, [rip + 0xa469f7]
00586249  48 8D 2D 40 14 A4 00            lea rbp, [rip + 0xa41440]
00586250  45 84 FF                        test r15b, r15b
00586253  0F 84 68 02 00 00               je 0x1405864c1
00586259  8B 05 31 0A A4 00               mov eax, dword ptr [rip + 0xa40a31]
0058625F  A8 01                           test al, 1
00586261  74 0E                           je 0x140586271
00586263  44 89 2D 26 0A A4 00            mov dword ptr [rip + 0xa40a26], r13d
0058626A  C6 05 4C 08 A4 00 01            mov byte ptr [rip + 0xa4084c], 1
00586271  8B 05 15 0A A4 00               mov eax, dword ptr [rip + 0xa40a15]
00586277  A8 01                           test al, 1
00586279  74 0E                           je 0x140586289
0058627B  44 89 2D 0A 0A A4 00            mov dword ptr [rip + 0xa40a0a], r13d
00586282  C6 05 34 08 A4 00 01            mov byte ptr [rip + 0xa40834], 1
00586289  8B 05 31 09 A4 00               mov eax, dword ptr [rip + 0xa40931]
0058628F  A8 01                           test al, 1
00586291  74 0F                           je 0x1405862a2
00586293  FF C0                           inc eax
00586295  C6 05 21 08 A4 00 01            mov byte ptr [rip + 0xa40821], 1
0058629C  89 05 1E 09 A4 00               mov dword ptr [rip + 0xa4091e], eax
005862A2  8B 35 E8 08 A4 00               mov esi, dword ptr [rip + 0xa408e8]
005862A8  85 F6                           test esi, esi
005862AA  74 2E                           je 0x1405862da
005862AC  0F B7 53 08                     movzx edx, word ptr [rbx + 8]
005862B0  41 8B C5                        mov eax, r13d
005862B3  48 8B CD                        mov rcx, rbp
005862B6  66 39 11                        cmp word ptr [rcx], dx
005862B9  74 0A                           je 0x1405862c5
005862BB  FF C0                           inc eax
005862BD  48 83 C1 02                     add rcx, 2
005862C1  3B C6                           cmp eax, esi
005862C3  72 F1                           jb 0x1405862b6
005862C5  3B C6                           cmp eax, esi
005862C7  75 11                           jne 0x1405862da
005862C9  41 8B F5                        mov esi, r13d
005862CC  44 89 2D BD 08 A4 00            mov dword ptr [rip + 0xa408bd], r13d
005862D3  C6 05 E3 07 A4 00 01            mov byte ptr [rip + 0xa407e3], 1
005862DA  44 39 2D DF 08 A4 00            cmp dword ptr [rip + 0xa408df], r13d
005862E1  41 BE 40 00 00 00               mov r14d, 0x40
005862E7  0F 84 FB 00 00 00               je 0x1405863e8
005862ED  45 8B C6                        mov r8d, r14d
005862F0  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
005862F5  33 D2                           xor edx, edx
005862F7  E8 44 09 14 00                  call 0x1406c6c40
005862FC  41 8B ED                        mov ebp, r13d
005862FF  85 F6                           test esi, esi
00586301  75 07                           jne 0x14058630a
00586303  0F B7 35 F6 EC A3 00            movzx esi, word ptr [rip + 0xa3ecf6]
0058630A  45 8B C5                        mov r8d, r13d
0058630D  85 F6                           test esi, esi
0058630F  74 5E                           je 0x14058636f
00586311  4C 8D 15 78 13 A4 00            lea r10, [rip + 0xa41378]
00586318  44 39 2D 71 08 A4 00            cmp dword ptr [rip + 0xa40871], r13d
0058631F  74 17                           je 0x140586338
00586321  41 0F B7 12                     movzx edx, word ptr [r10]
00586325  41 3B D6                        cmp edx, r14d
00586328  73 35                           jae 0x14058635f
0058632A  44 38 6C 14 40                  cmp byte ptr [rsp + rdx + 0x40], r13b
0058632F  75 2E                           jne 0x14058635f
00586331  C6 44 14 40 01                  mov byte ptr [rsp + rdx + 0x40], 1
00586336  EB 03                           jmp 0x14058633b
00586338  41 8B D0                        mov edx, r8d
0058633B  41 8B CD                        mov ecx, r13d
0058633E  3B CF                           cmp ecx, edi
00586340  73 1D                           jae 0x14058635f
00586342  8B C1                           mov eax, ecx
00586344  4C 8D 0C 80                     lea r9, [rax + rax*4]
00586348  46 38 6C CB 02                  cmp byte ptr [rbx + r9*8 + 2], r13b
0058634D  74 0A                           je 0x140586359
0058634F  42 0F B7 44 CB 08               movzx eax, word ptr [rbx + r9*8 + 8]
00586355  3B C2                           cmp eax, edx
00586357  74 04                           je 0x14058635d
00586359  FF C1                           inc ecx
0058635B  EB E1                           jmp 0x14058633e
0058635D  FF C5                           inc ebp
0058635F  41 FF C0                        inc r8d
00586362  49 83 C2 02                     add r10, 2
00586366  44 3B C6                        cmp r8d, esi
00586369  72 AD                           jb 0x140586318
0058636B  85 ED                           test ebp, ebp
0058636D  75 1B                           jne 0x14058638a
0058636F  44 39 2D 1A 08 A4 00            cmp dword ptr [rip + 0xa4081a], r13d
00586376  74 62                           je 0x1405863da
00586378  44 89 2D 11 08 A4 00            mov dword ptr [rip + 0xa40811], r13d
0058637F  C6 05 37 07 A4 00 01            mov byte ptr [rip + 0xa40737], 1
00586386  85 ED                           test ebp, ebp
00586388  74 50                           je 0x1405863da
0058638A  39 2D 30 08 A4 00               cmp dword ptr [rip + 0xa40830], ebp
00586390  77 48                           ja 0x1405863da
00586392  E8 0D D8 FF FF                  call 0x140583ba4
00586397  C6 05 1F 07 A4 00 01            mov byte ptr [rip + 0xa4071f], 1
0058639E  84 C0                           test al, al
005863A0  74 31                           je 0x1405863d3
005863A2  41 3B EE                        cmp ebp, r14d
005863A5  44 89 35 14 08 A4 00            mov dword ptr [rip + 0xa40814], r14d
005863AC  48 8D 2D DD 12 A4 00            lea rbp, [rip + 0xa412dd]
005863B3  4C 8D 05 86 68 A4 00            lea r8, [rip + 0xa46886]
005863BA  72 2C                           jb 0x1405863e8
005863BC  0F B7 43 08                     movzx eax, word ptr [rbx + 8]
005863C0  66 89 05 C9 12 A4 00            mov word ptr [rip + 0xa412c9], ax
005863C7  C7 05 BF 07 A4 00 01 00 00 00   mov dword ptr [rip + 0xa407bf], 1
005863D1  EB 15                           jmp 0x1405863e8
005863D3  44 89 2D E6 07 A4 00            mov dword ptr [rip + 0xa407e6], r13d
005863DA  4C 8D 05 5F 68 A4 00            lea r8, [rip + 0xa4685f]
005863E1  48 8D 2D A8 12 A4 00            lea rbp, [rip + 0xa412a8]
005863E8  44 38 2D B8 06 A4 00            cmp byte ptr [rip + 0xa406b8], r13b
005863EF  0F 84 CC 00 00 00               je 0x1405864c1
005863F5  0F B7 4B 08                     movzx ecx, word ptr [rbx + 8]
005863F9  48 03 C9                        add rcx, rcx
005863FC  49 8B 04 C8                     mov rax, qword ptr [r8 + rcx*8]
00586400  48 85 C0                        test rax, rax
00586403  0F 84 85 00 00 00               je 0x14058648e
00586409  49 8B 44 C8 08                  mov rax, qword ptr [r8 + rcx*8 + 8]
0058640E  48 0F BA 20 00                  bt qword ptr [rax], 0
00586413  0F 92 C0                        setb al
00586416  84 C0                           test al, al
00586418  74 74                           je 0x14058648e
0058641A  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00586423  48 8D 35 16 68 A4 00            lea rsi, [rip + 0xa46816]
0058642A  44 8B 5B 04                     mov r11d, dword ptr [rbx + 4]
0058642E  41 B8 01 00 00 00               mov r8d, 1
00586434  8B 90 A4 00 00 00               mov edx, dword ptr [rax + 0xa4]
0058643A  FF CA                           dec edx
0058643C  F7 D2                           not edx
0058643E  44 23 DA                        and r11d, edx
00586441  44 3B C7                        cmp r8d, edi
00586444  73 7B                           jae 0x1405864c1
00586446  41 8B C0                        mov eax, r8d
00586449  48 8D 0C 80                     lea rcx, [rax + rax*4]
0058644D  8B 44 CB 04                     mov eax, dword ptr [rbx + rcx*8 + 4]
00586451  23 C2                           and eax, edx
00586453  41 3B C3                        cmp eax, r11d
00586456  75 31                           jne 0x140586489
00586458  44 0F B7 4B 08                  movzx r9d, word ptr [rbx + 8]
0058645D  44 8B 54 CB 24                  mov r10d, dword ptr [rbx + rcx*8 + 0x24]
00586462  4D 03 C9                        add r9, r9
00586465  4A 8B 04 CE                     mov rax, qword ptr [rsi + r9*8]
00586469  4C 3B D0                        cmp r10, rax
0058646C  73 20                           jae 0x14058648e
0058646E  4A 8B 44 CE 08                  mov rax, qword ptr [rsi + r9*8 + 8]
00586473  41 8B CA                        mov ecx, r10d
00586476  49 C1 EA 06                     shr r10, 6
0058647A  83 E1 3F                        and ecx, 0x3f
0058647D  4A 0F A3 0C D0                  bt qword ptr [rax + r10*8], rcx
00586482  0F 92 C0                        setb al
00586485  84 C0                           test al, al
00586487  74 05                           je 0x14058648e
00586489  41 FF C0                        inc r8d
0058648C  EB B3                           jmp 0x140586441
0058648E  E8 11 D7 FF FF                  call 0x140583ba4
00586493  84 C0                           test al, al
00586495  74 1C                           je 0x1405864b3
00586497  0F B7 43 08                     movzx eax, word ptr [rbx + 8]
0058649B  66 89 05 EE 11 A4 00            mov word ptr [rip + 0xa411ee], ax
005864A2  44 89 35 17 07 A4 00            mov dword ptr [rip + 0xa40717], r14d
005864A9  C7 05 DD 06 A4 00 01 00 00 00   mov dword ptr [rip + 0xa406dd], 1
005864B3  44 88 2D ED 05 A4 00            mov byte ptr [rip + 0xa405ed], r13b
005864BA  C6 05 FC 05 A4 00 01            mov byte ptr [rip + 0xa405fc], 1
005864C1  C6 43 01 01                     mov byte ptr [rbx + 1], 1
005864C5  4C 8D 25 74 67 A4 00            lea r12, [rip + 0xa46774]
005864CC  C6 43 03 01                     mov byte ptr [rbx + 3], 1
005864D0  41 BE 01 00 00 00               mov r14d, 1
005864D6  85 FF                           test edi, edi
005864D8  0F 84 57 01 00 00               je 0x140586635
005864DE  48 8B D3                        mov rdx, rbx
005864E1  48 8B F7                        mov rsi, rdi
005864E4  44 38 2A                        cmp byte ptr [rdx], r13b
005864E7  0F 84 23 01 00 00               je 0x140586610
005864ED  44 38 6A 01                     cmp byte ptr [rdx + 1], r13b
005864F1  0F 85 16 01 00 00               jne 0x14058660d
005864F7  44 38 6A 02                     cmp byte ptr [rdx + 2], r13b
005864FB  0F 84 0C 01 00 00               je 0x14058660d
00586501  44 3B 74 24 28                  cmp r14d, dword ptr [rsp + 0x28]
00586506  0F 84 01 01 00 00               je 0x14058660d
0058650C  44 39 2D 7D 07 A4 00            cmp dword ptr [rip + 0xa4077d], r13d
00586513  74 33                           je 0x140586548
00586515  45 8B C5                        mov r8d, r13d
00586518  48 8D 4B 08                     lea rcx, [rbx + 8]
0058651C  4C 8B CF                        mov r9, rdi
0058651F  44 38 69 F9                     cmp byte ptr [rcx - 7], r13b
00586523  74 0C                           je 0x140586531
00586525  0F B7 42 08                     movzx eax, word ptr [rdx + 8]
00586529  66 39 01                        cmp word ptr [rcx], ax
0058652C  75 03                           jne 0x140586531
0058652E  41 FF C0                        inc r8d
00586531  48 83 C1 28                     add rcx, 0x28
00586535  49 83 E9 01                     sub r9, 1
00586539  75 E4                           jne 0x14058651f
0058653B  44 3B 05 4E 07 A4 00            cmp r8d, dword ptr [rip + 0xa4074e]
00586542  0F 84 C5 00 00 00               je 0x14058660d
00586548  44 39 2D 3D 07 A4 00            cmp dword ptr [rip + 0xa4073d], r13d
0058654F  74 4D                           je 0x14058659e
00586551  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0058655A  48 8D 4B 04                     lea rcx, [rbx + 4]
0058655E  44 8B 52 04                     mov r10d, dword ptr [rdx + 4]
00586562  45 8B CD                        mov r9d, r13d
00586565  4C 8B DF                        mov r11, rdi
00586568  44 8B 80 A4 00 00 00            mov r8d, dword ptr [rax + 0xa4]
0058656F  41 FF C8                        dec r8d
00586572  41 F7 D0                        not r8d
00586575  45 23 D0                        and r10d, r8d
00586578  44 38 69 FD                     cmp byte ptr [rcx - 3], r13b
0058657C  74 0D                           je 0x14058658b
0058657E  8B 01                           mov eax, dword ptr [rcx]
00586580  41 23 C0                        and eax, r8d
00586583  41 3B C2                        cmp eax, r10d
00586586  75 03                           jne 0x14058658b
00586588  41 FF C1                        inc r9d
0058658B  48 83 C1 28                     add rcx, 0x28
0058658F  49 83 EB 01                     sub r11, 1
00586593  75 E3                           jne 0x140586578
00586595  44 3B 0D F0 06 A4 00            cmp r9d, dword ptr [rip + 0xa406f0]
0058659C  74 6F                           je 0x14058660d
0058659E  44 8B 0D EB 05 A4 00            mov r9d, dword ptr [rip + 0xa405eb]
005865A5  45 85 C9                        test r9d, r9d
005865A8  74 1B                           je 0x1405865c5
005865AA  45 8B C5                        mov r8d, r13d
005865AD  45 3B C1                        cmp r8d, r9d
005865B0  73 5B                           jae 0x14058660d
005865B2  0F B7 42 0C                     movzx eax, word ptr [rdx + 0xc]
005865B6  41 8B C8                        mov ecx, r8d
005865B9  66 39 44 4D 00                  cmp word ptr [rbp + rcx*2], ax
005865BE  74 05                           je 0x1405865c5
005865C0  41 FF C0                        inc r8d
005865C3  EB E8                           jmp 0x1405865ad
005865C5  8B 05 F5 05 A4 00               mov eax, dword ptr [rip + 0xa405f5]
005865CB  85 C0                           test eax, eax
005865CD  74 05                           je 0x1405865d4
005865CF  44 3B F0                        cmp r14d, eax
005865D2  74 39                           je 0x14058660d
005865D4  44 38 2D CC 04 A4 00            cmp byte ptr [rip + 0xa404cc], r13b
005865DB  74 33                           je 0x140586610
005865DD  44 0F B7 42 08                  movzx r8d, word ptr [rdx + 8]
005865E2  44 8B 4A 24                     mov r9d, dword ptr [rdx + 0x24]
005865E6  4D 03 C0                        add r8, r8
005865E9  4B 8B 04 C4                     mov rax, qword ptr [r12 + r8*8]
005865ED  4C 3B C8                        cmp r9, rax
005865F0  73 1B                           jae 0x14058660d
005865F2  4B 8B 44 C4 08                  mov rax, qword ptr [r12 + r8*8 + 8]
005865F7  41 8B C9                        mov ecx, r9d
005865FA  49 C1 E9 06                     shr r9, 6
005865FE  83 E1 3F                        and ecx, 0x3f
00586601  4A 0F A3 0C C8                  bt qword ptr [rax + r9*8], rcx
00586606  0F 92 C0                        setb al
00586609  84 C0                           test al, al
0058660B  75 03                           jne 0x140586610
0058660D  44 88 2A                        mov byte ptr [rdx], r13b
00586610  48 83 C2 28                     add rdx, 0x28
00586614  48 83 EE 01                     sub rsi, 1
00586618  0F 85 C6 FE FF FF               jne 0x1405864e4
0058661E  41 8B C5                        mov eax, r13d
00586621  48 8B CB                        mov rcx, rbx
00586624  44 38 29                        cmp byte ptr [rcx], r13b
00586627  75 0F                           jne 0x140586638
00586629  FF C0                           inc eax
0058662B  48 83 C1 28                     add rcx, 0x28
0058662F  3B C7                           cmp eax, edi
00586631  72 F1                           jb 0x140586624
00586633  EB 03                           jmp 0x140586638
00586635  41 8B C5                        mov eax, r13d
00586638  3B C7                           cmp eax, edi
0058663A  0F 84 96 00 00 00               je 0x1405866d6
00586640  41 8B F5                        mov esi, r13d
00586643  85 FF                           test edi, edi
00586645  74 20                           je 0x140586667
00586647  48 8B EB                        mov rbp, rbx
0058664A  44 38 6D 00                     cmp byte ptr [rbp], r13b
0058664E  74 0D                           je 0x14058665d
00586650  44 8B C6                        mov r8d, esi
00586653  48 8B D3                        mov rdx, rbx
00586656  8B CF                           mov ecx, edi
00586658  E8 87 EC FF FF                  call 0x1405852e4
0058665D  FF C6                           inc esi
0058665F  48 83 C5 28                     add rbp, 0x28
00586663  3B F7                           cmp esi, edi
00586665  72 E3                           jb 0x14058664a
00586667  41 83 C9 FF                     or r9d, 0xffffffff
0058666B  41 8B D5                        mov edx, r13d
0058666E  3B D7                           cmp edx, edi
00586670  73 13                           jae 0x140586685
00586672  8B C2                           mov eax, edx
00586674  48 8D 0C 80                     lea rcx, [rax + rax*4]
00586678  44 38 2C CB                     cmp byte ptr [rbx + rcx*8], r13b
0058667C  75 04                           jne 0x140586682
0058667E  FF C2                           inc edx
00586680  EB EC                           jmp 0x14058666e
00586682  44 8B CA                        mov r9d, edx
00586685  45 8D 41 01                     lea r8d, [r9 + 1]
00586689  44 3B C7                        cmp r8d, edi
0058668C  73 28                           jae 0x1405866b6
0058668E  4B 8D 0C 80                     lea rcx, [r8 + r8*4]
00586692  48 8D 34 CB                     lea rsi, [rbx + rcx*8]
00586696  44 38 2E                        cmp byte ptr [rsi], r13b
00586699  74 0F                           je 0x1405866aa
0058669B  48 8B D3                        mov rdx, rbx
0058669E  E8 55 F4 FF FF                  call 0x140585af8
005866A3  83 F8 FF                        cmp eax, -1
005866A6  45 0F 44 C8                     cmove r9d, r8d
005866AA  41 FF C0                        inc r8d
005866AD  48 83 C6 28                     add rsi, 0x28
005866B1  44 3B C7                        cmp r8d, edi
005866B4  72 E0                           jb 0x140586696
005866B6  41 8B C1                        mov eax, r9d
005866B9  48 8D 2D D0 0F A4 00            lea rbp, [rip + 0xa40fd0]
005866C0  41 FF C6                        inc r14d
005866C3  48 8D 0C 80                     lea rcx, [rax + rax*4]
005866C7  C6 44 CB 01 01                  mov byte ptr [rbx + rcx*8 + 1], 1
005866CC  C6 44 CB 03 01                  mov byte ptr [rbx + rcx*8 + 3], 1
005866D1  E9 00 FE FF FF                  jmp 0x1405864d6
005866D6  45 8A E5                        mov r12b, r13b
005866D9  45 84 FF                        test r15b, r15b
005866DC  74 51                           je 0x14058672f
005866DE  BD 01 00 00 00                  mov ebp, 1
005866E3  3B FD                           cmp edi, ebp
005866E5  76 48                           jbe 0x14058672f
005866E7  48 8D 73 29                     lea rsi, [rbx + 0x29]
005866EB  44 38 2E                        cmp byte ptr [rsi], r13b
005866EE  74 35                           je 0x140586725
005866F0  44 8B C5                        mov r8d, ebp
005866F3  48 8B D3                        mov rdx, rbx
005866F6  8B CF                           mov ecx, edi
005866F8  E8 E7 EB FF FF                  call 0x1405852e4
005866FD  44 39 6E 1B                     cmp dword ptr [rsi + 0x1b], r13d
00586701  75 22                           jne 0x140586725
00586703  44 88 2E                        mov byte ptr [rsi], r13b
00586706  41 8A C5                        mov al, r13b
00586709  F7 05 C5 03 A4 00 00 08 00 00   test dword ptr [rip + 0xa403c5], 0x800
00586713  75 03                           jne 0x140586718
00586715  8A 46 01                        mov al, byte ptr [rsi + 1]
00586718  88 46 02                        mov byte ptr [rsi + 2], al
0058671B  41 B4 01                        mov r12b, 1
0058671E  C6 05 98 03 A4 00 01            mov byte ptr [rip + 0xa40398], 1
00586725  FF C5                           inc ebp
00586727  48 83 C6 28                     add rsi, 0x28
0058672B  3B EF                           cmp ebp, edi
0058672D  72 BC                           jb 0x1405866eb
0058672F  44 39 2D 5A 04 A4 00            cmp dword ptr [rip + 0xa4045a], r13d
00586736  75 58                           jne 0x140586790
00586738  44 38 2D 68 03 A4 00            cmp byte ptr [rip + 0xa40368], r13b
0058673F  75 4F                           jne 0x140586790
00586741  45 84 E4                        test r12b, r12b
00586744  75 4A                           jne 0x140586790
00586746  41 8B CD                        mov ecx, r13d
00586749  3B CF                           cmp ecx, edi
0058674B  73 43                           jae 0x140586790
0058674D  8B C1                           mov eax, ecx
0058674F  4C 8D 04 80                     lea r8, [rax + rax*4]
00586753  46 38 6C C3 02                  cmp byte ptr [rbx + r8*8 + 2], r13b
00586758  74 2B                           je 0x140586785
0058675A  41 8B D5                        mov edx, r13d
0058675D  85 FF                           test edi, edi
0058675F  74 20                           je 0x140586781
00586761  46 0F B7 4C C3 08               movzx r9d, word ptr [rbx + r8*8 + 8]
00586767  48 8D 43 01                     lea rax, [rbx + 1]
0058676B  66 44 39 48 07                  cmp word ptr [rax + 7], r9w
00586770  75 05                           jne 0x140586777
00586772  44 38 28                        cmp byte ptr [rax], r13b
00586775  75 0A                           jne 0x140586781
00586777  FF C2                           inc edx
00586779  48 83 C0 28                     add rax, 0x28
0058677D  3B D7                           cmp edx, edi
0058677F  72 EA                           jb 0x14058676b
00586781  3B D7                           cmp edx, edi
00586783  74 04                           je 0x140586789
00586785  FF C1                           inc ecx
00586787  EB C0                           jmp 0x140586749
00586789  B8 01 00 00 C0                  mov eax, 0xc0000001
0058678E  EB 02                           jmp 0x140586792
00586790  33 C0                           xor eax, eax
00586792  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
0058679A  48 33 CC                        xor rcx, rsp
0058679D  E8 9E 5E 12 00                  call 0x1406ac640
005867A2  4C 8D 9C 24 90 00 00 00         lea r11, [rsp + 0x90]
005867AA  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
005867AE  49 8B 6B 40                     mov rbp, qword ptr [r11 + 0x40]
005867B2  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
005867B6  49 8B E3                        mov rsp, r11
005867B9  41 5F                           pop r15
005867BB  41 5E                           pop r14
005867BD  41 5D                           pop r13
005867BF  41 5C                           pop r12
005867C1  5F                              pop rdi
005867C2  C3                              ret
005867C3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvlpSelectVpSet(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (144);
    result = (*(unsigned __int64 *)(v_rip + 8930734)) ^ (v_rsp);
    v_stack_m38 = result;
    v_r13 = 0;
    v_stack_m90 = v_xmm0;
    *(unsigned __int8 *)(v_rip + 10750212) = 0;
    result = HviGetImplementationLimits(v_stack_m90, a2, a3, a4);
    if (((*(unsigned int *)(v_rip + 10750149)) & (0x800000ULL)) == 0) goto loc_0058620B;
    if (((*(unsigned int *)(v_rip + 10750209)) & (0x800ULL)) != 0) goto loc_0058620B;
loc_005861DF:
    if (0 >= ((unsigned int)((unsigned int)(a1)))) goto loc_0058620B;
    result = HvlpComputeLpComparisonMetrics((unsigned int)((unsigned int)((unsigned int)(a1))), a2, 0, a4);
    if ((*(unsigned __int8 *)(a2 + 0 + 0 * 4 * 8 + 2)) == 0) goto loc_00586204;
    if ((*(unsigned int *)(a2 + 0 + 0 * 4 * 8 + 28)) == 0) goto loc_00586208;
loc_00586204:
    v_rsi = (unsigned int)((0) + 1);
    goto loc_005861DF;
loc_00586208:
loc_0058620B:
    if ((unsigned int)((unsigned int)(a1)) == 0) goto loc_00586242;
loc_00586216:
    *(unsigned __int16 *)(a2 + 8 + 4) = (unsigned __int16)(*(unsigned __int16 *)(a2 + 8));
    *(unsigned __int16 *)(a2 + 8 - 8) = 1;
    result = 0;
    if (((*(unsigned int *)(v_rip + 10750120)) & (0x800ULL)) == 0) {
        result = *(unsigned __int8 *)(a2 + 8 - 6);
    }
    *(unsigned __int8 *)(a2 + 8 - 5) = (unsigned __int8)(result);
    a1 = (a2 + 8) + (40);
    a2 = ((unsigned int)(a1)) - (1);
    if (condition_is_not_equal) goto loc_00586216;
loc_00586242:
    if (0 == 0) goto loc_005864C1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10750513)))) & (1)) != 0) {
        *(unsigned int *)(v_rip + 10750502) = 0;
        *(unsigned __int8 *)(v_rip + 10750028) = 1;
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10750485)))) & (1)) != 0) {
        *(unsigned int *)(v_rip + 10750474) = 0;
        *(unsigned __int8 *)(v_rip + 10750004) = 1;
    }
    result = (unsigned int)(*(unsigned int *)(v_rip + 10750257));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10750257)))) & (1)) != 0) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10750257))) + 1);
        *(unsigned __int8 *)(v_rip + 10749985) = 1;
        *(unsigned int *)(v_rip + 10750238) = (unsigned int)(result);
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10750184))) == 0) goto loc_005862DA;
loc_005862B6:
    if ((*(unsigned __int16 *)(v_rip + 10753088)) == ((unsigned __int16)(*(unsigned __int16 *)(a2 + 8)))) goto loc_005862C5;
    result = (unsigned int)((0) + 1);
    a1 = (v_rip + 10753088) + (2);
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10750184))))) goto loc_005862B6;
loc_005862C5:
    v_rsi = (unsigned int)(*(unsigned int *)(v_rip + 10750184));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10750184))))) {
        v_rsi = 0;
        *(unsigned int *)(v_rip + 10750141) = 0;
        *(unsigned __int8 *)(v_rip + 10749923) = 1;
    }
    if ((*(unsigned int *)(v_rip + 10750175)) == 0) goto loc_005863E8;
    a2 = 0;
    result = memset(v_stack_m78, a2, 64, a4);
    if ((unsigned int)(v_rsi) == 0) {
        v_rsi = *(unsigned __int16 *)(v_rip + 10743030);
    }
    if ((unsigned int)(v_rsi) == 0) goto loc_0058636F;
loc_00586318:
    if ((*(unsigned int *)(v_rip + 10750065)) == 0) goto loc_00586338;
    if (((unsigned int)(*(unsigned __int16 *)(v_rip + 10752888))) >= 64) goto loc_0058635F;
    if ((*(unsigned __int8 *)(v_rsp + *(unsigned __int16 *)(v_rip + 10752888) * 1 + 64)) != 0) goto loc_0058635F;
    *(unsigned __int8 *)(v_rsp + *(unsigned __int16 *)(v_rip + 10752888) * 1 + 64) = 1;
    goto loc_0058633B;
loc_00586338:
loc_0058633B:
loc_0058633E:
    if (0 >= ((unsigned int)((unsigned int)(a1)))) goto loc_0058635F;
    if ((*(unsigned __int8 *)(a2 + 0 + 0 * 4 * 8 + 2)) == 0) goto loc_00586359;
    if (((unsigned int)(*(unsigned __int16 *)(a2 + 0 + 0 * 4 * 8 + 8))) == 0) goto loc_0058635D;
loc_00586359:
    a1 = (unsigned int)((0) + 1);
    goto loc_0058633E;
loc_0058635D:
    v_rbp = (unsigned int)((0) + 1);
loc_0058635F:
    a3 = (unsigned int)((0) + 1);
    v_r10 = (v_rip + 10752888) + (2);
    if (((unsigned int)(a3)) < ((unsigned int)(v_rsi))) goto loc_00586318;
    if ((unsigned int)(v_rbp) != 0) goto loc_0058638A;
loc_0058636F:
    if ((*(unsigned int *)(v_rip + 10749978)) == 0) goto loc_005863DA;
    *(unsigned int *)(v_rip + 10749969) = 0;
    *(unsigned __int8 *)(v_rip + 10749751) = 1;
    if ((unsigned int)(v_rbp) == 0) goto loc_005863DA;
loc_0058638A:
    if ((*(unsigned int *)(v_rip + 10750000)) > ((unsigned int)(v_rbp))) goto loc_005863DA;
    result = HvlIsSingleGroupRequired(a1, 0, a3, 0 + 0 * 4);
    *(unsigned __int8 *)(v_rip + 10749727) = 1;
    if ((unsigned __int8)(result) == 0) goto loc_005863D3;
    *(unsigned int *)(v_rip + 10749972) = 64;
    if (((unsigned int)(v_rbp)) < 64) goto loc_005863E8;
    *(unsigned __int16 *)(v_rip + 10752713) = (unsigned __int16)(*(unsigned __int16 *)(a2 + 8));
    *(unsigned int *)(v_rip + 10749887) = 1;
    goto loc_005863E8;
loc_005863D3:
    *(unsigned int *)(v_rip + 10749926) = 0;
loc_005863DA:
loc_005863E8:
    if ((*(unsigned __int8 *)(v_rip + 10749624)) == 0) goto loc_005864C1;
    a1 = (*(unsigned __int16 *)(a2 + 8)) + (*(unsigned __int16 *)(a2 + 8));
    if (*(unsigned __int64 *)(v_rip + 10774623 + a1 * 8) == 0) goto loc_0058648E;
    result = (condition_is_below) ? 1 : 0;
    if ((unsigned __int8)(result) == 0) goto loc_0058648E;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 164))) - 1);
    a2 = (unsigned int)(~(a2));
    v_r11 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 4))) & ((unsigned int)(a2)));
loc_00586441:
    if (1 >= ((unsigned int)((unsigned int)(a1)))) goto loc_005864C1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 1 + 1 * 4 * 8 + 4))) & ((unsigned int)(a2)));
    if (((unsigned int)(result)) != ((unsigned int)(v_r11))) goto loc_00586489;
    a4 = (*(unsigned __int16 *)(a2 + 8)) + (*(unsigned __int16 *)(a2 + 8));
    if (((unsigned int)(*(unsigned int *)(a2 + 1 + 1 * 4 * 8 + 36))) >= (*(unsigned __int64 *)(v_rip + 10774550 + a4 * 8))) goto loc_0058648E;
    v_r10 = ((unsigned int)(*(unsigned int *)(a2 + 1 + 1 * 4 * 8 + 36))) >> (6);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 1 + 1 * 4 * 8 + 36))))) & (63));
    result = (condition_is_below) ? 1 : 0;
    if ((unsigned __int8)(result) == 0) goto loc_0058648E;
loc_00586489:
    a3 = (unsigned int)((1) + 1);
    goto loc_00586441;
loc_0058648E:
    result = HvlIsSingleGroupRequired(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned __int16 *)(a2 + 8);
        *(unsigned __int16 *)(v_rip + 10752494) = (unsigned __int16)(result);
        *(unsigned int *)(v_rip + 10749719) = 64;
        *(unsigned int *)(v_rip + 10749661) = 1;
    }
    *(unsigned __int8 *)(v_rip + 10749421) = 0;
    *(unsigned __int8 *)(v_rip + 10749436) = 1;
loc_005864C1:
    *(unsigned __int8 *)(a2 + 1) = 1;
    *(unsigned __int8 *)(a2 + 3) = 1;
loc_005864D6:
    if ((unsigned int)((unsigned int)(a1)) == 0) goto loc_00586635;
loc_005864E4:
    if ((*(unsigned __int8 *)(a2)) == 0) goto loc_00586610;
    if ((*(unsigned __int8 *)(a2 + 1)) != 0) goto loc_0058660D;
    if ((*(unsigned __int8 *)(a2 + 2)) == 0) goto loc_0058660D;
    if (1 == v_stack_m90) goto loc_0058660D;
    if ((*(unsigned int *)(v_rip + 10749821)) == 0) goto loc_00586548;
loc_0058651F:
    if ((*(unsigned __int8 *)(a2 + 8 - 7)) == 0) goto loc_00586531;
    if ((*(unsigned __int16 *)(a2 + 8)) == ((unsigned __int16)(*(unsigned __int16 *)(a2 + 8)))) {
        a3 = (unsigned int)((0) + 1);
    }
    a1 = (a2 + 8) + (40);
    a4 = ((unsigned int)(a1)) - (1);
    if (condition_is_not_equal) goto loc_0058651F;
    if (((unsigned int)(a3)) == (*(unsigned int *)(v_rip + 10749774))) goto loc_0058660D;
loc_00586548:
    if ((*(unsigned int *)(v_rip + 10749757)) == 0) goto loc_0058659E;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 164))) - 1);
    a3 = (unsigned int)(~(a3));
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 4))) & ((unsigned int)(a3)));
loc_00586578:
    if ((*(unsigned __int8 *)(a2 + 4 - 3)) == 0) goto loc_0058658B;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 4))) & ((unsigned int)(a3)));
    if (((unsigned int)(result)) == ((unsigned int)(v_r10))) {
        a4 = (unsigned int)((0) + 1);
    }
    a1 = (a2 + 4) + (40);
    v_r11 = ((unsigned int)(a1)) - (1);
    if (condition_is_not_equal) goto loc_00586578;
    if (((unsigned int)(a4)) == (*(unsigned int *)(v_rip + 10749680))) goto loc_0058660D;
loc_0058659E:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10749419))) == 0) goto loc_005865C5;
loc_005865AD:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10749419))))) goto loc_0058660D;
    if ((*(unsigned __int16 *)(v_rip + 10752680 + 0 * 2)) == ((unsigned __int16)(*(unsigned __int16 *)(a2 + 12)))) goto loc_005865C5;
    a3 = (unsigned int)((0) + 1);
    goto loc_005865AD;
loc_005865C5:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10749429))) == 0) goto loc_005865D4;
    if (1 == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10749429))))) goto loc_0058660D;
loc_005865D4:
    if ((*(unsigned __int8 *)(v_rip + 10749132)) == 0) goto loc_00586610;
    a3 = (*(unsigned __int16 *)(a2 + 8)) + (*(unsigned __int16 *)(a2 + 8));
    if (((unsigned int)(*(unsigned int *)(a2 + 36))) >= (*(unsigned __int64 *)(v_rip + 10774388 + a3 * 8))) goto loc_0058660D;
    a4 = ((unsigned int)(*(unsigned int *)(a2 + 36))) >> (6);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 36))))) & (63));
    result = (condition_is_below) ? 1 : 0;
    if ((unsigned __int8)(result) == 0) {
        *(unsigned __int8 *)(a2) = 0;
    }
    a2 = (a2) + (40);
    v_rsi = ((unsigned int)(a1)) - (1);
    if (condition_is_not_equal) goto loc_005864E4;
loc_00586624:
    if ((*(unsigned __int8 *)(a2)) != 0) goto loc_00586638;
    result = (unsigned int)((0) + 1);
    a1 = (a2) + (40);
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(a1)))) goto loc_00586624;
    goto loc_00586638;
loc_00586635:
loc_00586638:
    if (0 == ((unsigned int)((unsigned int)(a1)))) goto loc_005866D6;
    if ((unsigned int)((unsigned int)(a1)) == 0) goto loc_00586667;
loc_0058664A:
    result = 0;
    if ((*(unsigned __int8 *)(a2)) != 0) {
        a3 = 0;
        a2 = a2;
        a1 = (unsigned int)((unsigned int)(a1));
        result = HvlpComputeLpComparisonMetrics(a1, a2, a3, a4);
    }
    v_rsi = (unsigned int)((0) + 1);
    v_rbp = (a2) + (40);
    if (((unsigned int)(v_rsi)) < ((unsigned int)((unsigned int)(a1)))) goto loc_0058664A;
loc_00586667:
    a4 = (unsigned int)((a4) | (0xFFFFFFFFULL));
loc_0058666E:
    if (0 >= ((unsigned int)((unsigned int)(a1)))) goto loc_00586685;
    if ((*(unsigned __int8 *)(a2 + 0 + 0 * 4 * 8)) != 0) goto loc_00586682;
    a2 = (unsigned int)((0) + 1);
    goto loc_0058666E;
loc_00586682:
loc_00586685:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)) + 1)) >= ((unsigned int)((unsigned int)(a1)))) goto loc_005866B6;
loc_00586696:
    result = 0;
    if ((*(unsigned __int8 *)(a2 + (unsigned int)((unsigned int)(a2)) + 1 + (unsigned int)((unsigned int)(a2)) + 1 * 4 * 8)) != 0) {
        a2 = a2;
        result = HvlpLpComparison((unsigned int)((unsigned int)(a2)) + 1 + (unsigned int)((unsigned int)(a2)) + 1 * 4, a2, (unsigned int)((unsigned int)(a2)) + 1, (unsigned int)((unsigned int)(a2)));
        a4 = (unsigned int)((unsigned int)(a2));
        if (((unsigned int)(result)) == -1) { a4 = (unsigned int)((unsigned int)((unsigned int)(a2)) + 1); }
    }
    a3 = (unsigned int)(((unsigned int)((unsigned int)(a2)) + 1) + 1);
    v_rsi = (a2 + (unsigned int)((unsigned int)(a2)) + 1 + (unsigned int)((unsigned int)(a2)) + 1 * 4 * 8) + (40);
    if (((unsigned int)(a3)) < ((unsigned int)((unsigned int)(a1)))) goto loc_00586696;
loc_005866B6:
    v_r14 = (unsigned int)((1) + 1);
    *(unsigned __int8 *)(a2 + (unsigned int)((unsigned int)(a4)) + (unsigned int)((unsigned int)(a4)) * 4 * 8 + 1) = 1;
    *(unsigned __int8 *)(a2 + (unsigned int)((unsigned int)(a4)) + (unsigned int)((unsigned int)(a4)) * 4 * 8 + 3) = 1;
    goto loc_005864D6;
loc_005866D6:
    if (0 == 0) goto loc_0058672F;
    if (((unsigned int)((unsigned int)(a1))) <= 1) goto loc_0058672F;
loc_005866EB:
    if ((*(unsigned __int8 *)(a2 + 41)) == 0) goto loc_00586725;
    result = HvlpComputeLpComparisonMetrics((unsigned int)((unsigned int)((unsigned int)(a1))), a2, 1, a4);
    if ((*(unsigned int *)(a2 + 41 + 27)) != 0) goto loc_00586725;
    *(unsigned __int8 *)(a2 + 41) = 0;
    result = 0;
    if (((*(unsigned int *)(v_rip + 10748869)) & (0x800ULL)) == 0) {
        result = *(unsigned __int8 *)(a2 + 41 + 1);
    }
    *(unsigned __int8 *)(a2 + 41 + 2) = (unsigned __int8)(result);
    *(unsigned __int8 *)(v_rip + 10748824) = 1;
loc_00586725:
    v_rbp = (unsigned int)((1) + 1);
    v_rsi = (a2 + 41) + (40);
    if (((unsigned int)(v_rbp)) < ((unsigned int)((unsigned int)(a1)))) goto loc_005866EB;
loc_0058672F:
    if ((*(unsigned int *)(v_rip + 10749018)) != 0) goto loc_00586790;
    if ((*(unsigned __int8 *)(v_rip + 10748776)) != 0) goto loc_00586790;
    if (1 != 0) goto loc_00586790;
loc_00586749:
    if (0 >= ((unsigned int)((unsigned int)(a1)))) goto loc_00586790;
    if ((*(unsigned __int8 *)(a2 + 0 + 0 * 4 * 8 + 2)) == 0) goto loc_00586785;
    if ((unsigned int)((unsigned int)(a1)) == 0) goto loc_00586781;
loc_0058676B:
    if ((*(unsigned __int16 *)(a2 + 1 + 7)) != ((unsigned __int16)(*(unsigned __int16 *)(a2 + 0 + 0 * 4 * 8 + 8)))) goto loc_00586777;
    if ((*(unsigned __int8 *)(a2 + 1)) != 0) goto loc_00586781;
loc_00586777:
    a2 = (unsigned int)((0) + 1);
    result = (a2 + 1) + (40);
    if (((unsigned int)(a2)) < ((unsigned int)((unsigned int)(a1)))) goto loc_0058676B;
loc_00586781:
    if (((unsigned int)(a2)) == ((unsigned int)((unsigned int)(a1)))) goto loc_00586789;
loc_00586785:
    a1 = (unsigned int)((0) + 1);
    goto loc_00586749;
loc_00586789:
    goto loc_00586792;
loc_00586790:
    result = 0;
loc_00586792:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, 0 + 0 * 4, *(unsigned __int16 *)(a2 + 0 + 0 * 4 * 8 + 8));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HvlpSelectVpSet(int32_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m78;
    uint64_t v_stack_m90;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (144);
    result = (*(uint64_t *)(v_rip + 0x8845AE)) ^ (local_rsp);
    v_stack_m38 = result;
    local_r13 = 0;
    v_stack_m90 = v_xmm0;
    *(uint8_t *)(v_rip + 0xA40904) = 0;
    result = HviGetImplementationLimits(v_stack_m90, Arg2, a3, a4);
    if (((*(uint32_t *)(v_rip + 0xA408C5)) & (0x800000ULL)) == 0) goto loc_0058620B;
    if (((*(uint32_t *)(v_rip + 0xA40901)) & (0x800ULL)) != 0) goto loc_0058620B;
loc_005861DF:
    if (0 >= ((uint32_t)((uint32_t)(Arg1)))) goto loc_0058620B;
    result = HvlpComputeLpComparisonMetrics((uint32_t)((uint32_t)((uint32_t)(Arg1))), Arg2, 0, a4);
    if ((*(uint8_t *)(arg2 + 0x0 + 0x0 * 4 * 8 + 0x2)) == 0) goto loc_00586204;
    if ((*(uint32_t *)(arg2 + 0x0 + 0x0 * 4 * 8 + 0x1C)) == 0) goto loc_00586208;
loc_00586204:
    local_rsi = (uint32_t)((0) + 1);
    goto loc_005861DF;
loc_00586208:
loc_0058620B:
    if ((uint32_t)((uint32_t)(Arg1)) == 0) goto loc_00586242;
loc_00586216:
    *(uint16_t *)(arg2 + 0x8 + 0x4) = (uint16_t)(*(uint16_t *)(arg2 + 0x8));
    *(uint16_t *)(arg2 + 0x8 - 0x8) = 1;
    result = 0;
    if (((*(uint32_t *)(v_rip + 0xA408A8)) & (0x800ULL)) == 0) {
        result = *(uint8_t *)(arg2 + 0x8 - 0x6);
    }
    *(uint8_t *)(arg2 + 0x8 - 0x5) = (uint8_t)(result);
    Arg1 = (Arg2 + 8) + (40);
    Arg2 = ((uint32_t)(Arg1)) - (1);
    if (condition_is_not_equal) goto loc_00586216;
loc_00586242:
    if (0 == 0) goto loc_005864C1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA40A31)))) & (1)) != 0) {
        *(uint32_t *)(v_rip + 0xA40A26) = 0;
        *(uint8_t *)(v_rip + 0xA4084C) = 1;
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA40A15)))) & (1)) != 0) {
        *(uint32_t *)(v_rip + 0xA40A0A) = 0;
        *(uint8_t *)(v_rip + 0xA40834) = 1;
    }
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xA40931));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA40931)))) & (1)) != 0) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xA40931))) + 1);
        *(uint8_t *)(v_rip + 0xA40821) = 1;
        *(uint32_t *)(v_rip + 0xA4091E) = (uint32_t)(result);
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA408E8))) == 0) goto loc_005862DA;
loc_005862B6:
    if ((*(uint16_t *)(v_rip + 0xA41440)) == ((uint16_t)(*(uint16_t *)(arg2 + 0x8)))) goto loc_005862C5;
    result = (uint32_t)((0) + 1);
    Arg1 = (v_rip + 10753088) + (2);
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA408E8))))) goto loc_005862B6;
loc_005862C5:
    local_rsi = (uint32_t)(*(uint32_t *)(v_rip + 0xA408E8));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA408E8))))) {
        local_rsi = 0;
        *(uint32_t *)(v_rip + 0xA408BD) = 0;
        *(uint8_t *)(v_rip + 0xA407E3) = 1;
    }
    if ((*(uint32_t *)(v_rip + 0xA408DF)) == 0) goto loc_005863E8;
    Arg2 = 0;
    result = memset(v_stack_m78, Arg2, 64, a4);
    if ((uint32_t)(local_rsi) == 0) {
        local_rsi = *(uint16_t *)(v_rip + 0xA3ECF6);
    }
    if ((uint32_t)(local_rsi) == 0) goto loc_0058636F;
loc_00586318:
    if ((*(uint32_t *)(v_rip + 0xA40871)) == 0) goto loc_00586338;
    if (((uint32_t)(*(uint16_t *)(v_rip + 0xA41378))) >= 64) goto loc_0058635F;
    if ((*(uint8_t *)(local_rsp + *(uint16_t *)(v_rip + 0xA41378) * 1 + 0x40)) != 0) goto loc_0058635F;
    *(uint8_t *)(local_rsp + *(uint16_t *)(v_rip + 0xA41378) * 1 + 0x40) = 1;
    goto loc_0058633B;
loc_00586338:
loc_0058633B:
loc_0058633E:
    if (0 >= ((uint32_t)((uint32_t)(Arg1)))) goto loc_0058635F;
    if ((*(uint8_t *)(arg2 + 0x0 + 0x0 * 4 * 8 + 0x2)) == 0) goto loc_00586359;
    if (((uint32_t)(*(uint16_t *)(arg2 + 0x0 + 0x0 * 4 * 8 + 0x8))) == 0) goto loc_0058635D;
loc_00586359:
    Arg1 = (uint32_t)((0) + 1);
    goto loc_0058633E;
loc_0058635D:
    local_rbp = (uint32_t)((0) + 1);
loc_0058635F:
    a3 = (uint32_t)((0) + 1);
    local_r10 = (v_rip + 10752888) + (2);
    if (((uint32_t)(a3)) < ((uint32_t)(local_rsi))) goto loc_00586318;
    if ((uint32_t)(local_rbp) != 0) goto loc_0058638A;
loc_0058636F:
    if ((*(uint32_t *)(v_rip + 0xA4081A)) == 0) goto loc_005863DA;
    *(uint32_t *)(v_rip + 0xA40811) = 0;
    *(uint8_t *)(v_rip + 0xA40737) = 1;
    if ((uint32_t)(local_rbp) == 0) goto loc_005863DA;
loc_0058638A:
    if ((*(uint32_t *)(v_rip + 0xA40830)) > ((uint32_t)(local_rbp))) goto loc_005863DA;
    result = HvlIsSingleGroupRequired(Arg1, 0, a3, 0 + 0 * 4);
    *(uint8_t *)(v_rip + 0xA4071F) = 1;
    if ((uint8_t)(result) == 0) goto loc_005863D3;
    *(uint32_t *)(v_rip + 0xA40814) = 64;
    if (((uint32_t)(local_rbp)) < 64) goto loc_005863E8;
    *(uint16_t *)(v_rip + 0xA412C9) = (uint16_t)(*(uint16_t *)(arg2 + 0x8));
    *(uint32_t *)(v_rip + 0xA407BF) = 1;
    goto loc_005863E8;
loc_005863D3:
    *(uint32_t *)(v_rip + 0xA407E6) = 0;
loc_005863DA:
loc_005863E8:
    if ((*(uint8_t *)(v_rip + 0xA406B8)) == 0) goto loc_005864C1;
    Arg1 = (*(uint16_t *)(arg2 + 0x8)) + (*(uint16_t *)(arg2 + 0x8));
    if (*(uint64_t *)(v_rip + 0xA4685F + Arg1 * 8) == 0) goto loc_0058648E;
    result = (condition_is_below) ? 1 : 0;
    if ((uint8_t)(result) == 0) goto loc_0058648E;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xA4))) - 1);
    Arg2 = (uint32_t)(~(Arg2));
    local_r11 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x4))) & ((uint32_t)(Arg2)));
loc_00586441:
    if (1 >= ((uint32_t)((uint32_t)(Arg1)))) goto loc_005864C1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x1 + 0x1 * 4 * 8 + 0x4))) & ((uint32_t)(Arg2)));
    if (((uint32_t)(result)) != ((uint32_t)(local_r11))) goto loc_00586489;
    a4 = (*(uint16_t *)(arg2 + 0x8)) + (*(uint16_t *)(arg2 + 0x8));
    if (((uint32_t)(*(uint32_t *)(arg2 + 0x1 + 0x1 * 4 * 8 + 0x24))) >= (*(uint64_t *)(v_rip + 0xA46816 + a4 * 8))) goto loc_0058648E;
    local_r10 = ((uint32_t)(*(uint32_t *)(arg2 + 0x1 + 0x1 * 4 * 8 + 0x24))) >> (6);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x1 + 0x1 * 4 * 8 + 0x24))))) & (63));
    result = (condition_is_below) ? 1 : 0;
    if ((uint8_t)(result) == 0) goto loc_0058648E;
loc_00586489:
    a3 = (uint32_t)((1) + 1);
    goto loc_00586441;
loc_0058648E:
    result = HvlIsSingleGroupRequired(Arg1, Arg2, a3, a4);
    if ((uint8_t)(result) != 0) {
        result = *(uint16_t *)(arg2 + 0x8);
        *(uint16_t *)(v_rip + 0xA411EE) = (uint16_t)(result);
        *(uint32_t *)(v_rip + 0xA40717) = 64;
        *(uint32_t *)(v_rip + 0xA406DD) = 1;
    }
    *(uint8_t *)(v_rip + 0xA405ED) = 0;
    *(uint8_t *)(v_rip + 0xA405FC) = 1;
loc_005864C1:
    *(uint8_t *)(arg2 + 0x1) = 1;
    *(uint8_t *)(arg2 + 0x3) = 1;
loc_005864D6:
    if ((uint32_t)((uint32_t)(Arg1)) == 0) goto loc_00586635;
loc_005864E4:
    if ((*(uint8_t *)(arg2)) == 0) goto loc_00586610;
    if ((*(uint8_t *)(arg2 + 0x1)) != 0) goto loc_0058660D;
    if ((*(uint8_t *)(arg2 + 0x2)) == 0) goto loc_0058660D;
    if (1 == v_stack_m90) goto loc_0058660D;
    if ((*(uint32_t *)(v_rip + 0xA4077D)) == 0) goto loc_00586548;
loc_0058651F:
    if ((*(uint8_t *)(arg2 + 0x8 - 0x7)) == 0) goto loc_00586531;
    if ((*(uint16_t *)(arg2 + 0x8)) == ((uint16_t)(*(uint16_t *)(arg2 + 0x8)))) {
        a3 = (uint32_t)((0) + 1);
    }
    Arg1 = (Arg2 + 8) + (40);
    a4 = ((uint32_t)(Arg1)) - (1);
    if (condition_is_not_equal) goto loc_0058651F;
    if (((uint32_t)(a3)) == (*(uint32_t *)(v_rip + 0xA4074E))) goto loc_0058660D;
loc_00586548:
    if ((*(uint32_t *)(v_rip + 0xA4073D)) == 0) goto loc_0058659E;
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xA4))) - 1);
    a3 = (uint32_t)(~(a3));
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x4))) & ((uint32_t)(a3)));
loc_00586578:
    if ((*(uint8_t *)(arg2 + 0x4 - 0x3)) == 0) goto loc_0058658B;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x4))) & ((uint32_t)(a3)));
    if (((uint32_t)(result)) == ((uint32_t)(local_r10))) {
        a4 = (uint32_t)((0) + 1);
    }
    Arg1 = (Arg2 + 4) + (40);
    local_r11 = ((uint32_t)(Arg1)) - (1);
    if (condition_is_not_equal) goto loc_00586578;
    if (((uint32_t)(a4)) == (*(uint32_t *)(v_rip + 0xA406F0))) goto loc_0058660D;
loc_0058659E:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA405EB))) == 0) goto loc_005865C5;
loc_005865AD:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA405EB))))) goto loc_0058660D;
    if ((*(uint16_t *)(v_rip + 0xA412A8 + 0x0 * 2)) == ((uint16_t)(*(uint16_t *)(arg2 + 0xC)))) goto loc_005865C5;
    a3 = (uint32_t)((0) + 1);
    goto loc_005865AD;
loc_005865C5:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA405F5))) == 0) goto loc_005865D4;
    if (1 == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA405F5))))) goto loc_0058660D;
loc_005865D4:
    if ((*(uint8_t *)(v_rip + 0xA404CC)) == 0) goto loc_00586610;
    a3 = (*(uint16_t *)(arg2 + 0x8)) + (*(uint16_t *)(arg2 + 0x8));
    if (((uint32_t)(*(uint32_t *)(arg2 + 0x24))) >= (*(uint64_t *)(v_rip + 0xA46774 + a3 * 8))) goto loc_0058660D;
    a4 = ((uint32_t)(*(uint32_t *)(arg2 + 0x24))) >> (6);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x24))))) & (63));
    result = (condition_is_below) ? 1 : 0;
    if ((uint8_t)(result) == 0) {
        *(uint8_t *)(arg2) = 0;
    }
    Arg2 = (Arg2) + (40);
    local_rsi = ((uint32_t)(Arg1)) - (1);
    if (condition_is_not_equal) goto loc_005864E4;
loc_00586624:
    if ((*(uint8_t *)(arg2)) != 0) goto loc_00586638;
    result = (uint32_t)((0) + 1);
    Arg1 = (Arg2) + (40);
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(Arg1)))) goto loc_00586624;
    goto loc_00586638;
loc_00586635:
loc_00586638:
    if (0 == ((uint32_t)((uint32_t)(Arg1)))) goto loc_005866D6;
    if ((uint32_t)((uint32_t)(Arg1)) == 0) goto loc_00586667;
loc_0058664A:
    result = 0;
    if ((*(uint8_t *)(arg2)) != 0) {
        a3 = 0;
        Arg2 = Arg2;
        Arg1 = (uint32_t)((uint32_t)(Arg1));
        result = HvlpComputeLpComparisonMetrics(Arg1, Arg2, a3, a4);
    }
    local_rsi = (uint32_t)((0) + 1);
    local_rbp = (Arg2) + (40);
    if (((uint32_t)(local_rsi)) < ((uint32_t)((uint32_t)(Arg1)))) goto loc_0058664A;
loc_00586667:
    a4 = (uint32_t)((a4) | (0xFFFFFFFFULL));
loc_0058666E:
    if (0 >= ((uint32_t)((uint32_t)(Arg1)))) goto loc_00586685;
    if ((*(uint8_t *)(arg2 + 0x0 + 0x0 * 4 * 8)) != 0) goto loc_00586682;
    Arg2 = (uint32_t)((0) + 1);
    goto loc_0058666E;
loc_00586682:
loc_00586685:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)) + 1)) >= ((uint32_t)((uint32_t)(Arg1)))) goto loc_005866B6;
loc_00586696:
    result = 0;
    if ((*(uint8_t *)(arg2 + (uint32_t)((uint32_t)(arg2)) + 0x1 + (uint32_t)((uint32_t)(arg2)) + 0x1 * 4 * 8)) != 0) {
        Arg2 = Arg2;
        result = HvlpLpComparison((uint32_t)((uint32_t)(Arg2)) + 1 + (uint32_t)((uint32_t)(Arg2)) + 1 * 4, Arg2, (uint32_t)((uint32_t)(Arg2)) + 1, (uint32_t)((uint32_t)(Arg2)));
        a4 = (uint32_t)((uint32_t)(Arg2));
        if (((uint32_t)(result)) == -1) { a4 = (uint32_t)((uint32_t)((uint32_t)(Arg2)) + 1); }
    }
    a3 = (uint32_t)(((uint32_t)((uint32_t)(Arg2)) + 1) + 1);
    local_rsi = (Arg2 + (uint32_t)((uint32_t)(Arg2)) + 1 + (uint32_t)((uint32_t)(Arg2)) + 1 * 4 * 8) + (40);
    if (((uint32_t)(a3)) < ((uint32_t)((uint32_t)(Arg1)))) goto loc_00586696;
loc_005866B6:
    local_r14 = (uint32_t)((1) + 1);
    *(uint8_t *)(arg2 + (uint32_t)((uint32_t)(a4)) + (uint32_t)((uint32_t)(a4)) * 4 * 8 + 0x1) = 1;
    *(uint8_t *)(arg2 + (uint32_t)((uint32_t)(a4)) + (uint32_t)((uint32_t)(a4)) * 4 * 8 + 0x3) = 1;
    goto loc_005864D6;
loc_005866D6:
    if (0 == 0) goto loc_0058672F;
    if (((uint32_t)((uint32_t)(Arg1))) <= 1) goto loc_0058672F;
loc_005866EB:
    if ((*(uint8_t *)(arg2 + 0x29)) == 0) goto loc_00586725;
    result = HvlpComputeLpComparisonMetrics((uint32_t)((uint32_t)((uint32_t)(Arg1))), Arg2, 1, a4);
    if ((*(uint32_t *)(arg2 + 0x29 + 0x1B)) != 0) goto loc_00586725;
    *(uint8_t *)(arg2 + 0x29) = 0;
    result = 0;
    if (((*(uint32_t *)(v_rip + 0xA403C5)) & (0x800ULL)) == 0) {
        result = *(uint8_t *)(arg2 + 0x29 + 0x1);
    }
    *(uint8_t *)(arg2 + 0x29 + 0x2) = (uint8_t)(result);
    *(uint8_t *)(v_rip + 0xA40398) = 1;
loc_00586725:
    local_rbp = (uint32_t)((1) + 1);
    local_rsi = (Arg2 + 41) + (40);
    if (((uint32_t)(local_rbp)) < ((uint32_t)((uint32_t)(Arg1)))) goto loc_005866EB;
loc_0058672F:
    if ((*(uint32_t *)(v_rip + 0xA4045A)) != 0) goto loc_00586790;
    if ((*(uint8_t *)(v_rip + 0xA40368)) != 0) goto loc_00586790;
    if (1 != 0) goto loc_00586790;
loc_00586749:
    if (0 >= ((uint32_t)((uint32_t)(Arg1)))) goto loc_00586790;
    if ((*(uint8_t *)(arg2 + 0x0 + 0x0 * 4 * 8 + 0x2)) == 0) goto loc_00586785;
    if ((uint32_t)((uint32_t)(Arg1)) == 0) goto loc_00586781;
loc_0058676B:
    if ((*(uint16_t *)(arg2 + 0x1 + 0x7)) != ((uint16_t)(*(uint16_t *)(arg2 + 0x0 + 0x0 * 4 * 8 + 0x8)))) goto loc_00586777;
    if ((*(uint8_t *)(arg2 + 0x1)) != 0) goto loc_00586781;
loc_00586777:
    Arg2 = (uint32_t)((0) + 1);
    result = (Arg2 + 1) + (40);
    if (((uint32_t)(Arg2)) < ((uint32_t)((uint32_t)(Arg1)))) goto loc_0058676B;
loc_00586781:
    if (((uint32_t)(Arg2)) == ((uint32_t)((uint32_t)(Arg1)))) goto loc_00586789;
loc_00586785:
    Arg1 = (uint32_t)((0) + 1);
    goto loc_00586749;
loc_00586789:
    goto loc_00586792;
loc_00586790:
    result = 0;
loc_00586792:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, 0 + 0 * 4, *(uint16_t *)(arg2 + 0x0 + 0x0 * 4 * 8 + 0x8));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `- 0x8` | `16` | `W` |
| `Arg2` | `- 0x7` | `8` | `R` |
| `Arg2` | `- 0x6` | `8` | `R` |
| `Arg2` | `- 0x5` | `8` | `W` |
| `Arg2` | `- 0x3` | `8` | `R` |
| `Arg2` | `+ 0x0` | `8` | `R` |
| `Arg2` | `+ 0x0` | `8` | `W` |
| `Arg2` | `+ 0x0` | `16` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0 + rcx*8` | `8` | `R` |
| `Arg2` | `+ 0x0 + rcx*8` | `64` | `R` |
| `Arg2` | `+ 0x1` | `8` | `R` |
| `Arg2` | `+ 0x1` | `8` | `W` |
| `Arg2` | `+ 0x1` | `64` | `R` |
| `Arg2` | `+ 0x1 + rcx*8` | `8` | `W` |
| `Arg2` | `+ 0x2` | `8` | `R` |
| `Arg2` | `+ 0x2` | `8` | `W` |
| `Arg2` | `+ 0x2 + r8*8` | `8` | `R` |
| `Arg2` | `+ 0x2 + r9*8` | `8` | `R` |
| `Arg2` | `+ 0x2 + rbp*8` | `8` | `R` |
| `Arg2` | `+ 0x3` | `8` | `W` |
| `Arg2` | `+ 0x3 + rcx*8` | `8` | `W` |
| `Arg2` | `+ 0x4` | `16` | `W` |
| `Arg2` | `+ 0x4` | `32` | `R` |
| `Arg2` | `+ 0x4` | `64` | `R` |
| `Arg2` | `+ 0x4 + rcx*8` | `32` | `R` |
| `Arg2` | `+ 0x7` | `16` | `R` |
| `Arg2` | `+ 0x8` | `16` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x8 + r8*8` | `16` | `R` |
| `Arg2` | `+ 0x8 + r9*8` | `16` | `R` |
| `Arg2` | `+ 0xC` | `16` | `R` |

추가 오프셋 5개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0058616C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
