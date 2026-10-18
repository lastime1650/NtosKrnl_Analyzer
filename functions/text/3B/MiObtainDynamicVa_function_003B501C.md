# MiObtainDynamicVa

- RVA: `0x003B501C`–`0x003B598B` (길이 `2,415` bytes)
- VA: `0x00000001403B501C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008C610`
- 디코드: `647`개 명령, `2,415/2,415` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x003B50A7` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x003B50C9` → [MiExtendDynamicBitMap](MiExtendDynamicBitMap_function_003B6934.md) (function, `0x003B6934`)
- `0x003B50D6` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x003B52AA` → [RtlSetBitsEx](RtlSetBitsEx_function_003B6570.md) (function, `0x003B6570`)
- `0x003B5316` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x003B53DC` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x003B53EF` → [MiFindNextAlignedForwardRunClearEx](MiFindNextAlignedForwardRunClearEx_function_003B6F78.md) (function, `0x003B6F78`)
- `0x003B5455` → [MiReduceSystemRegionType](MiReduceSystemRegionType_function_003B5FCC.md) (function, `0x003B5FCC`)
- `0x003B5466` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x003B5968` → [MiFindNextAlignedForwardRunClearEx](MiFindNextAlignedForwardRunClearEx_function_003B6F78.md) (function, `0x003B6F78`)

### Direct callers
- [MiReservePoolMemory](MiReservePoolMemory_function_003B4AD8.md) at `0x003B4B12`
- [MiObtainSystemVa](MiObtainSystemVa_function_003B4F44.md) at `0x003B4F5B`

