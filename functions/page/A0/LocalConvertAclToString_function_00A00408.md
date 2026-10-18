# LocalConvertAclToString

- RVA: `0x00A00408`–`0x00A010B6` (길이 `3,246` bytes)
- VA: `0x0000000140A00408`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A7D8C`
- 디코드: `879`개 명령, `3,246/3,246` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **32**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x00A00484` → [SddlpAlloc](../92/SddlpAlloc_function_00925F88.md) (function, `0x00925F88`)
- `0x00A004D8` → [SddlpAlloc](../92/SddlpAlloc_function_00925F88.md) (function, `0x00925F88`)
- `0x00A004F1` → [SddlpAlloc](../92/SddlpAlloc_function_00925F88.md) (function, `0x00925F88`)
- `0x00A0050E` → [SddlpAlloc](../92/SddlpAlloc_function_00925F88.md) (function, `0x00925F88`)
- `0x00A006DB` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00A00723` → [LocalGetAceCondition](LocalGetAceCondition_function_00A010BC.md) (function, `0x00A010BC`)
- `0x00A00771` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00A0078A` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00A00793` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00A0079C` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00A007A5` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00A007E9` → [SddlpAlloc](../92/SddlpAlloc_function_00925F88.md) (function, `0x00925F88`)
- `0x00A0089A` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (function, `0x005064B0`)
- `0x00A00997` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00A009DF` → [LocalGetAceCondition](LocalGetAceCondition_function_00A010BC.md) (function, `0x00A010BC`)
- `0x00A00A14` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (function, `0x005064B0`)
- `0x00A00A2E` → [ultow_s](../../text/50/ultow_s_function_00504F30.md) (function, `0x00504F30`)
- `0x00A00AB4` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (function, `0x005064B0`)
- `0x00A00B80` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (function, `0x005064B0`)
- `0x00A00C1C` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (function, `0x005064B0`)
- `0x00A00CD0` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (function, `0x005064B0`)
- `0x00A00CFB` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00A00D47` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00A00D8C` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00A00E6E` → [LookupSidInTable](../92/LookupSidInTable_function_009293C0.md) (function, `0x009293C0`)
- `0x00A00ED3` → [LocalConvertSidToStringSidW](LocalConvertSidToStringSidW_function_00A0191C.md) (function, `0x00A0191C`)
- `0x00A00FB5` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (function, `0x005064B0`)
- `0x00A0100D` → [SddlpAlloc](../92/SddlpAlloc_function_00925F88.md) (function, `0x00925F88`)
- `0x00A0102F` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (function, `0x005064B0`)
- `0x00A0103E` → [RtlNtStatusToDosError](../92/RtlNtStatusToDosError_function_00926C40.md) (function, `0x00926C40`)
- `0x00A01075` → [SddlpUuidToString](../7A/SddlpUuidToString_function_007A53F4.md) (function, `0x007A53F4`)
- `0x00A01099` → [SddlpUuidToString](../7A/SddlpUuidToString_function_007A53F4.md) (function, `0x007A53F4`)

### Direct callers
- [LocalConvertSDToStringSD_Rev1](../92/LocalConvertSDToStringSD_Rev1_function_00924428.md) at `0x009248BA`
- [LocalConvertSDToStringSD_Rev1](../92/LocalConvertSDToStringSD_Rev1_function_00924428.md) at `0x009248FE`

