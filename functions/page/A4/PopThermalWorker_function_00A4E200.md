# PopThermalWorker

- RVA: `0x00A4E200`–`0x00A4E6C1` (길이 `1,217` bytes)
- VA: `0x0000000140A4E200`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000B0614`
- 디코드: `290`개 명령, `1,217/1,217` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00A4E26F` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)
- `0x00A4E341` → [KeSetTimer2](../../text/3A/KeSetTimer2_function_003A08E0.md) (function, `0x003A08E0`)
- `0x00A4E352` → [IoReuseIrp](../../text/24/IoReuseIrp_function_0024DD70.md) (function, `0x0024DD70`)
- `0x00A4E39C` → [IofCallDriver](../../text/29/IofCallDriver_function_0029B4B0.md) (function, `0x0029B4B0`)
- `0x00A4E3A4` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)
- `0x00A4E3B1` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A4E409` → [PopCheckThermalPolicy](PopCheckThermalPolicy_function_00A4E6C8.md) (function, `0x00A4E6C8`)
- `0x00A4E41A` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x00A4E487` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x00A4E4A4` → [PopDiagTraceThermalCoolingMode](PopDiagTraceThermalCoolingMode_function_00A4E96C.md) (function, `0x00A4E96C`)
- `0x00A4E4D3` → [IoReuseIrp](../../text/24/IoReuseIrp_function_0024DD70.md) (function, `0x0024DD70`)
- `0x00A4E523` → [PopCheckAndHandleThermalConditions](../../text/4A/PopCheckAndHandleThermalConditions_function_004A8C00.md) (function, `0x004A8C00`)
- `0x00A4E56A` → [PopFireThermalWmiEvent](../../text/5D/PopFireThermalWmiEvent_function_005D5448.md) (function, `0x005D5448`)
- `0x00A4E57C` → [PopDiagTraceThermalZoneEnumeration](../../text/5D/PopDiagTraceThermalZoneEnumeration_function_005D7154.md) (function, `0x005D7154`)
- `0x00A4E590` → [PopThermalUpdatePassiveTimeTracking](../AA/PopThermalUpdatePassiveTimeTracking_function_00AA15EC.md) (function, `0x00AA15EC`)
- `0x00A4E5B0` → [PopDiagTraceThermalZoneThrottlePerfTrack](../../text/5D/PopDiagTraceThermalZoneThrottlePerfTrack_function_005D7628.md) (function, `0x005D7628`)
- `0x00A4E5CB` → [PopDiagTracePassiveCooling](../76/PopDiagTracePassiveCooling_function_00761CAC.md) (function, `0x00761CAC`)
- `0x00A4E5F8` → [PopDiagTracePassiveCooling](../76/PopDiagTracePassiveCooling_function_00761CAC.md) (function, `0x00761CAC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00A4E21C` → RVA `0x00E0A740` (`.data`; read)
- `0x00A4E2EA` → RVA `0x00E67848` (`.data`; read)
- `0x00A4E31D` → RVA `0x00F0C960` (`.data`; read)
- `0x00A4E383` → RVA `0x004B1E40` (`PopThermalIrpComplete`; read)
- `0x00A4E4A9` → RVA `0x00E678C4` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **13**
  - `0x00A4E26F` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
  - `0x00A4E341` → [KeSetTimer2](../../text/3A/KeSetTimer2_function_003A08E0.md) (`PAGE` → `.text`)
  - `0x00A4E352` → [IoReuseIrp](../../text/24/IoReuseIrp_function_0024DD70.md) (`PAGE` → `.text`)
  - `0x00A4E39C` → [IofCallDriver](../../text/29/IofCallDriver_function_0029B4B0.md) (`PAGE` → `.text`)
  - `0x00A4E3A4` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
  - `0x00A4E3B1` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A4E41A` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x00A4E487` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x00A4E4D3` → [IoReuseIrp](../../text/24/IoReuseIrp_function_0024DD70.md) (`PAGE` → `.text`)
  - `0x00A4E523` → [PopCheckAndHandleThermalConditions](../../text/4A/PopCheckAndHandleThermalConditions_function_004A8C00.md) (`PAGE` → `.text`)
  - `0x00A4E56A` → [PopFireThermalWmiEvent](../../text/5D/PopFireThermalWmiEvent_function_005D5448.md) (`PAGE` → `.text`)
  - `0x00A4E57C` → [PopDiagTraceThermalZoneEnumeration](../../text/5D/PopDiagTraceThermalZoneEnumeration_function_005D7154.md) (`PAGE` → `.text`)
  - `0x00A4E5B0` → [PopDiagTraceThermalZoneThrottlePerfTrack](../../text/5D/PopDiagTraceThermalZoneThrottlePerfTrack_function_005D7628.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **16**
  - `0x00A4E43C` → [sub_00B3BE18 + 0xCD](../B3/Unknown_function_00B3BE18.md) (`tail-transfer`)
  - `0x00A4E459` → [sub_00B3BE18 + 0xCD](../B3/Unknown_function_00B3BE18.md) (`tail-transfer`)
  - `0x00A4E494` → [sub_00B3BE18](../B3/Unknown_function_00B3BE18.md) (`tail-transfer`)
  - `0x00A4E4FD` → [sub_00B3BE18 + 0xCD](../B3/Unknown_function_00B3BE18.md) (`tail-transfer`)
  - `0x00A4E5D6` → [sub_00B3BE18 + 0x164](../B3/Unknown_function_00B3BE18.md) (`tail-transfer`)
  - `0x00A4E5DE` → [sub_00B3BE18 + 0x1A7](../B3/Unknown_function_00B3BE18.md) (`tail-transfer`)
  - `0x00A4E604` → [sub_00B3BE18 + 0x1A7](../B3/Unknown_function_00B3BE18.md) (`tail-transfer`)
  - `0x00A4E623` → [sub_00B3BE18 + 0x1BD](../B3/Unknown_function_00B3BE18.md) (`tail-transfer`)
  - `0x00A4E640` → [sub_00B3BE18 + 0x1C8](../B3/Unknown_function_00B3BE18.md) (`tail-transfer`)
  - `0x00A4E661` → [sub_00B3BE18 + 0x1C8](../B3/Unknown_function_00B3BE18.md) (`tail-transfer`)
  - `0x00A4E685` → [sub_00B3BE18 + 0x1BD](../B3/Unknown_function_00B3BE18.md) (`tail-transfer`)
  - `0x00A4E694` → [sub_00B3BE18 + 0x1E2](../B3/Unknown_function_00B3BE18.md) (`tail-transfer`)
  - `0x00A4E6A4` → [sub_00B3BE18 + 0x1DC](../B3/Unknown_function_00B3BE18.md) (`tail-transfer`)
  - `0x00A4E6AD` → [sub_00B3BE18 + 0x1D7](../B3/Unknown_function_00B3BE18.md) (`tail-transfer`)
  - `0x00A4E6B6` → [sub_00B3BE18 + 0x1D7](../B3/Unknown_function_00B3BE18.md) (`tail-transfer`)
  - `0x00A4E6BC` → [sub_00B3BE18 + 0x1E2](../B3/Unknown_function_00B3BE18.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A4E200  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00A4E205  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
00A4E20A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00A4E20F  57                              push rdi
00A4E210  41 54                           push r12
00A4E212  41 55                           push r13
00A4E214  41 56                           push r14
00A4E216  41 57                           push r15
00A4E218  48 83 EC 60                     sub rsp, 0x60
00A4E21C  48 8B 05 1D C5 3B 00            mov rax, qword ptr [rip + 0x3bc51d]
00A4E223  48 33 C4                        xor rax, rsp
00A4E226  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00A4E22B  33 FF                           xor edi, edi
00A4E22D  4C 8D B9 B0 01 00 00            lea r15, [rcx + 0x1b0]
00A4E234  48 8B F1                        mov rsi, rcx
00A4E237  40 88 7C 24 30                  mov byte ptr [rsp + 0x30], dil
00A4E23C  0F 57 C0                        xorps xmm0, xmm0
00A4E23F  40 88 7C 24 32                  mov byte ptr [rsp + 0x32], dil
00A4E244  49 BE 08 00 00 00 80 F7 FF FF   movabs r14, 0xfffff78000000008
00A4E24E  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
00A4E253  4D 8B 36                        mov r14, qword ptr [r14]
00A4E256  48 8B 69 38                     mov rbp, qword ptr [rcx + 0x38]
00A4E25A  4C 8B 69 30                     mov r13, qword ptr [rcx + 0x30]
00A4E25E  49 8B CF                        mov rcx, r15
00A4E261  48 89 6C 24 38                  mov qword ptr [rsp + 0x38], rbp
00A4E266  40 88 7C 24 31                  mov byte ptr [rsp + 0x31], dil
00A4E26B  89 7C 24 34                     mov dword ptr [rsp + 0x34], edi
00A4E26F  E8 D0 28 9E FF                  call 0x140430b44
00A4E274  40 38 7E 42                     cmp byte ptr [rsi + 0x42], dil
00A4E278  0F 85 F9 01 00 00               jne 0x140a4e477
00A4E27E  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
00A4E281  44 8D 67 01                     lea r12d, [rdi + 1]
00A4E285  85 C0                           test eax, eax
00A4E287  0F 89 48 01 00 00               jns 0x140a4e3d5
00A4E28D  3D 9D 00 00 C0                  cmp eax, 0xc000009d
00A4E292  0F 85 AB 02 00 00               jne 0x140a4e543
00A4E298  40 8A C7                        mov al, dil
00A4E29B  0F B6 54 24 32                  movzx edx, byte ptr [rsp + 0x32]
00A4E2A0  4C 8D 4E 46                     lea r9, [rsi + 0x46]
00A4E2A4  0F B6 C8                        movzx ecx, al
00A4E2A7  41 8A 01                        mov al, byte ptr [r9]
00A4E2AA  38 46 45                        cmp byte ptr [rsi + 0x45], al
00A4E2AD  8B 46 54                        mov eax, dword ptr [rsi + 0x54]
00A4E2B0  41 0F 45 CC                     cmovne ecx, r12d
00A4E2B4  39 46 50                        cmp dword ptr [rsi + 0x50], eax
00A4E2B7  8A 46 40                        mov al, byte ptr [rsi + 0x40]
00A4E2BA  41 0F 45 D4                     cmovne edx, r12d
00A4E2BE  3C 06                           cmp al, 6
00A4E2C0  0F 84 80 00 00 00               je 0x140a4e346
00A4E2C6  3C 0A                           cmp al, 0xa
00A4E2C8  0F 84 44 03 00 00               je 0x140a4e612
00A4E2CE  3C 07                           cmp al, 7
00A4E2D0  0F 84 9B 03 00 00               je 0x140a4e671
00A4E2D6  84 C9                           test cl, cl
00A4E2D8  0F 85 4A 03 00 00               jne 0x140a4e628
00A4E2DE  84 D2                           test dl, dl
00A4E2E0  0F 85 5F 03 00 00               jne 0x140a4e645
00A4E2E6  0F B6 46 43                     movzx eax, byte ptr [rsi + 0x43]
00A4E2EA  8B 0D 58 95 41 00               mov ecx, dword ptr [rip + 0x419558]
00A4E2F0  3B C1                           cmp eax, ecx
00A4E2F2  0F 85 C5 01 00 00               jne 0x140a4e4bd
00A4E2F8  40 38 BE E4 00 00 00            cmp byte ptr [rsi + 0xe4], dil
00A4E2FF  0F 85 61 03 00 00               jne 0x140a4e666
00A4E305  48 8B CF                        mov rcx, rdi
00A4E308  44 88 66 40                     mov byte ptr [rsi + 0x40], r12b
00A4E30C  44 84 66 41                     test byte ptr [rsi + 0x41], r12b
00A4E310  74 0B                           je 0x140a4e31d
00A4E312  8B 46 68                        mov eax, dword ptr [rsi + 0x68]
00A4E315  85 C0                           test eax, eax
00A4E317  0F 85 41 01 00 00               jne 0x140a4e45e
00A4E31D  39 3D 3D E6 4B 00               cmp dword ptr [rip + 0x4be63d], edi
00A4E323  4C 8B CF                        mov r9, rdi
00A4E326  0F 85 5E 03 00 00               jne 0x140a4e68a
00A4E32C  48 85 C9                        test rcx, rcx
00A4E32F  74 15                           je 0x140a4e346
00A4E331  4C 2B F1                        sub r14, rcx
00A4E334  45 33 C0                        xor r8d, r8d
00A4E337  49 8B D6                        mov rdx, r14
00A4E33A  48 8D 8E 28 01 00 00            lea rcx, [rsi + 0x128]
00A4E341  E8 9A 25 95 FF                  call 0x1403a08e0
00A4E346  48 8B 5E 38                     mov rbx, qword ptr [rsi + 0x38]
00A4E34A  BA BB 00 00 C0                  mov edx, 0xc00000bb
00A4E34F  48 8B CB                        mov rcx, rbx
00A4E352  E8 19 FA 7F FF                  call 0x14024dd70
00A4E357  48 8B 83 B8 00 00 00            mov rax, qword ptr [rbx + 0xb8]
00A4E35E  B9 5C 00 00 00                  mov ecx, 0x5c
00A4E363  C6 40 B8 0F                     mov byte ptr [rax - 0x48], 0xf
00A4E367  C7 40 D0 80 40 29 00            mov dword ptr [rax - 0x30], 0x294080
00A4E36E  89 48 C8                        mov dword ptr [rax - 0x38], ecx
00A4E371  89 48 C0                        mov dword ptr [rax - 0x40], ecx
00A4E374  48 8D 46 70                     lea rax, [rsi + 0x70]
00A4E378  48 89 43 18                     mov qword ptr [rbx + 0x18], rax
00A4E37C  48 8B 85 B8 00 00 00            mov rax, qword ptr [rbp + 0xb8]
00A4E383  48 8D 0D B6 3A A6 FF            lea rcx, [rip - 0x59c54a]
00A4E38A  48 8B D5                        mov rdx, rbp
00A4E38D  48 89 48 F0                     mov qword ptr [rax - 0x10], rcx
00A4E391  49 8B CD                        mov rcx, r13
00A4E394  48 89 70 F8                     mov qword ptr [rax - 8], rsi
00A4E398  C6 40 BB E0                     mov byte ptr [rax - 0x45], 0xe0
00A4E39C  E8 0F D1 84 FF                  call 0x14029b4b0
00A4E3A1  49 8B CF                        mov rcx, r15
00A4E3A4  E8 13 18 89 FF                  call 0x1402dfbbc
00A4E3A9  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00A4E3AE  48 33 CC                        xor rcx, rsp
00A4E3B1  E8 8A E2 C5 FF                  call 0x1406ac640
00A4E3B6  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
00A4E3BB  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00A4E3BF  49 8B 6B 40                     mov rbp, qword ptr [r11 + 0x40]
00A4E3C3  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
00A4E3C7  49 8B E3                        mov rsp, r11
00A4E3CA  41 5F                           pop r15
00A4E3CC  41 5E                           pop r14
00A4E3CE  41 5D                           pop r13
00A4E3D0  41 5C                           pop r12
00A4E3D2  5F                              pop rdi
00A4E3D3  C3                              ret
00A4E3D4  CC                              int3
00A4E3D5  0F B6 4E 40                     movzx ecx, byte ptr [rsi + 0x40]
00A4E3D9  BB 64 00 00 00                  mov ebx, 0x64
00A4E3DE  41 2B CC                        sub ecx, r12d
00A4E3E1  0F 85 AA 00 00 00               jne 0x140a4e491
00A4E3E7  8A 46 41                        mov al, byte ptr [rsi + 0x41]
00A4E3EA  4C 89 B6 F0 00 00 00            mov qword ptr [rsi + 0xf0], r14
00A4E3F1  A8 02                           test al, 2
00A4E3F3  0F 84 7B 01 00 00               je 0x140a4e574
00A4E3F9  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00A4E3FE  49 8B D6                        mov rdx, r14
00A4E401  4C 8D 44 24 31                  lea r8, [rsp + 0x31]
00A4E406  48 8B CE                        mov rcx, rsi
00A4E409  E8 BA 02 00 00                  call 0x140a4e6c8
00A4E40E  48 8D 8E D8 01 00 00            lea rcx, [rsi + 0x1d8]
00A4E415  45 33 C0                        xor r8d, r8d
00A4E418  33 D2                           xor edx, edx
00A4E41A  E8 F1 0E 8F FF                  call 0x14033f310
00A4E41F  44 8A 7C 24 31                  mov r15b, byte ptr [rsp + 0x31]
00A4E424  44 8B 64 24 34                  mov r12d, dword ptr [rsp + 0x34]
00A4E429  0F B6 56 45                     movzx edx, byte ptr [rsi + 0x45]
00A4E42D  8B BE DC 00 00 00               mov edi, dword ptr [rsi + 0xdc]
00A4E433  0F B6 AE 90 00 00 00            movzx ebp, byte ptr [rsi + 0x90]
00A4E43A  3B FA                           cmp edi, edx
00A4E43C  0F 85 A3 DA 0E 00               jne 0x140b3bee5
00A4E442  8A 4E 41                        mov cl, byte ptr [rsi + 0x41]
00A4E445  8A C1                           mov al, cl
00A4E447  24 04                           and al, 4
00A4E449  3B FD                           cmp edi, ebp
00A4E44B  0F 83 AA 00 00 00               jae 0x140a4e4fb
00A4E451  84 C0                           test al, al
00A4E453  0F 85 AA 00 00 00               jne 0x140a4e503
00A4E459  E9 87 DA 0E 00                  jmp 0x140b3bee5
00A4E45E  48 03 46 60                     add rax, qword ptr [rsi + 0x60]
00A4E462  49 3B C6                        cmp rax, r14
00A4E465  7F 08                           jg 0x140a4e46f
00A4E467  89 7E 70                        mov dword ptr [rsi + 0x70], edi
00A4E46A  E9 AE FE FF FF                  jmp 0x140a4e31d
00A4E46F  48 8B C8                        mov rcx, rax
00A4E472  E9 A6 FE FF FF                  jmp 0x140a4e31d
00A4E477  40 88 7E 40                     mov byte ptr [rsi + 0x40], dil
00A4E47B  48 8D 8E C0 01 00 00            lea rcx, [rsi + 0x1c0]
00A4E482  45 33 C0                        xor r8d, r8d
00A4E485  33 D2                           xor edx, edx
00A4E487  E8 84 0E 8F FF                  call 0x14033f310
00A4E48C  E9 10 FF FF FF                  jmp 0x140a4e3a1
00A4E491  41 2B CC                        sub ecx, r12d
00A4E494  0F 85 7E D9 0E 00               jne 0x140b3be18
00A4E49A  0F B6 56 44                     movzx edx, byte ptr [rsi + 0x44]
00A4E49E  49 8B CD                        mov rcx, r13
00A4E4A1  88 56 43                        mov byte ptr [rsi + 0x43], dl
00A4E4A4  E8 C3 04 00 00                  call 0x140a4e96c
00A4E4A9  39 3D 15 94 41 00               cmp dword ptr [rip + 0x419415], edi
00A4E4AF  0F 85 B2 00 00 00               jne 0x140a4e567
00A4E4B5  41 8A C4                        mov al, r12b
00A4E4B8  E9 DE FD FF FF                  jmp 0x140a4e29b
00A4E4BD  48 8B 5E 38                     mov rbx, qword ptr [rsi + 0x38]
00A4E4C1  48 8D 7E 44                     lea rdi, [rsi + 0x44]
00A4E4C5  88 0F                           mov byte ptr [rdi], cl
00A4E4C7  BA BB 00 00 C0                  mov edx, 0xc00000bb
00A4E4CC  48 8B CB                        mov rcx, rbx
00A4E4CF  C6 46 40 02                     mov byte ptr [rsi + 0x40], 2
00A4E4D3  E8 98 F8 7F FF                  call 0x14024dd70
00A4E4D8  48 8B 83 B8 00 00 00            mov rax, qword ptr [rbx + 0xb8]
00A4E4DF  C6 40 B8 0F                     mov byte ptr [rax - 0x48], 0xf
00A4E4E3  83 60 C0 00                     and dword ptr [rax - 0x40], 0
00A4E4E7  C7 40 D0 84 80 29 00            mov dword ptr [rax - 0x30], 0x298084
00A4E4EE  44 89 60 C8                     mov dword ptr [rax - 0x38], r12d
00A4E4F2  48 89 7B 18                     mov qword ptr [rbx + 0x18], rdi
00A4E4F6  E9 81 FE FF FF                  jmp 0x140a4e37c
00A4E4FB  84 C0                           test al, al
00A4E4FD  0F 85 E2 D9 0E 00               jne 0x140b3bee5
00A4E503  8B 46 50                        mov eax, dword ptr [rsi + 0x50]
00A4E506  39 86 D8 00 00 00               cmp dword ptr [rsi + 0xd8], eax
00A4E50C  75 78                           jne 0x140a4e586
00A4E50E  80 E1 01                        and cl, 1
00A4E511  33 FF                           xor edi, edi
00A4E513  45 84 FF                        test r15b, r15b
00A4E516  74 49                           je 0x140a4e561
00A4E518  84 C9                           test cl, cl
00A4E51A  0F 84 97 00 00 00               je 0x140a4e5b7
00A4E520  48 8B CE                        mov rcx, rsi
00A4E523  E8 D8 A6 A5 FF                  call 0x1404a8c00
00A4E528  8A 44 24 30                     mov al, byte ptr [rsp + 0x30]
00A4E52C  4C 8D BE B0 01 00 00            lea r15, [rsi + 0x1b0]
00A4E533  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
00A4E538  41 BC 01 00 00 00               mov r12d, 1
00A4E53E  E9 58 FD FF FF                  jmp 0x140a4e29b
00A4E543  3D 20 01 00 C0                  cmp eax, 0xc0000120
00A4E548  0F 84 4A FD FF FF               je 0x140a4e298
00A4E54E  80 7E 40 07                     cmp byte ptr [rsi + 0x40], 7
00A4E552  0F 84 B1 00 00 00               je 0x140a4e609
00A4E558  C6 46 40 05                     mov byte ptr [rsi + 0x40], 5
00A4E55C  E9 1A FF FF FF                  jmp 0x140a4e47b
00A4E561  84 C9                           test cl, cl
00A4E563  74 BB                           je 0x140a4e520
00A4E565  EB 50                           jmp 0x140a4e5b7
00A4E567  8A 4E 43                        mov cl, byte ptr [rsi + 0x43]
00A4E56A  E8 D9 6E B8 FF                  call 0x1405d5448
00A4E56F  E9 41 FF FF FF                  jmp 0x140a4e4b5
00A4E574  0C 02                           or al, 2
00A4E576  48 8B CE                        mov rcx, rsi
00A4E579  88 46 41                        mov byte ptr [rsi + 0x41], al
00A4E57C  E8 D3 8B B8 FF                  call 0x1405d7154
00A4E581  E9 73 FE FF FF                  jmp 0x140a4e3f9
00A4E586  8A 56 50                        mov dl, byte ptr [rsi + 0x50]
00A4E589  48 8D 8E F8 01 00 00            lea rcx, [rsi + 0x1f8]
00A4E590  E8 57 30 05 00                  call 0x140aa15ec
00A4E595  8B 86 D8 00 00 00               mov eax, dword ptr [rsi + 0xd8]
00A4E59B  4D 8B C5                        mov r8, r13
00A4E59E  8B 8E 80 00 00 00               mov ecx, dword ptr [rsi + 0x80]
00A4E5A4  2B D8                           sub ebx, eax
00A4E5A6  8B D3                           mov edx, ebx
00A4E5A8  C6 44 24 32 01                  mov byte ptr [rsp + 0x32], 1
00A4E5AD  89 46 54                        mov dword ptr [rsi + 0x54], eax
00A4E5B0  E8 73 90 B8 FF                  call 0x1405d7628
00A4E5B5  33 FF                           xor edi, edi
00A4E5B7  48 8D 5E 70                     lea rbx, [rsi + 0x70]
00A4E5BB  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00A4E5BF  48 8B CB                        mov rcx, rbx
00A4E5C2  45 8B CC                        mov r9d, r12d
00A4E5C5  45 8A C7                        mov r8b, r15b
00A4E5C8  49 8B D5                        mov rdx, r13
00A4E5CB  E8 DC 36 D1 FF                  call 0x140761cac
00A4E5D0  8A 46 41                        mov al, byte ptr [rsi + 0x41]
00A4E5D3  45 84 FF                        test r15b, r15b
00A4E5D6  0F 84 A0 D9 0E 00               je 0x140b3bf7c
00A4E5DC  A8 01                           test al, 1
00A4E5DE  0F 85 DB D9 0E 00               jne 0x140b3bfbf
00A4E5E4  45 8B CC                        mov r9d, r12d
00A4E5E7  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
00A4E5EF  41 B0 01                        mov r8b, 1
00A4E5F2  49 8B D5                        mov rdx, r13
00A4E5F5  48 8B CB                        mov rcx, rbx
00A4E5F8  E8 AF 36 D1 FF                  call 0x140761cac
00A4E5FD  4C 89 B6 00 01 00 00            mov qword ptr [rsi + 0x100], r14
00A4E604  E9 B6 D9 0E 00                  jmp 0x140b3bfbf
00A4E609  44 88 66 40                     mov byte ptr [rsi + 0x40], r12b
00A4E60D  E9 86 FC FF FF                  jmp 0x140a4e298
00A4E612  4C 8D 8E 10 04 00 00            lea r9, [rsi + 0x410]
00A4E619  B8 10 00 00 00                  mov eax, 0x10
00A4E61E  BA 98 40 29 00                  mov edx, 0x294098
00A4E623  E9 AD D9 0E 00                  jmp 0x140b3bfd5
00A4E628  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
00A4E62C  45 8A C4                        mov r8b, r12b
00A4E62F  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
00A4E637  BA 88 80 29 00                  mov edx, 0x298088
00A4E63C  C6 46 40 03                     mov byte ptr [rsi + 0x40], 3
00A4E640  E9 9B D9 0E 00                  jmp 0x140b3bfe0
00A4E645  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
00A4E649  4C 8D 4E 54                     lea r9, [rsi + 0x54]
00A4E64D  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
00A4E655  45 8A C4                        mov r8b, r12b
00A4E658  C6 46 40 04                     mov byte ptr [rsi + 0x40], 4
00A4E65C  BA 8C 80 29 00                  mov edx, 0x29808c
00A4E661  E9 7A D9 0E 00                  jmp 0x140b3bfe0
00A4E666  C6 46 40 08                     mov byte ptr [rsi + 0x40], 8
00A4E66A  44 88 A6 D0 00 00 00            mov byte ptr [rsi + 0xd0], r12b
00A4E671  4C 8D 8E CC 00 00 00            lea r9, [rsi + 0xcc]
00A4E678  B8 18 00 00 00                  mov eax, 0x18
00A4E67D  45 89 21                        mov dword ptr [r9], r12d
00A4E680  BA 94 40 29 00                  mov edx, 0x294094
00A4E685  E9 4B D9 0E 00                  jmp 0x140b3bfd5
00A4E68A  48 8B 96 E8 00 00 00            mov rdx, qword ptr [rsi + 0xe8]
00A4E691  48 85 D2                        test rdx, rdx
00A4E694  0F 84 60 D9 0E 00               je 0x140b3bffa
00A4E69A  48 03 96 F0 00 00 00            add rdx, qword ptr [rsi + 0xf0]
00A4E6A1  49 3B D6                        cmp rdx, r14
00A4E6A4  0F 8E 4A D9 0E 00               jle 0x140b3bff4
00A4E6AA  48 85 C9                        test rcx, rcx
00A4E6AD  0F 84 3C D9 0E 00               je 0x140b3bfef
00A4E6B3  48 3B CA                        cmp rcx, rdx
00A4E6B6  0F 8D 33 D9 0E 00               jge 0x140b3bfef
00A4E6BC  E9 39 D9 0E 00                  jmp 0x140b3bffa
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopThermalWorker(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m2C;
    unsigned __int8 v_stack_m2E;
    unsigned __int64 v_stack_m2F;
    unsigned __int8 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m54;
    unsigned __int8 v_stack_m56;
    unsigned __int8 v_stack_m57;
    unsigned __int8 v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (96);
    result = (*(unsigned __int64 *)(v_rip + 3917085)) ^ (v_rsp);
    v_stack_m38 = result;
    v_rdi = 0;
    v_stack_m58 = 0;
    v_stack_m56 = 0;
    v_stack_m48 = v_xmm0;
    v_stack_m50 = *(unsigned __int64 *)(a1 + 56);
    v_stack_m57 = 0;
    v_stack_m54 = 0;
    result = PopAcquireRwLockExclusive(a1 + 432, a2, a3, a4);
    if ((*(unsigned __int8 *)(a1 + 66)) != 0) goto loc_00A4E477;
    if (!sign_flag) goto loc_00A4E3D5;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 56) + 48)))) != 0xC000009DULL) goto loc_00A4E543;
