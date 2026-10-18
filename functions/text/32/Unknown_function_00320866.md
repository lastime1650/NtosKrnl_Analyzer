# sub_00320866

- RVA: `0x00320866`–`0x00320E02` (길이 `1,436` bytes)
- VA: `0x0000000140320866`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00075688`
- 디코드: `330`개 명령, `1,436/1,436` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0032094B` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0032095F` → [KeShouldYieldProcessor](../27/KeShouldYieldProcessor_function_002773E0.md) (function, `0x002773E0`)
- `0x00320A14` → [MiAdjustFaultList](../44/MiAdjustFaultList_function_00440240.md) (function, `0x00440240`)
- `0x00320A73` → [MiAccessCheck](MiAccessCheck_function_0032B720.md) (function, `0x0032B720`)
- `0x00320AEA` → [MiResolveDemandZeroFault](../2B/MiResolveDemandZeroFault_function_002B5A40.md) (function, `0x002B5A40`)
- `0x00320B5D` → [MiCheckProtoAccess](MiCheckProtoAccess_function_0032DFE0.md) (function, `0x0032DFE0`)
- `0x00320B90` → [MiResolveTransitionFault](../28/MiResolveTransitionFault_function_00282940.md) (function, `0x00282940`)
- `0x00320C52` → [MiResolvePageFileFault](../36/MiResolvePageFileFault_function_0036D968.md) (function, `0x0036D968`)
- `0x00320CC9` → [KiIsTraceMemoryAccess](../41/KiIsTraceMemoryAccess_function_004184D0.md) (function, `0x004184D0`)
- `0x00320D50` → [MiComputeMaximumFaultCluster](../41/MiComputeMaximumFaultCluster_function_00418210.md) (function, `0x00418210`)
- `0x00320D93` → [KiRspInIstStack](../41/KiRspInIstStack_function_00418504.md) (function, `0x00418504`)
- `0x00320DAA` → [KiRspInIstStack](../41/KiRspInIstStack_function_00418504.md) (function, `0x00418504`)
- `0x00320DD0` → [MiAdvanceFaultList](../36/MiAdvanceFaultList_function_003637A0.md) (function, `0x003637A0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x003208C2` → RVA `0x00E38840` (`.data`; read)
- `0x00320985` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00320AC7` → RVA `0x00FC74C0` (`ALMOSTRO`; read)
- `0x00320CC2` → RVA `0x006BA587` (`ExpInterlockedPopEntrySListFault`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **34**
  - `0x00320871` → [sub_00320540 + 0x250](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x0032087B` → [sub_00320540 + 0x250](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x00320888` → [sub_00320540 + 0x259](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x003208A0` → [sub_00320540 + 0x259](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x003208F6` → [sub_00320540 + 0x259](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x00320959` → [sub_00320540 + 0x259](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x00320966` → [sub_00320540 + 0x259](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x00320980` → [sub_00320540 + 0x156](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x00320990` → [sub_00320540 + 0x182](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x003209AD` → [sub_00320540 + 0x182](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x003209BD` → [sub_00320540 + 0x182](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x003209E8` → [sub_00320540 + 0x182](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x003209F4` → [sub_00320540 + 0x263](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x003209FA` → [sub_00320540 + 0x112](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x00320A0A` → [sub_00320540 + 0x1BF](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x00320A1D` → [sub_00320540 + 0x1BF](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x00320A26` → [sub_00320540 + 0x1B2](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x00320A3E` → [sub_00320540 + 0x1B2](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x00320A7C` → [sub_00320540 + 0x1B2](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x00320A82` → [sub_00320540 + 0x1DD](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x00320AF1` → [sub_00320540 + 0x1DD](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x00320AF9` → [sub_00320540 + 0x1DD](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x00320B50` → [sub_00320540 + 0x1DD](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x00320B97` → [sub_00320540 + 0x1DD](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x00320C59` → [sub_00320540 + 0x1DD](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x00320C90` → [sub_00320540 + 0xE7](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x00320CA0` → [sub_00320540 + 0xE7](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x00320CA6` → [sub_00320540 + 0xCE](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x00320CFA` → [sub_00320540 + 0x1DD](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x00320D43` → [sub_00320540 + 0x259](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x00320D78` → [sub_00320540 + 0x21D](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x00320D82` → [sub_00320540 + 0x1DD](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x00320DDA` → [sub_00320540 + 0x1DD](Unknown_function_00320540.md) (`tail-transfer`)
  - `0x00320DF3` → [sub_00320540 + 0x259](Unknown_function_00320540.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00320866  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
0032086A  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0032086E  80 38 05                        cmp byte ptr [rax], 5
00320871  0F 85 19 FF FF FF               jne 0x140320790
00320877  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
0032087B  E9 10 FF FF FF                  jmp 0x140320790
00320880  8B 87 BC 00 00 00               mov eax, dword ptr [rdi + 0xbc]
00320886  A8 01                           test al, 1
00320888  0F 85 0B FF FF FF               jne 0x140320799
0032088E  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
00320894  A8 40                           test al, 0x40
00320896  0F 85 43 05 00 00               jne 0x140320ddf
0032089C  F6 45 C5 01                     test byte ptr [rbp - 0x3b], 1
003208A0  0F 85 F3 FE FF FF               jne 0x140320799
003208A6  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
003208AC  24 0F                           and al, 0xf
003208AE  3C 05                           cmp al, 5
003208B0  77 4A                           ja 0x1403208fc
003208B2  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
003208B8  24 0F                           and al, 0xf
003208BA  3C 01                           cmp al, 1
003208BC  0F 85 FA 04 00 00               jne 0x140320dbc
003208C2  48 8D 05 77 7F B1 00            lea rax, [rip + 0xb17f77]
003208C9  48 8B 08                        mov rcx, qword ptr [rax]
003208CC  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
003208D5  48 8B 80 38 88 00 00            mov rax, qword ptr [rax + 0x8838]
003208DC  48 85 C0                        test rax, rax
003208DF  0F 84 19 02 00 00               je 0x140320afe
003208E5  8B 80 44 01 00 00               mov eax, dword ptr [rax + 0x144]
003208EB  48 C1 E0 06                     shl rax, 6
003208EF  8B 04 01                        mov eax, dword ptr [rcx + rax]
003208F2  0F BA E0 1E                     bt eax, 0x1e
003208F6  0F 82 9D FE FF FF               jb 0x140320799
003208FC  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00320906  49 8B D7                        mov rdx, r15
00320909  48 C1 EA 09                     shr rdx, 9
0032090D  48 23 D0                        and rdx, rax
00320910  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0032091A  48 8B C0                        mov rax, rax
0032091D  48 03 D0                        add rdx, rax
00320920  49 8B C1                        mov rax, r9
00320923  48 3B D0                        cmp rdx, rax
00320926  0F 84 32 03 00 00               je 0x140320c5e
0032092C  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
00320932  A8 0F                           test al, 0xf
00320934  0F 84 A4 02 00 00               je 0x140320bde
0032093A  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
00320940  A8 0F                           test al, 0xf
00320942  0F 85 54 02 00 00               jne 0x140320b9c
00320948  48 8B CA                        mov rcx, rdx
0032094B  E8 50 1F F6 FF                  call 0x1402828a0
00320950  48 C1 E8 3C                     shr rax, 0x3c
00320954  83 E0 02                        and eax, 2
00320957  85 C0                           test eax, eax
00320959  0F 85 3A FE FF FF               jne 0x140320799
0032095F  E8 7C 6A F5 FF                  call 0x1402773e0
00320964  85 C0                           test eax, eax
00320966  0F 85 2D FE FF FF               jne 0x140320799
0032096C  49 B8 00 D0 BE 7D FB F6 FF FF   movabs r8, 0xfffff6fb7dbed000
00320976  48 B9 F8 D7 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed7f8
00320980  E9 11 FD FF FF                  jmp 0x140320696
00320985  48 F7 05 F8 60 CA 00 00 00 60 00  test qword ptr [rip + 0xca60f8], 0x600000
00320990  0F 84 2C FD FF FF               je 0x1403206c2
00320996  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0032099F  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
003209A6  80 B9 60 01 00 00 01            cmp byte ptr [rcx + 0x160], 1
003209AD  0F 84 0F FD FF FF               je 0x1403206c2
003209B3  48 8B 91 08 05 00 00            mov rdx, qword ptr [rcx + 0x508]
003209BA  48 85 D2                        test rdx, rdx
003209BD  0F 84 FF FC FF FF               je 0x1403206c2
003209C3  49 8B C7                        mov rax, r15
003209C6  48 C1 E8 03                     shr rax, 3
003209CA  25 FF 01 00 00                  and eax, 0x1ff
003209CF  48 8B 04 C2                     mov rax, qword ptr [rdx + rax*8]
003209D3  A8 20                           test al, 0x20
003209D5  74 04                           je 0x1403209db
003209D7  48 83 CB 20                     or rbx, 0x20
003209DB  48 8B CB                        mov rcx, rbx
003209DE  48 83 CB 42                     or rbx, 0x42
003209E2  A8 42                           test al, 0x42
003209E4  48 0F 44 D9                     cmove rbx, rcx
003209E8  E9 D5 FC FF FF                  jmp 0x1403206c2
003209ED  80 65 C5 FB                     and byte ptr [rbp - 0x3b], 0xfb
003209F1  48 85 C0                        test rax, rax
003209F4  0F 84 A9 FD FF FF               je 0x1403207a3
003209FA  E9 53 FC FF FF                  jmp 0x140320652
003209FF  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
00320A03  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00320A07  80 38 02                        cmp byte ptr [rax], 2
00320A0A  0F 85 EF FC FF FF               jne 0x1403206ff
00320A10  48 8D 4D 80                     lea rcx, [rbp - 0x80]
00320A14  E8 27 F8 11 00                  call 0x140440240
00320A19  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
00320A1D  E9 DD FC FF FF                  jmp 0x1403206ff
00320A22  F6 45 C5 10                     test byte ptr [rbp - 0x3b], 0x10
00320A26  0F 84 C6 FC FF FF               je 0x1403206f2
00320A2C  4C 8B CB                        mov r9, rbx
00320A2F  49 C1 E9 05                     shr r9, 5
00320A33  41 83 E1 1F                     and r9d, 0x1f
00320A37  41 81 F9 00 01 00 00            cmp r9d, 0x100
00320A3E  0F 84 AE FC FF FF               je 0x1403206f2
00320A44  41 8B C1                        mov eax, r9d
00320A47  83 E0 F8                        and eax, 0xfffffff8
00320A4A  83 F8 10                        cmp eax, 0x10
00320A4D  0F 84 98 02 00 00               je 0x140320ceb
00320A53  44 8B 45 D0                     mov r8d, dword ptr [rbp - 0x30]
00320A57  48 8B D6                        mov rdx, rsi
00320A5A  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
00320A5E  49 8B CF                        mov rcx, r15
00320A61  41 C1 E8 08                     shr r8d, 8
00320A65  41 80 E0 01                     and r8b, 1
00320A69  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
00320A6E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00320A73  E8 A8 AC 00 00                  call 0x14032b720
00320A78  8B C8                           mov ecx, eax
00320A7A  85 C0                           test eax, eax
00320A7C  0F 84 70 FC FF FF               je 0x1403206f2
00320A82  E9 96 FC FF FF                  jmp 0x14032071d
00320A87  48 0F BA E3 0B                  bt rbx, 0xb
00320A8C  0F 82 E7 00 00 00               jb 0x140320b79
00320A92  0F B6 C3                        movzx eax, bl
00320A95  C0 E8 02                        shr al, 2
00320A98  A8 01                           test al, 1
00320A9A  0F 85 99 01 00 00               jne 0x140320c39
00320AA0  48 8B 75 90                     mov rsi, qword ptr [rbp - 0x70]
00320AA4  F6 C1 01                        test cl, 1
00320AA7  75 5D                           jne 0x140320b06
00320AA9  48 85 F6                        test rsi, rsi
00320AAC  74 2D                           je 0x140320adb
00320AAE  0F B7 86 70 01 00 00            movzx eax, word ptr [rsi + 0x170]
00320AB5  32 D2                           xor dl, dl
00320AB7  66 83 F8 10                     cmp ax, 0x10
00320ABB  0F 84 EA 01 00 00               je 0x140320cab
00320AC1  66 83 F8 33                     cmp ax, 0x33
00320AC5  75 14                           jne 0x140320adb
00320AC7  4C 8B 25 F2 69 CA 00            mov r12, qword ptr [rip + 0xca69f2]
00320ACE  4C 39 A6 68 01 00 00            cmp qword ptr [rsi + 0x168], r12
00320AD5  74 3F                           je 0x140320b16
00320AD7  84 D2                           test dl, dl
00320AD9  75 3B                           jne 0x140320b16
00320ADB  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00320AE0  48 8D 4D 80                     lea rcx, [rbp - 0x80]
00320AE4  45 33 C0                        xor r8d, r8d
00320AE7  49 8B D7                        mov rdx, r15
00320AEA  E8 51 4F F9 FF                  call 0x1402b5a40
00320AEF  8B C8                           mov ecx, eax
00320AF1  E9 27 FC FF FF                  jmp 0x14032071d
00320AF6  41 8B CC                        mov ecx, r12d
00320AF9  E9 1F FC FF FF                  jmp 0x14032071d
00320AFE  41 8B C4                        mov eax, r12d
00320B01  E9 E5 FD FF FF                  jmp 0x1403208eb
00320B06  48 8B C6                        mov rax, rsi
00320B09  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00320B0D  80 38 01                        cmp byte ptr [rax], 1
00320B10  0F 85 E9 01 00 00               jne 0x140320cff
00320B16  F6 C1 01                        test cl, 1
00320B19  74 0D                           je 0x140320b28
00320B1B  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
00320B1F  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00320B23  80 38 06                        cmp byte ptr [rax], 6
00320B26  74 B3                           je 0x140320adb
00320B28  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
00320B32  48 39 45 80                     cmp qword ptr [rbp - 0x80], rax
00320B36  72 A3                           jb 0x140320adb
00320B38  48 C1 EB 05                     shr rbx, 5
00320B3C  83 E3 1F                        and ebx, 0x1f
00320B3F  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
00320B43  83 E3 F8                        and ebx, 0xfffffff8
00320B46  83 FB 10                        cmp ebx, 0x10
00320B49  75 90                           jne 0x140320adb
00320B4B  B9 05 00 00 C0                  mov ecx, 0xc0000005
00320B50  E9 C8 FB FF FF                  jmp 0x14032071d
00320B55  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00320B5A  49 8B CF                        mov rcx, r15
00320B5D  E8 7E D4 00 00                  call 0x14032dfe0
00320B62  48 85 C0                        test rax, rax
00320B65  0F 84 12 02 00 00               je 0x140320d7d
00320B6B  44 8B 4C 24 30                  mov r9d, dword ptr [rsp + 0x30]
00320B70  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00320B74  E9 BE FE FF FF                  jmp 0x140320a37
00320B79  48 8D 44 24 38                  lea rax, [rsp + 0x38]
00320B7E  4C 8B CE                        mov r9, rsi
00320B81  45 33 C0                        xor r8d, r8d
00320B84  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00320B89  49 8B D7                        mov rdx, r15
00320B8C  48 8D 4D 80                     lea rcx, [rbp - 0x80]
00320B90  E8 AB 1D F6 FF                  call 0x140282940
00320B95  8B C8                           mov ecx, eax
00320B97  E9 81 FB FF FF                  jmp 0x14032071d
00320B9C  49 8B C0                        mov rax, r8
00320B9F  48 3B D0                        cmp rdx, rax
00320BA2  0F 82 A0 FD FF FF               jb 0x140320948
00320BA8  49 8B C2                        mov rax, r10
00320BAB  48 3B D0                        cmp rdx, rax
00320BAE  0F 87 94 FD FF FF               ja 0x140320948
00320BB4  49 8B C0                        mov rax, r8
00320BB7  48 2B D0                        sub rdx, rax
00320BBA  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
00320BC0  48 C1 FA 03                     sar rdx, 3
00320BC4  03 D2                           add edx, edx
00320BC6  8B C2                           mov eax, edx
00320BC8  8B CA                           mov ecx, edx
00320BCA  48 C1 E8 05                     shr rax, 5
00320BCE  83 E1 1F                        and ecx, 0x1f
00320BD1  8B 14 83                        mov edx, dword ptr [rbx + rax*4]
00320BD4  D3 EA                           shr edx, cl
00320BD6  F6 C2 02                        test dl, 2
00320BD9  E9 7B FD FF FF                  jmp 0x140320959
00320BDE  49 8B C0                        mov rax, r8
00320BE1  48 3B D0                        cmp rdx, rax
00320BE4  0F 82 50 FD FF FF               jb 0x14032093a
00320BEA  49 8B C2                        mov rax, r10
00320BED  48 3B D0                        cmp rdx, rax
00320BF0  0F 87 44 FD FF FF               ja 0x14032093a
00320BF6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00320BFF  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00320C06  48 8B 81 10 04 00 00            mov rax, qword ptr [rcx + 0x410]
00320C0D  48 8B 88 68 05 00 00            mov rcx, qword ptr [rax + 0x568]
00320C14  48 85 C9                        test rcx, rcx
00320C17  0F 84 1D FD FF FF               je 0x14032093a
00320C1D  C1 EA 03                        shr edx, 3
00320C20  41 8B C4                        mov eax, r12d
00320C23  81 E2 FF 01 00 00               and edx, 0x1ff
00320C29  8B 0C 91                        mov ecx, dword ptr [rcx + rdx*4]
00320C2C  0F BA E1 1E                     bt ecx, 0x1e
00320C30  41 0F 42 C3                     cmovb eax, r11d
00320C34  E9 1E FD FF FF                  jmp 0x140320957
00320C39  F6 45 C5 10                     test byte ptr [rbp - 0x3b], 0x10
00320C3D  0F 85 85 01 00 00               jne 0x140320dc8
00320C43  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
00320C48  45 33 C0                        xor r8d, r8d
00320C4B  49 8B D7                        mov rdx, r15
00320C4E  48 8D 4D 80                     lea rcx, [rbp - 0x80]
00320C52  E8 11 CD 04 00                  call 0x14036d968
00320C57  8B C8                           mov ecx, eax
00320C59  E9 BF FA FF FF                  jmp 0x14032071d
00320C5E  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00320C67  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
00320C6D  24 0F                           and al, 0xf
00320C6F  75 69                           jne 0x140320cda
00320C71  BA 30 00 00 00                  mov edx, 0x30
00320C76  48 8B 84 11 40 9C 00 00         mov rax, qword ptr [rcx + rdx + 0x9c40]
00320C7E  48 85 C0                        test rax, rax
00320C81  E9 D3 FC FF FF                  jmp 0x140320959
00320C86  49 8B C5                        mov rax, r13
00320C89  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00320C8D  80 38 02                        cmp byte ptr [rax], 2
00320C90  0F 84 91 F9 FF FF               je 0x140320627
00320C96  49 8B C5                        mov rax, r13
00320C99  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00320C9D  80 38 01                        cmp byte ptr [rax], 1
00320CA0  0F 84 81 F9 FF FF               je 0x140320627
00320CA6  E9 63 F9 FF FF                  jmp 0x14032060e
00320CAB  F7 86 78 01 00 00 00 02 00 00   test dword ptr [rsi + 0x178], 0x200
00320CB5  0F 84 CC 00 00 00               je 0x140320d87
00320CBB  48 8B 8E 68 01 00 00            mov rcx, qword ptr [rsi + 0x168]
00320CC2  4C 8D 25 BE 98 39 00            lea r12, [rip + 0x3998be]
00320CC9  E8 02 78 0F 00                  call 0x1404184d0
00320CCE  0F B6 4D 90                     movzx ecx, byte ptr [rbp - 0x70]
00320CD2  0F B6 D0                        movzx edx, al
00320CD5  E9 F4 FD FF FF                  jmp 0x140320ace
00320CDA  3C 07                           cmp al, 7
00320CDC  74 43                           je 0x140320d21
00320CDE  3C 05                           cmp al, 5
00320CE0  BA 48 00 00 00                  mov edx, 0x48
00320CE5  49 0F 44 D4                     cmove rdx, r12
00320CE9  EB 8B                           jmp 0x140320c76
00320CEB  F6 45 C5 10                     test byte ptr [rbp - 0x3b], 0x10
00320CEF  0F 84 5E FD FF FF               je 0x140320a53
00320CF5  B9 05 00 00 C0                  mov ecx, 0xc0000005
00320CFA  E9 1E FA FF FF                  jmp 0x14032071d
00320CFF  48 8B C6                        mov rax, rsi
00320D02  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00320D06  80 38 03                        cmp byte ptr [rax], 3
00320D09  0F 84 07 FE FF FF               je 0x140320b16
00320D0F  48 83 E6 FE                     and rsi, 0xfffffffffffffffe
00320D13  80 3E 06                        cmp byte ptr [rsi], 6
00320D16  0F 85 BF FD FF FF               jne 0x140320adb
00320D1C  E9 F5 FD FF FF                  jmp 0x140320b16
00320D21  BA 18 00 00 00                  mov edx, 0x18
00320D26  48 8B 84 11 40 9C 00 00         mov rax, qword ptr [rcx + rdx + 0x9c40]
00320D2E  48 85 C0                        test rax, rax
00320D31  E9 23 FC FF FF                  jmp 0x140320959
00320D36  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
00320D3B  24 FB                           and al, 0xfb
00320D3D  88 45 C5                        mov byte ptr [rbp - 0x3b], al
00320D40  48 3B DA                        cmp rbx, rdx
00320D43  0F 84 50 FA FF FF               je 0x140320799
00320D49  48 2B D3                        sub rdx, rbx
00320D4C  48 8D 4D 80                     lea rcx, [rbp - 0x80]
00320D50  E8 BB 74 0F 00                  call 0x140418210
00320D55  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00320D5A  48 8B C8                        mov rcx, rax
00320D5D  48 83 F8 01                     cmp rax, 1
00320D61  75 0A                           jne 0x140320d6d
00320D63  F6 45 C5 08                     test byte ptr [rbp - 0x3b], 8
00320D67  74 04                           je 0x140320d6d
00320D69  80 65 C5 F7                     and byte ptr [rbp - 0x3b], 0xf7
00320D6D  45 33 E4                        xor r12d, r12d
00320D70  41 8B DC                        mov ebx, r12d
00320D73  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
00320D78  E9 E0 F9 FF FF                  jmp 0x14032075d
00320D7D  B9 05 00 00 C0                  mov ecx, 0xc0000005
00320D82  E9 96 F9 FF FF                  jmp 0x14032071d
00320D87  48 8B 96 80 01 00 00            mov rdx, qword ptr [rsi + 0x180]
00320D8E  B9 03 00 00 00                  mov ecx, 3
00320D93  E8 6C 77 0F 00                  call 0x140418504
00320D98  85 C0                           test eax, eax
00320D9A  0F 85 3B FD FF FF               jne 0x140320adb
00320DA0  48 8B 96 80 01 00 00            mov rdx, qword ptr [rsi + 0x180]
00320DA7  8D 48 02                        lea ecx, [rax + 2]
00320DAA  E8 55 77 0F 00                  call 0x140418504
00320DAF  85 C0                           test eax, eax
00320DB1  0F 85 24 FD FF FF               jne 0x140320adb
00320DB7  E9 FF FE FF FF                  jmp 0x140320cbb
00320DBC  48 8D 87 C0 00 00 00            lea rax, [rdi + 0xc0]
00320DC3  E9 01 FB FF FF                  jmp 0x1403208c9
00320DC8  4D 85 ED                        test r13, r13
00320DCB  74 08                           je 0x140320dd5
00320DCD  49 8B CD                        mov rcx, r13
00320DD0  E8 CB 29 04 00                  call 0x1403637a0
00320DD5  B9 34 04 00 C0                  mov ecx, 0xc0000434
00320DDA  E9 3E F9 FF FF                  jmp 0x14032071d
00320DDF  48 8B 87 80 00 00 00            mov rax, qword ptr [rdi + 0x80]
00320DE6  48 FF C0                        inc rax
00320DE9  48 3B 47 78                     cmp rax, qword ptr [rdi + 0x78]
00320DED  0F 82 A9 FA FF FF               jb 0x14032089c
00320DF3  E9 A1 F9 FF FF                  jmp 0x140320799
00320DF8  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00320DFD  E9 64 FA FF FF                  jmp 0x140320866
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00320866(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;

    result = (*(unsigned __int64 *)(v_rbp - 112)) & (-2);
    *(unsigned __int64 *)(v_rbp - 112) = result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00320866(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    uint64_t v_stack_p20;
    uint8_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;

    result = (*(uint64_t *)(local_rbp - 0x70)) & (-2);
    *(uint64_t *)(local_rbp - 0x70) = result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00320866&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