### Static image references
- `0x00A00495` → RVA `0x00011C88` (`.rdata`; read)
- `0x00A0049F` → RVA `0x00011C98` (`.rdata`; read)
- `0x00A004AA` → RVA `0x00011CA8` (`.rdata`; read)
- `0x00A00536` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00A0054A` → RVA `0x00E08ABC` (`.data`; read)
- `0x00A005B2` → RVA `0x00E08990` (`.data`; read)
- `0x00A005CF` → RVA `0x00E089A4` (`.data`; read)
- `0x00A00A07` → RVA `0x00014A78` (`.rdata`; read)
- `0x00A00BAF` → RVA `0x00E08C5C` (`.data`; read)
- `0x00A01021` → RVA `0x00011CF4` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x00A0089A` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (`PAGE` → `.text`)
  - `0x00A00A14` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (`PAGE` → `.text`)
  - `0x00A00A2E` → [ultow_s](../../text/50/ultow_s_function_00504F30.md) (`PAGE` → `.text`)
  - `0x00A00AB4` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (`PAGE` → `.text`)
  - `0x00A00B80` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (`PAGE` → `.text`)
  - `0x00A00C1C` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (`PAGE` → `.text`)
  - `0x00A00CD0` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (`PAGE` → `.text`)
  - `0x00A00FB5` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (`PAGE` → `.text`)
  - `0x00A0102F` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **13**
  - `0x00A0063B` → [sub_00B327B6](../B3/Unknown_function_00B327B6.md) (`tail-transfer`)
  - `0x00A0069D` → [sub_00B327B6](../B3/Unknown_function_00B327B6.md) (`tail-transfer`)
  - `0x00A006A6` → [sub_00B327B6](../B3/Unknown_function_00B327B6.md) (`tail-transfer`)
  - `0x00A006AF` → [sub_00B327B6](../B3/Unknown_function_00B327B6.md) (`tail-transfer`)
  - `0x00A006BA` → [sub_00B327B6](../B3/Unknown_function_00B327B6.md) (`tail-transfer`)
  - `0x00A00919` → [sub_00B327B6 + 0x79](../B3/Unknown_function_00B327B6.md) (`tail-transfer`)
  - `0x00A00966` → [sub_00B327B6 + 0x79](../B3/Unknown_function_00B327B6.md) (`tail-transfer`)
  - `0x00A0096F` → [sub_00B327B6 + 0x79](../B3/Unknown_function_00B327B6.md) (`tail-transfer`)
  - `0x00A00978` → [sub_00B327B6 + 0x79](../B3/Unknown_function_00B327B6.md) (`tail-transfer`)
  - `0x00A00981` → [sub_00B327B6 + 0x79](../B3/Unknown_function_00B327B6.md) (`tail-transfer`)
  - `0x00A0101B` → [sub_00B327B6 + 0x71](../B3/Unknown_function_00B327B6.md) (`tail-transfer`)
  - `0x00A0108D` → [sub_00B327B6 + 0xE8](../B3/Unknown_function_00B327B6.md) (`tail-transfer`)
  - `0x00A010B1` → [sub_00B327B6 + 0x119](../B3/Unknown_function_00B327B6.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A00408  48 8B C4                        mov rax, rsp
00A0040B  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00A0040F  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
00A00413  48 89 48 08                     mov qword ptr [rax + 8], rcx
00A00417  55                              push rbp
00A00418  56                              push rsi
00A00419  57                              push rdi
00A0041A  41 54                           push r12
00A0041C  41 55                           push r13
00A0041E  41 56                           push r14
00A00420  41 57                           push r15
00A00422  48 8D 68 C1                     lea rbp, [rax - 0x3f]
00A00426  48 81 EC B0 00 00 00            sub rsp, 0xb0
00A0042D  45 33 ED                        xor r13d, r13d
00A00430  49 8B D9                        mov rbx, r9
00A00433  44 89 6D A7                     mov dword ptr [rbp - 0x59], r13d
00A00437  48 8B F1                        mov rsi, rcx
00A0043A  44 89 6D EF                     mov dword ptr [rbp - 0x11], r13d
00A0043E  41 8B FD                        mov edi, r13d
00A00441  4C 89 6D CF                     mov qword ptr [rbp - 0x31], r13
00A00445  45 8B E5                        mov r12d, r13d
00A00448  44 89 6D AB                     mov dword ptr [rbp - 0x55], r13d
00A0044C  4C 89 6D C7                     mov qword ptr [rbp - 0x39], r13
00A00450  4C 89 6D D7                     mov qword ptr [rbp - 0x29], r13
00A00454  4C 89 6D BF                     mov qword ptr [rbp - 0x41], r13
00A00458  4D 85 C9                        test r9, r9
00A0045B  0F 84 1E 09 00 00               je 0x140a00d7f
00A00461  4C 8B 75 67                     mov r14, qword ptr [rbp + 0x67]
00A00465  4D 85 F6                        test r14, r14
00A00468  0F 84 11 09 00 00               je 0x140a00d7f
00A0046E  84 D2                           test dl, dl
00A00470  0F 84 53 0B 00 00               je 0x140a00fc9
00A00476  48 85 C9                        test rcx, rcx
00A00479  75 3F                           jne 0x140a004ba
00A0047B  8D 4E 24                        lea ecx, [rsi + 0x24]
00A0047E  4D 89 29                        mov qword ptr [r9], r13
00A00481  41 89 0E                        mov dword ptr [r14], ecx
00A00484  E8 FF 5A F2 FF                  call 0x140925f88
00A00489  48 89 03                        mov qword ptr [rbx], rax
00A0048C  48 85 C0                        test rax, rax
00A0048F  0F 84 C5 08 00 00               je 0x140a00d5a
00A00495  0F 10 05 EC 17 61 FF            movups xmm0, xmmword ptr [rip - 0x9ee814]
00A0049C  0F 11 00                        movups xmmword ptr [rax], xmm0
00A0049F  0F 10 0D F2 17 61 FF            movups xmm1, xmmword ptr [rip - 0x9ee80e]
00A004A6  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
00A004AA  8B 0D F8 17 61 FF               mov ecx, dword ptr [rip - 0x9ee808]
00A004B0  89 48 20                        mov dword ptr [rax + 0x20], ecx
00A004B3  33 C0                           xor eax, eax
00A004B5  E9 03 03 00 00                  jmp 0x140a007bd
00A004BA  0F B7 41 04                     movzx eax, word ptr [rcx + 4]
00A004BE  66 85 C0                        test ax, ax
00A004C1  0F 84 23 08 00 00               je 0x140a00cea
00A004C7  41 F6 D8                        neg r8b
00A004CA  8B C8                           mov ecx, eax
00A004CC  1B DB                           sbb ebx, ebx
00A004CE  48 C1 E1 03                     shl rcx, 3
00A004D2  83 C3 02                        add ebx, 2
00A004D5  89 5D 7F                        mov dword ptr [rbp + 0x7f], ebx
00A004D8  E8 AB 5A F2 FF                  call 0x140925f88
00A004DD  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
00A004E1  4C 8B F0                        mov r14, rax
00A004E4  48 85 C0                        test rax, rax
00A004E7  0F 84 13 08 00 00               je 0x140a00d00
00A004ED  0F B7 4E 04                     movzx ecx, word ptr [rsi + 4]
00A004F1  E8 92 5A F2 FF                  call 0x140925f88
00A004F6  48 89 45 FF                     mov qword ptr [rbp - 1], rax
00A004FA  4C 8B F8                        mov r15, rax
00A004FD  48 85 C0                        test rax, rax
00A00500  0F 84 F2 07 00 00               je 0x140a00cf8
00A00506  0F B7 4E 04                     movzx ecx, word ptr [rsi + 4]
00A0050A  48 C1 E1 02                     shl rcx, 2
00A0050E  E8 75 5A F2 FF                  call 0x140925f88
00A00513  45 33 DB                        xor r11d, r11d
00A00516  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
00A0051A  48 85 C0                        test rax, rax
00A0051D  0F 84 66 08 00 00               je 0x140a00d89
00A00523  4C 8D 76 08                     lea r14, [rsi + 8]
00A00527  44 89 5D B3                     mov dword ptr [rbp - 0x4d], r11d
00A0052B  45 8B FB                        mov r15d, r11d
00A0052E  45 8D 6B 08                     lea r13d, [r11 + 8]
00A00532  0F B7 46 04                     movzx eax, word ptr [rsi + 4]
00A00536  4C 8D 05 C3 FA 5F FF            lea r8, [rip - 0xa0053d]
00A0053D  44 3B F8                        cmp r15d, eax
00A00540  0F 83 21 01 00 00               jae 0x140a00667
00A00546  41 0F B6 36                     movzx esi, byte ptr [r14]
00A0054A  48 8D 0D 6B 85 40 00            lea rcx, [rip + 0x40856b]
00A00551  41 83 C4 02                     add r12d, 2
00A00555  41 8B D3                        mov edx, r11d
00A00558  44 89 65 A7                     mov dword ptr [rbp - 0x59], r12d
00A0055C  8B 41 04                        mov eax, dword ptr [rcx + 4]
00A0055F  23 C3                           and eax, ebx
00A00561  3B C3                           cmp eax, ebx
00A00563  75 04                           jne 0x140a00569
00A00565  3B 31                           cmp esi, dword ptr [rcx]
00A00567  74 0B                           je 0x140a00574
00A00569  FF C2                           inc edx
00A0056B  48 83 C1 18                     add rcx, 0x18
00A0056F  83 FA 11                        cmp edx, 0x11
00A00572  72 E8                           jb 0x140a0055c
00A00574  83 FA 11                        cmp edx, 0x11
00A00577  0F 83 E5 00 00 00               jae 0x140a00662
00A0057D  8B C2                           mov eax, edx
00A0057F  48 8D 0C 40                     lea rcx, [rax + rax*2]
00A00583  48 8D 04 CD B0 8A E0 00         lea rax, [rcx*8 + 0xe08ab0]
00A0058B  49 03 C0                        add rax, r8
00A0058E  0F 84 CE 00 00 00               je 0x140a00662
00A00594  48 8B 08                        mov rcx, qword ptr [rax]
00A00597  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A0059B  48 FF C0                        inc rax
00A0059E  66 44 39 1C 41                  cmp word ptr [rcx + rax*2], r11w
00A005A3  75 F6                           jne 0x140a0059b
00A005A5  41 0F B6 7E 01                  movzx edi, byte ptr [r14 + 1]
00A005AA  45 8D 24 44                     lea r12d, [r12 + rax*2]
00A005AE  41 83 C4 02                     add r12d, 2
00A005B2  4C 8D 3D D7 83 40 00            lea r15, [rip + 0x4083d7]
00A005B9  41 8B DB                        mov ebx, r11d
00A005BC  8B CB                           mov ecx, ebx
00A005BE  41 BB 01 00 00 00               mov r11d, 1
00A005C4  41 D3 E3                        shl r11d, cl
00A005C7  41 85 FB                        test r11d, edi
00A005CA  74 40                           je 0x140a0060c
00A005CC  8B 4D 7F                        mov ecx, dword ptr [rbp + 0x7f]
00A005CF  4C 8D 05 CE 83 40 00            lea r8, [rip + 0x4083ce]
00A005D6  33 D2                           xor edx, edx
00A005D8  44 8B D2                        mov r10d, edx
00A005DB  41 8B 40 FC                     mov eax, dword ptr [r8 - 4]
00A005DF  23 C1                           and eax, ecx
00A005E1  3B C1                           cmp eax, ecx
00A005E3  75 16                           jne 0x140a005fb
00A005E5  45 8B 08                        mov r9d, dword ptr [r8]
00A005E8  45 85 C9                        test r9d, r9d
00A005EB  0F 85 19 07 00 00               jne 0x140a00d0a
00A005F1  45 3B 58 F8                     cmp r11d, dword ptr [r8 - 8]
00A005F5  0F 84 F3 08 00 00               je 0x140a00eee
00A005FB  41 FF C2                        inc r10d
00A005FE  49 83 C0 20                     add r8, 0x20
00A00602  41 83 FA 09                     cmp r10d, 9
00A00606  0F 82 C8 09 00 00               jb 0x140a00fd4
00A0060C  45 33 DB                        xor r11d, r11d
00A0060F  FF C3                           inc ebx
00A00611  41 3B DD                        cmp ebx, r13d
00A00614  72 A6                           jb 0x140a005bc
00A00616  41 0F B6 0E                     movzx ecx, byte ptr [r14]
00A0061A  41 83 C4 02                     add r12d, 2
00A0061E  44 8B 7D B3                     mov r15d, dword ptr [rbp - 0x4d]
00A00622  44 89 65 A7                     mov dword ptr [rbp - 0x59], r12d
00A00626  44 89 65 AF                     mov dword ptr [rbp - 0x51], r12d
00A0062A  83 F9 09                        cmp ecx, 9
00A0062D  76 56                           jbe 0x140a00685
00A0062F  83 E9 0A                        sub ecx, 0xa
00A00632  0F 84 87 00 00 00               je 0x140a006bf
00A00638  83 E9 01                        sub ecx, 1
00A0063B  0F 84 75 21 13 00               je 0x140b327b6
00A00641  83 E9 02                        sub ecx, 2
00A00644  74 79                           je 0x140a006bf
00A00646  83 E9 04                        sub ecx, 4
00A00649  74 74                           je 0x140a006bf
00A0064B  83 E9 01                        sub ecx, 1
00A0064E  74 6F                           je 0x140a006bf
00A00650  83 E9 01                        sub ecx, 1
00A00653  74 6A                           je 0x140a006bf
00A00655  83 E9 01                        sub ecx, 1
00A00658  74 65                           je 0x140a006bf
00A0065A  83 F9 01                        cmp ecx, 1
00A0065D  74 60                           je 0x140a006bf
00A0065F  8B 5D 7F                        mov ebx, dword ptr [rbp + 0x7f]
00A00662  BF 38 05 00 00                  mov edi, 0x538
00A00667  45 85 E4                        test r12d, r12d
00A0066A  0F 84 E0 09 00 00               je 0x140a01050
00A00670  85 FF                           test edi, edi
00A00672  0F 84 61 01 00 00               je 0x140a007d9
00A00678  4C 8B 7D 5F                     mov r15, qword ptr [rbp + 0x5f]
00A0067C  4C 8B 6D B7                     mov r13, qword ptr [rbp - 0x49]
00A00680  E9 CD 00 00 00                  jmp 0x140a00752
00A00685  74 38                           je 0x140a006bf
00A00687  85 C9                           test ecx, ecx
00A00689  74 34                           je 0x140a006bf
00A0068B  83 E9 01                        sub ecx, 1
00A0068E  74 2F                           je 0x140a006bf
00A00690  83 E9 01                        sub ecx, 1
00A00693  74 2A                           je 0x140a006bf
00A00695  83 E9 01                        sub ecx, 1
00A00698  74 25                           je 0x140a006bf
00A0069A  83 E9 02                        sub ecx, 2
00A0069D  0F 84 13 21 13 00               je 0x140b327b6
00A006A3  83 E9 01                        sub ecx, 1
00A006A6  0F 84 0A 21 13 00               je 0x140b327b6
00A006AC  83 E9 01                        sub ecx, 1
00A006AF  0F 84 01 21 13 00               je 0x140b327b6
00A006B5  83 F9 01                        cmp ecx, 1
00A006B8  75 A5                           jne 0x140a0065f
00A006BA  E9 F7 20 13 00                  jmp 0x140b327b6
00A006BF  45 8B 66 04                     mov r12d, dword ptr [r14 + 4]
00A006C3  49 8D 76 08                     lea rsi, [r14 + 8]
00A006C7  48 89 75 C7                     mov qword ptr [rbp - 0x39], rsi
00A006CB  44 89 65 AB                     mov dword ptr [rbp - 0x55], r12d
00A006CF  48 8B 5D BF                     mov rbx, qword ptr [rbp - 0x41]
00A006D3  48 85 DB                        test rbx, rbx
00A006D6  74 0F                           je 0x140a006e7
00A006D8  48 8B CB                        mov rcx, rbx
00A006DB  E8 24 1D ED FF                  call 0x1408d2404
00A006E0  45 33 DB                        xor r11d, r11d
00A006E3  4C 89 5D BF                     mov qword ptr [rbp - 0x41], r11
00A006E7  8A 85 87 00 00 00               mov al, byte ptr [rbp + 0x87]
00A006ED  4C 8D 4D B3                     lea r9, [rbp - 0x4d]
00A006F1  88 44 24 40                     mov byte ptr [rsp + 0x40], al
00A006F5  4C 8D 45 BF                     lea r8, [rbp - 0x41]
00A006F9  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
00A006FD  48 8B D6                        mov rdx, rsi
00A00700  4C 89 5C 24 38                  mov qword ptr [rsp + 0x38], r11
00A00705  49 8B CE                        mov rcx, r14
00A00708  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A0070D  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
00A00711  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A00716  48 8D 45 AF                     lea rax, [rbp - 0x51]
00A0071A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A0071F  44 89 5D B3                     mov dword ptr [rbp - 0x4d], r11d
00A00723  E8 94 09 00 00                  call 0x140a010bc
00A00728  45 33 DB                        xor r11d, r11d
00A0072B  8B F8                           mov edi, eax
00A0072D  85 C0                           test eax, eax
00A0072F  0F 84 A6 08 00 00               je 0x140a00fdb
00A00735  44 8B 65 AF                     mov r12d, dword ptr [rbp - 0x51]
00A00739  44 89 65 A7                     mov dword ptr [rbp - 0x59], r12d
00A0073D  8B 5D 7F                        mov ebx, dword ptr [rbp + 0x7f]
00A00740  E9 22 FF FF FF                  jmp 0x140a00667
00A00745  44 8B 65 A7                     mov r12d, dword ptr [rbp - 0x59]
00A00749  BF 38 05 00 00                  mov edi, 0x538
00A0074E  4C 8B 7D 5F                     mov r15, qword ptr [rbp + 0x5f]
00A00752  48 8B 75 47                     mov rsi, qword ptr [rbp + 0x47]
00A00756  41 8B DB                        mov ebx, r11d
00A00759  66 44 3B 5E 04                  cmp r11w, word ptr [rsi + 4]
00A0075E  73 27                           jae 0x140a00787
00A00760  4C 8B 7D FF                     mov r15, qword ptr [rbp - 1]
00A00764  8B CB                           mov ecx, ebx
00A00766  46 38 1C 39                     cmp byte ptr [rcx + r15], r11b
00A0076A  74 0D                           je 0x140a00779
00A0076C  49 8B 4C CD 00                  mov rcx, qword ptr [r13 + rcx*8]
00A00771  E8 8E 1C ED FF                  call 0x1408d2404
00A00776  45 33 DB                        xor r11d, r11d
00A00779  0F B7 46 04                     movzx eax, word ptr [rsi + 4]
00A0077D  FF C3                           inc ebx
00A0077F  3B D8                           cmp ebx, eax
00A00781  72 E1                           jb 0x140a00764
00A00783  4C 8B 7D 5F                     mov r15, qword ptr [rbp + 0x5f]
00A00787  49 8B CD                        mov rcx, r13
00A0078A  E8 75 1C ED FF                  call 0x1408d2404
00A0078F  48 8B 4D FF                     mov rcx, qword ptr [rbp - 1]
00A00793  E8 6C 1C ED FF                  call 0x1408d2404
00A00798  48 8B 4D E7                     mov rcx, qword ptr [rbp - 0x19]
00A0079C  E8 63 1C ED FF                  call 0x1408d2404
00A007A1  48 8B 4D BF                     mov rcx, qword ptr [rbp - 0x41]
00A007A5  E8 5A 1C ED FF                  call 0x1408d2404
00A007AA  33 DB                           xor ebx, ebx
00A007AC  85 FF                           test edi, edi
00A007AE  0F 85 90 05 00 00               jne 0x140a00d44
00A007B4  48 8B 45 67                     mov rax, qword ptr [rbp + 0x67]
00A007B8  44 89 20                        mov dword ptr [rax], r12d
00A007BB  8B C7                           mov eax, edi
00A007BD  48 8B 9C 24 F8 00 00 00         mov rbx, qword ptr [rsp + 0xf8]
00A007C5  48 81 C4 B0 00 00 00            add rsp, 0xb0
00A007CC  41 5F                           pop r15
00A007CE  41 5E                           pop r14
00A007D0  41 5D                           pop r13
00A007D2  41 5C                           pop r12
00A007D4  5F                              pop rdi
00A007D5  5E                              pop rsi
00A007D6  5D                              pop rbp
00A007D7  C3                              ret
00A007D8  CC                              int3
00A007D9  41 F6 C4 01                     test r12b, 1
00A007DD  0F 85 77 08 00 00               jne 0x140a0105a
00A007E3  41 8B CC                        mov ecx, r12d
00A007E6  41 8B F4                        mov esi, r12d
00A007E9  E8 9A 57 F2 FF                  call 0x140925f88
00A007EE  4C 8B 7D 5F                     mov r15, qword ptr [rbp + 0x5f]
00A007F2  45 33 DB                        xor r11d, r11d
00A007F5  4C 8B F0                        mov r14, rax
00A007F8  49 89 07                        mov qword ptr [r15], rax
00A007FB  48 85 C0                        test rax, rax
00A007FE  0F 84 62 08 00 00               je 0x140a01066
00A00804  48 8B 45 47                     mov rax, qword ptr [rbp + 0x47]
00A00808  45 8B E3                        mov r12d, r11d
00A0080B  48 D1 EE                        shr rsi, 1
00A0080E  44 89 5D AF                     mov dword ptr [rbp - 0x51], r11d
00A00812  4C 8D 78 08                     lea r15, [rax + 8]
00A00816  0F B7 40 04                     movzx eax, word ptr [rax + 4]
00A0081A  41 B9 3B 00 00 00               mov r9d, 0x3b
00A00820  4C 89 7D D7                     mov qword ptr [rbp - 0x29], r15
00A00824  44 3B E0                        cmp r12d, eax
00A00827  0F 83 39 05 00 00               jae 0x140a00d66
00A0082D  48 85 F6                        test rsi, rsi
00A00830  0F 84 2B 05 00 00               je 0x140a00d61
00A00836  66 41 C7 06 28 00               mov word ptr [r14], 0x28
00A0083C  45 8D 61 C6                     lea r12d, [r9 - 0x3a]
00A00840  45 0F B6 07                     movzx r8d, byte ptr [r15]
00A00844  48 8D 15 71 82 40 00            lea rdx, [rip + 0x408271]
00A0084B  49 83 C6 02                     add r14, 2
00A0084F  41 8B CB                        mov ecx, r11d
00A00852  49 2B F4                        sub rsi, r12
00A00855  8B 42 04                        mov eax, dword ptr [rdx + 4]
00A00858  23 C3                           and eax, ebx
00A0085A  3B C3                           cmp eax, ebx
00A0085C  75 05                           jne 0x140a00863
00A0085E  44 3B 02                        cmp r8d, dword ptr [rdx]
00A00861  74 0C                           je 0x140a0086f
00A00863  41 03 CC                        add ecx, r12d
00A00866  48 83 C2 18                     add rdx, 0x18
00A0086A  83 F9 11                        cmp ecx, 0x11
00A0086D  72 E6                           jb 0x140a00855
00A0086F  83 F9 11                        cmp ecx, 0x11
00A00872  73 3C                           jae 0x140a008b0
00A00874  8B C1                           mov eax, ecx
00A00876  48 8D 0C 40                     lea rcx, [rax + rax*2]
00A0087A  48 8D 05 7F F7 5F FF            lea rax, [rip - 0xa00881]
00A00881  48 8D 98 B0 8A E0 00            lea rbx, [rax + 0xe08ab0]
00A00888  48 8D 1C CB                     lea rbx, [rbx + rcx*8]
00A0088C  48 85 DB                        test rbx, rbx
00A0088F  74 1F                           je 0x140a008b0
00A00891  4C 8B 03                        mov r8, qword ptr [rbx]
00A00894  48 8B D6                        mov rdx, rsi
00A00897  49 8B CE                        mov rcx, r14
00A0089A  E8 11 5C B0 FF                  call 0x1405064b0
00A0089F  8B 43 08                        mov eax, dword ptr [rbx + 8]
00A008A2  48 2B F0                        sub rsi, rax
00A008A5  45 33 DB                        xor r11d, r11d
00A008A8  4D 8D 34 46                     lea r14, [r14 + rax*2]
00A008AC  45 8D 4B 3B                     lea r9d, [r11 + 0x3b]
00A008B0  48 85 F6                        test rsi, rsi
00A008B3  0F 84 A8 04 00 00               je 0x140a00d61
00A008B9  66 45 89 0E                     mov word ptr [r14], r9w
00A008BD  41 8B FB                        mov edi, r11d
00A008C0  49 83 C6 02                     add r14, 2
00A008C4  49 2B F4                        sub rsi, r12
00A008C7  8B CF                           mov ecx, edi
00A008C9  45 8B DC                        mov r11d, r12d
00A008CC  41 D3 E3                        shl r11d, cl
00A008CF  45 84 5F 01                     test byte ptr [r15 + 1], r11b
00A008D3  0F 85 41 02 00 00               jne 0x140a00b1a
00A008D9  45 33 DB                        xor r11d, r11d
00A008DC  41 03 FC                        add edi, r12d
00A008DF  41 3B FD                        cmp edi, r13d
00A008E2  72 E3                           jb 0x140a008c7
00A008E4  48 85 F6                        test rsi, rsi
00A008E7  0F 84 74 04 00 00               je 0x140a00d61
00A008ED  66 41 C7 06 3B 00               mov word ptr [r14], 0x3b
00A008F3  49 2B F4                        sub rsi, r12
00A008F6  41 0F B6 0F                     movzx ecx, byte ptr [r15]
00A008FA  49 83 C6 02                     add r14, 2
00A008FE  4C 89 5D F7                     mov qword ptr [rbp - 9], r11
00A00902  4D 8B E3                        mov r12, r11
00A00905  4C 89 5D DF                     mov qword ptr [rbp - 0x21], r11
00A00909  4D 8B EB                        mov r13, r11
00A0090C  83 F9 09                        cmp ecx, 9
00A0090F  76 3D                           jbe 0x140a0094e
00A00911  83 E9 0A                        sub ecx, 0xa
00A00914  74 27                           je 0x140a0093d
00A00916  83 E9 01                        sub ecx, 1
00A00919  0F 84 10 1F 13 00               je 0x140b3282f
00A0091F  83 E9 02                        sub ecx, 2
00A00922  74 19                           je 0x140a0093d
00A00924  83 E9 04                        sub ecx, 4
00A00927  74 14                           je 0x140a0093d
00A00929  83 E9 01                        sub ecx, 1
00A0092C  74 0F                           je 0x140a0093d
00A0092E  83 E9 01                        sub ecx, 1
00A00931  74 0A                           je 0x140a0093d
00A00933  83 E9 01                        sub ecx, 1
00A00936  74 05                           je 0x140a0093d
00A00938  83 F9 01                        cmp ecx, 1
00A0093B  75 4A                           jne 0x140a00987
00A0093D  41 8B 47 04                     mov eax, dword ptr [r15 + 4]
00A00941  49 8D 7F 08                     lea rdi, [r15 + 8]
00A00945  48 89 7D C7                     mov qword ptr [rbp - 0x39], rdi
00A00949  89 45 AB                        mov dword ptr [rbp - 0x55], eax
00A0094C  EB 3D                           jmp 0x140a0098b
00A0094E  74 ED                           je 0x140a0093d
00A00950  85 C9                           test ecx, ecx
00A00952  74 E9                           je 0x140a0093d
00A00954  83 E9 01                        sub ecx, 1
00A00957  74 E4                           je 0x140a0093d
00A00959  83 E9 01                        sub ecx, 1
00A0095C  74 DF                           je 0x140a0093d
00A0095E  83 E9 01                        sub ecx, 1
00A00961  74 DA                           je 0x140a0093d
00A00963  83 E9 02                        sub ecx, 2
00A00966  0F 84 C3 1E 13 00               je 0x140b3282f
00A0096C  83 E9 01                        sub ecx, 1
00A0096F  0F 84 BA 1E 13 00               je 0x140b3282f
00A00975  83 E9 01                        sub ecx, 1
00A00978  0F 84 B1 1E 13 00               je 0x140b3282f
00A0097E  83 F9 01                        cmp ecx, 1
00A00981  0F 84 A8 1E 13 00               je 0x140b3282f
00A00987  48 8B 7D C7                     mov rdi, qword ptr [rbp - 0x39]
00A0098B  48 8B 5D BF                     mov rbx, qword ptr [rbp - 0x41]
00A0098F  48 85 DB                        test rbx, rbx
00A00992  74 0F                           je 0x140a009a3
00A00994  48 8B CB                        mov rcx, rbx
00A00997  E8 68 1A ED FF                  call 0x1408d2404
00A0099C  45 33 DB                        xor r11d, r11d
00A0099F  4C 89 5D BF                     mov qword ptr [rbp - 0x41], r11
00A009A3  8A 85 87 00 00 00               mov al, byte ptr [rbp + 0x87]
00A009A9  4C 8D 4D B3                     lea r9, [rbp - 0x4d]
00A009AD  88 44 24 40                     mov byte ptr [rsp + 0x40], al
00A009B1  4C 8D 45 BF                     lea r8, [rbp - 0x41]
00A009B5  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
00A009B9  48 8B D7                        mov rdx, rdi
00A009BC  4C 89 5C 24 38                  mov qword ptr [rsp + 0x38], r11
00A009C1  49 8B CF                        mov rcx, r15
00A009C4  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A009C9  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
00A009CD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A009D2  48 8D 45 EF                     lea rax, [rbp - 0x11]
00A009D6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A009DB  44 89 5D B3                     mov dword ptr [rbp - 0x4d], r11d
00A009DF  E8 D8 06 00 00                  call 0x140a010bc
00A009E4  45 33 DB                        xor r11d, r11d
00A009E7  89 45 B3                        mov dword ptr [rbp - 0x4d], eax
00A009EA  8B F8                           mov edi, eax
00A009EC  85 C0                           test eax, eax
00A009EE  0F 85 72 03 00 00               jne 0x140a00d66
00A009F4  8B 4D AF                        mov ecx, dword ptr [rbp - 0x51]
00A009F7  48 8B 45 E7                     mov rax, qword ptr [rbp - 0x19]
00A009FB  8B 04 88                        mov eax, dword ptr [rax + rcx*4]
00A009FE  83 F8 02                        cmp eax, 2
00A00A01  0F 85 9B 01 00 00               jne 0x140a00ba2
00A00A07  4C 8D 05 6A 40 61 FF            lea r8, [rip - 0x9ebf96]
00A00A0E  48 8B D6                        mov rdx, rsi
00A00A11  49 8B CE                        mov rcx, r14
00A00A14  E8 97 5A B0 FF                  call 0x1405064b0
00A00A19  8B 4D AB                        mov ecx, dword ptr [rbp - 0x55]
00A00A1C  44 8D 4F 10                     lea r9d, [rdi + 0x10]
00A00A20  49 83 C6 04                     add r14, 4
00A00A24  48 83 EE 02                     sub rsi, 2
00A00A28  4C 8B C6                        mov r8, rsi
00A00A2B  49 8B D6                        mov rdx, r14
00A00A2E  E8 FD 44 B0 FF                  call 0x140504f30
00A00A33  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A00A37  45 33 DB                        xor r11d, r11d
00A00A3A  48 FF C0                        inc rax
00A00A3D  66 45 39 1C 46                  cmp word ptr [r14 + rax*2], r11w
00A00A42  75 F6                           jne 0x140a00a3a
00A00A44  4D 8D 34 46                     lea r14, [r14 + rax*2]
00A00A48  48 2B F0                        sub rsi, rax
00A00A4B  48 85 F6                        test rsi, rsi
00A00A4E  0F 84 0D 03 00 00               je 0x140a00d61
00A00A54  B8 3B 00 00 00                  mov eax, 0x3b
00A00A59  48 FF CE                        dec rsi
00A00A5C  66 41 89 06                     mov word ptr [r14], ax
00A00A60  49 83 C6 02                     add r14, 2
00A00A64  4D 85 E4                        test r12, r12
00A00A67  0F 85 01 06 00 00               jne 0x140a0106e
00A00A6D  48 85 F6                        test rsi, rsi
00A00A70  0F 84 EB 02 00 00               je 0x140a00d61
00A00A76  66 41 89 06                     mov word ptr [r14], ax
00A00A7A  48 FF CE                        dec rsi
00A00A7D  49 83 C6 02                     add r14, 2
00A00A81  4D 85 ED                        test r13, r13
00A00A84  0F 85 08 06 00 00               jne 0x140a01092
00A00A8A  4C 8B 6D B7                     mov r13, qword ptr [rbp - 0x49]
00A00A8E  48 85 F6                        test rsi, rsi
00A00A91  0F 84 AE FC FF FF               je 0x140a00745
00A00A97  44 8B 65 AF                     mov r12d, dword ptr [rbp - 0x51]
00A00A9B  48 FF CE                        dec rsi
00A00A9E  66 41 89 06                     mov word ptr [r14], ax
00A00AA2  48 8B D6                        mov rdx, rsi
00A00AA5  49 83 C6 02                     add r14, 2
00A00AA9  49 8B CE                        mov rcx, r14
00A00AAC  4B 8B 5C E5 00                  mov rbx, qword ptr [r13 + r12*8]
00A00AB1  4C 8B C3                        mov r8, rbx
00A00AB4  E8 F7 59 B0 FF                  call 0x1405064b0
00A00AB9  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A00ABD  45 33 DB                        xor r11d, r11d
00A00AC0  48 FF C0                        inc rax
00A00AC3  66 44 39 1C 43                  cmp word ptr [rbx + rax*2], r11w
00A00AC8  75 F6                           jne 0x140a00ac0
00A00ACA  48 8B 5D BF                     mov rbx, qword ptr [rbp - 0x41]
00A00ACE  4D 8D 34 46                     lea r14, [r14 + rax*2]
00A00AD2  48 2B F0                        sub rsi, rax
00A00AD5  48 85 DB                        test rbx, rbx
00A00AD8  0F 85 83 00 00 00               jne 0x140a00b61
00A00ADE  48 83 FE 01                     cmp rsi, 1
00A00AE2  0F 86 5D FC FF FF               jbe 0x140a00745
00A00AE8  8B 5D 7F                        mov ebx, dword ptr [rbp + 0x7f]
00A00AEB  41 FF C4                        inc r12d
00A00AEE  66 41 C7 06 29 00               mov word ptr [r14], 0x29
00A00AF4  48 FF CE                        dec rsi
00A00AF7  49 83 C6 02                     add r14, 2
00A00AFB  44 89 65 AF                     mov dword ptr [rbp - 0x51], r12d
00A00AFF  41 BD 08 00 00 00               mov r13d, 8
00A00B05  66 45 89 1E                     mov word ptr [r14], r11w
00A00B09  41 0F B7 47 02                  movzx eax, word ptr [r15 + 2]
00A00B0E  4C 03 F8                        add r15, rax
00A00B11  48 8B 45 47                     mov rax, qword ptr [rbp + 0x47]
00A00B15  E9 FC FC FF FF                  jmp 0x140a00816
00A00B1A  41 8A 1F                        mov bl, byte ptr [r15]
00A00B1D  4C 8D 05 80 7E 40 00            lea r8, [rip + 0x407e80]
00A00B24  8B 4D 7F                        mov ecx, dword ptr [rbp + 0x7f]
00A00B27  33 D2                           xor edx, edx
00A00B29  44 8B CA                        mov r9d, edx
00A00B2C  41 8B 40 FC                     mov eax, dword ptr [r8 - 4]
00A00B30  23 C1                           and eax, ecx
00A00B32  3B C1                           cmp eax, ecx
00A00B34  75 16                           jne 0x140a00b4c
00A00B36  45 8B 10                        mov r10d, dword ptr [r8]
00A00B39  45 85 D2                        test r10d, r10d
00A00B3C  0F 85 ED 01 00 00               jne 0x140a00d2f
00A00B42  45 3B 58 F8                     cmp r11d, dword ptr [r8 - 8]
00A00B46  0F 84 3C 04 00 00               je 0x140a00f88
00A00B4C  45 03 CC                        add r9d, r12d
00A00B4F  49 83 C0 20                     add r8, 0x20
00A00B53  41 83 F9 09                     cmp r9d, 9
00A00B57  0F 83 7C FD FF FF               jae 0x140a008d9
00A00B5D  33 D2                           xor edx, edx
00A00B5F  EB CB                           jmp 0x140a00b2c
00A00B61  48 85 F6                        test rsi, rsi
00A00B64  0F 84 DB FB FF FF               je 0x140a00745
00A00B6A  66 41 C7 06 3B 00               mov word ptr [r14], 0x3b
00A00B70  48 FF CE                        dec rsi
00A00B73  49 83 C6 02                     add r14, 2
00A00B77  4C 8B C3                        mov r8, rbx
00A00B7A  49 8B CE                        mov rcx, r14
00A00B7D  48 8B D6                        mov rdx, rsi
00A00B80  E8 2B 59 B0 FF                  call 0x1405064b0
00A00B85  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A00B89  45 33 DB                        xor r11d, r11d
00A00B8C  48 FF C0                        inc rax
00A00B8F  66 44 39 1C 43                  cmp word ptr [rbx + rax*2], r11w
00A00B94  75 F6                           jne 0x140a00b8c
00A00B96  4D 8D 34 46                     lea r14, [r14 + rax*2]
00A00B9A  48 2B F0                        sub rsi, rax
00A00B9D  E9 3C FF FF FF                  jmp 0x140a00ade
00A00BA2  83 F8 01                        cmp eax, 1
00A00BA5  0F 85 88 00 00 00               jne 0x140a00c33
00A00BAB  41 80 3F 11                     cmp byte ptr [r15], 0x11
00A00BAF  48 8D 0D A6 80 40 00            lea rcx, [rip + 0x4080a6]
00A00BB6  44 8B 45 7F                     mov r8d, dword ptr [rbp + 0x7f]
00A00BBA  B8 04 00 00 00                  mov eax, 4
00A00BBF  44 8B 6D AB                     mov r13d, dword ptr [rbp - 0x55]
00A00BC3  44 0F 44 C0                     cmove r8d, eax
00A00BC7  41 8B D3                        mov edx, r11d
00A00BCA  8B 41 04                        mov eax, dword ptr [rcx + 4]
00A00BCD  41 23 C0                        and eax, r8d
00A00BD0  41 3B C0                        cmp eax, r8d
00A00BD3  75 05                           jne 0x140a00bda
00A00BD5  44 3B 29                        cmp r13d, dword ptr [rcx]
00A00BD8  74 0B                           je 0x140a00be5
00A00BDA  FF C2                           inc edx
00A00BDC  48 83 C1 18                     add rcx, 0x18
00A00BE0  83 FA 1C                        cmp edx, 0x1c
00A00BE3  72 E5                           jb 0x140a00bca
00A00BE5  4C 8B 6D DF                     mov r13, qword ptr [rbp - 0x21]
00A00BE9  83 FA 1C                        cmp edx, 0x1c
00A00BEC  0F 83 59 FE FF FF               jae 0x140a00a4b
00A00BF2  8B C2                           mov eax, edx
00A00BF4  48 8D 0C 40                     lea rcx, [rax + rax*2]
00A00BF8  48 8D 05 01 F4 5F FF            lea rax, [rip - 0xa00bff]
00A00BFF  48 8D 98 50 8C E0 00            lea rbx, [rax + 0xe08c50]
00A00C06  48 8D 1C CB                     lea rbx, [rbx + rcx*8]
00A00C0A  48 85 DB                        test rbx, rbx
00A00C0D  0F 84 38 FE FF FF               je 0x140a00a4b
00A00C13  4C 8B 03                        mov r8, qword ptr [rbx]
00A00C16  48 8B D6                        mov rdx, rsi
00A00C19  49 8B CE                        mov rcx, r14
00A00C1C  E8 8F 58 B0 FF                  call 0x1405064b0
00A00C21  8B 43 08                        mov eax, dword ptr [rbx + 8]
00A00C24  48 2B F0                        sub rsi, rax
00A00C27  45 33 DB                        xor r11d, r11d
00A00C2A  4D 8D 34 46                     lea r14, [r14 + rax*2]
00A00C2E  E9 18 FE FF FF                  jmp 0x140a00a4b
00A00C33  4C 8B 65 D7                     mov r12, qword ptr [rbp - 0x29]
00A00C37  45 8B FB                        mov r15d, r11d
00A00C3A  44 8B 6D 7F                     mov r13d, dword ptr [rbp + 0x7f]
00A00C3E  BF 04 00 00 00                  mov edi, 4
00A00C43  8B 45 AB                        mov eax, dword ptr [rbp - 0x55]
00A00C46  41 8B CF                        mov ecx, r15d
00A00C49  41 B8 01 00 00 00               mov r8d, 1
00A00C4F  41 D3 E0                        shl r8d, cl
00A00C52  44 23 C0                        and r8d, eax
00A00C55  75 1D                           jne 0x140a00c74
00A00C57  41 FF C7                        inc r15d
00A00C5A  41 83 FF 20                     cmp r15d, 0x20
00A00C5E  72 E6                           jb 0x140a00c46
00A00C60  8B 7D B3                        mov edi, dword ptr [rbp - 0x4d]
00A00C63  4C 8B 65 F7                     mov r12, qword ptr [rbp - 9]
00A00C67  4C 8B 6D DF                     mov r13, qword ptr [rbp - 0x21]
00A00C6B  4C 8B 7D D7                     mov r15, qword ptr [rbp - 0x29]
00A00C6F  E9 D7 FD FF FF                  jmp 0x140a00a4b
00A00C74  41 80 3C 24 11                  cmp byte ptr [r12], 0x11
00A00C79  48 8D 0D DC 7F 40 00            lea rcx, [rip + 0x407fdc]
00A00C80  45 8B CD                        mov r9d, r13d
00A00C83  41 8B D3                        mov edx, r11d
00A00C86  44 0F 44 CF                     cmove r9d, edi
00A00C8A  8B 41 04                        mov eax, dword ptr [rcx + 4]
00A00C8D  41 23 C1                        and eax, r9d
00A00C90  41 3B C1                        cmp eax, r9d
00A00C93  75 05                           jne 0x140a00c9a
00A00C95  44 3B 01                        cmp r8d, dword ptr [rcx]
00A00C98  74 0B                           je 0x140a00ca5
00A00C9A  FF C2                           inc edx
00A00C9C  48 83 C1 18                     add rcx, 0x18
00A00CA0  83 FA 1C                        cmp edx, 0x1c
00A00CA3  72 E5                           jb 0x140a00c8a
00A00CA5  83 FA 1C                        cmp edx, 0x1c
00A00CA8  73 38                           jae 0x140a00ce2
00A00CAA  8B C2                           mov eax, edx
00A00CAC  48 8D 0C 40                     lea rcx, [rax + rax*2]
00A00CB0  48 8D 05 49 F3 5F FF            lea rax, [rip - 0xa00cb7]
00A00CB7  48 8D 98 50 8C E0 00            lea rbx, [rax + 0xe08c50]
00A00CBE  48 8D 1C CB                     lea rbx, [rbx + rcx*8]
00A00CC2  48 85 DB                        test rbx, rbx
00A00CC5  74 1B                           je 0x140a00ce2
00A00CC7  4C 8B 03                        mov r8, qword ptr [rbx]
00A00CCA  48 8B D6                        mov rdx, rsi
00A00CCD  49 8B CE                        mov rcx, r14
00A00CD0  E8 DB 57 B0 FF                  call 0x1405064b0
00A00CD5  8B 43 08                        mov eax, dword ptr [rbx + 8]
00A00CD8  48 2B F0                        sub rsi, rax
00A00CDB  45 33 DB                        xor r11d, r11d
00A00CDE  4D 8D 34 46                     lea r14, [r14 + rax*2]
00A00CE2  8B 45 AB                        mov eax, dword ptr [rbp - 0x55]
00A00CE5  E9 6D FF FF FF                  jmp 0x140a00c57
00A00CEA  4D 89 29                        mov qword ptr [r9], r13
00A00CED  41 8B C5                        mov eax, r13d
00A00CF0  45 89 2E                        mov dword ptr [r14], r13d
00A00CF3  E9 C5 FA FF FF                  jmp 0x140a007bd
00A00CF8  49 8B CE                        mov rcx, r14
00A00CFB  E8 04 17 ED FF                  call 0x1408d2404
00A00D00  B8 08 00 00 00                  mov eax, 8
00A00D05  E9 B3 FA FF FF                  jmp 0x140a007bd
00A00D0A  41 3B D1                        cmp edx, r9d
00A00D0D  73 18                           jae 0x140a00d27
00A00D0F  49 8B 40 04                     mov rax, qword ptr [r8 + 4]
00A00D13  8B CA                           mov ecx, edx
00A00D15  40 38 34 01                     cmp byte ptr [rcx + rax], sil
00A00D19  74 04                           je 0x140a00d1f
00A00D1B  FF C2                           inc edx
00A00D1D  EB EB                           jmp 0x140a00d0a
00A00D1F  8B 4D 7F                        mov ecx, dword ptr [rbp + 0x7f]
00A00D22  E9 CA F8 FF FF                  jmp 0x140a005f1
00A00D27  8B 4D 7F                        mov ecx, dword ptr [rbp + 0x7f]
00A00D2A  E9 CC F8 FF FF                  jmp 0x140a005fb
00A00D2F  41 3B D2                        cmp edx, r10d
00A00D32  73 43                           jae 0x140a00d77
00A00D34  49 8B 40 04                     mov rax, qword ptr [r8 + 4]
00A00D38  8B CA                           mov ecx, edx
00A00D3A  38 1C 01                        cmp byte ptr [rcx + rax], bl
00A00D3D  74 30                           je 0x140a00d6f
00A00D3F  41 03 D4                        add edx, r12d
00A00D42  EB EB                           jmp 0x140a00d2f
00A00D44  49 8B 0F                        mov rcx, qword ptr [r15]
00A00D47  E8 B8 16 ED FF                  call 0x1408d2404
00A00D4C  48 8B 45 67                     mov rax, qword ptr [rbp + 0x67]
00A00D50  49 89 1F                        mov qword ptr [r15], rbx
00A00D53  89 18                           mov dword ptr [rax], ebx
00A00D55  E9 61 FA FF FF                  jmp 0x140a007bb
00A00D5A  B8 08 00 00 00                  mov eax, 8
00A00D5F  EB 8F                           jmp 0x140a00cf0
00A00D61  BF 38 05 00 00                  mov edi, 0x538
00A00D66  44 8B 65 A7                     mov r12d, dword ptr [rbp - 0x59]
00A00D6A  E9 09 F9 FF FF                  jmp 0x140a00678
00A00D6F  8B 4D 7F                        mov ecx, dword ptr [rbp + 0x7f]
00A00D72  E9 CB FD FF FF                  jmp 0x140a00b42
00A00D77  8B 4D 7F                        mov ecx, dword ptr [rbp + 0x7f]
00A00D7A  E9 CD FD FF FF                  jmp 0x140a00b4c
00A00D7F  B8 57 00 00 00                  mov eax, 0x57
00A00D84  E9 34 FA FF FF                  jmp 0x140a007bd
00A00D89  49 8B CE                        mov rcx, r14
00A00D8C  E8 73 16 ED FF                  call 0x1408d2404
00A00D91  49 8B CF                        mov rcx, r15
00A00D94  E9 62 FF FF FF                  jmp 0x140a00cfb
00A00D99  44 8B DB                        mov r11d, ebx
00A00D9C  41 8A 1E                        mov bl, byte ptr [r14]
00A00D9F  41 83 FB 20                     cmp r11d, 0x20
00A00DA3  0F 83 9A 00 00 00               jae 0x140a00e43
00A00DA9  41 8B CB                        mov ecx, r11d
00A00DAC  41 B8 01 00 00 00               mov r8d, 1
00A00DB2  41 D3 E0                        shl r8d, cl
00A00DB5  45 23 C4                        and r8d, r12d
00A00DB8  74 6A                           je 0x140a00e24
00A00DBA  80 FB 11                        cmp bl, 0x11
00A00DBD  48 8D 0D 98 7E 40 00            lea rcx, [rip + 0x407e98]
00A00DC4  B8 04 00 00 00                  mov eax, 4
00A00DC9  44 0F 44 C8                     cmove r9d, eax
00A00DCD  33 D2                           xor edx, edx
00A00DCF  8B 41 04                        mov eax, dword ptr [rcx + 4]
00A00DD2  41 23 C1                        and eax, r9d
00A00DD5  41 3B C1                        cmp eax, r9d
00A00DD8  75 05                           jne 0x140a00ddf
00A00DDA  44 3B 01                        cmp r8d, dword ptr [rcx]
00A00DDD  74 0B                           je 0x140a00dea
00A00DDF  FF C2                           inc edx
00A00DE1  48 83 C1 18                     add rcx, 0x18
00A00DE5  83 FA 1C                        cmp edx, 0x1c
00A00DE8  72 E5                           jb 0x140a00dcf
00A00DEA  83 FA 1C                        cmp edx, 0x1c
00A00DED  73 3D                           jae 0x140a00e2c
00A00DEF  48 8D 0C 52                     lea rcx, [rdx + rdx*2]
00A00DF3  33 D2                           xor edx, edx
00A00DF5  48 8D 05 04 F2 5F FF            lea rax, [rip - 0xa00dfc]
00A00DFC  48 8D 04 C8                     lea rax, [rax + rcx*8]
00A00E00  48 8D 80 50 8C E0 00            lea rax, [rax + 0xe08c50]
00A00E07  48 85 C0                        test rax, rax
00A00E0A  74 20                           je 0x140a00e2c
00A00E0C  48 8B 08                        mov rcx, qword ptr [rax]
00A00E0F  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A00E13  48 FF C0                        inc rax
00A00E16  66 39 14 41                     cmp word ptr [rcx + rax*2], dx
00A00E1A  75 F7                           jne 0x140a00e13
00A00E1C  44 8B 4D 7F                     mov r9d, dword ptr [rbp + 0x7f]
00A00E20  45 8D 14 42                     lea r10d, [r10 + rax*2]
00A00E24  41 FF C3                        inc r11d
00A00E27  E9 73 FF FF FF                  jmp 0x140a00d9f
00A00E2C  48 8B 4D E7                     mov rcx, qword ptr [rbp - 0x19]
00A00E30  41 BA 14 00 00 00               mov r10d, 0x14
00A00E36  42 C7 04 B9 02 00 00 00         mov dword ptr [rcx + r15*4], 2
00A00E3E  EB 03                           jmp 0x140a00e43
00A00E40  45 03 D2                        add r10d, r10d
00A00E43  44 8B 65 AF                     mov r12d, dword ptr [rbp - 0x51]
00A00E47  48 8D 45 D7                     lea rax, [rbp - 0x29]
00A00E4B  4C 8B 45 6F                     mov r8, qword ptr [rbp + 0x6f]
00A00E4F  41 83 C4 06                     add r12d, 6
00A00E53  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A00E58  45 03 E2                        add r12d, r10d
00A00E5B  8A 85 87 00 00 00               mov al, byte ptr [rbp + 0x87]
00A00E61  48 8B D6                        mov rdx, rsi
00A00E64  33 C9                           xor ecx, ecx
00A00E66  44 89 65 A7                     mov dword ptr [rbp - 0x59], r12d
00A00E6A  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00A00E6E  E8 4D 85 F2 FF                  call 0x1409293c0
00A00E73  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
00A00E77  45 33 DB                        xor r11d, r11d
00A00E7A  4A 8D 1C F9                     lea rbx, [rcx + r15*8]
00A00E7E  48 85 C0                        test rax, rax
00A00E81  74 3F                           je 0x140a00ec2
00A00E83  48 83 C0 02                     add rax, 2
00A00E87  48 89 03                        mov qword ptr [rbx], rax
00A00E8A  48 8B 0B                        mov rcx, qword ptr [rbx]
00A00E8D  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A00E91  48 FF C0                        inc rax
00A00E94  66 44 39 1C 41                  cmp word ptr [rcx + rax*2], r11w
00A00E99  75 F6                           jne 0x140a00e91
00A00E9B  48 8B 75 47                     mov rsi, qword ptr [rbp + 0x47]
00A00E9F  45 8D 24 44                     lea r12d, [r12 + rax*2]
00A00EA3  41 0F B7 46 02                  movzx eax, word ptr [r14 + 2]
00A00EA8  41 83 C4 04                     add r12d, 4
00A00EAC  8B 5D 7F                        mov ebx, dword ptr [rbp + 0x7f]
00A00EAF  41 FF C7                        inc r15d
00A00EB2  44 89 65 A7                     mov dword ptr [rbp - 0x59], r12d
00A00EB6  4C 03 F0                        add r14, rax
00A00EB9  44 89 7D B3                     mov dword ptr [rbp - 0x4d], r15d
00A00EBD  E9 70 F6 FF FF                  jmp 0x140a00532
00A00EC2  4C 39 5D D7                     cmp qword ptr [rbp - 0x29], r11
00A00EC6  0F 85 3C 01 00 00               jne 0x140a01008
00A00ECC  48 8B 4D C7                     mov rcx, qword ptr [rbp - 0x39]
00A00ED0  48 8B D3                        mov rdx, rbx
00A00ED3  E8 44 0A 00 00                  call 0x140a0191c
00A00ED8  45 33 DB                        xor r11d, r11d
00A00EDB  85 C0                           test eax, eax
00A00EDD  0F 88 59 01 00 00               js 0x140a0103c
00A00EE3  48 8B 45 FF                     mov rax, qword ptr [rbp - 1]
00A00EE7  41 C6 04 07 01                  mov byte ptr [r15 + rax], 1
00A00EEC  EB 9C                           jmp 0x140a00e8a
00A00EEE  45 33 DB                        xor r11d, r11d
00A00EF1  41 83 FA 09                     cmp r10d, 9
00A00EF5  0F 83 14 F7 FF FF               jae 0x140a0060f
00A00EFB  41 8B C2                        mov eax, r10d
00A00EFE  48 C1 E0 05                     shl rax, 5
00A00F02  49 03 C7                        add rax, r15
00A00F05  0F 84 04 F7 FF FF               je 0x140a0060f
00A00F0B  48 8B 08                        mov rcx, qword ptr [rax]
00A00F0E  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A00F12  48 FF C0                        inc rax
00A00F15  66 44 39 1C 41                  cmp word ptr [rcx + rax*2], r11w
00A00F1A  75 F6                           jne 0x140a00f12
00A00F1C  45 8D 24 44                     lea r12d, [r12 + rax*2]
00A00F20  E9 EA F6 FF FF                  jmp 0x140a0060f
00A00F25  8B 42 04                        mov eax, dword ptr [rdx + 4]
00A00F28  41 23 C0                        and eax, r8d
00A00F2B  41 3B C0                        cmp eax, r8d
00A00F2E  75 05                           jne 0x140a00f35
00A00F30  44 3B 22                        cmp r12d, dword ptr [rdx]
00A00F33  74 0B                           je 0x140a00f40
00A00F35  FF C1                           inc ecx
00A00F37  48 83 C2 18                     add rdx, 0x18
00A00F3B  83 F9 1C                        cmp ecx, 0x1c
00A00F3E  72 E5                           jb 0x140a00f25
00A00F40  83 F9 1C                        cmp ecx, 0x1c
00A00F43  0F 83 50 FE FF FF               jae 0x140a00d99
00A00F49  8B C1                           mov eax, ecx
00A00F4B  48 8D 0C 40                     lea rcx, [rax + rax*2]
00A00F4F  48 8D 05 AA F0 5F FF            lea rax, [rip - 0xa00f56]
00A00F56  48 8D 90 50 8C E0 00            lea rdx, [rax + 0xe08c50]
00A00F5D  48 8D 14 CA                     lea rdx, [rdx + rcx*8]
00A00F61  48 85 D2                        test rdx, rdx
00A00F64  0F 84 2F FE FF FF               je 0x140a00d99
00A00F6A  43 C7 04 BB 01 00 00 00         mov dword ptr [r11 + r15*4], 1
00A00F72  49 83 CA FF                     or r10, 0xffffffffffffffff
00A00F76  48 8B 02                        mov rax, qword ptr [rdx]
00A00F79  49 FF C2                        inc r10
00A00F7C  66 42 39 1C 50                  cmp word ptr [rax + r10*2], bx
00A00F81  75 F6                           jne 0x140a00f79
00A00F83  E9 B8 FE FF FF                  jmp 0x140a00e40
00A00F88  45 33 DB                        xor r11d, r11d
00A00F8B  41 83 F9 09                     cmp r9d, 9
00A00F8F  0F 83 47 F9 FF FF               jae 0x140a008dc
00A00F95  41 8B D9                        mov ebx, r9d
00A00F98  48 8D 05 F1 79 40 00            lea rax, [rip + 0x4079f1]
00A00F9F  48 C1 E3 05                     shl rbx, 5
00A00FA3  48 03 D8                        add rbx, rax
00A00FA6  0F 84 30 F9 FF FF               je 0x140a008dc
00A00FAC  4C 8B 03                        mov r8, qword ptr [rbx]
00A00FAF  48 8B D6                        mov rdx, rsi
00A00FB2  49 8B CE                        mov rcx, r14
00A00FB5  E8 F6 54 B0 FF                  call 0x1405064b0
00A00FBA  8B 43 08                        mov eax, dword ptr [rbx + 8]
00A00FBD  48 2B F0                        sub rsi, rax
00A00FC0  4D 8D 34 46                     lea r14, [r14 + rax*2]
00A00FC4  E9 10 F9 FF FF                  jmp 0x140a008d9
00A00FC9  4D 89 29                        mov qword ptr [r9], r13
00A00FCC  45 89 2E                        mov dword ptr [r14], r13d
00A00FCF  E9 DF F4 FF FF                  jmp 0x140a004b3
00A00FD4  33 D2                           xor edx, edx
00A00FD6  E9 00 F6 FF FF                  jmp 0x140a005db
00A00FDB  44 8B 4D 7F                     mov r9d, dword ptr [rbp + 0x7f]
00A00FDF  48 8D 15 76 7C 40 00            lea rdx, [rip + 0x407c76]
00A00FE6  33 DB                           xor ebx, ebx
00A00FE8  45 8B D3                        mov r10d, r11d
00A00FEB  4C 8B 5D E7                     mov r11, qword ptr [rbp - 0x19]
00A00FEF  45 8B C1                        mov r8d, r9d
00A00FF2  8B CB                           mov ecx, ebx
00A00FF4  8D 43 04                        lea eax, [rbx + 4]
00A00FF7  43 89 1C BB                     mov dword ptr [r11 + r15*4], ebx
00A00FFB  41 80 3E 11                     cmp byte ptr [r14], 0x11
00A00FFF  44 0F 44 C0                     cmove r8d, eax
00A01003  E9 1D FF FF FF                  jmp 0x140a00f25
00A01008  B9 06 00 00 00                  mov ecx, 6
00A0100D  E8 76 4F F2 FF                  call 0x140925f88
00A01012  45 33 DB                        xor r11d, r11d
00A01015  48 89 03                        mov qword ptr [rbx], rax
00A01018  48 85 C0                        test rax, rax
00A0101B  0F 84 06 18 13 00               je 0x140b32827
00A01021  4C 8D 05 CC 0C 61 FF            lea r8, [rip - 0x9ef334]
00A01028  48 8B C8                        mov rcx, rax
00A0102B  41 8D 53 03                     lea edx, [r11 + 3]
00A0102F  E8 7C 54 B0 FF                  call 0x1405064b0
00A01034  45 33 DB                        xor r11d, r11d
00A01037  E9 A7 FE FF FF                  jmp 0x140a00ee3
00A0103C  8B C8                           mov ecx, eax
00A0103E  E8 FD 5B F2 FF                  call 0x140926c40
00A01043  8B 5D 7F                        mov ebx, dword ptr [rbp + 0x7f]
00A01046  8B F8                           mov edi, eax
00A01048  45 33 DB                        xor r11d, r11d
00A0104B  E9 17 F6 FF FF                  jmp 0x140a00667
00A01050  BF 38 05 00 00                  mov edi, 0x538
00A01055  E9 1E F6 FF FF                  jmp 0x140a00678
00A0105A  41 FF C4                        inc r12d
00A0105D  44 89 65 A7                     mov dword ptr [rbp - 0x59], r12d
00A01061  E9 7D F7 FF FF                  jmp 0x140a007e3
00A01066  41 8B FD                        mov edi, r13d
00A01069  E9 0E F6 FF FF                  jmp 0x140a0067c
00A0106E  48 8D 55 CF                     lea rdx, [rbp - 0x31]
00A01072  49 8B CC                        mov rcx, r12
00A01075  E8 7A 43 DA FF                  call 0x1407a53f4
00A0107A  45 33 DB                        xor r11d, r11d
00A0107D  85 C0                           test eax, eax
00A0107F  0F 84 E1 FC FF FF               je 0x140a00d66
00A01085  4C 8B 45 CF                     mov r8, qword ptr [rbp - 0x31]
00A01089  48 83 CB FF                     or rbx, 0xffffffffffffffff
00A0108D  E9 0C 18 13 00                  jmp 0x140b3289e
00A01092  48 8D 55 CF                     lea rdx, [rbp - 0x31]
00A01096  49 8B CD                        mov rcx, r13
00A01099  E8 56 43 DA FF                  call 0x1407a53f4
00A0109E  45 33 DB                        xor r11d, r11d
00A010A1  85 C0                           test eax, eax
00A010A3  0F 84 BD FC FF FF               je 0x140a00d66
00A010A9  4C 8B 45 CF                     mov r8, qword ptr [rbp - 0x31]
00A010AD  48 83 CB FF                     or rbx, 0xffffffffffffffff
00A010B1  E9 19 18 13 00                  jmp 0x140b328cf
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall LocalConvertAclToString(__int64 a1, unsigned __int8 a2, unsigned __int8 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int8 v_stack_p40;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (176);
    v_r13 = 0;
    *(unsigned int *)(v_rsp - 63 - 89) = 0;
    *(unsigned int *)(v_rsp - 63 - 17) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 49) = 0;
    *(unsigned int *)(v_rsp - 63 - 85) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 57) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 41) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 65) = 0;
    if (a4 == 0) goto loc_00A00D7F;
    if (*(unsigned __int64 *)(v_rsp - 63 + 103) == 0) goto loc_00A00D7F;
    if (a2 == 0) goto loc_00A00FC9;
    if (a1 != 0) goto loc_00A004BA;
    *(unsigned __int64 *)(a4) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 103)) = (unsigned int)(a1 + 36);
    result = SddlpAlloc(a1 + 36, a2, a3, a4);
    *(unsigned __int64 *)(a4) = result;
    if (result == 0) goto loc_00A00D5A;
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm1;
    *(unsigned int *)(result + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 10414088)));
