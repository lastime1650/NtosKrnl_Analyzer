# MiLockDriverPageRange

- RVA: `0x00670160`–`0x006706AD` (길이 `1,357` bytes)
- VA: `0x0000000140670160`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D7754`
- 디코드: `342`개 명령, `1,357/1,357` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **28**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00670191` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00670253` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x00670289` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x006702B8` → [MiLockNestedPageTable](../23/MiLockNestedPageTable_function_0023E890.md) (function, `0x0023E890`)
- `0x006703A0` → [KeYieldProcessorEx](../3F/KeYieldProcessorEx_function_003FBD00.md) (function, `0x003FBD00`)
- `0x006703B3` → [MiReferenceDriverPage](../37/MiReferenceDriverPage_function_003701B4.md) (function, `0x003701B4`)
- `0x006703E5` → [KeSetPagePrivilege](../40/KeSetPagePrivilege_function_00407970.md) (function, `0x00407970`)
- `0x00670416` → [MiCaptureDirtyBitToPfn](../37/MiCaptureDirtyBitToPfn_function_00370DD0.md) (function, `0x00370DD0`)
- `0x00670467` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x006704B2` → [MiCopyOnWrite](../36/MiCopyOnWrite_function_00362A0C.md) (function, `0x00362A0C`)
- `0x006704CC` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x006704DB` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x006704E8` → [MiCopyOnWriteCheckConditions](../2A/MiCopyOnWriteCheckConditions_function_002A750C.md) (function, `0x002A750C`)
- `0x006704F0` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x006704FB` → [MiLockNestedPageTable](../23/MiLockNestedPageTable_function_0023E890.md) (function, `0x0023E890`)
- `0x0067050B` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x0067051A` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x00670540` → [MiMakeDriverPagesPrivate](../38/MiMakeDriverPagesPrivate_function_00384C60.md) (function, `0x00384C60`)
- `0x00670548` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x00670553` → [MiLockNestedPageTable](../23/MiLockNestedPageTable_function_0023E890.md) (function, `0x0023E890`)
- `0x00670567` → [MiMakeDemandZeroPte](../33/MiMakeDemandZeroPte_function_00337A00.md) (function, `0x00337A00`)
- `0x00670577` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00670586` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x006705BC` → [MmAccessFault](../27/MmAccessFault_function_0027EE80.md) (function, `0x0027EE80`)
- `0x006705CC` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x006705D7` → [MiLockNestedPageTable](../23/MiLockNestedPageTable_function_0023E890.md) (function, `0x0023E890`)
- `0x00670682` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00670691` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)

### Direct callers
- [MiLockPatchIatForDV](../68/MiLockPatchIatForDV_function_00682050.md) at `0x006821BB`
- [MmWriteSystemImageTracepoint](../68/MmWriteSystemImageTracepoint_function_00684150.md) at `0x006842D5`
- [MiLockAndMapEntireDriver](../../page/80/MiLockAndMapEntireDriver_function_008015C8.md) at `0x008016D4`
- [MiLockHotPatchPages](../../page/80/MiLockHotPatchPages_function_00804620.md) at `0x00804689`
- [MiPrepareDriverForHotPatch](../../page/80/MiPrepareDriverForHotPatch_function_008066F4.md) at `0x008067F9`
- [MmReapplyBootPatchImports](../../init/C6/MmReapplyBootPatchImports_function_00C67768.md) at `0x00C67860`
- [MmReapplyBootPatchImports](../../init/C6/MmReapplyBootPatchImports_function_00C67768.md) at `0x00C67880`

