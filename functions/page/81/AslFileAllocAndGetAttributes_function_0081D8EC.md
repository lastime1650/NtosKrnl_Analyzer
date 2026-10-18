# AslFileAllocAndGetAttributes

- RVA: `0x0081D8EC`–`0x0081DE22` (길이 `1,334` bytes)
- VA: `0x000000014081D8EC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00097FE8`
- 디코드: `368`개 명령, `1,334/1,334` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x0081D9E8` → [AslFileMappingEnsure](AslFileMappingEnsure_function_0081A5EC.md) (function, `0x0081A5EC`)
- `0x0081DA02` → [AslpFileLargeEnsureLargeFileMapping](../82/AslpFileLargeEnsureLargeFileMapping_function_00821538.md) (function, `0x00821538`)
- `0x0081DA27` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x0081DAE2` → [AslpFileGetVersionAttributes](AslpFileGetVersionAttributes_function_0081F968.md) (function, `0x0081F968`)
- `0x0081DB19` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x0081DBEB` → [AslpFileGetChecksumAttributes](AslpFileGetChecksumAttributes_function_0081E130.md) (function, `0x0081E130`)
- `0x0081DC12` → [AslpFileGetExeWrapperAttribute](AslpFileGetExeWrapperAttribute_function_0081EC80.md) (function, `0x0081EC80`)
- `0x0081DC39` → [AslpFileGetPeExportNameAttribute](AslpFileGetPeExportNameAttribute_function_0081F884.md) (function, `0x0081F884`)
- `0x0081DC60` → [AslpFileGetHeaderAttributesNE](AslpFileGetHeaderAttributesNE_function_0081EE80.md) (function, `0x0081EE80`)
- `0x0081DC87` → [AslpFileGetClrVersionAttribute](AslpFileGetClrVersionAttribute_function_0081E54C.md) (function, `0x0081E54C`)
- `0x0081DCF0` → [Feature_Arm64XMatching__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_Arm64XMatching__private_IsEnabledDeviceUsageNoInline_function_0069D4C0.md) (function, `0x0069D4C0`)
- `0x0081DD18` → [AslpFileIsArm64XBinary](../82/AslpFileIsArm64XBinary_function_008206B0.md) (function, `0x008206B0`)
- `0x0081DD6E` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x0081DDB1` → [AslpFileGetHeaderAttributesPE](AslpFileGetHeaderAttributesPE_function_0081F028.md) (function, `0x0081F028`)
- `0x0081DDD1` → [AslpFileGetFileKindDetailAttribute](AslpFileGetFileKindDetailAttribute_function_0081EDFC.md) (function, `0x0081EDFC`)

### Direct callers
- [SdbpCheckAllAttributes](SdbpCheckAllAttributes_function_008187EC.md) at `0x00818975`

