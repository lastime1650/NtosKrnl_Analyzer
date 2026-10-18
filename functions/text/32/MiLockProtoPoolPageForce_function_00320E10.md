# MiLockProtoPoolPageForce

- RVA: `0x00320E10`–`0x00321202` (길이 `1,010` bytes)
- VA: `0x0000000140320E10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000756AC`
- 디코드: `224`개 명령, `1,010/1,010` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00320EDE` → [MiSafeLockPage](MiSafeLockPage_function_00321620.md) (function, `0x00321620`)
- `0x00320F43` → [MmAccessFault](../27/MmAccessFault_function_0027EE80.md) (function, `0x0027EE80`)
- `0x00320FE2` → [MiLockOwnedProtoPage](MiLockOwnedProtoPage_function_00322560.md) (function, `0x00322560`)
- `0x00321050` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003210C7` → [MiIsPfnCommitNotCharged](../31/MiIsPfnCommitNotCharged_function_00317370.md) (function, `0x00317370`)
- `0x003210FC` → [MiChargeCommit](../28/MiChargeCommit_function_00286EB0.md) (function, `0x00286EB0`)
- `0x00321153` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00321162` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003211C8` → [MiChargePartitionResidentAvailable](../28/MiChargePartitionResidentAvailable_function_0028B000.md) (function, `0x0028B000`)
- `0x003211E7` → [MiReturnCommit](../24/MiReturnCommit_function_00248410.md) (function, `0x00248410`)
- `0x003211F8` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)

### Direct callers
- [MiInitializeNewImageSectionProtos](../2A/MiInitializeNewImageSectionProtos_function_002ABB80.md) at `0x002ABC65`
- [MiInitializeImageProtos](../2A/MiInitializeImageProtos_function_002ABDAC.md) at `0x002AC04D`
- [sub_002F6E32](../2F/Unknown_function_002F6E32.md) at `0x002F6EA1`
- [sub_002F6E32](../2F/Unknown_function_002F6E32.md) at `0x002F75FA`
- [MmCopyToCachedPage](../34/MmCopyToCachedPage_function_00347B44.md) at `0x00347E04`
- [MiPfPutPagesInTransition](../36/MiPfPutPagesInTransition_function_003640EC.md) at `0x003645D6`
- [MiMakeImageReadOnly](../49/MiMakeImageReadOnly_function_0049CB74.md) at `0x0049CC52`
- [MiDeletePerSessionProtos](../4A/MiDeletePerSessionProtos_function_004A0840.md) at `0x004A096B`
- [MiInitializeDynamicPfns](../67/MiInitializeDynamicPfns_function_00672BD0.md) at `0x00672DCA`
- [MiEliminateStaleExtents](../68/MiEliminateStaleExtents_function_006809A8.md) at `0x006809E1`
- [MiEnableLargeSubsection](../68/MiEnableLargeSubsection_function_00680BC4.md) at `0x00680C56`
- [MiFillFileOnlyProtoAsBad](../68/MiFillFileOnlyProtoAsBad_function_00680DB8.md) at `0x00680DF4`