### Static image references
- `0x0067021B` → RVA `0x00E2D940` (`.data`; read)
- `0x0067022F` → RVA `0x00E2D948` (`.data`; read)
- `0x00670427` → RVA `0x00E30088` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00670160  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
00670165  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
0067016A  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
0067016E  53                              push rbx
0067016F  55                              push rbp
00670170  56                              push rsi
00670171  57                              push rdi
00670172  41 54                           push r12
00670174  41 55                           push r13
00670176  41 56                           push r14
00670178  41 57                           push r15
0067017A  48 81 EC E8 00 00 00            sub rsp, 0xe8
00670181  8B FA                           mov edi, edx
00670183  4C 8B E1                        mov r12, rcx
00670186  33 D2                           xor edx, edx
00670188  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
0067018D  44 8D 42 78                     lea r8d, [rdx + 0x78]
00670191  E8 AA 6A 05 00                  call 0x1406c6c40
00670196  4D 8B 14 24                     mov r10, qword ptr [r12]
0067019A  8B CF                           mov ecx, edi
0067019C  48 C1 E1 0C                     shl rcx, 0xc
006701A0  33 DB                           xor ebx, ebx
006701A2  48 BA F8 FF FF FF 7F 00 00 00   movabs rdx, 0x7ffffffff8
006701AC  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
006701B1  49 03 4A 30                     add rcx, qword ptr [r10 + 0x30]
006701B5  4C 8B E9                        mov r13, rcx
006701B8  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
006701BD  49 C1 ED 09                     shr r13, 9
006701C1  4C 23 EA                        and r13, rdx
006701C4  48 B9 00 00 00 00 80 F6 FF FF   movabs rcx, 0xfffff68000000000
006701CE  48 8B C1                        mov rax, rcx
006701D1  4C 03 E8                        add r13, rax
006701D4  41 8B 44 24 60                  mov eax, dword ptr [r12 + 0x60]
006701D9  4D 8B F5                        mov r14, r13
006701DC  A8 02                           test al, 2
006701DE  74 0D                           je 0x1406701ed
006701E0  49 C1 EE 09                     shr r14, 9
006701E4  4C 23 F2                        and r14, rdx
006701E7  48 8B C1                        mov rax, rcx
006701EA  4C 03 F0                        add r14, rax
006701ED  48 8B 8C 24 50 01 00 00         mov rcx, qword ptr [rsp + 0x150]
006701F5  48 8B F3                        mov rsi, rbx
006701F8  48 8B C1                        mov rax, rcx
006701FB  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
00670200  48 83 C1 30                     add rcx, 0x30
00670204  48 F7 D8                        neg rax
00670207  48 1B C0                        sbb rax, rax
0067020A  48 23 C1                        and rax, rcx
0067020D  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00670212  8B C3                           mov eax, ebx
00670214  83 F8 01                        cmp eax, 1
00670217  73 29                           jae 0x140670242
00670219  8B C8                           mov ecx, eax
0067021B  48 8D 15 1E D7 7B 00            lea rdx, [rip + 0x7bd71e]
00670222  4C 39 14 CA                     cmp qword ptr [rdx + rcx*8], r10
00670226  74 04                           je 0x14067022c
00670228  FF C0                           inc eax
0067022A  EB E8                           jmp 0x140670214
0067022C  48 8B F1                        mov rsi, rcx
0067022F  48 8D 05 12 D7 7B 00            lea rax, [rip + 0x7bd712]
00670236  48 C1 E6 04                     shl rsi, 4
0067023A  48 03 F0                        add rsi, rax
0067023D  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
00670242  49 8B 6C 24 10                  mov rbp, qword ptr [r12 + 0x10]
00670247  8B 85 B8 00 00 00               mov eax, dword ptr [rbp + 0xb8]
0067024D  48 8B CD                        mov rcx, rbp
00670250  4C 8B FB                        mov r15, rbx
00670253  E8 98 C9 C0 FF                  call 0x14027cbf0
00670258  88 84 24 30 01 00 00            mov byte ptr [rsp + 0x130], al
0067025F  EB 07                           jmp 0x140670268
00670261  8B BC 24 38 01 00 00            mov edi, dword ptr [rsp + 0x138]
00670268  3B BC 24 40 01 00 00            cmp edi, dword ptr [rsp + 0x140]
0067026F  0F 87 F5 03 00 00               ja 0x14067066a
00670275  4D 85 FF                        test r15, r15
00670278  74 14                           je 0x14067028e
0067027A  49 F7 C5 FF 0F 00 00            test r13, 0xfff
00670281  75 3A                           jne 0x1406702bd
00670283  49 8B D7                        mov rdx, r15
00670286  48 8B CD                        mov rcx, rbp
00670289  E8 32 6C BA FF                  call 0x140216ec0
0067028E  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00670298  4D 8B FE                        mov r15, r14
0067029B  49 C1 EF 09                     shr r15, 9
0067029F  4C 23 F8                        and r15, rax
006702A2  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
006702AC  48 8B C0                        mov rax, rax
006702AF  4C 03 F8                        add r15, rax
006702B2  48 8B CD                        mov rcx, rbp
006702B5  49 8B D7                        mov rdx, r15
006702B8  E8 D3 E5 BC FF                  call 0x14023e890
006702BD  48 85 F6                        test rsi, rsi
006702C0  74 27                           je 0x1406702e9
006702C2  48 8B 06                        mov rax, qword ptr [rsi]
006702C5  8B D7                           mov edx, edi
006702C7  48 3B D0                        cmp rdx, rax
006702CA  73 1D                           jae 0x1406702e9
006702CC  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
006702D0  8B CA                           mov ecx, edx
006702D2  48 C1 EA 06                     shr rdx, 6
006702D6  83 E1 3F                        and ecx, 0x3f
006702D9  48 0F A3 0C D0                  bt qword ptr [rax + rdx*8], rcx
006702DE  0F 92 C0                        setb al
006702E1  84 C0                           test al, al
006702E3  0F 85 F3 02 00 00               jne 0x1406705dc
006702E9  49 39 5C 24 38                  cmp qword ptr [r12 + 0x38], rbx
006702EE  74 2A                           je 0x14067031a
006702F0  49 8B 44 24 30                  mov rax, qword ptr [r12 + 0x30]
006702F5  8B D7                           mov edx, edi
006702F7  48 3B D0                        cmp rdx, rax
006702FA  73 1E                           jae 0x14067031a
006702FC  49 8B 44 24 38                  mov rax, qword ptr [r12 + 0x38]
00670301  8B CA                           mov ecx, edx
00670303  48 C1 EA 06                     shr rdx, 6
00670307  83 E1 3F                        and ecx, 0x3f
0067030A  48 0F A3 0C D0                  bt qword ptr [rax + rdx*8], rcx
0067030F  0F 92 C0                        setb al
00670312  84 C0                           test al, al
00670314  0F 85 07 03 00 00               jne 0x140670621
0067031A  49 8B 36                        mov rsi, qword ptr [r14]
0067031D  40 F6 C6 01                     test sil, 1
00670321  0F 84 3B 02 00 00               je 0x140670562
00670327  48 C1 EE 0C                     shr rsi, 0xc
0067032B  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
00670335  48 23 F0                        and rsi, rax
00670338  41 8B 44 24 60                  mov eax, dword ptr [r12 + 0x60]
0067033D  A8 02                           test al, 2
0067033F  74 0F                           je 0x140670350
00670341  49 8B C5                        mov rax, r13
00670344  48 C1 E8 03                     shr rax, 3
00670348  25 FF 01 00 00                  and eax, 0x1ff
0067034D  48 03 F0                        add rsi, rax
00670350  48 8D 3C 76                     lea rdi, [rsi + rsi*2]
00670354  48 C1 E7 04                     shl rdi, 4
00670358  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00670362  48 03 F8                        add rdi, rax
00670365  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
00670369  48 85 C0                        test rax, rax
0067036C  0F 88 0F 01 00 00               js 0x140670481
00670372  49 8B 44 24 28                  mov rax, qword ptr [r12 + 0x28]
00670377  44 8B 9C 24 38 01 00 00         mov r11d, dword ptr [rsp + 0x138]
0067037F  4C 0F A3 18                     bt qword ptr [rax], r11
00670383  0F 92 C0                        setb al
00670386  84 C0                           test al, al
00670388  0F 85 8C 02 00 00               jne 0x14067061a
0067038E  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00670392  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
00670399  73 15                           jae 0x1406703b0
0067039B  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
006703A0  E8 5B B9 D8 FF                  call 0x1403fbd00
006703A5  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
006703A9  48 85 C0                        test rax, rax
006703AC  78 ED                           js 0x14067039b
006703AE  EB E2                           jmp 0x140670392
006703B0  48 8B CF                        mov rcx, rdi
006703B3  E8 FC FD CF FF                  call 0x1403701b4
006703B8  44 8B 84 24 48 01 00 00         mov r8d, dword ptr [rsp + 0x148]
006703C0  41 F6 C0 01                     test r8b, 1
006703C4  74 32                           je 0x1406703f8
006703C6  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
006703CA  48 C1 E8 3C                     shr rax, 0x3c
006703CE  24 07                           and al, 7
006703D0  3C 03                           cmp al, 3
006703D2  74 24                           je 0x1406703f8
006703D4  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
006703D9  41 B9 80 00 00 00               mov r9d, 0x80
006703DF  45 33 C0                        xor r8d, r8d
006703E2  48 8B CE                        mov rcx, rsi
006703E5  E8 86 75 D9 FF                  call 0x140407970
006703EA  41 83 4C 24 60 01               or dword ptr [r12 + 0x60], 1
006703F0  44 8B 84 24 48 01 00 00         mov r8d, dword ptr [rsp + 0x148]
006703F8  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
006703FD  48 85 D2                        test rdx, rdx
00670400  74 0B                           je 0x14067040d
00670402  8B 8C 24 38 01 00 00            mov ecx, dword ptr [rsp + 0x138]
00670409  48 89 34 CA                     mov qword ptr [rdx + rcx*8], rsi
0067040D  41 F6 C0 04                     test r8b, 4
00670411  75 2F                           jne 0x140670442
00670413  48 8B CF                        mov rcx, rdi
00670416  E8 B5 09 D0 FF                  call 0x140370dd0
0067041B  48 8B D0                        mov rdx, rax
0067041E  48 85 C0                        test rax, rax
00670421  74 22                           je 0x140670445
00670423  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
00670427  48 8B 0D 5A FC 7B 00            mov rcx, qword ptr [rip + 0x7bfc5a]
0067042E  48 C1 E8 2B                     shr rax, 0x2b
00670432  25 FF 03 00 00                  and eax, 0x3ff
00670437  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
0067043B  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00670440  EB 08                           jmp 0x14067044a
00670442  48 8B D3                        mov rdx, rbx
00670445  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0067044A  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
00670454  F0 48 21 4F 18                  lock and qword ptr [rdi + 0x18], rcx
00670459  48 85 D2                        test rdx, rdx
0067045C  74 0E                           je 0x14067046c
0067045E  41 B8 01 00 00 00               mov r8d, 1
00670464  48 8B C8                        mov rcx, rax
00670467  E8 64 3B C1 FF                  call 0x140283fd0
0067046C  49 8B 44 24 28                  mov rax, qword ptr [r12 + 0x28]
00670471  8B BC 24 38 01 00 00            mov edi, dword ptr [rsp + 0x138]
00670478  48 0F AB 38                     bts qword ptr [rax], rdi
0067047C  E9 A0 01 00 00                  jmp 0x140670621
00670481  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
00670485  48 0F BA E0 28                  bt rax, 0x28
0067048A  72 79                           jb 0x140670505
0067048C  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00670490  48 85 C0                        test rax, rax
00670493  78 70                           js 0x140670505
00670495  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00670499  48 85 C0                        test rax, rax
0067049C  74 67                           je 0x140670505
0067049E  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
006704A3  45 33 C9                        xor r9d, r9d
006704A6  49 83 C8 FF                     or r8, 0xffffffffffffffff
006704AA  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
006704AF  49 8B D6                        mov rdx, r14
006704B2  E8 55 25 CF FF                  call 0x140362a0c
006704B7  48 8B 74 24 30                  mov rsi, qword ptr [rsp + 0x30]
006704BC  8B F8                           mov edi, eax
006704BE  85 C0                           test eax, eax
006704C0  0F 89 9B FD FF FF               jns 0x140670261
006704C6  49 8B D7                        mov rdx, r15
006704C9  48 8B CD                        mov rcx, rbp
006704CC  E8 EF 69 BA FF                  call 0x140216ec0
006704D1  8A 94 24 30 01 00 00            mov dl, byte ptr [rsp + 0x130]
006704D8  48 8B CD                        mov rcx, rbp
006704DB  E8 B0 D1 C0 FF                  call 0x14027d690
006704E0  45 33 C0                        xor r8d, r8d
006704E3  8B D7                           mov edx, edi
006704E5  48 8B CD                        mov rcx, rbp
006704E8  E8 1F 70 C3 FF                  call 0x1402a750c
006704ED  48 8B CD                        mov rcx, rbp
006704F0  E8 FB C6 C0 FF                  call 0x14027cbf0
006704F5  49 8B D7                        mov rdx, r15
006704F8  48 8B CD                        mov rcx, rbp
006704FB  E8 90 E3 BC FF                  call 0x14023e890
00670500  E9 5C FD FF FF                  jmp 0x140670261
00670505  49 8B D7                        mov rdx, r15
00670508  48 8B CD                        mov rcx, rbp
0067050B  E8 B0 69 BA FF                  call 0x140216ec0
00670510  8A 94 24 30 01 00 00            mov dl, byte ptr [rsp + 0x130]
00670517  48 8B CD                        mov rcx, rbp
0067051A  E8 71 D1 C0 FF                  call 0x14027d690
0067051F  8B 84 24 40 01 00 00            mov eax, dword ptr [rsp + 0x140]
00670526  41 B9 08 00 00 00               mov r9d, 8
0067052C  8B BC 24 38 01 00 00            mov edi, dword ptr [rsp + 0x138]
00670533  49 8B D6                        mov rdx, r14
00670536  49 8B 0C 24                     mov rcx, qword ptr [r12]
0067053A  2B C7                           sub eax, edi
0067053C  4D 8D 04 C6                     lea r8, [r14 + rax*8]
00670540  E8 1B 47 D1 FF                  call 0x140384c60
00670545  48 8B CD                        mov rcx, rbp
00670548  E8 A3 C6 C0 FF                  call 0x14027cbf0
0067054D  49 8B D7                        mov rdx, r15
00670550  48 8B CD                        mov rcx, rbp
00670553  E8 38 E3 BC FF                  call 0x14023e890
00670558  48 8B 74 24 30                  mov rsi, qword ptr [rsp + 0x30]
0067055D  E9 06 FD FF FF                  jmp 0x140670268
00670562  B9 10 00 00 00                  mov ecx, 0x10
00670567  E8 94 74 CC FF                  call 0x140337a00
0067056C  48 3B F0                        cmp rsi, rax
0067056F  74 6B                           je 0x1406705dc
00670571  49 8B D7                        mov rdx, r15
00670574  48 8B CD                        mov rcx, rbp
00670577  E8 44 69 BA FF                  call 0x140216ec0
0067057C  8A 94 24 30 01 00 00            mov dl, byte ptr [rsp + 0x130]
00670583  48 8B CD                        mov rcx, rbp
00670586  E8 05 D1 C0 FF                  call 0x14027d690
0067058B  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
00670590  4C 8D 4C 24 60                  lea r9, [rsp + 0x60]
00670595  49 83 C9 01                     or r9, 1
00670599  66 C7 44 24 60 06 00            mov word ptr [rsp + 0x60], 6
006705A0  45 33 C0                        xor r8d, r8d
006705A3  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
006705A8  33 C9                           xor ecx, ecx
006705AA  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
006705AF  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
006705B4  48 89 9C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rbx
006705BC  E8 BF E8 C0 FF                  call 0x14027ee80
006705C1  85 C0                           test eax, eax
006705C3  0F 89 97 00 00 00               jns 0x140670660
006705C9  48 8B CD                        mov rcx, rbp
006705CC  E8 1F C6 C0 FF                  call 0x14027cbf0
006705D1  49 8B D7                        mov rdx, r15
006705D4  48 8B CD                        mov rcx, rbp
006705D7  E8 B4 E2 BC FF                  call 0x14023e890
006705DC  F6 84 24 48 01 00 00 02         test byte ptr [rsp + 0x148], 2
006705E4  75 3B                           jne 0x140670621
006705E6  49 39 5C 24 58                  cmp qword ptr [r12 + 0x58], rbx
006705EB  74 26                           je 0x140670613
006705ED  49 8B 44 24 50                  mov rax, qword ptr [r12 + 0x50]
006705F2  8B D7                           mov edx, edi
006705F4  48 3B D0                        cmp rdx, rax
006705F7  73 1A                           jae 0x140670613
006705F9  49 8B 44 24 58                  mov rax, qword ptr [r12 + 0x58]
006705FE  8B CA                           mov ecx, edx
00670600  48 C1 EA 06                     shr rdx, 6
00670604  83 E1 3F                        and ecx, 0x3f
00670607  48 0F A3 0C D0                  bt qword ptr [rax + rdx*8], rcx
0067060C  0F 92 C0                        setb al
0067060F  84 C0                           test al, al
00670611  75 0E                           jne 0x140670621
00670613  BB 7B 00 00 C0                  mov ebx, 0xc000007b
00670618  EB 62                           jmp 0x14067067c
0067061A  8B BC 24 38 01 00 00            mov edi, dword ptr [rsp + 0x138]
00670621  48 81 44 24 38 00 10 00 00      add qword ptr [rsp + 0x38], 0x1000
0067062A  FF C7                           inc edi
0067062C  48 8B 74 24 30                  mov rsi, qword ptr [rsp + 0x30]
00670631  49 83 C5 08                     add r13, 8
00670635  49 F7 C5 FF 0F 00 00            test r13, 0xfff
0067063C  89 BC 24 38 01 00 00            mov dword ptr [rsp + 0x138], edi
00670643  0F 95 C1                        setne cl
00670646  41 F6 44 24 60 02               test byte ptr [r12 + 0x60], 2
0067064C  0F 95 C0                        setne al
0067064F  84 C8                           test al, cl
00670651  0F 85 11 FC FF FF               jne 0x140670268
00670657  49 83 C6 08                     add r14, 8
0067065B  E9 08 FC FF FF                  jmp 0x140670268
00670660  48 8B 74 24 30                  mov rsi, qword ptr [rsp + 0x30]
00670665  E9 E3 FB FF FF                  jmp 0x14067024d
0067066A  48 8B 84 24 50 01 00 00         mov rax, qword ptr [rsp + 0x150]
00670672  48 85 C0                        test rax, rax
00670675  74 05                           je 0x14067067c
00670677  66 83 48 0A 02                  or word ptr [rax + 0xa], 2
0067067C  49 8B D7                        mov rdx, r15
0067067F  48 8B CD                        mov rcx, rbp
00670682  E8 39 68 BA FF                  call 0x140216ec0
00670687  8A 94 24 30 01 00 00            mov dl, byte ptr [rsp + 0x130]
0067068E  48 8B CD                        mov rcx, rbp
00670691  E8 FA CF C0 FF                  call 0x14027d690
00670696  8B C3                           mov eax, ebx
00670698  48 81 C4 E8 00 00 00            add rsp, 0xe8
0067069F  41 5F                           pop r15
006706A1  41 5E                           pop r14
006706A3  41 5D                           pop r13
006706A5  41 5C                           pop r12
006706A7  5F                              pop rdi
006706A8  5E                              pop rsi
006706A9  5D                              pop rbp
006706AA  5B                              pop rbx
006706AB  C3                              ret
006706AC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiLockDriverPageRange(__int64 a1, int a2, int a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (232);
    a2 = 0;
    result = memset(v_stack_mC8, a2, a2 + 120, a4);
    a1 = ((unsigned int)((unsigned int)((unsigned int)(a2)))) << (12);
    v_rbx = 0;
    v_stack_mE0 = 0;
    a1 = (a1) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 48));
    v_stack_mF0 = a1;
    v_r13 = (a1) >> (9);
    v_r13 = (v_r13) & (0);
    v_r13 = (v_r13) + (a1);
    result = (unsigned int)(*(unsigned int *)(a1 + 96));
    v_r14 = v_r13;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 96)))) & (2)) != 0) {
        v_r14 = (v_r13) >> (9);
        v_r14 = (v_r14) & (0);
        result = a1;
        v_r14 = (v_r14) + (result);
    }
    v_stack_mF8 = 0;
    a1 = (a5) + (48);
    result = -(a5);
    result = (result) & (a1);
    v_stack_mD8 = result;