loc_00A4E298:
loc_00A4E29B:
    a1 = 0;
    if ((*(unsigned __int8 *)(a1 + 69)) != ((unsigned __int8)(*(unsigned __int8 *)(a1 + 70)))) { a1 = (unsigned int)(v_rdi + 1); }
    a2 = v_stack_m56;
    if ((*(unsigned int *)(a1 + 80)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 84))))) { a2 = (unsigned int)(v_rdi + 1); }
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 64))) == 6) goto loc_00A4E346;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 64))) == 10) goto loc_00A4E612;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 64))) == 7) goto loc_00A4E671;
    if ((unsigned __int8)(a1) != 0) goto loc_00A4E628;
    if ((unsigned __int8)(a2) != 0) goto loc_00A4E645;
    if (((unsigned int)(*(unsigned __int8 *)(a1 + 67))) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4298072))))) goto loc_00A4E4BD;
    if ((*(unsigned __int8 *)(a1 + 228)) != 0) goto loc_00A4E666;
    *(unsigned __int8 *)(a1 + 64) = (unsigned __int8)(v_rdi + 1);
    if (((*(unsigned __int8 *)(a1 + 65)) & ((unsigned __int8)(v_rdi + 1))) == 0) goto loc_00A4E31D;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 104))) != 0) goto loc_00A4E45E;
