# MiSoftFaultMappedView

- RVA: `0x00365364`–`0x003658B3` (길이 `1,359` bytes)
- VA: `0x0000000140365364`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00079F0C`
- 디코드: `325`개 명령, `1,359/1,359` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x003653D3` → [MiVadMapsLargeImage](../2A/MiVadMapsLargeImage_function_002A70F0.md) (function, `0x002A70F0`)
- `0x00365494` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x0036551C` → [MiLockLeafPage](MiLockLeafPage_function_003658C0.md) (function, `0x003658C0`)
- `0x0036557D` → [MiImagePageOk](MiImagePageOk_function_00365AE0.md) (function, `0x00365AE0`)
- `0x00365629` → [MiWorkingSetIsContended](../2A/MiWorkingSetIsContended_function_002AE520.md) (function, `0x002AE520`)
- `0x00365636` → [KeShouldYieldProcessor](../27/KeShouldYieldProcessor_function_002773E0.md) (function, `0x002773E0`)
- `0x00365681` → [MiLockProtoPoolPage](../2B/MiLockProtoPoolPage_function_002B8B80.md) (function, `0x002B8B80`)
- `0x003656A2` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x003656BA` → [MiCompleteRestrictedImageFault](../2C/MiCompleteRestrictedImageFault_function_002C60D4.md) (function, `0x002C60D4`)
- `0x003656E1` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x003656FE` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00365729` → [MiMakeSystemAddressValid](../27/MiMakeSystemAddressValid_function_0027FF70.md) (function, `0x0027FF70`)
- `0x0036576F` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x0036578E` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x003657B2` → [MiCompleteRestrictedImageFault](../2C/MiCompleteRestrictedImageFault_function_002C60D4.md) (function, `0x002C60D4`)
- `0x003657CE` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x003657E7` → [MiCompleteRestrictedImageFault](../2C/MiCompleteRestrictedImageFault_function_002C60D4.md) (function, `0x002C60D4`)
- `0x003657FA` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00365811` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x0036581D` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00365849` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x0036586E` → [MiCompleteRestrictedImageFault](../2C/MiCompleteRestrictedImageFault_function_002C60D4.md) (function, `0x002C60D4`)
- `0x00365887` → [MiUnlockWorkingSetExclusive](../27/MiUnlockWorkingSetExclusive_function_0027EC70.md) (function, `0x0027EC70`)
- `0x00365895` → [MiUnlockWorkingSetExclusive](../27/MiUnlockWorkingSetExclusive_function_0027EC70.md) (function, `0x0027EC70`)

### Direct callers
- [MiMapViewOfImageSection](../../page/97/MiMapViewOfImageSection_function_0097E92C.md) at `0x0097F964`

### Static image references
- `0x00365387` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0036568C` → [sub_006E33B0](../6E/Unknown_function_006E33B0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00365364  48 8B C4                        mov rax, rsp
00365367  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0036536B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0036536F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00365373  55                              push rbp
00365374  41 54                           push r12
00365376  41 55                           push r13
00365378  41 56                           push r14
0036537A  41 57                           push r15
0036537C  48 8D 68 A1                     lea rbp, [rax - 0x5f]
00365380  48 81 EC F0 00 00 00            sub rsp, 0xf0
00365387  48 8B 05 B2 53 AA 00            mov rax, qword ptr [rip + 0xaa53b2]
0036538E  48 33 C4                        xor rax, rsp
00365391  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
00365395  8B 51 30                        mov edx, dword ptr [rcx + 0x30]
00365398  33 C0                           xor eax, eax
0036539A  48 89 45 87                     mov qword ptr [rbp - 0x79], rax
0036539E  0F 57 C0                        xorps xmm0, xmm0
003653A1  8B C2                           mov eax, edx
003653A3  4C 8B E9                        mov r13, rcx
003653A6  25 80 0F 00 00                  and eax, 0xf80
003653AB  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
003653B0  3D 80 00 00 00                  cmp eax, 0x80
003653B5  0F 84 5B 04 00 00               je 0x140365816
003653BB  0F BA E2 15                     bt edx, 0x15
003653BF  72 12                           jb 0x1403653d3
003653C1  8B C2                           mov eax, edx
003653C3  24 70                           and al, 0x70
003653C5  3C 20                           cmp al, 0x20
003653C7  75 0A                           jne 0x1403653d3
003653C9  0F BA E2 16                     bt edx, 0x16
003653CD  0F 82 43 04 00 00               jb 0x140365816
003653D3  E8 18 1D F4 FF                  call 0x1402a70f0
003653D8  85 C0                           test eax, eax
003653DA  0F 85 36 04 00 00               jne 0x140365816
003653E0  48 8B 41 48                     mov rax, qword ptr [rcx + 0x48]
003653E4  48 8B 08                        mov rcx, qword ptr [rax]
003653E7  F7 41 38 00 00 00 08            test dword ptr [rcx + 0x38], 0x8000000
003653EE  0F 85 22 04 00 00               jne 0x140365816
003653F4  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003653FD  45 33 E4                        xor r12d, r12d
00365400  83 64 24 24 00                  and dword ptr [rsp + 0x24], 0
00365405  45 33 F6                        xor r14d, r14d
00365408  4C 89 65 8F                     mov qword ptr [rbp - 0x71], r12
0036540C  48 8B 98 B8 00 00 00            mov rbx, qword ptr [rax + 0xb8]
00365413  48 8B 41 20                     mov rax, qword ptr [rcx + 0x20]
00365417  48 81 C3 00 04 00 00            add rbx, 0x400
0036541E  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00365423  48 89 45 97                     mov qword ptr [rbp - 0x69], rax
00365427  48 85 C0                        test rax, rax
0036542A  0F 84 E6 03 00 00               je 0x140365816
00365430  41 0F B6 4D 20                  movzx ecx, byte ptr [r13 + 0x20]
00365435  48 BA FF FF FF FF 0F 00 00 00   movabs rdx, 0xfffffffff
0036543F  41 8B 45 18                     mov eax, dword ptr [r13 + 0x18]
00365443  45 33 FF                        xor r15d, r15d
00365446  49 8B 75 50                     mov rsi, qword ptr [r13 + 0x50]
0036544A  48 C1 E1 20                     shl rcx, 0x20
0036544E  48 0B C8                        or rcx, rax
00365451  C6 44 24 20 11                  mov byte ptr [rsp + 0x20], 0x11
00365456  48 23 CA                        and rcx, rdx
00365459  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
00365463  49 8B C0                        mov rax, r8
00365466  48 8D 3C C8                     lea rdi, [rax + rcx*8]
0036546A  41 0F B6 4D 21                  movzx ecx, byte ptr [r13 + 0x21]
0036546F  41 8B 45 1C                     mov eax, dword ptr [r13 + 0x1c]
00365473  48 C1 E1 20                     shl rcx, 0x20
00365477  48 0B C8                        or rcx, rax
0036547A  48 23 CA                        and rcx, rdx
0036547D  49 8B C0                        mov rax, r8
00365480  80 4D 84 08                     or byte ptr [rbp - 0x7c], 8
00365484  48 8D 04 C8                     lea rax, [rax + rcx*8]
00365488  48 8B CB                        mov rcx, rbx
0036548B  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
0036548F  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
00365494  E8 57 77 F1 FF                  call 0x14027cbf0
00365499  88 45 83                        mov byte ptr [rbp - 0x7d], al
0036549C  8B 4C 24 24                     mov ecx, dword ptr [rsp + 0x24]
003654A0  48 3B 7D 9F                     cmp rdi, qword ptr [rbp - 0x61]
003654A4  0F 87 18 03 00 00               ja 0x1403657c2
003654AA  49 3B 75 58                     cmp rsi, qword ptr [r13 + 0x58]
003654AE  0F 87 0E 03 00 00               ja 0x1403657c2
003654B4  48 83 7D 97 00                  cmp qword ptr [rbp - 0x69], 0
003654B9  0F 84 03 03 00 00               je 0x1403657c2
003654BF  85 C9                           test ecx, ecx
003654C1  74 09                           je 0x1403654cc
003654C3  F6 C1 07                        test cl, 7
003654C6  0F 84 53 01 00 00               je 0x14036561f
003654CC  48 83 7D 87 00                  cmp qword ptr [rbp - 0x79], 0
003654D1  0F 84 C1 02 00 00               je 0x140365798
003654D7  48 F7 C7 FF 0F 00 00            test rdi, 0xfff
003654DE  0F 84 B4 02 00 00               je 0x140365798
003654E4  48 8B 07                        mov rax, qword ptr [rdi]
003654E7  FF C1                           inc ecx
003654E9  89 4C 24 24                     mov dword ptr [rsp + 0x24], ecx
003654ED  48 85 C0                        test rax, rax
003654F0  0F 85 1C 01 00 00               jne 0x140365612
003654F6  48 F7 C6 FF 0F 00 00            test rsi, 0xfff
003654FD  0F 84 64 01 00 00               je 0x140365667
00365503  4D 85 FF                        test r15, r15
00365506  0F 84 5B 01 00 00               je 0x140365667
0036550C  48 8B 06                        mov rax, qword ptr [rsi]
0036550F  A8 01                           test al, 1
00365511  0F 84 FB 00 00 00               je 0x140365612
00365517  33 D2                           xor edx, edx
00365519  48 8B CE                        mov rcx, rsi
0036551C  E8 9F 03 00 00                  call 0x1403658c0
00365521  48 8B D8                        mov rbx, rax
00365524  48 85 C0                        test rax, rax
00365527  0F 84 D3 00 00 00               je 0x140365600
0036552D  48 8B 06                        mov rax, qword ptr [rsi]
00365530  A8 01                           test al, 1
00365532  0F 84 67 03 00 00               je 0x14036589f
00365538  48 FF 4D 97                     dec qword ptr [rbp - 0x69]
0036553C  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
0036553F  48 0F BA E0 0A                  bt rax, 0xa
00365544  0F 83 55 03 00 00               jae 0x14036589f
0036554A  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
0036554D  C1 E8 18                        shr eax, 0x18
00365550  A8 40                           test al, 0x40
00365552  0F 85 47 03 00 00               jne 0x14036589f
00365558  48 8B CF                        mov rcx, rdi
0036555B  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00365565  48 C1 E1 19                     shl rcx, 0x19
00365569  48 8B C0                        mov rax, rax
0036556C  48 C1 E0 19                     shl rax, 0x19
00365570  4D 8B CD                        mov r9, r13
00365573  48 2B C8                        sub rcx, rax
00365576  48 8B D3                        mov rdx, rbx
00365579  48 C1 F9 10                     sar rcx, 0x10
0036557D  E8 5E 05 00 00                  call 0x140365ae0
00365582  85 C0                           test eax, eax
00365584  0F 84 15 03 00 00               je 0x14036589f
0036558A  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00365594  4C 8B C3                        mov r8, rbx
00365597  4C 2B C0                        sub r8, rax
0036559A  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
003655A4  49 C1 F8 04                     sar r8, 4
003655A8  4C 0F AF C0                     imul r8, rax
003655AC  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
003655B0  48 8D 48 01                     lea rcx, [rax + 1]
003655B4  48 8B D1                        mov rdx, rcx
003655B7  48 33 D0                        xor rdx, rax
003655BA  48 B8 00 00 00 00 00 00 00 C0   movabs rax, 0xc000000000000000
003655C4  48 23 D0                        and rdx, rax
003655C7  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
003655D1  48 33 D1                        xor rdx, rcx
003655D4  48 89 53 18                     mov qword ptr [rbx + 0x18], rdx
003655D8  F0 48 21 43 18                  lock and qword ptr [rbx + 0x18], rax
003655DD  49 83 F8 FF                     cmp r8, -1
003655E1  74 1D                           je 0x140365600
003655E3  45 85 F6                        test r14d, r14d
003655E6  4E 89 44 F5 A7                  mov qword ptr [rbp + r14*8 - 0x59], r8
003655EB  4C 0F 44 E7                     cmove r12, rdi
003655EF  41 FF C6                        inc r14d
003655F2  4C 89 65 8F                     mov qword ptr [rbp - 0x71], r12
003655F6  41 83 FE 10                     cmp r14d, 0x10
003655FA  0F 84 9B 00 00 00               je 0x14036569b
00365600  48 8B 5C 24 28                  mov rbx, qword ptr [rsp + 0x28]
00365605  48 83 C6 08                     add rsi, 8
00365609  48 83 C7 08                     add rdi, 8
0036560D  E9 8A FE FF FF                  jmp 0x14036549c
00365612  48 83 C6 08                     add rsi, 8
00365616  48 83 C7 08                     add rdi, 8
0036561A  E9 81 FE FF FF                  jmp 0x1403654a0
0036561F  0F B6 55 84                     movzx edx, byte ptr [rbp - 0x7c]
00365623  48 8B CB                        mov rcx, rbx
00365626  83 E2 01                        and edx, 1
00365629  E8 F2 8E F4 FF                  call 0x1402ae520
0036562E  85 C0                           test eax, eax
00365630  0F 85 99 00 00 00               jne 0x1403656cf
00365636  E8 A5 1D F1 FF                  call 0x1402773e0
0036563B  85 C0                           test eax, eax
0036563D  0F 85 8C 00 00 00               jne 0x1403656cf
00365643  4D 85 FF                        test r15, r15
00365646  74 16                           je 0x14036565e
00365648  49 8B 07                        mov rax, qword ptr [r15]
0036564B  48 B9 FE FF FF FF FF 0F 00 00   movabs rcx, 0xffffffffffe
00365655  48 85 C1                        test rcx, rax
00365658  0F 85 F5 01 00 00               jne 0x140365853
0036565E  8B 4C 24 24                     mov ecx, dword ptr [rsp + 0x24]
00365662  E9 65 FE FF FF                  jmp 0x1403654cc
00365667  4D 85 FF                        test r15, r15
0036566A  0F 85 F8 00 00 00               jne 0x140365768
00365670  45 85 F6                        test r14d, r14d
00365673  0F 85 2A 01 00 00               jne 0x1403657a3
00365679  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
0036567E  48 8B CE                        mov rcx, rsi
00365681  E8 FA 34 F5 FF                  call 0x1402b8b80
00365686  4C 8B F8                        mov r15, rax
00365689  48 85 C0                        test rax, rax
0036568C  0F 84 1E DD 37 00               je 0x1406e33b0
00365692  8B 4C 24 24                     mov ecx, dword ptr [rsp + 0x24]
00365696  E9 71 FE FF FF                  jmp 0x14036550c
0036569B  8A 54 24 20                     mov dl, byte ptr [rsp + 0x20]
0036569F  49 8B CF                        mov rcx, r15
003656A2  E8 E9 09 EE FF                  call 0x140246090
003656A7  45 33 FF                        xor r15d, r15d
003656AA  4C 8D 45 A7                     lea r8, [rbp - 0x59]
003656AE  49 8B D4                        mov rdx, r12
003656B1  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
003656B6  45 8D 4F 10                     lea r9d, [r15 + 0x10]
003656BA  E8 15 0A F6 FF                  call 0x1402c60d4
003656BF  85 C0                           test eax, eax
003656C1  0F 84 25 01 00 00               je 0x1403657ec
003656C7  45 33 F6                        xor r14d, r14d
003656CA  E9 31 FF FF FF                  jmp 0x140365600
003656CF  41 BC 01 00 00 00               mov r12d, 1
003656D5  4D 85 FF                        test r15, r15
003656D8  74 0F                           je 0x1403656e9
003656DA  8A 54 24 20                     mov dl, byte ptr [rsp + 0x20]
003656DE  49 8B CF                        mov rcx, r15
003656E1  E8 AA 09 EE FF                  call 0x140246090
003656E6  45 33 FF                        xor r15d, r15d
003656E9  45 85 F6                        test r14d, r14d
003656EC  0F 85 6C 01 00 00               jne 0x14036585e
003656F2  48 8B 55 87                     mov rdx, qword ptr [rbp - 0x79]
003656F6  48 85 D2                        test rdx, rdx
003656F9  74 08                           je 0x140365703
003656FB  48 8B CB                        mov rcx, rbx
003656FE  E8 BD 17 EB FF                  call 0x140216ec0
00365703  41 83 FC 01                     cmp r12d, 1
00365707  74 73                           je 0x14036577c
00365709  41 8B 5D 30                     mov ebx, dword ptr [r13 + 0x30]
0036570D  C1 EB 0C                        shr ebx, 0xc
00365710  83 E3 7F                        and ebx, 0x7f
00365713  41 83 FC 01                     cmp r12d, 1
00365717  0F 84 27 01 00 00               je 0x140365844
0036571D  44 8A 45 83                     mov r8b, byte ptr [rbp - 0x7d]
00365721  45 33 C9                        xor r9d, r9d
00365724  8B D3                           mov edx, ebx
00365726  48 8B CF                        mov rcx, rdi
00365729  E8 42 A8 F1 FF                  call 0x14027ff70
0036572E  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00365738  48 8B CF                        mov rcx, rdi
0036573B  48 C1 E9 09                     shr rcx, 9
0036573F  48 23 C8                        and rcx, rax
00365742  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0036574C  48 8B C0                        mov rax, rax
0036574F  48 8B 5C 24 28                  mov rbx, qword ptr [rsp + 0x28]
00365754  48 03 C8                        add rcx, rax
00365757  4C 8B 65 8F                     mov r12, qword ptr [rbp - 0x71]
0036575B  48 89 4D 87                     mov qword ptr [rbp - 0x79], rcx
0036575F  8B 4C 24 24                     mov ecx, dword ptr [rsp + 0x24]
00365763  E9 7C FD FF FF                  jmp 0x1403654e4
00365768  8A 54 24 20                     mov dl, byte ptr [rsp + 0x20]
0036576C  49 8B CF                        mov rcx, r15
0036576F  E8 1C 09 EE FF                  call 0x140246090
00365774  45 33 FF                        xor r15d, r15d
00365777  E9 F4 FE FF FF                  jmp 0x140365670
0036577C  F6 45 84 01                     test byte ptr [rbp - 0x7c], 1
00365780  8A 55 83                        mov dl, byte ptr [rbp - 0x7d]
00365783  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00365788  0F 85 F9 00 00 00               jne 0x140365887
0036578E  E8 FD 7E F1 FF                  call 0x14027d690
00365793  E9 71 FF FF FF                  jmp 0x140365709
00365798  41 BC 02 00 00 00               mov r12d, 2
0036579E  E9 32 FF FF FF                  jmp 0x1403656d5
003657A3  45 8B CE                        mov r9d, r14d
003657A6  4C 8D 45 A7                     lea r8, [rbp - 0x59]
003657AA  49 8B D4                        mov rdx, r12
003657AD  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
003657B2  E8 1D 09 F6 FF                  call 0x1402c60d4
003657B7  45 33 F6                        xor r14d, r14d
003657BA  85 C0                           test eax, eax
003657BC  0F 85 B7 FE FF FF               jne 0x140365679
003657C2  4D 85 FF                        test r15, r15
003657C5  74 0C                           je 0x1403657d3
003657C7  8A 54 24 20                     mov dl, byte ptr [rsp + 0x20]
003657CB  49 8B CF                        mov rcx, r15
003657CE  E8 BD 08 EE FF                  call 0x140246090
003657D3  45 85 F6                        test r14d, r14d
003657D6  74 14                           je 0x1403657ec
003657D8  45 8B CE                        mov r9d, r14d
003657DB  4C 8D 45 A7                     lea r8, [rbp - 0x59]
003657DF  49 8B D4                        mov rdx, r12
003657E2  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
003657E7  E8 E8 08 F6 FF                  call 0x1402c60d4
003657EC  48 8B 55 87                     mov rdx, qword ptr [rbp - 0x79]
003657F0  48 85 D2                        test rdx, rdx
003657F3  74 0A                           je 0x1403657ff
003657F5  48 8B 4C 24 28                  mov rcx, qword ptr [rsp + 0x28]
003657FA  E8 C1 16 EB FF                  call 0x140216ec0
003657FF  F6 45 84 01                     test byte ptr [rbp - 0x7c], 1
00365803  8A 55 83                        mov dl, byte ptr [rbp - 0x7d]
00365806  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0036580B  0F 85 84 00 00 00               jne 0x140365895
00365811  E8 7A 7E F1 FF                  call 0x14027d690
00365816  48 8B 4D 27                     mov rcx, qword ptr [rbp + 0x27]
0036581A  48 33 CC                        xor rcx, rsp
0036581D  E8 1E 6E 34 00                  call 0x1406ac640
00365822  4C 8D 9C 24 F0 00 00 00         lea r11, [rsp + 0xf0]
0036582A  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0036582E  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00365832  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00365836  49 8B E3                        mov rsp, r11
00365839  41 5F                           pop r15
0036583B  41 5E                           pop r14
0036583D  41 5D                           pop r13
0036583F  41 5C                           pop r12
00365841  5D                              pop rbp
00365842  C3                              ret
00365843  CC                              int3
00365844  48 8B 4C 24 28                  mov rcx, qword ptr [rsp + 0x28]
00365849  E8 A2 73 F1 FF                  call 0x14027cbf0
0036584E  E9 CA FE FF FF                  jmp 0x14036571d
00365853  41 BC 01 00 00 00               mov r12d, 1
00365859  E9 7C FE FF FF                  jmp 0x1403656da
0036585E  48 8B 55 8F                     mov rdx, qword ptr [rbp - 0x71]
00365862  4C 8D 45 A7                     lea r8, [rbp - 0x59]
00365866  45 8B CE                        mov r9d, r14d
00365869  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
0036586E  E8 61 08 F6 FF                  call 0x1402c60d4
00365873  45 33 F6                        xor r14d, r14d
00365876  85 C0                           test eax, eax
00365878  0F 85 74 FE FF FF               jne 0x1403656f2
0036587E  4C 8B 65 8F                     mov r12, qword ptr [rbp - 0x71]
00365882  E9 3B FF FF FF                  jmp 0x1403657c2
00365887  E8 E4 93 F1 FF                  call 0x14027ec70
0036588C  80 65 84 FE                     and byte ptr [rbp - 0x7c], 0xfe
00365890  E9 74 FE FF FF                  jmp 0x140365709
00365895  E8 D6 93 F1 FF                  call 0x14027ec70
0036589A  E9 77 FF FF FF                  jmp 0x140365816
0036589F  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
003658A9  F0 48 21 43 18                  lock and qword ptr [rbx + 0x18], rax
003658AE  E9 4D FD FF FF                  jmp 0x140365600
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiSoftFaultMappedView(__int64 a1)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF4;
    unsigned __int8 v_stack_mF8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (240);
    result = (*(unsigned __int64 *)(v_rip + 11162546)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 39) = result;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 121) = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48))))) & (0xF80ULL));
    v_stack_mE8 = v_xmm0;
    if (((unsigned int)(result)) == 128) goto loc_00365816;
    if (((unsigned int)(result)) < 128) goto loc_003653D3;
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48))))) & (112));
    if (((unsigned __int8)(result)) != 32) goto loc_003653D3;
    if (((unsigned __int8)(result)) < 32) goto loc_00365816;