### Static image references
- `0x0081DA0D` → RVA `0x0003FBF0` (`.rdata`; read)
- `0x0081DA1A` → RVA `0x0003FC20` (`.rdata`; read)
- `0x0081DA35` → RVA `0x0003EE90` (`.rdata`; read)
- `0x0081DB00` → RVA `0x0003FC40` (`.rdata`; read)
- `0x0081DBFA` → RVA `0x0003FA10` (`.rdata`; read)
- `0x0081DC21` → RVA `0x0003F950` (`.rdata`; read)
- `0x0081DC48` → RVA `0x0003F980` (`.rdata`; read)
- `0x0081DC6F` → RVA `0x0003F9E0` (`.rdata`; read)
- `0x0081DC96` → RVA `0x0003F9B0` (`.rdata`; read)
- `0x0081DD55` → RVA `0x0003F928` (`.rdata`; read)
- `0x0081DDBC` → RVA `0x0003F8F8` (`.rdata`; read)
- `0x0081DDEE` → RVA `0x0003F8C8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0081DCF0` → [Feature_Arm64XMatching__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_Arm64XMatching__private_IsEnabledDeviceUsageNoInline_function_0069D4C0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0081D8EC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0081D8F1  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0081D8F6  55                              push rbp
0081D8F7  56                              push rsi
0081D8F8  57                              push rdi
0081D8F9  41 54                           push r12
0081D8FB  41 55                           push r13
0081D8FD  41 56                           push r14
0081D8FF  41 57                           push r15
0081D901  48 83 EC 30                     sub rsp, 0x30
0081D905  33 FF                           xor edi, edi
0081D907  4C 8B F2                        mov r14, rdx
0081D90A  48 8B F1                        mov rsi, rcx
0081D90D  4D 85 C0                        test r8, r8
0081D910  75 07                           jne 0x14081d919
0081D912  8B DF                           mov ebx, edi
0081D914  E9 F1 04 00 00                  jmp 0x14081de0a
0081D919  BD 01 00 00 00                  mov ebp, 1
0081D91E  44 8D 65 01                     lea r12d, [rbp + 1]
0081D922  39 6A 40                        cmp dword ptr [rdx + 0x40], ebp
0081D925  75 42                           jne 0x14081d969
0081D927  8B D7                           mov edx, edi
0081D929  48 8D 41 18                     lea rax, [rcx + 0x18]
0081D92D  44 8D 7D 03                     lea r15d, [rbp + 3]
0081D931  8B 08                           mov ecx, dword ptr [rax]
0081D933  85 D2                           test edx, edx
0081D935  74 15                           je 0x14081d94c
0081D937  83 FA 11                        cmp edx, 0x11
0081D93A  74 10                           je 0x14081d94c
0081D93C  83 FA 1C                        cmp edx, 0x1c
0081D93F  74 05                           je 0x14081d946
0081D941  41 0B CC                        or ecx, r12d
0081D944  EB 14                           jmp 0x14081d95a
0081D946  48 89 68 F8                     mov qword ptr [rax - 8], rbp
0081D94A  EB 04                           jmp 0x14081d950
0081D94C  48 89 78 F8                     mov qword ptr [rax - 8], rdi
0081D950  44 89 60 E8                     mov dword ptr [rax - 0x18], r12d
0081D954  0B CD                           or ecx, ebp
0081D956  4C 89 78 F0                     mov qword ptr [rax - 0x10], r15
0081D95A  89 08                           mov dword ptr [rax], ecx
0081D95C  03 D5                           add edx, ebp
0081D95E  48 83 C0 20                     add rax, 0x20
0081D962  83 FA 24                        cmp edx, 0x24
0081D965  7C CA                           jl 0x14081d931
0081D967  EB A9                           jmp 0x14081d912
0081D969  39 7A 50                        cmp dword ptr [rdx + 0x50], edi
0081D96C  74 77                           je 0x14081d9e5
0081D96E  8B D7                           mov edx, edi
0081D970  4C 8D 41 18                     lea r8, [rcx + 0x18]
0081D974  83 FA 10                        cmp edx, 0x10
0081D977  77 27                           ja 0x14081d9a0
0081D979  74 5F                           je 0x14081d9da
0081D97B  83 FA 09                        cmp edx, 9
0081D97E  77 19                           ja 0x14081d999
0081D980  74 58                           je 0x14081d9da
0081D982  8B CA                           mov ecx, edx
0081D984  2B CD                           sub ecx, ebp
0081D986  74 52                           je 0x14081d9da
0081D988  41 2B CC                        sub ecx, r12d
0081D98B  74 4D                           je 0x14081d9da
0081D98D  2B CD                           sub ecx, ebp
0081D98F  74 49                           je 0x14081d9da
0081D991  2B CD                           sub ecx, ebp
0081D993  74 45                           je 0x14081d9da
0081D995  2B CD                           sub ecx, ebp
0081D997  EB 34                           jmp 0x14081d9cd
0081D999  8B CA                           mov ecx, edx
0081D99B  83 E9 0A                        sub ecx, 0xa
0081D99E  EB EB                           jmp 0x14081d98b
0081D9A0  83 FA 1C                        cmp edx, 0x1c
0081D9A3  77 16                           ja 0x14081d9bb
0081D9A5  74 33                           je 0x14081d9da
0081D9A7  8B CA                           mov ecx, edx
0081D9A9  83 E9 11                        sub ecx, 0x11
0081D9AC  74 2C                           je 0x14081d9da
0081D9AE  2B CD                           sub ecx, ebp
0081D9B0  74 28                           je 0x14081d9da
0081D9B2  2B CD                           sub ecx, ebp
0081D9B4  74 24                           je 0x14081d9da
0081D9B6  83 E9 03                        sub ecx, 3
0081D9B9  EB 12                           jmp 0x14081d9cd
0081D9BB  8B CA                           mov ecx, edx
0081D9BD  83 E9 1D                        sub ecx, 0x1d
0081D9C0  74 18                           je 0x14081d9da
0081D9C2  2B CD                           sub ecx, ebp
0081D9C4  74 14                           je 0x14081d9da
0081D9C6  2B CD                           sub ecx, ebp
0081D9C8  74 10                           je 0x14081d9da
0081D9CA  41 2B CC                        sub ecx, r12d
0081D9CD  74 0B                           je 0x14081d9da
0081D9CF  2B CD                           sub ecx, ebp
0081D9D1  74 07                           je 0x14081d9da
0081D9D3  3B CD                           cmp ecx, ebp
0081D9D5  74 03                           je 0x14081d9da
0081D9D7  45 09 20                        or dword ptr [r8], r12d
0081D9DA  03 D5                           add edx, ebp
0081D9DC  49 83 C0 20                     add r8, 0x20
0081D9E0  83 FA 24                        cmp edx, 0x24
0081D9E3  7C 8F                           jl 0x14081d974
0081D9E5  49 8B CE                        mov rcx, r14
0081D9E8  E8 FF CB FF FF                  call 0x14081a5ec
0081D9ED  8B D8                           mov ebx, eax
0081D9EF  3D 17 00 00 C0                  cmp eax, 0xc0000017
0081D9F4  75 3B                           jne 0x14081da31
0081D9F6  41 39 7E 50                     cmp dword ptr [r14 + 0x50], edi
0081D9FA  75 39                           jne 0x14081da35
0081D9FC  49 8B D6                        mov rdx, r14
0081D9FF  48 8B CE                        mov rcx, rsi
0081DA02  E8 31 3B 00 00                  call 0x140821538
0081DA07  8B D8                           mov ebx, eax
0081DA09  85 C0                           test eax, eax
0081DA0B  79 37                           jns 0x14081da44
0081DA0D  4C 8D 0D DC 21 82 FF            lea r9, [rip - 0x7dde24]
0081DA14  41 B8 1A 03 00 00               mov r8d, 0x31a
0081DA1A  48 8D 15 FF 21 82 FF            lea rdx, [rip - 0x7dde01]
0081DA21  8B CD                           mov ecx, ebp
0081DA23  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0081DA27  E8 C0 0A 14 00                  call 0x14095e4ec
0081DA2C  E9 D9 03 00 00                  jmp 0x14081de0a
0081DA31  85 C0                           test eax, eax
0081DA33  79 0F                           jns 0x14081da44
0081DA35  4C 8D 0D 54 14 82 FF            lea r9, [rip - 0x7debac]
0081DA3C  41 B8 1E 03 00 00               mov r8d, 0x31e
0081DA42  EB D6                           jmp 0x14081da1a
0081DA44  8B EF                           mov ebp, edi
0081DA46  4C 8B EF                        mov r13, rdi
0081DA49  48 8D 3D D0 21 82 FF            lea rdi, [rip - 0x7dde30]
0081DA50  41 BF 04 00 00 00               mov r15d, 4
0081DA56  83 FD 24                        cmp ebp, 0x24
0081DA59  0F 8D A9 03 00 00               jge 0x14081de08
0081DA5F  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
0081DA67  8B CD                           mov ecx, ebp
0081DA69  48 D3 E8                        shr rax, cl
0081DA6C  A8 01                           test al, 1
0081DA6E  0F 84 68 03 00 00               je 0x14081dddc
0081DA74  42 8B 44 2E 18                  mov eax, dword ptr [rsi + r13 + 0x18]
0081DA79  BA 03 00 00 00                  mov edx, 3
0081DA7E  84 C2                           test dl, al
0081DA80  0F 85 56 03 00 00               jne 0x14081dddc
0081DA86  83 FD 12                        cmp ebp, 0x12
0081DA89  0F 8F 07 01 00 00               jg 0x14081db96
0081DA8F  0F 84 16 03 00 00               je 0x14081ddab
0081DA95  83 FD 09                        cmp ebp, 9
0081DA98  0F 8F 85 00 00 00               jg 0x14081db23
0081DA9E  74 3C                           je 0x14081dadc
0081DAA0  85 ED                           test ebp, ebp
0081DAA2  0F 84 CD 02 00 00               je 0x14081dd75
0081DAA8  83 E9 01                        sub ecx, 1
0081DAAB  0F 84 FA 02 00 00               je 0x14081ddab
0081DAB1  83 E9 01                        sub ecx, 1
0081DAB4  0F 84 2B 01 00 00               je 0x14081dbe5
0081DABA  83 E9 01                        sub ecx, 1
0081DABD  74 1D                           je 0x14081dadc
0081DABF  83 E9 01                        sub ecx, 1
0081DAC2  74 18                           je 0x14081dadc
0081DAC4  83 E9 01                        sub ecx, 1
0081DAC7  74 13                           je 0x14081dadc
0081DAC9  83 E9 01                        sub ecx, 1
0081DACC  74 0E                           je 0x14081dadc
0081DACE  83 E9 01                        sub ecx, 1
0081DAD1  74 09                           je 0x14081dadc
0081DAD3  83 F9 01                        cmp ecx, 1
0081DAD6  0F 85 0B 03 00 00               jne 0x14081dde7
0081DADC  49 8B D6                        mov rdx, r14
0081DADF  48 8B CE                        mov rcx, rsi
0081DAE2  E8 81 1E 00 00                  call 0x14081f968
0081DAE7  3D 88 00 00 C0                  cmp eax, 0xc0000088
0081DAEC  7E 12                           jle 0x14081db00
0081DAEE  8D 88 74 FF FF 3F               lea ecx, [rax + 0x3fffff74]
0081DAF4  81 F9 73 FF FF 3F               cmp ecx, 0x3fffff73
0081DAFA  0F 87 DC 02 00 00               ja 0x14081dddc
0081DB00  4C 8D 0D 39 21 82 FF            lea r9, [rip - 0x7ddec7]
0081DB07  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0081DB0B  41 B8 5D 03 00 00               mov r8d, 0x35d
0081DB11  48 8B D7                        mov rdx, rdi
0081DB14  B9 01 00 00 00                  mov ecx, 1
0081DB19  E8 CE 09 14 00                  call 0x14095e4ec
0081DB1E  E9 B9 02 00 00                  jmp 0x14081dddc
0081DB23  83 E9 0A                        sub ecx, 0xa
0081DB26  74 B4                           je 0x14081dadc
0081DB28  83 E9 01                        sub ecx, 1
0081DB2B  74 AF                           je 0x14081dadc
0081DB2D  83 E9 01                        sub ecx, 1
0081DB30  74 AA                           je 0x14081dadc
0081DB32  83 E9 01                        sub ecx, 1
0081DB35  74 A5                           je 0x14081dadc
0081DB37  83 E9 01                        sub ecx, 1
0081DB3A  74 A0                           je 0x14081dadc
0081DB3C  83 E9 01                        sub ecx, 1
0081DB3F  74 9B                           je 0x14081dadc
0081DB41  83 E9 01                        sub ecx, 1
0081DB44  74 96                           je 0x14081dadc
0081DB46  83 F9 01                        cmp ecx, 1
0081DB49  0F 85 98 02 00 00               jne 0x14081dde7
0081DB4F  41 8B 4E 40                     mov ecx, dword ptr [r14 + 0x40]
0081DB53  41 2B CF                        sub ecx, r15d
0081DB56  74 18                           je 0x14081db70
0081DB58  83 E9 01                        sub ecx, 1
0081DB5B  74 0E                           je 0x14081db6b
0081DB5D  83 F9 01                        cmp ecx, 1
0081DB60  74 04                           je 0x14081db66
0081DB62  33 C0                           xor eax, eax
0081DB64  EB 0F                           jmp 0x14081db75
0081DB66  48 8B C2                        mov rax, rdx
0081DB69  EB 0A                           jmp 0x14081db75
0081DB6B  49 8B C4                        mov rax, r12
0081DB6E  EB 05                           jmp 0x14081db75
0081DB70  B8 01 00 00 00                  mov eax, 1
0081DB75  83 8E 38 02 00 00 01            or dword ptr [rsi + 0x238], 1
0081DB7C  44 89 A6 20 02 00 00            mov dword ptr [rsi + 0x220], r12d
0081DB83  4C 89 BE 28 02 00 00            mov qword ptr [rsi + 0x228], r15
0081DB8A  48 89 86 30 02 00 00            mov qword ptr [rsi + 0x230], rax
0081DB91  E9 46 02 00 00                  jmp 0x14081dddc
0081DB96  83 FD 1B                        cmp ebp, 0x1b
0081DB99  0F 8F 09 01 00 00               jg 0x14081dca8
0081DB9F  0F 84 DC 00 00 00               je 0x14081dc81
0081DBA5  83 E9 13                        sub ecx, 0x13
0081DBA8  0F 84 FD 01 00 00               je 0x14081ddab
0081DBAE  83 E9 01                        sub ecx, 1
0081DBB1  0F 84 A3 00 00 00               je 0x14081dc5a
0081DBB7  83 E9 01                        sub ecx, 1
0081DBBA  0F 84 9A 00 00 00               je 0x14081dc5a
0081DBC0  83 E9 01                        sub ecx, 1
0081DBC3  0F 84 E2 01 00 00               je 0x14081ddab
0081DBC9  83 E9 01                        sub ecx, 1
0081DBCC  74 65                           je 0x14081dc33
0081DBCE  83 E9 01                        sub ecx, 1
0081DBD1  0F 84 05 FF FF FF               je 0x14081dadc
0081DBD7  83 E9 01                        sub ecx, 1
0081DBDA  74 30                           je 0x14081dc0c
0081DBDC  83 F9 01                        cmp ecx, 1
0081DBDF  0F 85 02 02 00 00               jne 0x14081dde7
0081DBE5  49 8B D6                        mov rdx, r14
0081DBE8  48 8B CE                        mov rcx, rsi
0081DBEB  E8 40 05 00 00                  call 0x14081e130
0081DBF0  8B D8                           mov ebx, eax
0081DBF2  85 C0                           test eax, eax
0081DBF4  0F 89 E2 01 00 00               jns 0x14081dddc
0081DBFA  4C 8D 0D 0F 1E 82 FF            lea r9, [rip - 0x7de1f1]
0081DC01  41 B8 D5 03 00 00               mov r8d, 0x3d5
0081DC07  E9 EF 01 00 00                  jmp 0x14081ddfb
0081DC0C  49 8B D6                        mov rdx, r14
0081DC0F  48 8B CE                        mov rcx, rsi
0081DC12  E8 69 10 00 00                  call 0x14081ec80
0081DC17  8B D8                           mov ebx, eax
0081DC19  85 C0                           test eax, eax
0081DC1B  0F 89 BB 01 00 00               jns 0x14081dddc
0081DC21  4C 8D 0D 28 1D 82 FF            lea r9, [rip - 0x7de2d8]
0081DC28  41 B8 AE 03 00 00               mov r8d, 0x3ae
0081DC2E  E9 C8 01 00 00                  jmp 0x14081ddfb
0081DC33  49 8B D6                        mov rdx, r14
0081DC36  48 8B CE                        mov rcx, rsi
0081DC39  E8 46 1C 00 00                  call 0x14081f884
0081DC3E  8B D8                           mov ebx, eax
0081DC40  85 C0                           test eax, eax
0081DC42  0F 89 94 01 00 00               jns 0x14081dddc
0081DC48  4C 8D 0D 31 1D 82 FF            lea r9, [rip - 0x7de2cf]
0081DC4F  41 B8 B7 03 00 00               mov r8d, 0x3b7
0081DC55  E9 A1 01 00 00                  jmp 0x14081ddfb
0081DC5A  49 8B D6                        mov rdx, r14
0081DC5D  48 8B CE                        mov rcx, rsi
0081DC60  E8 1B 12 00 00                  call 0x14081ee80
0081DC65  8B D8                           mov ebx, eax
0081DC67  85 C0                           test eax, eax
0081DC69  0F 89 6D 01 00 00               jns 0x14081dddc
0081DC6F  4C 8D 0D 6A 1D 82 FF            lea r9, [rip - 0x7de296]
0081DC76  41 B8 CA 03 00 00               mov r8d, 0x3ca
0081DC7C  E9 7A 01 00 00                  jmp 0x14081ddfb
0081DC81  49 8B D6                        mov rdx, r14
0081DC84  48 8B CE                        mov rcx, rsi
0081DC87  E8 C0 08 00 00                  call 0x14081e54c
0081DC8C  8B D8                           mov ebx, eax
0081DC8E  85 C0                           test eax, eax
0081DC90  0F 89 46 01 00 00               jns 0x14081dddc
0081DC96  4C 8D 0D 13 1D 82 FF            lea r9, [rip - 0x7de2ed]
0081DC9D  41 B8 C0 03 00 00               mov r8d, 0x3c0
0081DCA3  E9 53 01 00 00                  jmp 0x14081ddfb
0081DCA8  83 E9 1C                        sub ecx, 0x1c
0081DCAB  0F 84 1A 01 00 00               je 0x14081ddcb
0081DCB1  83 E9 01                        sub ecx, 1
0081DCB4  0F 84 F1 00 00 00               je 0x14081ddab
0081DCBA  83 E9 01                        sub ecx, 1
0081DCBD  0F 84 E8 00 00 00               je 0x14081ddab
0081DCC3  83 E9 01                        sub ecx, 1
0081DCC6  0F 84 DF 00 00 00               je 0x14081ddab
0081DCCC  83 E9 01                        sub ecx, 1
0081DCCF  0F 84 A0 00 00 00               je 0x14081dd75
0081DCD5  83 E9 01                        sub ecx, 1
0081DCD8  0F 84 CD 00 00 00               je 0x14081ddab
0081DCDE  83 E9 01                        sub ecx, 1
0081DCE1  0F 84 FE FE FF FF               je 0x14081dbe5
0081DCE7  83 F9 01                        cmp ecx, 1
0081DCEA  0F 85 F7 00 00 00               jne 0x14081dde7
0081DCF0  E8 CB F7 E7 FF                  call 0x14069d4c0
0081DCF5  85 C0                           test eax, eax
0081DCF7  75 0C                           jne 0x14081dd05
0081DCF9  44 09 A6 78 04 00 00            or dword ptr [rsi + 0x478], r12d
0081DD00  E9 D7 00 00 00                  jmp 0x14081dddc
0081DD05  49 8B D6                        mov rdx, r14
0081DD08  C6 84 24 88 00 00 00 00         mov byte ptr [rsp + 0x88], 0
0081DD10  48 8D 8C 24 88 00 00 00         lea rcx, [rsp + 0x88]
0081DD18  E8 93 29 00 00                  call 0x1408206b0
0081DD1D  85 C0                           test eax, eax
0081DD1F  78 2D                           js 0x14081dd4e
0081DD21  83 A6 60 04 00 00 00            and dword ptr [rsi + 0x460], 0
0081DD28  0F B6 84 24 88 00 00 00         movzx eax, byte ptr [rsp + 0x88]
0081DD30  83 8E 78 04 00 00 01            or dword ptr [rsi + 0x478], 1
0081DD37  48 89 86 70 04 00 00            mov qword ptr [rsi + 0x470], rax
0081DD3E  48 C7 86 68 04 00 00 01 00 00 00  mov qword ptr [rsi + 0x468], 1
0081DD49  E9 8E 00 00 00                  jmp 0x14081dddc
0081DD4E  3D 22 00 00 80                  cmp eax, 0x80000022
0081DD53  74 A4                           je 0x14081dcf9
0081DD55  4C 8D 0D CC 1B 82 FF            lea r9, [rip - 0x7de434]
0081DD5C  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0081DD60  41 B8 9D 03 00 00               mov r8d, 0x39d
0081DD66  48 8B D7                        mov rdx, rdi
0081DD69  B9 01 00 00 00                  mov ecx, 1
0081DD6E  E8 79 07 14 00                  call 0x14095e4ec
0081DD73  EB 84                           jmp 0x14081dcf9
0081DD75  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
0081DD79  83 8E 18 04 00 00 01            or dword ptr [rsi + 0x418], 1
0081DD80  83 4E 18 01                     or dword ptr [rsi + 0x18], 1
0081DD84  8B C8                           mov ecx, eax
0081DD86  48 89 4E 10                     mov qword ptr [rsi + 0x10], rcx
0081DD8A  89 96 00 04 00 00               mov dword ptr [rsi + 0x400], edx
0081DD90  48 C7 86 08 04 00 00 08 00 00 00  mov qword ptr [rsi + 0x408], 8
0081DD9B  48 89 86 10 04 00 00            mov qword ptr [rsi + 0x410], rax
0081DDA2  44 89 26                        mov dword ptr [rsi], r12d
0081DDA5  4C 89 7E 08                     mov qword ptr [rsi + 8], r15
0081DDA9  EB 31                           jmp 0x14081dddc
0081DDAB  49 8B D6                        mov rdx, r14
0081DDAE  48 8B CE                        mov rcx, rsi
0081DDB1  E8 72 12 00 00                  call 0x14081f028
0081DDB6  8B D8                           mov ebx, eax
0081DDB8  85 C0                           test eax, eax
0081DDBA  79 20                           jns 0x14081dddc
0081DDBC  4C 8D 0D 35 1B 82 FF            lea r9, [rip - 0x7de4cb]
0081DDC3  41 B8 89 03 00 00               mov r8d, 0x389
0081DDC9  EB 30                           jmp 0x14081ddfb
0081DDCB  49 8B D6                        mov rdx, r14
0081DDCE  48 8B CE                        mov rcx, rsi
0081DDD1  E8 26 10 00 00                  call 0x14081edfc
0081DDD6  8B D8                           mov ebx, eax
0081DDD8  85 C0                           test eax, eax
0081DDDA  78 12                           js 0x14081ddee
0081DDDC  FF C5                           inc ebp
0081DDDE  49 83 C5 20                     add r13, 0x20
0081DDE2  E9 6F FC FF FF                  jmp 0x14081da56
0081DDE7  BB E5 00 00 C0                  mov ebx, 0xc00000e5
0081DDEC  EB 1C                           jmp 0x14081de0a
0081DDEE  4C 8D 0D D3 1A 82 FF            lea r9, [rip - 0x7de52d]
0081DDF5  41 B8 79 03 00 00               mov r8d, 0x379
0081DDFB  48 8B D7                        mov rdx, rdi
0081DDFE  B9 01 00 00 00                  mov ecx, 1
0081DE03  E9 1B FC FF FF                  jmp 0x14081da23
0081DE08  33 DB                           xor ebx, ebx
0081DE0A  8B C3                           mov eax, ebx
0081DE0C  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
0081DE11  48 83 C4 30                     add rsp, 0x30
0081DE15  41 5F                           pop r15
0081DE17  41 5E                           pop r14
0081DE19  41 5D                           pop r13
0081DE1B  41 5C                           pop r12
0081DE1D  5F                              pop rdi
0081DE1E  5E                              pop rsi
0081DE1F  5D                              pop rbp
0081DE20  C3                              ret
0081DE21  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AslFileAllocAndGetAttributes(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (48);
    v_rdi = 0;
    if (a3 != 0) goto loc_0081D919;
loc_0081D912:
    goto loc_0081DE0A;
loc_0081D919:
    if ((*(unsigned int *)(a2 + 64)) != 1) goto loc_0081D969;
loc_0081D931:
    if (0 == 0) goto loc_0081D94C;
    if (0 == 17) goto loc_0081D94C;
    if (0 == 28) goto loc_0081D946;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 24))) | ((unsigned int)(1 + 1)));
    goto loc_0081D95A;