loc_00670214:
    if (0 >= 1) goto loc_00670242;
    if ((*(unsigned __int64 *)(v_rip + 8115998 + 0 * 8)) == (*(unsigned __int64 *)(a1))) goto loc_0067022C;
    result = (unsigned int)((0) + 1);
    goto loc_00670214;
loc_0067022C:
    v_rsi = (0) << (4);
    v_rsi = (v_rsi) + (v_rip + 8115986);
    v_stack_mF8 = v_rsi;
loc_00670242:
loc_0067024D:
    result = MiLockWorkingSetShared(*(unsigned __int64 *)(a1 + 16), v_rip + 8115998, a2 + 120, a4);
    v_stack_p8 = (unsigned __int8)(result);
    goto loc_00670268;
loc_00670261:
loc_00670268:
    if (((unsigned int)((unsigned int)(v_stack_p10))) > v_stack_p18) goto loc_0067066A;
    if (0 == 0) goto loc_0067028E;
    if (((v_r13) & (0xFFFULL)) != 0) goto loc_006702BD;
    result = MiUnlockPageTable(*(unsigned __int64 *)(a1 + 16), 0, a2 + 120, a4);
loc_0067028E:
    v_r15 = (v_r14) >> (9);
    v_r15 = (v_r15) & (result);
    v_r15 = (v_r15) + (result);
    result = MiLockNestedPageTable(*(unsigned __int64 *)(a1 + 16), v_r15, a2 + 120, a4);