loc_00A004B3:
    result = 0;
    goto loc_00A007BD;
loc_00A004BA:
    if ((unsigned __int16)(*(unsigned __int16 *)((unsigned int)(*(unsigned int *)(v_rip - 10414088)) + 4)) == 0) goto loc_00A00CEA;
    a3 = (unsigned __int8)(-(a3));
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)((unsigned int)(*(unsigned int *)(v_rip - 10414088)) + 4)))) << (3);
    v_rbx = (unsigned int)((a4) + (2));
    *(unsigned int *)(v_rsp - 63 + 127) = (unsigned int)(v_rbx);
    result = SddlpAlloc(a1, a2, a3, a4);
    *(unsigned __int64 *)(v_rsp - 63 - 73) = result;
    if (result == 0) goto loc_00A00D00;
    result = SddlpAlloc(*(unsigned __int16 *)(a1 + 4), a2, a3, a4);
    *(unsigned __int64 *)(v_rsp - 63 - 1) = result;
    if (result == 0) goto loc_00A00CF8;
    a1 = (*(unsigned __int16 *)(a1 + 4)) << (2);
    result = SddlpAlloc(a1, a2, a3, a4);
    v_r11 = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 25) = result;
    if (result == 0) goto loc_00A00D89;
    *(unsigned int *)(v_rsp - 63 - 77) = 0;