### Static image references
- `0x003B512A` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x003B52D0` → RVA `0x00E2F080` (`.data`; read)
- `0x003B52DC` → RVA `0x00E2EEC8` (`.data`; read)
- `0x003B52ED` → RVA `0x00E2EEC8` (`.data`; write)
- `0x003B5304` → RVA `0x00E38A08` (`.data`; read)
- `0x003B53D3` → RVA `0x00E39680` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x003B5951` → [sub_006E73C4](../6E/Unknown_function_006E73C4.md) (`tail-transfer`)
  - `0x003B597D` → [sub_006E73C4 + 0xC](../6E/Unknown_function_006E73C4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003B501C  48 8B C4                        mov rax, rsp
003B501F  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
003B5023  89 50 10                        mov dword ptr [rax + 0x10], edx
003B5026  48 89 48 08                     mov qword ptr [rax + 8], rcx
003B502A  55                              push rbp
003B502B  53                              push rbx
003B502C  56                              push rsi
003B502D  57                              push rdi
003B502E  41 54                           push r12
003B5030  41 55                           push r13
003B5032  41 56                           push r14
003B5034  41 57                           push r15
003B5036  48 8D 68 A1                     lea rbp, [rax - 0x5f]
003B503A  48 81 EC 98 00 00 00            sub rsp, 0x98
003B5041  0F 57 C0                        xorps xmm0, xmm0
003B5044  41 BD 01 00 00 00               mov r13d, 1
003B504A  49 83 CB FF                     or r11, 0xffffffffffffffff
003B504E  4C 89 6D EF                     mov qword ptr [rbp - 0x11], r13
003B5052  0F 11 45 07                     movups xmmword ptr [rbp + 7], xmm0
003B5056  49 8B FB                        mov rdi, r11
003B5059  41 8B C0                        mov eax, r8d
003B505C  44 8B E2                        mov r12d, edx
003B505F  4C 8B F1                        mov r14, rcx
003B5062  44 0F 20 C3                     mov rbx, cr8
003B5066  48 89 5D F7                     mov qword ptr [rbp - 9], rbx
003B506A  49 8B 4E 18                     mov rcx, qword ptr [r14 + 0x18]
003B506E  83 C0 F6                        add eax, -0xa
003B5071  4C 89 75 E7                     mov qword ptr [rbp - 0x19], r14
003B5075  41 B8 00 02 00 00               mov r8d, 0x200
003B507B  48 89 4D 7F                     mov qword ptr [rbp + 0x7f], rcx
003B507F  4D 8B FE                        mov r15, r14
003B5082  A9 FD FF FF FF                  test eax, 0xfffffffd
003B5087  74 61                           je 0x1403b50ea
003B5089  49 83 3F 00                     cmp qword ptr [r15], 0
003B508D  0F 85 AF 00 00 00               jne 0x1403b5142
003B5093  49 8D 76 40                     lea rsi, [r14 + 0x40]
003B5097  48 89 75 FF                     mov qword ptr [rbp - 1], rsi
003B509B  48 8B CE                        mov rcx, rsi
003B509E  80 FB 02                        cmp bl, 2
003B50A1  0F 84 BB 03 00 00               je 0x1403b5462
003B50A7  E8 E4 35 E9 FF                  call 0x140248690
003B50AC  88 45 7F                        mov byte ptr [rbp + 0x7f], al
003B50AF  49 83 CB FF                     or r11, 0xffffffffffffffff
003B50B3  49 3B FB                        cmp rdi, r11
003B50B6  0F 85 9B 01 00 00               jne 0x1403b5257
003B50BC  44 8B 4D 77                     mov r9d, dword ptr [rbp + 0x77]
003B50C0  45 33 C0                        xor r8d, r8d
003B50C3  49 8B D7                        mov rdx, r15
003B50C6  49 8B CE                        mov rcx, r14
003B50C9  E8 66 18 00 00                  call 0x1403b6934
003B50CE  8A 55 7F                        mov dl, byte ptr [rbp + 0x7f]
003B50D1  48 8B CE                        mov rcx, rsi
003B50D4  8B D8                           mov ebx, eax
003B50D6  E8 E5 31 E9 FF                  call 0x1402482c0
003B50DB  85 DB                           test ebx, ebx
003B50DD  0F 85 04 04 00 00               jne 0x1403b54e7
003B50E3  33 C0                           xor eax, eax
003B50E5  E9 3C 02 00 00                  jmp 0x1403b5326
003B50EA  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
003B50EE  4C 8D 7D 07                     lea r15, [rbp + 7]
003B50F2  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
003B50F6  48 C1 E9 06                     shr rcx, 6
003B50FA  4C 89 7D E7                     mov qword ptr [rbp - 0x19], r15
003B50FE  48 8D 14 C8                     lea rdx, [rax + rcx*8]
003B5102  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
003B5106  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
003B510A  48 89 45 07                     mov qword ptr [rbp + 7], rax
003B510E  48 C1 E8 06                     shr rax, 6
003B5112  48 C1 E0 03                     shl rax, 3
003B5116  48 2B D0                        sub rdx, rax
003B5119  48 89 4D 7F                     mov qword ptr [rbp + 0x7f], rcx
003B511D  48 89 55 0F                     mov qword ptr [rbp + 0xf], rdx
003B5121  45 3B E0                        cmp r12d, r8d
003B5124  0F 82 5F FF FF FF               jb 0x1403b5089
003B512A  48 F7 05 53 19 C1 00 00 00 00 40  test qword ptr [rip + 0xc11953], 0x40000000
003B5135  4D 0F 45 E8                     cmovne r13, r8
003B5139  4C 89 6D EF                     mov qword ptr [rbp - 0x11], r13
003B513D  E9 47 FF FF FF                  jmp 0x1403b5089
003B5142  41 8B F4                        mov esi, r12d
003B5145  49 83 FD 01                     cmp r13, 1
003B5149  0F 85 10 08 00 00               jne 0x1403b595f
003B514F  4D 8B 2F                        mov r13, qword ptr [r15]
003B5152  4D 8B 7F 08                     mov r15, qword ptr [r15 + 8]
003B5156  49 3B CD                        cmp rcx, r13
003B5159  48 1B FF                        sbb rdi, rdi
003B515C  48 23 F9                        and rdi, rcx
003B515F  4D 8D 4D FF                     lea r9, [r13 - 1]
003B5163  45 85 E4                        test r12d, r12d
003B5166  75 11                           jne 0x1403b5179
003B5168  48 83 E7 F8                     and rdi, 0xfffffffffffffff8
003B516C  4C 8B 7D E7                     mov r15, qword ptr [rbp - 0x19]
003B5170  4C 8B 6D EF                     mov r13, qword ptr [rbp - 0x11]
003B5174  E9 1A FF FF FF                  jmp 0x1403b5093
003B5179  44 8B 55 6F                     mov r10d, dword ptr [rbp + 0x6f]
003B517D  4C 8B E7                        mov r12, rdi
003B5180  83 65 A7 00                     and dword ptr [rbp - 0x59], 0
003B5184  49 8B C1                        mov rax, r9
003B5187  49 2B C4                        sub rax, r12
003B518A  48 FF C0                        inc rax
003B518D  48 3B C6                        cmp rax, rsi
003B5190  0F 82 AB 07 00 00               jb 0x1403b5941
003B5196  4D 8B F1                        mov r14, r9
003B5199  41 8A CC                        mov cl, r12b
003B519C  4C 2B F6                        sub r14, rsi
003B519F  80 E1 3F                        and cl, 0x3f
003B51A2  49 FF C6                        inc r14
003B51A5  41 B8 01 00 00 00               mov r8d, 1
003B51AB  49 D3 E0                        shl r8, cl
003B51AE  49 8B C6                        mov rax, r14
003B51B1  48 C1 E8 06                     shr rax, 6
003B51B5  49 FF C8                        dec r8
003B51B8  49 8D 1C C7                     lea rbx, [r15 + rax*8]
003B51BC  49 8B C4                        mov rax, r12
003B51BF  48 C1 E8 06                     shr rax, 6
003B51C3  49 8D 14 C7                     lea rdx, [r15 + rax*8]
003B51C7  4C 0B 02                        or r8, qword ptr [rdx]
003B51CA  48 83 FE 7F                     cmp rsi, 0x7f
003B51CE  0F 87 12 04 00 00               ja 0x1403b55e6
003B51D4  BF 40 00 00 00                  mov edi, 0x40
003B51D9  48 3B F7                        cmp rsi, rdi
003B51DC  0F 83 9A 03 00 00               jae 0x1403b557c
003B51E2  48 83 FE 01                     cmp rsi, 1
003B51E6  0F 87 84 02 00 00               ja 0x1403b5470
003B51EC  4D 3B C3                        cmp r8, r11
003B51EF  75 2B                           jne 0x1403b521c
003B51F1  48 83 C2 08                     add rdx, 8
003B51F5  48 3B D3                        cmp rdx, rbx
003B51F8  76 58                           jbe 0x1403b5252
003B51FA  49 8B FB                        mov rdi, r11
003B51FD  48 8B 4D 7F                     mov rcx, qword ptr [rbp + 0x7f]
003B5201  4D 85 E4                        test r12, r12
003B5204  74 3B                           je 0x1403b5241
003B5206  4C 8D 0C 0E                     lea r9, [rsi + rcx]
003B520A  4D 3B CD                        cmp r9, r13
003B520D  4D 0F 47 CD                     cmova r9, r13
003B5211  49 FF C9                        dec r9
003B5214  45 33 E4                        xor r12d, r12d
003B5217  E9 64 FF FF FF                  jmp 0x1403b5180
003B521C  49 F7 D0                        not r8
003B521F  48 8B FA                        mov rdi, rdx
003B5222  49 2B FF                        sub rdi, r15
003B5225  49 0F BC C0                     bsf rax, r8
003B5229  48 C1 FF 03                     sar rdi, 3
003B522D  48 C1 E7 06                     shl rdi, 6
003B5231  89 45 A7                        mov dword ptr [rbp - 0x59], eax
003B5234  48 03 F8                        add rdi, rax
003B5237  49 3B FE                        cmp rdi, r14
003B523A  77 BE                           ja 0x1403b51fa
003B523C  49 3B FB                        cmp rdi, r11
003B523F  74 BC                           je 0x1403b51fd
003B5241  4C 8B 75 67                     mov r14, qword ptr [rbp + 0x67]
003B5245  44 8B 65 6F                     mov r12d, dword ptr [rbp + 0x6f]
003B5249  48 8B 5D F7                     mov rbx, qword ptr [rbp - 9]
003B524D  E9 1A FF FF FF                  jmp 0x1403b516c
003B5252  4C 8B 02                        mov r8, qword ptr [rdx]
003B5255  EB 95                           jmp 0x1403b51ec
003B5257  41 8B DC                        mov ebx, r12d
003B525A  49 83 FD 01                     cmp r13, 1
003B525E  0F 85 82 01 00 00               jne 0x1403b53e6
003B5264  4D 8B 2F                        mov r13, qword ptr [r15]
003B5267  4D 8B 67 08                     mov r12, qword ptr [r15 + 8]
003B526B  49 3B FD                        cmp rdi, r13
003B526E  4D 1B F6                        sbb r14, r14
003B5271  4C 23 F7                        and r14, rdi
003B5274  49 8D 55 FF                     lea rdx, [r13 - 1]
003B5278  48 85 DB                        test rbx, rbx
003B527B  0F 85 BA 00 00 00               jne 0x1403b533b
003B5281  49 8B FE                        mov rdi, r14
003B5284  48 83 E7 F8                     and rdi, 0xfffffffffffffff8
003B5288  44 8B 65 6F                     mov r12d, dword ptr [rbp + 0x6f]
003B528C  4C 8B 75 67                     mov r14, qword ptr [rbp + 0x67]
003B5290  41 8B DC                        mov ebx, r12d
003B5293  4C 8B 6D EF                     mov r13, qword ptr [rbp - 0x11]
003B5297  48 83 FF FF                     cmp rdi, -1
003B529B  0F 84 1B FE FF FF               je 0x1403b50bc
003B52A1  4C 8B C3                        mov r8, rbx
003B52A4  48 8B D7                        mov rdx, rdi
003B52A7  49 8B CF                        mov rcx, r15
003B52AA  E8 C1 12 00 00                  call 0x1403b6570
003B52AF  44 8B 6D 77                     mov r13d, dword ptr [rbp + 0x77]
003B52B3  41 8D 45 F6                     lea eax, [r13 - 0xa]
003B52B7  A9 FD FF FF FF                  test eax, 0xfffffffd
003B52BC  0F 84 77 01 00 00               je 0x1403b5439
003B52C2  41 83 FC 01                     cmp r12d, 1
003B52C6  75 08                           jne 0x1403b52d0
003B52C8  48 8D 47 01                     lea rax, [rdi + 1]
003B52CC  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
003B52D0  48 8D 05 A9 9D A7 00            lea rax, [rip + 0xa79da9]
003B52D7  4C 3B F0                        cmp r14, rax
003B52DA  75 25                           jne 0x1403b5301
003B52DC  48 8B 0D E5 9B A7 00            mov rcx, qword ptr [rip + 0xa79be5]
003B52E3  48 8B C3                        mov rax, rbx
003B52E6  48 C1 E0 15                     shl rax, 0x15
003B52EA  48 2B C8                        sub rcx, rax
003B52ED  48 89 0D D4 9B A7 00            mov qword ptr [rip + 0xa79bd4], rcx
003B52F4  48 81 F9 00 00 00 08            cmp rcx, 0x8000000
003B52FB  0F 86 CF 00 00 00               jbe 0x1403b53d0
003B5301  49 63 C5                        movsxd rax, r13d
003B5304  48 8D 0D FD 36 A8 00            lea rcx, [rip + 0xa836fd]
003B530B  F0 48 01 1C C1                  lock add qword ptr [rcx + rax*8], rbx
003B5310  8A 55 7F                        mov dl, byte ptr [rbp + 0x7f]
003B5313  48 8B CE                        mov rcx, rsi
003B5316  E8 A5 2F E9 FF                  call 0x1402482c0
003B531B  48 C1 E7 15                     shl rdi, 0x15
003B531F  49 03 7E 20                     add rdi, qword ptr [r14 + 0x20]
003B5323  48 8B C7                        mov rax, rdi
003B5326  48 81 C4 98 00 00 00            add rsp, 0x98
003B532D  41 5F                           pop r15
003B532F  41 5E                           pop r14
003B5331  41 5D                           pop r13
003B5333  41 5C                           pop r12
003B5335  5F                              pop rdi
003B5336  5E                              pop rsi
003B5337  5B                              pop rbx
003B5338  5D                              pop rbp
003B5339  C3                              ret
003B533A  CC                              int3
003B533B  83 65 AB 00                     and dword ptr [rbp - 0x55], 0
003B533F  48 8B C2                        mov rax, rdx
003B5342  49 2B C6                        sub rax, r14
003B5345  48 FF C0                        inc rax
003B5348  48 3B C3                        cmp rax, rbx
003B534B  72 65                           jb 0x1403b53b2
003B534D  4C 8B FA                        mov r15, rdx
003B5350  41 8A CE                        mov cl, r14b
003B5353  4C 2B FB                        sub r15, rbx
003B5356  80 E1 3F                        and cl, 0x3f
003B5359  49 FF C7                        inc r15
003B535C  41 B9 01 00 00 00               mov r9d, 1
003B5362  49 D3 E1                        shl r9, cl
003B5365  49 8B C7                        mov rax, r15
003B5368  48 C1 E8 06                     shr rax, 6
003B536C  49 FF C9                        dec r9
003B536F  49 8D 34 C4                     lea rsi, [r12 + rax*8]
003B5373  49 8B C6                        mov rax, r14
003B5376  48 C1 E8 06                     shr rax, 6
003B537A  4D 8D 04 C4                     lea r8, [r12 + rax*8]
003B537E  4D 0B 08                        or r9, qword ptr [r8]
003B5381  48 83 FB 7F                     cmp rbx, 0x7f
003B5385  0F 87 22 03 00 00               ja 0x1403b56ad
003B538B  41 BA 40 00 00 00               mov r10d, 0x40
003B5391  49 3B DA                        cmp rbx, r10
003B5394  0F 83 00 02 00 00               jae 0x1403b559a
003B539A  48 83 FB 01                     cmp rbx, 1
003B539E  0F 87 60 01 00 00               ja 0x1403b5504
003B53A4  4D 3B CB                        cmp r9, r11
003B53A7  75 53                           jne 0x1403b53fc
003B53A9  49 83 C0 08                     add r8, 8
003B53AD  4C 3B C6                        cmp r8, rsi
003B53B0  76 7F                           jbe 0x1403b5431
003B53B2  49 8B D3                        mov rdx, r11
003B53B5  4D 85 F6                        test r14, r14
003B53B8  74 67                           je 0x1403b5421
003B53BA  48 8D 14 3B                     lea rdx, [rbx + rdi]
003B53BE  49 3B D5                        cmp rdx, r13
003B53C1  49 0F 47 D5                     cmova rdx, r13
003B53C5  48 FF CA                        dec rdx
003B53C8  45 33 F6                        xor r14d, r14d
003B53CB  E9 6B FF FF FF                  jmp 0x1403b533b
003B53D0  45 33 C0                        xor r8d, r8d
003B53D3  48 8D 0D A6 42 A8 00            lea rcx, [rip + 0xa842a6]
003B53DA  33 D2                           xor edx, edx
003B53DC  E8 2F 9F F8 FF                  call 0x14033f310
003B53E1  E9 1B FF FF FF                  jmp 0x1403b5301
003B53E6  4D 8B C5                        mov r8, r13
003B53E9  48 8B D3                        mov rdx, rbx
003B53EC  49 8B CF                        mov rcx, r15
003B53EF  E8 84 1B 00 00                  call 0x1403b6f78
003B53F4  48 8B F8                        mov rdi, rax
003B53F7  E9 9B FE FF FF                  jmp 0x1403b5297
003B53FC  49 F7 D1                        not r9
003B53FF  49 8B D0                        mov rdx, r8
003B5402  49 2B D4                        sub rdx, r12
003B5405  49 0F BC C1                     bsf rax, r9
003B5409  48 C1 FA 03                     sar rdx, 3
003B540D  48 C1 E2 06                     shl rdx, 6
003B5411  89 45 AB                        mov dword ptr [rbp - 0x55], eax
003B5414  48 03 D0                        add rdx, rax
003B5417  49 3B D7                        cmp rdx, r15
003B541A  77 96                           ja 0x1403b53b2
003B541C  49 3B D3                        cmp rdx, r11
003B541F  74 94                           je 0x1403b53b5
003B5421  48 8B 75 FF                     mov rsi, qword ptr [rbp - 1]
003B5425  48 8B FA                        mov rdi, rdx
003B5428  4C 8B 7D E7                     mov r15, qword ptr [rbp - 0x19]
003B542C  E9 57 FE FF FF                  jmp 0x1403b5288
003B5431  4D 8B 08                        mov r9, qword ptr [r8]
003B5434  E9 6B FF FF FF                  jmp 0x1403b53a4
003B5439  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
003B543D  49 2B 4E 08                     sub rcx, qword ptr [r14 + 8]
003B5441  48 C1 E1 03                     shl rcx, 3
003B5445  41 83 FC 01                     cmp r12d, 1
003B5449  0F 84 A8 00 00 00               je 0x1403b54f7
003B544F  48 03 F9                        add rdi, rcx
003B5452  41 8B CD                        mov ecx, r13d
003B5455  E8 72 0B 00 00                  call 0x1403b5fcc
003B545A  44 8B E8                        mov r13d, eax
003B545D  E9 6E FE FF FF                  jmp 0x1403b52d0
003B5462  C6 45 7F 11                     mov byte ptr [rbp + 0x7f], 0x11
003B5466  E8 15 3A E9 FF                  call 0x140248e80
003B546B  E9 3F FC FF FF                  jmp 0x1403b50af
003B5470  45 33 D2                        xor r10d, r10d
003B5473  49 C1 E9 06                     shr r9, 6
003B5477  4F 8D 1C CF                     lea r11, [r15 + r9*8]
003B547B  49 83 F8 FF                     cmp r8, -1
003B547F  0F 84 43 01 00 00               je 0x1403b55c8
003B5485  49 0F BC C0                     bsf rax, r8
003B5489  0F 44 C7                        cmove eax, edi
003B548C  89 45 C3                        mov dword ptr [rbp - 0x3d], eax
003B548F  41 8D 0C 02                     lea ecx, [r10 + rax]
003B5493  48 3B CE                        cmp rcx, rsi
003B5496  0F 83 19 01 00 00               jae 0x1403b55b5
003B549C  44 8B 55 6F                     mov r10d, dword ptr [rbp + 0x6f]
003B54A0  4D 8B C8                        mov r9, r8
003B54A3  49 F7 D1                        not r9
003B54A6  49 8B C1                        mov rax, r9
003B54A9  41 8B CA                        mov ecx, r10d
003B54AC  D1 E9                           shr ecx, 1
003B54AE  48 D3 E8                        shr rax, cl
003B54B1  4C 23 C8                        and r9, rax
003B54B4  0F 84 FF 02 00 00               je 0x1403b57b9
003B54BA  44 2B D1                        sub r10d, ecx
003B54BD  41 83 FA 01                     cmp r10d, 1
003B54C1  77 E3                           ja 0x1403b54a6
003B54C3  49 0F BC C1                     bsf rax, r9
003B54C7  89 45 A7                        mov dword ptr [rbp - 0x59], eax
003B54CA  8B F8                           mov edi, eax
003B54CC  44 8B 55 6F                     mov r10d, dword ptr [rbp + 0x6f]
003B54D0  49 2B D7                        sub rdx, r15
003B54D3  48 C1 FA 03                     sar rdx, 3
003B54D7  48 C1 E2 06                     shl rdx, 6
003B54DB  48 03 FA                        add rdi, rdx
003B54DE  49 83 CB FF                     or r11, 0xffffffffffffffff
003B54E2  E9 50 FD FF FF                  jmp 0x1403b5237
003B54E7  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
003B54EA  49 83 CB FF                     or r11, 0xffffffffffffffff
003B54EE  48 8B 5D F7                     mov rbx, qword ptr [rbp - 9]
003B54F2  E9 73 FB FF FF                  jmp 0x1403b506a
003B54F7  48 8D 47 01                     lea rax, [rdi + 1]
003B54FB  49 89 46 30                     mov qword ptr [r14 + 0x30], rax
003B54FF  E9 4B FF FF FF                  jmp 0x1403b544f
003B5504  45 33 D2                        xor r10d, r10d
003B5507  48 C1 EA 06                     shr rdx, 6
003B550B  4D 8D 1C D4                     lea r11, [r12 + rdx*8]
003B550F  49 83 F9 FF                     cmp r9, -1
003B5513  0F 84 76 01 00 00               je 0x1403b568f
003B5519  49 0F BC C1                     bsf rax, r9
003B551D  B9 40 00 00 00                  mov ecx, 0x40
003B5522  0F 44 C1                        cmove eax, ecx
003B5525  89 45 DF                        mov dword ptr [rbp - 0x21], eax
003B5528  41 8D 0C 02                     lea ecx, [r10 + rax]
003B552C  48 3B CB                        cmp rcx, rbx
003B552F  0F 83 8B 00 00 00               jae 0x1403b55c0
003B5535  44 8B 55 6F                     mov r10d, dword ptr [rbp + 0x6f]
003B5539  49 8B D1                        mov rdx, r9
003B553C  48 F7 D2                        not rdx
003B553F  48 8B C2                        mov rax, rdx
003B5542  41 8B CA                        mov ecx, r10d
003B5545  D1 E9                           shr ecx, 1
003B5547  48 D3 E8                        shr rax, cl
003B554A  48 23 D0                        and rdx, rax
003B554D  0F 84 A3 02 00 00               je 0x1403b57f6
003B5553  44 2B D1                        sub r10d, ecx
003B5556  41 83 FA 01                     cmp r10d, 1
003B555A  77 E3                           ja 0x1403b553f
003B555C  48 0F BC C2                     bsf rax, rdx
003B5560  89 45 AB                        mov dword ptr [rbp - 0x55], eax
003B5563  8B D0                           mov edx, eax
003B5565  4D 2B C4                        sub r8, r12
003B5568  49 C1 F8 03                     sar r8, 3
003B556C  49 C1 E0 06                     shl r8, 6
003B5570  49 03 D0                        add rdx, r8
003B5573  49 83 CB FF                     or r11, 0xffffffffffffffff
003B5577  E9 9B FE FF FF                  jmp 0x1403b5417
003B557C  4C 8B CF                        mov r9, rdi
003B557F  4D 85 C0                        test r8, r8
003B5582  0F 89 C1 03 00 00               jns 0x1403b5949
003B5588  48 83 C2 08                     add rdx, 8
003B558C  48 3B D3                        cmp rdx, rbx
003B558F  0F 87 65 FC FF FF               ja 0x1403b51fa
003B5595  4C 8B 02                        mov r8, qword ptr [rdx]
003B5598  EB E5                           jmp 0x1403b557f
003B559A  4D 85 C9                        test r9, r9
003B559D  0F 89 D2 03 00 00               jns 0x1403b5975
003B55A3  49 83 C0 08                     add r8, 8
003B55A7  4C 3B C6                        cmp r8, rsi
003B55AA  0F 87 02 FE FF FF               ja 0x1403b53b2
003B55B0  4D 8B 08                        mov r9, qword ptr [r8]
003B55B3  EB E5                           jmp 0x1403b559a
003B55B5  41 8B FA                        mov edi, r10d
003B55B8  48 F7 DF                        neg rdi
003B55BB  E9 0C FF FF FF                  jmp 0x1403b54cc
003B55C0  41 8B D2                        mov edx, r10d
003B55C3  48 F7 DA                        neg rdx
003B55C6  EB 9D                           jmp 0x1403b5565
003B55C8  48 83 C2 08                     add rdx, 8
003B55CC  48 3B D3                        cmp rdx, rbx
003B55CF  0F 87 0C 02 00 00               ja 0x1403b57e1
003B55D5  4C 8B 02                        mov r8, qword ptr [rdx]
003B55D8  49 83 F8 FF                     cmp r8, -1
003B55DC  74 EA                           je 0x1403b55c8
003B55DE  45 33 D2                        xor r10d, r10d
003B55E1  E9 9F FE FF FF                  jmp 0x1403b5485
003B55E6  41 F6 C6 3F                     test r14b, 0x3f
003B55EA  4C 8D 4B 08                     lea r9, [rbx + 8]
003B55EE  4C 0F 44 CB                     cmove r9, rbx
003B55F2  4D 85 C0                        test r8, r8
003B55F5  0F 84 86 01 00 00               je 0x1403b5781
003B55FB  48 83 C2 08                     add rdx, 8
003B55FF  48 83 3A 00                     cmp qword ptr [rdx], 0
003B5603  75 56                           jne 0x1403b565b
003B5605  83 65 AF 00                     and dword ptr [rbp - 0x51], 0
003B5609  49 0F BD C0                     bsr rax, r8
003B560D  0F 84 29 02 00 00               je 0x1403b583c
003B5613  B9 3F 00 00 00                  mov ecx, 0x3f
003B5618  2B C8                           sub ecx, eax
003B561A  89 4D AF                        mov dword ptr [rbp - 0x51], ecx
003B561D  48 8B FA                        mov rdi, rdx
003B5620  44 8B C1                        mov r8d, ecx
003B5623  49 2B FF                        sub rdi, r15
003B5626  48 C1 FF 03                     sar rdi, 3
003B562A  48 C1 E7 06                     shl rdi, 6
003B562E  49 2B F8                        sub rdi, r8
003B5631  49 3B FE                        cmp rdi, r14
003B5634  0F 87 C0 FB FF FF               ja 0x1403b51fa
003B563A  48 8B C6                        mov rax, rsi
003B563D  49 2B C0                        sub rax, r8
003B5640  48 C1 E8 06                     shr rax, 6
003B5644  4C 8D 04 C2                     lea r8, [rdx + rax*8]
003B5648  48 83 C2 08                     add rdx, 8
003B564C  49 3B D0                        cmp rdx, r8
003B564F  0F 84 FC 00 00 00               je 0x1403b5751
003B5655  48 83 3A 00                     cmp qword ptr [rdx], 0
003B5659  74 ED                           je 0x1403b5648
003B565B  48 8B C2                        mov rax, rdx
003B565E  49 3B D1                        cmp rdx, r9
003B5661  0F 87 93 FB FF FF               ja 0x1403b51fa
003B5667  48 83 C2 08                     add rdx, 8
003B566B  48 83 3A 00                     cmp qword ptr [rdx], 0
003B566F  75 EA                           jne 0x1403b565b
003B5671  48 8B 00                        mov rax, qword ptr [rax]
003B5674  83 65 B3 00                     and dword ptr [rbp - 0x4d], 0
003B5678  4C 0F BD C0                     bsr r8, rax
003B567C  0F 84 C4 01 00 00               je 0x1403b5846
003B5682  B9 3F 00 00 00                  mov ecx, 0x3f
003B5687  41 2B C8                        sub ecx, r8d
003B568A  89 4D B3                        mov dword ptr [rbp - 0x4d], ecx
003B568D  EB 8E                           jmp 0x1403b561d
003B568F  49 83 C0 08                     add r8, 8
003B5693  4C 3B C6                        cmp r8, rsi
003B5696  0F 87 82 01 00 00               ja 0x1403b581e
003B569C  4D 8B 08                        mov r9, qword ptr [r8]
003B569F  49 83 F9 FF                     cmp r9, -1
003B56A3  74 EA                           je 0x1403b568f
003B56A5  45 33 D2                        xor r10d, r10d
003B56A8  E9 6C FE FF FF                  jmp 0x1403b5519
003B56AD  41 F6 C7 3F                     test r15b, 0x3f
003B56B1  4C 8D 56 08                     lea r10, [rsi + 8]
003B56B5  4C 0F 44 D6                     cmove r10, rsi
003B56B9  4D 85 C9                        test r9, r9
003B56BC  0F 84 8E 01 00 00               je 0x1403b5850
003B56C2  49 83 C0 08                     add r8, 8
003B56C6  49 83 38 00                     cmp qword ptr [r8], 0
003B56CA  75 52                           jne 0x1403b571e
003B56CC  83 65 CB 00                     and dword ptr [rbp - 0x35], 0
003B56D0  49 0F BD C1                     bsr rax, r9
003B56D4  0F 84 7D 01 00 00               je 0x1403b5857
003B56DA  B9 3F 00 00 00                  mov ecx, 0x3f
003B56DF  2B C8                           sub ecx, eax
003B56E1  89 4D CB                        mov dword ptr [rbp - 0x35], ecx
003B56E4  49 8B D0                        mov rdx, r8
003B56E7  44 8B C9                        mov r9d, ecx
003B56EA  49 2B D4                        sub rdx, r12
003B56ED  48 C1 FA 03                     sar rdx, 3
003B56F1  48 C1 E2 06                     shl rdx, 6
003B56F5  49 2B D1                        sub rdx, r9
003B56F8  49 3B D7                        cmp rdx, r15
003B56FB  0F 87 B1 FC FF FF               ja 0x1403b53b2
003B5701  48 8B C3                        mov rax, rbx
003B5704  49 2B C1                        sub rax, r9
003B5707  48 C1 E8 06                     shr rax, 6
003B570B  4D 8D 0C C0                     lea r9, [r8 + rax*8]
003B570F  49 83 C0 08                     add r8, 8
003B5713  4D 3B C1                        cmp r8, r9
003B5716  74 70                           je 0x1403b5788
003B5718  49 83 38 00                     cmp qword ptr [r8], 0
003B571C  74 F1                           je 0x1403b570f
003B571E  49 8B C0                        mov rax, r8
003B5721  4D 3B C2                        cmp r8, r10
003B5724  0F 87 88 FC FF FF               ja 0x1403b53b2
003B572A  49 83 C0 08                     add r8, 8
003B572E  49 83 38 00                     cmp qword ptr [r8], 0
003B5732  75 EA                           jne 0x1403b571e
003B5734  48 8B 00                        mov rax, qword ptr [rax]
003B5737  83 65 CF 00                     and dword ptr [rbp - 0x31], 0
003B573B  48 0F BD D0                     bsr rdx, rax
003B573F  0F 84 EA 00 00 00               je 0x1403b582f
003B5745  B9 3F 00 00 00                  mov ecx, 0x3f
003B574A  2B CA                           sub ecx, edx
003B574C  E9 E3 00 00 00                  jmp 0x1403b5834
003B5751  45 8B C2                        mov r8d, r10d
003B5754  44 2B C1                        sub r8d, ecx
003B5757  41 83 E0 3F                     and r8d, 0x3f
003B575B  0F 84 DB FA FF FF               je 0x1403b523c
003B5761  48 8B 02                        mov rax, qword ptr [rdx]
003B5764  48 0F BC C8                     bsf rcx, rax
003B5768  B8 40 00 00 00                  mov eax, 0x40
003B576D  0F 44 C8                        cmove ecx, eax
003B5770  89 4D B7                        mov dword ptr [rbp - 0x49], ecx
003B5773  41 3B C8                        cmp ecx, r8d
003B5776  0F 83 C0 FA FF FF               jae 0x1403b523c
003B577C  E9 DA FE FF FF                  jmp 0x1403b565b
003B5781  33 C9                           xor ecx, ecx
003B5783  E9 95 FE FF FF                  jmp 0x1403b561d
003B5788  44 8B 4D 6F                     mov r9d, dword ptr [rbp + 0x6f]
003B578C  44 2B C9                        sub r9d, ecx
003B578F  41 83 E1 3F                     and r9d, 0x3f
003B5793  0F 84 83 FC FF FF               je 0x1403b541c
003B5799  49 8B 00                        mov rax, qword ptr [r8]
003B579C  48 0F BC C8                     bsf rcx, rax
003B57A0  B8 40 00 00 00                  mov eax, 0x40
003B57A5  0F 44 C8                        cmove ecx, eax
003B57A8  89 4D D3                        mov dword ptr [rbp - 0x2d], ecx
003B57AB  41 3B C9                        cmp ecx, r9d
003B57AE  0F 82 6A FF FF FF               jb 0x1403b571e
003B57B4  E9 63 FC FF FF                  jmp 0x1403b541c
003B57B9  49 3B D3                        cmp rdx, r11
003B57BC  74 23                           je 0x1403b57e1
003B57BE  83 65 C7 00                     and dword ptr [rbp - 0x39], 0
003B57C2  49 0F BD C0                     bsr rax, r8
003B57C6  74 29                           je 0x1403b57f1
003B57C8  41 BA 3F 00 00 00               mov r10d, 0x3f
003B57CE  44 2B D0                        sub r10d, eax
003B57D1  48 83 C2 08                     add rdx, 8
003B57D5  44 89 55 C7                     mov dword ptr [rbp - 0x39], r10d
003B57D9  4C 8B 02                        mov r8, qword ptr [rdx]
003B57DC  E9 9A FC FF FF                  jmp 0x1403b547b
003B57E1  44 8B 55 6F                     mov r10d, dword ptr [rbp + 0x6f]
003B57E5  49 83 CB FF                     or r11, 0xffffffffffffffff
003B57E9  49 8B FB                        mov rdi, r11
003B57EC  E9 0C FA FF FF                  jmp 0x1403b51fd
003B57F1  44 8B D7                        mov r10d, edi
003B57F4  EB DB                           jmp 0x1403b57d1
003B57F6  4D 3B C3                        cmp r8, r11
003B57F9  74 23                           je 0x1403b581e
003B57FB  83 65 E3 00                     and dword ptr [rbp - 0x1d], 0
003B57FF  49 0F BD C1                     bsr rax, r9
003B5803  74 22                           je 0x1403b5827
003B5805  41 BA 3F 00 00 00               mov r10d, 0x3f
003B580B  44 2B D0                        sub r10d, eax
003B580E  49 83 C0 08                     add r8, 8
003B5812  44 89 55 E3                     mov dword ptr [rbp - 0x1d], r10d
003B5816  4D 8B 08                        mov r9, qword ptr [r8]
003B5819  E9 F1 FC FF FF                  jmp 0x1403b550f
003B581E  49 83 CB FF                     or r11, 0xffffffffffffffff
003B5822  E9 8B FB FF FF                  jmp 0x1403b53b2
003B5827  41 BA 40 00 00 00               mov r10d, 0x40
003B582D  EB DF                           jmp 0x1403b580e
003B582F  B9 40 00 00 00                  mov ecx, 0x40
003B5834  89 4D CF                        mov dword ptr [rbp - 0x31], ecx
003B5837  E9 A8 FE FF FF                  jmp 0x1403b56e4
003B583C  B9 40 00 00 00                  mov ecx, 0x40
003B5841  E9 D4 FD FF FF                  jmp 0x1403b561a
003B5846  B9 40 00 00 00                  mov ecx, 0x40
003B584B  E9 3A FE FF FF                  jmp 0x1403b568a
003B5850  33 C9                           xor ecx, ecx
003B5852  E9 8D FE FF FF                  jmp 0x1403b56e4
003B5857  B9 40 00 00 00                  mov ecx, 0x40
003B585C  E9 80 FE FF FF                  jmp 0x1403b56e1
003B5861  48 8B FA                        mov rdi, rdx
003B5864  44 8B C0                        mov r8d, eax
003B5867  49 2B FF                        sub rdi, r15
003B586A  89 45 BB                        mov dword ptr [rbp - 0x45], eax
003B586D  48 C1 FF 03                     sar rdi, 3
003B5871  48 FF C7                        inc rdi
003B5874  48 C1 E7 06                     shl rdi, 6
003B5878  49 2B F8                        sub rdi, r8
003B587B  49 3B FE                        cmp rdi, r14
003B587E  0F 87 76 F9 FF FF               ja 0x1403b51fa
003B5884  48 8B CE                        mov rcx, rsi
003B5887  49 2B C8                        sub rcx, r8
003B588A  0F 84 AC F9 FF FF               je 0x1403b523c
003B5890  48 83 C2 08                     add rdx, 8
003B5894  48 8B 02                        mov rax, qword ptr [rdx]
003B5897  4C 8B C0                        mov r8, rax
003B589A  49 3B C9                        cmp rcx, r9
003B589D  72 19                           jb 0x1403b58b8
003B589F  48 85 C0                        test rax, rax
003B58A2  0F 85 D7 FC FF FF               jne 0x1403b557f
003B58A8  49 2B C9                        sub rcx, r9
003B58AB  0F 84 8B F9 FF FF               je 0x1403b523c
003B58B1  48 83 C2 08                     add rdx, 8
003B58B5  4C 8B 02                        mov r8, qword ptr [rdx]
003B58B8  49 0F BC C0                     bsf rax, r8
003B58BC  41 0F 44 C1                     cmove eax, r9d
003B58C0  89 45 BF                        mov dword ptr [rbp - 0x41], eax
003B58C3  48 3B C1                        cmp rax, rcx
003B58C6  0F 82 B3 FC FF FF               jb 0x1403b557f
003B58CC  E9 6B F9 FF FF                  jmp 0x1403b523c
003B58D1  49 8B D0                        mov rdx, r8
003B58D4  44 8B C8                        mov r9d, eax
003B58D7  49 2B D4                        sub rdx, r12
003B58DA  89 45 D7                        mov dword ptr [rbp - 0x29], eax
003B58DD  48 C1 FA 03                     sar rdx, 3
003B58E1  48 FF C2                        inc rdx
003B58E4  48 C1 E2 06                     shl rdx, 6
003B58E8  49 2B D1                        sub rdx, r9
003B58EB  49 3B D7                        cmp rdx, r15
003B58EE  0F 87 BE FA FF FF               ja 0x1403b53b2
003B58F4  48 8B CB                        mov rcx, rbx
003B58F7  49 2B C9                        sub rcx, r9
003B58FA  0F 84 1C FB FF FF               je 0x1403b541c
003B5900  49 83 C0 08                     add r8, 8
003B5904  49 8B 00                        mov rax, qword ptr [r8]
003B5907  4C 8B C8                        mov r9, rax
003B590A  49 3B CA                        cmp rcx, r10
003B590D  72 19                           jb 0x1403b5928
003B590F  48 85 C0                        test rax, rax
003B5912  0F 85 82 FC FF FF               jne 0x1403b559a
003B5918  49 2B CA                        sub rcx, r10
003B591B  0F 84 FB FA FF FF               je 0x1403b541c
003B5921  49 83 C0 08                     add r8, 8
003B5925  4D 8B 08                        mov r9, qword ptr [r8]
003B5928  49 0F BC C1                     bsf rax, r9
003B592C  41 0F 44 C2                     cmove eax, r10d
003B5930  89 45 DB                        mov dword ptr [rbp - 0x25], eax
003B5933  48 3B C1                        cmp rax, rcx
003B5936  0F 82 5E FC FF FF               jb 0x1403b559a
003B593C  E9 DB FA FF FF                  jmp 0x1403b541c
003B5941  49 8B FB                        mov rdi, r11
003B5944  E9 B8 F8 FF FF                  jmp 0x1403b5201
003B5949  83 65 BB 00                     and dword ptr [rbp - 0x45], 0
003B594D  49 0F BD C8                     bsr rcx, r8
003B5951  0F 85 6D 1A 33 00               jne 0x1406e73c4
003B5957  41 8B C1                        mov eax, r9d
003B595A  E9 02 FF FF FF                  jmp 0x1403b5861
003B595F  4D 8B C5                        mov r8, r13
003B5962  48 8B D6                        mov rdx, rsi
003B5965  49 8B CF                        mov rcx, r15
003B5968  E8 0B 16 00 00                  call 0x1403b6f78
003B596D  48 8B F8                        mov rdi, rax
003B5970  E9 1E F7 FF FF                  jmp 0x1403b5093
003B5975  83 65 D7 00                     and dword ptr [rbp - 0x29], 0
003B5979  49 0F BD C9                     bsr rcx, r9
003B597D  0F 85 4D 1A 33 00               jne 0x1406e73d0
003B5983  41 8B C2                        mov eax, r10d
003B5986  E9 46 FF FF FF                  jmp 0x1403b58d1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiObtainDynamicVa(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;

    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned int *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (152);
    v_r11 = (v_r11) | (-1);
    *(unsigned __int64 *)(v_rsp - 95 - 17) = 1;
    *(unsigned __int64 *)(v_rsp - 95 + 7) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 - 9) = v_cr8;
loc_003B506A:
    result = (unsigned int)(((unsigned int)(a3)) + (-10));
    *(unsigned __int64 *)(v_rsp - 95 - 25) = a1;
    *(unsigned __int64 *)(v_rsp - 95 + 127) = *(unsigned __int64 *)(a1 + 24);
    if ((((unsigned int)(result)) & (0xFFFFFFFDULL)) == 0) goto loc_003B50EA;
loc_003B5089:
    if ((*(unsigned __int64 *)(a1)) != 0) goto loc_003B5142;
loc_003B5093:
    *(unsigned __int64 *)(v_rsp - 95 - 1) = a1 + 64;
    if (((unsigned __int8)(v_cr8)) == 2) goto loc_003B5462;
    result = ExAcquireSpinLockExclusive(a1 + 64, a2, 512, a4);
    *(unsigned __int8 *)(v_rsp - 95 + 127) = (unsigned __int8)(result);
loc_003B50AF:
    v_r11 = (v_r11) | (-1);
    if (v_r11 != v_r11) goto loc_003B5257;
loc_003B50BC:
    a3 = 0;
    result = MiExtendDynamicBitMap(a1, a1, a3, (unsigned int)(*(unsigned int *)(v_rsp - 95 + 119)));
    result = MiReleaseSpinLockExclusive(a1 + 64, *(unsigned __int8 *)(v_rsp - 95 + 127), a3, (unsigned int)(*(unsigned int *)(v_rsp - 95 + 119)));
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_003B54E7;
    result = 0;
    goto loc_003B5326;
loc_003B50EA:
    a1 = (*(unsigned __int64 *)(a1 + 16)) >> (6);
    *(unsigned __int64 *)(v_rsp - 95 - 25) = v_rsp - 95 + 7;
    *(unsigned __int64 *)(v_rsp - 95 + 7) = *(unsigned __int64 *)(a1 + 40);
    result = (*(unsigned __int64 *)(a1 + 40)) >> (6);
    result = (result) << (3);
    a2 = (*(unsigned __int64 *)(a1 + 8) + a1 * 8) - (result);
    *(unsigned __int64 *)(v_rsp - 95 + 127) = *(unsigned __int64 *)(a1 + 48);
    *(unsigned __int64 *)(v_rsp - 95 + 15) = a2;
    if (((unsigned int)((unsigned int)(a2))) < 0) goto loc_003B5089;
    v_r13 = 1;
    if (((*(unsigned __int64 *)(v_rip + 12654931)) & (0x40000000ULL)) != 0) { v_r13 = 0; }
    *(unsigned __int64 *)(v_rsp - 95 - 17) = v_r13;
    goto loc_003B5089;
loc_003B5142:
    if (v_r13 != 1) goto loc_003B595F;
    v_rdi = (v_r11) & (*(unsigned __int64 *)(a1 + 48));
    if ((unsigned int)((unsigned int)(a2)) != 0) goto loc_003B5179;
    v_rdi = (v_rdi) & (-8);
loc_003B516C:
    goto loc_003B5093;
loc_003B5179:
loc_003B5180:
    result = (*(unsigned __int64 *)(v_rsp - 95 + 7) - 1) - (v_rdi);
    result = (result) + 1;
    if (result < ((unsigned int)((unsigned int)((unsigned int)(a2))))) goto loc_003B5941;
    v_r14 = (*(unsigned __int64 *)(v_rsp - 95 + 7) - 1) - ((unsigned int)((unsigned int)((unsigned int)(a2))));
    a1 = (unsigned __int8)(((unsigned __int8)(v_rdi)) & (63));
    v_r14 = (v_r14) + 1;
    a3 = (1) << ((unsigned __int8)(a1));
    result = (v_r14) >> (6);
    a3 = (a3) - 1;
    result = (v_rdi) >> (6);
    a3 = (a3) | (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 25) + result * 8));
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) > 127) goto loc_003B55E6;
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) >= 64) goto loc_003B557C;
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) > 1) goto loc_003B5470;
loc_003B51EC:
    if (a3 != v_r11) goto loc_003B521C;
    a2 = (*(unsigned __int64 *)(v_rsp - 95 - 25) + result * 8) + (8);
    if (a2 <= (*(unsigned __int64 *)(v_rsp - 95 - 25) + result * 8)) goto loc_003B5252;