loc_00A4E31D:
    if ((*(unsigned int *)(v_rip + 4974141)) != 0) goto loc_00A4E68A;
    result = (unsigned int)(*(unsigned int *)(a1 + 104));
    v_r14 = *(unsigned __int64 *)(v_r14);
    if (0 != 0) {
        v_r14 = (*(unsigned __int64 *)(v_r14)) - (0);
        a3 = 0;
        a2 = v_r14;
        a1 = a1 + 296;
        result = KeSetTimer2(a1, a2, a3, 0);
    }
    result = IoReuseIrp(*(unsigned __int64 *)(a1 + 56), (unsigned int)(0xC00000BBULL), a3, 0);
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 184) - 72) = 15;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 184) - 48) = 0x294080ULL;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 184) - 56) = 92;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 184) - 64) = 92;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 24) = a1 + 112;
loc_00A4E37C:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 184) - 16) = v_rip - 5883210;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 184) - 8) = a1;
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 184) - 69) = 224;
    result = IofCallDriver(*(unsigned __int64 *)(a1 + 48), *(unsigned __int64 *)(a1 + 56), a3, 0);
loc_00A4E3A1:
    result = PopReleaseRwLock(a1 + 432, *(unsigned __int64 *)(a1 + 56), a3, 0);
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(a1 + 56), a3, 0);
    return result;