loc_00A00532:
    if (0 >= ((unsigned int)(*(unsigned __int16 *)(a1 + 4)))) goto loc_00A00667;
    v_r12 = (unsigned int)((0) + (2));
    *(unsigned int *)(v_rsp - 63 - 89) = (unsigned int)(v_r12);
loc_00A0055C:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 4228459 + 4))) & ((unsigned int)(v_rbx)));
    if (((unsigned int)(result)) != ((unsigned int)(v_rbx))) goto loc_00A00569;
    if (((unsigned int)(*(unsigned __int8 *)(a1 + 8))) == (*(unsigned int *)(v_rip + 4228459))) goto loc_00A00574;
loc_00A00569:
    a2 = (unsigned int)((0) + 1);
    a1 = (v_rip + 4228459) + (24);
    if (a2 < 17) goto loc_00A0055C;
loc_00A00574:
    if (a2 >= 17) goto loc_00A00662;
    result = ((unsigned int)(a2) + (unsigned int)(a2) * 2 * 8 + 14715568) + (v_rip - 10487101);
    if (condition_is_equal) goto loc_00A00662;
    result = (result) | (-1);
loc_00A0059B:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(result) + result * 2)) != 0) goto loc_00A0059B;
    v_r12 = (unsigned int)((v_r12 + result * 2) + (2));