loc_003B51FA:
loc_003B51FD:
loc_003B5201:
    if (v_rdi == 0) goto loc_003B5241;
    a4 = (unsigned int)((unsigned int)((unsigned int)(a2))) + *(unsigned __int64 *)(v_rsp - 95 + 127) * 1;
    if (((unsigned int)((unsigned int)((unsigned int)(a2))) + *(unsigned __int64 *)(v_rsp - 95 + 127) * 1) > (*(unsigned __int64 *)(v_rsp - 95 - 17))) { a4 = *(unsigned __int64 *)(v_rsp - 95 - 17); }
    a4 = (a4) - 1;
    v_r12 = 0;
    goto loc_003B5180;
loc_003B521C:
    a3 = ~(a3);
    v_rdi = (a2) - (*(unsigned __int64 *)(v_rsp - 95 - 25));
    v_rdi = (v_rdi) >> (3);
    v_rdi = (v_rdi) << (6);
    *(unsigned int *)(v_rsp - 95 - 89) = (unsigned int)(result);
    v_rdi = (v_rdi) + (result);
loc_003B5237:
    if (v_rdi > v_r14) goto loc_003B51FA;
loc_003B523C:
    if (v_rdi == v_r11) goto loc_003B51FD;
loc_003B5241:
    goto loc_003B516C;