loc_006702BD:
    if (v_rsi == 0) goto loc_006702E9;
    if (((unsigned int)((unsigned int)((unsigned int)(v_stack_p10)))) >= (*(unsigned __int64 *)(v_rsi))) goto loc_006702E9;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_p10)))) >> (6);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p10)))))) & (63));
    result = (condition_is_below) ? 1 : 0;
    if ((unsigned __int8)(result) != 0) goto loc_006705DC;
loc_006702E9:
    if ((*(unsigned __int64 *)(a1 + 56)) == 0) goto loc_0067031A;
    if (((unsigned int)((unsigned int)((unsigned int)(v_stack_p10)))) >= (*(unsigned __int64 *)(a1 + 48))) goto loc_0067031A;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_p10)))) >> (6);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p10)))))) & (63));
    result = (condition_is_below) ? 1 : 0;
    if ((unsigned __int8)(result) != 0) goto loc_00670621;
loc_0067031A:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r14))) & (1)) == 0) goto loc_00670562;
    v_rsi = (*(unsigned __int64 *)(v_r14)) >> (12);
    v_rsi = (v_rsi) & (result);
    result = (unsigned int)(*(unsigned int *)(a1 + 96));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 96)))) & (2)) != 0) {
        result = v_r13;
        result = (result) >> (3);
        result = (unsigned int)((result) & (511));
        v_rsi = (v_rsi) + (result);
    }
    v_rdi = (v_rsi + v_rsi * 2) << (4);
    v_rdi = (v_rdi) + (result);
    if (sign_flag) goto loc_00670481;
    result = (condition_is_below) ? 1 : 0;
    if ((unsigned __int8)(result) != 0) goto loc_0067061A;
    v_stack_mE8 = 0;