loc_0081D946:
    *(unsigned __int64 *)(a1 + 24 - 8) = 1;
    goto loc_0081D950;
loc_0081D94C:
    *(unsigned __int64 *)(a1 + 24 - 8) = 0;
loc_0081D950:
    *(unsigned int *)(a1 + 24 - 24) = (unsigned int)(1 + 1);
    a1 = (unsigned int)((a1) | (1));
    *(unsigned __int64 *)(a1 + 24 - 16) = 1 + 3;
loc_0081D95A:
    *(unsigned int *)(a1 + 24) = (unsigned int)(a1);
    a2 = (unsigned int)((0) + (1));
    result = (a1 + 24) + (32);
    if (((unsigned int)(a2)) < 36) goto loc_0081D931;
    goto loc_0081D912;
loc_0081D969:
    if ((*(unsigned int *)(a2 + 80)) == 0) goto loc_0081D9E5;
loc_0081D974:
    if (0 > 16) goto loc_0081D9A0;
    if (0 == 16) goto loc_0081D9DA;
    if (0 > 9) goto loc_0081D999;
    if (0 == 9) goto loc_0081D9DA;
    a1 = (unsigned int)((0) - (1));
    if (condition_is_equal) goto loc_0081D9DA;
    a1 = (unsigned int)((a1) - ((unsigned int)(1 + 1)));
