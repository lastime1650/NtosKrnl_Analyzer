# CmpPostNotify

- RVA: `0x008645D8`–`0x008649A6` (길이 `974` bytes)
- VA: `0x00000001408645D8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006B96C`
- 디코드: `255`개 명령, `974/974` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00864658` → [ExAcquireFastMutexUnsafe](../../text/3F/ExAcquireFastMutexUnsafe_function_003F3720.md) (function, `0x003F3720`)
- `0x00864681` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)
- `0x008646BC` → [Feature_2602282298__private_IsEnabledDeviceUsageNoInline](../../text/66/Feature_2602282298__private_IsEnabledDeviceUsageNoInline_function_0066A3E8.md) (function, `0x0066A3E8`)
- `0x00864722` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0086475C` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x008647ED` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0086483C` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00864865` → [CmpAddToDelayedDeref](../A3/CmpAddToDelayedDeref_function_00A34034.md) (function, `0x00A34034`)
- `0x0086486D` → [CmpFreePostBlock](../84/CmpFreePostBlock_function_00848560.md) (function, `0x00848560`)
- `0x008648B1` → [CmpCancelSubordinatePost](../A3/CmpCancelSubordinatePost_function_00A33FE8.md) (function, `0x00A33FE8`)
- `0x008648B9` → [CmpAddToDelayedDeref](../A3/CmpAddToDelayedDeref_function_00A34034.md) (function, `0x00A34034`)
- `0x008648DF` → [CmpFreeSubordinatePost](../90/CmpFreeSubordinatePost_function_00906CA0.md) (function, `0x00906CA0`)
- `0x0086492D` → [KeInsertQueueApc](../../text/20/KeInsertQueueApc_function_00203F10.md) (function, `0x00203F10`)
- `0x0086494B` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x00864969` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)
- `0x00864978` → [CmpDelayedDerefKeys](../A2/CmpDelayedDerefKeys_function_00A23B88.md) (function, `0x00A23B88`)
- `0x00864987` → [CmpSignalDeferredPosts](../84/CmpSignalDeferredPosts_function_008484B0.md) (function, `0x008484B0`)

### Direct callers
- [CmpCloseKeyObject](CmpCloseKeyObject_function_00863AD0.md) at `0x00863C64`
- [sub_0086560A](Unknown_function_0086560A.md) at `0x00865845`
- [sub_008C73D5](../8C/Unknown_function_008C73D5.md) at `0x008C7421`
- [CmpPerformUnloadKey](../9A/CmpPerformUnloadKey_function_009AFA28.md) at `0x009AFB9E`
- [CmpFlushNotify](../9B/CmpFlushNotify_function_009B36A8.md) at `0x009B3710`
- [CmpNotifyChangeKey](../A4/CmpNotifyChangeKey_function_00A43C80.md) at `0x00A43FB7`