loc_003653D3:
    result = MiVadMapsLargeImage(a1, (unsigned int)(*(unsigned int *)(a1 + 48)), a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00365816;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) + 56)) & (0x8000000ULL)) != 0) goto loc_00365816;
    v_r12 = 0;
    v_r14 = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 113) = 0;
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
    v_stack_mF0 = v_rbx;
    *(unsigned __int64 *)(v_rsp - 95 - 105) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) + 32);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) + 32) == 0) goto loc_00365816;
    v_r15 = 0;
    a1 = (*(unsigned __int8 *)(a1 + 32)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(a1 + 24)));
    v_stack_mF8 = 17;
    a1 = (a1) & ((unsigned int)(*(unsigned int *)(a1 + 48)));
    a1 = (*(unsigned __int8 *)(a1 + 33)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(a1 + 28)));
    a1 = (a1) & ((unsigned int)(*(unsigned int *)(a1 + 48)));
    *(unsigned __int64 *)(v_rsp - 95 - 97) = a3 + a1 * 8;
    v_stack_mE8 = v_rbx;
    result = MiLockWorkingSetShared(v_rbx, (unsigned int)(*(unsigned int *)(a1 + 48)), a3, a4);
    *(unsigned __int8 *)(v_rsp - 95 - 125) = (unsigned __int8)(result);