loc_00A005BC:
    v_r11 = (unsigned int)((1) << (0));
    if ((((unsigned int)(v_r11)) & ((unsigned int)(*(unsigned __int8 *)(a1 + 8 + 1)))) == 0) goto loc_00A0060C;
    a2 = 0;
loc_00A005DB:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 4228046 - 4))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 127)))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 127))))) goto loc_00A005FB;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4228046))) != 0) goto loc_00A00D0A;
loc_00A005F1:
    if (((unsigned int)(v_r11)) == (*(unsigned int *)(v_rip + 4228046 - 8))) goto loc_00A00EEE;
loc_00A005FB:
    v_r10 = (unsigned int)((0) + 1);
    a3 = (v_rip + 4228046) + (32);
    if (((unsigned int)(v_r10)) < 9) goto loc_00A00FD4;
loc_00A0060C:
    v_r11 = 0;
loc_00A0060F:
    v_rbx = (unsigned int)((0) + 1);
    if (((unsigned int)(v_rbx)) < ((unsigned int)(v_r11 + 8))) goto loc_00A005BC;
    v_r12 = (unsigned int)((v_r12) + (2));
    *(unsigned int *)(v_rsp - 63 - 89) = (unsigned int)(v_r12);
    *(unsigned int *)(v_rsp - 63 - 81) = (unsigned int)(v_r12);
    if (((unsigned int)(*(unsigned __int8 *)(a1 + 8))) <= 9) goto loc_00A00685;
    a1 = (unsigned int)((*(unsigned __int8 *)(a1 + 8)) - (10));
    if (condition_is_equal) goto loc_00A006BF;
    a1 = (unsigned int)((a1) - (1));
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00A006BF;
    a1 = (unsigned int)((a1) - (4));
    if (condition_is_equal) goto loc_00A006BF;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A006BF;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A006BF;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A006BF;
    if (((unsigned int)(a1)) == 1) goto loc_00A006BF;
loc_00A0065F:
loc_00A00662:
loc_00A00667:
    if ((unsigned int)(v_r12) == 0) goto loc_00A01050;
    if ((unsigned int)((unsigned int)(0x538ULL)) == 0) goto loc_00A007D9;
loc_00A00678:
loc_00A0067C:
    goto loc_00A00752;
loc_00A00685:
    if ((unsigned int)((unsigned int)(0x538ULL)) == 0) goto loc_00A006BF;
    if ((unsigned int)(a1) == 0) goto loc_00A006BF;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A006BF;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A006BF;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A006BF;
    a1 = (unsigned int)((a1) - (2));
    a1 = (unsigned int)((a1) - (1));
    a1 = (unsigned int)((a1) - (1));
    if (((unsigned int)(a1)) != 1) goto loc_00A0065F;
loc_00A006BF:
    *(unsigned __int64 *)(v_rsp - 63 - 57) = a1 + 8 + 8;
    *(unsigned int *)(v_rsp - 63 - 85) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8 + 4)));
    if (*(unsigned __int64 *)(v_rsp - 63 - 65) != 0) {
        a1 = *(unsigned __int64 *)(v_rsp - 63 - 65);
        result = PdcCloseEvent(a1, a2, a3, (unsigned int)(*(unsigned int *)(v_rip + 4228046)));
        v_r11 = 0;
        *(unsigned __int64 *)(v_rsp - 63 - 65) = 0;
    }
    v_stack_mA8 = (unsigned __int8)(*(unsigned __int8 *)(v_rsp - 63 + 135));
    v_stack_mB0 = 0;
    v_stack_mB8 = *(unsigned __int64 *)(v_rsp - 63 + 119);
    v_stack_mC0 = *(unsigned __int64 *)(v_rsp - 63 + 111);
    v_stack_mC8 = v_rsp - 63 - 81;
    *(unsigned int *)(v_rsp - 63 - 77) = 0;
    result = LocalGetAceCondition(a1 + 8, a1 + 8 + 8, v_rsp - 63 - 65, v_rsp - 63 - 77);
    v_r11 = 0;
    if ((unsigned int)(result) == 0) goto loc_00A00FDB;
    *(unsigned int *)(v_rsp - 63 - 89) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 - 81)));
    goto loc_00A00667;
loc_00A00745:
loc_00A00752:
    if (0 >= (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 63 + 71) + 4))) goto loc_00A00787;
loc_00A00764:
    if ((*(unsigned __int8 *)(0 + *(unsigned __int64 *)(v_rsp - 63 - 1) * 1)) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 73) + 0 * 8);
        result = PdcCloseEvent(a1, a1 + 8 + 8, v_rsp - 63 - 65, v_rsp - 63 - 77);
        v_r11 = 0;
    }
    v_rbx = (unsigned int)((0) + 1);
    if (((unsigned int)(v_rbx)) < ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 63 + 71) + 4)))) goto loc_00A00764;
loc_00A00787:
    result = PdcCloseEvent(*(unsigned __int64 *)(v_rsp - 63 - 73), a1 + 8 + 8, v_rsp - 63 - 65, v_rsp - 63 - 77);
    result = PdcCloseEvent(*(unsigned __int64 *)(v_rsp - 63 - 1), a1 + 8 + 8, v_rsp - 63 - 65, v_rsp - 63 - 77);
    result = PdcCloseEvent(*(unsigned __int64 *)(v_rsp - 63 - 25), a1 + 8 + 8, v_rsp - 63 - 65, v_rsp - 63 - 77);
    result = PdcCloseEvent(*(unsigned __int64 *)(v_rsp - 63 - 65), a1 + 8 + 8, v_rsp - 63 - 65, v_rsp - 63 - 77);
    v_rbx = 0;
    if ((unsigned int)((unsigned int)(0x538ULL)) != 0) goto loc_00A00D44;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 103)) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 - 89)));
loc_00A007BB:
loc_00A007BD:
    v_rsp = (v_rsp) + (176);
    return (unsigned int)((unsigned int)((unsigned int)(0x538ULL)));
loc_00A007D9:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 63 - 89)))) & (1)) != 0) goto loc_00A0105A;
loc_00A007E3:
    result = SddlpAlloc((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 - 89)))), a1 + 8 + 8, v_rsp - 63 - 65, v_rsp - 63 - 77);
    v_r11 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 + 95)) = result;
    if (result == 0) goto loc_00A01066;
    v_rsi = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 - 89))))) >> (1);
    *(unsigned int *)(v_rsp - 63 - 81) = 0;
loc_00A00816:
    *(unsigned __int64 *)(v_rsp - 63 - 41) = *(unsigned __int64 *)(v_rsp - 63 + 71) + 8;
    if (0 >= ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 63 + 71) + 4)))) goto loc_00A00D66;
    if (v_rsi == 0) goto loc_00A00D61;
    *(unsigned __int16 *)(result) = 40;
    v_r14 = (result) + (2);
    v_rsi = (v_rsi) - (59 - 58);
loc_00A00855:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 4227697 + 4))) & ((unsigned int)(v_stack_p10)));
    if (((unsigned int)(result)) != ((unsigned int)(v_stack_p10))) goto loc_00A00863;
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 63 + 71) + 8))) == (*(unsigned int *)(v_rip + 4227697))) goto loc_00A0086F;
loc_00A00863:
    a1 = (unsigned int)((0) + ((unsigned int)(59 - 58)));
    a2 = (v_rip + 4227697) + (24);
    if (((unsigned int)(a1)) < 17) goto loc_00A00855;
loc_00A0086F:
    if (((unsigned int)(a1)) >= 17) goto loc_00A008B0;
    result = v_rip - 10487937;
    if (v_rip - 10487937 + 14715568 + (unsigned int)((unsigned int)(a1)) + (unsigned int)((unsigned int)(a1)) * 2 * 8 != 0) {
        a3 = *(unsigned __int64 *)(v_rip - 10487937 + 14715568 + (unsigned int)((unsigned int)(a1)) + (unsigned int)((unsigned int)(a1)) * 2 * 8);
        a2 = v_rsi;
        a1 = v_r14;
        result = wcscpy_s(a1, a2, a3, 59);
        result = *(unsigned int *)(v_rip - 10487937 + 14715568 + (unsigned int)((unsigned int)(a1)) + (unsigned int)((unsigned int)(a1)) * 2 * 8 + 8);
        v_rsi = (v_rsi) - (result);
        v_r11 = 0;
        v_r14 = v_r14 + result * 2;
        a4 = v_r11 + 59;
    }
    if (v_rsi == 0) goto loc_00A00D61;
    *(unsigned __int16 *)(v_r14) = (unsigned __int16)(a4);
    v_r14 = (v_r14) + (2);
    v_rsi = (v_rsi) - (59 - 58);
loc_00A008C7:
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(59 - 58))) << (0));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 63 + 71) + 8 + 1)) & ((unsigned __int8)(v_r11))) != 0) goto loc_00A00B1A;
loc_00A008D9:
    v_r11 = 0;
loc_00A008DC:
    v_rdi = (unsigned int)((0) + ((unsigned int)(59 - 58)));
    if (((unsigned int)(v_rdi)) < ((unsigned int)(*(unsigned __int64 *)(v_rsp - 63 - 73)))) goto loc_00A008C7;
    if (v_rsi == 0) goto loc_00A00D61;
    *(unsigned __int16 *)(v_r14) = 59;
    v_rsi = (v_rsi) - (59 - 58);
    v_r14 = (v_r14) + (2);
    *(unsigned __int64 *)(v_rsp - 63 - 9) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 33) = 0;
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 63 + 71) + 8))) <= 9) goto loc_00A0094E;
    a1 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 63 + 71) + 8)) - (10));
    if (condition_is_equal) goto loc_00A0093D;
    a1 = (unsigned int)((a1) - (1));
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00A0093D;
    a1 = (unsigned int)((a1) - (4));
    if (condition_is_equal) goto loc_00A0093D;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A0093D;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A0093D;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A0093D;
    if (((unsigned int)(a1)) != 1) goto loc_00A00987;
loc_00A0093D:
    *(unsigned __int64 *)(v_rsp - 63 - 57) = *(unsigned __int64 *)(v_rsp - 63 + 71) + 8 + 8;
    *(unsigned int *)(v_rsp - 63 - 85) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 71) + 8 + 4)));
    goto loc_00A0098B;
loc_00A0094E:
    if (((unsigned int)(a1)) == 1) goto loc_00A0093D;
    if ((unsigned int)(a1) == 0) goto loc_00A0093D;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A0093D;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A0093D;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A0093D;
    a1 = (unsigned int)((a1) - (2));
    a1 = (unsigned int)((a1) - (1));
    a1 = (unsigned int)((a1) - (1));
loc_00A00987:
loc_00A0098B:
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 71) + 8 + 4));
    if (*(unsigned __int64 *)(v_rsp - 63 - 65) != 0) {
        a1 = *(unsigned __int64 *)(v_rsp - 63 - 65);
        result = PdcCloseEvent(a1, a2, a3, a4);
        v_r11 = 0;
        *(unsigned __int64 *)(v_rsp - 63 - 65) = 0;
    }
    v_stack_p40 = (unsigned __int8)(*(unsigned __int8 *)(v_rsp - 63 + 135));
    v_stack_p38 = 0;
    v_stack_p30 = *(unsigned __int64 *)(v_rsp - 63 + 119);
    v_stack_p28 = *(unsigned __int64 *)(v_rsp - 63 + 111);
    v_stack_p20 = v_rsp - 63 - 17;
    *(unsigned int *)(v_rsp - 63 - 77) = 0;
    result = LocalGetAceCondition(*(unsigned __int64 *)(v_rsp - 63 + 71) + 8, *(unsigned __int64 *)(v_rsp - 63 - 57), v_rsp - 63 - 65, v_rsp - 63 - 77);
    v_r11 = 0;
    *(unsigned int *)(v_rsp - 63 - 77) = (unsigned int)(result);
    if ((unsigned int)(result) != 0) goto loc_00A00D66;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 - 25) + (unsigned int)(*(unsigned int *)(v_rsp - 63 - 81)) * 4)))) != 2) goto loc_00A00BA2;
    result = wcscpy_s(v_r14, v_rsi, v_rip - 10403734, v_rsp - 63 - 77);
    v_r14 = (v_r14) + (4);
    v_rsi = (v_rsi) - (2);
    result = ultow_s((unsigned int)(*(unsigned int *)(v_rsp - 63 - 85)), v_r14, v_rsi, (unsigned int)((unsigned int)(result)) + 16);
    result = (result) | (-1);
    v_r11 = 0;
loc_00A00A3A:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_r14 + result * 2)) != 0) goto loc_00A00A3A;
    v_rsi = (v_rsi) - (result);
loc_00A00A4B:
    if (v_rsi == 0) goto loc_00A00D61;
    v_rsi = (v_rsi) - 1;
    *(unsigned __int16 *)(v_r14 + result * 2) = 59;
    v_r14 = (v_r14 + result * 2) + (2);
    if (0 != 0) goto loc_00A0106E;
    if (v_rsi == 0) goto loc_00A00D61;
    *(unsigned __int16 *)(v_r14) = 59;
    v_rsi = (v_rsi) - 1;
    v_r14 = (v_r14) + (2);
    if (0 != 0) goto loc_00A01092;
    if (v_rsi == 0) goto loc_00A00745;
    v_rsi = (v_rsi) - 1;
    *(unsigned __int16 *)(v_r14) = 59;
    v_r14 = (v_r14) + (2);
    result = wcscpy_s(v_r14, v_rsi, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 73) + (unsigned int)(*(unsigned int *)(v_rsp - 63 - 81)) * 8), (unsigned int)((unsigned int)(result)) + 16);
    result = (result) | (-1);
    v_r11 = 0;
loc_00A00AC0:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 73) + (unsigned int)(*(unsigned int *)(v_rsp - 63 - 81)) * 8) + result * 2)) != 0) goto loc_00A00AC0;
    v_rsi = (v_rsi) - (result);
    if (*(unsigned __int64 *)(v_rsp - 63 - 65) != 0) goto loc_00A00B61;
loc_00A00ADE:
    if (v_rsi <= 1) goto loc_00A00745;
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 63 - 81))) + 1);
    *(unsigned __int16 *)(v_r14 + result * 2) = 41;
    v_rsi = (v_rsi) - 1;
    v_r14 = (v_r14 + result * 2) + (2);
    *(unsigned int *)(v_rsp - 63 - 81) = (unsigned int)(v_r12);
    *(unsigned __int16 *)(v_r14) = 0;
    v_r15 = (*(unsigned __int64 *)(v_rsp - 63 + 71) + 8) + (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 63 + 71) + 8 + 2));
    goto loc_00A00816;
loc_00A00B1A:
    a2 = 0;
loc_00A00B2C:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 4226688 - 4))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 127)))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 127))))) goto loc_00A00B4C;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4226688))) != 0) goto loc_00A00D2F;
loc_00A00B42:
    if (0 == (*(unsigned int *)(v_rip + 4226688 - 8))) goto loc_00A00F88;
loc_00A00B4C:
    a4 = (unsigned int)((0) + ((unsigned int)(v_r12)));
    a3 = (v_rip + 4226688) + (32);
    if (((unsigned int)(a4)) >= 9) goto loc_00A008D9;
    a2 = 0;
    goto loc_00A00B2C;
loc_00A00B61:
    if (v_rsi == 0) goto loc_00A00745;
    *(unsigned __int16 *)(v_r14) = 59;
    v_rsi = (v_rsi) - 1;
    v_r14 = (v_r14) + (2);
    result = wcscpy_s(v_r14, v_rsi, *(unsigned __int8 *)(v_r15), a4);
    result = (result) | (-1);
    v_r11 = 0;
loc_00A00B8C:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int8 *)(v_r15) + result * 2)) != 0) goto loc_00A00B8C;
    v_rsi = (v_rsi) - (result);
    goto loc_00A00ADE;
loc_00A00BA2:
    if (((unsigned int)(result)) != 1) goto loc_00A00C33;
    a3 = (unsigned int)(*(unsigned int *)(v_rsp - 63 + 127));
    if ((*(unsigned __int8 *)(v_r15)) == 17) { a3 = 4; }
loc_00A00BCA:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 4227238 + 4))) & (a3));
    if (((unsigned int)(result)) != a3) goto loc_00A00BDA;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 - 85)))) == (*(unsigned int *)(v_rip + 4227238))) goto loc_00A00BE5;