loc_00670392:
    if (condition_is_above_or_equal) goto loc_006703B0;
loc_0067039B:
    result = KeYieldProcessorEx(v_stack_mE8, a2, a2 + 120, a4);
    if (sign_flag) goto loc_0067039B;
    goto loc_00670392;
loc_006703B0:
    result = MiReferenceDriverPage(v_rdi, a2, a2 + 120, a4);
    if ((((unsigned __int8)((unsigned int)(v_stack_p20))) & (1)) == 0) goto loc_006703F8;
    result = (*(unsigned __int64 *)(v_rdi + 40)) >> (60);
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) != 3) {
        a2 = v_stack_mF0;
        a4 = 128;
        a3 = 0;
        a1 = v_rsi;
        result = KeSetPagePrivilege(a1, a2, a3, a4);
        a3 = v_stack_p20;
    }
    if (v_stack_mD8 != 0) {
        a1 = v_stack_p10;
        *(unsigned __int64 *)(v_stack_mD8 + a1 * 8) = v_rsi;
    }
    if ((((unsigned __int8)(a3)) & (4)) != 0) goto loc_00670442;
    result = MiCaptureDirtyBitToPfn(v_rdi, v_stack_mD8, a3, a4);
    if (result == 0) goto loc_00670445;
    result = (*(unsigned __int64 *)(v_rdi + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_stack_mE0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8125530) + result * 8);
    goto loc_0067044A;