### Static image references
- `0x00320EA5` → RVA `0x00E2DCE0` (`.data`; read)
- `0x0032103F` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0032109F` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x003210DD` → RVA `0x00E30088` (`.data`; read)
- `0x00321145` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00321184` → RVA `0x00E38D00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00320E10  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00320E15  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
00320E1A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00320E1F  57                              push rdi
00320E20  41 54                           push r12
00320E22  41 55                           push r13
00320E24  41 56                           push r14
00320E26  41 57                           push r15
00320E28  48 83 EC 20                     sub rsp, 0x20
00320E2C  4C 8B F9                        mov r15, rcx
00320E2F  4C 8B E9                        mov r13, rcx
00320E32  49 C1 EF 09                     shr r15, 9
00320E36  48 B9 F8 FF FF FF 7F 00 00 00   movabs rcx, 0x7ffffffff8
00320E40  4C 23 F9                        and r15, rcx
00320E43  4C 8B F2                        mov r14, rdx
00320E46  48 B9 00 00 00 00 80 F6 FF FF   movabs rcx, 0xfffff68000000000
00320E50  4C 03 F9                        add r15, rcx
00320E53  45 33 E4                        xor r12d, r12d
00320E56  49 B8 00 00 00 00 00 DE FF FF   movabs r8, 0xffffde0000000000
00320E60  49 B9 00 00 00 00 00 00 40 00   movabs r9, 0x40000000000000
00320E6A  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
00320E74  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
00320E7E  4D 85 F6                        test r14, r14
00320E81  74 04                           je 0x140320e87
00320E83  41 C6 06 11                     mov byte ptr [r14], 0x11
00320E87  49 8B 1F                        mov rbx, qword ptr [r15]
00320E8A  F6 C3 01                        test bl, 1
00320E8D  0F 84 A3 00 00 00               je 0x140320f36
00320E93  48 0F BA E3 09                  bt rbx, 9
00320E98  0F 82 98 00 00 00               jb 0x140320f36
00320E9E  48 C1 EB 0C                     shr rbx, 0xc
00320EA2  48 23 DA                        and rbx, rdx
00320EA5  48 3B 1D 34 CE B0 00            cmp rbx, qword ptr [rip + 0xb0ce34]
00320EAC  77 D9                           ja 0x140320e87
00320EAE  48 8D 0C 5B                     lea rcx, [rbx + rbx*2]
00320EB2  48 03 C9                        add rcx, rcx
00320EB5  48 8B C0                        mov rax, rax
00320EB8  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
00320EBC  49 85 C1                        test r9, rax
00320EBF  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
00320EC9  74 BC                           je 0x140320e87
00320ECB  49 8B C0                        mov rax, r8
00320ECE  48 8D 3C C8                     lea rdi, [rax + rcx*8]
00320ED2  4D 85 F6                        test r14, r14
00320ED5  0F 84 AF 01 00 00               je 0x14032108a
00320EDB  48 8B CB                        mov rcx, rbx
00320EDE  E8 3D 07 00 00                  call 0x140321620
00320EE3  0F B6 F0                        movzx esi, al
00320EE6  49 B8 00 00 00 00 00 DE FF FF   movabs r8, 0xffffde0000000000
00320EF0  3C 11                           cmp al, 0x11
00320EF2  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
00320EFC  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
00320F06  49 B9 00 00 00 00 00 00 40 00   movabs r9, 0x40000000000000
00320F10  0F 84 71 FF FF FF               je 0x140320e87
00320F16  49 8B 07                        mov rax, qword ptr [r15]
00320F19  A8 01                           test al, 1
00320F1B  75 30                           jne 0x140320f4d
00320F1D  40 80 FE 11                     cmp sil, 0x11
00320F21  0F 85 CA 02 00 00               jne 0x1403211f1
00320F27  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
00320F31  F0 48 21 4F 18                  lock and qword ptr [rdi + 0x18], rcx
00320F36  45 33 C9                        xor r9d, r9d
00320F39  45 33 C0                        xor r8d, r8d
00320F3C  49 8B D5                        mov rdx, r13
00320F3F  41 8D 49 02                     lea ecx, [r9 + 2]
00320F43  E8 38 DF F5 FF                  call 0x14027ee80
00320F48  E9 09 FF FF FF                  jmp 0x140320e56
00320F4D  48 0F BA E0 09                  bt rax, 9
00320F52  72 C9                           jb 0x140320f1d
00320F54  48 C1 E8 0C                     shr rax, 0xc
00320F58  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
00320F62  48 23 C2                        and rax, rdx
00320F65  48 3B D8                        cmp rbx, rax
00320F68  0F 85 9A 00 00 00               jne 0x140321008
00320F6E  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
00320F72  48 0F BA E0 28                  bt rax, 0x28
00320F77  72 47                           jb 0x140320fc0
00320F79  48 0F BA 67 28 35               bt qword ptr [rdi + 0x28], 0x35
00320F7F  72 3F                           jb 0x140320fc0
00320F81  8B 4F 20                        mov ecx, dword ptr [rdi + 0x20]
00320F84  48 BA FF FF FF FF FF FF FF 3F   movabs rdx, 0x3fffffffffffffff
00320F8E  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
00320F92  48 23 C2                        and rax, rdx
00320F95  66 85 C9                        test cx, cx
00320F98  0F 84 1A 01 00 00               je 0x1403210b8
00320F9E  66 83 F9 01                     cmp cx, 1
00320FA2  0F 85 63 01 00 00               jne 0x14032110b
00320FA8  48 85 C0                        test rax, rax
00320FAB  0F 84 85 01 00 00               je 0x140321136
00320FB1  41 BC 01 00 00 00               mov r12d, 1
00320FB7  45 85 E4                        test r12d, r12d
00320FBA  0F 85 F8 00 00 00               jne 0x1403210b8
00320FC0  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
00320FC3  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00320FC7  66 FF C0                        inc ax
00320FCA  66 89 44 24 50                  mov word ptr [rsp + 0x50], ax
00320FCF  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
00320FD3  89 47 20                        mov dword ptr [rdi + 0x20], eax
00320FD6  40 80 FE 11                     cmp sil, 0x11
00320FDA  74 03                           je 0x140320fdf
00320FDC  41 88 36                        mov byte ptr [r14], sil
00320FDF  48 8B CF                        mov rcx, rdi
00320FE2  E8 79 15 00 00                  call 0x140322560
00320FE7  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
00320FEC  48 8B C7                        mov rax, rdi
00320FEF  48 8B 6C 24 60                  mov rbp, qword ptr [rsp + 0x60]
00320FF4  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00320FF9  48 83 C4 20                     add rsp, 0x20
00320FFD  41 5F                           pop r15
00320FFF  41 5E                           pop r14
00321001  41 5D                           pop r13
00321003  41 5C                           pop r12
00321005  5F                              pop rdi
00321006  C3                              ret
00321007  CC                              int3
00321008  49 BA FF FF FF FF FF FF FF 7F   movabs r10, 0x7fffffffffffffff
00321012  F0 4C 21 57 18                  lock and qword ptr [rdi + 0x18], r10
00321017  49 B8 00 00 00 00 00 DE FF FF   movabs r8, 0xffffde0000000000
00321021  49 B9 00 00 00 00 00 00 40 00   movabs r9, 0x40000000000000
0032102B  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
00321035  40 80 FE 01                     cmp sil, 1
00321039  0F 87 48 FE FF FF               ja 0x140320e87
0032103F  44 39 25 DA 5C CA 00            cmp dword ptr [rip + 0xca5cda], r12d
00321046  74 17                           je 0x14032105f
00321048  44 0F 20 C1                     mov rcx, cr8
0032104C  40 0F B6 D6                     movzx edx, sil
00321050  E8 43 46 1D 00                  call 0x1404f5698
00321055  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
0032105F  40 0F B6 C6                     movzx eax, sil
00321063  44 0F 22 C0                     mov cr8, rax
00321067  49 B8 00 00 00 00 00 DE FF FF   movabs r8, 0xffffde0000000000
00321071  49 B9 00 00 00 00 00 00 40 00   movabs r9, 0x40000000000000
0032107B  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
00321085  E9 FD FD FF FF                  jmp 0x140320e87
0032108A  40 B6 11                        mov sil, 0x11
0032108D  41 8B EC                        mov ebp, r12d
00321090  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
00321097  0F 83 79 FE FF FF               jae 0x140320f16
0032109D  FF C5                           inc ebp
0032109F  85 2D 07 42 CA 00               test dword ptr [rip + 0xca4207], ebp
003210A5  0F 84 9A 00 00 00               je 0x140321145
003210AB  F3 90                           pause
003210AD  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
003210B1  48 85 C0                        test rax, rax
003210B4  79 DA                           jns 0x140321090
003210B6  EB E5                           jmp 0x14032109d
003210B8  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
003210BC  40 32 ED                        xor bpl, bpl
003210BF  48 85 C0                        test rax, rax
003210C2  78 66                           js 0x14032112a
003210C4  48 8B CF                        mov rcx, rdi
003210C7  E8 A4 62 FF FF                  call 0x140317370
003210CC  85 C0                           test eax, eax
003210CE  0F 84 98 00 00 00               je 0x14032116c
003210D4  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
003210D8  BA 01 00 00 00                  mov edx, 1
003210DD  48 8B 05 A4 EF B0 00            mov rax, qword ptr [rip + 0xb0efa4]
003210E4  40 B5 01                        mov bpl, 1
003210E7  48 C1 E9 2B                     shr rcx, 0x2b
003210EB  81 E1 FF 03 00 00               and ecx, 0x3ff
003210F1  44 8D 42 03                     lea r8d, [rdx + 3]
003210F5  48 8B 1C C8                     mov rbx, qword ptr [rax + rcx*8]
003210F9  48 8B CB                        mov rcx, rbx
003210FC  E8 AF 5D F6 FF                  call 0x140286eb0
00321101  85 C0                           test eax, eax
00321103  0F 84 CD FE FF FF               je 0x140320fd6
00321109  EB 79                           jmp 0x140321184
0032110B  66 83 F9 02                     cmp cx, 2
0032110F  0F 85 AB FE FF FF               jne 0x140320fc0
00321115  48 85 C0                        test rax, rax
00321118  0F 84 A2 FE FF FF               je 0x140320fc0
0032111E  F6 47 22 08                     test byte ptr [rdi + 0x22], 8
00321122  0F 84 98 FE FF FF               je 0x140320fc0
00321128  EB 8E                           jmp 0x1403210b8
0032112A  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
0032112D  48 0F BA E0 0A                  bt rax, 0xa
00321132  72 A0                           jb 0x1403210d4
00321134  EB 8E                           jmp 0x1403210c4
00321136  F6 47 22 08                     test byte ptr [rdi + 0x22], 8
0032113A  0F 84 77 FE FF FF               je 0x140320fb7
00321140  E9 6C FE FF FF                  jmp 0x140320fb1
00321145  8B 05 6D 59 CA 00               mov eax, dword ptr [rip + 0xca596d]
0032114B  A8 40                           test al, 0x40
0032114D  0F 84 58 FF FF FF               je 0x1403210ab
00321153  E8 38 E3 FE FF                  call 0x14030f490
00321158  84 C0                           test al, al
0032115A  0F 84 4B FF FF FF               je 0x1403210ab
00321160  8B CD                           mov ecx, ebp
00321162  E8 F9 E2 FE FF                  call 0x14030f460
00321167  E9 41 FF FF FF                  jmp 0x1403210ad
0032116C  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
00321170  48 8B 0D 11 EF B0 00            mov rcx, qword ptr [rip + 0xb0ef11]
00321177  48 C1 E8 2B                     shr rax, 0x2b
0032117B  25 FF 03 00 00                  and eax, 0x3ff
00321180  48 8B 1C C1                     mov rbx, qword ptr [rcx + rax*8]
00321184  48 8D 05 75 7B B1 00            lea rax, [rip + 0xb17b75]
0032118B  48 3B D8                        cmp rbx, rax
0032118E  75 2A                           jne 0x1403211ba
00321190  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
00321199  8B 82 9C 8B 00 00               mov eax, dword ptr [rdx + 0x8b9c]
0032119F  8D 48 FF                        lea ecx, [rax - 1]
003211A2  83 F9 FD                        cmp ecx, -3
003211A5  77 13                           ja 0x1403211ba
003211A7  8D 48 FF                        lea ecx, [rax - 1]
003211AA  F0 0F B1 8A 9C 8B 00 00         lock cmpxchg dword ptr [rdx + 0x8b9c], ecx
003211B2  0F 84 08 FE FF FF               je 0x140320fc0
003211B8  EB E5                           jmp 0x14032119f
003211BA  BA 01 00 00 00                  mov edx, 1
003211BF  41 B8 FF FF FF FF               mov r8d, 0xffffffff
003211C5  48 8B CB                        mov rcx, rbx
003211C8  E8 33 9E F6 FF                  call 0x14028b000
003211CD  85 C0                           test eax, eax
003211CF  0F 85 EB FD FF FF               jne 0x140320fc0
003211D5  40 84 ED                        test bpl, bpl
003211D8  0F 84 F8 FD FF FF               je 0x140320fd6
003211DE  45 33 C0                        xor r8d, r8d
003211E1  8D 50 01                        lea edx, [rax + 1]
003211E4  48 8B CB                        mov rcx, rbx
003211E7  E8 24 72 F2 FF                  call 0x140248410
003211EC  E9 E5 FD FF FF                  jmp 0x140320fd6
003211F1  40 0F B6 D6                     movzx edx, sil
003211F5  48 8B CF                        mov rcx, rdi
003211F8  E8 E3 91 FF FF                  call 0x14031a3e0
003211FD  E9 34 FD FF FF                  jmp 0x140320f36
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiLockProtoPoolPageForce(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_r15 = (a1) >> (9);
    v_r15 = (v_r15) & (a1);
    v_r15 = (v_r15) + (a1);
    v_r12 = 0;
loc_00320E56:
    if (a2 != 0) {
        *(unsigned __int8 *)(a2) = 17;
    }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (1)) == 0) goto loc_00320F36;
    if (condition_is_below) goto loc_00320F36;
    v_rbx = (*(unsigned __int64 *)(v_r15)) >> (12);
    v_rbx = (v_rbx) & (a2);
    if (v_rbx > (*(unsigned __int64 *)(v_rip + 11587124))) goto loc_00320E87;
    a1 = (v_rbx + v_rbx * 2) + (v_rbx + v_rbx * 2);
    if (((a4) & (*(unsigned __int64 *)(result + a1 * 8))) == 0) goto loc_00320E87;
    if (a2 == 0) goto loc_0032108A;
    result = MiSafeLockPage(v_rbx, a2, a3, a4);
    if (((unsigned __int8)(result)) == 17) goto loc_00320E87;