loc_00A00BDA:
    a2 = (unsigned int)((0) + 1);
    a1 = (v_rip + 4227238) + (24);
    if (a2 < 28) goto loc_00A00BCA;
loc_00A00BE5:
    if (a2 >= 28) goto loc_00A00A4B;
    if (v_rip - 10488831 + 14715984 + (unsigned int)(a2) + (unsigned int)(a2) * 2 * 8 == 0) goto loc_00A00A4B;
    result = wcscpy_s(v_r14 + result * 2, v_rsi, *(unsigned __int64 *)(v_rip - 10488831 + 14715984 + (unsigned int)(a2) + (unsigned int)(a2) * 2 * 8), a4);
    v_rsi = (v_rsi) - ((unsigned int)(*(unsigned int *)(v_rip - 10488831 + 14715984 + (unsigned int)(a2) + (unsigned int)(a2) * 2 * 8 + 8)));
    v_r11 = 0;
    goto loc_00A00A4B;
loc_00A00C33:
loc_00A00C46:
    a3 = (unsigned int)((1) << (0));
    a3 = (unsigned int)((a3) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 - 85)))));
    if (condition_is_not_equal) goto loc_00A00C74;
loc_00A00C57:
    v_r15 = (unsigned int)((0) + 1);
    if (((unsigned int)(v_r15)) < 32) goto loc_00A00C46;
    goto loc_00A00A4B;
loc_00A00C74:
    a4 = (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 63 - 33)));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 63 - 9))) == 17) { a4 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 - 77))); }
loc_00A00C8A:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 4227036 + 4))) & ((unsigned int)(a4)));
    if (((unsigned int)(result)) != ((unsigned int)(a4))) goto loc_00A00C9A;
    if (a3 == (*(unsigned int *)(v_rip + 4227036))) goto loc_00A00CA5;
loc_00A00C9A:
    a2 = (unsigned int)((0) + 1);
    a1 = (v_rip + 4227036) + (24);
    if (a2 < 28) goto loc_00A00C8A;
loc_00A00CA5:
    if (a2 >= 28) goto loc_00A00CE2;
    result = v_rip - 10489015;
    v_r14 = v_r14 + result * 2 + (unsigned int)(*(unsigned int *)(v_rip - 10488831 + 14715984 + (unsigned int)(a2) + (unsigned int)(a2) * 2 * 8 + 8)) * 2;
    if (v_rip - 10489015 + 14715984 + (unsigned int)(a2) + (unsigned int)(a2) * 2 * 8 != 0) {
        a3 = *(unsigned __int64 *)(v_rip - 10489015 + 14715984 + (unsigned int)(a2) + (unsigned int)(a2) * 2 * 8);
        a2 = v_rsi;
        a1 = v_r14 + result * 2 + (unsigned int)(*(unsigned int *)(v_rip - 10488831 + 14715984 + (unsigned int)(a2) + (unsigned int)(a2) * 2 * 8 + 8)) * 2;
        result = wcscpy_s(a1, a2, a3, a4);
        result = *(unsigned int *)(v_rip - 10489015 + 14715984 + (unsigned int)(a2) + (unsigned int)(a2) * 2 * 8 + 8);
        v_rsi = (v_rsi) - (result);
        v_r11 = 0;
        v_r14 = v_r14 + result * 2 + (unsigned int)(*(unsigned int *)(v_rip - 10488831 + 14715984 + (unsigned int)(a2) + (unsigned int)(a2) * 2 * 8 + 8)) * 2 + result * 2;
    }
    goto loc_00A00C57;
loc_00A00CEA:
    *(unsigned __int64 *)(a4) = *(unsigned __int64 *)(v_rsp - 63 - 33);
loc_00A00CF0:
    *(unsigned int *)(v_r14) = (unsigned int)(*(unsigned __int64 *)(v_rsp - 63 - 33));
    goto loc_00A007BD;
loc_00A00CF8:
loc_00A00CFB:
    result = PdcCloseEvent(v_r14, a2, a3, a4);
loc_00A00D00:
    goto loc_00A007BD;
loc_00A00D0A:
    if (a2 >= ((unsigned int)(a4))) goto loc_00A00D27;
    if ((*(unsigned __int8 *)((unsigned int)(a2) + *(unsigned __int64 *)(a3 + 4) * 1)) == ((unsigned __int8)(v_rsi))) goto loc_00A00D1F;
    a2 = (unsigned int)((a2) + 1);
    goto loc_00A00D0A;
loc_00A00D1F:
    goto loc_00A005F1;
loc_00A00D27:
    goto loc_00A005FB;
loc_00A00D2F:
    if (a2 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4226688))))) goto loc_00A00D77;
    if ((*(unsigned __int8 *)((unsigned int)(a2) + *(unsigned __int64 *)(a3 + 4) * 1)) == ((unsigned __int8)(v_rip - 10489015 + 14715984 + (unsigned int)(a2) + (unsigned int)(a2) * 2 * 8))) goto loc_00A00D6F;
    a2 = (unsigned int)((a2) + ((unsigned int)(*(unsigned __int64 *)(v_rsp - 63 - 9))));
    goto loc_00A00D2F;
loc_00A00D44:
    result = PdcCloseEvent(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 41)), a2, a3, a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 41)) = v_rip - 10489015 + 14715984 + (unsigned int)(a2) + (unsigned int)(a2) * 2 * 8;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 103)) = (unsigned int)(v_rip - 10489015 + 14715984 + (unsigned int)(a2) + (unsigned int)(a2) * 2 * 8);
    goto loc_00A007BB;
loc_00A00D5A:
    goto loc_00A00CF0;
loc_00A00D61:
loc_00A00D66:
    goto loc_00A00678;
loc_00A00D6F:
    goto loc_00A00B42;
loc_00A00D77:
    goto loc_00A00B4C;
loc_00A00D7F:
    goto loc_00A007BD;
loc_00A00D89:
    result = PdcCloseEvent(v_r14, a2, a3, a4);
    goto loc_00A00CFB;
loc_00A00D99:
loc_00A00D9F:
    if (((unsigned int)((unsigned int)((unsigned int)(v_rip - 10489015 + 14715984 + (unsigned int)(a2) + (unsigned int)(a2) * 2 * 8)))) >= 32) goto loc_00A00E43;
    a3 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rip - 10489015 + 14715984 + (unsigned int)(a2) + (unsigned int)(a2) * 2 * 8)))))));
    a3 = (unsigned int)((a3) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 - 89)))));
    if (condition_is_equal) goto loc_00A00E24;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r14))) == 17) { a4 = 4; }
    a2 = 0;
loc_00A00DCF:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 4226712 + 4))) & ((unsigned int)(a4)));
    if (((unsigned int)(result)) != ((unsigned int)(a4))) goto loc_00A00DDF;
    if (a3 == (*(unsigned int *)(v_rip + 4226712))) goto loc_00A00DEA;
loc_00A00DDF:
    a2 = (unsigned int)((a2) + 1);
    a1 = (v_rip + 4226712) + (24);
    if (a2 < 28) goto loc_00A00DCF;
loc_00A00DEA:
    if (a2 >= 28) goto loc_00A00E2C;
    a2 = 0;
    if (v_rip - 10489340 + a2 + a2 * 2 * 8 + 14715984 == 0) goto loc_00A00E2C;
    result = (v_rip - 10489340 + a2 + a2 * 2 * 8 + 14715984) | (-1);
loc_00A00E13:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 10489340 + a2 + a2 * 2 * 8 + 14715984) + result * 2)) != 0) goto loc_00A00E13;
loc_00A00E24:
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(v_rip - 10489015 + 14715984 + (unsigned int)(a2) + (unsigned int)(a2) * 2 * 8))) + 1);
    goto loc_00A00D9F;
loc_00A00E2C:
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 - 25) + *(unsigned __int64 *)(v_rsp - 63 - 41) * 4) = 2;
    goto loc_00A00E43;
loc_00A00E40:
    v_r10 = (unsigned int)((20) + (20));
loc_00A00E43:
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 63 - 81))) + (6));
    v_stack_p30 = v_rsp - 63 - 41;
    v_r12 = (unsigned int)((v_r12) + ((unsigned int)(v_r10)));
    a1 = 0;
    *(unsigned int *)(v_rsp - 63 - 89) = (unsigned int)(v_r12);
    v_stack_p28 = (unsigned __int8)(*(unsigned __int8 *)(v_rsp - 63 + 135));
    result = LookupSidInTable(a1, v_rsi, *(unsigned __int64 *)(v_rsp - 63 + 111), (unsigned int)(*(unsigned int *)(v_rsp - 63 + 127)));
    v_r11 = 0;
    if (result == 0) goto loc_00A00EC2;
    result = (result) + (2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 73) + *(unsigned __int64 *)(v_rsp - 63 - 41) * 8) = result;
loc_00A00E8A:
    result = (result) | (-1);
loc_00A00E91:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 73) + *(unsigned __int64 *)(v_rsp - 63 - 41) * 8) + result * 2)) != 0) goto loc_00A00E91;
    v_r12 = (unsigned int)((v_r12 + result * 2) + (4));
    v_r15 = (unsigned int)((*(unsigned __int64 *)(v_rsp - 63 - 41)) + 1);
    *(unsigned int *)(v_rsp - 63 - 89) = (unsigned int)(v_r12);
    v_r14 = (v_r14) + (*(unsigned __int16 *)(v_r14 + 2));
    *(unsigned int *)(v_rsp - 63 - 77) = (unsigned int)(v_r15);
    goto loc_00A00532;
loc_00A00EC2:
    if ((*(unsigned __int64 *)(v_rsp - 63 - 41)) != 0) goto loc_00A01008;
    result = LocalConvertSidToStringSidW(*(unsigned __int64 *)(v_rsp - 63 - 57), (unsigned int)(*(unsigned int *)(v_rsp - 63 + 127)), *(unsigned __int64 *)(v_rsp - 63 + 111), (unsigned int)(*(unsigned int *)(v_rsp - 63 + 127)));
    v_r11 = 0;
    if (sign_flag) goto loc_00A0103C;
loc_00A00EE3:
    *(unsigned __int8 *)(v_r15 + *(unsigned __int64 *)(v_rsp - 63 - 1) * 1) = 1;
    goto loc_00A00E8A;
loc_00A00EEE:
    v_r11 = 0;
    if (((unsigned int)(v_r10)) >= 9) goto loc_00A0060F;
    result = ((unsigned int)((unsigned int)(v_r10))) << (5);
    result = (result) + (v_r15);
    if (condition_is_equal) goto loc_00A0060F;
    result = (result) | (-1);
loc_00A00F12:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(result) + result * 2)) != 0) goto loc_00A00F12;
    goto loc_00A0060F;
loc_00A00F25:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 127)) + 4))) & ((unsigned int)(*(unsigned __int64 *)(v_rsp - 63 + 111))));
    if (((unsigned int)(result)) != ((unsigned int)(*(unsigned __int64 *)(v_rsp - 63 + 111)))) goto loc_00A00F35;
    if (((unsigned int)(v_r12 + result * 2)) == (*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 127))))) goto loc_00A00F40;
loc_00A00F35:
    a1 = (unsigned int)((*(unsigned __int64 *)(result)) + 1);
    a2 = ((unsigned int)(*(unsigned int *)(v_rsp - 63 + 127))) + (24);
    if (((unsigned int)(a1)) < 28) goto loc_00A00F25;
loc_00A00F40:
    if (((unsigned int)(a1)) >= 28) goto loc_00A00D99;
    if (v_rip - 10489686 + 14715984 + (unsigned int)((unsigned int)(a1)) + (unsigned int)((unsigned int)(a1)) * 2 * 8 == 0) goto loc_00A00D99;
    *(unsigned int *)(v_r11 + v_r15 * 4) = 1;
    v_r10 = (v_r10) | (-1);
loc_00A00F79:
    v_r10 = (v_r10) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 10489686 + 14715984 + (unsigned int)((unsigned int)(a1)) + (unsigned int)((unsigned int)(a1)) * 2 * 8) + v_r10 * 2)) != ((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 127))))) goto loc_00A00F79;
    goto loc_00A00E40;
loc_00A00F88:
    v_r11 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 127)))) >= 9) goto loc_00A008DC;
    v_rbx = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 127))))) << (5);
    v_rbx = (v_rbx) + (v_rip + 4225521);
    if (condition_is_equal) goto loc_00A008DC;
    result = wcscpy_s(v_r14, *(unsigned __int64 *)(v_rsp - 63 + 71), *(unsigned __int64 *)(v_rbx), (unsigned int)(*(unsigned int *)(v_rsp - 63 + 127)));
    v_rsi = (*(unsigned __int64 *)(v_rsp - 63 + 71)) - ((unsigned int)(*(unsigned int *)(v_rbx + 8)));
    goto loc_00A008D9;
loc_00A00FC9:
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 127))) = *(unsigned __int64 *)(v_rsp - 63 - 33);
    *(unsigned int *)(v_r14 + (unsigned int)(*(unsigned int *)(v_rbx + 8)) * 2) = (unsigned int)(*(unsigned __int64 *)(v_rsp - 63 - 33));
    goto loc_00A004B3;
loc_00A00FD4:
    a2 = 0;
    goto loc_00A005DB;
loc_00A00FDB:
    v_rbx = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 - 25) + v_r15 * 4) = 0;
    a3 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 127))));
    if ((*(unsigned __int8 *)(v_r14 + (unsigned int)(*(unsigned int *)(v_rbx + 8)) * 2)) == 17) { a3 = (unsigned int)(v_rbx + 4); }
    goto loc_00A00F25;
loc_00A01008:
    result = SddlpAlloc(6, v_rip + 4226166, a3, (unsigned int)(*(unsigned int *)(v_rsp - 63 + 127)));
    v_r11 = 0;
    *(unsigned __int64 *)(v_rbx) = result;
    result = wcscpy_s(result, v_r11 + 3, v_rip - 10416948, (unsigned int)(*(unsigned int *)(v_rsp - 63 + 127)));
    v_r11 = 0;
    goto loc_00A00EE3;
loc_00A0103C:
    result = RtlNtStatusToDosError((unsigned int)((unsigned int)(result)), v_r11 + 3, v_rip - 10416948, (unsigned int)(*(unsigned int *)(v_rsp - 63 + 127)));
    v_r11 = 0;
    goto loc_00A00667;
loc_00A01050:
    goto loc_00A00678;
loc_00A0105A:
    v_r12 = (unsigned int)((v_r12 + result * 2) + 1);
    *(unsigned int *)(v_rsp - 63 - 89) = (unsigned int)(v_r12);
    goto loc_00A007E3;
loc_00A01066:
    goto loc_00A0067C;
loc_00A0106E:
    result = SddlpUuidToString(v_r12, v_rsp - 63 - 49, v_rip - 10416948, (unsigned int)(*(unsigned int *)(v_rsp - 63 + 127)));
    v_r11 = 0;
    if ((unsigned int)(result) == 0) goto loc_00A00D66;
    v_rbx = ((unsigned int)(*(unsigned int *)(v_rsp - 63 + 127))) | (-1);
loc_00A01092:
    result = SddlpUuidToString(*(unsigned __int64 *)(v_rsp - 63 - 33), v_rsp - 63 - 49, *(unsigned __int64 *)(v_rsp - 63 - 49), (unsigned int)(*(unsigned int *)(v_rsp - 63 + 127)));
    v_r11 = 0;
    if ((unsigned int)(result) == 0) goto loc_00A00D66;
    v_rbx = (v_rbx) | (-1);
}
```

## 5. (Beta) C Style

```c
int64_t LocalConvertAclToString(void *Arg1, uint8_t Arg2, uint8_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint8_t v_stack_p40;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(void **)(local_rsp + 0x20) = Arg4;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (176);
    local_r13 = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x59) = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x11) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x31) = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x55) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x39) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x29) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x41) = 0;
    if (Arg4 == NULL) goto loc_00A00D7F;
    if (*(uint64_t *)(local_rsp - 0x3F + 0x67) == 0) goto loc_00A00D7F;
    if (Arg2 == 0) goto loc_00A00FC9;
    if (Arg1 != NULL) goto loc_00A004BA;
    *(uint64_t *)(arg4) = 0;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x67)) = (uint32_t)(Arg1 + 36);
    result = SddlpAlloc(Arg1 + 36, Arg2, Arg3, Arg4);
    *(uint64_t *)(arg4) = result;
    if (result == 0) goto loc_00A00D5A;
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm1;
    *(uint32_t *)(result + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x9EE808)));
loc_00A004B3:
    result = 0;
    goto loc_00A007BD;