loc_0036549C:
loc_003654A0:
    if ((a3 + a1 * 8) > (*(unsigned __int64 *)(v_rsp - 95 - 97))) goto loc_003657C2;
    if ((*(unsigned __int64 *)(a1 + 80)) > (*(unsigned __int64 *)(a1 + 88))) goto loc_003657C2;
    if ((*(unsigned __int64 *)(v_rsp - 95 - 105)) == 0) goto loc_003657C2;
    if ((unsigned int)((unsigned int)(v_stack_mF4)) == 0) goto loc_003654CC;
    if ((((unsigned __int8)((unsigned int)(v_stack_mF4))) & (7)) == 0) goto loc_0036561F;
loc_003654CC:
    if ((*(unsigned __int64 *)(v_rsp - 95 - 121)) == 0) goto loc_00365798;
    if (((a3 + a1 * 8) & (0xFFFULL)) == 0) goto loc_00365798;
loc_003654E4:
    a1 = (unsigned int)(((unsigned int)(v_stack_mF4)) + 1);
    v_stack_mF4 = (unsigned int)(a1);
    if (*(unsigned __int64 *)(a3 + a1 * 8) != 0) goto loc_00365612;
    if (((*(unsigned __int64 *)(a1 + 80)) & (0xFFFULL)) == 0) goto loc_00365667;
    if (0 == 0) goto loc_00365667;