loc_0081D98B:
    if (condition_is_equal) goto loc_0081D9DA;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081D9DA;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081D9DA;
    a1 = (unsigned int)((a1) - (1));
    goto loc_0081D9CD;
loc_0081D999:
    a1 = (unsigned int)((0) - (10));
    goto loc_0081D98B;
loc_0081D9A0:
    if (0 > 28) goto loc_0081D9BB;
    if (0 == 28) goto loc_0081D9DA;
    a1 = (unsigned int)((0) - (17));
    if (condition_is_equal) goto loc_0081D9DA;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081D9DA;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081D9DA;
    a1 = (unsigned int)((a1) - (3));
    goto loc_0081D9CD;
loc_0081D9BB:
    a1 = (unsigned int)((0) - (29));
    if (condition_is_equal) goto loc_0081D9DA;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081D9DA;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081D9DA;
    a1 = (unsigned int)((a1) - ((unsigned int)(1 + 1)));
loc_0081D9CD:
    if (condition_is_equal) goto loc_0081D9DA;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081D9DA;
    if (((unsigned int)(a1)) != 1) {
    }
    a2 = (unsigned int)((0) + (1));
    a3 = (a1 + 24) + (32);
    if (((unsigned int)(a2)) < 36) goto loc_0081D974;
loc_0081D9E5:
    result = AslFileMappingEnsure(a2, a2, a3, a4);
    if (((unsigned int)(result)) != 0xC0000017ULL) goto loc_0081DA31;
    if ((*(unsigned int *)(a2 + 80)) != 0) goto loc_0081DA35;
    result = AslpFileLargeEnsureLargeFileMapping(a1, a2, a3, a4);
    if (!sign_flag) goto loc_0081DA44;