loc_00A4E3D5:
    a1 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 64)) - ((unsigned int)(v_rdi + 1)));
    if (condition_is_not_equal) goto loc_00A4E491;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 240) = v_r14;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 65))) & (2)) == 0) goto loc_00A4E574;
loc_00A4E3F9:
    result = PopCheckThermalPolicy(*(unsigned __int64 *)(v_stack_m28 + 72), v_r14, v_stack_m2F, v_stack_m2C);
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(*(unsigned __int64 *)(v_stack_m28 + 72) + 472, a2, a3, v_stack_m2C);
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 65))) & (4));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 220)))) >= ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 144)))) goto loc_00A4E4FB;
    if ((unsigned __int8)(result) != 0) goto loc_00A4E503;
loc_00A4E45E:
    result = (result) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 96));
    if (result > v_r14) goto loc_00A4E46F;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 112) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 220)));
    goto loc_00A4E31D;
loc_00A4E46F:
    goto loc_00A4E31D;
loc_00A4E477:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 64) = (unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 220)));
loc_00A4E47B:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(*(unsigned __int64 *)(v_stack_m28 + 72) + 448, a2, a3, v_stack_m2C);
    goto loc_00A4E3A1;
loc_00A4E491:
    a1 = (unsigned int)((*(unsigned __int64 *)(v_stack_m28 + 72) + 448) - ((unsigned int)((unsigned int)(v_stack_m2C))));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 67) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 68));
    result = PopDiagTraceThermalCoolingMode(*(unsigned __int64 *)(a1 + 48), *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 68), a3, v_stack_m2C);
    if ((*(unsigned int *)(v_rip + 4297749)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 220))))) goto loc_00A4E567;