loc_003B5252:
    goto loc_003B51EC;
loc_003B5257:
    if ((*(unsigned __int64 *)(v_rsp - 95 - 17)) != 1) goto loc_003B53E6;
    v_r14 = (*(unsigned __int64 *)(v_rsp - 95 + 103)) & (v_rdi);
    if ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111)))) != 0) goto loc_003B533B;
    v_rdi = (v_r14) & (-8);
loc_003B5288:
loc_003B5297:
    if (v_rdi == -1) goto loc_003B50BC;
    result = RtlSetBitsEx(*(unsigned __int64 *)(v_rsp - 95 - 25), v_rdi, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111)))), a4);
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 119)) - 10)) & (0xFFFFFFFDULL)) == 0) goto loc_003B5439;
    result = (unsigned int)(*(unsigned int *)(v_rsp - 95 + 119)) - 10;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111)))) == 1) {
        result = v_rdi + 1;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 24) = result;
    }
    if ((*(unsigned __int64 *)(v_rsp - 95 + 103)) != (v_rip + 10984873)) goto loc_003B5301;
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111))))) << (21);
    a1 = (*(unsigned __int64 *)(v_rip + 10984421)) - (result);
    *(unsigned __int64 *)(v_rip + 10984404) = a1;
    if (a1 <= 0x8000000ULL) goto loc_003B53D0;