loc_00670442:
loc_00670445:
loc_0067044A:
    result = v_stack_mE0;
    if (0 != 0) {
        a3 = 1;
        a1 = v_stack_mE0;
        result = MiReleasePageFileInfo(a1, 0, a3, a4);
    }
    goto loc_00670621;
loc_00670481:
    if (condition_is_below) goto loc_00670505;
    if (sign_flag) goto loc_00670505;
    if (*(unsigned __int64 *)((unsigned int)(v_stack_p10) + 8) == 0) goto loc_00670505;
    a4 = 0;
    a3 = (a3) | (-1);
    v_stack_m108 = 0;
    result = MiCopyOnWrite(v_stack_mF0, v_r14, a3, a4);
    if (!sign_flag) goto loc_00670261;
    result = MiUnlockPageTable(*(unsigned __int64 *)(a1 + 16), v_r15, a3, a4);
    result = MiUnlockWorkingSetShared(*(unsigned __int64 *)(a1 + 16), v_stack_p8, a3, a4);
    a3 = 0;
    result = MiCopyOnWriteCheckConditions(*(unsigned __int64 *)(a1 + 16), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a3, a4);
    result = MiLockWorkingSetShared(*(unsigned __int64 *)(a1 + 16), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a3, a4);
    result = MiLockNestedPageTable(*(unsigned __int64 *)(a1 + 16), v_r15, a3, a4);
    goto loc_00670261;
loc_00670505:
    result = MiUnlockPageTable(*(unsigned __int64 *)(a1 + 16), v_r15, a3, a4);
    result = MiUnlockWorkingSetShared(*(unsigned __int64 *)(a1 + 16), v_stack_p8, a3, a4);
    result = (unsigned int)(((unsigned int)(v_stack_p18)) - ((unsigned int)((unsigned int)(v_stack_p10))));
    result = MiMakeDriverPagesPrivate(*(unsigned __int64 *)(a1), v_r14, v_r14 + result * 8, 8);
    result = MiLockWorkingSetShared(*(unsigned __int64 *)(a1 + 16), v_r14, v_r14 + result * 8, 8);
    result = MiLockNestedPageTable(*(unsigned __int64 *)(a1 + 16), v_r15, v_r14 + result * 8, 8);
    goto loc_00670268;
loc_00670562:
    result = MiMakeDemandZeroPte(16, v_r15, v_r14 + result * 8, 8);
    if (v_stack_mF8 == result) goto loc_006705DC;
    result = MiUnlockPageTable(*(unsigned __int64 *)(a1 + 16), v_r15, v_r14 + result * 8, 8);
    result = MiUnlockWorkingSetShared(*(unsigned __int64 *)(a1 + 16), v_stack_p8, v_r14 + result * 8, 8);
    a4 = (v_stack_mC8) | (1);
    v_stack_mC8 = 6;
    a3 = 0;
    v_stack_mC0 = 0;
    a1 = 0;
    v_stack_mB8 = 0;
    v_stack_mB0 = 0;
    v_stack_mA8 = 0;
    result = MmAccessFault(a1, v_stack_mF0, a3, a4);
    if (!sign_flag) goto loc_00670660;
    result = MiLockWorkingSetShared(*(unsigned __int64 *)(a1 + 16), v_stack_mF0, a3, a4);
    result = MiLockNestedPageTable(*(unsigned __int64 *)(a1 + 16), v_r15, a3, a4);
loc_006705DC:
    if (((v_stack_p20) & (2)) != 0) goto loc_00670621;
    if ((*(unsigned __int64 *)(a1 + 88)) == 0) goto loc_00670613;
    if (((unsigned int)((unsigned int)((unsigned int)(v_stack_p10)))) >= (*(unsigned __int64 *)(a1 + 80))) goto loc_00670613;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_p10)))) >> (6);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p10)))))) & (63));
    result = (condition_is_below) ? 1 : 0;
    if ((unsigned __int8)(result) != 0) goto loc_00670621;
loc_00670613:
    goto loc_0067067C;