loc_00320F16:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (1)) != 0) goto loc_00320F4D;
loc_00320F1D:
    if (((unsigned __int8)((unsigned __int8)(result))) != 17) goto loc_003211F1;
loc_00320F36:
    a4 = 0;
    a3 = 0;
    result = MmAccessFault(a4 + 2, a1, a3, a4);
    goto loc_00320E56;
loc_00320F4D:
    if (condition_is_below) goto loc_00320F1D;
    result = (result) >> (12);
    result = (result) & (a1);
    if (v_rbx != result) goto loc_00321008;
    if (v_rbx < result) goto loc_00320FC0;
    if (v_rbx < result) goto loc_00320FC0;
    result = (*(unsigned __int64 *)(a3 + a1 * 8 + 24)) & (a1);
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(a3 + a1 * 8 + 32))) == 0) goto loc_003210B8;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(a3 + a1 * 8 + 32)))) != 1) goto loc_0032110B;
    if (result == 0) goto loc_00321136;
loc_00320FB1:
loc_00320FB7:
    if (1 != 0) goto loc_003210B8;
loc_00320FC0:
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + a1 * 8 + 32)));
    result = (unsigned __int16)(((unsigned int)(*(unsigned int *)(a3 + a1 * 8 + 32))) + 1);
    v_stack_p8 = (unsigned __int16)(result);
    *(unsigned int *)(a3 + a1 * 8 + 32) = (unsigned int)((unsigned int)(v_stack_p8));