loc_0036550C:
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 80)))) & (1)) == 0) goto loc_00365612;
    a2 = 0;
    result = MiLockLeafPage(*(unsigned __int64 *)(a1 + 80), a2, a3, a4);
    if (result == 0) goto loc_00365600;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 80)))) & (1)) == 0) goto loc_0036589F;
    if (condition_is_above_or_equal) goto loc_0036589F;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (64)) != 0) goto loc_0036589F;
    a1 = (a3 + a1 * 8) << (25);
    result = (result) << (25);
    a1 = (a1) - (result);
    a1 = (a1) >> (16);
    result = MiImagePageOk(a1, result, a3, a1);
    if ((unsigned int)(result) == 0) goto loc_0036589F;
    a3 = (result) - (result);
    a3 = (a3) >> (4);
    a3 = (a3) * (result);
    a2 = (*(unsigned __int64 *)(result + 24) + 1) ^ (*(unsigned __int64 *)(result + 24));
    a2 = (a2) & (*(unsigned __int64 *)(result + 24));
    a2 = (a2) ^ (*(unsigned __int64 *)(result + 24) + 1);
    *(unsigned __int64 *)(result + 24) = a2;
    if (a3 == -1) goto loc_00365600;
    *(unsigned __int64 *)(v_rsp - 95 + v_r14 * 8 - 89) = a3;
    if (0 == 0) { v_r12 = a3 + a1 * 8; }
    v_r14 = (unsigned int)((v_r14) + 1);
    *(unsigned __int64 *)(v_rsp - 95 - 113) = v_r12;
    if (((unsigned int)(v_r14)) == 16) goto loc_0036569B;