loc_00A4E4B5:
    goto loc_00A4E29B;
loc_00A4E4BD:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 68) = (unsigned __int8)(*(unsigned __int64 *)(a1 + 48));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 64) = 2;
    result = IoReuseIrp(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 56), (unsigned int)(0xC00000BBULL), a3, v_stack_m2C);
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 56) + 184) - 72) = 15;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 56) + 184) - 48) = 0x298084ULL;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 56) + 184) - 56) = (unsigned int)((unsigned int)(v_stack_m2C));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 56) + 24) = *(unsigned __int64 *)(v_stack_m28 + 72) + 68;
    goto loc_00A4E37C;
loc_00A4E4FB:
loc_00A4E503:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 216)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 80))))) goto loc_00A4E586;
    a1 = (unsigned __int8)((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 56)) & (1));
    v_rdi = 0;
    if ((unsigned __int8)(v_stack_m2F) == 0) goto loc_00A4E561;
    if ((unsigned __int8)(a1) == 0) goto loc_00A4E5B7;
loc_00A4E520:
    result = PopCheckAndHandleThermalConditions(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)(0xC00000BBULL), a3, v_stack_m2C);
    goto loc_00A4E29B;
loc_00A4E543:
    if (((unsigned int)(v_stack_m30)) == 0xC0000120ULL) goto loc_00A4E298;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 64)) == 7) goto loc_00A4E609;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 64) = 5;
    goto loc_00A4E47B;