loc_00A004BA:
    if ((uint16_t)(*(uint16_t *)((uint32_t)(*(uint32_t *)(v_rip - 0x9EE808)) + 0x4)) == 0) goto loc_00A00CEA;
    Arg3 = (uint8_t)(-(Arg3));
    Arg1 = ((uint32_t)((uint32_t)(*(uint16_t *)((uint32_t)(*(uint32_t *)(v_rip - 0x9EE808)) + 0x4)))) << (3);
    local_rbx = (uint32_t)((Arg4) + (2));
    *(uint32_t *)(local_rsp - 0x3F + 0x7F) = (uint32_t)(local_rbx);
    result = SddlpAlloc(Arg1, Arg2, Arg3, Arg4);
    *(uint64_t *)(local_rsp - 0x3F - 0x49) = result;
    if (result == 0) goto loc_00A00D00;
    result = SddlpAlloc(*(uint16_t *)(arg1 + 0x4), Arg2, Arg3, Arg4);
    *(uint64_t *)(local_rsp - 0x3F - 0x1) = result;
    if (result == 0) goto loc_00A00CF8;
    Arg1 = (*(uint16_t *)(arg1 + 0x4)) << (2);
    result = SddlpAlloc(Arg1, Arg2, Arg3, Arg4);
    local_r11 = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x19) = result;
    if (result == 0) goto loc_00A00D89;
    *(uint32_t *)(local_rsp - 0x3F - 0x4D) = 0;
loc_00A00532:
    if (0 >= ((uint32_t)(*(uint16_t *)(arg1 + 0x4)))) goto loc_00A00667;
    local_r12 = (uint32_t)((0) + (2));
    *(uint32_t *)(local_rsp - 0x3F - 0x59) = (uint32_t)(local_r12);
loc_00A0055C:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x40856B + 0x4))) & ((uint32_t)(local_rbx)));
    if (((uint32_t)(result)) != ((uint32_t)(local_rbx))) goto loc_00A00569;
    if (((uint32_t)(*(uint8_t *)(arg1 + 0x8))) == (*(uint32_t *)(v_rip + 0x40856B))) goto loc_00A00574;
loc_00A00569:
    Arg2 = (uint32_t)((0) + 1);
    Arg1 = (v_rip + 4228459) + (24);
    if (Arg2 < 17) goto loc_00A0055C;
loc_00A00574:
    if (Arg2 >= 17) goto loc_00A00662;
    result = ((uint32_t)(Arg2) + (uint32_t)(Arg2) * 2 * 8 + 14715568) + (v_rip - 10487101);
    if (condition_is_equal) goto loc_00A00662;
    result = (result) | (-1);
loc_00A0059B:
    result = (result) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(result) + result * 2)) != 0) goto loc_00A0059B;
    local_r12 = (uint32_t)((local_r12 + result * 2) + (2));
loc_00A005BC:
    local_r11 = (uint32_t)((1) << (0));
    if ((((uint32_t)(local_r11)) & ((uint32_t)(*(uint8_t *)(arg1 + 0x8 + 0x1)))) == 0) goto loc_00A0060C;
    Arg2 = 0;
loc_00A005DB:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x4083CE - 0x4))) & ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F)))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F))))) goto loc_00A005FB;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4083CE))) != 0) goto loc_00A00D0A;
loc_00A005F1:
    if (((uint32_t)(local_r11)) == (*(uint32_t *)(v_rip + 0x4083CE - 0x8))) goto loc_00A00EEE;
loc_00A005FB:
    local_r10 = (uint32_t)((0) + 1);
    Arg3 = (v_rip + 4228046) + (32);
    if (((uint32_t)(local_r10)) < 9) goto loc_00A00FD4;
loc_00A0060C:
    local_r11 = 0;
loc_00A0060F:
    local_rbx = (uint32_t)((0) + 1);
    if (((uint32_t)(local_rbx)) < ((uint32_t)(local_r11 + 8))) goto loc_00A005BC;
    local_r12 = (uint32_t)((local_r12) + (2));
    *(uint32_t *)(local_rsp - 0x3F - 0x59) = (uint32_t)(local_r12);
    *(uint32_t *)(local_rsp - 0x3F - 0x51) = (uint32_t)(local_r12);
    if (((uint32_t)(*(uint8_t *)(arg1 + 0x8))) <= 9) goto loc_00A00685;
    Arg1 = (uint32_t)((*(uint8_t *)(arg1 + 0x8)) - (10));
    if (condition_is_equal) goto loc_00A006BF;
    Arg1 = (uint32_t)((Arg1) - (1));
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00A006BF;
    Arg1 = (uint32_t)((Arg1) - (4));
    if (condition_is_equal) goto loc_00A006BF;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A006BF;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A006BF;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A006BF;
    if (((uint32_t)(Arg1)) == 1) goto loc_00A006BF;
loc_00A0065F:
loc_00A00662:
loc_00A00667:
    if ((uint32_t)(local_r12) == 0) goto loc_00A01050;
    if ((uint32_t)((uint32_t)(0x538ULL)) == 0) goto loc_00A007D9;
loc_00A00678:
loc_00A0067C:
    goto loc_00A00752;
loc_00A00685:
    if ((uint32_t)((uint32_t)(0x538ULL)) == 0) goto loc_00A006BF;
    if ((uint32_t)(Arg1) == 0) goto loc_00A006BF;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A006BF;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A006BF;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A006BF;
    Arg1 = (uint32_t)((Arg1) - (2));
    Arg1 = (uint32_t)((Arg1) - (1));
    Arg1 = (uint32_t)((Arg1) - (1));
    if (((uint32_t)(Arg1)) != 1) goto loc_00A0065F;
loc_00A006BF:
    *(void **)(local_rsp - 0x3F - 0x39) = Arg1 + 8 + 8;
    *(uint32_t *)(local_rsp - 0x3F - 0x55) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8 + 0x4)));
    if (*(uint64_t *)(local_rsp - 0x3F - 0x41) != 0) {
        Arg1 = *(uint64_t *)(local_rsp - 0x3F - 0x41);
        result = PdcCloseEvent(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_rip + 0x4083CE)));
        local_r11 = 0;
        *(uint64_t *)(local_rsp - 0x3F - 0x41) = 0;
    }
    v_stack_mA8 = (uint8_t)(*(uint8_t *)(local_rsp - 0x3F + 0x87));
    v_stack_mB0 = 0;
    v_stack_mB8 = *(uint64_t *)(local_rsp - 0x3F + 0x77);
    v_stack_mC0 = *(uint64_t *)(local_rsp - 0x3F + 0x6F);
    v_stack_mC8 = local_rsp - 63 - 81;
    *(uint32_t *)(local_rsp - 0x3F - 0x4D) = 0;
    result = LocalGetAceCondition(Arg1 + 8, Arg1 + 8 + 8, local_rsp - 63 - 65, local_rsp - 63 - 77);
    local_r11 = 0;
    if ((uint32_t)(result) == 0) goto loc_00A00FDB;
    *(uint32_t *)(local_rsp - 0x3F - 0x59) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x51)));
    goto loc_00A00667;
loc_00A00745:
loc_00A00752:
    if (0 >= (*(uint16_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x47) + 0x4))) goto loc_00A00787;
loc_00A00764:
    if ((*(uint8_t *)(0 + *(uint64_t *)(local_rsp - 0x3F - 0x1) * 1)) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x49) + 0x0 * 8);
        result = PdcCloseEvent(Arg1, Arg1 + 8 + 8, local_rsp - 63 - 65, local_rsp - 63 - 77);
        local_r11 = 0;
    }
    local_rbx = (uint32_t)((0) + 1);
    if (((uint32_t)(local_rbx)) < ((uint32_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x47) + 0x4)))) goto loc_00A00764;
loc_00A00787:
    result = PdcCloseEvent(*(uint64_t *)(local_rsp - 0x3F - 0x49), Arg1 + 8 + 8, local_rsp - 63 - 65, local_rsp - 63 - 77);
    result = PdcCloseEvent(*(uint64_t *)(local_rsp - 0x3F - 0x1), Arg1 + 8 + 8, local_rsp - 63 - 65, local_rsp - 63 - 77);
    result = PdcCloseEvent(*(uint64_t *)(local_rsp - 0x3F - 0x19), Arg1 + 8 + 8, local_rsp - 63 - 65, local_rsp - 63 - 77);
    result = PdcCloseEvent(*(uint64_t *)(local_rsp - 0x3F - 0x41), Arg1 + 8 + 8, local_rsp - 63 - 65, local_rsp - 63 - 77);
    local_rbx = 0;
    if ((uint32_t)((uint32_t)(0x538ULL)) != 0) goto loc_00A00D44;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x67)) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x59)));
loc_00A007BB:
loc_00A007BD:
    local_rsp = (local_rsp) + (176);
    return (uint32_t)((uint32_t)((uint32_t)(0x538ULL)));
loc_00A007D9:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x59)))) & (1)) != 0) goto loc_00A0105A;
loc_00A007E3:
    result = SddlpAlloc((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x59)))), Arg1 + 8 + 8, local_rsp - 63 - 65, local_rsp - 63 - 77);
    local_r11 = 0;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x5F)) = result;
    if (result == 0) goto loc_00A01066;
    local_rsi = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x59))))) >> (1);
    *(uint32_t *)(local_rsp - 0x3F - 0x51) = 0;
loc_00A00816:
    *(uint64_t *)(local_rsp - 0x3F - 0x29) = *(uint64_t *)(local_rsp - 0x3F + 0x47) + 8;
    if (0 >= ((uint32_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x47) + 0x4)))) goto loc_00A00D66;
    if (local_rsi == 0) goto loc_00A00D61;
    *(uint16_t *)(result) = 40;
    local_r14 = (result) + (2);
    local_rsi = (local_rsi) - (59 - 58);
loc_00A00855:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x408271 + 0x4))) & ((uint32_t)(v_stack_p10)));
    if (((uint32_t)(result)) != ((uint32_t)(v_stack_p10))) goto loc_00A00863;
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x47) + 0x8))) == (*(uint32_t *)(v_rip + 0x408271))) goto loc_00A0086F;
loc_00A00863:
    Arg1 = (uint32_t)((0) + ((uint32_t)(59 - 58)));
    Arg2 = (v_rip + 4227697) + (24);
    if (((uint32_t)(Arg1)) < 17) goto loc_00A00855;
loc_00A0086F:
    if (((uint32_t)(Arg1)) >= 17) goto loc_00A008B0;
    result = v_rip - 10487937;
    if (v_rip - 10487937 + 14715568 + (uint32_t)((uint32_t)(Arg1)) + (uint32_t)((uint32_t)(Arg1)) * 2 * 8 != 0) {
        Arg3 = *(uint64_t *)(v_rip - 0xA00881 + 0xE08AB0 + (uint32_t)((uint32_t)(arg1)) + (uint32_t)((uint32_t)(arg1)) * 2 * 8);
        Arg2 = local_rsi;
        Arg1 = local_r14;
        result = wcscpy_s(Arg1, Arg2, Arg3, 59);
        result = *(uint32_t *)(v_rip - 0xA00881 + 0xE08AB0 + (uint32_t)((uint32_t)(arg1)) + (uint32_t)((uint32_t)(arg1)) * 2 * 8 + 0x8);
        local_rsi = (local_rsi) - (result);
        local_r11 = 0;
        local_r14 = local_r14 + result * 2;
        Arg4 = local_r11 + 59;
    }
    if (local_rsi == 0) goto loc_00A00D61;
    *(uint16_t *)(local_r14) = (uint16_t)(Arg4);
    local_r14 = (local_r14) + (2);
    local_rsi = (local_rsi) - (59 - 58);
loc_00A008C7:
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(59 - 58))) << (0));
    if (((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x47) + 0x8 + 0x1)) & ((uint8_t)(local_r11))) != 0) goto loc_00A00B1A;
loc_00A008D9:
    local_r11 = 0;
loc_00A008DC:
    local_rdi = (uint32_t)((0) + ((uint32_t)(59 - 58)));
    if (((uint32_t)(local_rdi)) < ((uint32_t)(*(uint64_t *)(local_rsp - 0x3F - 0x49)))) goto loc_00A008C7;
    if (local_rsi == 0) goto loc_00A00D61;
    *(uint16_t *)(local_r14) = 59;
    local_rsi = (local_rsi) - (59 - 58);
    local_r14 = (local_r14) + (2);
    *(uint64_t *)(local_rsp - 0x3F - 0x9) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x21) = 0;
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x47) + 0x8))) <= 9) goto loc_00A0094E;
    Arg1 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x47) + 0x8)) - (10));
    if (condition_is_equal) goto loc_00A0093D;
    Arg1 = (uint32_t)((Arg1) - (1));
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00A0093D;
    Arg1 = (uint32_t)((Arg1) - (4));
    if (condition_is_equal) goto loc_00A0093D;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A0093D;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A0093D;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A0093D;
    if (((uint32_t)(Arg1)) != 1) goto loc_00A00987;
loc_00A0093D:
    *(uint64_t *)(local_rsp - 0x3F - 0x39) = *(uint64_t *)(local_rsp - 0x3F + 0x47) + 8 + 8;
    *(uint32_t *)(local_rsp - 0x3F - 0x55) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x47) + 0x8 + 0x4)));
    goto loc_00A0098B;
loc_00A0094E:
    if (((uint32_t)(Arg1)) == 1) goto loc_00A0093D;
    if ((uint32_t)(Arg1) == 0) goto loc_00A0093D;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A0093D;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A0093D;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A0093D;
    Arg1 = (uint32_t)((Arg1) - (2));
    Arg1 = (uint32_t)((Arg1) - (1));
    Arg1 = (uint32_t)((Arg1) - (1));
loc_00A00987:
loc_00A0098B:
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x47) + 0x8 + 0x4));
    if (*(uint64_t *)(local_rsp - 0x3F - 0x41) != 0) {
        Arg1 = *(uint64_t *)(local_rsp - 0x3F - 0x41);
        result = PdcCloseEvent(Arg1, Arg2, Arg3, Arg4);
        local_r11 = 0;
        *(uint64_t *)(local_rsp - 0x3F - 0x41) = 0;
    }
    v_stack_p40 = (uint8_t)(*(uint8_t *)(local_rsp - 0x3F + 0x87));
    v_stack_p38 = 0;
    v_stack_p30 = *(uint64_t *)(local_rsp - 0x3F + 0x77);
    v_stack_p28 = *(uint64_t *)(local_rsp - 0x3F + 0x6F);
    v_stack_p20 = local_rsp - 63 - 17;
    *(uint32_t *)(local_rsp - 0x3F - 0x4D) = 0;
    result = LocalGetAceCondition(*(uint64_t *)(local_rsp - 0x3F + 0x47) + 8, *(uint64_t *)(local_rsp - 0x3F - 0x39), local_rsp - 63 - 65, local_rsp - 63 - 77);
    local_r11 = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x4D) = (uint32_t)(result);
    if ((uint32_t)(result) != 0) goto loc_00A00D66;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x19) + (uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x51)) * 4)))) != 2) goto loc_00A00BA2;
    result = wcscpy_s(local_r14, local_rsi, v_rip - 10403734, local_rsp - 63 - 77);
    local_r14 = (local_r14) + (4);
    local_rsi = (local_rsi) - (2);
    result = ultow_s((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x55)), local_r14, local_rsi, (uint32_t)((uint32_t)(result)) + 16);
    result = (result) | (-1);
    local_r11 = 0;
loc_00A00A3A:
    result = (result) + 1;
    if ((*(uint16_t *)(local_r14 + result * 2)) != 0) goto loc_00A00A3A;
    local_rsi = (local_rsi) - (result);
loc_00A00A4B:
    if (local_rsi == 0) goto loc_00A00D61;
    local_rsi = (local_rsi) - 1;
    *(uint16_t *)(local_r14 + result * 2) = 59;
    local_r14 = (local_r14 + result * 2) + (2);
    if (0 != 0) goto loc_00A0106E;
    if (local_rsi == 0) goto loc_00A00D61;
    *(uint16_t *)(local_r14) = 59;
    local_rsi = (local_rsi) - 1;
    local_r14 = (local_r14) + (2);
    if (0 != 0) goto loc_00A01092;
    if (local_rsi == 0) goto loc_00A00745;
    local_rsi = (local_rsi) - 1;
    *(uint16_t *)(local_r14) = 59;
    local_r14 = (local_r14) + (2);
    result = wcscpy_s(local_r14, local_rsi, *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x49) + (uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x51)) * 8), (uint32_t)((uint32_t)(result)) + 16);
    result = (result) | (-1);
    local_r11 = 0;
loc_00A00AC0:
    result = (result) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x49) + (uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x51)) * 8) + result * 2)) != 0) goto loc_00A00AC0;
    local_rsi = (local_rsi) - (result);
    if (*(uint64_t *)(local_rsp - 0x3F - 0x41) != 0) goto loc_00A00B61;
loc_00A00ADE:
    if (local_rsi <= 1) goto loc_00A00745;
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x51))) + 1);
    *(uint16_t *)(local_r14 + result * 2) = 41;
    local_rsi = (local_rsi) - 1;
    local_r14 = (local_r14 + result * 2) + (2);
    *(uint32_t *)(local_rsp - 0x3F - 0x51) = (uint32_t)(local_r12);
    *(uint16_t *)(local_r14) = 0;
    local_r15 = (*(uint64_t *)(local_rsp - 0x3F + 0x47) + 8) + (*(uint16_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x47) + 0x8 + 0x2));
    goto loc_00A00816;
loc_00A00B1A:
    Arg2 = 0;
loc_00A00B2C:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x407E80 - 0x4))) & ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F)))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F))))) goto loc_00A00B4C;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x407E80))) != 0) goto loc_00A00D2F;
loc_00A00B42:
    if (0 == (*(uint32_t *)(v_rip + 0x407E80 - 0x8))) goto loc_00A00F88;