loc_00365600:
    v_rsi = (*(unsigned __int64 *)(a1 + 80)) + (8);
    v_rdi = (a3 + a1 * 8) + (8);
    goto loc_0036549C;
loc_00365612:
    v_rsi = (v_rsi) + (8);
    v_rdi = (v_rdi) + (8);
    goto loc_003654A0;
loc_0036561F:
    a2 = (unsigned int)((*(unsigned __int8 *)(v_rsp - 95 - 124)) & (1));
    result = MiWorkingSetIsContended(v_stack_mF0, a2, a3, a1);
    if ((unsigned int)(result) != 0) goto loc_003656CF;
    result = KeShouldYieldProcessor(v_stack_mF0, a2, a3, a1);
    if ((unsigned int)(result) != 0) goto loc_003656CF;
    if (0 == 0) goto loc_0036565E;
    if (((v_stack_mF0) & (*(unsigned __int64 *)(v_r15))) != 0) goto loc_00365853;
loc_0036565E:
    goto loc_003654CC;
loc_00365667:
    if (0 != 0) goto loc_00365768;
loc_00365670:
    if ((unsigned int)(v_r14) != 0) goto loc_003657A3;
loc_00365679:
    result = MiLockProtoPoolPage(v_rsi, v_stack_mF8, a3, a1);
    goto loc_0036550C;
