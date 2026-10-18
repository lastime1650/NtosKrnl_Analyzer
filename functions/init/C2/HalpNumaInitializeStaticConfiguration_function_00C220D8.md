# HalpNumaInitializeStaticConfiguration

- RVA: `0x00C220D8`–`0x00C22978` (길이 `2,208` bytes)
- VA: `0x0000000140C220D8`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C4704`
- 디코드: `594`개 명령, `2,208/2,208` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **16**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **28**

### Outgoing calls
- `0x00C22117` → [HalpAcpiGetTable](../../text/3F/HalpAcpiGetTable_function_003F6BF8.md) (function, `0x003F6BF8`)
- `0x00C22131` → [HalpAcpiGetTable](../../text/3F/HalpAcpiGetTable_function_003F6BF8.md) (function, `0x003F6BF8`)
- `0x00C2214B` → [HalpAcpiGetTable](../../text/3F/HalpAcpiGetTable_function_003F6BF8.md) (function, `0x003F6BF8`)
- `0x00C22166` → [HalpInitializeConfigurationFromMadt](HalpInitializeConfigurationFromMadt_function_00C21D54.md) (function, `0x00C21D54`)
- `0x00C2218C` → [HalpGetNumaProcMemoryCount](HalpGetNumaProcMemoryCount_function_00C21B40.md) (function, `0x00C21B40`)
- `0x00C221AB` → [HalpAllocateNumaConfigData](HalpAllocateNumaConfigData_function_00C2190C.md) (function, `0x00C2190C`)
- `0x00C221CA` → [HalpMmAllocateMemoryInternal](../../text/54/HalpMmAllocateMemoryInternal_function_00544990.md) (function, `0x00544990`)
- `0x00C22226` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C222A5` → [HalpVerifySratEntryLengthAndFlag](HalpVerifySratEntryLengthAndFlag_function_00C23158.md) (function, `0x00C23158`)
- `0x00C224A8` → [qsort](../../text/50/qsort_function_005009F0.md) (function, `0x005009F0`)
- `0x00C224C5` → [qsort](../../text/50/qsort_function_005009F0.md) (function, `0x005009F0`)
- `0x00C225E1` → [HalpUpdateConfigurationFromMsct](HalpUpdateConfigurationFromMsct_function_00C22DB0.md) (function, `0x00C22DB0`)
- `0x00C225F4` → [HalpAcpiGetTable](../../text/3F/HalpAcpiGetTable_function_003F6BF8.md) (function, `0x003F6BF8`)
- `0x00C22838` → [HalpNumaSortProcessors](HalpNumaSortProcessors_function_00C22D14.md) (function, `0x00C22D14`)
- `0x00C22863` → [HalpGetAvailableProximityId](HalpGetAvailableProximityId_function_00C21AB0.md) (function, `0x00C21AB0`)
- `0x00C22961` → [HalpChannelInitializeStaticConfiguration](HalpChannelInitializeStaticConfiguration_function_00C25318.md) (function, `0x00C25318`)

### Direct callers
- [HalpSetupAcpiPhase0](HalpSetupAcpiPhase0_function_00C23EDC.md) at `0x00C23FFC`