loc_00A4E561:
    if ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 72)) == 0) goto loc_00A4E520;
    goto loc_00A4E5B7;
loc_00A4E567:
    result = PopFireThermalWmiEvent(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 67), (unsigned int)(0xC00000BBULL), a3, v_stack_m2C);
    goto loc_00A4E4B5;
loc_00A4E574:
    result = (unsigned __int8)((result) | (2));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 65) = (unsigned __int8)(result);
    result = PopDiagTraceThermalZoneEnumeration(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)(0xC00000BBULL), a3, v_stack_m2C);
    goto loc_00A4E3F9;
loc_00A4E586:
    result = PopThermalUpdatePassiveTimeTracking(*(unsigned __int64 *)(v_stack_m28 + 72) + 504, *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 80), a3, v_stack_m2C);
    v_rbx = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 56)) - ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 216)))));
    v_stack_m2E = 1;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 84) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 216)));
    result = PopDiagTraceThermalZoneThrottlePerfTrack((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 128)), (unsigned int)((unsigned int)(v_rbx)), *(unsigned __int64 *)(a1 + 48), v_stack_m2C);
    v_rdi = 0;
loc_00A4E5B7:
    v_stack_m40 = 0;
    result = PopDiagTracePassiveCooling(*(unsigned __int64 *)(v_stack_m28 + 72) + 112, *(unsigned __int64 *)(a1 + 48), (unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 72) + 432), 1);
    v_stack_m40 = 1;
    result = PopDiagTracePassiveCooling(*(unsigned __int64 *)(v_stack_m28 + 72) + 112, *(unsigned __int64 *)(a1 + 48), 1, 1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 256) = v_r14;