loc_0036569B:
    result = MiUnlockProtoPoolPage(result, v_stack_mF8, a3, a1);
    v_r15 = 0;
    result = MiCompleteRestrictedImageFault(v_stack_mE8, v_r12, v_rsp - 95 - 89, v_r15 + 16);
    if ((unsigned int)(result) == 0) goto loc_003657EC;
    v_r14 = 0;
    goto loc_00365600;
loc_003656CF:
loc_003656D5:
    if (0 != 0) {
        a2 = v_stack_mF8;
        a1 = 0;
        result = MiUnlockProtoPoolPage(a1, a2, v_rsp - 95 - 89, v_r15 + 16);
        v_r15 = 0;
    }
    if (0 != 0) goto loc_0036585E;
loc_003656F2:
    if (*(unsigned __int64 *)(v_rsp - 95 - 121) != 0) {
        a1 = v_stack_mF0;
        result = MiUnlockPageTable(a1, *(unsigned __int64 *)(v_rsp - 95 - 121), v_rsp - 95 - 89, v_r15 + 16);
    }
    if (1 == 1) goto loc_0036577C;
loc_00365709:
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 48))) >> (12));
    v_rbx = (unsigned int)((v_rbx) & (127));
    if (1 == 1) goto loc_00365844;
loc_0036571D:
    a4 = 0;
    result = MiMakeSystemAddressValid(v_rdi, (unsigned int)((unsigned int)(v_rbx)), *(unsigned __int8 *)(v_rsp - 95 - 125), a4);
    a1 = (v_rdi) >> (9);
    a1 = (a1) & (result);
    a1 = (a1) + (result);
    *(unsigned __int64 *)(v_rsp - 95 - 121) = a1;
    goto loc_003654E4;
loc_00365768:
    result = MiUnlockProtoPoolPage(0, v_stack_mF8, *(unsigned __int8 *)(v_rsp - 95 - 125), a4);
    v_r15 = 0;
    goto loc_00365670;
loc_0036577C:
    if (((*(unsigned __int8 *)(v_rsp - 95 - 124)) & (1)) != 0) goto loc_00365887;
    result = MiUnlockWorkingSetShared(v_stack_mE8, *(unsigned __int8 *)(v_rsp - 95 - 125), *(unsigned __int8 *)(v_rsp - 95 - 125), a4);
    goto loc_00365709;
loc_00365798:
    goto loc_003656D5;
loc_003657A3:
    result = MiCompleteRestrictedImageFault(v_stack_mE8, 2, v_rsp - 95 - 89, 0);
    v_r14 = 0;
    if ((unsigned int)(result) != 0) goto loc_00365679;
loc_003657C2:
    if (0 != 0) {
        a2 = v_stack_mF8;
        a1 = 0;
        result = MiUnlockProtoPoolPage(a1, a2, v_rsp - 95 - 89, 0);
    }
    if (0 != 0) {
        a4 = 0;
        a3 = v_rsp - 95 - 89;
        a2 = 2;
        a1 = v_stack_mE8;
        result = MiCompleteRestrictedImageFault(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 95 - 121) != 0) {
        a1 = v_stack_mF0;
        result = MiUnlockPageTable(a1, *(unsigned __int64 *)(v_rsp - 95 - 121), a3, a4);
    }
    if (((*(unsigned __int8 *)(v_rsp - 95 - 124)) & (1)) != 0) goto loc_00365895;
    result = MiUnlockWorkingSetShared(v_stack_mE8, *(unsigned __int8 *)(v_rsp - 95 - 125), a3, a4);
loc_00365816:
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 39)) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int8 *)(v_rsp - 95 - 125), a3, a4);
    return result;
loc_00365844:
    result = MiLockWorkingSetShared(v_stack_mC8, *(unsigned __int8 *)(v_rsp - 95 - 125), a3, a4);
    goto loc_0036571D;
loc_00365853:
    goto loc_003656DA;
loc_0036585E:
    result = MiCompleteRestrictedImageFault(v_stack_mC0, *(unsigned __int64 *)(v_rsp - 95 - 113), v_rsp - 95 - 89, 0);
    v_r14 = 0;
    if ((unsigned int)(result) != 0) goto loc_003656F2;
    goto loc_003657C2;
loc_00365887:
    result = MiUnlockWorkingSetExclusive(v_stack_mC0, *(unsigned __int64 *)(v_rsp - 95 - 113), v_rsp - 95 - 89, 0);
    goto loc_00365709;
loc_00365895:
    result = MiUnlockWorkingSetExclusive(v_stack_mC0, *(unsigned __int64 *)(v_rsp - 95 - 113), v_rsp - 95 - 89, 0);
    goto loc_00365816;