### Static image references
- `0x00864651` → RVA `0x00EF5940` (`.data`; read)
- `0x00864714` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **10**
  - `0x00864658` → [ExAcquireFastMutexUnsafe](../../text/3F/ExAcquireFastMutexUnsafe_function_003F3720.md) (`PAGE` → `.text`)
  - `0x00864681` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (`PAGE` → `.text`)
  - `0x008646BC` → [Feature_2602282298__private_IsEnabledDeviceUsageNoInline](../../text/66/Feature_2602282298__private_IsEnabledDeviceUsageNoInline_function_0066A3E8.md) (`PAGE` → `.text`)
  - `0x00864722` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (`PAGE` → `.text`)
  - `0x0086475C` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (`PAGE` → `.text`)
  - `0x008647ED` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (`PAGE` → `.text`)
  - `0x0086483C` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (`PAGE` → `.text`)
  - `0x0086492D` → [KeInsertQueueApc](../../text/20/KeInsertQueueApc_function_00203F10.md) (`PAGE` → `.text`)
  - `0x0086494B` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x00864969` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008645D8  48 8B C4                        mov rax, rsp
008645DB  48 89 58 08                     mov qword ptr [rax + 8], rbx
008645DF  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
008645E3  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
008645E7  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
008645EB  55                              push rbp
008645EC  41 56                           push r14
008645EE  41 57                           push r15
008645F0  48 8B EC                        mov rbp, rsp
008645F3  48 83 EC 40                     sub rsp, 0x40
008645F7  48 83 7D 48 00                  cmp qword ptr [rbp + 0x48], 0
008645FC  0F 57 C0                        xorps xmm0, xmm0
008645FF  0F 57 C9                        xorps xmm1, xmm1
00864602  41 8B F9                        mov edi, r9d
00864605  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00864609  48 8B D9                        mov rbx, rcx
0086460C  0F 11 4D F0                     movups xmmword ptr [rbp - 0x10], xmm1
00864610  75 10                           jne 0x140864622
00864612  48 8D 45 E0                     lea rax, [rbp - 0x20]
00864616  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0086461A  48 8D 45 E0                     lea rax, [rbp - 0x20]
0086461E  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00864622  48 8D 75 E0                     lea rsi, [rbp - 0x20]
00864626  48 0F 45 75 48                  cmovne rsi, qword ptr [rbp + 0x48]
0086462B  48 83 7D 50 00                  cmp qword ptr [rbp + 0x50], 0
00864630  75 10                           jne 0x140864642
00864632  48 8D 45 F0                     lea rax, [rbp - 0x10]
00864636  48 89 45 F8                     mov qword ptr [rbp - 8], rax
0086463A  48 8D 45 F0                     lea rax, [rbp - 0x10]
0086463E  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00864642  4C 8D 75 F0                     lea r14, [rbp - 0x10]
00864646  4C 0F 45 75 50                  cmovne r14, qword ptr [rbp + 0x50]
0086464B  80 7D 40 00                     cmp byte ptr [rbp + 0x40], 0
0086464F  75 0C                           jne 0x14086465d
00864651  48 8D 0D E8 12 69 00            lea rcx, [rip + 0x6912e8]
00864658  E8 C3 F0 B8 FF                  call 0x1403f3720
0086465D  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
00864660  4C 8D 7B 10                     lea r15, [rbx + 0x10]
00864664  4D 39 3F                        cmp qword ptr [r15], r15
00864667  75 22                           jne 0x14086468b
00864669  0F BA E8 1F                     bts eax, 0x1f
0086466D  80 7D 40 00                     cmp byte ptr [rbp + 0x40], 0
00864671  89 43 30                        mov dword ptr [rbx + 0x30], eax
00864674  0F 85 12 03 00 00               jne 0x14086498c
0086467A  48 8D 0D BF 12 69 00            lea rcx, [rip + 0x6912bf]
00864681  E8 1A BD 9E FF                  call 0x1402503a0
00864686  E9 01 03 00 00                  jmp 0x14086498c
0086468B  0F BA F0 1F                     btr eax, 0x1f
0086468F  89 43 30                        mov dword ptr [rbx + 0x30], eax
00864692  49 8B 1F                        mov rbx, qword ptr [r15]
00864695  49 3B DF                        cmp rbx, r15
00864698  0F 84 BE 02 00 00               je 0x14086495c
0086469E  4C 39 7B 08                     cmp qword ptr [rbx + 8], r15
008646A2  0F 85 AD 02 00 00               jne 0x140864955
008646A8  48 8B 03                        mov rax, qword ptr [rbx]
008646AB  48 39 58 08                     cmp qword ptr [rax + 8], rbx
008646AF  0F 85 A0 02 00 00               jne 0x140864955
008646B5  49 89 07                        mov qword ptr [r15], rax
008646B8  4C 89 78 08                     mov qword ptr [rax + 8], r15
008646BC  E8 27 5D E0 FF                  call 0x14066a3e8
008646C1  85 C0                           test eax, eax
008646C3  0F 85 AD 00 00 00               jne 0x140864776
008646C9  81 FF 0B 01 00 00               cmp edi, 0x10b
008646CF  0F 85 A2 01 00 00               jne 0x140864877
008646D5  F7 43 38 00 00 01 00            test dword ptr [rbx + 0x38], 0x10000
008646DC  0F 85 95 01 00 00               jne 0x140864877
008646E2  48 8D 43 20                     lea rax, [rbx + 0x20]
008646E6  48 8B 10                        mov rdx, qword ptr [rax]
008646E9  48 39 42 08                     cmp qword ptr [rdx + 8], rax
008646ED  0F 85 62 02 00 00               jne 0x140864955
008646F3  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
008646F7  48 39 01                        cmp qword ptr [rcx], rax
008646FA  0F 85 55 02 00 00               jne 0x140864955
00864700  48 89 11                        mov qword ptr [rcx], rdx
00864703  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
00864707  44 0F 20 C7                     mov rdi, cr8
0086470B  B8 01 00 00 00                  mov eax, 1
00864710  44 0F 22 C0                     mov cr8, rax
00864714  83 3D 05 26 76 00 00            cmp dword ptr [rip + 0x762605], 0
0086471B  74 0A                           je 0x140864727
0086471D  8A D0                           mov dl, al
0086471F  40 8A CF                        mov cl, dil
00864722  E8 D5 0F C9 FF                  call 0x1404f56fc
00864727  48 8D 43 10                     lea rax, [rbx + 0x10]
0086472B  48 8B 10                        mov rdx, qword ptr [rax]
0086472E  48 39 42 08                     cmp qword ptr [rdx + 8], rax
00864732  0F 85 1D 02 00 00               jne 0x140864955
00864738  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0086473C  48 39 01                        cmp qword ptr [rcx], rax
0086473F  0F 85 10 02 00 00               jne 0x140864955
00864745  48 89 11                        mov qword ptr [rcx], rdx
00864748  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
0086474C  83 3D CD 25 76 00 00            cmp dword ptr [rip + 0x7625cd], 0
00864753  74 0C                           je 0x140864761
00864755  44 0F 20 C1                     mov rcx, cr8
00864759  40 8A D7                        mov dl, dil
0086475C  E8 37 0F C9 FF                  call 0x1404f5698
00864761  40 0F B6 C7                     movzx eax, dil
00864765  44 0F 22 C0                     mov cr8, rax
00864769  B8 01 00 00 00                  mov eax, 1
0086476E  39 43 38                        cmp dword ptr [rbx + 0x38], eax
00864771  E9 E0 00 00 00                  jmp 0x140864856
00864776  48 83 23 00                     and qword ptr [rbx], 0
0086477A  48 83 63 08 00                  and qword ptr [rbx + 8], 0
0086477F  81 FF 0B 01 00 00               cmp edi, 0x10b
00864785  0F 85 EC 00 00 00               jne 0x140864877
0086478B  F7 43 38 00 00 01 00            test dword ptr [rbx + 0x38], 0x10000
00864792  0F 85 DF 00 00 00               jne 0x140864877
00864798  48 8D 4B 20                     lea rcx, [rbx + 0x20]
0086479C  48 8B 11                        mov rdx, qword ptr [rcx]
0086479F  48 8D 41 08                     lea rax, [rcx + 8]
008647A3  48 85 D2                        test rdx, rdx
008647A6  75 05                           jne 0x1408647ad
008647A8  48 39 10                        cmp qword ptr [rax], rdx
008647AB  74 25                           je 0x1408647d2
008647AD  48 39 4A 08                     cmp qword ptr [rdx + 8], rcx
008647B1  0F 85 9E 01 00 00               jne 0x140864955
008647B7  4C 8B 00                        mov r8, qword ptr [rax]
008647BA  49 39 08                        cmp qword ptr [r8], rcx
008647BD  0F 85 92 01 00 00               jne 0x140864955
008647C3  49 89 10                        mov qword ptr [r8], rdx
008647C6  4C 89 42 08                     mov qword ptr [rdx + 8], r8
008647CA  48 83 21 00                     and qword ptr [rcx], 0
008647CE  48 83 20 00                     and qword ptr [rax], 0
008647D2  44 0F 20 C7                     mov rdi, cr8
008647D6  B8 01 00 00 00                  mov eax, 1
008647DB  44 0F 22 C0                     mov cr8, rax
008647DF  83 3D 3A 25 76 00 00            cmp dword ptr [rip + 0x76253a], 0
008647E6  74 0A                           je 0x1408647f2
008647E8  8A D0                           mov dl, al
008647EA  40 8A CF                        mov cl, dil
008647ED  E8 0A 0F C9 FF                  call 0x1404f56fc
008647F2  48 8D 4B 10                     lea rcx, [rbx + 0x10]
008647F6  4C 8B 01                        mov r8, qword ptr [rcx]
008647F9  48 8D 41 08                     lea rax, [rcx + 8]
008647FD  4D 85 C0                        test r8, r8
00864800  75 05                           jne 0x140864807
00864802  4C 39 00                        cmp qword ptr [rax], r8
00864805  74 25                           je 0x14086482c
00864807  49 39 48 08                     cmp qword ptr [r8 + 8], rcx
0086480B  0F 85 44 01 00 00               jne 0x140864955
00864811  48 8B 10                        mov rdx, qword ptr [rax]
00864814  48 39 0A                        cmp qword ptr [rdx], rcx
00864817  0F 85 38 01 00 00               jne 0x140864955
0086481D  4C 89 02                        mov qword ptr [rdx], r8
00864820  49 89 50 08                     mov qword ptr [r8 + 8], rdx
00864824  48 83 21 00                     and qword ptr [rcx], 0
00864828  48 83 20 00                     and qword ptr [rax], 0
0086482C  83 3D ED 24 76 00 00            cmp dword ptr [rip + 0x7624ed], 0
00864833  74 0C                           je 0x140864841
00864835  44 0F 20 C1                     mov rcx, cr8
00864839  40 8A D7                        mov dl, dil
0086483C  E8 57 0E C9 FF                  call 0x1404f5698
00864841  40 0F B6 C7                     movzx eax, dil
00864845  44 0F 22 C0                     mov cr8, rax
00864849  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
0086484C  0F B7 C8                        movzx ecx, ax
0086484F  B8 01 00 00 00                  mov eax, 1
00864854  3B C8                           cmp ecx, eax
00864856  8B 7D 38                        mov edi, dword ptr [rbp + 0x38]
00864859  0F 84 33 FE FF FF               je 0x140864692
0086485F  48 8B D6                        mov rdx, rsi
00864862  48 8B CB                        mov rcx, rbx
00864865  E8 CA F7 1C 00                  call 0x140a34034
0086486A  48 8B CB                        mov rcx, rbx
0086486D  E8 EE 3C FE FF                  call 0x140848560
00864872  E9 1B FE FF FF                  jmp 0x140864692
00864877  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
0086487A  0F BA E0 10                     bt eax, 0x10
0086487E  72 1F                           jb 0x14086489f
00864880  48 8B C3                        mov rax, rbx
00864883  48 8B 40 20                     mov rax, qword ptr [rax + 0x20]
00864887  0F BA 70 18 10                  btr dword ptr [rax + 0x18], 0x10
0086488C  48 83 E8 20                     sub rax, 0x20
00864890  48 3B C3                        cmp rax, rbx
00864893  75 EE                           jne 0x140864883
00864895  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
00864898  0F BA E8 10                     bts eax, 0x10
0086489C  89 43 38                        mov dword ptr [rbx + 0x38], eax
0086489F  0F B7 C0                        movzx eax, ax
008648A2  B9 01 00 00 00                  mov ecx, 1
008648A7  3B C1                           cmp eax, ecx
008648A9  74 13                           je 0x1408648be
008648AB  48 8B D6                        mov rdx, rsi
008648AE  48 8B CB                        mov rcx, rbx
008648B1  E8 32 F7 1C 00                  call 0x140a33fe8
008648B6  48 8B CB                        mov rcx, rbx
008648B9  E8 76 F7 1C 00                  call 0x140a34034
008648BE  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
008648C1  0F B7 C8                        movzx ecx, ax
008648C4  83 E9 01                        sub ecx, 1
008648C7  74 6E                           je 0x140864937
008648C9  83 E9 01                        sub ecx, 1
008648CC  74 4F                           je 0x14086491d
008648CE  83 E9 01                        sub ecx, 1
008648D1  74 09                           je 0x1408648dc
008648D3  83 F9 01                        cmp ecx, 1
008648D6  0F 85 B6 FD FF FF               jne 0x140864692
008648DC  48 8B CB                        mov rcx, rbx
008648DF  E8 BC 23 0A 00                  call 0x140906ca0
008648E4  48 83 C3 10                     add rbx, 0x10
008648E8  48 8B 0B                        mov rcx, qword ptr [rbx]
008648EB  48 39 59 08                     cmp qword ptr [rcx + 8], rbx
008648EF  75 64                           jne 0x140864955
008648F1  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
008648F5  48 39 18                        cmp qword ptr [rax], rbx
008648F8  75 5B                           jne 0x140864955
008648FA  48 89 08                        mov qword ptr [rax], rcx
008648FD  48 89 41 08                     mov qword ptr [rcx + 8], rax
00864901  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00864905  4C 39 30                        cmp qword ptr [rax], r14
00864908  75 4B                           jne 0x140864955
0086490A  4C 89 33                        mov qword ptr [rbx], r14
0086490D  48 89 43 08                     mov qword ptr [rbx + 8], rax
00864911  48 89 18                        mov qword ptr [rax], rbx
00864914  49 89 5E 08                     mov qword ptr [r14 + 8], rbx
00864918  E9 75 FD FF FF                  jmp 0x140864692
0086491D  48 8B 4B 40                     mov rcx, qword ptr [rbx + 0x40]
00864921  45 33 C9                        xor r9d, r9d
00864924  48 83 C1 10                     add rcx, 0x10
00864928  8B D7                           mov edx, edi
0086492A  4C 8B C3                        mov r8, rbx
0086492D  E8 DE F5 99 FF                  call 0x140203f10
00864932  E9 5B FD FF FF                  jmp 0x140864692
00864937  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0086493B  45 33 C0                        xor r8d, r8d
0086493E  48 83 23 00                     and qword ptr [rbx], 0
00864942  33 D2                           xor edx, edx
00864944  89 78 18                        mov dword ptr [rax + 0x18], edi
00864947  48 8B 4B 40                     mov rcx, qword ptr [rbx + 0x40]
0086494B  E8 C0 A9 AD FF                  call 0x14033f310
00864950  E9 3D FD FF FF                  jmp 0x140864692
00864955  B9 03 00 00 00                  mov ecx, 3
0086495A  CD 29                           int 0x29
0086495C  80 7D 40 00                     cmp byte ptr [rbp + 0x40], 0
00864960  75 0C                           jne 0x14086496e
00864962  48 8D 0D D7 0F 69 00            lea rcx, [rip + 0x690fd7]
00864969  E8 32 BA 9E FF                  call 0x1402503a0
0086496E  48 83 7D 48 00                  cmp qword ptr [rbp + 0x48], 0
00864973  75 08                           jne 0x14086497d
00864975  48 8B CE                        mov rcx, rsi
00864978  E8 0B F2 1B 00                  call 0x140a23b88
0086497D  48 83 7D 50 00                  cmp qword ptr [rbp + 0x50], 0
00864982  75 08                           jne 0x14086498c
00864984  49 8B CE                        mov rcx, r14
00864987  E8 24 3B FE FF                  call 0x1408484b0
0086498C  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00864991  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00864996  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
0086499B  48 83 C4 40                     add rsp, 0x40
0086499F  41 5F                           pop r15
008649A1  41 5E                           pop r14
008649A3  5D                              pop rbp
008649A4  C3                              ret
008649A5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpPostNotify(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned __int8 a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    *(unsigned int *)(v_rsp + 32) = a4;
    v_rsp = (v_rsp) - (64);
    v_stack_m38 = v_xmm0;
    v_stack_m28 = v_xmm1;
    result = v_rsp;
    if (a6 == 0) {
        result = v_stack_m38;
        v_stack_m30 = result;
        result = v_stack_m38;
        v_stack_m38 = result;
    }
    v_rsi = v_stack_m38;
    if (a6 != 0) { v_rsi = a6; }
    if (a7 == 0) {
        result = v_stack_m28;
        v_stack_m20 = result;
        result = v_stack_m28;
        v_stack_m28 = result;
    }
    v_r14 = v_stack_m28;
    if (a7 != 0) { v_r14 = a7; }
    if (a5 == 0) {
        a1 = v_rip + 6886120;
        result = ExAcquireFastMutexUnsafe(a1, a2, a3, a4);
    }
    if ((*(unsigned __int64 *)(a1 + 16)) != (a1 + 16)) goto loc_0086468B;
    *(unsigned int *)(a1 + 48) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)));
    if (a5 != 0) goto loc_0086498C;
    result = ExReleaseFastMutexUnsafe(v_rip + 6886079, a2, a3, a4);
    goto loc_0086498C;
loc_0086468B:
    *(unsigned int *)(a1 + 48) = (unsigned int)(result);
loc_00864692:
    if ((*(unsigned __int64 *)(a1 + 16)) == (a1 + 16)) goto loc_0086495C;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8)) != (a1 + 16)) goto loc_00864955;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16)) + 8)) != (*(unsigned __int64 *)(a1 + 16))) goto loc_00864955;
    *(unsigned __int64 *)(a1 + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16)) + 8) = a1 + 16;
    result = Feature_2602282298__private_IsEnabledDeviceUsageNoInline(v_rip + 6886079, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00864776;
    if (((unsigned int)((unsigned int)(a4))) != 267) goto loc_00864877;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 56)) & (0x10000ULL)) != 0) goto loc_00864877;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 32) + 8)) != (*(unsigned __int64 *)(a1 + 16) + 32)) goto loc_00864955;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 32 + 8))) != (*(unsigned __int64 *)(a1 + 16) + 32)) goto loc_00864955;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 32 + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 32);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 32) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 32 + 8);
    result = 1;
    if ((*(unsigned int *)(v_rip + 7742981)) != 0) {
        a2 = 1;
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16) + 8)) != (*(unsigned __int64 *)(a1 + 16) + 16)) goto loc_00864955;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16 + 8))) != (*(unsigned __int64 *)(a1 + 16) + 16)) goto loc_00864955;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16 + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16 + 8);
    result = *(unsigned __int64 *)(a1 + 16) + 16;
    if ((*(unsigned int *)(v_rip + 7742925)) != 0) {
        a1 = 1;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    goto loc_00864856;
loc_00864776:
    if (((unsigned int)(v_cr8)) != 267) goto loc_00864877;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 56)) & (0x10000ULL)) != 0) goto loc_00864877;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 32) != 0) goto loc_008647AD;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 32 + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 32))) goto loc_008647D2;
loc_008647AD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 32) + 8)) != (*(unsigned __int64 *)(a1 + 16) + 32)) goto loc_00864955;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 32 + 8))) != (*(unsigned __int64 *)(a1 + 16) + 32)) goto loc_00864955;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 32 + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 32);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 32) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 32 + 8);
loc_008647D2:
    result = 1;
    if ((*(unsigned int *)(v_rip + 7742778)) != 0) {
        a2 = 1;
        a1 = (unsigned __int8)((unsigned __int8)(v_cr8));
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 32 + 8), a4);
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16) != 0) goto loc_00864807;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16 + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16))) goto loc_0086482C;
loc_00864807:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16) + 8)) != (*(unsigned __int64 *)(a1 + 16) + 16)) goto loc_00864955;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16 + 8))) != (*(unsigned __int64 *)(a1 + 16) + 16)) goto loc_00864955;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16 + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16 + 8);
loc_0086482C:
    result = *(unsigned __int64 *)(a1 + 16) + 16 + 8;
    if ((*(unsigned int *)(v_rip + 7742701)) != 0) {
        a1 = 1;
        a2 = (unsigned __int8)((unsigned __int8)(v_cr8));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16), a4);
    }
loc_00864856:
    if (((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 56))))) == 1) goto loc_00864692;
    result = CmpAddToDelayedDeref(*(unsigned __int64 *)(a1 + 16), v_rsi, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16), a4);
    result = CmpFreePostBlock(*(unsigned __int64 *)(a1 + 16), v_rsi, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16), a4);
    goto loc_00864692;
loc_00864877:
    if (((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 56))))) < 1) goto loc_0086489F;
loc_00864883:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 32)) - (32);
    if (result != (*(unsigned __int64 *)(a1 + 16))) goto loc_00864883;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 56) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 56)));
loc_0086489F:
    result = (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 56)));
    if (((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 56))))) != 1) {
        a2 = v_rsi;
        a1 = *(unsigned __int64 *)(a1 + 16);
        result = CmpCancelSubordinatePost(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16), a4);
        a1 = *(unsigned __int64 *)(a1 + 16);
        result = CmpAddToDelayedDeref(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16), a4);
    }
    a1 = (unsigned int)(((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 56)))) - (1));
    if (condition_is_equal) goto loc_00864937;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0086491D;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008648DC;
    if (((unsigned int)(a1)) != 1) goto loc_00864692;
loc_008648DC:
    result = CmpFreeSubordinatePost(*(unsigned __int64 *)(a1 + 16), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16), a4);
    v_rbx = (*(unsigned __int64 *)(a1 + 16)) + (16);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx) + 8)) != v_rbx) goto loc_00864955;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8))) != v_rbx) goto loc_00864955;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8)) = *(unsigned __int64 *)(v_rbx);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx) + 8) = *(unsigned __int64 *)(v_rbx + 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r14 + 8))) != v_r14) goto loc_00864955;
    *(unsigned __int64 *)(v_rbx) = v_r14;
    *(unsigned __int64 *)(v_rbx + 8) = *(unsigned __int64 *)(v_r14 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r14 + 8)) = v_rbx;
    *(unsigned __int64 *)(v_r14 + 8) = v_rbx;
    goto loc_00864692;
loc_0086491D:
    a4 = 0;
    a1 = (*(unsigned __int64 *)(v_rbx + 64)) + (16);
    result = KeInsertQueueApc(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p20))), v_rbx, a4);
    goto loc_00864692;
loc_00864937:
    a3 = 0;
    a2 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rbx + 64) + 24) = (unsigned int)((unsigned int)(v_stack_p20));
    result = KeSetEvent(*(unsigned __int64 *)(v_rbx + 64), a2, a3, a4);
    goto loc_00864692;
loc_00864955:
loc_0086495C:
    if (a5 == 0) {
        a1 = v_rip + 6885335;
        result = ExReleaseFastMutexUnsafe(a1, a2, a3, a4);
    }
    if (a6 == 0) {
        a1 = v_rsi;
        result = CmpDelayedDerefKeys(a1, a2, a3, a4);
    }
    if (a7 == 0) {
        a1 = v_r14;
        result = CmpSignalDeferredPosts(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpPostNotify(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint8_t Arg5, int64_t Arg6, int64_t Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    local_rsp = (local_rsp) - (64);
    v_stack_m38 = v_xmm0;
    v_stack_m28 = v_xmm1;
    result = local_rsp;
    if (Arg6 == 0) {
        result = v_stack_m38;
        v_stack_m30 = result;
        result = v_stack_m38;
        v_stack_m38 = result;
    }
    local_rsi = v_stack_m38;
    if (Arg6 != 0) { local_rsi = Arg6; }
    if (Arg7 == 0) {
        result = v_stack_m28;
        v_stack_m20 = result;
        result = v_stack_m28;
        v_stack_m28 = result;
    }
    local_r14 = v_stack_m28;
    if (Arg7 != 0) { local_r14 = Arg7; }
    if (Arg5 == 0) {
        Arg1 = v_rip + 6886120;
        result = ExAcquireFastMutexUnsafe(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint64_t *)(arg1 + 0x10)) != (Arg1 + 16)) goto loc_0086468B;
    *(uint32_t *)(arg1 + 0x30) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)));
    if (Arg5 != 0) goto loc_0086498C;
    result = ExReleaseFastMutexUnsafe(v_rip + 6886079, Arg2, Arg3, Arg4);
    goto loc_0086498C;
loc_0086468B:
    *(uint32_t *)(arg1 + 0x30) = (uint32_t)(result);
loc_00864692:
    if ((*(uint64_t *)(arg1 + 0x10)) == (Arg1 + 16)) goto loc_0086495C;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8)) != (Arg1 + 16)) goto loc_00864955;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10)) + 0x8)) != (*(uint64_t *)(arg1 + 0x10))) goto loc_00864955;
    *(uint64_t *)(arg1 + 0x10) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x10));
    *(void **)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10)) + 0x8) = Arg1 + 16;
    result = Feature_2602282298__private_IsEnabledDeviceUsageNoInline(v_rip + 6886079, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00864776;
    if (((uint32_t)((uint32_t)(Arg4))) != 267) goto loc_00864877;
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x38)) & (0x10000ULL)) != 0) goto loc_00864877;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x20) + 0x8)) != (*(uint64_t *)(arg1 + 0x10) + 32)) goto loc_00864955;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x20 + 0x8))) != (*(uint64_t *)(arg1 + 0x10) + 32)) goto loc_00864955;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x20 + 0x8)) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x20);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x20) + 0x8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x20 + 0x8);
    result = 1;
    if ((*(uint32_t *)(v_rip + 0x762605)) != 0) {
        Arg2 = 1;
        Arg1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10) + 0x8)) != (*(uint64_t *)(arg1 + 0x10) + 16)) goto loc_00864955;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10 + 0x8))) != (*(uint64_t *)(arg1 + 0x10) + 16)) goto loc_00864955;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10 + 0x8)) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10) + 0x8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10 + 0x8);
    result = *(uint64_t *)(arg1 + 0x10) + 16;
    if ((*(uint32_t *)(v_rip + 0x7625CD)) != 0) {
        Arg1 = 1;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
    goto loc_00864856;
loc_00864776:
    if (((uint32_t)(v_cr8)) != 267) goto loc_00864877;
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x38)) & (0x10000ULL)) != 0) goto loc_00864877;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x20) != 0) goto loc_008647AD;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x20 + 0x8)) == (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x20))) goto loc_008647D2;
loc_008647AD:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x20) + 0x8)) != (*(uint64_t *)(arg1 + 0x10) + 32)) goto loc_00864955;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x20 + 0x8))) != (*(uint64_t *)(arg1 + 0x10) + 32)) goto loc_00864955;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x20 + 0x8)) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x20);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x20) + 0x8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x20 + 0x8);
loc_008647D2:
    result = 1;
    if ((*(uint32_t *)(v_rip + 0x76253A)) != 0) {
        Arg2 = 1;
        Arg1 = (uint8_t)((uint8_t)(v_cr8));
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x20 + 0x8), Arg4);
    }
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10) != 0) goto loc_00864807;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10 + 0x8)) == (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10))) goto loc_0086482C;
loc_00864807:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10) + 0x8)) != (*(uint64_t *)(arg1 + 0x10) + 16)) goto loc_00864955;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10 + 0x8))) != (*(uint64_t *)(arg1 + 0x10) + 16)) goto loc_00864955;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10 + 0x8)) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10) + 0x8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10 + 0x8);
loc_0086482C:
    result = *(uint64_t *)(arg1 + 0x10) + 16 + 8;
    if ((*(uint32_t *)(v_rip + 0x7624ED)) != 0) {
        Arg1 = 1;
        Arg2 = (uint8_t)((uint8_t)(v_cr8));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10), Arg4);
    }
loc_00864856:
    if (((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x38))))) == 1) goto loc_00864692;
    result = CmpAddToDelayedDeref(*(uint64_t *)(arg1 + 0x10), local_rsi, *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10), Arg4);
    result = CmpFreePostBlock(*(uint64_t *)(arg1 + 0x10), local_rsi, *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10), Arg4);
    goto loc_00864692;
loc_00864877:
    if (((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x38))))) < 1) goto loc_0086489F;
loc_00864883:
    result = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x20)) - (32);
    if (result != (*(uint64_t *)(arg1 + 0x10))) goto loc_00864883;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x38) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x38)));
loc_0086489F:
    result = (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x38)));
    if (((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x38))))) != 1) {
        Arg2 = local_rsi;
        Arg1 = *(uint64_t *)(arg1 + 0x10);
        result = CmpCancelSubordinatePost(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10), Arg4);
        Arg1 = *(uint64_t *)(arg1 + 0x10);
        result = CmpAddToDelayedDeref(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10), Arg4);
    }
    Arg1 = (uint32_t)(((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x38)))) - (1));
    if (condition_is_equal) goto loc_00864937;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0086491D;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008648DC;
    if (((uint32_t)(Arg1)) != 1) goto loc_00864692;
loc_008648DC:
    result = CmpFreeSubordinatePost(*(uint64_t *)(arg1 + 0x10), Arg2, *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10), Arg4);
    local_rbx = (*(uint64_t *)(arg1 + 0x10)) + (16);
    if ((*(uint64_t *)(*(uint64_t *)(local_rbx) + 0x8)) != local_rbx) goto loc_00864955;
    if ((*(uint64_t *)(*(uint64_t *)(local_rbx + 0x8))) != local_rbx) goto loc_00864955;
    *(uint64_t *)(*(uint64_t *)(local_rbx + 0x8)) = *(uint64_t *)(local_rbx);
    *(uint64_t *)(*(uint64_t *)(local_rbx) + 0x8) = *(uint64_t *)(local_rbx + 0x8);
    if ((*(uint64_t *)(*(uint64_t *)(local_r14 + 0x8))) != local_r14) goto loc_00864955;
    *(uint64_t *)(local_rbx) = local_r14;
    *(uint64_t *)(local_rbx + 0x8) = *(uint64_t *)(local_r14 + 0x8);
    *(uint64_t *)(*(uint64_t *)(local_r14 + 0x8)) = local_rbx;
    *(uint64_t *)(local_r14 + 0x8) = local_rbx;
    goto loc_00864692;
loc_0086491D:
    Arg4 = 0;
    Arg1 = (*(uint64_t *)(local_rbx + 0x40)) + (16);
    result = KeInsertQueueApc(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p20))), local_rbx, Arg4);
    goto loc_00864692;
loc_00864937:
    Arg3 = 0;
    Arg2 = 0;
    *(uint32_t *)(*(uint64_t *)(local_rbx + 0x40) + 0x18) = (uint32_t)((uint32_t)(v_stack_p20));
    result = KeSetEvent(*(uint64_t *)(local_rbx + 0x40), Arg2, Arg3, Arg4);
    goto loc_00864692;
loc_00864955:
loc_0086495C:
    if (Arg5 == 0) {
        Arg1 = v_rip + 6885335;
        result = ExReleaseFastMutexUnsafe(Arg1, Arg2, Arg3, Arg4);
    }
    if (Arg6 == 0) {
        Arg1 = local_rsi;
        result = CmpDelayedDerefKeys(Arg1, Arg2, Arg3, Arg4);
    }
    if (Arg7 == 0) {
        Arg1 = local_r14;
        result = CmpSignalDeferredPosts(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x30` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008645D8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