loc_00320FD6:
    if (((unsigned __int8)((unsigned __int8)(result))) != 17) {
        *(unsigned __int8 *)(a2) = (unsigned __int8)((unsigned __int8)(result));
    }
    result = MiLockOwnedProtoPage(a3 + a1 * 8, a1, a3, a4);
    v_rsp = (v_rsp) + (32);
    return a3 + a1 * 8;
loc_00321008:
    if (((unsigned __int8)(v_stack_p20)) > 1) goto loc_00320E87;
    result = a3 + a1 * 8;
    if ((*(unsigned int *)(v_rip + 13262042)) != 1) {
        a1 = v_cr8;
        a2 = (unsigned __int8)(v_stack_p20);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    goto loc_00320E87;
loc_0032108A:
loc_00321090:
    if ((*(unsigned int *)(v_rip + 13262042)) >= 1) goto loc_00320F16;
loc_0032109D:
    v_rbp = (unsigned int)((1) + 1);
    if (((*(unsigned int *)(v_rip + 13255175)) & ((unsigned int)(v_rbp))) == 0) goto loc_00321145;
loc_003210AB:
loc_003210AD:
    if (!sign_flag) goto loc_00321090;
    goto loc_0032109D;
loc_003210B8:
    v_rbp = 0;
    if (sign_flag) goto loc_0032112A;
loc_003210C4:
    result = MiIsPfnCommitNotCharged(a3 + a1 * 8, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0032116C;
loc_003210D4:
    a1 = (*(unsigned __int64 *)(a3 + a1 * 8 + 40)) >> (43);
    a1 = (unsigned int)((a1) & (0x3FFULL));
    result = MiChargeCommit(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11595684) + a1 * 8), 1, 1 + 3, a4);
    if ((unsigned int)(result) == 0) goto loc_00320FD6;
    goto loc_00321184;
