# KiResumeThread

- RVA: `0x00203644`–`0x00203A41` (길이 `1,021` bytes)
- VA: `0x0000000140203644`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CA90`
- 디코드: `263`개 명령, `1,021/1,021` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x002036EA` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x0020370E` → [KiSignalThreadForApc](KiSignalThreadForApc_function_00204360.md) (function, `0x00204360`)
- `0x00203798` → [KiAcquireKobjectLockSafe](../25/KiAcquireKobjectLockSafe_function_00251C90.md) (function, `0x00251C90`)
- `0x002037DD` → [KiSignalThread](../21/KiSignalThread_function_0021F9E0.md) (function, `0x0021F9E0`)
- `0x00203880` → [KiInsertQueueInternal](../21/KiInsertQueueInternal_function_00219B30.md) (function, `0x00219B30`)
- `0x0020390A` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00203919` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0020394B` → [KiComputeDueTime](../23/KiComputeDueTime_function_002332E8.md) (function, `0x002332E8`)
- `0x0020396C` → [KiInsertTimerTable](../23/KiInsertTimerTable_function_00233400.md) (function, `0x00233400`)
- `0x002039C6` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002039D5` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00203A09` → [KiTimerWaitTest](../23/KiTimerWaitTest_function_002337D0.md) (function, `0x002337D0`)
- `0x00203A25` → [KeInsertQueueDpc](KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)
- `0x00203A37` → [KiTraceSetTimer](../22/KiTraceSetTimer_function_0022FB08.md) (function, `0x0022FB08`)

### Direct callers
- [KeResumeThread](KeResumeThread_function_00202858.md) at `0x002028DA`
- [KeForceResumeThread](KeForceResumeThread_function_0020292C.md) at `0x0020299A`
- [KiThawSingleThread](KiThawSingleThread_function_00203560.md) at `0x002035E5`
- [KiAdjustThreadTimer](../5C/KiAdjustThreadTimer_function_005C3A3C.md) at `0x005C3B27`

### Static image references
- `0x0020367F` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x002038FC` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00203979` → RVA `0x00FC6B08` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00203644  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00203649  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0020364E  56                              push rsi
0020364F  57                              push rdi
00203650  41 54                           push r12
00203652  41 56                           push r14
00203654  41 57                           push r15
00203656  48 83 EC 30                     sub rsp, 0x30
0020365A  83 64 24 70 00                  and dword ptr [rsp + 0x70], 0
0020365F  45 8A F0                        mov r14b, r8b
00203662  33 FF                           xor edi, edi
00203664  C7 81 E4 02 00 00 01 00 00 00   mov dword ptr [rcx + 0x2e4], 1
0020366E  4C 8B E2                        mov r12, rdx
00203671  48 8B D9                        mov rbx, rcx
00203674  F0 48 0F BA 6B 40 00            lock bts qword ptr [rbx + 0x40], 0
0020367B  73 1B                           jae 0x140203698
0020367D  FF C7                           inc edi
0020367F  85 3D 27 1C DC 00               test dword ptr [rip + 0xdc1c27], edi
00203685  0F 84 71 02 00 00               je 0x1402038fc
0020368B  F3 90                           pause
0020368D  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
00203691  48 85 C0                        test rax, rax
00203694  74 DE                           je 0x140203674
00203696  EB E5                           jmp 0x14020367d
00203698  80 BB 84 01 00 00 05            cmp byte ptr [rbx + 0x184], 5
0020369F  0F 84 8F 00 00 00               je 0x140203734
002036A5  BD 00 01 00 00                  mov ebp, 0x100
002036AA  45 84 F6                        test r14b, r14b
002036AD  75 42                           jne 0x1402036f1
002036AF  48 C7 43 40 00 00 00 00         mov qword ptr [rbx + 0x40], 0
002036B7  48 8D B3 E0 02 00 00            lea rsi, [rbx + 0x2e0]
002036BE  48 8D 5E 08                     lea rbx, [rsi + 8]
002036C2  48 8B 3B                        mov rdi, qword ptr [rbx]
002036C5  48 3B FB                        cmp rdi, rbx
002036C8  74 4B                           je 0x140203715
002036CA  48 8B C7                        mov rax, rdi
002036CD  48 8B 3F                        mov rdi, qword ptr [rdi]
002036D0  8A 48 10                        mov cl, byte ptr [rax + 0x10]
002036D3  80 F9 01                        cmp cl, 1
002036D6  0F 85 90 01 00 00               jne 0x14020386c
002036DC  44 0F B7 40 12                  movzx r8d, word ptr [rax + 0x12]
002036E1  45 33 C9                        xor r9d, r9d
002036E4  48 8B D0                        mov rdx, rax
002036E7  49 8B CC                        mov rcx, r12
002036EA  E8 E1 CF 14 00                  call 0x1403506d0
002036EF  EB D4                           jmp 0x1402036c5
002036F1  8B 43 78                        mov eax, dword ptr [rbx + 0x78]
002036F4  0F BA E0 0F                     bt eax, 0xf
002036F8  0F 82 C5 00 00 00               jb 0x1402037c3
002036FE  48 8D 93 88 02 00 00            lea rdx, [rbx + 0x288]
00203705  45 33 C9                        xor r9d, r9d
00203708  41 B0 02                        mov r8b, 2
0020370B  49 8B CC                        mov rcx, r12
0020370E  E8 4D 0C 00 00                  call 0x140204360
00203713  EB 9A                           jmp 0x1402036af
00203715  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0020371A  48 89 5B 08                     mov qword ptr [rbx + 8], rbx
0020371E  48 89 1B                        mov qword ptr [rbx], rbx
00203721  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00203726  48 83 C4 30                     add rsp, 0x30
0020372A  41 5F                           pop r15
0020372C  41 5E                           pop r14
0020372E  41 5C                           pop r12
00203730  5F                              pop rdi
00203731  5E                              pop rsi
00203732  C3                              ret
00203733  CC                              int3
00203734  8A 4B 70                        mov cl, byte ptr [rbx + 0x70]
00203737  8A C1                           mov al, cl
00203739  24 07                           and al, 7
0020373B  3C 04                           cmp al, 4
0020373D  0F 85 62 FF FF FF               jne 0x1402036a5
00203743  45 84 F6                        test r14b, r14b
00203746  0F 85 63 01 00 00               jne 0x1402038af
0020374C  80 E1 FD                        and cl, 0xfd
0020374F  80 C9 05                        or cl, 5
00203752  88 4B 70                        mov byte ptr [rbx + 0x70], cl
00203755  40 32 ED                        xor bpl, bpl
00203758  48 C7 43 40 00 00 00 00         mov qword ptr [rbx + 0x40], 0
00203760  44 8A BB 4B 02 00 00            mov r15b, byte ptr [rbx + 0x24b]
00203767  41 3A EF                        cmp bpl, r15b
0020376A  0F 83 85 00 00 00               jae 0x1402037f5
00203770  40 0F B6 C5                     movzx eax, bpl
00203774  48 8D 3C 40                     lea rdi, [rax + rax*2]
00203778  48 C1 E7 04                     shl rdi, 4
0020377C  48 03 BB D0 00 00 00            add rdi, qword ptr [rbx + 0xd0]
00203783  80 7F 11 06                     cmp byte ptr [rdi + 0x11], 6
00203787  0F 85 45 01 00 00               jne 0x1402038d2
0020378D  48 8B 77 20                     mov rsi, qword ptr [rdi + 0x20]
00203791  48 8B CE                        mov rcx, rsi
00203794  C6 47 11 04                     mov byte ptr [rdi + 0x11], 4
00203798  E8 F3 E4 04 00                  call 0x140251c90
0020379D  83 7E 04 00                     cmp dword ptr [rsi + 4], 0
002037A1  7F 44                           jg 0x1402037e7
002037A3  8A 06                           mov al, byte ptr [rsi]
002037A5  24 7F                           and al, 0x7f
002037A7  3C 02                           cmp al, 2
002037A9  74 3C                           je 0x1402037e7
002037AB  48 8D 46 08                     lea rax, [rsi + 8]
002037AF  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
002037B3  48 39 01                        cmp qword ptr [rcx], rax
002037B6  0F 84 01 01 00 00               je 0x1402038bd
002037BC  B9 03 00 00 00                  mov ecx, 3
002037C1  CD 29                           int 0x29
002037C3  8A 83 84 01 00 00               mov al, byte ptr [rbx + 0x184]
002037C9  3C 05                           cmp al, 5
002037CB  0F 85 DE FE FF FF               jne 0x1402036af
002037D1  45 33 C9                        xor r9d, r9d
002037D4  4C 8B C5                        mov r8, rbp
002037D7  48 8B D3                        mov rdx, rbx
002037DA  49 8B CC                        mov rcx, r12
002037DD  E8 FE C1 01 00                  call 0x14021f9e0
002037E2  E9 C8 FE FF FF                  jmp 0x1402036af
002037E7  F0 81 26 7F FF FF FF            lock and dword ptr [rsi], 0xffffff7f
002037EE  C6 47 11 05                     mov byte ptr [rdi + 0x11], 5
002037F2  41 B6 01                        mov r14b, 1
002037F5  33 FF                           xor edi, edi
002037F7  0F BA 63 74 11                  bt dword ptr [rbx + 0x74], 0x11
002037FC  0F 82 21 01 00 00               jb 0x140203923
00203802  33 F6                           xor esi, esi
00203804  F0 48 0F BA 6B 40 00            lock bts qword ptr [rbx + 0x40], 0
0020380B  73 1B                           jae 0x140203828
0020380D  FF C6                           inc esi
0020380F  85 35 97 1A DC 00               test dword ptr [rip + 0xdc1a97], esi
00203815  0F 84 9D 01 00 00               je 0x1402039b8
0020381B  F3 90                           pause
0020381D  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
00203821  48 85 C0                        test rax, rax
00203824  74 DE                           je 0x140203804
00203826  EB E5                           jmp 0x14020380d
00203828  8B 43 74                        mov eax, dword ptr [rbx + 0x74]
0020382B  8A 4B 70                        mov cl, byte ptr [rbx + 0x70]
0020382E  0F BA F0 09                     btr eax, 9
00203832  C1 E7 09                        shl edi, 9
00203835  0B F8                           or edi, eax
00203837  8A C1                           mov al, cl
00203839  0F BA F7 11                     btr edi, 0x11
0020383D  24 E7                           and al, 0xe7
0020383F  89 7B 74                        mov dword ptr [rbx + 0x74], edi
00203842  3C 05                           cmp al, 5
00203844  0F 85 5A 01 00 00               jne 0x1402039a4
0020384A  48 0F BE 93 87 01 00 00         movsx rdx, byte ptr [rbx + 0x187]
00203852  C1 EF 04                        shr edi, 4
00203855  40 F6 C7 01                     test dil, 1
00203859  75 7F                           jne 0x1402038da
0020385B  F6 83 C2 00 00 00 02            test byte ptr [rbx + 0xc2], 2
00203862  0F 85 30 01 00 00               jne 0x140203998
00203868  8A D1                           mov dl, cl
0020386A  EB 34                           jmp 0x1402038a0
0020386C  80 F9 02                        cmp cl, 2
0020386F  0F 85 74 01 00 00               jne 0x1402039e9
00203875  C6 40 11 05                     mov byte ptr [rax + 0x11], 5
00203879  48 8B D0                        mov rdx, rax
0020387C  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
00203880  E8 AB 62 01 00                  call 0x140219b30
00203885  E9 3B FE FF FF                  jmp 0x1402036c5
0020388A  80 7B 72 00                     cmp byte ptr [rbx + 0x72], 0
0020388E  0F 85 62 01 00 00               jne 0x1402039f6
00203894  33 C0                           xor eax, eax
00203896  8A D1                           mov dl, cl
00203898  85 C0                           test eax, eax
0020389A  0F 85 02 01 00 00               jne 0x1402039a2
002038A0  80 BB 83 02 00 00 25            cmp byte ptr [rbx + 0x283], 0x25
002038A7  8A CA                           mov cl, dl
002038A9  0F 84 FD 00 00 00               je 0x1402039ac
002038AF  80 E1 F9                        and cl, 0xf9
002038B2  80 C9 01                        or cl, 1
002038B5  88 4B 70                        mov byte ptr [rbx + 0x70], cl
002038B8  E9 E8 FD FF FF                  jmp 0x1402036a5
002038BD  48 89 07                        mov qword ptr [rdi], rax
002038C0  48 89 4F 08                     mov qword ptr [rdi + 8], rcx
002038C4  48 89 39                        mov qword ptr [rcx], rdi
002038C7  48 89 78 08                     mov qword ptr [rax + 8], rdi
002038CB  F0 81 26 7F FF FF FF            lock and dword ptr [rsi], 0xffffff7f
002038D2  40 FE C5                        inc bpl
002038D5  E9 8D FE FF FF                  jmp 0x140203767
002038DA  80 7C 1A 72 00                  cmp byte ptr [rdx + rbx + 0x72], 0
002038DF  0F 85 11 01 00 00               jne 0x1402039f6
002038E5  84 D2                           test dl, dl
002038E7  74 A1                           je 0x14020388a
002038E9  48 8D 83 A8 00 00 00            lea rax, [rbx + 0xa8]
002038F0  48 39 00                        cmp qword ptr [rax], rax
002038F3  74 95                           je 0x14020388a
002038F5  B8 C0 00 00 00                  mov eax, 0xc0
002038FA  EB 9A                           jmp 0x140203896
002038FC  8B 05 B6 31 DC 00               mov eax, dword ptr [rip + 0xdc31b6]
00203902  A8 40                           test al, 0x40
00203904  0F 84 81 FD FF FF               je 0x14020368b
0020390A  E8 81 BB 10 00                  call 0x14030f490
0020390F  84 C0                           test al, al
00203911  0F 84 74 FD FF FF               je 0x14020368b
00203917  8B CF                           mov ecx, edi
00203919  E8 42 BB 10 00                  call 0x14030f460
0020391E  E9 6A FD FF FF                  jmp 0x14020368d
00203923  45 84 F6                        test r14b, r14b
00203926  0F 85 D6 FE FF FF               jne 0x140203802
0020392C  48 8B 93 18 01 00 00            mov rdx, qword ptr [rbx + 0x118]
00203933  48 8D BB 00 01 00 00            lea rdi, [rbx + 0x100]
0020393A  81 0F 80 00 00 40               or dword ptr [rdi], 0x40000080
00203940  4C 8D 4C 24 70                  lea r9, [rsp + 0x70]
00203945  48 8B CF                        mov rcx, rdi
00203948  45 33 C0                        xor r8d, r8d
0020394B  E8 98 F9 02 00                  call 0x1402332e8
00203950  85 C0                           test eax, eax
00203952  0F 84 87 00 00 00               je 0x1402039df
00203958  44 8B 4C 24 70                  mov r9d, dword ptr [rsp + 0x70]
0020395D  45 33 C0                        xor r8d, r8d
00203960  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00203966  48 8B D7                        mov rdx, rdi
00203969  49 8B CC                        mov rcx, r12
0020396C  E8 8F FA 02 00                  call 0x140233400
00203971  84 C0                           test al, al
00203973  0F 84 87 00 00 00               je 0x140203a00
00203979  0F BA 25 87 31 DC 00 11         bt dword ptr [rip + 0xdc3187], 0x11
00203981  0F 82 A8 00 00 00               jb 0x140203a2f
00203987  F0 81 27 7F FF FF FF            lock and dword ptr [rdi], 0xffffff7f
0020398E  BF 01 00 00 00                  mov edi, 1
00203993  E9 6A FE FF FF                  jmp 0x140203802
00203998  84 D2                           test dl, dl
0020399A  0F 84 C8 FE FF FF               je 0x140203868
002039A0  8A D1                           mov dl, cl
002039A2  8A CA                           mov cl, dl
002039A4  41 B6 01                        mov r14b, 1
002039A7  E9 03 FF FF FF                  jmp 0x1402038af
002039AC  8B 43 78                        mov eax, dword ptr [rbx + 0x78]
002039AF  A8 10                           test al, 0x10
002039B1  75 F1                           jne 0x1402039a4
002039B3  E9 F7 FE FF FF                  jmp 0x1402038af
002039B8  8B 05 FA 30 DC 00               mov eax, dword ptr [rip + 0xdc30fa]
002039BE  A8 40                           test al, 0x40
002039C0  0F 84 55 FE FF FF               je 0x14020381b
002039C6  E8 C5 BA 10 00                  call 0x14030f490
002039CB  84 C0                           test al, al
002039CD  0F 84 48 FE FF FF               je 0x14020381b
002039D3  8B CE                           mov ecx, esi
002039D5  E8 86 BA 10 00                  call 0x14030f460
002039DA  E9 3E FE FF FF                  jmp 0x14020381d
002039DF  41 B6 01                        mov r14b, 1
002039E2  33 FF                           xor edi, edi
002039E4  E9 19 FE FF FF                  jmp 0x140203802
002039E9  80 F9 04                        cmp cl, 4
002039EC  74 25                           je 0x140203a13
002039EE  4C 8B C5                        mov r8, rbp
002039F1  E9 EB FC FF FF                  jmp 0x1402036e1
002039F6  B8 01 01 00 00                  mov eax, 0x101
002039FB  E9 96 FE FF FF                  jmp 0x140203896
00203A00  45 33 C0                        xor r8d, r8d
00203A03  48 8B D7                        mov rdx, rdi
00203A06  49 8B CC                        mov rcx, r12
00203A09  E8 C2 FD 02 00                  call 0x1402337d0
00203A0E  E9 7B FF FF FF                  jmp 0x14020398e
00203A13  C6 40 11 05                     mov byte ptr [rax + 0x11], 5
00203A17  4C 8B C0                        mov r8, rax
00203A1A  83 66 04 00                     and dword ptr [rsi + 4], 0
00203A1E  48 8B D6                        mov rdx, rsi
00203A21  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
00203A25  E8 26 42 00 00                  call 0x140207c50
00203A2A  E9 96 FC FF FF                  jmp 0x1402036c5
00203A2F  41 B0 01                        mov r8b, 1
00203A32  33 D2                           xor edx, edx
00203A34  48 8B CF                        mov rcx, rdi
00203A37  E8 CC C0 02 00                  call 0x14022fb08
00203A3C  E9 4D FF FF FF                  jmp 0x14020398e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiResumeThread(__int64 a1, __int64 a2, unsigned __int8 a3, int a4)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_rsp = (v_rsp) - (48);
    v_rdi = 0;
    *(unsigned int *)(a1 + 740) = 1;
loc_00203674:
    if (condition_is_above_or_equal) goto loc_00203698;
loc_0020367D:
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((*(unsigned int *)(v_rip + 14425127)) & ((unsigned int)(v_rdi))) == 0) goto loc_002038FC;
loc_0020368B:
loc_0020368D:
    if (*(unsigned __int64 *)(a1 + 64) == 0) goto loc_00203674;
    goto loc_0020367D;
loc_00203698:
    if ((*(unsigned __int8 *)(a1 + 388)) == 5) goto loc_00203734;
loc_002036A5:
    if (a3 != 0) goto loc_002036F1;
loc_002036AF:
    *(unsigned __int64 *)(a1 + 64) = 0;
loc_002036C5:
    if ((*(unsigned __int64 *)(a1 + 736 + 8)) == (a1 + 736 + 8)) goto loc_00203715;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 736 + 8) + 16))) != 1) goto loc_0020386C;
loc_002036E1:
    a4 = 0;
    result = KiTryUnwaitThread(a2, *(unsigned __int64 *)(a1 + 736 + 8), *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 736 + 8) + 18), a4);
    goto loc_002036C5;
loc_002036F1:
    if (condition_is_below) goto loc_002037C3;
    a4 = 0;
    result = KiSignalThreadForApc(a2, a1 + 736 + 8 + 648, 2, a4);
    goto loc_002036AF;
loc_00203715:
    *(unsigned __int64 *)(a1 + 736 + 8 + 8) = a1 + 736 + 8;
    *(unsigned __int64 *)(a1 + 736 + 8) = a1 + 736 + 8;
    v_rsp = (v_rsp) + (48);
    return result;
loc_00203734:
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 112))) & (7));
    if (((unsigned __int8)(result)) != 4) goto loc_002036A5;
    if (a3 != 0) goto loc_002038AF;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_stack_p8 + 112)) & (253));
    a1 = (unsigned __int8)((a1) | (5));
    *(unsigned __int8 *)(v_stack_p8 + 112) = (unsigned __int8)(a1);
    v_rbp = 0;
    *(unsigned __int64 *)(v_stack_p8 + 64) = 0;
loc_00203767:
    if (0 >= ((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 587)))) goto loc_002037F5;
    v_rdi = (0 + 0 * 2) << (4);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_stack_p8 + 208));
    if ((*(unsigned __int8 *)(v_rdi + 17)) != 6) goto loc_002038D2;
    *(unsigned __int8 *)(v_rdi + 17) = 4;
    result = KiAcquireKobjectLockSafe(*(unsigned __int64 *)(v_rdi + 32), a1 + 736 + 8 + 648, 2, a4);
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rdi + 32) + 4)) > 0) goto loc_002037E7;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rdi + 32))) & (127));
    if (((unsigned __int8)(result)) == 2) goto loc_002037E7;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 32) + 8 + 8))) == (*(unsigned __int64 *)(v_rdi + 32) + 8)) goto loc_002038BD;
loc_002037C3:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 388))) != 5) goto loc_002036AF;
    a4 = 0;
    result = KiSignalThread(a2, v_stack_p8, 0, a4);
    goto loc_002036AF;
loc_002037E7:
    *(unsigned __int8 *)(v_rdi + 17) = 5;
loc_002037F5:
    v_rdi = 0;
    if (condition_is_below) goto loc_00203923;
loc_00203802:
    v_rsi = 0;
loc_00203804:
    if (condition_is_above_or_equal) goto loc_00203828;
loc_0020380D:
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (((*(unsigned int *)(v_rip + 14424727)) & ((unsigned int)(v_rsi))) == 0) goto loc_002039B8;
loc_0020381B:
loc_0020381D:
    if (*(unsigned __int64 *)(v_stack_p8 + 64) == 0) goto loc_00203804;
    goto loc_0020380D;
loc_00203828:
    v_rdi = (unsigned int)((v_rdi) << (9));
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 116)))));
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 112))) & (231));
    *(unsigned int *)(v_stack_p8 + 116) = (unsigned int)(v_rdi);
    if (((unsigned __int8)(result)) != 5) goto loc_002039A4;
    v_rdi = (unsigned int)((v_rdi) >> (4));
    if ((((unsigned __int8)(v_rdi)) & (1)) != 0) goto loc_002038DA;
    if (((*(unsigned __int8 *)(v_stack_p8 + 194)) & (2)) != 0) goto loc_00203998;
loc_00203868:
    goto loc_002038A0;
loc_0020386C:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 112))) != 2) goto loc_002039E9;
    *(unsigned __int8 *)(result + 17) = 5;
    result = KiInsertQueueInternal(*(unsigned __int64 *)(result + 24), result, 0, a4);
    goto loc_002036C5;
loc_0020388A:
    if ((*(unsigned __int8 *)(v_stack_p8 + 114)) != 0) goto loc_002039F6;
    result = 0;
loc_00203896:
    if (0 != 0) goto loc_002039A2;
loc_002038A0:
    if ((*(unsigned __int8 *)(v_stack_p8 + 643)) == 37) goto loc_002039AC;
loc_002038AF:
    a1 = (unsigned __int8)(((unsigned __int8)((unsigned __int8)(*(unsigned __int64 *)(result + 24)))) & (249));
    a1 = (unsigned __int8)((a1) | (1));
    *(unsigned __int8 *)(v_stack_p8 + 112) = (unsigned __int8)(a1);
    goto loc_002036A5;
loc_002038BD:
    *(unsigned __int64 *)(v_rdi) = 0;
    *(unsigned __int64 *)(v_rdi + 8) = a1;
    *(unsigned __int64 *)(a1) = v_rdi;
    *(unsigned __int64 *)(result + 8) = v_rdi;
loc_002038D2:
    v_rbp = (unsigned __int8)((v_rbp) + 1);
    goto loc_00203767;
loc_002038DA:
    if ((*(unsigned __int8 *)((unsigned __int8)(*(unsigned __int64 *)(result + 24)) + v_stack_p8 * 1 + 114)) != 0) goto loc_002039F6;
    if ((unsigned __int8)((unsigned __int8)(*(unsigned __int64 *)(result + 24))) == 0) goto loc_0020388A;
    if ((*(unsigned __int64 *)(v_stack_p8 + 168)) == (v_stack_p8 + 168)) goto loc_0020388A;
    goto loc_00203896;
loc_002038FC:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14430646)))) & (64)) == 0) goto loc_0020368B;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, (unsigned __int8)(*(unsigned __int64 *)(result + 24)), 0, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0020368B;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rdi)), (unsigned __int8)(*(unsigned __int64 *)(result + 24)), 0, a4);
    goto loc_0020368D;
loc_00203923:
    if (1 != 0) goto loc_00203802;
    a3 = 0;
    result = KiComputeDueTime(v_stack_p8 + 256, *(unsigned __int64 *)(v_stack_p8 + 280), a3, v_stack_p70);
    if ((unsigned int)(result) == 0) goto loc_002039DF;
    a3 = 0;
    result = KiInsertTimerTable(a2, v_stack_p8 + 256, a3, (unsigned int)(v_stack_p70));
    if ((unsigned __int8)(result) == 0) goto loc_00203A00;
    if (condition_is_below) goto loc_00203A2F;
loc_0020398E:
    goto loc_00203802;
loc_00203998:
    if ((unsigned __int8)(v_stack_p8 + 256) == 0) goto loc_00203868;
loc_002039A2:
loc_002039A4:
    goto loc_002038AF;
loc_002039AC:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 120)))) & (16)) != 0) goto loc_002039A4;
    goto loc_002038AF;
loc_002039B8:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14430458)))) & (64)) == 0) goto loc_0020381B;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned __int8)((unsigned __int8)(a2)), (unsigned __int8)(a2), a3, (unsigned int)(v_stack_p70));
    if ((unsigned __int8)(result) == 0) goto loc_0020381B;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), (unsigned __int8)(a2), a3, (unsigned int)(v_stack_p70));
    goto loc_0020381D;
loc_002039DF:
    v_rdi = 0;
    goto loc_00203802;
loc_002039E9:
    if (((unsigned __int8)((unsigned int)((unsigned int)(v_rsi)))) == 4) goto loc_00203A13;
    goto loc_002036E1;
loc_002039F6:
    goto loc_00203896;
loc_00203A00:
    a3 = 0;
    result = KiTimerWaitTest(a2, 0, a3, (unsigned int)(v_stack_p70));
    goto loc_0020398E;
loc_00203A13:
    *(unsigned __int8 *)(result + 17) = 5;
    result = KeInsertQueueDpc(*(unsigned __int64 *)(result + 24), v_rsi, result, (unsigned int)(v_stack_p70));
    goto loc_002036C5;
loc_00203A2F:
    a2 = 0;
    result = KiTraceSetTimer(0, a2, 1, (unsigned int)(v_stack_p70));
    goto loc_0020398E;
}
```