loc_003B5301:
    result = MiReleaseSpinLockExclusive((unsigned int)((unsigned int)((unsigned int)(a2))), *(unsigned __int8 *)(v_rsp - 95 + 127), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111)))), a4);
    v_rdi = (v_rdi) << (21);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 32));
loc_003B5326:
    v_rsp = (v_rsp) + (152);
    return v_rdi;
loc_003B533B:
    result = (*(unsigned __int8 *)(v_rsp - 95 + 127)) - (*(unsigned __int64 *)(v_rsp - 95 + 103));
    result = (result) + 1;
    if (result < ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111)))))) goto loc_003B53B2;
    v_r15 = (*(unsigned __int8 *)(v_rsp - 95 + 127)) - ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111)))));
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(v_rsp - 95 + 103))) & (63));
    v_r15 = (v_r15) + 1;
    a4 = (1) << ((unsigned __int8)(a1));
    result = (v_r15) >> (6);
    a4 = (a4) - 1;
    result = (*(unsigned __int64 *)(v_rsp - 95 + 103)) >> (6);
    a4 = (a4) | (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111)) + result * 8));
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111))))) > 127) goto loc_003B56AD;
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111))))) >= 64) goto loc_003B559A;
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111))))) > 1) goto loc_003B5504;
loc_003B53A4:
    if (a4 != v_r11) goto loc_003B53FC;
    a3 = ((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111)) + result * 8) + (8);
    if (a3 <= ((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111)) + result * 8)) goto loc_003B5431;
loc_003B53B2:
loc_003B53B5:
    if (*(unsigned __int64 *)(v_rsp - 95 + 103) == 0) goto loc_003B5421;
    a2 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111)))) + v_rdi * 1;
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111)))) + v_rdi * 1) > ((unsigned int)(*(unsigned int *)(v_rsp - 95 + 119)))) { a2 = (unsigned int)(*(unsigned int *)(v_rsp - 95 + 119)); }
    a2 = (a2) - 1;
    v_r14 = 0;
    goto loc_003B533B;
loc_003B53D0:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(v_rip + 11027110, a2, a3, a4);
    goto loc_003B5301;
loc_003B53E6:
    result = MiFindNextAlignedForwardRunClearEx(v_r15, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111)))), (unsigned int)(*(unsigned int *)(v_rsp - 95 + 119)), a4);
    goto loc_003B5297;
loc_003B53FC:
    a4 = ~(a4);
    a2 = ((unsigned int)(*(unsigned int *)(v_rsp - 95 + 119))) - ((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111)));
    a2 = (a2) >> (3);
    a2 = (a2) << (6);
    *(unsigned int *)(v_rsp - 95 - 85) = (unsigned int)(result);
    a2 = (a2) + (result);
loc_003B5417:
    if (a2 > v_r15) goto loc_003B53B2;
loc_003B541C:
    if (a2 == v_r11) goto loc_003B53B5;
loc_003B5421:
    goto loc_003B5288;
loc_003B5431:
    goto loc_003B53A4;
loc_003B5439:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 25) + 8)) - (*(unsigned __int64 *)(v_r14 + 8));
    a1 = (a1) << (3);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111)))) == 1) goto loc_003B54F7;
loc_003B544F:
    v_rdi = (a2) + (a1);
    result = MiReduceSystemRegionType((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 119)))), a2, (unsigned int)(*(unsigned int *)(v_rsp - 95 + 119)), *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 119))));
    goto loc_003B52D0;
loc_003B5462:
    *(unsigned __int8 *)(v_rsp - 95 + 127) = 17;
    result = ExAcquireSpinLockExclusiveAtDpcLevel((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 119)))), a2, (unsigned int)(*(unsigned int *)(v_rsp - 95 + 119)), *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 119))));
    goto loc_003B50AF;
loc_003B5470:
    v_r10 = 0;
    a4 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 119)))) >> (6);
loc_003B547B:
    if (((unsigned int)(*(unsigned int *)(v_rsp - 95 + 119))) == -1) goto loc_003B55C8;
loc_003B5485:
    if (((unsigned int)(*(unsigned int *)(v_rsp - 95 + 119))) == -1) { result = (unsigned int)(v_rdi); }
    *(unsigned int *)(v_rsp - 95 - 61) = (unsigned int)(result);
    if ((v_r10 + result * 1) >= (*(unsigned __int64 *)(v_rsp - 95 - 1))) goto loc_003B55B5;
    a4 = ~((unsigned int)(*(unsigned int *)(v_rsp - 95 + 119)));
loc_003B54A6:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111))))) >> (1));
    result = (a4) >> ((unsigned __int8)(a1));
    a4 = (a4) & (result);
    if (condition_is_equal) goto loc_003B57B9;
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111))) - ((unsigned int)(a1)));
    if (((unsigned int)(v_r10)) > 1) goto loc_003B54A6;
    *(unsigned int *)(v_rsp - 95 - 89) = (unsigned int)(result);
loc_003B54CC:
    a2 = (a2) - (*(unsigned __int64 *)(v_rsp - 95 - 25));
    a2 = (a2) >> (3);
    a2 = (a2) << (6);
    v_rdi = ((unsigned int)((unsigned int)(result))) + (a2);
    v_r11 = (*(unsigned __int64 *)(v_rsp - 95 - 25) + a4 * 8) | (-1);
    goto loc_003B5237;
loc_003B54E7:
    v_r11 = (v_r11) | (-1);
    goto loc_003B506A;
loc_003B54F7:
    *(unsigned __int64 *)(v_r14 + 48) = v_rdi + 1;
    goto loc_003B544F;
loc_003B5504:
    v_r10 = 0;
    a2 = (a2) >> (6);
loc_003B550F:
    if (a4 == -1) goto loc_003B568F;
loc_003B5519:
    result = v_rdi + 1;
    if (a4 == -1) { result = 64; }
    *(unsigned int *)(v_rsp - 95 - 33) = (unsigned int)(result);
    if ((v_r10 + result * 1) >= (*(unsigned __int64 *)(v_rsp - 95 - 9))) goto loc_003B55C0;
    a2 = ~(a4);
loc_003B553F:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111))))) >> (1));
    result = (a2) >> ((unsigned __int8)(a1));
    a2 = (a2) & (result);
    if (condition_is_equal) goto loc_003B57F6;
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111))) - ((unsigned int)(a1)));
    if (((unsigned int)(v_r10)) > 1) goto loc_003B553F;
    *(unsigned int *)(v_rsp - 95 - 85) = (unsigned int)(result);
loc_003B5565:
    a3 = ((unsigned int)(*(unsigned int *)(v_rsp - 95 + 119))) - ((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111)));
    a3 = (a3) >> (3);
    a3 = (a3) << (6);
    a2 = ((unsigned int)((unsigned int)(result))) + (a3);
    v_r11 = ((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111)) + a2 * 8) | (-1);
    goto loc_003B5417;
loc_003B557C:
loc_003B557F:
    if (!sign_flag) goto loc_003B5949;
    a2 = (a2) + (8);
    if (a2 > (*(unsigned __int64 *)(v_rsp - 95 - 9))) goto loc_003B51FA;
    goto loc_003B557F;
loc_003B559A:
    if (!sign_flag) goto loc_003B5975;
    a3 = (*(unsigned __int64 *)(a2)) + (8);
    if (a3 > (*(unsigned __int64 *)(v_rsp - 95 - 1))) goto loc_003B53B2;
    goto loc_003B559A;