loc_0032110B:
    if (((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11595684) + a1 * 8))) != 2) goto loc_00320FC0;
    if (result == 0) goto loc_00320FC0;
    if (((*(unsigned __int8 *)(a3 + a1 * 8 + 34)) & (8)) == 0) goto loc_00320FC0;
    goto loc_003210B8;
loc_0032112A:
    if (condition_is_below) goto loc_003210D4;
    goto loc_003210C4;
loc_00321136:
    if (((*(unsigned __int8 *)(a3 + a1 * 8 + 34)) & (8)) == 0) goto loc_00320FB7;
    goto loc_00320FB1;
loc_00321145:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13261165)))) & (64)) == 0) goto loc_003210AB;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11595684) + a1 * 8), 1, 1 + 3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_003210AB;
    result = HvlNotifyLongSpinWait(1, 1, 1 + 3, a4);
    goto loc_003210AD;
loc_0032116C:
    result = (*(unsigned __int64 *)(a3 + a1 * 8 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
loc_00321184:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11595537) + result * 8)) != (v_rip + 11631477)) goto loc_003211BA;
loc_0032119F:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35740)) - 1)) > -3) goto loc_003211BA;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35740)) - 1)) == -3) goto loc_00320FC0;
    goto loc_0032119F;
loc_003211BA:
    result = MiChargePartitionResidentAvailable(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11595537) + result * 8), 1, (unsigned int)(0xFFFFFFFFULL), a4);
    if ((unsigned int)(result) != 0) goto loc_00320FC0;
    if (1 == 0) goto loc_00320FD6;
    a3 = 0;
    result = MiReturnCommit(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11595537) + result * 8), result + 1, a3, a4);
    goto loc_00320FD6;