### Static image references
- `0x00C22110` → RVA `0x00F90664` (`.data`; write)
- `0x00C2211F` → RVA `0x00E117E8` (`.data`; write)
- `0x00C22139` → RVA `0x00F90618` (`.data`; write)
- `0x00C22150` → RVA `0x00F90670` (`.data`; write)
- `0x00C22157` → RVA `0x00F90618` (`.data`; read)
- `0x00C221B0` → RVA `0x00F90658` (`.data`; read)
- `0x00C221CF` → RVA `0x00F90628` (`.data`; write)
- `0x00C2239E` → RVA `0x00E0A828` (`.data`; read)
- `0x00C223A7` → RVA `0x00E0A828` (`.data`; write)
- `0x00C223AE` → RVA `0x00F90600` (`.data`; read)
- `0x00C223B7` → RVA `0x00F90600` (`.data`; write)
- `0x00C223BE` → RVA `0x00F90608` (`.data`; read)
- `0x00C223C5` → RVA `0x00F90638` (`.data`; read/write)
- `0x00C223E9` → RVA `0x00F90628` (`.data`; read)
- `0x00C22456` → RVA `0x00E0A820` (`.data`; write)
- `0x00C22480` → RVA `0x00558EA0` (`HalpNodeCostSort`; read)
- `0x00C22491` → RVA `0x00F90630` (`.data`; write)
- `0x00C22497` → RVA `0x00F90650` (`.data`; write)
- `0x00C224AD` → RVA `0x00F90650` (`.data`; read)
- `0x00C224B3` → RVA `0x00558E70` (`HalpCompareNumaMemoryRanges`; read)
- `0x00C22528` → RVA `0x00F90660` (`.data`; write)
- `0x00C2259B` → RVA `0x00F90670` (`.data`; read)
- `0x00C225D5` → RVA `0x00E0A820` (`.data`; read)
- `0x00C226AB` → RVA `0x00F90668` (`.data`; write)
- `0x00C226B2` → RVA `0x00F90668` (`.data`; read)
- `0x00C22816` → RVA `0x00E10462` (`.data`; read)
- `0x00C2284F` → RVA `0x00E0A81C` (`.data`; read)
- `0x00C2295B` → RVA `0x00FC4050` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **8**
  - `0x00C22117` → [HalpAcpiGetTable](../../text/3F/HalpAcpiGetTable_function_003F6BF8.md) (`INIT` → `.text`)
  - `0x00C22131` → [HalpAcpiGetTable](../../text/3F/HalpAcpiGetTable_function_003F6BF8.md) (`INIT` → `.text`)
  - `0x00C2214B` → [HalpAcpiGetTable](../../text/3F/HalpAcpiGetTable_function_003F6BF8.md) (`INIT` → `.text`)
  - `0x00C221CA` → [HalpMmAllocateMemoryInternal](../../text/54/HalpMmAllocateMemoryInternal_function_00544990.md) (`INIT` → `.text`)
  - `0x00C22226` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C224A8` → [qsort](../../text/50/qsort_function_005009F0.md) (`INIT` → `.text`)
  - `0x00C224C5` → [qsort](../../text/50/qsort_function_005009F0.md) (`INIT` → `.text`)
  - `0x00C225F4` → [HalpAcpiGetTable](../../text/3F/HalpAcpiGetTable_function_003F6BF8.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C220D8  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00C220DD  55                              push rbp
00C220DE  53                              push rbx
00C220DF  56                              push rsi
00C220E0  57                              push rdi
00C220E1  41 54                           push r12
00C220E3  41 55                           push r13
00C220E5  41 56                           push r14
00C220E7  41 57                           push r15
00C220E9  48 8B EC                        mov rbp, rsp
00C220EC  48 83 EC 58                     sub rsp, 0x58
00C220F0  33 F6                           xor esi, esi
00C220F2  45 33 C9                        xor r9d, r9d
00C220F5  45 33 C0                        xor r8d, r8d
00C220F8  89 75 60                        mov dword ptr [rbp + 0x60], esi
00C220FB  BA 4D 50 53 54                  mov edx, 0x5453504d
00C22100  89 75 F0                        mov dword ptr [rbp - 0x10], esi
00C22103  4C 8B F1                        mov r14, rcx
00C22106  89 75 E8                        mov dword ptr [rbp - 0x18], esi
00C22109  44 8D 7E 01                     lea r15d, [rsi + 1]
00C2210D  89 75 EC                        mov dword ptr [rbp - 0x14], esi
00C22110  44 88 3D 4D E5 36 00            mov byte ptr [rip + 0x36e54d], r15b
00C22117  E8 DC 4A 7D FF                  call 0x1403f6bf8
00C2211C  45 33 C9                        xor r9d, r9d
00C2211F  48 89 05 C2 F6 1E 00            mov qword ptr [rip + 0x1ef6c2], rax
00C22126  45 33 C0                        xor r8d, r8d
00C22129  BA 53 52 41 54                  mov edx, 0x54415253
00C2212E  49 8B CE                        mov rcx, r14
00C22131  E8 C2 4A 7D FF                  call 0x1403f6bf8
00C22136  45 33 C9                        xor r9d, r9d
00C22139  48 89 05 D8 E4 36 00            mov qword ptr [rip + 0x36e4d8], rax
00C22140  45 33 C0                        xor r8d, r8d
00C22143  BA 4D 53 43 54                  mov edx, 0x5443534d
00C22148  49 8B CE                        mov rcx, r14
00C2214B  E8 A8 4A 7D FF                  call 0x1403f6bf8
00C22150  48 89 05 19 E5 36 00            mov qword ptr [rip + 0x36e519], rax
00C22157  48 8B 05 BA E4 36 00            mov rax, qword ptr [rip + 0x36e4ba]
00C2215E  48 85 C0                        test rax, rax
00C22161  75 0D                           jne 0x140c22170
00C22163  49 8B CE                        mov rcx, r14
00C22166  E8 E9 FB FF FF                  call 0x140c21d54
00C2216B  E9 F6 07 00 00                  jmp 0x140c22966
00C22170  8A 40 08                        mov al, byte ptr [rax + 8]
00C22173  4C 8D 4D 60                     lea r9, [rbp + 0x60]
00C22177  3C 03                           cmp al, 3
00C22179  88 45 50                        mov byte ptr [rbp + 0x50], al
00C2217C  4C 8D 45 E8                     lea r8, [rbp - 0x18]
00C22180  48 8D 55 EC                     lea rdx, [rbp - 0x14]
00C22184  0F 93 45 58                     setae byte ptr [rbp + 0x58]
00C22188  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00C2218C  E8 AF F9 FF FF                  call 0x140c21b40
00C22191  84 C0                           test al, al
00C22193  0F 84 CD 07 00 00               je 0x140c22966
00C22199  8B 7D E8                        mov edi, dword ptr [rbp - 0x18]
00C2219C  44 8B C7                        mov r8d, edi
00C2219F  8B 5D EC                        mov ebx, dword ptr [rbp - 0x14]
00C221A2  8B D3                           mov edx, ebx
00C221A4  44 8B 4D 60                     mov r9d, dword ptr [rbp + 0x60]
00C221A8  8B 4D F0                        mov ecx, dword ptr [rbp - 0x10]
00C221AB  E8 5C F7 FF FF                  call 0x140c2190c
00C221B0  48 39 35 A1 E4 36 00            cmp qword ptr [rip + 0x36e4a1], rsi
00C221B7  0F 84 A9 07 00 00               je 0x140c22966
00C221BD  85 FF                           test edi, edi
00C221BF  74 1E                           je 0x140c221df
00C221C1  8D 0C 7F                        lea ecx, [rdi + rdi*2]
00C221C4  41 8B D7                        mov edx, r15d
00C221C7  C1 E1 03                        shl ecx, 3
00C221CA  E8 C1 27 92 FF                  call 0x140544990
00C221CF  48 89 05 52 E4 36 00            mov qword ptr [rip + 0x36e452], rax
00C221D6  48 85 C0                        test rax, rax
00C221D9  0F 84 87 07 00 00               je 0x140c22966
00C221DF  8B FE                           mov edi, esi
00C221E1  85 DB                           test ebx, ebx
00C221E3  74 6C                           je 0x140c22251
00C221E5  83 FB 04                        cmp ebx, 4
00C221E8  72 41                           jb 0x140c2222b
00C221EA  48 8B 15 67 E4 36 00            mov rdx, qword ptr [rip + 0x36e467]
00C221F1  8D 43 FF                        lea eax, [rbx - 1]
00C221F4  4C 8B 0A                        mov r9, qword ptr [rdx]
00C221F7  49 8D 04 81                     lea rax, [r9 + rax*4]
00C221FB  4C 3B CA                        cmp r9, rdx
00C221FE  77 05                           ja 0x140c22205
00C22200  48 3B C2                        cmp rax, rdx
00C22203  73 26                           jae 0x140c2222b
00C22205  8B C3                           mov eax, ebx
00C22207  83 E0 FC                        and eax, 0xfffffffc
00C2220A  83 C7 04                        add edi, 4
00C2220D  3B F8                           cmp edi, eax
00C2220F  72 F9                           jb 0x140c2220a
00C22211  44 8B C0                        mov r8d, eax
00C22214  83 CA FF                        or edx, 0xffffffff
00C22217  49 C1 E8 02                     shr r8, 2
00C2221B  49 8B C9                        mov rcx, r9
00C2221E  49 C1 E0 04                     shl r8, 4
00C22222  49 83 E0 FC                     and r8, 0xfffffffffffffffc
00C22226  E8 15 4A AA FF                  call 0x1406c6c40
00C2222B  3B FB                           cmp edi, ebx
00C2222D  73 22                           jae 0x140c22251
00C2222F  8B D7                           mov edx, edi
00C22231  48 C1 E2 02                     shl rdx, 2
00C22235  2B DF                           sub ebx, edi
00C22237  44 8B C3                        mov r8d, ebx
00C2223A  48 8B 05 17 E4 36 00            mov rax, qword ptr [rip + 0x36e417]
00C22241  48 8B 08                        mov rcx, qword ptr [rax]
00C22244  83 0C 0A FF                     or dword ptr [rdx + rcx], 0xffffffff
00C22248  48 8D 52 04                     lea rdx, [rdx + 4]
00C2224C  4D 2B C7                        sub r8, r15
00C2224F  75 E9                           jne 0x140c2223a
00C22251  48 8B 05 C0 E3 36 00            mov rax, qword ptr [rip + 0x36e3c0]
00C22258  44 8B FE                        mov r15d, esi
00C2225B  8B DE                           mov ebx, esi
00C2225D  44 8A E6                        mov r12b, sil
00C22260  44 8B EE                        mov r13d, esi
00C22263  8B 78 04                        mov edi, dword ptr [rax + 4]
00C22266  4C 8D 50 30                     lea r10, [rax + 0x30]
00C2226A  48 03 F8                        add rdi, rax
00C2226D  49 8D 42 02                     lea rax, [r10 + 2]
00C22271  48 3B C7                        cmp rax, rdi
00C22274  0F 87 FF 01 00 00               ja 0x140c22479
00C2227A  48 8B 35 D7 E3 36 00            mov rsi, qword ptr [rip + 0x36e3d7]
00C22281  44 8A 75 50                     mov r14b, byte ptr [rbp + 0x50]
00C22285  41 0F B6 42 01                  movzx eax, byte ptr [r10 + 1]
00C2228A  3C 02                           cmp al, 2
00C2228C  0F 82 E3 01 00 00               jb 0x140c22475
00C22292  4D 8D 1C 02                     lea r11, [r10 + rax]
00C22296  4C 3B DF                        cmp r11, rdi
00C22299  0F 87 D6 01 00 00               ja 0x140c22475
00C2229F  8A 55 58                        mov dl, byte ptr [rbp + 0x58]
00C222A2  49 8B CA                        mov rcx, r10
00C222A5  E8 AE 0E 00 00                  call 0x140c23158
00C222AA  84 C0                           test al, al
00C222AC  75 08                           jne 0x140c222b6
00C222AE  4D 8B D3                        mov r10, r11
00C222B1  E9 B2 01 00 00                  jmp 0x140c22468
00C222B6  48 8B 05 5B E3 36 00            mov rax, qword ptr [rip + 0x36e35b]
00C222BD  41 B9 01 00 00 00               mov r9d, 1
00C222C3  44 38 48 08                     cmp byte ptr [rax + 8], r9b
00C222C7  75 07                           jne 0x140c222d0
00C222C9  45 0F B6 42 02                  movzx r8d, byte ptr [r10 + 2]
00C222CE  EB 40                           jmp 0x140c22310
00C222D0  41 8A 02                        mov al, byte ptr [r10]
00C222D3  84 C0                           test al, al
00C222D5  75 2B                           jne 0x140c22302
00C222D7  41 0F B6 42 0A                  movzx eax, byte ptr [r10 + 0xa]
00C222DC  45 0F B6 42 0B                  movzx r8d, byte ptr [r10 + 0xb]
00C222E1  41 C1 E0 08                     shl r8d, 8
00C222E5  44 03 C0                        add r8d, eax
00C222E8  41 0F B6 42 09                  movzx eax, byte ptr [r10 + 9]
00C222ED  41 C1 E0 08                     shl r8d, 8
00C222F1  44 03 C0                        add r8d, eax
00C222F4  41 0F B6 42 02                  movzx eax, byte ptr [r10 + 2]
00C222F9  41 C1 E0 08                     shl r8d, 8
00C222FD  44 03 C0                        add r8d, eax
00C22300  EB 0E                           jmp 0x140c22310
00C22302  3C 02                           cmp al, 2
00C22304  75 06                           jne 0x140c2230c
00C22306  45 8B 42 04                     mov r8d, dword ptr [r10 + 4]
00C2230A  EB 04                           jmp 0x140c22310
00C2230C  45 8B 42 02                     mov r8d, dword ptr [r10 + 2]
00C22310  8B 4E 38                        mov ecx, dword ptr [rsi + 0x38]
00C22313  45 33 DB                        xor r11d, r11d
00C22316  85 C9                           test ecx, ecx
00C22318  74 15                           je 0x140c2232f
00C2231A  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
00C2231E  44 3B 00                        cmp r8d, dword ptr [rax]
00C22321  74 0C                           je 0x140c2232f
00C22323  45 03 D9                        add r11d, r9d
00C22326  48 83 C0 04                     add rax, 4
00C2232A  44 3B D9                        cmp r11d, ecx
00C2232D  72 EF                           jb 0x140c2231e
00C2232F  44 3B D9                        cmp r11d, ecx
00C22332  75 1B                           jne 0x140c2234f
00C22334  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
00C22338  46 89 04 98                     mov dword ptr [rax + r11*4], r8d
00C2233C  48 8B 05 15 E3 36 00            mov rax, qword ptr [rip + 0x36e315]
00C22343  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00C22347  46 89 04 99                     mov dword ptr [rcx + r11*4], r8d
00C2234B  44 01 4E 38                     add dword ptr [rsi + 0x38], r9d
00C2234F  41 0F B6 12                     movzx edx, byte ptr [r10]
00C22353  8B CA                           mov ecx, edx
00C22355  85 D2                           test edx, edx
00C22357  74 0E                           je 0x140c22367
00C22359  41 2B C9                        sub ecx, r9d
00C2235C  74 29                           je 0x140c22387
00C2235E  41 3B C9                        cmp ecx, r9d
00C22361  0F 85 F9 00 00 00               jne 0x140c22460
00C22367  84 D2                           test dl, dl
00C22369  0F 85 91 00 00 00               jne 0x140c22400
00C2236F  45 0F B6 4A 03                  movzx r9d, byte ptr [r10 + 3]
00C22374  41 81 F9 FF 00 00 00            cmp r9d, 0xff
00C2237B  0F 85 83 00 00 00               jne 0x140c22404
00C22381  41 83 C9 FF                     or r9d, 0xffffffff
00C22385  EB 7D                           jmp 0x140c22404
00C22387  4D 8B 4A 08                     mov r9, qword ptr [r10 + 8]
00C2238B  49 8B 4A 10                     mov rcx, qword ptr [r10 + 0x10]
00C2238F  49 C1 E9 0C                     shr r9, 0xc
00C22393  48 C1 E9 0C                     shr rcx, 0xc
00C22397  4D 8D 59 FF                     lea r11, [r9 - 1]
00C2239B  4C 03 D9                        add r11, rcx
00C2239E  4C 3B 0D 83 84 1E 00            cmp r9, qword ptr [rip + 0x1e8483]
00C223A5  73 07                           jae 0x140c223ae
00C223A7  4C 89 0D 7A 84 1E 00            mov qword ptr [rip + 0x1e847a], r9
00C223AE  4C 3B 1D 4B E2 36 00            cmp r11, qword ptr [rip + 0x36e24b]
00C223B5  76 07                           jbe 0x140c223be
00C223B7  4C 89 1D 42 E2 36 00            mov qword ptr [rip + 0x36e242], r11
00C223BE  48 8B 05 43 E2 36 00            mov rax, qword ptr [rip + 0x36e243]
00C223C5  48 01 0D 6C E2 36 00            add qword ptr [rip + 0x36e26c], rcx
00C223CC  8B CB                           mov ecx, ebx
00C223CE  48 03 C9                        add rcx, rcx
00C223D1  8B D3                           mov edx, ebx
00C223D3  FF C3                           inc ebx
00C223D5  4C 89 0C C8                     mov qword ptr [rax + rcx*8], r9
00C223D9  48 8B 05 28 E2 36 00            mov rax, qword ptr [rip + 0x36e228]
00C223E0  44 89 44 C8 08                  mov dword ptr [rax + rcx*8 + 8], r8d
00C223E5  48 8D 0C 52                     lea rcx, [rdx + rdx*2]
00C223E9  48 8B 05 38 E2 36 00            mov rax, qword ptr [rip + 0x36e238]
00C223F0  4C 89 4C C8 08                  mov qword ptr [rax + rcx*8 + 8], r9
00C223F5  4C 89 5C C8 10                  mov qword ptr [rax + rcx*8 + 0x10], r11
00C223FA  44 89 04 C8                     mov dword ptr [rax + rcx*8], r8d
00C223FE  EB 60                           jmp 0x140c22460
00C22400  45 8B 4A 08                     mov r9d, dword ptr [r10 + 8]
00C22404  48 8B 15 4D E2 36 00            mov rdx, qword ptr [rip + 0x36e24d]
00C2240B  41 8B CF                        mov ecx, r15d
00C2240E  48 8B 02                        mov rax, qword ptr [rdx]
00C22411  44 89 0C 88                     mov dword ptr [rax + rcx*4], r9d
00C22415  41 B9 01 00 00 00               mov r9d, 1
00C2241B  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
00C2241F  45 03 F9                        add r15d, r9d
00C22422  44 89 04 88                     mov dword ptr [rax + rcx*4], r8d
00C22426  48 8B 42 28                     mov rax, qword ptr [rdx + 0x28]
00C2242A  46 01 0C 98                     add dword ptr [rax + r11*4], r9d
00C2242E  41 80 FE 03                     cmp r14b, 3
00C22432  72 2C                           jb 0x140c22460
00C22434  41 80 3A 00                     cmp byte ptr [r10], 0
00C22438  75 06                           jne 0x140c22440
00C2243A  41 8B 42 0C                     mov eax, dword ptr [r10 + 0xc]
00C2243E  EB 04                           jmp 0x140c22444
00C22440  41 8B 42 10                     mov eax, dword ptr [r10 + 0x10]
00C22444  45 84 E4                        test r12b, r12b
00C22447  75 08                           jne 0x140c22451
00C22449  45 8A E1                        mov r12b, r9b
00C2244C  44 8B E8                        mov r13d, eax
00C2244F  EB 0F                           jmp 0x140c22460
00C22451  44 3B E8                        cmp r13d, eax
00C22454  74 0A                           je 0x140c22460
00C22456  C7 05 C0 83 1E 00 02 00 00 00   mov dword ptr [rip + 0x1e83c0], 2
00C22460  41 0F B6 42 01                  movzx eax, byte ptr [r10 + 1]
00C22465  4C 03 D0                        add r10, rax
00C22468  49 8D 42 02                     lea rax, [r10 + 2]
00C2246C  48 3B C7                        cmp rax, rdi
00C2246F  0F 86 10 FE FF FF               jbe 0x140c22285
00C22475  4C 8B 75 48                     mov r14, qword ptr [rbp + 0x48]
00C22479  48 8B 05 D8 E1 36 00            mov rax, qword ptr [rip + 0x36e1d8]
00C22480  4C 8D 0D 19 6A 93 FF            lea r9, [rip - 0x6c95e7]
00C22487  BF 10 00 00 00                  mov edi, 0x10
00C2248C  8B D3                           mov edx, ebx
00C2248E  44 8B C7                        mov r8d, edi
00C22491  89 1D 99 E1 36 00               mov dword ptr [rip + 0x36e199], ebx
00C22497  89 1D B3 E1 36 00               mov dword ptr [rip + 0x36e1b3], ebx
00C2249D  44 89 78 3C                     mov dword ptr [rax + 0x3c], r15d
00C224A1  48 8B 0D 60 E1 36 00            mov rcx, qword ptr [rip + 0x36e160]
00C224A8  E8 43 E5 8D FF                  call 0x1405009f0
00C224AD  8B 15 9D E1 36 00               mov edx, dword ptr [rip + 0x36e19d]
00C224B3  4C 8D 0D B6 69 93 FF            lea r9, [rip - 0x6c964a]
00C224BA  48 8B 0D 67 E1 36 00            mov rcx, qword ptr [rip + 0x36e167]
00C224C1  44 8D 47 08                     lea r8d, [rdi + 8]
00C224C5  E8 26 E5 8D FF                  call 0x1405009f0
00C224CA  45 33 ED                        xor r13d, r13d
00C224CD  44 8D 7F F1                     lea r15d, [rdi - 0xf]
00C224D1  45 8B CD                        mov r9d, r13d
00C224D4  41 3B DF                        cmp ebx, r15d
00C224D7  76 39                           jbe 0x140c22512
00C224D9  41 8B CD                        mov ecx, r13d
00C224DC  44 8D 53 FF                     lea r10d, [rbx - 1]
00C224E0  8B D7                           mov edx, edi
00C224E2  4C 8B 05 1F E1 36 00            mov r8, qword ptr [rip + 0x36e11f]
00C224E9  42 8B 44 02 08                  mov eax, dword ptr [rdx + r8 + 8]
00C224EE  42 39 44 01 08                  cmp dword ptr [rcx + r8 + 8], eax
00C224F3  74 15                           je 0x140c2250a
00C224F5  42 0F 10 04 02                  movups xmm0, xmmword ptr [rdx + r8]
00C224FA  45 03 CF                        add r9d, r15d
00C224FD  41 8B C9                        mov ecx, r9d
00C22500  48 C1 E1 04                     shl rcx, 4
00C22504  F3 42 0F 7F 04 01               movdqu xmmword ptr [rcx + r8], xmm0
00C2250A  48 03 D7                        add rdx, rdi
00C2250D  4D 2B D7                        sub r10, r15
00C22510  75 D0                           jne 0x140c224e2
00C22512  48 8B 05 EF E0 36 00            mov rax, qword ptr [rip + 0x36e0ef]
00C22519  41 8D 51 01                     lea edx, [r9 + 1]
00C2251D  8B CA                           mov ecx, edx
00C2251F  48 03 C9                        add rcx, rcx
00C22522  89 15 08 E1 36 00               mov dword ptr [rip + 0x36e108], edx
00C22528  89 15 32 E1 36 00               mov dword ptr [rip + 0x36e132], edx
00C2252E  44 8B CA                        mov r9d, edx
00C22531  48 83 0C C8 FF                  or qword ptr [rax + rcx*8], 0xffffffffffffffff
00C22536  48 8B 05 CB E0 36 00            mov rax, qword ptr [rip + 0x36e0cb]
00C2253D  8B CA                           mov ecx, edx
00C2253F  48 03 C9                        add rcx, rcx
00C22542  44 89 6C C8 08                  mov dword ptr [rax + rcx*8 + 8], r13d
00C22547  48 8B 05 BA E0 36 00            mov rax, qword ptr [rip + 0x36e0ba]
00C2254E  4C 89 28                        mov qword ptr [rax], r13
00C22551  85 D2                           test edx, edx
00C22553  74 46                           je 0x140c2259b
00C22555  4C 8B 15 FC E0 36 00            mov r10, qword ptr [rip + 0x36e0fc]
00C2255C  4D 8B C5                        mov r8, r13
00C2255F  45 8B 5A 38                     mov r11d, dword ptr [r10 + 0x38]
00C22563  41 8B D5                        mov edx, r13d
00C22566  48 8B 1D 9B E0 36 00            mov rbx, qword ptr [rip + 0x36e09b]
00C2256D  41 3B D3                        cmp edx, r11d
00C22570  73 21                           jae 0x140c22593
00C22572  49 8B 42 18                     mov rax, qword ptr [r10 + 0x18]
00C22576  8B CA                           mov ecx, edx
00C22578  8B 0C 88                        mov ecx, dword ptr [rax + rcx*4]
00C2257B  41 39 4C 18 08                  cmp dword ptr [r8 + rbx + 8], ecx
00C22580  74 05                           je 0x140c22587
00C22582  41 03 D7                        add edx, r15d
00C22585  EB E6                           jmp 0x140c2256d
00C22587  48 8B 05 7A E0 36 00            mov rax, qword ptr [rip + 0x36e07a]
00C2258E  41 89 54 00 08                  mov dword ptr [r8 + rax + 8], edx
00C22593  4C 03 C7                        add r8, rdi
00C22596  4D 2B CF                        sub r9, r15
00C22599  75 C4                           jne 0x140c2255f
00C2259B  4C 39 2D CE E0 36 00            cmp qword ptr [rip + 0x36e0ce], r13
00C225A2  74 42                           je 0x140c225e6
00C225A4  48 8B 15 AD E0 36 00            mov rdx, qword ptr [rip + 0x36e0ad]
00C225AB  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
00C225AF  4C 8D 42 3C                     lea r8, [rdx + 0x3c]
00C225B3  44 8B 4A 44                     mov r9d, dword ptr [rdx + 0x44]
00C225B7  48 8D 4A 38                     lea rcx, [rdx + 0x38]
00C225BB  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00C225C0  48 8B 42 28                     mov rax, qword ptr [rdx + 0x28]
00C225C4  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00C225C9  48 8B 42 18                     mov rax, qword ptr [rdx + 0x18]
00C225CD  8B 52 40                        mov edx, dword ptr [rdx + 0x40]
00C225D0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00C225D5  48 8D 05 44 82 1E 00            lea rax, [rip + 0x1e8244]
00C225DC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C225E1  E8 CA 07 00 00                  call 0x140c22db0
00C225E6  45 33 C9                        xor r9d, r9d
00C225E9  45 33 C0                        xor r8d, r8d
00C225EC  BA 53 4C 49 54                  mov edx, 0x54494c53
00C225F1  49 8B CE                        mov rcx, r14
00C225F4  E8 FF 45 7D FF                  call 0x1403f6bf8
00C225F9  4C 8B D0                        mov r10, rax
00C225FC  48 85 C0                        test rax, rax
00C225FF  0F 84 A6 00 00 00               je 0x140c226ab
00C22605  44 8B 58 24                     mov r11d, dword ptr [rax + 0x24]
00C22609  41 8B CB                        mov ecx, r11d
00C2260C  41 0F AF CB                     imul ecx, r11d
00C22610  83 C1 2C                        add ecx, 0x2c
00C22613  3B 48 04                        cmp ecx, dword ptr [rax + 4]
00C22616  0F 87 96 00 00 00               ja 0x140c226b2
00C2261C  4C 8B 05 35 E0 36 00            mov r8, qword ptr [rip + 0x36e035]
00C22623  45 8B CD                        mov r9d, r13d
00C22626  45 3B 48 38                     cmp r9d, dword ptr [r8 + 0x38]
00C2262A  73 7F                           jae 0x140c226ab
00C2262C  49 8B 40 18                     mov rax, qword ptr [r8 + 0x18]
00C22630  41 8B C9                        mov ecx, r9d
00C22633  8B 3C 88                        mov edi, dword ptr [rax + rcx*4]
00C22636  41 3B FB                        cmp edi, r11d
00C22639  73 77                           jae 0x140c226b2
00C2263B  41 0F AF FB                     imul edi, r11d
00C2263F  41 8B DD                        mov ebx, r13d
00C22642  41 3B 58 38                     cmp ebx, dword ptr [r8 + 0x38]
00C22646  73 3C                           jae 0x140c22684
00C22648  49 8B 40 18                     mov rax, qword ptr [r8 + 0x18]
00C2264C  8B CB                           mov ecx, ebx
00C2264E  8B 14 88                        mov edx, dword ptr [rax + rcx*4]
00C22651  41 3B D3                        cmp edx, r11d
00C22654  73 5C                           jae 0x140c226b2
00C22656  8D 04 3A                        lea eax, [rdx + rdi]
00C22659  42 0F B6 44 10 2C               movzx eax, byte ptr [rax + r10 + 0x2c]
00C2265F  3C 0A                           cmp al, 0xa
00C22661  72 4F                           jb 0x140c226b2
00C22663  B9 80 00 00 00                  mov ecx, 0x80
00C22668  8B D0                           mov edx, eax
00C2266A  49 8B 40 30                     mov rax, qword ptr [r8 + 0x30]
00C2266E  0F AF D1                        imul edx, ecx
00C22671  41 8B C9                        mov ecx, r9d
00C22674  41 0F AF 48 40                  imul ecx, dword ptr [r8 + 0x40]
00C22679  03 CB                           add ecx, ebx
00C2267B  41 03 DF                        add ebx, r15d
00C2267E  66 89 14 48                     mov word ptr [rax + rcx*2], dx
00C22682  EB BE                           jmp 0x140c22642
00C22684  41 8B 48 40                     mov ecx, dword ptr [r8 + 0x40]
00C22688  BA 00 05 00 00                  mov edx, 0x500
00C2268D  49 8B 40 30                     mov rax, qword ptr [r8 + 0x30]
00C22691  41 03 CF                        add ecx, r15d
00C22694  41 0F AF C9                     imul ecx, r9d
00C22698  66 39 14 48                     cmp word ptr [rax + rcx*2], dx
00C2269C  75 14                           jne 0x140c226b2
00C2269E  66 44 89 2C 48                  mov word ptr [rax + rcx*2], r13w
00C226A3  45 03 CF                        add r9d, r15d
00C226A6  E9 7B FF FF FF                  jmp 0x140c22626
00C226AB  4C 89 15 B6 DF 36 00            mov qword ptr [rip + 0x36dfb6], r10
00C226B2  4C 39 2D AF DF 36 00            cmp qword ptr [rip + 0x36dfaf], r13
00C226B9  49 8B 86 F0 00 00 00            mov rax, qword ptr [r14 + 0xf0]
00C226C0  4C 8B 88 28 01 00 00            mov r9, qword ptr [rax + 0x128]
00C226C7  49 8D 71 04                     lea rsi, [r9 + 4]
00C226CB  0F 85 45 01 00 00               jne 0x140c22816
00C226D1  4D 85 C9                        test r9, r9
00C226D4  0F 84 EA 00 00 00               je 0x140c227c4
00C226DA  48 8B 15 77 DF 36 00            mov rdx, qword ptr [rip + 0x36df77]
00C226E1  41 8B 01                        mov eax, dword ptr [r9]
00C226E4  48 8D 7A 38                     lea rdi, [rdx + 0x38]
00C226E8  3B 07                           cmp eax, dword ptr [rdi]
00C226EA  0F 85 D4 00 00 00               jne 0x140c227c4
00C226F0  41 8B DD                        mov ebx, r13d
00C226F3  4C 8D 24 86                     lea r12, [rsi + rax*4]
00C226F7  45 8B D5                        mov r10d, r13d
00C226FA  4C 8D 7A 18                     lea r15, [rdx + 0x18]
00C226FE  44 3B 17                        cmp r10d, dword ptr [rdi]
00C22701  0F 83 0F 01 00 00               jae 0x140c22816
00C22707  45 8B 19                        mov r11d, dword ptr [r9]
00C2270A  45 8B C5                        mov r8d, r13d
00C2270D  45 8B F2                        mov r14d, r10d
00C22710  45 3B C3                        cmp r8d, r11d
00C22713  73 1D                           jae 0x140c22732
00C22715  49 8B 07                        mov rax, qword ptr [r15]
00C22718  41 8B D0                        mov edx, r8d
00C2271B  42 8B 0C B0                     mov ecx, dword ptr [rax + r14*4]
00C2271F  39 0C 96                        cmp dword ptr [rsi + rdx*4], ecx
00C22722  74 05                           je 0x140c22729
00C22724  41 FF C0                        inc r8d
00C22727  EB E7                           jmp 0x140c22710
00C22729  41 8B D8                        mov ebx, r8d
00C2272C  41 0F AF DB                     imul ebx, r11d
00C22730  EB 06                           jmp 0x140c22738
00C22732  0F 84 86 00 00 00               je 0x140c227be
00C22738  45 8B DD                        mov r11d, r13d
00C2273B  41 B8 01 00 00 00               mov r8d, 1
00C22741  44 3B 1F                        cmp r11d, dword ptr [rdi]
00C22744  73 56                           jae 0x140c2279c
00C22746  41 8B 11                        mov edx, dword ptr [r9]
00C22749  41 8B CD                        mov ecx, r13d
00C2274C  45 8B C3                        mov r8d, r11d
00C2274F  85 D2                           test edx, edx
00C22751  74 19                           je 0x140c2276c
00C22753  49 8B 07                        mov rax, qword ptr [r15]
00C22756  46 8B 04 80                     mov r8d, dword ptr [rax + r8*4]
00C2275A  48 8B C6                        mov rax, rsi
00C2275D  44 39 00                        cmp dword ptr [rax], r8d
00C22760  74 0A                           je 0x140c2276c
00C22762  FF C1                           inc ecx
00C22764  48 83 C0 04                     add rax, 4
00C22768  3B CA                           cmp ecx, edx
00C2276A  72 F1                           jb 0x140c2275d
00C2276C  3B CA                           cmp ecx, edx
00C2276E  74 4E                           je 0x140c227be
00C22770  8D 04 0B                        lea eax, [rbx + rcx]
00C22773  41 8B D2                        mov edx, r10d
00C22776  48 8B 0D DB DE 36 00            mov rcx, qword ptr [rip + 0x36dedb]
00C2277D  41 B8 01 00 00 00               mov r8d, 1
00C22783  41 0F B7 04 44                  movzx eax, word ptr [r12 + rax*2]
00C22788  0F AF 51 40                     imul edx, dword ptr [rcx + 0x40]
00C2278C  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
00C22790  41 03 D3                        add edx, r11d
00C22793  45 03 D8                        add r11d, r8d
00C22796  66 89 04 51                     mov word ptr [rcx + rdx*2], ax
00C2279A  EB A5                           jmp 0x140c22741
00C2279C  48 8B 15 B5 DE 36 00            mov rdx, qword ptr [rip + 0x36deb5]
00C227A3  8B 4A 40                        mov ecx, dword ptr [rdx + 0x40]
00C227A6  48 8B 42 30                     mov rax, qword ptr [rdx + 0x30]
00C227AA  41 03 C8                        add ecx, r8d
00C227AD  41 0F AF CA                     imul ecx, r10d
00C227B1  45 03 D0                        add r10d, r8d
00C227B4  66 44 89 2C 48                  mov word ptr [rax + rcx*2], r13w
00C227B9  E9 40 FF FF FF                  jmp 0x140c226fe
00C227BE  41 BF 01 00 00 00               mov r15d, 1
00C227C4  48 8B 15 8D DE 36 00            mov rdx, qword ptr [rip + 0x36de8d]
00C227CB  45 8B C5                        mov r8d, r13d
00C227CE  8B 42 38                        mov eax, dword ptr [rdx + 0x38]
00C227D1  85 C0                           test eax, eax
00C227D3  74 41                           je 0x140c22816
00C227D5  45 8B CD                        mov r9d, r13d
00C227D8  85 C0                           test eax, eax
00C227DA  74 1C                           je 0x140c227f8
00C227DC  48 8B 42 30                     mov rax, qword ptr [rdx + 0x30]
00C227E0  41 8B C8                        mov ecx, r8d
00C227E3  0F AF 4A 40                     imul ecx, dword ptr [rdx + 0x40]
00C227E7  41 03 C9                        add ecx, r9d
00C227EA  45 03 CF                        add r9d, r15d
00C227ED  66 44 89 3C 48                  mov word ptr [rax + rcx*2], r15w
00C227F2  44 3B 4A 38                     cmp r9d, dword ptr [rdx + 0x38]
00C227F6  72 E4                           jb 0x140c227dc
00C227F8  8B 4A 40                        mov ecx, dword ptr [rdx + 0x40]
00C227FB  48 8B 42 30                     mov rax, qword ptr [rdx + 0x30]
00C227FF  41 03 CF                        add ecx, r15d
00C22802  41 0F AF C8                     imul ecx, r8d
00C22806  45 03 C7                        add r8d, r15d
00C22809  66 44 89 2C 48                  mov word ptr [rax + rcx*2], r13w
00C2280E  8B 42 38                        mov eax, dword ptr [rdx + 0x38]
00C22811  44 3B C0                        cmp r8d, eax
00C22814  72 BF                           jb 0x140c227d5
00C22816  44 38 2D 45 DC 1E 00            cmp byte ptr [rip + 0x1edc45], r13b
00C2281D  0F 84 2B 01 00 00               je 0x140c2294e
00C22823  48 8B 1D 2E DE 36 00            mov rbx, qword ptr [rip + 0x36de2e]
00C2282A  48 89 5D 50                     mov qword ptr [rbp + 0x50], rbx
00C2282E  4C 8B 03                        mov r8, qword ptr [rbx]
00C22831  48 8B 53 10                     mov rdx, qword ptr [rbx + 0x10]
00C22835  8B 4B 3C                        mov ecx, dword ptr [rbx + 0x3c]
00C22838  E8 D7 04 00 00                  call 0x140c22d14
00C2283D  8B 7B 38                        mov edi, dword ptr [rbx + 0x38]
00C22840  41 8B F5                        mov esi, r13d
00C22843  85 FF                           test edi, edi
00C22845  0F 84 03 01 00 00               je 0x140c2294e
00C2284B  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
00C2284F  44 8B 3D C6 7F 1E 00            mov r15d, dword ptr [rip + 0x1e7fc6]
00C22856  44 8B F6                        mov r14d, esi
00C22859  46 39 3C B0                     cmp dword ptr [rax + r14*4], r15d
00C2285D  0F 86 DE 00 00 00               jbe 0x140c22941
00C22863  E8 48 F2 FF FF                  call 0x140c21ab0
00C22868  4C 8B 15 E9 DD 36 00            mov r10, qword ptr [rip + 0x36dde9]
00C2286F  8D 4F 01                        lea ecx, [rdi + 1]
00C22872  89 4B 38                        mov dword ptr [rbx + 0x38], ecx
00C22875  44 8B E0                        mov r12d, eax
00C22878  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
00C2287C  45 8B DD                        mov r11d, r13d
00C2287F  8B D7                           mov edx, edi
00C22881  46 8B 0C B1                     mov r9d, dword ptr [rcx + r14*4]
00C22885  46 89 3C B1                     mov dword ptr [rcx + r14*4], r15d
00C22889  45 2B CF                        sub r9d, r15d
00C2288C  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
00C22890  44 89 0C 91                     mov dword ptr [rcx + rdx*4], r9d
00C22894  49 8B 42 18                     mov rax, qword ptr [r10 + 0x18]
00C22898  44 89 24 90                     mov dword ptr [rax + rdx*4], r12d
00C2289C  49 8B 4A 20                     mov rcx, qword ptr [r10 + 0x20]
00C228A0  42 8B 04 B1                     mov eax, dword ptr [rcx + r14*4]
00C228A4  89 04 91                        mov dword ptr [rcx + rdx*4], eax
00C228A7  85 FF                           test edi, edi
00C228A9  74 4A                           je 0x140c228f5
00C228AB  BB 01 00 00 00                  mov ebx, 1
00C228B0  4D 8B 42 30                     mov r8, qword ptr [r10 + 0x30]
00C228B4  41 8B CB                        mov ecx, r11d
00C228B7  41 0F AF 4A 40                  imul ecx, dword ptr [r10 + 0x40]
00C228BC  8D 04 31                        lea eax, [rcx + rsi]
00C228BF  03 CF                           add ecx, edi
00C228C1  41 0F B7 04 40                  movzx eax, word ptr [r8 + rax*2]
00C228C6  66 41 89 04 48                  mov word ptr [r8 + rcx*2], ax
00C228CB  41 8B 4A 40                     mov ecx, dword ptr [r10 + 0x40]
00C228CF  8B C1                           mov eax, ecx
00C228D1  49 8B 52 30                     mov rdx, qword ptr [r10 + 0x30]
00C228D5  0F AF C6                        imul eax, esi
00C228D8  0F AF CF                        imul ecx, edi
00C228DB  41 03 C3                        add eax, r11d
00C228DE  41 03 CB                        add ecx, r11d
00C228E1  44 03 DB                        add r11d, ebx
00C228E4  0F B7 04 42                     movzx eax, word ptr [rdx + rax*2]
00C228E8  66 89 04 4A                     mov word ptr [rdx + rcx*2], ax
00C228EC  44 3B DF                        cmp r11d, edi
00C228EF  72 BF                           jb 0x140c228b0
00C228F1  48 8B 5D 50                     mov rbx, qword ptr [rbp + 0x50]
00C228F5  4C 8B 05 5C DD 36 00            mov r8, qword ptr [rip + 0x36dd5c]
00C228FC  41 BA 01 00 00 00               mov r10d, 1
00C22902  41 8B 48 40                     mov ecx, dword ptr [r8 + 0x40]
00C22906  49 8B 40 30                     mov rax, qword ptr [r8 + 0x30]
00C2290A  41 03 CA                        add ecx, r10d
00C2290D  0F AF CF                        imul ecx, edi
00C22910  66 44 89 2C 48                  mov word ptr [rax + rcx*2], r13w
00C22915  8B 53 3C                        mov edx, dword ptr [rbx + 0x3c]
00C22918  41 2B D2                        sub edx, r10d
00C2291B  74 24                           je 0x140c22941
00C2291D  8B FE                           mov edi, esi
00C2291F  45 85 C9                        test r9d, r9d
00C22922  74 1D                           je 0x140c22941
00C22924  49 8B 40 18                     mov rax, qword ptr [r8 + 0x18]
00C22928  4C 8B 5B 10                     mov r11, qword ptr [rbx + 0x10]
00C2292C  8B 0C B8                        mov ecx, dword ptr [rax + rdi*4]
00C2292F  41 39 0C 93                     cmp dword ptr [r11 + rdx*4], ecx
00C22933  75 07                           jne 0x140c2293c
00C22935  41 FF C9                        dec r9d
00C22938  45 89 24 93                     mov dword ptr [r11 + rdx*4], r12d
00C2293C  83 C2 FF                        add edx, -1
00C2293F  75 DE                           jne 0x140c2291f
00C22941  8B 7B 38                        mov edi, dword ptr [rbx + 0x38]
00C22944  FF C6                           inc esi
00C22946  3B F7                           cmp esi, edi
00C22948  0F 82 FD FE FF FF               jb 0x140c2284b
00C2294E  BB 01 00 00 00                  mov ebx, 1
00C22953  39 1D C7 7E 1E 00               cmp dword ptr [rip + 0x1e7ec7], ebx
00C22959  74 06                           je 0x140c22961
00C2295B  88 1D EF 16 3A 00               mov byte ptr [rip + 0x3a16ef], bl
00C22961  E8 B2 29 00 00                  call 0x140c25318
00C22966  48 83 C4 58                     add rsp, 0x58
00C2296A  41 5F                           pop r15
00C2296C  41 5E                           pop r14
00C2296E  41 5D                           pop r13
00C22970  41 5C                           pop r12
00C22972  5F                              pop rdi
00C22973  5E                              pop rsi
00C22974  5B                              pop rbx
00C22975  5D                              pop rbp
00C22976  C3                              ret
00C22977  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpNumaInitializeStaticConfiguration(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int8 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (88);
    v_rsi = 0;
    a4 = 0;
    a3 = 0;
    v_stack_p20 = 0;
    v_stack_m50 = 0;
    v_stack_m58 = 0;
    v_stack_m54 = 0;
    *(unsigned __int8 *)(v_rip + 3597645) = (unsigned __int8)(v_rsi + 1);
    result = HalpAcpiGetTable(a1, (unsigned int)(0x5453504DULL), a3, a4);
    a4 = 0;
    *(unsigned __int64 *)(v_rip + 2029250) = result;
    a3 = 0;
    result = HalpAcpiGetTable(a1, (unsigned int)(0x54415253ULL), a3, a4);
    a4 = 0;
    *(unsigned __int64 *)(v_rip + 3597528) = result;
    a3 = 0;
    result = HalpAcpiGetTable(a1, (unsigned int)(0x5443534DULL), a3, a4);
    *(unsigned __int64 *)(v_rip + 3597593) = result;
    if (*(unsigned __int64 *)(v_rip + 3597498) != 0) goto loc_00C22170;
    result = HalpInitializeConfigurationFromMadt(a1, (unsigned int)(0x5443534DULL), a3, a4);
    goto loc_00C22966;
loc_00C22170:
    v_stack_p10 = (unsigned __int8)(*(unsigned __int8 *)(result + 8));
    result = HalpGetNumaProcMemoryCount(v_stack_m50, v_stack_m54, v_stack_m58, v_stack_p20);
    if ((unsigned __int8)(result) == 0) goto loc_00C22966;
    result = HalpAllocateNumaConfigData((unsigned int)(v_stack_m50), (unsigned int)((unsigned int)((unsigned int)(v_stack_m54))), (unsigned int)((unsigned int)((unsigned int)(v_stack_m58))), (unsigned int)(v_stack_p20));
    if ((*(unsigned __int64 *)(v_rip + 3597473)) == 0) goto loc_00C22966;
    if ((unsigned int)((unsigned int)(v_stack_m58)) == 0) goto loc_00C221DF;
    a1 = (unsigned int)(((unsigned int)(v_stack_m58) + (unsigned int)(v_stack_m58) * 2) << (3));
    result = HalpMmAllocateMemoryInternal(a1, (unsigned int)((unsigned int)(v_rsi + 1)), (unsigned int)((unsigned int)((unsigned int)(v_stack_m58))), (unsigned int)(v_stack_p20));
    *(unsigned __int64 *)(v_rip + 3597394) = result;
    if (result == 0) goto loc_00C22966;
loc_00C221DF:
    if ((unsigned int)((unsigned int)(v_stack_m54)) == 0) goto loc_00C22251;
    if (((unsigned int)((unsigned int)(v_stack_m54))) < 4) goto loc_00C2222B;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3597415))) > (*(unsigned __int64 *)(v_rip + 3597415))) goto loc_00C22205;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3597415)) + (unsigned int)(v_stack_m54) - 1 * 4) >= (*(unsigned __int64 *)(v_rip + 3597415))) goto loc_00C2222B;
loc_00C22205:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m54)))) & (0xFFFFFFFCULL));
loc_00C2220A:
    v_rdi = (unsigned int)((0) + (4));
    if (((unsigned int)(v_rdi)) < ((unsigned int)(result))) goto loc_00C2220A;
    a2 = (unsigned int)((*(unsigned __int64 *)(v_rip + 3597415)) | (0xFFFFFFFFULL));
    a3 = ((unsigned int)((unsigned int)(result))) >> (2);
    a3 = (a3) << (4);
    a3 = (a3) & (-4);
    result = memset(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3597415)), a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3597415)));
loc_00C2222B:
    if (((unsigned int)(v_rdi)) >= ((unsigned int)((unsigned int)(v_stack_m54)))) goto loc_00C22251;
    a2 = ((unsigned int)((unsigned int)(v_rdi))) << (2);
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m54)) - ((unsigned int)(v_rdi)));
loc_00C2223A:
    a3 = ((unsigned int)((unsigned int)(v_rbx))) - (v_rsi + 1);
    if (condition_is_not_equal) goto loc_00C2223A;
loc_00C22251:
    v_rdi = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3597248) + 4))) + (*(unsigned __int64 *)(v_rip + 3597248));
    if ((*(unsigned __int64 *)(v_rip + 3597248) + 48 + 2) > v_rdi) goto loc_00C22479;
loc_00C22285:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1))) < 2) goto loc_00C22475;
    if ((*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1) > v_rdi) goto loc_00C22475;
    result = HalpVerifySratEntryLengthAndFlag(*(unsigned __int64 *)(v_rip + 3597248) + 48, v_stack_p18, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3597415)));
    if ((unsigned __int8)(result) != 0) goto loc_00C222B6;
    goto loc_00C22468;
loc_00C222B6:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597147) + 8)) != 1) goto loc_00C222D0;
    goto loc_00C22310;
loc_00C222D0:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1)) != 0) goto loc_00C22302;
    a3 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1 + 11)) << (8));
    a3 = (unsigned int)((a3) + ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1 + 10))));
    a3 = (unsigned int)((a3) << (8));
    a3 = (unsigned int)((a3) + ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1 + 9))));
    a3 = (unsigned int)((a3) << (8));
    a3 = (unsigned int)((a3) + ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1 + 2))));
    goto loc_00C22310;
loc_00C22302:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1 + 2))) != 2) goto loc_00C2230C;
    goto loc_00C22310;
loc_00C2230C:
loc_00C22310:
    v_r11 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3597271) + 56))) == 0) goto loc_00C2232F;
loc_00C2231E:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1 + 2)))) == (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3597271) + 24)))) goto loc_00C2232F;
    v_r11 = (unsigned int)((v_r11) + (1));
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3597271) + 24)) + (4);
    if (((unsigned int)(v_r11)) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3597271) + 56))))) goto loc_00C2231E;
loc_00C2232F:
    if (((unsigned int)(v_r11)) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3597271) + 56))))) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3597271) + 24);
        *(unsigned int *)(result + v_r11 * 4) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1 + 2)));
        result = *(unsigned __int64 *)(v_rip + 3597077);
        a1 = *(unsigned __int64 *)(result + 32);
        *(unsigned int *)(a1 + v_r11 * 4) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1 + 2)));
    }
    if ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1)) == 0) goto loc_00C22367;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1)))) - (1));
    if (condition_is_equal) goto loc_00C22387;
    if (((unsigned int)(a1)) != 1) goto loc_00C22460;
loc_00C22367:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1)) != 0) goto loc_00C22400;
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1 + 3))) != 255) goto loc_00C22404;
    a4 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1 + 3)) | (0xFFFFFFFFULL));
    goto loc_00C22404;
loc_00C22387:
    a4 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1 + 8)) >> (12);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1 + 16)) >> (12);
    v_r11 = (a4 - 1) + (a1);
    if (a4 < (*(unsigned __int64 *)(v_rip + 2000003))) {
        *(unsigned __int64 *)(v_rip + 1999994) = a4;
    }
    if (v_r11 >= = (*(unsigned __int64 *)(v_rip + 3596875))) {
        *(unsigned __int64 *)(v_rip + 3596866) = v_r11;
    }
    a1 = (0) + (0);
    v_rbx = (unsigned int)((0) + 1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3596867) + a1 * 8) = a4;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3596840) + a1 * 8 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1 + 2)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3596856) + 0 + 0 * 2 * 8 + 8) = a4;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3596856) + 0 + 0 * 2 * 8 + 16) = v_r11;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3596856) + 0 + 0 * 2 * 8) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1 + 2)));
    goto loc_00C22460;
loc_00C22400:
loc_00C22404:
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3596877)) + 0 * 4) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1 + 8)));
    v_r15 = (unsigned int)((0) + (1));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3596877) + 16) + 0 * 4) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1 + 2)));
    if (((unsigned __int8)(v_stack_p10)) < 3) goto loc_00C22460;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1)) != 0) goto loc_00C22440;
    goto loc_00C22444;
loc_00C22440:
loc_00C22444:
    if (0 != 0) goto loc_00C22451;
    goto loc_00C22460;
loc_00C22451:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1 + 16)))))) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1 + 16))))) {
        *(unsigned int *)(v_rip + 1999808) = 2;
    }
    v_r10 = (*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1) + (*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3597248) + 48 + 1) * 1 + 1));
loc_00C22468:
    if ((v_r10 + 2) <= v_rdi) goto loc_00C22285;
loc_00C22475:
loc_00C22479:
    *(unsigned int *)(v_rip + 3596697) = (unsigned int)(v_rbx);
    *(unsigned int *)(v_rip + 3596723) = (unsigned int)(v_rbx);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3596760) + 60) = (unsigned int)(v_r15);
    result = qsort(*(unsigned __int64 *)(v_rip + 3596640), (unsigned int)((unsigned int)(v_rbx)), 16, v_rip - 7116263);
    result = qsort(*(unsigned __int64 *)(v_rip + 3596647), (unsigned int)(*(unsigned int *)(v_rip + 3596701)), 16 + 8, v_rip - 7116362);
    v_r13 = 0;
    if (((unsigned int)(v_rbx)) <= ((unsigned int)(16 - 15))) goto loc_00C22512;
loc_00C224E2:
    if ((*(unsigned int *)(0 + *(unsigned __int64 *)(v_rip + 3596575) * 1 + 8)) != ((unsigned int)((unsigned int)(*(unsigned int *)(16 + *(unsigned __int64 *)(v_rip + 3596575) * 1 + 8))))) {
        a4 = (unsigned int)((0) + ((unsigned int)(16 - 15)));
        a1 = a4;
        a1 = (a1) << (4);
        *(unsigned __int64 *)(a1 + *(unsigned __int64 *)(v_rip + 3596575) * 1) = v_xmm0;
    }
    a2 = (16) + (16);
    v_r10 = (v_rbx - 1) - (16 - 15);
    if (condition_is_not_equal) goto loc_00C224E2;
loc_00C22512:
    a1 = ((unsigned int)((unsigned int)(a4 + 1))) + ((unsigned int)((unsigned int)(a4 + 1)));
    *(unsigned int *)(v_rip + 3596552) = (unsigned int)(a4 + 1);
    *(unsigned int *)(v_rip + 3596594) = (unsigned int)(a4 + 1);
    a1 = ((unsigned int)((unsigned int)(a4 + 1))) + ((unsigned int)((unsigned int)(a4 + 1)));
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3596491) + a1 * 8 + 8) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3596474)) = 0;
    if ((unsigned int)(a4 + 1) == 0) goto loc_00C2259B;
loc_00C2255F:
loc_00C2256D:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3596540) + 56))))) goto loc_00C22593;
    if ((*(unsigned int *)(0 + *(unsigned __int64 *)(v_rip + 3596443) * 1 + 8)) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3596540) + 24) + 0 * 4))))) goto loc_00C22587;
    a2 = (unsigned int)((0) + ((unsigned int)(16 - 15)));
    goto loc_00C2256D;
loc_00C22587:
    *(unsigned int *)(0 + *(unsigned __int64 *)(v_rip + 3596410) * 1 + 8) = (unsigned int)(a2);
loc_00C22593:
    a3 = (0) + (16);
    a4 = ((unsigned int)((unsigned int)(a4 + 1))) - (16 - 15);
    if (condition_is_not_equal) goto loc_00C2255F;
loc_00C2259B:
    result = *(unsigned __int64 *)(v_rip + 3596410);
    if ((*(unsigned __int64 *)(v_rip + 3596494)) != 0) {
        a2 = *(unsigned __int64 *)(v_rip + 3596461);
        result = *(unsigned __int64 *)(a2 + 16);
        a3 = a2 + 60;
        a4 = *(unsigned int *)(a2 + 68);
        a1 = a2 + 56;
        v_stack_m60 = result;
        result = *(unsigned __int64 *)(a2 + 40);
        v_stack_m68 = result;
        result = *(unsigned __int64 *)(a2 + 24);
        a2 = *(unsigned int *)(a2 + 64);
        v_stack_m70 = result;
        result = v_rip + 1999428;
        v_stack_m78 = result;
        result = HalpUpdateConfigurationFromMsct(a1, a2, a3, a4);
    }
    a4 = 0;
    a3 = 0;
    result = HalpAcpiGetTable(v_stack_p8, (unsigned int)(0x54494C53ULL), a3, a4);
    if (result == 0) goto loc_00C226AB;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 36))))) * ((unsigned int)((unsigned int)(*(unsigned int *)(result + 36)))));
    a1 = (unsigned int)((a1) + (44));
    if (((unsigned int)(a1)) > (*(unsigned int *)(result + 4))) goto loc_00C226B2;
loc_00C22626:
    if (0 >= (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3596341) + 56))) goto loc_00C226AB;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3596341) + 24) + 0 * 4)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(result + 36))))) goto loc_00C226B2;
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3596341) + 24) + 0 * 4))) * ((unsigned int)((unsigned int)(*(unsigned int *)(result + 36)))));
loc_00C22642:
    if (0 >= (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3596341) + 56))) goto loc_00C22684;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3596341) + 24) + 0 * 4)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(result + 36))))) goto loc_00C226B2;
    if (((unsigned __int8)(*(unsigned __int8 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3596341) + 24) + 0 * 4)) + v_rdi * 1 + result * 1 + 44))) < 10) goto loc_00C226B2;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3596341) + 24) + 0 * 4)) + v_rdi * 1 + result * 1 + 44)))) * (128));
    a1 = (unsigned int)((0) * (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3596341) + 64)));
    a1 = (unsigned int)((a1) + (0));
    v_rbx = (unsigned int)((0) + ((unsigned int)(16 - 15)));
    *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3596341) + 48) + a1 * 2) = (unsigned __int16)(a2);
    goto loc_00C22642;
loc_00C22684:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3596341) + 64))) + ((unsigned int)(16 - 15)));
    a1 = (unsigned int)((a1) * (0));
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3596341) + 48) + a1 * 2)) != ((unsigned __int16)((unsigned int)(0x500ULL)))) goto loc_00C226B2;
    *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3596341) + 48) + a1 * 2) = 0;
    a4 = (unsigned int)((0) + ((unsigned int)(16 - 15)));
    goto loc_00C22626;
loc_00C226AB:
    *(unsigned __int64 *)(v_rip + 3596214) = result;
loc_00C226B2:
    if ((*(unsigned __int64 *)(v_rip + 3596207)) != 0) goto loc_00C22816;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 240) + 296) == 0) goto loc_00C227C4;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 240) + 296))))) != (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3596151) + 56))) goto loc_00C227C4;
loc_00C226FE:
    if (0 >= (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3596151) + 56))) goto loc_00C22816;
loc_00C22710:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 240) + 296)))))) goto loc_00C22732;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 240) + 296) + 4 + 0 * 4)) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3596151) + 24) + 0 * 4))))) goto loc_00C22729;
    a3 = (unsigned int)((0) + 1);
    goto loc_00C22710;
loc_00C22729:
    v_rbx = (unsigned int)(((unsigned int)(a3)) * ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 240) + 296))))));
    goto loc_00C22738;
loc_00C22732:
    if (condition_is_equal) goto loc_00C227BE;
loc_00C22738:
loc_00C22741:
    if (0 >= (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3596151) + 56))) goto loc_00C2279C;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 240) + 296)))) == 0) goto loc_00C2276C;
loc_00C2275D:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 240) + 296) + 4)) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3596151) + 24) + 0 * 4))))) goto loc_00C2276C;
    a1 = (unsigned int)((0) + 1);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 240) + 296) + 4) + (4);
    if (((unsigned int)(a1)) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 240) + 296)))))) goto loc_00C2275D;
loc_00C2276C:
    if (((unsigned int)(a1)) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 240) + 296)))))) goto loc_00C227BE;
    a2 = (unsigned int)((0) * (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3595995) + 64)));
    a2 = (unsigned int)((a2) + (0));
    v_r11 = (unsigned int)((0) + (1));
    *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3595995) + 48) + a2 * 2) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 240) + 296) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 240) + 296))) * 4 + v_rbx + a1 * 1 * 2));
    goto loc_00C22741;
loc_00C2279C:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3595957) + 64))) + (1));
    a1 = (unsigned int)((a1) * (0));
    v_r10 = (unsigned int)((0) + (1));
    *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3595957) + 48) + a1 * 2) = 0;
    goto loc_00C226FE;
loc_00C227BE:
loc_00C227C4:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3595917) + 56))) == 0) goto loc_00C22816;
loc_00C227D5:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3595917) + 56))) == 0) goto loc_00C227F8;
loc_00C227DC:
    a1 = (unsigned int)((0) * (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3595917) + 64)));
    a1 = (unsigned int)((a1) + (0));
    a4 = (unsigned int)((0) + (1));
    *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3595917) + 48) + a1 * 2) = 1;
    if (a4 < (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3595917) + 56))) goto loc_00C227DC;
loc_00C227F8:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3595917) + 64))) + (1));
    a1 = (unsigned int)((a1) * (0));
    a3 = (unsigned int)((0) + (1));
    *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3595917) + 48) + a1 * 2) = 0;
    if (a3 < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3595917) + 56))))) goto loc_00C227D5;
loc_00C22816:
    if ((*(unsigned __int8 *)(v_rip + 2022469)) == 0) goto loc_00C2294E;
    v_stack_p10 = *(unsigned __int64 *)(v_rip + 3595822);
    result = HalpNumaSortProcessors((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3595822) + 60)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3595822) + 16), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3595822)), a4);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3595822) + 56))) == 0) goto loc_00C2294E;
loc_00C2284B:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3595822) + 40) + 0 * 4)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 1998790))))) goto loc_00C22941;
    result = HalpGetAvailableProximityId((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3595822) + 60)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3595822) + 16), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3595822)), a4);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3595822) + 56) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3595822) + 56)) + 1);
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3595822) + 40) + 0 * 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 1998790)));
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3595822) + 40) + 0 * 4))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 1998790)))));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3595822) + 40) + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3595822) + 56)))) * 4) = a4;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3595753) + 24) + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3595822) + 56)))) * 4) = (unsigned int)((unsigned int)((unsigned int)(result)));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3595753) + 32) + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3595822) + 56)))) * 4) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3595753) + 32) + 0 * 4)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3595822) + 56))) == 0) goto loc_00C228F5;
loc_00C228B0:
    a1 = (unsigned int)((0) * (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3595753) + 64)));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3595822) + 56)))));
    *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3595753) + 48) + a1 * 2) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3595753) + 48) + a1 + 0 * 1 * 2));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3595753) + 64))))) * (0));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3595753) + 64))) * ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3595822) + 56)))));
    result = (unsigned int)((result) + (0));
    a1 = (unsigned int)((a1) + (0));
    v_r11 = (unsigned int)((0) + (1));
    *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3595753) + 48) + a1 * 2) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3595753) + 48) + result * 2));
    if (((unsigned int)(v_r11)) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3595822) + 56))))) goto loc_00C228B0;
loc_00C228F5:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3595612) + 64))) + (1));
    a1 = (unsigned int)((a1) * ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3595822) + 56)))));
    *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3595612) + 48) + a1 * 2) = 0;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 60))) - (1));
    if (condition_is_equal) goto loc_00C22941;
loc_00C2291F:
    if (a4 == 0) goto loc_00C22941;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 16) + a2 * 4)) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3595612) + 24) + 0 * 4))))) {
        a4 = (unsigned int)((a4) - 1);
        *(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 16) + a2 * 4) = (unsigned int)((unsigned int)((unsigned int)(result)));
    }
    a2 = (unsigned int)((a2) + (-1));
    if (condition_is_not_equal) goto loc_00C2291F;
loc_00C22941:
    v_rsi = (unsigned int)((0) + 1);
    if (((unsigned int)(v_rsi)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 56))))) goto loc_00C2284B;
loc_00C2294E:
    if ((*(unsigned int *)(v_rip + 1998535)) != 1) {
        *(unsigned __int8 *)(v_rip + 3806959) = 1;
    }
    result = HalpChannelInitializeStaticConfiguration((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3595612) + 24) + 0 * 4)), a2, *(unsigned __int64 *)(v_rip + 3595612), a4);
loc_00C22966:
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpNumaInitializeStaticConfiguration(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint8_t v_stack_p10;
    uint8_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (88);
    local_rsi = 0;
    Arg4 = 0;
    Arg3 = 0;
    v_stack_p20 = 0;
    v_stack_m50 = 0;
    v_stack_m58 = 0;
    v_stack_m54 = 0;
    *(uint8_t *)(v_rip + 0x36E54D) = (uint8_t)(local_rsi + 1);
    result = HalpAcpiGetTable(Arg1, (uint32_t)(0x5453504DULL), Arg3, Arg4);
    Arg4 = 0;
    *(uint64_t *)(v_rip + 0x1EF6C2) = result;
    Arg3 = 0;
    result = HalpAcpiGetTable(Arg1, (uint32_t)(0x54415253ULL), Arg3, Arg4);
    Arg4 = 0;
    *(uint64_t *)(v_rip + 0x36E4D8) = result;
    Arg3 = 0;
    result = HalpAcpiGetTable(Arg1, (uint32_t)(0x5443534DULL), Arg3, Arg4);
    *(uint64_t *)(v_rip + 0x36E519) = result;
    if (*(uint64_t *)(v_rip + 0x36E4BA) != 0) goto loc_00C22170;
    result = HalpInitializeConfigurationFromMadt(Arg1, (uint32_t)(0x5443534DULL), Arg3, Arg4);
    goto loc_00C22966;
loc_00C22170:
    v_stack_p10 = (uint8_t)(*(uint8_t *)(result + 0x8));
    result = HalpGetNumaProcMemoryCount(v_stack_m50, v_stack_m54, v_stack_m58, v_stack_p20);
    if ((uint8_t)(result) == 0) goto loc_00C22966;
    result = HalpAllocateNumaConfigData((uint32_t)(v_stack_m50), (uint32_t)((uint32_t)((uint32_t)(v_stack_m54))), (uint32_t)((uint32_t)((uint32_t)(v_stack_m58))), (uint32_t)(v_stack_p20));
    if ((*(uint64_t *)(v_rip + 0x36E4A1)) == 0) goto loc_00C22966;
    if ((uint32_t)((uint32_t)(v_stack_m58)) == 0) goto loc_00C221DF;
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m58) + (uint32_t)(v_stack_m58) * 2) << (3));
    result = HalpMmAllocateMemoryInternal(Arg1, (uint32_t)((uint32_t)(local_rsi + 1)), (uint32_t)((uint32_t)((uint32_t)(v_stack_m58))), (uint32_t)(v_stack_p20));
    *(uint64_t *)(v_rip + 0x36E452) = result;
    if (result == 0) goto loc_00C22966;
loc_00C221DF:
    if ((uint32_t)((uint32_t)(v_stack_m54)) == 0) goto loc_00C22251;
    if (((uint32_t)((uint32_t)(v_stack_m54))) < 4) goto loc_00C2222B;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x36E467))) > (*(uint64_t *)(v_rip + 0x36E467))) goto loc_00C22205;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x36E467)) + (uint32_t)(v_stack_m54) - 1 * 4) >= (*(uint64_t *)(v_rip + 0x36E467))) goto loc_00C2222B;
loc_00C22205:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m54)))) & (0xFFFFFFFCULL));
loc_00C2220A:
    local_rdi = (uint32_t)((0) + (4));
    if (((uint32_t)(local_rdi)) < ((uint32_t)(result))) goto loc_00C2220A;
    Arg2 = (uint32_t)((*(uint64_t *)(v_rip + 0x36E467)) | (0xFFFFFFFFULL));
    Arg3 = ((uint32_t)((uint32_t)(result))) >> (2);
    Arg3 = (Arg3) << (4);
    Arg3 = (Arg3) & (-4);
    result = memset(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36E467)), Arg2, Arg3, *(uint64_t *)(*(uint64_t *)(v_rip + 0x36E467)));
loc_00C2222B:
    if (((uint32_t)(local_rdi)) >= ((uint32_t)((uint32_t)(v_stack_m54)))) goto loc_00C22251;
    Arg2 = ((uint32_t)((uint32_t)(local_rdi))) << (2);
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m54)) - ((uint32_t)(local_rdi)));
loc_00C2223A:
    Arg3 = ((uint32_t)((uint32_t)(local_rbx))) - (local_rsi + 1);
    if (condition_is_not_equal) goto loc_00C2223A;
loc_00C22251:
    local_rdi = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x4))) + (*(uint64_t *)(v_rip + 0x36E3C0));
    if ((*(uint64_t *)(v_rip + 0x36E3C0) + 48 + 2) > local_rdi) goto loc_00C22479;
loc_00C22285:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1))) < 2) goto loc_00C22475;
    if ((*(uint64_t *)(v_rip + 0x36E3C0) + 48 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1) > local_rdi) goto loc_00C22475;
    result = HalpVerifySratEntryLengthAndFlag(*(uint64_t *)(v_rip + 0x36E3C0) + 48, v_stack_p18, Arg3, *(uint64_t *)(*(uint64_t *)(v_rip + 0x36E467)));
    if ((uint8_t)(result) != 0) goto loc_00C222B6;
    goto loc_00C22468;
loc_00C222B6:
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x36E35B) + 0x8)) != 1) goto loc_00C222D0;
    goto loc_00C22310;
loc_00C222D0:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1)) != 0) goto loc_00C22302;
    Arg3 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1 + 0xB)) << (8));
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1 + 0xA))));
    Arg3 = (uint32_t)((Arg3) << (8));
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1 + 0x9))));
    Arg3 = (uint32_t)((Arg3) << (8));
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1 + 0x2))));
    goto loc_00C22310;
loc_00C22302:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1 + 0x2))) != 2) goto loc_00C2230C;
    goto loc_00C22310;
loc_00C2230C:
loc_00C22310:
    local_r11 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36E3D7) + 0x38))) == 0) goto loc_00C2232F;
loc_00C2231E:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1 + 0x2)))) == (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36E3D7) + 0x18)))) goto loc_00C2232F;
    local_r11 = (uint32_t)((local_r11) + (1));
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0x36E3D7) + 0x18)) + (4);
    if (((uint32_t)(local_r11)) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36E3D7) + 0x38))))) goto loc_00C2231E;
loc_00C2232F:
    if (((uint32_t)(local_r11)) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36E3D7) + 0x38))))) {
        result = *(uint64_t *)(*(uint64_t *)(v_rip + 0x36E3D7) + 0x18);
        *(uint32_t *)(result + local_r11 * 4) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1 + 0x2)));
        result = *(uint64_t *)(v_rip + 0x36E315);
        Arg1 = *(uint64_t *)(result + 0x20);
        *(uint32_t *)(Arg1 + local_r11 * 4) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1 + 0x2)));
    }
    if ((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1)) == 0) goto loc_00C22367;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1)))) - (1));
    if (condition_is_equal) goto loc_00C22387;
    if (((uint32_t)(Arg1)) != 1) goto loc_00C22460;
loc_00C22367:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1)) != 0) goto loc_00C22400;
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1 + 0x3))) != 255) goto loc_00C22404;
    Arg4 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1 + 0x3)) | (0xFFFFFFFFULL));
    goto loc_00C22404;
loc_00C22387:
    Arg4 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1 + 0x8)) >> (12);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1 + 0x10)) >> (12);
    local_r11 = (Arg4 - 1) + (Arg1);
    if (Arg4 < (*(uint64_t *)(v_rip + 0x1E8483))) {
        *(uint64_t *)(v_rip + 0x1E847A) = Arg4;
    }
    if (local_r11 >= = (*(uint64_t *)(v_rip + 0x36E24B))) {
        *(uint64_t *)(v_rip + 0x36E242) = local_r11;
    }
    Arg1 = (0) + (0);
    local_rbx = (uint32_t)((0) + 1);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x36E243) + Arg1 * 8) = Arg4;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x36E228) + Arg1 * 8 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1 + 0x2)));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x36E238) + 0x0 + 0x0 * 2 * 8 + 0x8) = Arg4;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x36E238) + 0x0 + 0x0 * 2 * 8 + 0x10) = local_r11;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x36E238) + 0x0 + 0x0 * 2 * 8) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1 + 0x2)));
    goto loc_00C22460;
loc_00C22400:
loc_00C22404:
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36E24D)) + 0x0 * 4) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1 + 0x8)));
    local_r15 = (uint32_t)((0) + (1));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36E24D) + 0x10) + 0x0 * 4) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1 + 0x2)));
    if (((uint8_t)(v_stack_p10)) < 3) goto loc_00C22460;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1)) != 0) goto loc_00C22440;
    goto loc_00C22444;
loc_00C22440:
loc_00C22444:
    if (0 != 0) goto loc_00C22451;
    goto loc_00C22460;
loc_00C22451:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1 + 0x10)))))) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1 + 0x10))))) {
        *(uint32_t *)(v_rip + 0x1E83C0) = 2;
    }
    local_r10 = (*(uint64_t *)(v_rip + 0x36E3C0) + 48 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1) + (*(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + *(uint8_t *)(*(uint64_t *)(v_rip + 0x36E3C0) + 0x30 + 0x1) * 1 + 0x1));
loc_00C22468:
    if ((local_r10 + 2) <= local_rdi) goto loc_00C22285;
loc_00C22475:
loc_00C22479:
    *(uint32_t *)(v_rip + 0x36E199) = (uint32_t)(local_rbx);
    *(uint32_t *)(v_rip + 0x36E1B3) = (uint32_t)(local_rbx);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x36E1D8) + 0x3C) = (uint32_t)(local_r15);
    result = qsort(*(uint64_t *)(v_rip + 0x36E160), (uint32_t)((uint32_t)(local_rbx)), 16, v_rip - 7116263);
    result = qsort(*(uint64_t *)(v_rip + 0x36E167), (uint32_t)(*(uint32_t *)(v_rip + 0x36E19D)), 16 + 8, v_rip - 7116362);
    local_r13 = 0;
    if (((uint32_t)(local_rbx)) <= ((uint32_t)(16 - 15))) goto loc_00C22512;
loc_00C224E2:
    if ((*(uint32_t *)(0 + *(uint64_t *)(v_rip + 0x36E11F) * 1 + 0x8)) != ((uint32_t)((uint32_t)(*(uint32_t *)(16 + *(uint64_t *)(v_rip + 0x36E11F) * 1 + 0x8))))) {
        Arg4 = (uint32_t)((0) + ((uint32_t)(16 - 15)));
        Arg1 = Arg4;
        Arg1 = (Arg1) << (4);
        *(uint64_t *)(Arg1 + *(uint64_t *)(v_rip + 0x36E11F) * 1) = v_xmm0;
    }
    Arg2 = (16) + (16);
    local_r10 = (local_rbx - 1) - (16 - 15);
    if (condition_is_not_equal) goto loc_00C224E2;
loc_00C22512:
    Arg1 = ((uint32_t)((uint32_t)(Arg4 + 1))) + ((uint32_t)((uint32_t)(Arg4 + 1)));
    *(uint32_t *)(v_rip + 0x36E108) = (uint32_t)(Arg4 + 1);
    *(uint32_t *)(v_rip + 0x36E132) = (uint32_t)(Arg4 + 1);
    Arg1 = ((uint32_t)((uint32_t)(Arg4 + 1))) + ((uint32_t)((uint32_t)(Arg4 + 1)));
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x36E0CB) + Arg1 * 8 + 0x8) = 0;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x36E0BA)) = 0;
    if ((uint32_t)(Arg4 + 1) == 0) goto loc_00C2259B;
loc_00C2255F:
loc_00C2256D:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36E0FC) + 0x38))))) goto loc_00C22593;
    if ((*(uint32_t *)(0 + *(uint64_t *)(v_rip + 0x36E09B) * 1 + 0x8)) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36E0FC) + 0x18) + 0x0 * 4))))) goto loc_00C22587;
    Arg2 = (uint32_t)((0) + ((uint32_t)(16 - 15)));
    goto loc_00C2256D;
loc_00C22587:
    *(uint32_t *)(0 + *(uint64_t *)(v_rip + 0x36E07A) * 1 + 0x8) = (uint32_t)(Arg2);
loc_00C22593:
    Arg3 = (0) + (16);
    Arg4 = ((uint32_t)((uint32_t)(Arg4 + 1))) - (16 - 15);
    if (condition_is_not_equal) goto loc_00C2255F;
loc_00C2259B:
    result = *(uint64_t *)(v_rip + 0x36E07A);
    if ((*(uint64_t *)(v_rip + 0x36E0CE)) != 0) {
        Arg2 = *(uint64_t *)(v_rip + 0x36E0AD);
        result = *(uint64_t *)(Arg2 + 0x10);
        Arg3 = Arg2 + 60;
        Arg4 = *(uint32_t *)(Arg2 + 0x44);
        Arg1 = Arg2 + 56;
        v_stack_m60 = result;
        result = *(uint64_t *)(Arg2 + 0x28);
        v_stack_m68 = result;
        result = *(uint64_t *)(Arg2 + 0x18);
        Arg2 = *(uint32_t *)(Arg2 + 0x40);
        v_stack_m70 = result;
        result = v_rip + 1999428;
        v_stack_m78 = result;
        result = HalpUpdateConfigurationFromMsct(Arg1, Arg2, Arg3, Arg4);
    }
    Arg4 = 0;
    Arg3 = 0;
    result = HalpAcpiGetTable(v_stack_p8, (uint32_t)(0x54494C53ULL), Arg3, Arg4);
    if (result == 0) goto loc_00C226AB;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x24))))) * ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x24)))));
    Arg1 = (uint32_t)((Arg1) + (44));
    if (((uint32_t)(Arg1)) > (*(uint32_t *)(result + 0x4))) goto loc_00C226B2;
loc_00C22626:
    if (0 >= (*(uint32_t *)(*(uint64_t *)(v_rip + 0x36E035) + 0x38))) goto loc_00C226AB;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36E035) + 0x18) + 0x0 * 4)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x24))))) goto loc_00C226B2;
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36E035) + 0x18) + 0x0 * 4))) * ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x24)))));
loc_00C22642:
    if (0 >= (*(uint32_t *)(*(uint64_t *)(v_rip + 0x36E035) + 0x38))) goto loc_00C22684;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36E035) + 0x18) + 0x0 * 4)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x24))))) goto loc_00C226B2;
    if (((uint8_t)(*(uint8_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36E035) + 0x18) + 0x0 * 4)) + local_rdi * 1 + result * 1 + 0x2C))) < 10) goto loc_00C226B2;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36E035) + 0x18) + 0x0 * 4)) + local_rdi * 1 + result * 1 + 0x2C)))) * (128));
    Arg1 = (uint32_t)((0) * (*(uint32_t *)(*(uint64_t *)(v_rip + 0x36E035) + 0x40)));
    Arg1 = (uint32_t)((Arg1) + (0));
    local_rbx = (uint32_t)((0) + ((uint32_t)(16 - 15)));
    *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36E035) + 0x30) + Arg1 * 2) = (uint16_t)(Arg2);
    goto loc_00C22642;
loc_00C22684:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36E035) + 0x40))) + ((uint32_t)(16 - 15)));
    Arg1 = (uint32_t)((Arg1) * (0));
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36E035) + 0x30) + Arg1 * 2)) != ((uint16_t)((uint32_t)(0x500ULL)))) goto loc_00C226B2;
    *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36E035) + 0x30) + Arg1 * 2) = 0;
    Arg4 = (uint32_t)((0) + ((uint32_t)(16 - 15)));
    goto loc_00C22626;
loc_00C226AB:
    *(uint64_t *)(v_rip + 0x36DFB6) = result;
loc_00C226B2:
    if ((*(uint64_t *)(v_rip + 0x36DFAF)) != 0) goto loc_00C22816;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0xF0) + 0x128) == 0) goto loc_00C227C4;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0xF0) + 0x128))))) != (*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DF77) + 0x38))) goto loc_00C227C4;
loc_00C226FE:
    if (0 >= (*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DF77) + 0x38))) goto loc_00C22816;
loc_00C22710:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0xF0) + 0x128)))))) goto loc_00C22732;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0xF0) + 0x128) + 0x4 + 0x0 * 4)) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36DF77) + 0x18) + 0x0 * 4))))) goto loc_00C22729;
    Arg3 = (uint32_t)((0) + 1);
    goto loc_00C22710;
loc_00C22729:
    local_rbx = (uint32_t)(((uint32_t)(Arg3)) * ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0xF0) + 0x128))))));
    goto loc_00C22738;
loc_00C22732:
    if (condition_is_equal) goto loc_00C227BE;
loc_00C22738:
loc_00C22741:
    if (0 >= (*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DF77) + 0x38))) goto loc_00C2279C;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0xF0) + 0x128)))) == 0) goto loc_00C2276C;
loc_00C2275D:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0xF0) + 0x128) + 0x4)) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36DF77) + 0x18) + 0x0 * 4))))) goto loc_00C2276C;
    Arg1 = (uint32_t)((0) + 1);
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0xF0) + 0x128) + 4) + (4);
    if (((uint32_t)(Arg1)) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0xF0) + 0x128)))))) goto loc_00C2275D;
loc_00C2276C:
    if (((uint32_t)(Arg1)) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0xF0) + 0x128)))))) goto loc_00C227BE;
    Arg2 = (uint32_t)((0) * (*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DEDB) + 0x40)));
    Arg2 = (uint32_t)((Arg2) + (0));
    local_r11 = (uint32_t)((0) + (1));
    *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36DEDB) + 0x30) + Arg2 * 2) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0xF0) + 0x128) + 0x4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0xF0) + 0x128))) * 4 + local_rbx + Arg1 * 1 * 2));
    goto loc_00C22741;
loc_00C2279C:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DEB5) + 0x40))) + (1));
    Arg1 = (uint32_t)((Arg1) * (0));
    local_r10 = (uint32_t)((0) + (1));
    *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36DEB5) + 0x30) + Arg1 * 2) = 0;
    goto loc_00C226FE;
loc_00C227BE:
loc_00C227C4:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DE8D) + 0x38))) == 0) goto loc_00C22816;
loc_00C227D5:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DE8D) + 0x38))) == 0) goto loc_00C227F8;
loc_00C227DC:
    Arg1 = (uint32_t)((0) * (*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DE8D) + 0x40)));
    Arg1 = (uint32_t)((Arg1) + (0));
    Arg4 = (uint32_t)((0) + (1));
    *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36DE8D) + 0x30) + Arg1 * 2) = 1;
    if (Arg4 < (*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DE8D) + 0x38))) goto loc_00C227DC;
loc_00C227F8:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DE8D) + 0x40))) + (1));
    Arg1 = (uint32_t)((Arg1) * (0));
    Arg3 = (uint32_t)((0) + (1));
    *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36DE8D) + 0x30) + Arg1 * 2) = 0;
    if (Arg3 < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DE8D) + 0x38))))) goto loc_00C227D5;
loc_00C22816:
    if ((*(uint8_t *)(v_rip + 0x1EDC45)) == 0) goto loc_00C2294E;
    v_stack_p10 = *(uint64_t *)(v_rip + 0x36DE2E);
    result = HalpNumaSortProcessors((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DE2E) + 0x3C)), *(uint64_t *)(*(uint64_t *)(v_rip + 0x36DE2E) + 0x10), *(uint64_t *)(*(uint64_t *)(v_rip + 0x36DE2E)), Arg4);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DE2E) + 0x38))) == 0) goto loc_00C2294E;
loc_00C2284B:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36DE2E) + 0x28) + 0x0 * 4)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x1E7FC6))))) goto loc_00C22941;
    result = HalpGetAvailableProximityId((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DE2E) + 0x3C)), *(uint64_t *)(*(uint64_t *)(v_rip + 0x36DE2E) + 0x10), *(uint64_t *)(*(uint64_t *)(v_rip + 0x36DE2E)), Arg4);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x36DE2E) + 0x38) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DE2E) + 0x38)) + 1);
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36DE2E) + 0x28) + 0x0 * 4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x1E7FC6)));
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36DE2E) + 0x28) + 0x0 * 4))) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x1E7FC6)))));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36DE2E) + 0x28) + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DE2E) + 0x38)))) * 4) = Arg4;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36DDE9) + 0x18) + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DE2E) + 0x38)))) * 4) = (uint32_t)((uint32_t)((uint32_t)(result)));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36DDE9) + 0x20) + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DE2E) + 0x38)))) * 4) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36DDE9) + 0x20) + 0x0 * 4)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DE2E) + 0x38))) == 0) goto loc_00C228F5;
loc_00C228B0:
    Arg1 = (uint32_t)((0) * (*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DDE9) + 0x40)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DE2E) + 0x38)))));
    *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36DDE9) + 0x30) + Arg1 * 2) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36DDE9) + 0x30) + Arg1 + 0x0 * 1 * 2));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DDE9) + 0x40))))) * (0));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DDE9) + 0x40))) * ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DE2E) + 0x38)))));
    result = (uint32_t)((result) + (0));
    Arg1 = (uint32_t)((Arg1) + (0));
    local_r11 = (uint32_t)((0) + (1));
    *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36DDE9) + 0x30) + Arg1 * 2) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36DDE9) + 0x30) + result * 2));
    if (((uint32_t)(local_r11)) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DE2E) + 0x38))))) goto loc_00C228B0;
loc_00C228F5:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DD5C) + 0x40))) + (1));
    Arg1 = (uint32_t)((Arg1) * ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x36DE2E) + 0x38)))));
    *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36DD5C) + 0x30) + Arg1 * 2) = 0;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x3C))) - (1));
    if (condition_is_equal) goto loc_00C22941;
loc_00C2291F:
    if (Arg4 == 0) goto loc_00C22941;
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x10) + Arg2 * 4)) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36DD5C) + 0x18) + 0x0 * 4))))) {
        Arg4 = (uint32_t)((Arg4) - 1);
        *(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x10) + Arg2 * 4) = (uint32_t)((uint32_t)((uint32_t)(result)));
    }
    Arg2 = (uint32_t)((Arg2) + (-1));
    if (condition_is_not_equal) goto loc_00C2291F;
loc_00C22941:
    local_rsi = (uint32_t)((0) + 1);
    if (((uint32_t)(local_rsi)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x38))))) goto loc_00C2284B;
loc_00C2294E:
    if ((*(uint32_t *)(v_rip + 0x1E7EC7)) != 1) {
        *(uint8_t *)(v_rip + 0x3A16EF) = 1;
    }
    result = HalpChannelInitializeStaticConfiguration((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x36DD5C) + 0x18) + 0x0 * 4)), Arg2, *(uint64_t *)(v_rip + 0x36DD5C), Arg4);
loc_00C22966:
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C220D8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