loc_003B55B5:
    v_rdi = -((unsigned int)((unsigned int)(v_r10)));
    goto loc_003B54CC;
loc_003B55C0:
    a2 = -((unsigned int)((unsigned int)(v_r10)));
    goto loc_003B5565;
loc_003B55C8:
    a2 = (a2) + (8);
    if (a2 > (*(unsigned __int64 *)(v_rsp - 95 - 9))) goto loc_003B57E1;
    if ((*(unsigned __int64 *)(a2)) == -1) goto loc_003B55C8;
    v_r10 = 0;
    goto loc_003B5485;
loc_003B55E6:
    a4 = *(unsigned __int64 *)(v_rsp - 95 - 9) + 8;
    if (((0) & (63)) == 0) { a4 = *(unsigned __int64 *)(v_rsp - 95 - 9); }
    if (*(unsigned __int64 *)(a2) == 0) goto loc_003B5781;
    a2 = (a2) + (8);
    if ((*(unsigned __int64 *)(a2)) != 0) goto loc_003B565B;
    if ((*(unsigned __int64 *)(a2)) == 0) goto loc_003B583C;
    a1 = (unsigned int)((63) - ((unsigned int)(result)));
loc_003B561A:
    *(unsigned int *)(v_rsp - 95 - 81) = (unsigned int)(a1);
loc_003B561D:
    v_rdi = (a2) - (*(unsigned __int64 *)(v_rsp - 95 - 25));
    v_rdi = (v_rdi) >> (3);
    v_rdi = (v_rdi) << (6);
    v_rdi = (v_rdi) - ((unsigned int)((unsigned int)(a1)));
    if (v_rdi > 0) goto loc_003B51FA;
    result = (*(unsigned __int64 *)(v_rsp - 95 - 1)) - ((unsigned int)((unsigned int)(a1)));
    result = (result) >> (6);
loc_003B5648:
    a2 = (a2) + (8);
    if (a2 == (a2 + result * 8)) goto loc_003B5751;
    if ((*(unsigned __int64 *)(a2)) == 0) goto loc_003B5648;
loc_003B565B:
    if (a2 > a4) goto loc_003B51FA;
    a2 = (a2) + (8);
    if ((*(unsigned __int64 *)(a2)) != 0) goto loc_003B565B;
    if ((*(unsigned __int64 *)(a2)) == 0) goto loc_003B5846;
    a1 = (unsigned int)((63) - ((unsigned int)(a2 + result * 8)));
loc_003B568A:
    *(unsigned int *)(v_rsp - 95 - 77) = (unsigned int)(a1);
    goto loc_003B561D;
loc_003B568F:
    a3 = (a2 + result * 8) + (8);
    if (a3 > (*(unsigned __int64 *)(v_rsp - 95 - 1))) goto loc_003B581E;
    if ((*(unsigned __int64 *)(a3)) == -1) goto loc_003B568F;
    v_r10 = 0;
    goto loc_003B5519;
loc_003B56AD:
    v_r10 = *(unsigned __int64 *)(v_rsp - 95 - 1) + 8;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rsp - 95 - 25))) & (63)) == 0) { v_r10 = *(unsigned __int64 *)(v_rsp - 95 - 1); }
    if (*(unsigned __int64 *)(a3) == 0) goto loc_003B5850;
    a3 = (a3) + (8);
    if ((*(unsigned __int64 *)(a3)) != 0) goto loc_003B571E;
    if ((*(unsigned __int64 *)(a3)) == 0) goto loc_003B5857;
    a1 = (unsigned int)((63) - ((unsigned int)(*(unsigned __int64 *)(a2))));
loc_003B56E1:
    *(unsigned int *)(v_rsp - 95 - 53) = (unsigned int)(a1);
loc_003B56E4:
    a2 = (a3) - ((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111)));
    a2 = (a2) >> (3);
    a2 = (a2) << (6);
    a2 = (a2) - ((unsigned int)((unsigned int)(a1)));
    if (a2 > (*(unsigned __int64 *)(v_rsp - 95 - 25))) goto loc_003B53B2;
    result = (*(unsigned __int64 *)(v_rsp - 95 - 9)) - ((unsigned int)((unsigned int)(a1)));
    result = (result) >> (6);
loc_003B570F:
    a3 = (a3) + (8);
    if (a3 == (a3 + result * 8)) goto loc_003B5788;
    if ((*(unsigned __int64 *)(a3)) == 0) goto loc_003B570F;
loc_003B571E:
    if (a3 > v_r10) goto loc_003B53B2;
    a3 = (a3) + (8);
    if ((*(unsigned __int64 *)(a3)) != 0) goto loc_003B571E;
    if ((*(unsigned __int64 *)(a3)) == 0) goto loc_003B582F;
    a1 = (unsigned int)((63) - (a2));
    goto loc_003B5834;
loc_003B5751:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) - ((unsigned int)(a1)));
    a3 = (unsigned int)((a3) & (63));
    if (condition_is_equal) goto loc_003B523C;
    if (condition_is_equal) { a1 = 64; }
    *(unsigned int *)(v_rsp - 95 - 73) = (unsigned int)(a1);
    if (((unsigned int)(a1)) >= a3) goto loc_003B523C;
    goto loc_003B565B;
loc_003B5781:
    a1 = 0;
    goto loc_003B561D;
loc_003B5788:
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111))) - (0));
    a4 = (unsigned int)((a4) & (63));
    if (condition_is_equal) goto loc_003B541C;
    if (condition_is_equal) { a1 = 64; }
    *(unsigned int *)(v_rsp - 95 - 45) = (unsigned int)(a1);
    if (((unsigned int)(a1)) < ((unsigned int)(a4))) goto loc_003B571E;
    goto loc_003B541C;
loc_003B57B9:
    if (a2 == v_r11) goto loc_003B57E1;
    if (a2 == v_r11) goto loc_003B57F1;
    v_r10 = (unsigned int)((63) - (64));
loc_003B57D1:
    a2 = (a2) + (8);
    *(unsigned int *)(v_rsp - 95 - 57) = (unsigned int)(v_r10);
    goto loc_003B547B;
loc_003B57E1:
    v_r11 = (v_r11) | (-1);
    goto loc_003B51FD;
loc_003B57F1:
    goto loc_003B57D1;
loc_003B57F6:
    if ((*(unsigned __int64 *)(a2)) == v_r11) goto loc_003B581E;
    if ((*(unsigned __int64 *)(a2)) == v_r11) goto loc_003B5827;
    v_r10 = (unsigned int)((63) - (64));
loc_003B580E:
    a3 = (*(unsigned __int64 *)(a2)) + (8);
    *(unsigned int *)(v_rsp - 95 - 29) = (unsigned int)(v_r10);
    goto loc_003B550F;
loc_003B581E:
    v_r11 = (v_r11) | (-1);
    goto loc_003B53B2;
loc_003B5827:
    goto loc_003B580E;
loc_003B582F:
loc_003B5834:
    *(unsigned int *)(v_rsp - 95 - 49) = 64;
    goto loc_003B56E4;
loc_003B583C:
    goto loc_003B561A;
loc_003B5846:
    goto loc_003B568A;
loc_003B5850:
    a1 = 0;
    goto loc_003B56E4;
loc_003B5857:
    goto loc_003B56E1;
loc_003B5861:
    v_rdi = (a2) - (*(unsigned __int64 *)(v_rsp - 95 - 25));
    *(unsigned int *)(v_rsp - 95 - 69) = 64;
    v_rdi = (v_rdi) >> (3);
    v_rdi = (v_rdi) + 1;
    v_rdi = (v_rdi) << (6);
    v_rdi = (v_rdi) - (64);
    if (v_rdi > 0) goto loc_003B51FA;
    a1 = (*(unsigned __int64 *)(v_rsp - 95 - 1)) - (64);
    if (condition_is_equal) goto loc_003B523C;
    a2 = (a2) + (8);
    if (a1 < (*(unsigned __int64 *)(a3))) goto loc_003B58B8;
    if (*(unsigned __int64 *)(a2) != 0) goto loc_003B557F;
    a1 = (a1) - (*(unsigned __int64 *)(a3));
    if (condition_is_equal) goto loc_003B523C;
    a2 = (a2) + (8);
loc_003B58B8:
    result = *(unsigned __int64 *)(a2);
    if (condition_is_equal) { result = (unsigned int)(*(unsigned __int64 *)(a3)); }
    *(unsigned int *)(v_rsp - 95 - 65) = (unsigned int)(result);
    if (result < a1) goto loc_003B557F;
    goto loc_003B523C;
loc_003B58D1:
    a2 = (*(unsigned __int64 *)(a2)) - ((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111)));
    *(unsigned int *)(v_rsp - 95 - 41) = (unsigned int)(result);
    a2 = (a2) >> (3);
    a2 = (a2) + 1;
    a2 = (a2) << (6);
    a2 = (a2) - ((unsigned int)((unsigned int)(result)));
    if (a2 > (*(unsigned __int64 *)(v_rsp - 95 - 25))) goto loc_003B53B2;
    a1 = (*(unsigned __int64 *)(v_rsp - 95 - 9)) - ((unsigned int)((unsigned int)(result)));
    if (condition_is_equal) goto loc_003B541C;
    a3 = (*(unsigned __int64 *)(a2)) + (8);
    if (a1 < 64) goto loc_003B5928;
    if (*(unsigned __int64 *)(a3) != 0) goto loc_003B559A;
    a1 = (a1) - (64);
    if (condition_is_equal) goto loc_003B541C;
    a3 = (a3) + (8);
loc_003B5928:
    result = *(unsigned __int64 *)(a3);
    if (condition_is_equal) { result = 64; }
    *(unsigned int *)(v_rsp - 95 - 37) = (unsigned int)(result);
    if (result < a1) goto loc_003B559A;
    goto loc_003B541C;
loc_003B5941:
    goto loc_003B5201;
loc_003B5949:
    goto loc_003B5861;
loc_003B595F:
    result = MiFindNextAlignedForwardRunClearEx(*(unsigned __int64 *)(v_rsp - 95 - 25), *(unsigned __int64 *)(v_rsp - 95 - 1), (unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(a3));
    goto loc_003B5093;
loc_003B5975:
    goto loc_003B58D1;
}
```

## 5. (Beta) C Style

```c
int64_t MiObtainDynamicVa(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;

    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (152);
    local_r11 = (local_r11) | (-1);
    *(uint64_t *)(local_rsp - 0x5F - 0x11) = 1;
    *(uint64_t *)(local_rsp - 0x5F + 0x7) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F - 0x9) = v_cr8;
loc_003B506A:
    result = (uint32_t)(((uint32_t)(Arg3)) + (-10));
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = Arg1;
    *(uint64_t *)(local_rsp - 0x5F + 0x7F) = *(uint64_t *)(Arg1 + 0x18);
    if ((((uint32_t)(result)) & (0xFFFFFFFDULL)) == 0) goto loc_003B50EA;
loc_003B5089:
    if ((*(uint64_t *)(Arg1)) != 0) goto loc_003B5142;
loc_003B5093:
    *(uint64_t *)(local_rsp - 0x5F - 0x1) = Arg1 + 64;
    if (((uint8_t)(v_cr8)) == 2) goto loc_003B5462;
    result = ExAcquireSpinLockExclusive(Arg1 + 64, Arg2, 512, a4);
    *(uint8_t *)(local_rsp - 0x5F + 0x7F) = (uint8_t)(result);
loc_003B50AF:
    local_r11 = (local_r11) | (-1);
    if (local_r11 != local_r11) goto loc_003B5257;