loc_003211F1:
    result = MiUnlockPage(a3 + a1 * 8, 17, a3, a4);
    goto loc_00320F36;
}
```

## 5. (Beta) C Style

```c
int64_t MiLockProtoPoolPageForce(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_r15 = (Arg1) >> (9);
    local_r15 = (local_r15) & (Arg1);
    local_r15 = (local_r15) + (Arg1);
    local_r12 = 0;
loc_00320E56:
    if (Arg2 != 0) {
        *(uint8_t *)(Arg2) = 17;
    }
    if ((((uint8_t)(*(uint64_t *)(local_r15))) & (1)) == 0) goto loc_00320F36;
    if (condition_is_below) goto loc_00320F36;
    local_rbx = (*(uint64_t *)(local_r15)) >> (12);
    local_rbx = (local_rbx) & (Arg2);
    if (local_rbx > (*(uint64_t *)(v_rip + 0xB0CE34))) goto loc_00320E87;
    Arg1 = (local_rbx + local_rbx * 2) + (local_rbx + local_rbx * 2);
    if (((a4) & (*(uint64_t *)(result + Arg1 * 8))) == 0) goto loc_00320E87;
    if (Arg2 == 0) goto loc_0032108A;
    result = MiSafeLockPage(local_rbx, Arg2, a3, a4);
    if (((uint8_t)(result)) == 17) goto loc_00320E87;
loc_00320F16:
    if ((((uint8_t)(*(uint64_t *)(local_r15))) & (1)) != 0) goto loc_00320F4D;
loc_00320F1D:
    if (((uint8_t)((uint8_t)(result))) != 17) goto loc_003211F1;
loc_00320F36:
    a4 = 0;
    a3 = 0;
    result = MmAccessFault(a4 + 2, Arg1, a3, a4);
    goto loc_00320E56;
loc_00320F4D:
    if (condition_is_below) goto loc_00320F1D;
    result = (result) >> (12);
    result = (result) & (Arg1);
    if (local_rbx != result) goto loc_00321008;
    if (local_rbx < result) goto loc_00320FC0;
    if (local_rbx < result) goto loc_00320FC0;
    result = (*(uint64_t *)(a3 + Arg1 * 8 + 0x18)) & (Arg1);
    if ((uint16_t)((uint32_t)(*(uint32_t *)(a3 + Arg1 * 8 + 0x20))) == 0) goto loc_003210B8;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(a3 + Arg1 * 8 + 0x20)))) != 1) goto loc_0032110B;
    if (result == 0) goto loc_00321136;
loc_00320FB1:
loc_00320FB7:
    if (1 != 0) goto loc_003210B8;