loc_00A00B4C:
    Arg4 = (uint32_t)((0) + ((uint32_t)(local_r12)));
    Arg3 = (v_rip + 4226688) + (32);
    if (((uint32_t)(Arg4)) >= 9) goto loc_00A008D9;
    Arg2 = 0;
    goto loc_00A00B2C;
loc_00A00B61:
    if (local_rsi == 0) goto loc_00A00745;
    *(uint16_t *)(local_r14) = 59;
    local_rsi = (local_rsi) - 1;
    local_r14 = (local_r14) + (2);
    result = wcscpy_s(local_r14, local_rsi, *(uint8_t *)(local_r15), Arg4);
    result = (result) | (-1);
    local_r11 = 0;
loc_00A00B8C:
    result = (result) + 1;
    if ((*(uint16_t *)(*(uint8_t *)(local_r15) + result * 2)) != 0) goto loc_00A00B8C;
    local_rsi = (local_rsi) - (result);
    goto loc_00A00ADE;
loc_00A00BA2:
    if (((uint32_t)(result)) != 1) goto loc_00A00C33;
    Arg3 = (uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F));
    if ((*(uint8_t *)(local_r15)) == 17) { Arg3 = 4; }
loc_00A00BCA:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x4080A6 + 0x4))) & (Arg3));
    if (((uint32_t)(result)) != Arg3) goto loc_00A00BDA;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x55)))) == (*(uint32_t *)(v_rip + 0x4080A6))) goto loc_00A00BE5;
loc_00A00BDA:
    Arg2 = (uint32_t)((0) + 1);
    Arg1 = (v_rip + 4227238) + (24);
    if (Arg2 < 28) goto loc_00A00BCA;
loc_00A00BE5:
    if (Arg2 >= 28) goto loc_00A00A4B;
    if (v_rip - 10488831 + 14715984 + (uint32_t)(Arg2) + (uint32_t)(Arg2) * 2 * 8 == 0) goto loc_00A00A4B;
    result = wcscpy_s(local_r14 + result * 2, local_rsi, *(uint64_t *)(v_rip - 0xA00BFF + 0xE08C50 + (uint32_t)(Arg2) + (uint32_t)(Arg2) * 2 * 8), Arg4);
    local_rsi = (local_rsi) - ((uint32_t)(*(uint32_t *)(v_rip - 0xA00BFF + 0xE08C50 + (uint32_t)(Arg2) + (uint32_t)(Arg2) * 2 * 8 + 0x8)));
    local_r11 = 0;
    goto loc_00A00A4B;
loc_00A00C33:
loc_00A00C46:
    Arg3 = (uint32_t)((1) << (0));
    Arg3 = (uint32_t)((Arg3) & ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x55)))));
    if (condition_is_not_equal) goto loc_00A00C74;
loc_00A00C57:
    local_r15 = (uint32_t)((0) + 1);
    if (((uint32_t)(local_r15)) < 32) goto loc_00A00C46;
    goto loc_00A00A4B;
loc_00A00C74:
    Arg4 = (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x3F - 0x21)));
    if ((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x9))) == 17) { Arg4 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x4D))); }
loc_00A00C8A:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x407FDC + 0x4))) & ((uint32_t)(Arg4)));
    if (((uint32_t)(result)) != ((uint32_t)(Arg4))) goto loc_00A00C9A;
    if (Arg3 == (*(uint32_t *)(v_rip + 0x407FDC))) goto loc_00A00CA5;
loc_00A00C9A:
    Arg2 = (uint32_t)((0) + 1);
    Arg1 = (v_rip + 4227036) + (24);
    if (Arg2 < 28) goto loc_00A00C8A;
loc_00A00CA5:
    if (Arg2 >= 28) goto loc_00A00CE2;
    result = v_rip - 10489015;
    local_r14 = local_r14 + result * 2 + (uint32_t)(*(uint32_t *)(v_rip - 0xA00BFF + 0xE08C50 + (uint32_t)(Arg2) + (uint32_t)(Arg2) * 2 * 8 + 0x8)) * 2;
    if (v_rip - 10489015 + 14715984 + (uint32_t)(Arg2) + (uint32_t)(Arg2) * 2 * 8 != 0) {
        Arg3 = *(uint64_t *)(v_rip - 0xA00CB7 + 0xE08C50 + (uint32_t)(Arg2) + (uint32_t)(Arg2) * 2 * 8);
        Arg2 = local_rsi;
        Arg1 = local_r14 + result * 2 + (uint32_t)(*(uint32_t *)(v_rip - 0xA00BFF + 0xE08C50 + (uint32_t)(Arg2) + (uint32_t)(Arg2) * 2 * 8 + 0x8)) * 2;
        result = wcscpy_s(Arg1, Arg2, Arg3, Arg4);
        result = *(uint32_t *)(v_rip - 0xA00CB7 + 0xE08C50 + (uint32_t)(Arg2) + (uint32_t)(Arg2) * 2 * 8 + 0x8);
        local_rsi = (local_rsi) - (result);
        local_r11 = 0;
        local_r14 = local_r14 + result * 2 + (uint32_t)(*(uint32_t *)(v_rip - 0xA00BFF + 0xE08C50 + (uint32_t)(Arg2) + (uint32_t)(Arg2) * 2 * 8 + 0x8)) * 2 + result * 2;
    }
    goto loc_00A00C57;
loc_00A00CEA:
    *(uint64_t *)(arg4) = *(uint64_t *)(local_rsp - 0x3F - 0x21);
loc_00A00CF0:
    *(uint32_t *)(local_r14) = (uint32_t)(*(uint64_t *)(local_rsp - 0x3F - 0x21));
    goto loc_00A007BD;
loc_00A00CF8:
loc_00A00CFB:
    result = PdcCloseEvent(local_r14, Arg2, Arg3, Arg4);
loc_00A00D00:
    goto loc_00A007BD;
loc_00A00D0A:
    if (Arg2 >= ((uint32_t)(Arg4))) goto loc_00A00D27;
    if ((*(uint8_t *)((uint32_t)(Arg2) + *(uint64_t *)(Arg3 + 0x4) * 1)) == ((uint8_t)(local_rsi))) goto loc_00A00D1F;
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_00A00D0A;
loc_00A00D1F:
    goto loc_00A005F1;
loc_00A00D27:
    goto loc_00A005FB;
loc_00A00D2F:
    if (Arg2 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x407E80))))) goto loc_00A00D77;
    if ((*(uint8_t *)((uint32_t)(Arg2) + *(uint64_t *)(Arg3 + 0x4) * 1)) == ((uint8_t)(v_rip - 10489015 + 14715984 + (uint32_t)(Arg2) + (uint32_t)(Arg2) * 2 * 8))) goto loc_00A00D6F;
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(*(uint64_t *)(local_rsp - 0x3F - 0x9))));
    goto loc_00A00D2F;
loc_00A00D44:
    result = PdcCloseEvent(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x29)), Arg2, Arg3, Arg4);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x29)) = v_rip - 10489015 + 14715984 + (uint32_t)(Arg2) + (uint32_t)(Arg2) * 2 * 8;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x67)) = (uint32_t)(v_rip - 10489015 + 14715984 + (uint32_t)(Arg2) + (uint32_t)(Arg2) * 2 * 8);
    goto loc_00A007BB;
loc_00A00D5A:
    goto loc_00A00CF0;
loc_00A00D61:
loc_00A00D66:
    goto loc_00A00678;
loc_00A00D6F:
    goto loc_00A00B42;
loc_00A00D77:
    goto loc_00A00B4C;
loc_00A00D7F:
    goto loc_00A007BD;
loc_00A00D89:
    result = PdcCloseEvent(local_r14, Arg2, Arg3, Arg4);
    goto loc_00A00CFB;
loc_00A00D99:
loc_00A00D9F:
    if (((uint32_t)((uint32_t)((uint32_t)(v_rip - 10489015 + 14715984 + (uint32_t)(Arg2) + (uint32_t)(Arg2) * 2 * 8)))) >= 32) goto loc_00A00E43;
    Arg3 = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_rip - 10489015 + 14715984 + (uint32_t)(Arg2) + (uint32_t)(Arg2) * 2 * 8)))))));
    Arg3 = (uint32_t)((Arg3) & ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x59)))));
    if (condition_is_equal) goto loc_00A00E24;
    if (((uint8_t)(*(uint8_t *)(local_r14))) == 17) { Arg4 = 4; }
    Arg2 = 0;
loc_00A00DCF:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x407E98 + 0x4))) & ((uint32_t)(Arg4)));
    if (((uint32_t)(result)) != ((uint32_t)(Arg4))) goto loc_00A00DDF;
    if (Arg3 == (*(uint32_t *)(v_rip + 0x407E98))) goto loc_00A00DEA;
loc_00A00DDF:
    Arg2 = (uint32_t)((Arg2) + 1);
    Arg1 = (v_rip + 4226712) + (24);
    if (Arg2 < 28) goto loc_00A00DCF;
loc_00A00DEA:
    if (Arg2 >= 28) goto loc_00A00E2C;
    Arg2 = 0;
    if (v_rip - 10489340 + Arg2 + Arg2 * 2 * 8 + 14715984 == 0) goto loc_00A00E2C;
    result = (v_rip - 10489340 + Arg2 + Arg2 * 2 * 8 + 14715984) | (-1);
loc_00A00E13:
    result = (result) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_rip - 0xA00DFC + Arg2 + Arg2 * 2 * 8 + 0xE08C50) + result * 2)) != 0) goto loc_00A00E13;
loc_00A00E24:
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(v_rip - 10489015 + 14715984 + (uint32_t)(Arg2) + (uint32_t)(Arg2) * 2 * 8))) + 1);
    goto loc_00A00D9F;
loc_00A00E2C:
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x19) + *(uint64_t *)(local_rsp - 0x3F - 0x29) * 4) = 2;
    goto loc_00A00E43;
loc_00A00E40:
    local_r10 = (uint32_t)((20) + (20));
loc_00A00E43:
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x51))) + (6));
    v_stack_p30 = local_rsp - 63 - 41;
    local_r12 = (uint32_t)((local_r12) + ((uint32_t)(local_r10)));
    Arg1 = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x59) = (uint32_t)(local_r12);
    v_stack_p28 = (uint8_t)(*(uint8_t *)(local_rsp - 0x3F + 0x87));
    result = LookupSidInTable(Arg1, local_rsi, *(uint64_t *)(local_rsp - 0x3F + 0x6F), (uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F)));
    local_r11 = 0;
    if (result == 0) goto loc_00A00EC2;
    result = (result) + (2);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x49) + *(uint64_t *)(local_rsp - 0x3F - 0x29) * 8) = result;
loc_00A00E8A:
    result = (result) | (-1);
loc_00A00E91:
    result = (result) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x49) + *(uint64_t *)(local_rsp - 0x3F - 0x29) * 8) + result * 2)) != 0) goto loc_00A00E91;
    local_r12 = (uint32_t)((local_r12 + result * 2) + (4));
    local_r15 = (uint32_t)((*(uint64_t *)(local_rsp - 0x3F - 0x29)) + 1);
    *(uint32_t *)(local_rsp - 0x3F - 0x59) = (uint32_t)(local_r12);
    local_r14 = (local_r14) + (*(uint16_t *)(local_r14 + 0x2));
    *(uint32_t *)(local_rsp - 0x3F - 0x4D) = (uint32_t)(local_r15);
    goto loc_00A00532;
loc_00A00EC2:
    if ((*(uint64_t *)(local_rsp - 0x3F - 0x29)) != 0) goto loc_00A01008;
    result = LocalConvertSidToStringSidW(*(uint64_t *)(local_rsp - 0x3F - 0x39), (uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F)), *(uint64_t *)(local_rsp - 0x3F + 0x6F), (uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F)));
    local_r11 = 0;
    if (sign_flag) goto loc_00A0103C;
loc_00A00EE3:
    *(uint8_t *)(local_r15 + *(uint64_t *)(local_rsp - 0x3F - 0x1) * 1) = 1;
    goto loc_00A00E8A;
loc_00A00EEE:
    local_r11 = 0;
    if (((uint32_t)(local_r10)) >= 9) goto loc_00A0060F;
    result = ((uint32_t)((uint32_t)(local_r10))) << (5);
    result = (result) + (local_r15);
    if (condition_is_equal) goto loc_00A0060F;
    result = (result) | (-1);
loc_00A00F12:
    result = (result) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(result) + result * 2)) != 0) goto loc_00A00F12;
    goto loc_00A0060F;
loc_00A00F25:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F)) + 0x4))) & ((uint32_t)(*(uint64_t *)(local_rsp - 0x3F + 0x6F))));
    if (((uint32_t)(result)) != ((uint32_t)(*(uint64_t *)(local_rsp - 0x3F + 0x6F)))) goto loc_00A00F35;
    if (((uint32_t)(local_r12 + result * 2)) == (*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F))))) goto loc_00A00F40;
loc_00A00F35:
    Arg1 = (uint32_t)((*(uint64_t *)(result)) + 1);
    Arg2 = ((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F))) + (24);
    if (((uint32_t)(Arg1)) < 28) goto loc_00A00F25;
loc_00A00F40:
    if (((uint32_t)(Arg1)) >= 28) goto loc_00A00D99;
    if (v_rip - 10489686 + 14715984 + (uint32_t)((uint32_t)(Arg1)) + (uint32_t)((uint32_t)(Arg1)) * 2 * 8 == 0) goto loc_00A00D99;
    *(uint32_t *)(local_r11 + local_r15 * 4) = 1;
    local_r10 = (local_r10) | (-1);
loc_00A00F79:
    local_r10 = (local_r10) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_rip - 0xA00F56 + 0xE08C50 + (uint32_t)((uint32_t)(arg1)) + (uint32_t)((uint32_t)(arg1)) * 2 * 8) + local_r10 * 2)) != ((uint16_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F))))) goto loc_00A00F79;
    goto loc_00A00E40;
loc_00A00F88:
    local_r11 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F)))) >= 9) goto loc_00A008DC;
    local_rbx = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F))))) << (5);
    local_rbx = (local_rbx) + (v_rip + 4225521);
    if (condition_is_equal) goto loc_00A008DC;
    result = wcscpy_s(local_r14, *(uint64_t *)(local_rsp - 0x3F + 0x47), *(uint64_t *)(local_rbx), (uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F)));
    local_rsi = (*(uint64_t *)(local_rsp - 0x3F + 0x47)) - ((uint32_t)(*(uint32_t *)(local_rbx + 0x8)));
    goto loc_00A008D9;
loc_00A00FC9:
    *(uint64_t *)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F))) = *(uint64_t *)(local_rsp - 0x3F - 0x21);
    *(uint32_t *)(local_r14 + (uint32_t)(*(uint32_t *)(local_rbx + 0x8)) * 2) = (uint32_t)(*(uint64_t *)(local_rsp - 0x3F - 0x21));
    goto loc_00A004B3;
loc_00A00FD4:
    Arg2 = 0;
    goto loc_00A005DB;
loc_00A00FDB:
    local_rbx = 0;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x19) + local_r15 * 4) = 0;
    Arg3 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F))));
    if ((*(uint8_t *)(local_r14 + (uint32_t)(*(uint32_t *)(local_rbx + 0x8)) * 2)) == 17) { Arg3 = (uint32_t)(local_rbx + 4); }
    goto loc_00A00F25;
loc_00A01008:
    result = SddlpAlloc(6, v_rip + 4226166, Arg3, (uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F)));
    local_r11 = 0;
    *(uint64_t *)(local_rbx) = result;
    result = wcscpy_s(result, local_r11 + 3, v_rip - 10416948, (uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F)));
    local_r11 = 0;
    goto loc_00A00EE3;
loc_00A0103C:
    result = RtlNtStatusToDosError((uint32_t)((uint32_t)(result)), local_r11 + 3, v_rip - 10416948, (uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F)));
    local_r11 = 0;
    goto loc_00A00667;
loc_00A01050:
    goto loc_00A00678;
loc_00A0105A:
    local_r12 = (uint32_t)((local_r12 + result * 2) + 1);
    *(uint32_t *)(local_rsp - 0x3F - 0x59) = (uint32_t)(local_r12);
    goto loc_00A007E3;
loc_00A01066:
    goto loc_00A0067C;
loc_00A0106E:
    result = SddlpUuidToString(local_r12, local_rsp - 63 - 49, v_rip - 10416948, (uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F)));
    local_r11 = 0;
    if ((uint32_t)(result) == 0) goto loc_00A00D66;
    local_rbx = ((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F))) | (-1);
loc_00A01092:
    result = SddlpUuidToString(*(uint64_t *)(local_rsp - 0x3F - 0x21), local_rsp - 63 - 49, *(uint64_t *)(local_rsp - 0x3F - 0x31), (uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F)));
    local_r11 = 0;
    if ((uint32_t)(result) == 0) goto loc_00A00D66;
    local_rbx = (local_rbx) | (-1);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x1` | `8` | `R` |
| `Arg1` | `+ 0x2` | `16` | `R` |
| `Arg1` | `+ 0x4` | `16` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x24` | `32` | `R` |
| `Arg4` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A00408&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
