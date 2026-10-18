# CcFlushCachePostProcessOneRange

- RVA: `0x00359710`–`0x00359C88` (길이 `1,400` bytes)
- VA: `0x0000000140359710`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000798C8`
- 디코드: `319`개 명령, `1,400/1,400` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00359806` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003598F5` → [CcUnpinFileDataEx](CcUnpinFileDataEx_function_00359DEC.md) (function, `0x00359DEC`)
- `0x00359904` → [CcSetDirtyPinnedData](CcSetDirtyPinnedData_function_0035A120.md) (function, `0x0035A120`)
- `0x00359911` → [CcUnpinFileDataEx](CcUnpinFileDataEx_function_00359DEC.md) (function, `0x00359DEC`)
- `0x00359947` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x00359A19` → [CcPostDeferredWrites](CcPostDeferredWrites_function_003590FC.md) (function, `0x003590FC`)
- `0x00359A55` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00359A64` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x00359AC1` → [CcSetDirtyInMask](../3C/CcSetDirtyInMask_function_003CB688.md) (function, `0x003CB688`)
- `0x00359AE6` → [CcIsFatalWriteError](../40/CcIsFatalWriteError_function_0040855C.md) (function, `0x0040855C`)
- `0x00359B68` → [MmFlushSection](../23/MmFlushSection_function_002375E4.md) (function, `0x002375E4`)
- `0x00359B95` → [CcIsFatalWriteError](../40/CcIsFatalWriteError_function_0040855C.md) (function, `0x0040855C`)
- `0x00359BE4` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x00359BF8` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x00359C1B` → [CcPerfLogFlushSection](../47/CcPerfLogFlushSection_function_0047CE0C.md) (function, `0x0047CE0C`)
- `0x00359C64` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00359C82` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [CcWriteBehindAsync](CcWriteBehindAsync_function_003549E8.md) at `0x00354AE7`
- [CcWriteBehindInternal](CcWriteBehindInternal_function_00357540.md) at `0x0035763A`
- [CcFlushCachePriv](CcFlushCachePriv_function_0035B040.md) at `0x0035B17A`
- [CcAsyncLazywriteWorkerMulti](../4D/CcAsyncLazywriteWorkerMulti_function_004D1574.md) at `0x004D19C8`
- [CcWriteBehindAsyncFlushOneRange](../57/CcWriteBehindAsyncFlushOneRange_function_0057FAEC.md) at `0x0057FB47`

### Static image references
- `0x003597C7` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x003597D4` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x00359931` → RVA `0x00F0DE58` (`.data`; read)
- `0x0035995E` → RVA `0x00F8F570` (`.data`; read)
- `0x00359B30` → RVA `0x00FC6B10` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00359710  40 53                           push rbx
00359712  55                              push rbp
00359713  56                              push rsi
00359714  57                              push rdi
00359715  41 54                           push r12
00359717  41 55                           push r13
00359719  41 56                           push r14
0035971B  41 57                           push r15
0035971D  48 83 EC 78                     sub rsp, 0x78
00359721  4C 8B 21                        mov r12, qword ptr [rcx]
00359724  48 8D 71 3C                     lea rsi, [rcx + 0x3c]
00359728  4C 8B 69 70                     mov r13, qword ptr [rcx + 0x70]
0035972C  33 C0                           xor eax, eax
0035972E  83 3E 00                        cmp dword ptr [rsi], 0
00359731  0F 57 C0                        xorps xmm0, xmm0
00359734  48 8B 69 10                     mov rbp, qword ptr [rcx + 0x10]
00359738  48 8B F9                        mov rdi, rcx
0035973B  44 0F B6 B1 84 00 00 00         movzx r14d, byte ptr [rcx + 0x84]
00359743  4C 8B 79 18                     mov r15, qword ptr [rcx + 0x18]
00359747  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0035974C  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00359750  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00359755  0F B6 81 85 00 00 00            movzx eax, byte ptr [rcx + 0x85]
0035975C  88 84 24 C0 00 00 00            mov byte ptr [rsp + 0xc0], al
00359763  48 8B 41 60                     mov rax, qword ptr [rcx + 0x60]
00359767  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0035976C  8B 41 68                        mov eax, dword ptr [rcx + 0x68]
0035976F  B9 02 00 00 00                  mov ecx, 2
00359774  89 84 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], eax
0035977B  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
00359780  4C 89 64 24 48                  mov qword ptr [rsp + 0x48], r12
00359785  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
0035978A  0F 85 C1 01 00 00               jne 0x140359951
00359790  41 8B 55 00                     mov edx, dword ptr [r13]
00359794  85 D2                           test edx, edx
00359796  0F 88 34 03 00 00               js 0x140359ad0
0035979C  F7 85 98 00 00 00 00 04 00 00   test dword ptr [rbp + 0x98], 0x400
003597A6  75 67                           jne 0x14035980f
003597A8  49 8D 9C 24 00 03 00 00         lea rbx, [r12 + 0x300]
003597B0  48 C7 44 24 58 00 00 00 00      mov qword ptr [rsp + 0x58], 0
003597B9  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
003597BE  90                              nop
003597BF  44 0F 20 C6                     mov rsi, cr8
003597C3  44 0F 22 C1                     mov cr8, rcx
003597C7  83 3D 52 D5 C6 00 00            cmp dword ptr [rip + 0xc6d552], 0
003597CE  0F 85 7A 02 00 00               jne 0x140359a4e
003597D4  F6 05 2B D3 C6 00 21            test byte ptr [rip + 0xc6d32b], 0x21
003597DB  40 88 74 24 68                  mov byte ptr [rsp + 0x68], sil
003597E0  0F 85 4B 01 00 00               jne 0x140359931
003597E6  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
003597EB  48 87 13                        xchg qword ptr [rbx], rdx
003597EE  48 85 D2                        test rdx, rdx
003597F1  0F 85 68 02 00 00               jne 0x140359a5f
003597F7  81 8D 98 00 00 00 00 04 00 00   or dword ptr [rbp + 0x98], 0x400
00359801  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00359806  E8 D5 94 FE FF                  call 0x140342ce0
0035980B  48 8D 77 3C                     lea rsi, [rdi + 0x3c]
0035980F  45 84 F6                        test r14b, r14b
00359812  74 1B                           je 0x14035982f
00359814  65 FF 04 25 6C 89 00 00         inc dword ptr gs:[0x896c]
0035981C  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
0035981F  05 FF 0F 00 00                  add eax, 0xfff
00359824  C1 E8 0C                        shr eax, 0xc
00359827  65 01 04 25 70 89 00 00         add dword ptr gs:[0x8970], eax
0035982F  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
00359832  05 FF 0F 00 00                  add eax, 0xfff
00359837  C1 E8 0C                        shr eax, 0xc
0035983A  01 87 F8 00 00 00               add dword ptr [rdi + 0xf8], eax
00359840  83 3E 00                        cmp dword ptr [rsi], 0
00359843  0F 85 08 01 00 00               jne 0x140359951
00359849  83 7F 40 00                     cmp dword ptr [rdi + 0x40], 0
0035984D  0F 85 FE 00 00 00               jne 0x140359951
00359853  45 32 E4                        xor r12b, r12b
00359856  48 8B 77 78                     mov rsi, qword ptr [rdi + 0x78]
0035985A  33 DB                           xor ebx, ebx
0035985C  44 8B 7F 30                     mov r15d, dword ptr [rdi + 0x30]
00359860  48 85 F6                        test rsi, rsi
00359863  75 57                           jne 0x1403598bc
00359865  45 84 E4                        test r12b, r12b
00359868  0F 85 00 02 00 00               jne 0x140359a6e
0035986E  44 8B 4F 30                     mov r9d, dword ptr [rdi + 0x30]
00359872  44 8B 47 34                     mov r8d, dword ptr [rdi + 0x34]
00359876  4C 01 8F E0 00 00 00            add qword ptr [rdi + 0xe0], r9
0035987D  45 03 C1                        add r8d, r9d
00359880  44 89 47 34                     mov dword ptr [rdi + 0x34], r8d
00359884  41 81 F8 00 00 04 00            cmp r8d, 0x40000
0035988B  0F 83 6E 01 00 00               jae 0x1403599ff
00359891  45 84 F6                        test r14b, r14b
00359894  0F 85 13 01 00 00               jne 0x1403599ad
0035989A  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
0035989F  4D 85 C0                        test r8, r8
003598A2  0F 85 27 01 00 00               jne 0x1403599cf
003598A8  80 BF C9 00 00 00 00            cmp byte ptr [rdi + 0xc9], 0
003598AF  0F 85 75 01 00 00               jne 0x140359a2a
003598B5  B0 01                           mov al, 1
003598B7  E9 DF 00 00 00                  jmp 0x14035999b
003598BC  B8 FD 02 00 00                  mov eax, 0x2fd
003598C1  66 39 06                        cmp word ptr [rsi], ax
003598C4  0F 85 A0 03 00 00               jne 0x140359c6a
003598CA  44 8B E8                        mov r13d, eax
003598CD  4C 8B 7E 10                     mov r15, qword ptr [rsi + 0x10]
003598D1  66 44 39 2E                     cmp word ptr [rsi], r13w
003598D5  75 3F                           jne 0x140359916
003598D7  8B 95 98 00 00 00               mov edx, dword ptr [rbp + 0x98]
003598DD  48 8B 5E 08                     mov rbx, qword ptr [rsi + 8]
003598E1  0F BA E2 09                     bt edx, 9
003598E5  73 13                           jae 0x1403598fa
003598E7  D1 EA                           shr edx, 1
003598E9  41 B8 02 00 00 00               mov r8d, 2
003598EF  80 E2 01                        and dl, 1
003598F2  48 8B CE                        mov rcx, rsi
003598F5  E8 F2 04 00 00                  call 0x140359dec
003598FA  45 84 E4                        test r12b, r12b
003598FD  74 0A                           je 0x140359909
003598FF  33 D2                           xor edx, edx
00359901  48 8B CE                        mov rcx, rsi
00359904  E8 17 08 00 00                  call 0x14035a120
00359909  45 33 C0                        xor r8d, r8d
0035990C  B2 01                           mov dl, 1
0035990E  48 8B CE                        mov rcx, rsi
00359911  E8 D6 04 00 00                  call 0x140359dec
00359916  48 C7 C0 F0 FF FF FF            mov rax, 0xfffffffffffffff0
0035991D  49 8D 34 07                     lea rsi, [r15 + rax]
00359921  48 39 5F 28                     cmp qword ptr [rdi + 0x28], rbx
00359925  75 A6                           jne 0x1403598cd
00359927  4C 8B 6C 24 38                  mov r13, qword ptr [rsp + 0x38]
0035992C  E9 3D FF FF FF                  jmp 0x14035986e
00359931  8B 05 21 45 BB 00               mov eax, dword ptr [rip + 0xbb4521]
00359937  85 C0                           test eax, eax
00359939  0F 85 A7 FE FF FF               jne 0x1403597e6
0035993F  48 8B D3                        mov rdx, rbx
00359942  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00359947  E8 04 BF F1 FF                  call 0x140275850
0035994C  E9 A6 FE FF FF                  jmp 0x1403597f7
00359951  41 B4 01                        mov r12b, 1
00359954  E9 FD FE FF FF                  jmp 0x140359856
00359959  B8 CD CC CC CC                  mov eax, 0xcccccccd
0035995E  F7 25 0C 5C C3 00               mul dword ptr [rip + 0xc35c0c]
00359964  C1 EA 03                        shr edx, 3
00359967  8B C2                           mov eax, edx
00359969  48 03 87 98 00 00 00            add rax, qword ptr [rdi + 0x98]
00359970  48 89 87 A0 00 00 00            mov qword ptr [rdi + 0xa0], rax
00359977  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
00359981  48 8B 00                        mov rax, qword ptr [rax]
00359984  48 3B 87 A0 00 00 00            cmp rax, qword ptr [rdi + 0xa0]
0035998B  0F 8E 09 FF FF FF               jle 0x14035989a
00359991  49 C7 45 08 5E 8A 00 00         mov qword ptr [r13 + 8], 0x8a5e
00359999  32 C0                           xor al, al
0035999B  48 83 C4 78                     add rsp, 0x78
0035999F  41 5F                           pop r15
003599A1  41 5E                           pop r14
003599A3  41 5D                           pop r13
003599A5  41 5C                           pop r12
003599A7  5F                              pop rdi
003599A8  5E                              pop rsi
003599A9  5D                              pop rbp
003599AA  5B                              pop rbx
003599AB  C3                              ret
003599AC  CC                              int3
003599AD  80 BC 24 C0 00 00 00 00         cmp byte ptr [rsp + 0xc0], 0
003599B5  0F 85 DF FE FF FF               jne 0x14035989a
003599BB  48 8B 87 B8 00 00 00            mov rax, qword ptr [rdi + 0xb8]
003599C2  48 39 00                        cmp qword ptr [rax], rax
003599C5  74 92                           je 0x140359959
003599C7  8B 05 A3 5B C3 00               mov eax, dword ptr [rip + 0xc35ba3]
003599CD  EB 9A                           jmp 0x140359969
003599CF  8B 57 30                        mov edx, dword ptr [rdi + 0x30]
003599D2  48 03 57 28                     add rdx, qword ptr [rdi + 0x28]
003599D6  48 89 57 28                     mov qword ptr [rdi + 0x28], rdx
003599DA  49 8B 08                        mov rcx, qword ptr [r8]
003599DD  44 8B 84 24 D8 00 00 00         mov r8d, dword ptr [rsp + 0xd8]
003599E5  4A 8D 04 01                     lea rax, [rcx + r8]
003599E9  48 3B C2                        cmp rax, rdx
003599EC  7E AB                           jle 0x140359999
003599EE  2B CA                           sub ecx, edx
003599F0  48 89 57 20                     mov qword ptr [rdi + 0x20], rdx
003599F4  41 03 C8                        add ecx, r8d
003599F7  89 4F 30                        mov dword ptr [rdi + 0x30], ecx
003599FA  E9 A9 FE FF FF                  jmp 0x1403598a8
003599FF  48 8B 87 B8 00 00 00            mov rax, qword ptr [rdi + 0xb8]
00359A06  48 39 00                        cmp qword ptr [rax], rax
00359A09  0F 84 82 FE FF FF               je 0x140359891
00359A0F  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
00359A14  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00359A19  E8 DE F6 FF FF                  call 0x1403590fc
00359A1E  C7 47 34 00 00 00 00            mov dword ptr [rdi + 0x34], 0
00359A25  E9 67 FE FF FF                  jmp 0x140359891
00359A2A  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
00359A2D  48 01 87 D0 00 00 00            add qword ptr [rdi + 0xd0], rax
00359A34  48 8B 87 E0 00 00 00            mov rax, qword ptr [rdi + 0xe0]
00359A3B  48 C1 E8 0C                     shr rax, 0xc
00359A3F  48 3B 87 D8 00 00 00            cmp rax, qword ptr [rdi + 0xd8]
00359A46  0F 92 C0                        setb al
00359A49  E9 4D FF FF FF                  jmp 0x14035999b
00359A4E  0F B6 D1                        movzx edx, cl
00359A51  40 0F B6 CE                     movzx ecx, sil
00359A55  E8 A2 BC 19 00                  call 0x1404f56fc
00359A5A  E9 75 FD FF FF                  jmp 0x1403597d4
00359A5F  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00359A64  E8 47 E4 EF FF                  call 0x140257eb0
00359A69  E9 89 FD FF FF                  jmp 0x1403597f7
00359A6E  48 8B 5F 28                     mov rbx, qword ptr [rdi + 0x28]
00359A72  48 89 9C 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rbx
00359A7A  45 85 FF                        test r15d, r15d
00359A7D  0F 84 EB FD FF FF               je 0x14035986e
00359A83  41 8B CF                        mov ecx, r15d
00359A86  48 8B C3                        mov rax, rbx
00359A89  48 FF C9                        dec rcx
00359A8C  48 25 00 00 00 FE               and rax, 0xfffffffffe000000
00359A92  48 03 CB                        add rcx, rbx
00359A95  48 81 E1 00 00 00 FE            and rcx, 0xfffffffffe000000
00359A9C  48 3B C1                        cmp rax, rcx
00359A9F  72 5A                           jb 0x140359afb
00359AA1  41 8B F7                        mov esi, r15d
00359AA4  45 33 C9                        xor r9d, r9d
00359AA7  81 FE 00 00 00 02               cmp esi, 0x2000000
00359AAD  0F 87 97 01 00 00               ja 0x140359c4a
00359AB3  44 8B C6                        mov r8d, esi
00359AB6  48 8D 94 24 C8 00 00 00         lea rdx, [rsp + 0xc8]
00359ABE  48 8B CD                        mov rcx, rbp
00359AC1  E8 C2 1B 07 00                  call 0x1403cb688
00359AC6  8B C6                           mov eax, esi
00359AC8  48 03 D8                        add rbx, rax
00359ACB  44 2B FE                        sub r15d, esi
00359ACE  EB A2                           jmp 0x140359a72
00359AD0  48 8B 5F 28                     mov rbx, qword ptr [rdi + 0x28]
00359AD4  48 8B CD                        mov rcx, rbp
00359AD7  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
00359ADA  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
00359ADF  89 84 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], eax
00359AE6  E8 71 EA 0A 00                  call 0x14040855c
00359AEB  84 C0                           test al, al
00359AED  75 1C                           jne 0x140359b0b
00359AEF  C7 47 40 01 00 00 00            mov dword ptr [rdi + 0x40], 1
00359AF6  E9 45 FD FF FF                  jmp 0x140359840
00359AFB  8D B3 FF FF FF 01               lea esi, [rbx + 0x1ffffff]
00359B01  81 E6 00 00 00 FE               and esi, 0xfe000000
00359B07  2B F3                           sub esi, ebx
00359B09  EB 99                           jmp 0x140359aa4
00359B0B  8B B4 24 C8 00 00 00            mov esi, dword ptr [rsp + 0xc8]
00359B12  41 0F B6 C6                     movzx eax, r14b
00359B16  F6 D8                           neg al
00359B18  1B C0                           sbb eax, eax
00359B1A  25 16 00 00 80                  and eax, 0x80000016
00359B1F  89 84 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], eax
00359B26  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
00359B30  F7 05 D6 CF C6 00 00 00 02 00   test dword ptr [rip + 0xc6cfd6], 0x20000
00359B3A  0F 85 BF 00 00 00               jne 0x140359bff
00359B40  8B 84 24 D0 00 00 00            mov eax, dword ptr [rsp + 0xd0]
00359B47  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00359B4C  41 89 45 00                     mov dword ptr [r13], eax
00359B50  45 33 C9                        xor r9d, r9d
00359B53  8B 47 38                        mov eax, dword ptr [rdi + 0x38]
00359B56  41 B8 00 10 00 00               mov r8d, 0x1000
00359B5C  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00359B60  49 8B CF                        mov rcx, r15
00359B63  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00359B68  E8 77 DA ED FF                  call 0x1402375e4
00359B6D  85 C0                           test eax, eax
00359B6F  79 19                           jns 0x140359b8a
00359B71  41 8B 4D 00                     mov ecx, dword ptr [r13]
00359B75  45 84 F6                        test r14b, r14b
00359B78  0F 84 A7 00 00 00               je 0x140359c25
00359B7E  81 F9 16 00 00 80               cmp ecx, 0x80000016
00359B84  0F 84 A3 00 00 00               je 0x140359c2d
00359B8A  41 8B 55 00                     mov edx, dword ptr [r13]
00359B8E  85 D2                           test edx, edx
00359B90  79 45                           jns 0x140359bd7
00359B92  48 8B CD                        mov rcx, rbp
00359B95  E8 C2 E9 0A 00                  call 0x14040855c
00359B9A  8B 8F 80 00 00 00               mov ecx, dword ptr [rdi + 0x80]
00359BA0  84 C0                           test al, al
00359BA2  0F 84 8E 00 00 00               je 0x140359c36
00359BA8  85 C9                           test ecx, ecx
00359BAA  75 0A                           jne 0x140359bb6
00359BAC  41 8B 45 00                     mov eax, dword ptr [r13]
00359BB0  89 87 80 00 00 00               mov dword ptr [rdi + 0x80], eax
00359BB6  48 81 C3 00 10 00 00            add rbx, 0x1000
00359BBD  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
00359BC2  81 C6 00 F0 FF FF               add esi, 0xfffff000
00359BC8  0F 85 62 FF FF FF               jne 0x140359b30
00359BCE  48 8D 77 3C                     lea rsi, [rdi + 0x3c]
00359BD2  E9 69 FC FF FF                  jmp 0x140359840
00359BD7  49 8D 8C 24 00 03 00 00         lea rcx, [r12 + 0x300]
00359BDF  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
00359BE4  E8 B7 BB F1 FF                  call 0x1402757a0
00359BE9  81 8D 98 00 00 00 00 04 00 00   or dword ptr [rbp + 0x98], 0x400
00359BF3  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00359BF8  E8 E3 90 FE FF                  call 0x140342ce0
00359BFD  EB B7                           jmp 0x140359bb6
00359BFF  8B 47 38                        mov eax, dword ptr [rdi + 0x38]
00359C02  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
00359C07  48 8B 8F B0 00 00 00            mov rcx, qword ptr [rdi + 0xb0]
00359C0E  41 B9 00 10 00 00               mov r9d, 0x1000
00359C14  48 8B D5                        mov rdx, rbp
00359C17  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00359C1B  E8 EC 31 12 00                  call 0x14047ce0c
00359C20  E9 1B FF FF FF                  jmp 0x140359b40
00359C25  85 C9                           test ecx, ecx
00359C27  0F 85 5D FF FF FF               jne 0x140359b8a
00359C2D  41 89 45 00                     mov dword ptr [r13], eax
00359C31  E9 54 FF FF FF                  jmp 0x140359b8a
00359C36  C7 47 40 01 00 00 00            mov dword ptr [rdi + 0x40], 1
00359C3D  85 C9                           test ecx, ecx
00359C3F  0F 85 71 FF FF FF               jne 0x140359bb6
00359C45  E9 62 FF FF FF                  jmp 0x140359bac
00359C4A  BA 5F 15 00 00                  mov edx, 0x155f
00359C4F  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
00359C58  B9 34 00 00 00                  mov ecx, 0x34
00359C5D  49 C7 C0 20 04 00 C0            mov r8, 0xffffffffc0000420
00359C64  E8 F7 39 1A 00                  call 0x1404fd660
00359C69  CC                              int3
00359C6A  45 33 C9                        xor r9d, r9d
00359C6D  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00359C72  BA 72 15 00 00                  mov edx, 0x1572
00359C77  49 C7 C0 20 04 00 C0            mov r8, 0xffffffffc0000420
00359C7E  41 8D 49 34                     lea ecx, [r9 + 0x34]
00359C82  E8 D9 39 1A 00                  call 0x1404fd660
00359C87  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcFlushCachePostProcessOneRange(__int64 a1)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p58;
    unsigned __int8 v_stack_p8;
    unsigned __int8 v_stack_pC0;
    unsigned __int64 v_stack_pC8;
    unsigned int v_stack_pD0;
    unsigned int v_stack_pD8;

    v_rsp = (v_rsp) - (120);
    result = 0;
    v_stack_m50 = 0;
    v_stack_m78 = *(unsigned __int64 *)(a1 + 8);
    v_stack_p8 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 133));
    v_stack_m68 = *(unsigned __int64 *)(a1 + 96);
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 104)));
    v_stack_m60 = v_xmm0;
    v_stack_m70 = *(unsigned __int64 *)(a1);
    v_stack_m80 = *(unsigned __int64 *)(a1 + 112);
    if ((*(unsigned int *)(a1 + 60)) != 0) goto loc_00359951;
    if (sign_flag) goto loc_00359AD0;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 152)) & (0x400ULL)) != 0) goto loc_0035980F;
    v_stack_m60 = 0;
    v_stack_m58 = *(unsigned __int64 *)(a1) + 768;
    if ((*(unsigned int *)(v_rip + 13030738)) != 0) goto loc_00359A4E;
loc_003597D4:
    v_stack_m50 = (unsigned __int8)(v_cr8);
    if (((*(unsigned __int8 *)(v_rip + 13030187)) & (33)) != 0) goto loc_00359931;
loc_003597E6:
    if (v_stack_m60 != 0) goto loc_00359A5F;
loc_003597F7:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m60, v_stack_m60, a3, a4);
loc_0035980F:
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 132)) != 0) {
        result = *(unsigned int *)(a1 + 48);
        result = (unsigned int)((result) + (0xFFFULL));
        result = (unsigned int)((result) >> (12));
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 48))) + (0xFFFULL));
    result = (unsigned int)((result) >> (12));
loc_00359840:
    if ((*(unsigned int *)(a1 + 60)) != 0) goto loc_00359951;
    if ((*(unsigned int *)(a1 + 64)) != 0) goto loc_00359951;
    v_r12 = 0;
loc_00359856:
    v_rbx = 0;
    if (*(unsigned __int64 *)(a1 + 120) != 0) goto loc_003598BC;
    if (0 != 0) goto loc_00359A6E;
loc_0035986E:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 52))) + ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))));
    *(unsigned int *)(a1 + 52) = (unsigned int)(a3);
    if (((unsigned int)(a3)) >= 0x40000ULL) goto loc_003599FF;
loc_00359891:
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 132)) != 0) goto loc_003599AD;
loc_0035989A:
    if (v_stack_m68 != 0) goto loc_003599CF;
loc_003598A8:
    if ((*(unsigned __int8 *)(a1 + 201)) != 0) goto loc_00359A2A;
    goto loc_0035999B;
loc_003598BC:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 120))) != 765) goto loc_00359C6A;
loc_003598CD:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 120))) != 765) goto loc_00359916;
    result = 765;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 120))) < 765) {
        a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 152))) >> (1));
        a3 = 2;
        a2 = (unsigned __int8)((a2) & (1));
        a1 = *(unsigned __int64 *)(a1 + 120);
        result = CcUnpinFileDataEx(a1, a2, a3, (unsigned int)(*(unsigned int *)(a1 + 48)));
    }
    if (0 != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(a1 + 120);
        result = CcSetDirtyPinnedData(a1, a2, a3, (unsigned int)(*(unsigned int *)(a1 + 48)));
    }
    a3 = 0;
    result = CcUnpinFileDataEx(*(unsigned __int64 *)(a1 + 120), 1, a3, (unsigned int)(*(unsigned int *)(a1 + 48)));
loc_00359916:
    if ((*(unsigned __int64 *)(a1 + 40)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 120) + 8))) goto loc_003598CD;
    goto loc_0035986E;
loc_00359931:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12272929))) != 0) goto loc_003597E6;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_m60, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 120) + 8), a3, (unsigned int)(*(unsigned int *)(a1 + 48)));
    goto loc_003597F7;
loc_00359951:
    goto loc_00359856;
loc_00359959:
    a2 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 120) + 8)) >> (3));
loc_00359969:
    result = ((unsigned int)((unsigned int)(a2))) + (*(unsigned __int64 *)(a1 + 152));
    *(unsigned __int64 *)(a1 + 160) = result;
    if ((*(unsigned __int64 *)(result)) <= (*(unsigned __int64 *)(a1 + 160))) goto loc_0035989A;
    *(unsigned __int64 *)(v_stack_m80 + 8) = 0x8A5EULL;
loc_00359999:
    result = 0;
loc_0035999B:
    v_rsp = (v_rsp) + (120);
    return result;
loc_003599AD:
    if (v_stack_pC0 != 0) goto loc_0035989A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184))) == (*(unsigned __int64 *)(a1 + 184))) goto loc_00359959;
    goto loc_00359969;
loc_003599CF:
    a2 = ((unsigned int)(*(unsigned int *)(a1 + 48))) + (*(unsigned __int64 *)(a1 + 40));
    *(unsigned __int64 *)(a1 + 40) = a2;
    if ((*(unsigned __int64 *)(a3) + (unsigned int)(v_stack_pD8) * 1) <= a2) goto loc_00359999;
    a1 = (unsigned int)((*(unsigned __int64 *)(a3)) - ((unsigned int)(a2)));
    *(unsigned __int64 *)(a1 + 32) = a2;
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned int)(v_stack_pD8))));
    *(unsigned int *)(a1 + 48) = (unsigned int)(a1);
    goto loc_003598A8;
loc_003599FF:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184))) == (*(unsigned __int64 *)(a1 + 184))) goto loc_00359891;
    result = CcPostDeferredWrites(v_stack_p48, v_stack_p40, (unsigned int)(v_stack_pD8), (unsigned int)(*(unsigned int *)(a1 + 48)));
    *(unsigned int *)(a1 + 52) = 0;
    goto loc_00359891;
loc_00359A2A:
    result = (*(unsigned __int64 *)(a1 + 224)) >> (12);
    result = (result < (*(unsigned __int64 *)(a1 + 216))) ? 1 : 0;
    goto loc_0035999B;
loc_00359A4E:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 120) + 16) + -16 * 1), (unsigned __int8)(v_stack_p48), (unsigned int)(v_stack_pD8), (unsigned int)(*(unsigned int *)(a1 + 48)));
    goto loc_003597D4;
loc_00359A5F:
    result = KxWaitForLockOwnerShip(v_stack_p58, (unsigned __int8)(v_stack_p48), (unsigned int)(v_stack_pD8), (unsigned int)(*(unsigned int *)(a1 + 48)));
    goto loc_003597F7;
loc_00359A6E:
loc_00359A72:
    v_stack_pC8 = *(unsigned __int64 *)(a1 + 40);
    if ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 120) + 16)) == 0) goto loc_0035986E;
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 120) + 16)))) - 1;
    result = (*(unsigned __int64 *)(a1 + 40)) & (0xFFFFFFFFFE000000ULL);
    a1 = (a1) + (*(unsigned __int64 *)(a1 + 40));
    a1 = (a1) & (0xFFFFFFFFFE000000ULL);
    if (result < a1) goto loc_00359AFB;
loc_00359AA4:
    a4 = 0;
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 120) + 16))))) > 0x2000000ULL) goto loc_00359C4A;
    result = CcSetDirtyInMask(*(unsigned __int64 *)(a1 + 16), v_stack_pC8, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 120) + 16))))), a4);
    v_rbx = (*(unsigned __int64 *)(a1 + 40)) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 120) + 16))))));
    v_r15 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 120) + 16)) - ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 120) + 16))))));
    goto loc_00359A72;
loc_00359AD0:
    v_stack_p30 = *(unsigned __int64 *)(a1 + 40);
    v_stack_pC8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)));
    result = CcIsFatalWriteError(*(unsigned __int64 *)(a1 + 16), v_stack_pC8, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 120) + 16))))), a4);
    if ((unsigned __int8)(result) != 0) goto loc_00359B0B;
    *(unsigned int *)(a1 + 64) = 1;
    goto loc_00359840;
loc_00359AFB:
    v_rsi = (unsigned int)((*(unsigned __int64 *)(a1 + 40) + 33554431) & (0xFE000000ULL));
    v_rsi = (unsigned int)((v_rsi) - ((unsigned int)(*(unsigned __int64 *)(a1 + 40))));
    goto loc_00359AA4;
loc_00359B0B:
    result = (unsigned __int8)(-((unsigned __int8)(*(unsigned __int8 *)(a1 + 132))));
    result = (unsigned int)((result) & (0x80000016ULL));
    v_stack_pD0 = (unsigned int)(result);
loc_00359B30:
    if (((*(unsigned int *)(v_rip + 13029334)) & (0x20000ULL)) != 0) goto loc_00359BFF;
loc_00359B40:
    *(unsigned int *)(v_stack_m80) = (unsigned int)((unsigned int)(v_stack_pD0));
    a4 = 0;
    v_stack_p28 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 56)));
    v_stack_p20 = v_stack_m80;
    result = MmFlushSection(v_r15, v_stack_p30, (unsigned int)(0x1000ULL), a4);
    if (!sign_flag) goto loc_00359B8A;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 132)) == 0) goto loc_00359C25;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m80)))) == 0x80000016ULL) goto loc_00359C2D;
loc_00359B8A:
    if (!sign_flag) goto loc_00359BD7;
    result = CcIsFatalWriteError(*(unsigned __int64 *)(a1 + 16), (unsigned int)(*(unsigned int *)(v_stack_m80)), (unsigned int)(0x1000ULL), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00359C36;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 128))) == 0) {
        result = *(unsigned int *)(v_stack_m80);
        *(unsigned int *)(a1 + 128) = (unsigned int)(result);
    }
    v_rbx = (*(unsigned __int64 *)(a1 + 40)) + (0x1000ULL);
    v_stack_p30 = v_rbx;
    v_rsi = (unsigned int)(((unsigned int)(v_stack_pC8)) + (0xFFFFF000ULL));
    if (condition_is_not_equal) goto loc_00359B30;
    goto loc_00359840;
loc_00359BD7:
    result = KeAcquireInStackQueuedSpinLock(1 + 768, v_stack_p58, (unsigned int)(0x1000ULL), a4);
    result = KeReleaseInStackQueuedSpinLock(v_stack_p58, v_stack_p58, (unsigned int)(0x1000ULL), a4);
    goto loc_00359BB6;
loc_00359BFF:
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 56)));
    result = CcPerfLogFlushSection(*(unsigned __int64 *)(a1 + 176), *(unsigned __int64 *)(a1 + 16), v_stack_p30, (unsigned int)(0x1000ULL));
    goto loc_00359B40;
loc_00359C25:
    if ((unsigned int)(*(unsigned __int64 *)(a1 + 176)) != 0) goto loc_00359B8A;
loc_00359C2D:
    *(unsigned int *)(v_stack_m80) = (unsigned int)(result);
    goto loc_00359B8A;
loc_00359C36:
    *(unsigned int *)(a1 + 64) = 1;
    if ((unsigned int)(*(unsigned __int64 *)(a1 + 176)) != 0) goto loc_00359BB6;
    goto loc_00359BAC;
loc_00359C4A:
    v_stack_p20 = 0;
    result = KeBugCheckEx(52, (unsigned int)(0x155FULL), 0xFFFFFFFFC0000420ULL, (unsigned int)(0x1000ULL));
loc_00359C6A:
    a4 = 0;
    v_stack_p20 = v_rbx;
    result = KeBugCheckEx(a4 + 52, (unsigned int)(0x1572ULL), 0xFFFFFFFFC0000420ULL, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CcFlushCachePostProcessOneRange(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p58;
    uint8_t v_stack_p8;
    uint8_t v_stack_pC0;
    uint64_t v_stack_pC8;
    uint32_t v_stack_pD0;
    uint32_t v_stack_pD8;

    local_rsp = (local_rsp) - (120);
    result = 0;
    v_stack_m50 = 0;
    v_stack_m78 = *(uint64_t *)(arg1 + 0x8);
    v_stack_p8 = (uint8_t)(*(uint8_t *)(arg1 + 0x85));
    v_stack_m68 = *(uint64_t *)(arg1 + 0x60);
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x68)));
    v_stack_m60 = v_xmm0;
    v_stack_m70 = *(uint64_t *)(arg1);
    v_stack_m80 = *(uint64_t *)(arg1 + 0x70);
    if ((*(uint32_t *)(arg1 + 0x3C)) != 0) goto loc_00359951;
    if (sign_flag) goto loc_00359AD0;
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x98)) & (0x400ULL)) != 0) goto loc_0035980F;
    v_stack_m60 = 0;
    v_stack_m58 = *(uint64_t *)(arg1) + 768;
    if ((*(uint32_t *)(v_rip + 0xC6D552)) != 0) goto loc_00359A4E;
loc_003597D4:
    v_stack_m50 = (uint8_t)(v_cr8);
    if (((*(uint8_t *)(v_rip + 0xC6D32B)) & (33)) != 0) goto loc_00359931;
loc_003597E6:
    if (v_stack_m60 != 0) goto loc_00359A5F;
loc_003597F7:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m60, v_stack_m60, a3, a4);
loc_0035980F:
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x84)) != 0) {
        result = *(uint32_t *)(arg1 + 0x30);
        result = (uint32_t)((result) + (0xFFFULL));
        result = (uint32_t)((result) >> (12));
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x30))) + (0xFFFULL));
    result = (uint32_t)((result) >> (12));
loc_00359840:
    if ((*(uint32_t *)(arg1 + 0x3C)) != 0) goto loc_00359951;
    if ((*(uint32_t *)(arg1 + 0x40)) != 0) goto loc_00359951;
    local_r12 = 0;
loc_00359856:
    local_rbx = 0;
    if (*(uint64_t *)(arg1 + 0x78) != 0) goto loc_003598BC;
    if (0 != 0) goto loc_00359A6E;
loc_0035986E:
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x34))) + ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))));
    *(uint32_t *)(arg1 + 0x34) = (uint32_t)(a3);
    if (((uint32_t)(a3)) >= 0x40000ULL) goto loc_003599FF;
loc_00359891:
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x84)) != 0) goto loc_003599AD;
loc_0035989A:
    if (v_stack_m68 != 0) goto loc_003599CF;
loc_003598A8:
    if ((*(uint8_t *)(arg1 + 0xC9)) != 0) goto loc_00359A2A;
    goto loc_0035999B;
loc_003598BC:
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x78))) != 765) goto loc_00359C6A;
loc_003598CD:
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x78))) != 765) goto loc_00359916;
    result = 765;
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x78))) < 765) {
        a2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x98))) >> (1));
        a3 = 2;
        a2 = (uint8_t)((a2) & (1));
        Arg1 = *(uint64_t *)(arg1 + 0x78);
        result = CcUnpinFileDataEx(Arg1, a2, a3, (uint32_t)(*(uint32_t *)(arg1 + 0x30)));
    }
    if (0 != 0) {
        a2 = 0;
        Arg1 = *(uint64_t *)(arg1 + 0x78);
        result = CcSetDirtyPinnedData(Arg1, a2, a3, (uint32_t)(*(uint32_t *)(arg1 + 0x30)));
    }
    a3 = 0;
    result = CcUnpinFileDataEx(*(uint64_t *)(arg1 + 0x78), 1, a3, (uint32_t)(*(uint32_t *)(arg1 + 0x30)));
loc_00359916:
    if ((*(uint64_t *)(arg1 + 0x28)) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x78) + 0x8))) goto loc_003598CD;
    goto loc_0035986E;
loc_00359931:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB4521))) != 0) goto loc_003597E6;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_m60, *(uint64_t *)(*(uint64_t *)(arg1 + 0x78) + 0x8), a3, (uint32_t)(*(uint32_t *)(arg1 + 0x30)));
    goto loc_003597F7;
loc_00359951:
    goto loc_00359856;
loc_00359959:
    a2 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(arg1 + 0x78) + 0x8)) >> (3));
loc_00359969:
    result = ((uint32_t)((uint32_t)(a2))) + (*(uint64_t *)(arg1 + 0x98));
    *(uint64_t *)(arg1 + 0xA0) = result;
    if ((*(uint64_t *)(result)) <= (*(uint64_t *)(arg1 + 0xA0))) goto loc_0035989A;
    *(uint64_t *)(v_stack_m80 + 0x8) = 0x8A5EULL;
loc_00359999:
    result = 0;
loc_0035999B:
    local_rsp = (local_rsp) + (120);
    return result;
loc_003599AD:
    if (v_stack_pC0 != 0) goto loc_0035989A;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8))) == (*(uint64_t *)(arg1 + 0xB8))) goto loc_00359959;
    goto loc_00359969;
loc_003599CF:
    a2 = ((uint32_t)(*(uint32_t *)(arg1 + 0x30))) + (*(uint64_t *)(arg1 + 0x28));
    *(uint64_t *)(arg1 + 0x28) = a2;
    if ((*(uint64_t *)(a3) + (uint32_t)(v_stack_pD8) * 1) <= a2) goto loc_00359999;
    Arg1 = (uint32_t)((*(uint64_t *)(a3)) - ((uint32_t)(a2)));
    *(uint64_t *)(arg1 + 0x20) = a2;
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint32_t)(v_stack_pD8))));
    *(uint32_t *)(arg1 + 0x30) = (uint32_t)(Arg1);
    goto loc_003598A8;
loc_003599FF:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8))) == (*(uint64_t *)(arg1 + 0xB8))) goto loc_00359891;
    result = CcPostDeferredWrites(v_stack_p48, v_stack_p40, (uint32_t)(v_stack_pD8), (uint32_t)(*(uint32_t *)(arg1 + 0x30)));
    *(uint32_t *)(arg1 + 0x34) = 0;
    goto loc_00359891;
loc_00359A2A:
    result = (*(uint64_t *)(arg1 + 0xE0)) >> (12);
    result = (result < (*(uint64_t *)(arg1 + 0xD8))) ? 1 : 0;
    goto loc_0035999B;
loc_00359A4E:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x78) + 0x10) + -16 * 1), (uint8_t)(v_stack_p48), (uint32_t)(v_stack_pD8), (uint32_t)(*(uint32_t *)(arg1 + 0x30)));
    goto loc_003597D4;
loc_00359A5F:
    result = KxWaitForLockOwnerShip(v_stack_p58, (uint8_t)(v_stack_p48), (uint32_t)(v_stack_pD8), (uint32_t)(*(uint32_t *)(arg1 + 0x30)));
    goto loc_003597F7;
loc_00359A6E:
loc_00359A72:
    v_stack_pC8 = *(uint64_t *)(arg1 + 0x28);
    if ((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x78) + 0x10)) == 0) goto loc_0035986E;
    Arg1 = ((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x78) + 0x10)))) - 1;
    result = (*(uint64_t *)(arg1 + 0x28)) & (0xFFFFFFFFFE000000ULL);
    Arg1 = (Arg1) + (*(uint64_t *)(arg1 + 0x28));
    Arg1 = (Arg1) & (0xFFFFFFFFFE000000ULL);
    if (result < Arg1) goto loc_00359AFB;
loc_00359AA4:
    a4 = 0;
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x78) + 0x10))))) > 0x2000000ULL) goto loc_00359C4A;
    result = CcSetDirtyInMask(*(uint64_t *)(arg1 + 0x10), v_stack_pC8, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x78) + 0x10))))), a4);
    local_rbx = (*(uint64_t *)(arg1 + 0x28)) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x78) + 0x10))))));
    local_r15 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(arg1 + 0x78) + 0x10)) - ((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x78) + 0x10))))));
    goto loc_00359A72;
loc_00359AD0:
    v_stack_p30 = *(uint64_t *)(arg1 + 0x28);
    v_stack_pC8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)));
    result = CcIsFatalWriteError(*(uint64_t *)(arg1 + 0x10), v_stack_pC8, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x78) + 0x10))))), a4);
    if ((uint8_t)(result) != 0) goto loc_00359B0B;
    *(uint32_t *)(arg1 + 0x40) = 1;
    goto loc_00359840;
loc_00359AFB:
    local_rsi = (uint32_t)((*(uint64_t *)(arg1 + 0x28) + 33554431) & (0xFE000000ULL));
    local_rsi = (uint32_t)((local_rsi) - ((uint32_t)(*(uint64_t *)(arg1 + 0x28))));
    goto loc_00359AA4;
loc_00359B0B:
    result = (uint8_t)(-((uint8_t)(*(uint8_t *)(arg1 + 0x84))));
    result = (uint32_t)((result) & (0x80000016ULL));
    v_stack_pD0 = (uint32_t)(result);
loc_00359B30:
    if (((*(uint32_t *)(v_rip + 0xC6CFD6)) & (0x20000ULL)) != 0) goto loc_00359BFF;
loc_00359B40:
    *(uint32_t *)(v_stack_m80) = (uint32_t)((uint32_t)(v_stack_pD0));
    a4 = 0;
    v_stack_p28 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)));
    v_stack_p20 = v_stack_m80;
    result = MmFlushSection(local_r15, v_stack_p30, (uint32_t)(0x1000ULL), a4);
    if (!sign_flag) goto loc_00359B8A;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x84)) == 0) goto loc_00359C25;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m80)))) == 0x80000016ULL) goto loc_00359C2D;
loc_00359B8A:
    if (!sign_flag) goto loc_00359BD7;
    result = CcIsFatalWriteError(*(uint64_t *)(arg1 + 0x10), (uint32_t)(*(uint32_t *)(v_stack_m80)), (uint32_t)(0x1000ULL), a4);
    if ((uint8_t)(result) == 0) goto loc_00359C36;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x80))) == 0) {
        result = *(uint32_t *)(v_stack_m80);
        *(uint32_t *)(arg1 + 0x80) = (uint32_t)(result);
    }
    local_rbx = (*(uint64_t *)(arg1 + 0x28)) + (0x1000ULL);
    v_stack_p30 = local_rbx;
    local_rsi = (uint32_t)(((uint32_t)(v_stack_pC8)) + (0xFFFFF000ULL));
    if (condition_is_not_equal) goto loc_00359B30;
    goto loc_00359840;
loc_00359BD7:
    result = KeAcquireInStackQueuedSpinLock(1 + 768, v_stack_p58, (uint32_t)(0x1000ULL), a4);
    result = KeReleaseInStackQueuedSpinLock(v_stack_p58, v_stack_p58, (uint32_t)(0x1000ULL), a4);
    goto loc_00359BB6;
loc_00359BFF:
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)));
    result = CcPerfLogFlushSection(*(uint64_t *)(arg1 + 0xB0), *(uint64_t *)(arg1 + 0x10), v_stack_p30, (uint32_t)(0x1000ULL));
    goto loc_00359B40;
loc_00359C25:
    if ((uint32_t)(*(uint64_t *)(arg1 + 0xB0)) != 0) goto loc_00359B8A;
loc_00359C2D:
    *(uint32_t *)(v_stack_m80) = (uint32_t)(result);
    goto loc_00359B8A;
loc_00359C36:
    *(uint32_t *)(arg1 + 0x40) = 1;
    if ((uint32_t)(*(uint64_t *)(arg1 + 0xB0)) != 0) goto loc_00359BB6;
    goto loc_00359BAC;
loc_00359C4A:
    v_stack_p20 = 0;
    result = KeBugCheckEx(52, (uint32_t)(0x155FULL), 0xFFFFFFFFC0000420ULL, (uint32_t)(0x1000ULL));
loc_00359C6A:
    a4 = 0;
    v_stack_p20 = local_rbx;
    result = KeBugCheckEx(a4 + 52, (uint32_t)(0x1572ULL), 0xFFFFFFFFC0000420ULL, a4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `W` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `W` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x30` | `32` | `W` |
| `Arg1` | `+ 0x34` | `32` | `R` |
| `Arg1` | `+ 0x34` | `32` | `W` |
| `Arg1` | `+ 0x38` | `32` | `R` |
| `Arg1` | `+ 0x3C` | `64` | `R` |
| `Arg1` | `+ 0x40` | `32` | `R` |
| `Arg1` | `+ 0x40` | `32` | `W` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x68` | `32` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R` |
| `Arg1` | `+ 0x78` | `64` | `R` |
| `Arg1` | `+ 0x80` | `32` | `R` |
| `Arg1` | `+ 0x80` | `32` | `W` |
| `Arg1` | `+ 0x84` | `8` | `R` |
| `Arg1` | `+ 0x85` | `8` | `R` |
| `Arg1` | `+ 0x98` | `64` | `R` |
| `Arg1` | `+ 0xA0` | `64` | `R` |
| `Arg1` | `+ 0xA0` | `64` | `W` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg1` | `+ 0xC9` | `8` | `R` |
| `Arg1` | `+ 0xD0` | `64` | `R/W` |
| `Arg1` | `+ 0xD8` | `64` | `R` |

추가 오프셋 3개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00359710&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