loc_00A4E609:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 64) = 1;
    goto loc_00A4E298;
loc_00A4E612:
loc_00A4E628:
    v_stack_m38 = 0;
    v_stack_m40 = 4;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 64) = 3;
loc_00A4E645:
    v_stack_m38 = 0;
    v_stack_m40 = 4;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 64) = 4;
loc_00A4E666:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 64) = 8;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 208) = 1;
loc_00A4E671:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 204) = 1;
loc_00A4E68A:
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 232)) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 240));
}
```

## 5. (Beta) C Style

```c
int64_t PopThermalWorker(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m2C;
    uint8_t v_stack_m2E;
    uint64_t v_stack_m2F;
    uint8_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m54;
    uint8_t v_stack_m56;
    uint8_t v_stack_m57;
    uint8_t v_stack_m58;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (96);
    result = (*(uint64_t *)(v_rip + 0x3BC51D)) ^ (local_rsp);
    v_stack_m38 = result;
    local_rdi = 0;
    v_stack_m58 = 0;
    v_stack_m56 = 0;
    v_stack_m48 = v_xmm0;
    v_stack_m50 = *(uint64_t *)(arg1 + 0x38);
    v_stack_m57 = 0;
    v_stack_m54 = 0;
    result = PopAcquireRwLockExclusive(Arg1 + 432, Arg2, Arg3, a4);
    if ((*(uint8_t *)(arg1 + 0x42)) != 0) goto loc_00A4E477;
    if (!sign_flag) goto loc_00A4E3D5;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x38) + 0x30)))) != 0xC000009DULL) goto loc_00A4E543;
loc_00A4E298:
loc_00A4E29B:
    Arg1 = 0;
    if ((*(uint8_t *)(arg1 + 0x45)) != ((uint8_t)(*(uint8_t *)(arg1 + 0x46)))) { Arg1 = (uint32_t)(local_rdi + 1); }
    Arg2 = v_stack_m56;
    if ((*(uint32_t *)(arg1 + 0x50)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x54))))) { Arg2 = (uint32_t)(local_rdi + 1); }
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x40))) == 6) goto loc_00A4E346;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x40))) == 10) goto loc_00A4E612;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x40))) == 7) goto loc_00A4E671;
    if ((uint8_t)(Arg1) != 0) goto loc_00A4E628;
    if ((uint8_t)(Arg2) != 0) goto loc_00A4E645;
    if (((uint32_t)(*(uint8_t *)(arg1 + 0x43))) != ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x419558))))) goto loc_00A4E4BD;
    if ((*(uint8_t *)(arg1 + 0xE4)) != 0) goto loc_00A4E666;
    *(uint8_t *)(arg1 + 0x40) = (uint8_t)(local_rdi + 1);
    if (((*(uint8_t *)(arg1 + 0x41)) & ((uint8_t)(local_rdi + 1))) == 0) goto loc_00A4E31D;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x68))) != 0) goto loc_00A4E45E;
loc_00A4E31D:
    if ((*(uint32_t *)(v_rip + 0x4BE63D)) != 0) goto loc_00A4E68A;
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x68));
    local_r14 = *(uint64_t *)(local_r14);
    if (0 != 0) {
        local_r14 = (*(uint64_t *)(local_r14)) - (0);
        Arg3 = 0;
        Arg2 = local_r14;
        Arg1 = Arg1 + 296;
        result = KeSetTimer2(Arg1, Arg2, Arg3, 0);
    }
    result = IoReuseIrp(*(uint64_t *)(arg1 + 0x38), (uint32_t)(0xC00000BBULL), Arg3, 0);
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0xB8) - 0x48) = 15;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0xB8) - 0x30) = 0x294080ULL;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0xB8) - 0x38) = 92;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0xB8) - 0x40) = 92;
    *(void **)(*(uint64_t *)(arg1 + 0x38) + 0x18) = Arg1 + 112;
loc_00A4E37C:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0xB8) - 0x10) = v_rip - 5883210;
    *(void **)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0xB8) - 0x8) = Arg1;
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0xB8) - 0x45) = 224;
    result = IofCallDriver(*(uint64_t *)(arg1 + 0x30), *(uint64_t *)(arg1 + 0x38), Arg3, 0);
loc_00A4E3A1:
    result = PopReleaseRwLock(Arg1 + 432, *(uint64_t *)(arg1 + 0x38), Arg3, 0);
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(arg1 + 0x38), Arg3, 0);
    return result;
loc_00A4E3D5:
    Arg1 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x40)) - ((uint32_t)(local_rdi + 1)));
    if (condition_is_not_equal) goto loc_00A4E491;
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xF0) = local_r14;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x41))) & (2)) == 0) goto loc_00A4E574;
loc_00A4E3F9:
    result = PopCheckThermalPolicy(*(uint64_t *)(v_stack_m28 + 0x48), local_r14, v_stack_m2F, v_stack_m2C);
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(*(uint64_t *)(v_stack_m28 + 0x48) + 472, Arg2, Arg3, v_stack_m2C);
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x41))) & (4));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xDC)))) >= ((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x90)))) goto loc_00A4E4FB;
    if ((uint8_t)(result) != 0) goto loc_00A4E503;
loc_00A4E45E:
    result = (result) + (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x60));
    if (result > local_r14) goto loc_00A4E46F;
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x70) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xDC)));
    goto loc_00A4E31D;
loc_00A4E46F:
    goto loc_00A4E31D;