loc_0067061A:
loc_00670621:
    v_rdi = (unsigned int)(((unsigned int)(v_stack_p10)) + 1);
    v_r13 = (v_r13) + (8);
    v_stack_p10 = (unsigned int)(v_rdi);
    a1 = (((v_r13) & (0xFFFULL)) != 0) ? 1 : 0;
    result = (((*(unsigned __int8 *)(a1 + 96)) & (2)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_00670268;
    v_r14 = (v_r14) + (8);
    goto loc_00670268;
loc_00670660:
    goto loc_0067024D;
loc_0067066A:
    if (a5 != 0) {
    }
    result = MiUnlockPageTable(*(unsigned __int64 *)(a1 + 16), v_r15, a3, a4);
    result = MiUnlockWorkingSetShared(*(unsigned __int64 *)(a1 + 16), v_stack_p8, a3, a4);
    v_rsp = (v_rsp) + (232);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000007BULL)));
}
```

## 5. (Beta) C Style

```c
int64_t MiLockDriverPageRange(void *Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4, int64_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint8_t v_stack_p8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (232);
    Arg2 = 0;
    result = memset(v_stack_mC8, Arg2, Arg2 + 120, Arg4);
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(Arg2)))) << (12);
    local_rbx = 0;
    v_stack_mE0 = 0;
    Arg1 = (Arg1) + (*(uint64_t *)(*(uint64_t *)(arg1) + 0x30));
    v_stack_mF0 = Arg1;
    local_r13 = (Arg1) >> (9);
    local_r13 = (local_r13) & (0);
    local_r13 = (local_r13) + (Arg1);
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x60));
    local_r14 = local_r13;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x60)))) & (2)) != 0) {
        local_r14 = (local_r13) >> (9);
        local_r14 = (local_r14) & (0);
        result = Arg1;
        local_r14 = (local_r14) + (result);
    }
    v_stack_mF8 = 0;
    Arg1 = (Arg5) + (48);
    result = -(Arg5);
    result = (result) & (Arg1);
    v_stack_mD8 = result;
loc_00670214:
    if (0 >= 1) goto loc_00670242;
    if ((*(uint64_t *)(v_rip + 0x7BD71E + 0x0 * 8)) == (*(uint64_t *)(arg1))) goto loc_0067022C;
    result = (uint32_t)((0) + 1);
    goto loc_00670214;
loc_0067022C:
    local_rsi = (0) << (4);
    local_rsi = (local_rsi) + (v_rip + 8115986);
    v_stack_mF8 = local_rsi;
loc_00670242:
loc_0067024D:
    result = MiLockWorkingSetShared(*(uint64_t *)(arg1 + 0x10), v_rip + 8115998, Arg2 + 120, Arg4);
    v_stack_p8 = (uint8_t)(result);
    goto loc_00670268;
loc_00670261:
loc_00670268:
    if (((uint32_t)((uint32_t)(v_stack_p10))) > v_stack_p18) goto loc_0067066A;
    if (0 == 0) goto loc_0067028E;
    if (((local_r13) & (0xFFFULL)) != 0) goto loc_006702BD;
    result = MiUnlockPageTable(*(uint64_t *)(arg1 + 0x10), 0, Arg2 + 120, Arg4);
loc_0067028E:
    local_r15 = (local_r14) >> (9);
    local_r15 = (local_r15) & (result);
    local_r15 = (local_r15) + (result);
    result = MiLockNestedPageTable(*(uint64_t *)(arg1 + 0x10), local_r15, Arg2 + 120, Arg4);
loc_006702BD:
    if (local_rsi == 0) goto loc_006702E9;
    if (((uint32_t)((uint32_t)((uint32_t)(v_stack_p10)))) >= (*(uint64_t *)(local_rsi))) goto loc_006702E9;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_p10)))) >> (6);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p10)))))) & (63));
    result = (condition_is_below) ? 1 : 0;
    if ((uint8_t)(result) != 0) goto loc_006705DC;
loc_006702E9:
    if ((*(uint64_t *)(arg1 + 0x38)) == 0) goto loc_0067031A;
    if (((uint32_t)((uint32_t)((uint32_t)(v_stack_p10)))) >= (*(uint64_t *)(arg1 + 0x30))) goto loc_0067031A;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_p10)))) >> (6);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p10)))))) & (63));
    result = (condition_is_below) ? 1 : 0;
    if ((uint8_t)(result) != 0) goto loc_00670621;
loc_0067031A:
    if ((((uint8_t)(*(uint64_t *)(local_r14))) & (1)) == 0) goto loc_00670562;
    local_rsi = (*(uint64_t *)(local_r14)) >> (12);
    local_rsi = (local_rsi) & (result);
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x60));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x60)))) & (2)) != 0) {
        result = local_r13;
        result = (result) >> (3);
        result = (uint32_t)((result) & (511));
        local_rsi = (local_rsi) + (result);
    }
    local_rdi = (local_rsi + local_rsi * 2) << (4);
    local_rdi = (local_rdi) + (result);
    if (sign_flag) goto loc_00670481;
    result = (condition_is_below) ? 1 : 0;
    if ((uint8_t)(result) != 0) goto loc_0067061A;
    v_stack_mE8 = 0;
loc_00670392:
    if (condition_is_above_or_equal) goto loc_006703B0;
loc_0067039B:
    result = KeYieldProcessorEx(v_stack_mE8, Arg2, Arg2 + 120, Arg4);
    if (sign_flag) goto loc_0067039B;
    goto loc_00670392;
loc_006703B0:
    result = MiReferenceDriverPage(local_rdi, Arg2, Arg2 + 120, Arg4);
    if ((((uint8_t)((uint32_t)(v_stack_p20))) & (1)) == 0) goto loc_006703F8;
    result = (*(uint64_t *)(local_rdi + 0x28)) >> (60);
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) != 3) {
        Arg2 = v_stack_mF0;
        Arg4 = 128;
        Arg3 = 0;
        Arg1 = local_rsi;
        result = KeSetPagePrivilege(Arg1, Arg2, Arg3, Arg4);
        Arg3 = v_stack_p20;
    }
    if (v_stack_mD8 != 0) {
        Arg1 = v_stack_p10;
        *(uint64_t *)(v_stack_mD8 + arg1 * 8) = local_rsi;
    }
    if ((((uint8_t)(Arg3)) & (4)) != 0) goto loc_00670442;
    result = MiCaptureDirtyBitToPfn(local_rdi, v_stack_mD8, Arg3, Arg4);
    if (result == 0) goto loc_00670445;
    result = (*(uint64_t *)(local_rdi + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    v_stack_mE0 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x7BFC5A) + result * 8);
    goto loc_0067044A;