loc_003B50BC:
    Arg3 = 0;
    result = MiExtendDynamicBitMap(Arg1, Arg1, Arg3, (uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x77)));
    result = MiReleaseSpinLockExclusive(Arg1 + 64, *(uint8_t *)(local_rsp - 0x5F + 0x7F), Arg3, (uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x77)));
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_003B54E7;
    result = 0;
    goto loc_003B5326;
loc_003B50EA:
    Arg1 = (*(uint64_t *)(Arg1 + 0x10)) >> (6);
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = local_rsp - 95 + 7;
    *(uint64_t *)(local_rsp - 0x5F + 0x7) = *(uint64_t *)(Arg1 + 0x28);
    result = (*(uint64_t *)(Arg1 + 0x28)) >> (6);
    result = (result) << (3);
    Arg2 = (*(uint64_t *)(Arg1 + 0x8) + Arg1 * 8) - (result);
    *(uint64_t *)(local_rsp - 0x5F + 0x7F) = *(uint64_t *)(Arg1 + 0x30);
    *(uint64_t *)(local_rsp - 0x5F + 0xF) = Arg2;
    if (((uint32_t)((uint32_t)(Arg2))) < 0) goto loc_003B5089;
    local_r13 = 1;
    if (((*(uint64_t *)(v_rip + 0xC11953)) & (0x40000000ULL)) != 0) { local_r13 = 0; }
    *(uint64_t *)(local_rsp - 0x5F - 0x11) = local_r13;
    goto loc_003B5089;
loc_003B5142:
    if (local_r13 != 1) goto loc_003B595F;
    local_rdi = (local_r11) & (*(uint64_t *)(Arg1 + 0x30));
    if ((uint32_t)((uint32_t)(Arg2)) != 0) goto loc_003B5179;
    local_rdi = (local_rdi) & (-8);
loc_003B516C:
    goto loc_003B5093;
loc_003B5179:
loc_003B5180:
    result = (*(uint64_t *)(local_rsp - 0x5F + 0x7) - 1) - (local_rdi);
    result = (result) + 1;
    if (result < ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) goto loc_003B5941;
    local_r14 = (*(uint64_t *)(local_rsp - 0x5F + 0x7) - 1) - ((uint32_t)((uint32_t)((uint32_t)(Arg2))));
    Arg1 = (uint8_t)(((uint8_t)(local_rdi)) & (63));
    local_r14 = (local_r14) + 1;
    Arg3 = (1) << ((uint8_t)(Arg1));
    result = (local_r14) >> (6);
    Arg3 = (Arg3) - 1;
    result = (local_rdi) >> (6);
    Arg3 = (Arg3) | (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x19) + result * 8));
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) > 127) goto loc_003B55E6;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) >= 64) goto loc_003B557C;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) > 1) goto loc_003B5470;
loc_003B51EC:
    if (Arg3 != local_r11) goto loc_003B521C;
    Arg2 = (*(uint64_t *)(local_rsp - 0x5F - 0x19) + result * 8) + (8);
    if (Arg2 <= (*(uint64_t *)(local_rsp - 0x5F - 0x19) + result * 8)) goto loc_003B5252;
loc_003B51FA:
loc_003B51FD:
loc_003B5201:
    if (local_rdi == 0) goto loc_003B5241;
    a4 = (uint32_t)((uint32_t)((uint32_t)(Arg2))) + *(uint64_t *)(local_rsp - 0x5F + 0x7F) * 1;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2))) + *(uint64_t *)(local_rsp - 0x5F + 0x7F) * 1) > (*(uint64_t *)(local_rsp - 0x5F - 0x11))) { a4 = *(uint64_t *)(local_rsp - 0x5F - 0x11); }
    a4 = (a4) - 1;
    local_r12 = 0;
    goto loc_003B5180;
loc_003B521C:
    Arg3 = ~(Arg3);
    local_rdi = (Arg2) - (*(uint64_t *)(local_rsp - 0x5F - 0x19));
    local_rdi = (local_rdi) >> (3);
    local_rdi = (local_rdi) << (6);
    *(uint32_t *)(local_rsp - 0x5F - 0x59) = (uint32_t)(result);
    local_rdi = (local_rdi) + (result);
loc_003B5237:
    if (local_rdi > local_r14) goto loc_003B51FA;
loc_003B523C:
    if (local_rdi == local_r11) goto loc_003B51FD;
loc_003B5241:
    goto loc_003B516C;
loc_003B5252:
    goto loc_003B51EC;
loc_003B5257:
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x11)) != 1) goto loc_003B53E6;
    local_r14 = (*(uint64_t *)(local_rsp - 0x5F + 0x67)) & (local_rdi);
    if ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F)))) != 0) goto loc_003B533B;
    local_rdi = (local_r14) & (-8);
loc_003B5288:
loc_003B5297:
    if (local_rdi == -1) goto loc_003B50BC;
    result = RtlSetBitsEx(*(uint64_t *)(local_rsp - 0x5F - 0x19), local_rdi, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F)))), a4);
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x77)) - 10)) & (0xFFFFFFFDULL)) == 0) goto loc_003B5439;
    result = (uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x77)) - 10;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F)))) == 1) {
        result = local_rdi + 1;
        *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x18) = result;
    }
    if ((*(uint64_t *)(local_rsp - 0x5F + 0x67)) != (v_rip + 10984873)) goto loc_003B5301;
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F))))) << (21);
    Arg1 = (*(uint64_t *)(v_rip + 0xA79BE5)) - (result);
    *(uint64_t *)(v_rip + 0xA79BD4) = Arg1;
    if (Arg1 <= 0x8000000ULL) goto loc_003B53D0;
loc_003B5301:
    result = MiReleaseSpinLockExclusive((uint32_t)((uint32_t)((uint32_t)(Arg2))), *(uint8_t *)(local_rsp - 0x5F + 0x7F), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F)))), a4);
    local_rdi = (local_rdi) << (21);
    local_rdi = (local_rdi) + (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x20));
loc_003B5326:
    local_rsp = (local_rsp) + (152);
    return local_rdi;
loc_003B533B:
    result = (*(uint8_t *)(local_rsp - 0x5F + 0x7F)) - (*(uint64_t *)(local_rsp - 0x5F + 0x67));
    result = (result) + 1;
    if (result < ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F)))))) goto loc_003B53B2;
    local_r15 = (*(uint8_t *)(local_rsp - 0x5F + 0x7F)) - ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F)))));
    Arg1 = (uint8_t)(((uint8_t)(*(uint64_t *)(local_rsp - 0x5F + 0x67))) & (63));
    local_r15 = (local_r15) + 1;
    a4 = (1) << ((uint8_t)(Arg1));
    result = (local_r15) >> (6);
    a4 = (a4) - 1;
    result = (*(uint64_t *)(local_rsp - 0x5F + 0x67)) >> (6);
    a4 = (a4) | (*(uint64_t *)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F)) + result * 8));
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F))))) > 127) goto loc_003B56AD;
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F))))) >= 64) goto loc_003B559A;
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F))))) > 1) goto loc_003B5504;
loc_003B53A4:
    if (a4 != local_r11) goto loc_003B53FC;
    Arg3 = ((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F)) + result * 8) + (8);
    if (Arg3 <= ((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F)) + result * 8)) goto loc_003B5431;
loc_003B53B2:
loc_003B53B5:
    if (*(uint64_t *)(local_rsp - 0x5F + 0x67) == 0) goto loc_003B5421;
    Arg2 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F)))) + local_rdi * 1;
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F)))) + local_rdi * 1) > ((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x77)))) { Arg2 = (uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x77)); }
    Arg2 = (Arg2) - 1;
    local_r14 = 0;
    goto loc_003B533B;
loc_003B53D0:
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(v_rip + 11027110, Arg2, Arg3, a4);
    goto loc_003B5301;
loc_003B53E6:
    result = MiFindNextAlignedForwardRunClearEx(local_r15, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F)))), (uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x77)), a4);
    goto loc_003B5297;
loc_003B53FC:
    a4 = ~(a4);
    Arg2 = ((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x77))) - ((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F)));
    Arg2 = (Arg2) >> (3);
    Arg2 = (Arg2) << (6);
    *(uint32_t *)(local_rsp - 0x5F - 0x55) = (uint32_t)(result);
    Arg2 = (Arg2) + (result);
loc_003B5417:
    if (Arg2 > local_r15) goto loc_003B53B2;
loc_003B541C:
    if (Arg2 == local_r11) goto loc_003B53B5;
loc_003B5421:
    goto loc_003B5288;
loc_003B5431:
    goto loc_003B53A4;
loc_003B5439:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x19) + 0x8)) - (*(uint64_t *)(local_r14 + 0x8));
    Arg1 = (Arg1) << (3);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F)))) == 1) goto loc_003B54F7;
loc_003B544F:
    local_rdi = (Arg2) + (Arg1);
    result = MiReduceSystemRegionType((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x77)))), Arg2, (uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x77)), *(uint64_t *)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x77))));
    goto loc_003B52D0;
loc_003B5462:
    *(uint8_t *)(local_rsp - 0x5F + 0x7F) = 17;
    result = ExAcquireSpinLockExclusiveAtDpcLevel((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x77)))), Arg2, (uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x77)), *(uint64_t *)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x77))));
    goto loc_003B50AF;
loc_003B5470:
    local_r10 = 0;
    a4 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x77)))) >> (6);
loc_003B547B:
    if (((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x77))) == -1) goto loc_003B55C8;
loc_003B5485:
    if (((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x77))) == -1) { result = (uint32_t)(local_rdi); }
    *(uint32_t *)(local_rsp - 0x5F - 0x3D) = (uint32_t)(result);
    if ((local_r10 + result * 1) >= (*(uint64_t *)(local_rsp - 0x5F - 0x1))) goto loc_003B55B5;
    a4 = ~((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x77)));
loc_003B54A6:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F))))) >> (1));
    result = (a4) >> ((uint8_t)(Arg1));
    a4 = (a4) & (result);
    if (condition_is_equal) goto loc_003B57B9;
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F))) - ((uint32_t)(Arg1)));
    if (((uint32_t)(local_r10)) > 1) goto loc_003B54A6;
    *(uint32_t *)(local_rsp - 0x5F - 0x59) = (uint32_t)(result);
loc_003B54CC:
    Arg2 = (Arg2) - (*(uint64_t *)(local_rsp - 0x5F - 0x19));
    Arg2 = (Arg2) >> (3);
    Arg2 = (Arg2) << (6);
    local_rdi = ((uint32_t)((uint32_t)(result))) + (Arg2);
    local_r11 = (*(uint64_t *)(local_rsp - 0x5F - 0x19) + a4 * 8) | (-1);
    goto loc_003B5237;
loc_003B54E7:
    local_r11 = (local_r11) | (-1);
    goto loc_003B506A;
loc_003B54F7:
    *(uint64_t *)(local_r14 + 0x30) = local_rdi + 1;
    goto loc_003B544F;
loc_003B5504:
    local_r10 = 0;
    Arg2 = (Arg2) >> (6);
loc_003B550F:
    if (a4 == -1) goto loc_003B568F;
loc_003B5519:
    result = local_rdi + 1;
    if (a4 == -1) { result = 64; }
    *(uint32_t *)(local_rsp - 0x5F - 0x21) = (uint32_t)(result);
    if ((local_r10 + result * 1) >= (*(uint64_t *)(local_rsp - 0x5F - 0x9))) goto loc_003B55C0;
    Arg2 = ~(a4);
loc_003B553F:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F))))) >> (1));
    result = (Arg2) >> ((uint8_t)(Arg1));
    Arg2 = (Arg2) & (result);
    if (condition_is_equal) goto loc_003B57F6;
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F))) - ((uint32_t)(Arg1)));
    if (((uint32_t)(local_r10)) > 1) goto loc_003B553F;
    *(uint32_t *)(local_rsp - 0x5F - 0x55) = (uint32_t)(result);