loc_0081DA1A:
loc_0081DA23:
    v_stack_m48 = (unsigned int)(result);
    result = AslLogCallPrintf(1, v_rip - 8248833, 794, v_rip - 8248868);
    goto loc_0081DE0A;
loc_0081DA31:
    if (!sign_flag) goto loc_0081DA44;
loc_0081DA35:
    goto loc_0081DA1A;
loc_0081DA44:
loc_0081DA56:
    if (0 >= 36) goto loc_0081DE08;
    result = (v_stack_p18) >> (0);
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_0081DDDC;
    if (((3) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 0 * 1 + 24))))) != 0) goto loc_0081DDDC;
    if (0 > 18) goto loc_0081DB96;
    if (0 == 18) goto loc_0081DDAB;
    if (0 > 9) goto loc_0081DB23;
    if (0 == 9) goto loc_0081DADC;
    if (0 == 0) goto loc_0081DD75;
    a1 = (unsigned int)((0) - (1));
    if (condition_is_equal) goto loc_0081DDAB;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081DBE5;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081DADC;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081DADC;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081DADC;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081DADC;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081DADC;
    if (((unsigned int)(a1)) != 1) goto loc_0081DDE7;
loc_0081DADC:
    result = AslpFileGetVersionAttributes(a1, a2, 798, v_rip - 8252332);
    if (((unsigned int)(result)) <= 0xC0000088ULL) goto loc_0081DB00;
    if (((unsigned int)(result + 1073741684)) > 0x3FFFFF73ULL) goto loc_0081DDDC;