loc_00670442:
loc_00670445:
loc_0067044A:
    result = v_stack_mE0;
    if (0 != 0) {
        Arg3 = 1;
        Arg1 = v_stack_mE0;
        result = MiReleasePageFileInfo(Arg1, 0, Arg3, Arg4);
    }
    goto loc_00670621;
loc_00670481:
    if (condition_is_below) goto loc_00670505;
    if (sign_flag) goto loc_00670505;
    if (*(uint64_t *)((uint32_t)(v_stack_p10) + 0x8) == 0) goto loc_00670505;
    Arg4 = 0;
    Arg3 = (Arg3) | (-1);
    v_stack_m108 = 0;
    result = MiCopyOnWrite(v_stack_mF0, local_r14, Arg3, Arg4);
    if (!sign_flag) goto loc_00670261;
    result = MiUnlockPageTable(*(uint64_t *)(arg1 + 0x10), local_r15, Arg3, Arg4);
    result = MiUnlockWorkingSetShared(*(uint64_t *)(arg1 + 0x10), v_stack_p8, Arg3, Arg4);
    Arg3 = 0;
    result = MiCopyOnWriteCheckConditions(*(uint64_t *)(arg1 + 0x10), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg3, Arg4);
    result = MiLockWorkingSetShared(*(uint64_t *)(arg1 + 0x10), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg3, Arg4);
    result = MiLockNestedPageTable(*(uint64_t *)(arg1 + 0x10), local_r15, Arg3, Arg4);
    goto loc_00670261;
loc_00670505:
    result = MiUnlockPageTable(*(uint64_t *)(arg1 + 0x10), local_r15, Arg3, Arg4);
    result = MiUnlockWorkingSetShared(*(uint64_t *)(arg1 + 0x10), v_stack_p8, Arg3, Arg4);
    result = (uint32_t)(((uint32_t)(v_stack_p18)) - ((uint32_t)((uint32_t)(v_stack_p10))));
    result = MiMakeDriverPagesPrivate(*(uint64_t *)(arg1), local_r14, local_r14 + result * 8, 8);
    result = MiLockWorkingSetShared(*(uint64_t *)(arg1 + 0x10), local_r14, local_r14 + result * 8, 8);
    result = MiLockNestedPageTable(*(uint64_t *)(arg1 + 0x10), local_r15, local_r14 + result * 8, 8);
    goto loc_00670268;
loc_00670562:
    result = MiMakeDemandZeroPte(16, local_r15, local_r14 + result * 8, 8);
    if (v_stack_mF8 == result) goto loc_006705DC;
    result = MiUnlockPageTable(*(uint64_t *)(arg1 + 0x10), local_r15, local_r14 + result * 8, 8);
    result = MiUnlockWorkingSetShared(*(uint64_t *)(arg1 + 0x10), v_stack_p8, local_r14 + result * 8, 8);
    Arg4 = (v_stack_mC8) | (1);
    v_stack_mC8 = 6;
    Arg3 = 0;
    v_stack_mC0 = 0;
    Arg1 = 0;
    v_stack_mB8 = 0;
    v_stack_mB0 = 0;
    v_stack_mA8 = 0;
    result = MmAccessFault(Arg1, v_stack_mF0, Arg3, Arg4);
    if (!sign_flag) goto loc_00670660;
    result = MiLockWorkingSetShared(*(uint64_t *)(arg1 + 0x10), v_stack_mF0, Arg3, Arg4);
    result = MiLockNestedPageTable(*(uint64_t *)(arg1 + 0x10), local_r15, Arg3, Arg4);
loc_006705DC:
    if (((v_stack_p20) & (2)) != 0) goto loc_00670621;
    if ((*(uint64_t *)(arg1 + 0x58)) == 0) goto loc_00670613;
    if (((uint32_t)((uint32_t)((uint32_t)(v_stack_p10)))) >= (*(uint64_t *)(arg1 + 0x50))) goto loc_00670613;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_p10)))) >> (6);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p10)))))) & (63));
    result = (condition_is_below) ? 1 : 0;
    if ((uint8_t)(result) != 0) goto loc_00670621;
loc_00670613:
    goto loc_0067067C;
loc_0067061A:
loc_00670621:
    local_rdi = (uint32_t)(((uint32_t)(v_stack_p10)) + 1);
    local_r13 = (local_r13) + (8);
    v_stack_p10 = (uint32_t)(local_rdi);
    Arg1 = (((local_r13) & (0xFFFULL)) != 0) ? 1 : 0;
    result = (((*(uint8_t *)(arg1 + 0x60)) & (2)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_00670268;
    local_r14 = (local_r14) + (8);
    goto loc_00670268;
loc_00670660:
    goto loc_0067024D;
loc_0067066A:
    if (Arg5 != 0) {
    }
    result = MiUnlockPageTable(*(uint64_t *)(arg1 + 0x10), local_r15, Arg3, Arg4);
    result = MiUnlockWorkingSetShared(*(uint64_t *)(arg1 + 0x10), v_stack_p8, Arg3, Arg4);
    local_rsp = (local_rsp) + (232);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000007BULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x60` | `8` | `R` |
| `Arg1` | `+ 0x60` | `32` | `R` |
| `Arg1` | `+ 0x60` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00670160&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