loc_00A4E477:
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x40) = (uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xDC)));
loc_00A4E47B:
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(*(uint64_t *)(v_stack_m28 + 0x48) + 448, Arg2, Arg3, v_stack_m2C);
    goto loc_00A4E3A1;
loc_00A4E491:
    Arg1 = (uint32_t)((*(uint64_t *)(v_stack_m28 + 0x48) + 448) - ((uint32_t)((uint32_t)(v_stack_m2C))));
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x43) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x44));
    result = PopDiagTraceThermalCoolingMode(*(uint64_t *)(arg1 + 0x30), *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x44), Arg3, v_stack_m2C);
    if ((*(uint32_t *)(v_rip + 0x419415)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xDC))))) goto loc_00A4E567;
loc_00A4E4B5:
    goto loc_00A4E29B;
loc_00A4E4BD:
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x44) = (uint8_t)(*(uint64_t *)(arg1 + 0x30));
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x40) = 2;
    result = IoReuseIrp(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x38), (uint32_t)(0xC00000BBULL), Arg3, v_stack_m2C);
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x38) + 0xB8) - 0x48) = 15;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x38) + 0xB8) - 0x30) = 0x298084ULL;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x38) + 0xB8) - 0x38) = (uint32_t)((uint32_t)(v_stack_m2C));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x38) + 0x18) = *(uint64_t *)(v_stack_m28 + 0x48) + 68;
    goto loc_00A4E37C;
loc_00A4E4FB:
loc_00A4E503:
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xD8)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x50))))) goto loc_00A4E586;
    Arg1 = (uint8_t)((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x38)) & (1));
    local_rdi = 0;
    if ((uint8_t)(v_stack_m2F) == 0) goto loc_00A4E561;
    if ((uint8_t)(Arg1) == 0) goto loc_00A4E5B7;
loc_00A4E520:
    result = PopCheckAndHandleThermalConditions(*(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)(0xC00000BBULL), Arg3, v_stack_m2C);
    goto loc_00A4E29B;
loc_00A4E543:
    if (((uint32_t)(v_stack_m30)) == 0xC0000120ULL) goto loc_00A4E298;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x40)) == 7) goto loc_00A4E609;
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x40) = 5;
    goto loc_00A4E47B;
loc_00A4E561:
    if ((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x48)) == 0) goto loc_00A4E520;
    goto loc_00A4E5B7;
loc_00A4E567:
    result = PopFireThermalWmiEvent(*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x43), (uint32_t)(0xC00000BBULL), Arg3, v_stack_m2C);
    goto loc_00A4E4B5;
loc_00A4E574:
    result = (uint8_t)((result) | (2));
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x41) = (uint8_t)(result);
    result = PopDiagTraceThermalZoneEnumeration(*(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)(0xC00000BBULL), Arg3, v_stack_m2C);
    goto loc_00A4E3F9;
loc_00A4E586:
    result = PopThermalUpdatePassiveTimeTracking(*(uint64_t *)(v_stack_m28 + 0x48) + 504, *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x50), Arg3, v_stack_m2C);
    local_rbx = (uint32_t)((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x38)) - ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xD8)))));
    v_stack_m2E = 1;
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x54) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xD8)));
    result = PopDiagTraceThermalZoneThrottlePerfTrack((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x80)), (uint32_t)((uint32_t)(local_rbx)), *(uint64_t *)(arg1 + 0x30), v_stack_m2C);
    local_rdi = 0;
loc_00A4E5B7:
    v_stack_m40 = 0;
    result = PopDiagTracePassiveCooling(*(uint64_t *)(v_stack_m28 + 0x48) + 112, *(uint64_t *)(arg1 + 0x30), (uint8_t)(*(uint64_t *)(v_stack_m28 + 0x48) + 432), 1);
    v_stack_m40 = 1;
    result = PopDiagTracePassiveCooling(*(uint64_t *)(v_stack_m28 + 0x48) + 112, *(uint64_t *)(arg1 + 0x30), 1, 1);
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x100) = local_r14;
loc_00A4E609:
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x40) = 1;
    goto loc_00A4E298;
loc_00A4E612:
loc_00A4E628:
    v_stack_m38 = 0;
    v_stack_m40 = 4;
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x40) = 3;
loc_00A4E645:
    v_stack_m38 = 0;
    v_stack_m40 = 4;
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x40) = 4;
loc_00A4E666:
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x40) = 8;
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xD0) = 1;
loc_00A4E671:
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xCC) = 1;
loc_00A4E68A:
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xE8)) + (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xF0));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x0` | `8` | `W` |
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x40` | `8` | `R` |
| `Arg1` | `+ 0x40` | `8` | `W` |
| `Arg1` | `+ 0x41` | `8` | `R` |
| `Arg1` | `+ 0x41` | `8` | `W` |
| `Arg1` | `+ 0x42` | `8` | `R` |
| `Arg1` | `+ 0x43` | `8` | `R` |
| `Arg1` | `+ 0x43` | `8` | `W` |
| `Arg1` | `+ 0x44` | `8` | `R` |
| `Arg1` | `+ 0x44` | `64` | `R` |
| `Arg1` | `+ 0x45` | `8` | `R` |
| `Arg1` | `+ 0x46` | `64` | `R` |
| `Arg1` | `+ 0x50` | `8` | `R` |
| `Arg1` | `+ 0x50` | `32` | `R` |
| `Arg1` | `+ 0x54` | `32` | `R` |
| `Arg1` | `+ 0x54` | `32` | `W` |
| `Arg1` | `+ 0x54` | `64` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x68` | `32` | `R` |
| `Arg1` | `+ 0x70` | `32` | `W` |
| `Arg1` | `+ 0x70` | `64` | `R` |
| `Arg1` | `+ 0x80` | `32` | `R` |
| `Arg1` | `+ 0x90` | `8` | `R` |
| `Arg1` | `+ 0xCC` | `64` | `R` |
| `Arg1` | `+ 0xD0` | `8` | `W` |
| `Arg1` | `+ 0xD8` | `32` | `R` |
| `Arg1` | `+ 0xDC` | `32` | `R` |
| `Arg1` | `+ 0xE4` | `8` | `R` |

추가 오프셋 10개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A4E200&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