loc_0081DB00:
    v_stack_m48 = (unsigned int)(result);
    result = AslLogCallPrintf(1, v_rip - 8248880, 861, v_rip - 8249031);
    goto loc_0081DDDC;
loc_0081DB23:
    a1 = (unsigned int)((1) - (10));
    if (condition_is_equal) goto loc_0081DADC;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081DADC;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081DADC;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081DADC;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081DADC;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081DADC;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081DADC;
    if (((unsigned int)(a1)) != 1) goto loc_0081DDE7;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 64))) - (4));
    if (condition_is_equal) goto loc_0081DB70;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081DB6B;
    if (((unsigned int)(a1)) == 1) goto loc_0081DB66;
    result = 0;
    goto loc_0081DB75;
loc_0081DB66:
    goto loc_0081DB75;
loc_0081DB6B:
    goto loc_0081DB75;
loc_0081DB70:
loc_0081DB75:
    *(unsigned int *)(a1 + 544) = (unsigned int)(1 + 1);
    *(unsigned __int64 *)(a1 + 552) = 4;
    *(unsigned __int64 *)(a1 + 560) = 1;
    goto loc_0081DDDC;
loc_0081DB96:
    if (0 > 27) goto loc_0081DCA8;
    if (0 == 27) goto loc_0081DC81;
    a1 = (unsigned int)((a1) - (19));
    if (condition_is_equal) goto loc_0081DDAB;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081DC5A;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081DC5A;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081DDAB;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081DC33;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081DADC;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081DC0C;
    if (((unsigned int)(a1)) != 1) goto loc_0081DDE7;
loc_0081DBE5:
    result = AslpFileGetChecksumAttributes(a1, a2, 861, v_rip - 8249031);
    if (!sign_flag) goto loc_0081DDDC;
    goto loc_0081DDFB;
loc_0081DC0C:
    result = AslpFileGetExeWrapperAttribute(a1, a2, 981, v_rip - 8249841);
    if (!sign_flag) goto loc_0081DDDC;
    goto loc_0081DDFB;
loc_0081DC33:
    result = AslpFileGetPeExportNameAttribute(a1, a2, 942, v_rip - 8250072);
    if (!sign_flag) goto loc_0081DDDC;
    goto loc_0081DDFB;
loc_0081DC5A:
    result = AslpFileGetHeaderAttributesNE(a1, a2, 951, v_rip - 8250063);
    if (!sign_flag) goto loc_0081DDDC;
    goto loc_0081DDFB;
loc_0081DC81:
    result = AslpFileGetClrVersionAttribute(a1, a2, 970, v_rip - 8250006);
    if (!sign_flag) goto loc_0081DDDC;
    goto loc_0081DDFB;
loc_0081DCA8:
    a1 = (unsigned int)((a1) - (28));
    if (condition_is_equal) goto loc_0081DDCB;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081DDAB;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081DDAB;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081DDAB;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081DD75;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081DDAB;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0081DBE5;
    if (((unsigned int)(a1)) != 1) goto loc_0081DDE7;
    result = Feature_Arm64XMatching__private_IsEnabledDeviceUsageNoInline(a1, a2, 960, v_rip - 8250093);
    if ((unsigned int)(result) != 0) goto loc_0081DD05;
loc_0081DCF9:
    goto loc_0081DDDC;
loc_0081DD05:
    v_stack_p20 = 0;
    result = AslpFileIsArm64XBinary(v_stack_p20, a2, 960, v_rip - 8250093);
    if (sign_flag) goto loc_0081DD4E;
    *(unsigned __int64 *)(a1 + 1136) = v_stack_p20;
    *(unsigned __int64 *)(a1 + 1128) = 1;
    goto loc_0081DDDC;
loc_0081DD4E:
    if (((unsigned int)(v_stack_p20)) == 0x80000022ULL) goto loc_0081DCF9;
    v_stack_m48 = (unsigned int)(v_stack_p20);
    result = AslLogCallPrintf(1, v_rip - 8248880, 925, v_rip - 8250420);
    goto loc_0081DCF9;
loc_0081DD75:
    *(unsigned __int64 *)(a1 + 16) = (unsigned int)((unsigned int)(*(unsigned __int64 *)(a2 + 24)));
    *(unsigned int *)(a1 + 1024) = (unsigned int)(v_rip - 8248880);
    *(unsigned __int64 *)(a1 + 1032) = 8;
    *(unsigned __int64 *)(a1 + 1040) = *(unsigned __int64 *)(a2 + 24);
    *(unsigned int *)(a1) = (unsigned int)(1 + 1);
    *(unsigned __int64 *)(a1 + 8) = 4;
    goto loc_0081DDDC;
loc_0081DDAB:
    result = AslpFileGetHeaderAttributesPE(a1, a2, 925, v_rip - 8250420);
    if (!sign_flag) goto loc_0081DDDC;
    goto loc_0081DDFB;