loc_00320FC0:
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(a3 + Arg1 * 8 + 0x20)));
    result = (uint16_t)(((uint32_t)(*(uint32_t *)(a3 + Arg1 * 8 + 0x20))) + 1);
    v_stack_p8 = (uint16_t)(result);
    *(uint32_t *)(a3 + Arg1 * 8 + 0x20) = (uint32_t)((uint32_t)(v_stack_p8));
loc_00320FD6:
    if (((uint8_t)((uint8_t)(result))) != 17) {
        *(uint8_t *)(Arg2) = (uint8_t)((uint8_t)(result));
    }
    result = MiLockOwnedProtoPage(a3 + Arg1 * 8, Arg1, a3, a4);
    local_rsp = (local_rsp) + (32);
    return a3 + Arg1 * 8;
loc_00321008:
    if (((uint8_t)(v_stack_p20)) > 1) goto loc_00320E87;
    result = a3 + Arg1 * 8;
    if ((*(uint32_t *)(v_rip + 0xCA5CDA)) != 1) {
        Arg1 = v_cr8;
        Arg2 = (uint8_t)(v_stack_p20);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, a3, a4);
    }
    goto loc_00320E87;
loc_0032108A:
loc_00321090:
    if ((*(uint32_t *)(v_rip + 0xCA5CDA)) >= 1) goto loc_00320F16;
loc_0032109D:
    local_rbp = (uint32_t)((1) + 1);
    if (((*(uint32_t *)(v_rip + 0xCA4207)) & ((uint32_t)(local_rbp))) == 0) goto loc_00321145;
loc_003210AB:
loc_003210AD:
    if (!sign_flag) goto loc_00321090;
    goto loc_0032109D;
loc_003210B8:
    local_rbp = 0;
    if (sign_flag) goto loc_0032112A;
loc_003210C4:
    result = MiIsPfnCommitNotCharged(a3 + Arg1 * 8, Arg2, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_0032116C;
loc_003210D4:
    Arg1 = (*(uint64_t *)(a3 + Arg1 * 8 + 0x28)) >> (43);
    Arg1 = (uint32_t)((Arg1) & (0x3FFULL));
    result = MiChargeCommit(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0EFA4) + Arg1 * 8), 1, 1 + 3, a4);
    if ((uint32_t)(result) == 0) goto loc_00320FD6;
    goto loc_00321184;
loc_0032110B:
    if (((uint16_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0EFA4) + Arg1 * 8))) != 2) goto loc_00320FC0;
    if (result == 0) goto loc_00320FC0;
    if (((*(uint8_t *)(a3 + Arg1 * 8 + 0x22)) & (8)) == 0) goto loc_00320FC0;
    goto loc_003210B8;
loc_0032112A:
    if (condition_is_below) goto loc_003210D4;
    goto loc_003210C4;
loc_00321136:
    if (((*(uint8_t *)(a3 + Arg1 * 8 + 0x22)) & (8)) == 0) goto loc_00320FB7;
    goto loc_00320FB1;
loc_00321145:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCA596D)))) & (64)) == 0) goto loc_003210AB;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0EFA4) + Arg1 * 8), 1, 1 + 3, a4);
    if ((uint8_t)(result) == 0) goto loc_003210AB;
    result = HvlNotifyLongSpinWait(1, 1, 1 + 3, a4);
    goto loc_003210AD;
loc_0032116C:
    result = (*(uint64_t *)(a3 + Arg1 * 8 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
loc_00321184:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0EF11) + result * 8)) != (v_rip + 11631477)) goto loc_003211BA;
loc_0032119F:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B9C)) - 1)) > -3) goto loc_003211BA;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B9C)) - 1)) == -3) goto loc_00320FC0;
    goto loc_0032119F;
loc_003211BA:
    result = MiChargePartitionResidentAvailable(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0EF11) + result * 8), 1, (uint32_t)(0xFFFFFFFFULL), a4);
    if ((uint32_t)(result) != 0) goto loc_00320FC0;
    if (1 == 0) goto loc_00320FD6;
    a3 = 0;
    result = MiReturnCommit(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0EF11) + result * 8), result + 1, a3, a4);
    goto loc_00320FD6;
loc_003211F1:
    result = MiUnlockPage(a3 + Arg1 * 8, 17, a3, a4);
    goto loc_00320F36;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00320E10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