loc_003B5565:
    Arg3 = ((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x77))) - ((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F)));
    Arg3 = (Arg3) >> (3);
    Arg3 = (Arg3) << (6);
    Arg2 = ((uint32_t)((uint32_t)(result))) + (Arg3);
    local_r11 = ((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F)) + Arg2 * 8) | (-1);
    goto loc_003B5417;
loc_003B557C:
loc_003B557F:
    if (!sign_flag) goto loc_003B5949;
    Arg2 = (Arg2) + (8);
    if (Arg2 > (*(uint64_t *)(local_rsp - 0x5F - 0x9))) goto loc_003B51FA;
    goto loc_003B557F;
loc_003B559A:
    if (!sign_flag) goto loc_003B5975;
    Arg3 = (*(uint64_t *)(Arg2)) + (8);
    if (Arg3 > (*(uint64_t *)(local_rsp - 0x5F - 0x1))) goto loc_003B53B2;
    goto loc_003B559A;
loc_003B55B5:
    local_rdi = -((uint32_t)((uint32_t)(local_r10)));
    goto loc_003B54CC;
loc_003B55C0:
    Arg2 = -((uint32_t)((uint32_t)(local_r10)));
    goto loc_003B5565;
loc_003B55C8:
    Arg2 = (Arg2) + (8);
    if (Arg2 > (*(uint64_t *)(local_rsp - 0x5F - 0x9))) goto loc_003B57E1;
    if ((*(uint64_t *)(Arg2)) == -1) goto loc_003B55C8;
    local_r10 = 0;
    goto loc_003B5485;
loc_003B55E6:
    a4 = *(uint64_t *)(local_rsp - 0x5F - 0x9) + 8;
    if (((0) & (63)) == 0) { a4 = *(uint64_t *)(local_rsp - 0x5F - 0x9); }
    if (*(uint64_t *)(Arg2) == 0) goto loc_003B5781;
    Arg2 = (Arg2) + (8);
    if ((*(uint64_t *)(Arg2)) != 0) goto loc_003B565B;
    if ((*(uint64_t *)(Arg2)) == 0) goto loc_003B583C;
    Arg1 = (uint32_t)((63) - ((uint32_t)(result)));
loc_003B561A:
    *(uint32_t *)(local_rsp - 0x5F - 0x51) = (uint32_t)(Arg1);
loc_003B561D:
    local_rdi = (Arg2) - (*(uint64_t *)(local_rsp - 0x5F - 0x19));
    local_rdi = (local_rdi) >> (3);
    local_rdi = (local_rdi) << (6);
    local_rdi = (local_rdi) - ((uint32_t)((uint32_t)(Arg1)));
    if (local_rdi > 0) goto loc_003B51FA;
    result = (*(uint64_t *)(local_rsp - 0x5F - 0x1)) - ((uint32_t)((uint32_t)(Arg1)));
    result = (result) >> (6);
loc_003B5648:
    Arg2 = (Arg2) + (8);
    if (Arg2 == (Arg2 + result * 8)) goto loc_003B5751;
    if ((*(uint64_t *)(Arg2)) == 0) goto loc_003B5648;
loc_003B565B:
    if (Arg2 > a4) goto loc_003B51FA;
    Arg2 = (Arg2) + (8);
    if ((*(uint64_t *)(Arg2)) != 0) goto loc_003B565B;
    if ((*(uint64_t *)(Arg2)) == 0) goto loc_003B5846;
    Arg1 = (uint32_t)((63) - ((uint32_t)(Arg2 + result * 8)));
loc_003B568A:
    *(uint32_t *)(local_rsp - 0x5F - 0x4D) = (uint32_t)(Arg1);
    goto loc_003B561D;
loc_003B568F:
    Arg3 = (Arg2 + result * 8) + (8);
    if (Arg3 > (*(uint64_t *)(local_rsp - 0x5F - 0x1))) goto loc_003B581E;
    if ((*(uint64_t *)(Arg3)) == -1) goto loc_003B568F;
    local_r10 = 0;
    goto loc_003B5519;
loc_003B56AD:
    local_r10 = *(uint64_t *)(local_rsp - 0x5F - 0x1) + 8;
    if ((((uint8_t)(*(uint64_t *)(local_rsp - 0x5F - 0x19))) & (63)) == 0) { local_r10 = *(uint64_t *)(local_rsp - 0x5F - 0x1); }
    if (*(uint64_t *)(Arg3) == 0) goto loc_003B5850;
    Arg3 = (Arg3) + (8);
    if ((*(uint64_t *)(Arg3)) != 0) goto loc_003B571E;
    if ((*(uint64_t *)(Arg3)) == 0) goto loc_003B5857;
    Arg1 = (uint32_t)((63) - ((uint32_t)(*(uint64_t *)(Arg2))));
loc_003B56E1:
    *(uint32_t *)(local_rsp - 0x5F - 0x35) = (uint32_t)(Arg1);
loc_003B56E4:
    Arg2 = (Arg3) - ((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F)));
    Arg2 = (Arg2) >> (3);
    Arg2 = (Arg2) << (6);
    Arg2 = (Arg2) - ((uint32_t)((uint32_t)(Arg1)));
    if (Arg2 > (*(uint64_t *)(local_rsp - 0x5F - 0x19))) goto loc_003B53B2;
    result = (*(uint64_t *)(local_rsp - 0x5F - 0x9)) - ((uint32_t)((uint32_t)(Arg1)));
    result = (result) >> (6);
loc_003B570F:
    Arg3 = (Arg3) + (8);
    if (Arg3 == (Arg3 + result * 8)) goto loc_003B5788;
    if ((*(uint64_t *)(Arg3)) == 0) goto loc_003B570F;
loc_003B571E:
    if (Arg3 > local_r10) goto loc_003B53B2;
    Arg3 = (Arg3) + (8);
    if ((*(uint64_t *)(Arg3)) != 0) goto loc_003B571E;
    if ((*(uint64_t *)(Arg3)) == 0) goto loc_003B582F;
    Arg1 = (uint32_t)((63) - (Arg2));
    goto loc_003B5834;
loc_003B5751:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) - ((uint32_t)(Arg1)));
    Arg3 = (uint32_t)((Arg3) & (63));
    if (condition_is_equal) goto loc_003B523C;
    if (condition_is_equal) { Arg1 = 64; }
    *(uint32_t *)(local_rsp - 0x5F - 0x49) = (uint32_t)(Arg1);
    if (((uint32_t)(Arg1)) >= Arg3) goto loc_003B523C;
    goto loc_003B565B;
loc_003B5781:
    Arg1 = 0;
    goto loc_003B561D;
loc_003B5788:
    a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F))) - (0));
    a4 = (uint32_t)((a4) & (63));
    if (condition_is_equal) goto loc_003B541C;
    if (condition_is_equal) { Arg1 = 64; }
    *(uint32_t *)(local_rsp - 0x5F - 0x2D) = (uint32_t)(Arg1);
    if (((uint32_t)(Arg1)) < ((uint32_t)(a4))) goto loc_003B571E;
    goto loc_003B541C;
loc_003B57B9:
    if (Arg2 == local_r11) goto loc_003B57E1;
    if (Arg2 == local_r11) goto loc_003B57F1;
    local_r10 = (uint32_t)((63) - (64));
loc_003B57D1:
    Arg2 = (Arg2) + (8);
    *(uint32_t *)(local_rsp - 0x5F - 0x39) = (uint32_t)(local_r10);
    goto loc_003B547B;
loc_003B57E1:
    local_r11 = (local_r11) | (-1);
    goto loc_003B51FD;
loc_003B57F1:
    goto loc_003B57D1;
loc_003B57F6:
    if ((*(uint64_t *)(Arg2)) == local_r11) goto loc_003B581E;
    if ((*(uint64_t *)(Arg2)) == local_r11) goto loc_003B5827;
    local_r10 = (uint32_t)((63) - (64));
loc_003B580E:
    Arg3 = (*(uint64_t *)(Arg2)) + (8);
    *(uint32_t *)(local_rsp - 0x5F - 0x1D) = (uint32_t)(local_r10);
    goto loc_003B550F;
loc_003B581E:
    local_r11 = (local_r11) | (-1);
    goto loc_003B53B2;
loc_003B5827:
    goto loc_003B580E;
loc_003B582F:
loc_003B5834:
    *(uint32_t *)(local_rsp - 0x5F - 0x31) = 64;
    goto loc_003B56E4;
loc_003B583C:
    goto loc_003B561A;
loc_003B5846:
    goto loc_003B568A;
loc_003B5850:
    Arg1 = 0;
    goto loc_003B56E4;
loc_003B5857:
    goto loc_003B56E1;
loc_003B5861:
    local_rdi = (Arg2) - (*(uint64_t *)(local_rsp - 0x5F - 0x19));
    *(uint32_t *)(local_rsp - 0x5F - 0x45) = 64;
    local_rdi = (local_rdi) >> (3);
    local_rdi = (local_rdi) + 1;
    local_rdi = (local_rdi) << (6);
    local_rdi = (local_rdi) - (64);
    if (local_rdi > 0) goto loc_003B51FA;
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F - 0x1)) - (64);
    if (condition_is_equal) goto loc_003B523C;
    Arg2 = (Arg2) + (8);
    if (Arg1 < (*(uint64_t *)(Arg3))) goto loc_003B58B8;
    if (*(uint64_t *)(Arg2) != 0) goto loc_003B557F;
    Arg1 = (Arg1) - (*(uint64_t *)(Arg3));
    if (condition_is_equal) goto loc_003B523C;
    Arg2 = (Arg2) + (8);
loc_003B58B8:
    result = *(uint64_t *)(Arg2);
    if (condition_is_equal) { result = (uint32_t)(*(uint64_t *)(Arg3)); }
    *(uint32_t *)(local_rsp - 0x5F - 0x41) = (uint32_t)(result);
    if (result < Arg1) goto loc_003B557F;
    goto loc_003B523C;
loc_003B58D1:
    Arg2 = (*(uint64_t *)(Arg2)) - ((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F)));
    *(uint32_t *)(local_rsp - 0x5F - 0x29) = (uint32_t)(result);
    Arg2 = (Arg2) >> (3);
    Arg2 = (Arg2) + 1;
    Arg2 = (Arg2) << (6);
    Arg2 = (Arg2) - ((uint32_t)((uint32_t)(result)));
    if (Arg2 > (*(uint64_t *)(local_rsp - 0x5F - 0x19))) goto loc_003B53B2;
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F - 0x9)) - ((uint32_t)((uint32_t)(result)));
    if (condition_is_equal) goto loc_003B541C;
    Arg3 = (*(uint64_t *)(Arg2)) + (8);
    if (Arg1 < 64) goto loc_003B5928;
    if (*(uint64_t *)(Arg3) != 0) goto loc_003B559A;
    Arg1 = (Arg1) - (64);
    if (condition_is_equal) goto loc_003B541C;
    Arg3 = (Arg3) + (8);
loc_003B5928:
    result = *(uint64_t *)(Arg3);
    if (condition_is_equal) { result = 64; }
    *(uint32_t *)(local_rsp - 0x5F - 0x25) = (uint32_t)(result);
    if (result < Arg1) goto loc_003B559A;
    goto loc_003B541C;
loc_003B5941:
    goto loc_003B5201;
loc_003B5949:
    goto loc_003B5861;
loc_003B595F:
    result = MiFindNextAlignedForwardRunClearEx(*(uint64_t *)(local_rsp - 0x5F - 0x19), *(uint64_t *)(local_rsp - 0x5F - 0x1), (uint32_t)((uint32_t)(result)), *(uint64_t *)(Arg3));
    goto loc_003B5093;
loc_003B5975:
    goto loc_003B58D1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003B501C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