loc_0081DDCB:
    result = AslpFileGetFileKindDetailAttribute(a1, a2, 905, v_rip - 8250571);
    if (sign_flag) goto loc_0081DDEE;
loc_0081DDDC:
    v_rbp = (unsigned int)((0) + 1);
    v_r13 = (0) + (32);
    goto loc_0081DA56;
loc_0081DDE7:
    goto loc_0081DE0A;
loc_0081DDEE:
loc_0081DDFB:
    goto loc_0081DA23;
loc_0081DE08:
    v_rbx = 0;
loc_0081DE0A:
    v_rsp = (v_rsp) + (48);
    return 0;
}
```

## 5. (Beta) C Style

```c
int64_t AslFileAllocAndGetAttributes(void *Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r13;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_m48;
    uint64_t v_stack_p18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (48);
    local_rdi = 0;
    if (Arg3 != 0) goto loc_0081D919;
loc_0081D912:
    goto loc_0081DE0A;
loc_0081D919:
    if ((*(uint32_t *)(arg2 + 0x40)) != 1) goto loc_0081D969;
loc_0081D931:
    if (0 == 0) goto loc_0081D94C;
    if (0 == 17) goto loc_0081D94C;
    if (0 == 28) goto loc_0081D946;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x18))) | ((uint32_t)(1 + 1)));
    goto loc_0081D95A;
loc_0081D946:
    *(uint64_t *)(arg1 + 0x18 - 0x8) = 1;
    goto loc_0081D950;
loc_0081D94C:
    *(uint64_t *)(arg1 + 0x18 - 0x8) = 0;
loc_0081D950:
    *(uint32_t *)(arg1 + 0x18 - 0x18) = (uint32_t)(1 + 1);
    Arg1 = (uint32_t)((Arg1) | (1));
    *(uint64_t *)(arg1 + 0x18 - 0x10) = 1 + 3;
loc_0081D95A:
    *(uint32_t *)(arg1 + 0x18) = (uint32_t)(Arg1);
    Arg2 = (uint32_t)((0) + (1));
    result = (Arg1 + 24) + (32);
    if (((uint32_t)(Arg2)) < 36) goto loc_0081D931;
    goto loc_0081D912;
loc_0081D969:
    if ((*(uint32_t *)(arg2 + 0x50)) == 0) goto loc_0081D9E5;
loc_0081D974:
    if (0 > 16) goto loc_0081D9A0;
    if (0 == 16) goto loc_0081D9DA;
    if (0 > 9) goto loc_0081D999;
    if (0 == 9) goto loc_0081D9DA;
    Arg1 = (uint32_t)((0) - (1));
    if (condition_is_equal) goto loc_0081D9DA;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(1 + 1)));
loc_0081D98B:
    if (condition_is_equal) goto loc_0081D9DA;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081D9DA;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081D9DA;
    Arg1 = (uint32_t)((Arg1) - (1));
    goto loc_0081D9CD;
loc_0081D999:
    Arg1 = (uint32_t)((0) - (10));
    goto loc_0081D98B;
loc_0081D9A0:
    if (0 > 28) goto loc_0081D9BB;
    if (0 == 28) goto loc_0081D9DA;
    Arg1 = (uint32_t)((0) - (17));
    if (condition_is_equal) goto loc_0081D9DA;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081D9DA;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081D9DA;
    Arg1 = (uint32_t)((Arg1) - (3));
    goto loc_0081D9CD;
loc_0081D9BB:
    Arg1 = (uint32_t)((0) - (29));
    if (condition_is_equal) goto loc_0081D9DA;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081D9DA;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081D9DA;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(1 + 1)));
loc_0081D9CD:
    if (condition_is_equal) goto loc_0081D9DA;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081D9DA;
    if (((uint32_t)(Arg1)) != 1) {
    }
    Arg2 = (uint32_t)((0) + (1));
    Arg3 = (Arg1 + 24) + (32);
    if (((uint32_t)(Arg2)) < 36) goto loc_0081D974;
loc_0081D9E5:
    result = AslFileMappingEnsure(Arg2, Arg2, Arg3, a4);
    if (((uint32_t)(result)) != 0xC0000017ULL) goto loc_0081DA31;
    if ((*(uint32_t *)(arg2 + 0x50)) != 0) goto loc_0081DA35;
    result = AslpFileLargeEnsureLargeFileMapping(Arg1, Arg2, Arg3, a4);
    if (!sign_flag) goto loc_0081DA44;
loc_0081DA1A:
loc_0081DA23:
    v_stack_m48 = (uint32_t)(result);
    result = AslLogCallPrintf(1, v_rip - 8248833, 794, v_rip - 8248868);
    goto loc_0081DE0A;
loc_0081DA31:
    if (!sign_flag) goto loc_0081DA44;
loc_0081DA35:
    goto loc_0081DA1A;
loc_0081DA44:
loc_0081DA56:
    if (0 >= 36) goto loc_0081DE08;
    result = (v_stack_p18) >> (0);
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_0081DDDC;
    if (((3) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x0 * 1 + 0x18))))) != 0) goto loc_0081DDDC;
    if (0 > 18) goto loc_0081DB96;
    if (0 == 18) goto loc_0081DDAB;
    if (0 > 9) goto loc_0081DB23;
    if (0 == 9) goto loc_0081DADC;
    if (0 == 0) goto loc_0081DD75;
    Arg1 = (uint32_t)((0) - (1));
    if (condition_is_equal) goto loc_0081DDAB;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081DBE5;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081DADC;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081DADC;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081DADC;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081DADC;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081DADC;
    if (((uint32_t)(Arg1)) != 1) goto loc_0081DDE7;
loc_0081DADC:
    result = AslpFileGetVersionAttributes(Arg1, Arg2, 798, v_rip - 8252332);
    if (((uint32_t)(result)) <= 0xC0000088ULL) goto loc_0081DB00;
    if (((uint32_t)(result + 1073741684)) > 0x3FFFFF73ULL) goto loc_0081DDDC;
loc_0081DB00:
    v_stack_m48 = (uint32_t)(result);
    result = AslLogCallPrintf(1, v_rip - 8248880, 861, v_rip - 8249031);
    goto loc_0081DDDC;