## 5. (Beta) C Style

```c
int64_t KiResumeThread(void *Arg1, int64_t Arg2, uint8_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p70;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    local_rsp = (local_rsp) - (48);
    local_rdi = 0;
    *(uint32_t *)(arg1 + 0x2E4) = 1;
loc_00203674:
    if (condition_is_above_or_equal) goto loc_00203698;
loc_0020367D:
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((*(uint32_t *)(v_rip + 0xDC1C27)) & ((uint32_t)(local_rdi))) == 0) goto loc_002038FC;
loc_0020368B:
loc_0020368D:
    if (*(uint64_t *)(arg1 + 0x40) == 0) goto loc_00203674;
    goto loc_0020367D;
loc_00203698:
    if ((*(uint8_t *)(arg1 + 0x184)) == 5) goto loc_00203734;
loc_002036A5:
    if (Arg3 != 0) goto loc_002036F1;
loc_002036AF:
    *(uint64_t *)(arg1 + 0x40) = 0;
loc_002036C5:
    if ((*(uint64_t *)(arg1 + 0x2E0 + 0x8)) == (Arg1 + 736 + 8)) goto loc_00203715;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x2E0 + 0x8) + 0x10))) != 1) goto loc_0020386C;
loc_002036E1:
    Arg4 = 0;
    result = KiTryUnwaitThread(Arg2, *(uint64_t *)(arg1 + 0x2E0 + 0x8), *(uint16_t *)(*(uint64_t *)(arg1 + 0x2E0 + 0x8) + 0x12), Arg4);
    goto loc_002036C5;
loc_002036F1:
    if (condition_is_below) goto loc_002037C3;
    Arg4 = 0;
    result = KiSignalThreadForApc(Arg2, Arg1 + 736 + 8 + 648, 2, Arg4);
    goto loc_002036AF;
loc_00203715:
    *(void **)(arg1 + 0x2E0 + 0x8 + 0x8) = Arg1 + 736 + 8;
    *(void **)(arg1 + 0x2E0 + 0x8) = Arg1 + 736 + 8;
    local_rsp = (local_rsp) + (48);
    return result;
loc_00203734:
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x70))) & (7));
    if (((uint8_t)(result)) != 4) goto loc_002036A5;
    if (Arg3 != 0) goto loc_002038AF;
    Arg1 = (uint8_t)((*(uint8_t *)(v_stack_p8 + 0x70)) & (253));
    Arg1 = (uint8_t)((Arg1) | (5));
    *(uint8_t *)(v_stack_p8 + 0x70) = (uint8_t)(Arg1);
    local_rbp = 0;
    *(uint64_t *)(v_stack_p8 + 0x40) = 0;
loc_00203767:
    if (0 >= ((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x24B)))) goto loc_002037F5;
    local_rdi = (0 + 0 * 2) << (4);
    local_rdi = (local_rdi) + (*(uint64_t *)(v_stack_p8 + 0xD0));
    if ((*(uint8_t *)(local_rdi + 0x11)) != 6) goto loc_002038D2;
    *(uint8_t *)(local_rdi + 0x11) = 4;
    result = KiAcquireKobjectLockSafe(*(uint64_t *)(local_rdi + 0x20), Arg1 + 736 + 8 + 648, 2, Arg4);
    if ((*(uint32_t *)(*(uint64_t *)(local_rdi + 0x20) + 0x4)) > 0) goto loc_002037E7;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(local_rdi + 0x20))) & (127));
    if (((uint8_t)(result)) == 2) goto loc_002037E7;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0x20) + 0x8 + 0x8))) == (*(uint64_t *)(local_rdi + 0x20) + 8)) goto loc_002038BD;
loc_002037C3:
    if (((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x184))) != 5) goto loc_002036AF;
    Arg4 = 0;
    result = KiSignalThread(Arg2, v_stack_p8, 0, Arg4);
    goto loc_002036AF;
loc_002037E7:
    *(uint8_t *)(local_rdi + 0x11) = 5;
loc_002037F5:
    local_rdi = 0;
    if (condition_is_below) goto loc_00203923;
loc_00203802:
    local_rsi = 0;
loc_00203804:
    if (condition_is_above_or_equal) goto loc_00203828;
loc_0020380D:
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (((*(uint32_t *)(v_rip + 0xDC1A97)) & ((uint32_t)(local_rsi))) == 0) goto loc_002039B8;
loc_0020381B:
loc_0020381D:
    if (*(uint64_t *)(v_stack_p8 + 0x40) == 0) goto loc_00203804;
    goto loc_0020380D;
loc_00203828:
    local_rdi = (uint32_t)((local_rdi) << (9));
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x74)))));
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x70))) & (231));
    *(uint32_t *)(v_stack_p8 + 0x74) = (uint32_t)(local_rdi);
    if (((uint8_t)(result)) != 5) goto loc_002039A4;
    local_rdi = (uint32_t)((local_rdi) >> (4));
    if ((((uint8_t)(local_rdi)) & (1)) != 0) goto loc_002038DA;
    if (((*(uint8_t *)(v_stack_p8 + 0xC2)) & (2)) != 0) goto loc_00203998;
loc_00203868:
    goto loc_002038A0;
loc_0020386C:
    if (((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x70))) != 2) goto loc_002039E9;
    *(uint8_t *)(result + 0x11) = 5;
    result = KiInsertQueueInternal(*(uint64_t *)(result + 0x18), result, 0, Arg4);
    goto loc_002036C5;
loc_0020388A:
    if ((*(uint8_t *)(v_stack_p8 + 0x72)) != 0) goto loc_002039F6;
    result = 0;
loc_00203896:
    if (0 != 0) goto loc_002039A2;
loc_002038A0:
    if ((*(uint8_t *)(v_stack_p8 + 0x283)) == 37) goto loc_002039AC;
loc_002038AF:
    Arg1 = (uint8_t)(((uint8_t)((uint8_t)(*(uint64_t *)(result + 0x18)))) & (249));
    Arg1 = (uint8_t)((Arg1) | (1));
    *(uint8_t *)(v_stack_p8 + 0x70) = (uint8_t)(Arg1);
    goto loc_002036A5;
loc_002038BD:
    *(uint64_t *)(local_rdi) = 0;
    *(void **)(local_rdi + 0x8) = Arg1;
    *(uint64_t *)(arg1) = local_rdi;
    *(uint64_t *)(result + 0x8) = local_rdi;
loc_002038D2:
    local_rbp = (uint8_t)((local_rbp) + 1);
    goto loc_00203767;
loc_002038DA:
    if ((*(uint8_t *)((uint8_t)(*(uint64_t *)(result + 0x18)) + v_stack_p8 * 1 + 0x72)) != 0) goto loc_002039F6;
    if ((uint8_t)((uint8_t)(*(uint64_t *)(result + 0x18))) == 0) goto loc_0020388A;
    if ((*(uint64_t *)(v_stack_p8 + 0xA8)) == (v_stack_p8 + 168)) goto loc_0020388A;
    goto loc_00203896;
loc_002038FC:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xDC31B6)))) & (64)) == 0) goto loc_0020368B;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, (uint8_t)(*(uint64_t *)(result + 0x18)), 0, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0020368B;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rdi)), (uint8_t)(*(uint64_t *)(result + 0x18)), 0, Arg4);
    goto loc_0020368D;
loc_00203923:
    if (1 != 0) goto loc_00203802;
    Arg3 = 0;
    result = KiComputeDueTime(v_stack_p8 + 256, *(uint64_t *)(v_stack_p8 + 0x118), Arg3, v_stack_p70);
    if ((uint32_t)(result) == 0) goto loc_002039DF;
    Arg3 = 0;
    result = KiInsertTimerTable(Arg2, v_stack_p8 + 256, Arg3, (uint32_t)(v_stack_p70));
    if ((uint8_t)(result) == 0) goto loc_00203A00;
    if (condition_is_below) goto loc_00203A2F;
loc_0020398E:
    goto loc_00203802;
loc_00203998:
    if ((uint8_t)(v_stack_p8 + 256) == 0) goto loc_00203868;
loc_002039A2:
loc_002039A4:
    goto loc_002038AF;
loc_002039AC:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x78)))) & (16)) != 0) goto loc_002039A4;
    goto loc_002038AF;
loc_002039B8:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xDC30FA)))) & (64)) == 0) goto loc_0020381B;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint8_t)((uint8_t)(Arg2)), (uint8_t)(Arg2), Arg3, (uint32_t)(v_stack_p70));
    if ((uint8_t)(result) == 0) goto loc_0020381B;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), (uint8_t)(Arg2), Arg3, (uint32_t)(v_stack_p70));
    goto loc_0020381D;
loc_002039DF:
    local_rdi = 0;
    goto loc_00203802;
loc_002039E9:
    if (((uint8_t)((uint32_t)((uint32_t)(local_rsi)))) == 4) goto loc_00203A13;
    goto loc_002036E1;
loc_002039F6:
    goto loc_00203896;
loc_00203A00:
    Arg3 = 0;
    result = KiTimerWaitTest(Arg2, 0, Arg3, (uint32_t)(v_stack_p70));
    goto loc_0020398E;
loc_00203A13:
    *(uint8_t *)(result + 0x11) = 5;
    result = KeInsertQueueDpc(*(uint64_t *)(result + 0x18), local_rsi, result, (uint32_t)(v_stack_p70));
    goto loc_002036C5;
loc_00203A2F:
    Arg2 = 0;
    result = KiTraceSetTimer(0, Arg2, 1, (uint32_t)(v_stack_p70));
    goto loc_0020398E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x4` | `32` | `R/W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R/W` |
| `Arg1` | `+ 0x40` | `64` | `W` |
| `Arg1` | `+ 0x70` | `8` | `R` |
| `Arg1` | `+ 0x70` | `8` | `W` |
| `Arg1` | `+ 0x72` | `8` | `R` |
| `Arg1` | `+ 0x74` | `32` | `R` |
| `Arg1` | `+ 0x74` | `32` | `W` |
| `Arg1` | `+ 0x78` | `32` | `R` |
| `Arg1` | `+ 0xA8` | `64` | `R` |
| `Arg1` | `+ 0xC2` | `8` | `R` |
| `Arg1` | `+ 0xD0` | `64` | `R` |
| `Arg1` | `+ 0x100` | `64` | `R` |
| `Arg1` | `+ 0x118` | `64` | `R` |
| `Arg1` | `+ 0x184` | `8` | `R` |
| `Arg1` | `+ 0x187` | `8` | `R` |
| `Arg1` | `+ 0x24B` | `8` | `R` |
| `Arg1` | `+ 0x283` | `8` | `R` |
| `Arg1` | `+ 0x288` | `64` | `R` |
| `Arg1` | `+ 0x2E0` | `64` | `R` |
| `Arg1` | `+ 0x2E4` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00203644&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