loc_0036589F:
    goto loc_00365600;
}
```

## 5. (Beta) C Style

```c
int64_t MiSoftFaultMappedView(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF4;
    uint8_t v_stack_mF8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (240);
    result = (*(uint64_t *)(v_rip + 0xAA53B2)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x27) = result;
    result = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x79) = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30))))) & (0xF80ULL));
    v_stack_mE8 = v_xmm0;
    if (((uint32_t)(result)) == 128) goto loc_00365816;
    if (((uint32_t)(result)) < 128) goto loc_003653D3;
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30))))) & (112));
    if (((uint8_t)(result)) != 32) goto loc_003653D3;
    if (((uint8_t)(result)) < 32) goto loc_00365816;
loc_003653D3:
    result = MiVadMapsLargeImage(Arg1, (uint32_t)(*(uint32_t *)(arg1 + 0x30)), a3, a4);
    if ((uint32_t)(result) != 0) goto loc_00365816;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) + 0x38)) & (0x8000000ULL)) != 0) goto loc_00365816;
    local_r12 = 0;
    local_r14 = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x71) = 0;
    local_rbx = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
    v_stack_mF0 = local_rbx;
    *(uint64_t *)(local_rsp - 0x5F - 0x69) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) + 0x20);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) + 0x20) == 0) goto loc_00365816;
    local_r15 = 0;
    Arg1 = (*(uint8_t *)(arg1 + 0x20)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(arg1 + 0x18)));
    v_stack_mF8 = 17;
    Arg1 = (Arg1) & ((uint32_t)(*(uint32_t *)(arg1 + 0x30)));
    Arg1 = (*(uint8_t *)(arg1 + 0x21)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(arg1 + 0x1C)));
    Arg1 = (Arg1) & ((uint32_t)(*(uint32_t *)(arg1 + 0x30)));
    *(uint64_t *)(local_rsp - 0x5F - 0x61) = a3 + Arg1 * 8;
    v_stack_mE8 = local_rbx;
    result = MiLockWorkingSetShared(local_rbx, (uint32_t)(*(uint32_t *)(arg1 + 0x30)), a3, a4);
    *(uint8_t *)(local_rsp - 0x5F - 0x7D) = (uint8_t)(result);
loc_0036549C:
loc_003654A0:
    if ((a3 + Arg1 * 8) > (*(uint64_t *)(local_rsp - 0x5F - 0x61))) goto loc_003657C2;
    if ((*(uint64_t *)(arg1 + 0x50)) > (*(uint64_t *)(arg1 + 0x58))) goto loc_003657C2;
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x69)) == 0) goto loc_003657C2;
    if ((uint32_t)((uint32_t)(v_stack_mF4)) == 0) goto loc_003654CC;
    if ((((uint8_t)((uint32_t)(v_stack_mF4))) & (7)) == 0) goto loc_0036561F;
loc_003654CC:
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x79)) == 0) goto loc_00365798;
    if (((a3 + Arg1 * 8) & (0xFFFULL)) == 0) goto loc_00365798;
loc_003654E4:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_mF4)) + 1);
    v_stack_mF4 = (uint32_t)(Arg1);
    if (*(uint64_t *)(a3 + arg1 * 8) != 0) goto loc_00365612;
    if (((*(uint64_t *)(arg1 + 0x50)) & (0xFFFULL)) == 0) goto loc_00365667;
    if (0 == 0) goto loc_00365667;
loc_0036550C:
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x50)))) & (1)) == 0) goto loc_00365612;
    a2 = 0;
    result = MiLockLeafPage(*(uint64_t *)(arg1 + 0x50), a2, a3, a4);
    if (result == 0) goto loc_00365600;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x50)))) & (1)) == 0) goto loc_0036589F;
    if (condition_is_above_or_equal) goto loc_0036589F;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (64)) != 0) goto loc_0036589F;
    Arg1 = (a3 + Arg1 * 8) << (25);
    result = (result) << (25);
    Arg1 = (Arg1) - (result);
    Arg1 = (Arg1) >> (16);
    result = MiImagePageOk(Arg1, result, a3, Arg1);
    if ((uint32_t)(result) == 0) goto loc_0036589F;
    a3 = (result) - (result);
    a3 = (a3) >> (4);
    a3 = (a3) * (result);
    a2 = (*(uint64_t *)(result + 0x18) + 1) ^ (*(uint64_t *)(result + 0x18));
    a2 = (a2) & (*(uint64_t *)(result + 0x18));
    a2 = (a2) ^ (*(uint64_t *)(result + 0x18) + 1);
    *(uint64_t *)(result + 0x18) = a2;
    if (a3 == -1) goto loc_00365600;
    *(uint64_t *)(local_rsp - 0x5F + local_r14 * 8 - 0x59) = a3;
    if (0 == 0) { local_r12 = a3 + Arg1 * 8; }
    local_r14 = (uint32_t)((local_r14) + 1);
    *(uint64_t *)(local_rsp - 0x5F - 0x71) = local_r12;
    if (((uint32_t)(local_r14)) == 16) goto loc_0036569B;
loc_00365600:
    local_rsi = (*(uint64_t *)(arg1 + 0x50)) + (8);
    local_rdi = (a3 + Arg1 * 8) + (8);
    goto loc_0036549C;
loc_00365612:
    local_rsi = (local_rsi) + (8);
    local_rdi = (local_rdi) + (8);
    goto loc_003654A0;
loc_0036561F:
    a2 = (uint32_t)((*(uint8_t *)(local_rsp - 0x5F - 0x7C)) & (1));
    result = MiWorkingSetIsContended(v_stack_mF0, a2, a3, Arg1);
    if ((uint32_t)(result) != 0) goto loc_003656CF;
    result = KeShouldYieldProcessor(v_stack_mF0, a2, a3, Arg1);
    if ((uint32_t)(result) != 0) goto loc_003656CF;
    if (0 == 0) goto loc_0036565E;
    if (((v_stack_mF0) & (*(uint64_t *)(local_r15))) != 0) goto loc_00365853;