loc_0081DB23:
    Arg1 = (uint32_t)((1) - (10));
    if (condition_is_equal) goto loc_0081DADC;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081DADC;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081DADC;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081DADC;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081DADC;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081DADC;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081DADC;
    if (((uint32_t)(Arg1)) != 1) goto loc_0081DDE7;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x40))) - (4));
    if (condition_is_equal) goto loc_0081DB70;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081DB6B;
    if (((uint32_t)(Arg1)) == 1) goto loc_0081DB66;
    result = 0;
    goto loc_0081DB75;
loc_0081DB66:
    goto loc_0081DB75;
loc_0081DB6B:
    goto loc_0081DB75;
loc_0081DB70:
loc_0081DB75:
    *(uint32_t *)(arg1 + 0x220) = (uint32_t)(1 + 1);
    *(uint64_t *)(arg1 + 0x228) = 4;
    *(uint64_t *)(arg1 + 0x230) = 1;
    goto loc_0081DDDC;
loc_0081DB96:
    if (0 > 27) goto loc_0081DCA8;
    if (0 == 27) goto loc_0081DC81;
    Arg1 = (uint32_t)((Arg1) - (19));
    if (condition_is_equal) goto loc_0081DDAB;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081DC5A;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081DC5A;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081DDAB;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081DC33;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081DADC;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081DC0C;
    if (((uint32_t)(Arg1)) != 1) goto loc_0081DDE7;
loc_0081DBE5:
    result = AslpFileGetChecksumAttributes(Arg1, Arg2, 861, v_rip - 8249031);
    if (!sign_flag) goto loc_0081DDDC;
    goto loc_0081DDFB;
loc_0081DC0C:
    result = AslpFileGetExeWrapperAttribute(Arg1, Arg2, 981, v_rip - 8249841);
    if (!sign_flag) goto loc_0081DDDC;
    goto loc_0081DDFB;
loc_0081DC33:
    result = AslpFileGetPeExportNameAttribute(Arg1, Arg2, 942, v_rip - 8250072);
    if (!sign_flag) goto loc_0081DDDC;
    goto loc_0081DDFB;
loc_0081DC5A:
    result = AslpFileGetHeaderAttributesNE(Arg1, Arg2, 951, v_rip - 8250063);
    if (!sign_flag) goto loc_0081DDDC;
    goto loc_0081DDFB;
loc_0081DC81:
    result = AslpFileGetClrVersionAttribute(Arg1, Arg2, 970, v_rip - 8250006);
    if (!sign_flag) goto loc_0081DDDC;
    goto loc_0081DDFB;
loc_0081DCA8:
    Arg1 = (uint32_t)((Arg1) - (28));
    if (condition_is_equal) goto loc_0081DDCB;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081DDAB;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081DDAB;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081DDAB;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081DD75;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081DDAB;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0081DBE5;
    if (((uint32_t)(Arg1)) != 1) goto loc_0081DDE7;
    result = Feature_Arm64XMatching__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, 960, v_rip - 8250093);
    if ((uint32_t)(result) != 0) goto loc_0081DD05;
loc_0081DCF9:
    goto loc_0081DDDC;
loc_0081DD05:
    v_stack_p20 = 0;
    result = AslpFileIsArm64XBinary(v_stack_p20, Arg2, 960, v_rip - 8250093);
    if (sign_flag) goto loc_0081DD4E;
    *(uint64_t *)(arg1 + 0x470) = v_stack_p20;
    *(uint64_t *)(arg1 + 0x468) = 1;
    goto loc_0081DDDC;
loc_0081DD4E:
    if (((uint32_t)(v_stack_p20)) == 0x80000022ULL) goto loc_0081DCF9;
    v_stack_m48 = (uint32_t)(v_stack_p20);
    result = AslLogCallPrintf(1, v_rip - 8248880, 925, v_rip - 8250420);
    goto loc_0081DCF9;
loc_0081DD75:
    *(uint64_t *)(arg1 + 0x10) = (uint32_t)((uint32_t)(*(uint64_t *)(arg2 + 0x18)));
    *(uint32_t *)(arg1 + 0x400) = (uint32_t)(v_rip - 8248880);
    *(uint64_t *)(arg1 + 0x408) = 8;
    *(uint64_t *)(arg1 + 0x410) = *(uint64_t *)(arg2 + 0x18);
    *(uint32_t *)(arg1) = (uint32_t)(1 + 1);
    *(uint64_t *)(arg1 + 0x8) = 4;
    goto loc_0081DDDC;
loc_0081DDAB:
    result = AslpFileGetHeaderAttributesPE(Arg1, Arg2, 925, v_rip - 8250420);
    if (!sign_flag) goto loc_0081DDDC;
    goto loc_0081DDFB;
loc_0081DDCB:
    result = AslpFileGetFileKindDetailAttribute(Arg1, Arg2, 905, v_rip - 8250571);
    if (sign_flag) goto loc_0081DDEE;
loc_0081DDDC:
    local_rbp = (uint32_t)((0) + 1);
    local_r13 = (0) + (32);
    goto loc_0081DA56;
loc_0081DDE7:
    goto loc_0081DE0A;
loc_0081DDEE:
loc_0081DDFB:
    goto loc_0081DA23;
loc_0081DE08:
    local_rbx = 0;
loc_0081DE0A:
    local_rsp = (local_rsp) + (48);
    return 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x18` | `32` | `W` |
| `Arg1` | `- 0x10` | `64` | `W` |
| `Arg1` | `- 0x8` | `64` | `W` |
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `W` |
| `Arg1` | `+ 0x18` | `32` | `R/W` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x18 + r13*1` | `32` | `R` |
| `Arg1` | `+ 0x220` | `32` | `W` |
| `Arg1` | `+ 0x228` | `64` | `W` |
| `Arg1` | `+ 0x230` | `64` | `W` |
| `Arg1` | `+ 0x238` | `32` | `R/W` |
| `Arg1` | `+ 0x400` | `32` | `W` |
| `Arg1` | `+ 0x408` | `64` | `W` |
| `Arg1` | `+ 0x410` | `64` | `W` |
| `Arg1` | `+ 0x418` | `32` | `R/W` |
| `Arg1` | `+ 0x460` | `32` | `R/W` |
| `Arg1` | `+ 0x468` | `64` | `W` |
| `Arg1` | `+ 0x470` | `64` | `W` |
| `Arg1` | `+ 0x478` | `32` | `R/W` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x40` | `32` | `R` |
| `Arg2` | `+ 0x50` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0081D8EC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