loc_0036565E:
    goto loc_003654CC;
loc_00365667:
    if (0 != 0) goto loc_00365768;
loc_00365670:
    if ((uint32_t)(local_r14) != 0) goto loc_003657A3;
loc_00365679:
    result = MiLockProtoPoolPage(local_rsi, v_stack_mF8, a3, Arg1);
    goto loc_0036550C;
loc_0036569B:
    result = MiUnlockProtoPoolPage(result, v_stack_mF8, a3, Arg1);
    local_r15 = 0;
    result = MiCompleteRestrictedImageFault(v_stack_mE8, local_r12, local_rsp - 95 - 89, local_r15 + 16);
    if ((uint32_t)(result) == 0) goto loc_003657EC;
    local_r14 = 0;
    goto loc_00365600;
loc_003656CF:
loc_003656D5:
    if (0 != 0) {
        a2 = v_stack_mF8;
        Arg1 = 0;
        result = MiUnlockProtoPoolPage(Arg1, a2, local_rsp - 95 - 89, local_r15 + 16);
        local_r15 = 0;
    }
    if (0 != 0) goto loc_0036585E;
loc_003656F2:
    if (*(uint64_t *)(local_rsp - 0x5F - 0x79) != 0) {
        Arg1 = v_stack_mF0;
        result = MiUnlockPageTable(Arg1, *(uint64_t *)(local_rsp - 0x5F - 0x79), local_rsp - 95 - 89, local_r15 + 16);
    }
    if (1 == 1) goto loc_0036577C;
loc_00365709:
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x30))) >> (12));
    local_rbx = (uint32_t)((local_rbx) & (127));
    if (1 == 1) goto loc_00365844;
loc_0036571D:
    a4 = 0;
    result = MiMakeSystemAddressValid(local_rdi, (uint32_t)((uint32_t)(local_rbx)), *(uint8_t *)(local_rsp - 0x5F - 0x7D), a4);
    Arg1 = (local_rdi) >> (9);
    Arg1 = (Arg1) & (result);
    Arg1 = (Arg1) + (result);
    *(void **)(local_rsp - 0x5F - 0x79) = Arg1;
    goto loc_003654E4;
loc_00365768:
    result = MiUnlockProtoPoolPage(0, v_stack_mF8, *(uint8_t *)(local_rsp - 0x5F - 0x7D), a4);
    local_r15 = 0;
    goto loc_00365670;
loc_0036577C:
    if (((*(uint8_t *)(local_rsp - 0x5F - 0x7C)) & (1)) != 0) goto loc_00365887;
    result = MiUnlockWorkingSetShared(v_stack_mE8, *(uint8_t *)(local_rsp - 0x5F - 0x7D), *(uint8_t *)(local_rsp - 0x5F - 0x7D), a4);
    goto loc_00365709;
loc_00365798:
    goto loc_003656D5;
loc_003657A3:
    result = MiCompleteRestrictedImageFault(v_stack_mE8, 2, local_rsp - 95 - 89, 0);
    local_r14 = 0;
    if ((uint32_t)(result) != 0) goto loc_00365679;
loc_003657C2:
    if (0 != 0) {
        a2 = v_stack_mF8;
        Arg1 = 0;
        result = MiUnlockProtoPoolPage(Arg1, a2, local_rsp - 95 - 89, 0);
    }
    if (0 != 0) {
        a4 = 0;
        a3 = local_rsp - 95 - 89;
        a2 = 2;
        Arg1 = v_stack_mE8;
        result = MiCompleteRestrictedImageFault(Arg1, a2, a3, a4);
    }
    if (*(uint64_t *)(local_rsp - 0x5F - 0x79) != 0) {
        Arg1 = v_stack_mF0;
        result = MiUnlockPageTable(Arg1, *(uint64_t *)(local_rsp - 0x5F - 0x79), a3, a4);
    }
    if (((*(uint8_t *)(local_rsp - 0x5F - 0x7C)) & (1)) != 0) goto loc_00365895;
    result = MiUnlockWorkingSetShared(v_stack_mE8, *(uint8_t *)(local_rsp - 0x5F - 0x7D), a3, a4);
loc_00365816:
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x27)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint8_t *)(local_rsp - 0x5F - 0x7D), a3, a4);
    return result;
loc_00365844:
    result = MiLockWorkingSetShared(v_stack_mC8, *(uint8_t *)(local_rsp - 0x5F - 0x7D), a3, a4);
    goto loc_0036571D;
loc_00365853:
    goto loc_003656DA;
loc_0036585E:
    result = MiCompleteRestrictedImageFault(v_stack_mC0, *(uint64_t *)(local_rsp - 0x5F - 0x71), local_rsp - 95 - 89, 0);
    local_r14 = 0;
    if ((uint32_t)(result) != 0) goto loc_003656F2;
    goto loc_003657C2;
loc_00365887:
    result = MiUnlockWorkingSetExclusive(v_stack_mC0, *(uint64_t *)(local_rsp - 0x5F - 0x71), local_rsp - 95 - 89, 0);
    goto loc_00365709;
loc_00365895:
    result = MiUnlockWorkingSetExclusive(v_stack_mC0, *(uint64_t *)(local_rsp - 0x5F - 0x71), local_rsp - 95 - 89, 0);
    goto loc_00365816;
loc_0036589F:
    goto loc_00365600;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x20` | `8` | `R` |
| `Arg1` | `+ 0x21` | `8` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00365364&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
