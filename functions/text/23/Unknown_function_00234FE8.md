# sub_00234FE8

- RVA: `0x00234FE8`–`0x00235343` (길이 `859` bytes)
- VA: `0x0000000140234FE8`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060640`
- 디코드: `202`개 명령, `859/859` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00234FF6` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00235006` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0023501E` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0023502D` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00235189` → [KiProcessExpiredTimerList](KiProcessExpiredTimerList_function_00234200.md) (function, `0x00234200`)
- `0x002351BC` → [KiProcessExpiredTimerList](KiProcessExpiredTimerList_function_00234200.md) (function, `0x00234200`)
- `0x0023522F` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0023523F` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0023525C` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0023526C` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00235284` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00235294` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002352AF` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002352BF` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002352D7` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002352E2` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002352FF` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0023530F` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00234FE8` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00235063` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **27**
  - `0x00234FF0` → [sub_00234B6E + 0x1B](Unknown_function_00234B6E.md) (`tail-transfer`)
  - `0x00234FFD` → [sub_00234B6E + 0x1B](Unknown_function_00234B6E.md) (`tail-transfer`)
  - `0x0023500B` → [sub_00234B6E + 0x1D](Unknown_function_00234B6E.md) (`tail-transfer`)
  - `0x00235018` → [sub_00234B6E + 0x7C](Unknown_function_00234B6E.md) (`tail-transfer`)
  - `0x00235025` → [sub_00234B6E + 0x7C](Unknown_function_00234B6E.md) (`tail-transfer`)
  - `0x00235032` → [sub_00234B6E + 0x7E](Unknown_function_00234B6E.md) (`tail-transfer`)
  - `0x00235049` → [sub_00234B6E + 0x346](Unknown_function_00234B6E.md) (`tail-transfer`)
  - `0x0023509B` → [sub_00234B6E + 0x326](Unknown_function_00234B6E.md) (`tail-transfer`)
  - `0x002350DC` → [sub_00234B6E + 0x40D](Unknown_function_00234B6E.md) (`tail-transfer`)
  - `0x00235140` → [sub_00234B6E + 0x3F0](Unknown_function_00234B6E.md) (`tail-transfer`)
  - `0x00235149` → [sub_002348D3 + 0x160](Unknown_function_002348D3.md) (`tail-transfer`)
  - `0x0023514F` → [sub_002348D3 + 0x13A](Unknown_function_002348D3.md) (`tail-transfer`)
  - `0x00235158` → [sub_002348D3 + 0x1FF](Unknown_function_002348D3.md) (`tail-transfer`)
  - `0x0023515E` → [sub_002348D3 + 0x1D9](Unknown_function_002348D3.md) (`tail-transfer`)
  - `0x00235167` → [sub_00234B6E + 0x2F](Unknown_function_00234B6E.md) (`tail-transfer`)
  - `0x00235196` → [sub_002348D3 + 0x13E](Unknown_function_002348D3.md) (`tail-transfer`)
  - `0x0023519F` → [sub_00234B6E + 0x95](Unknown_function_00234B6E.md) (`tail-transfer`)
  - `0x002351C9` → [sub_002348D3 + 0x1DD](Unknown_function_002348D3.md) (`tail-transfer`)
  - `0x002351EE` → [sub_00234B6E + 0x2A0](Unknown_function_00234B6E.md) (`tail-transfer`)
  - `0x0023521C` → [sub_00234B6E + 0x241](Unknown_function_00234B6E.md) (`tail-transfer`)
  - `0x00235229` → [sub_00234B6E + 0x31A](Unknown_function_00234B6E.md) (`tail-transfer`)
  - `0x00235249` → [sub_00234B6E + 0x31C](Unknown_function_00234B6E.md) (`tail-transfer`)
  - `0x00235256` → [sub_00234B6E + 0x3E1](Unknown_function_00234B6E.md) (`tail-transfer`)
  - `0x00235263` → [sub_00234B6E + 0x3E1](Unknown_function_00234B6E.md) (`tail-transfer`)
  - `0x00235271` → [sub_00234B6E + 0x3E3](Unknown_function_00234B6E.md) (`tail-transfer`)
  - `0x00235322` → [sub_002348D3 + 0x25B](Unknown_function_002348D3.md) (`tail-transfer`)
  - `0x0023532C` → [sub_00234B6E + 0x31A](Unknown_function_00234B6E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00234FE8  8B 05 CA 1A D9 00               mov eax, dword ptr [rip + 0xd91aca]
00234FEE  A8 40                           test al, 0x40
00234FF0  0F 84 93 FB FF FF               je 0x140234b89
00234FF6  E8 95 A4 0D 00                  call 0x14030f490
00234FFB  84 C0                           test al, al
00234FFD  0F 84 86 FB FF FF               je 0x140234b89
00235003  41 8B CC                        mov ecx, r12d
00235006  E8 55 A4 0D 00                  call 0x14030f460
0023500B  E9 7B FB FF FF                  jmp 0x140234b8b
00235010  8B 05 A2 1A D9 00               mov eax, dword ptr [rip + 0xd91aa2]
00235016  A8 40                           test al, 0x40
00235018  0F 84 CC FB FF FF               je 0x140234bea
0023501E  E8 6D A4 0D 00                  call 0x14030f490
00235023  84 C0                           test al, al
00235025  0F 84 BF FB FF FF               je 0x140234bea
0023502B  8B CD                           mov ecx, ebp
0023502D  E8 2E A4 0D 00                  call 0x14030f460
00235032  E9 B5 FB FF FF                  jmp 0x140234bec
00235037  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
0023503D  48 8B CB                        mov rcx, rbx
00235040  73 04                           jae 0x140235046
00235042  F3 90                           pause
00235044  EB 09                           jmp 0x14023504f
00235046  48 85 DB                        test rbx, rbx
00235049  0F 85 65 FE FF FF               jne 0x140234eb4
0023504F  F0 49 83 24 24 00               lock and qword ptr [r12], 0
00235055  45 33 E4                        xor r12d, r12d
00235058  F0 48 0F BA 29 00               lock bts qword ptr [rcx], 0
0023505E  73 1C                           jae 0x14023507c
00235060  41 FF C4                        inc r12d
00235063  44 85 25 42 02 D9 00            test dword ptr [rip + 0xd90242], r12d
0023506A  0F 84 06 02 00 00               je 0x140235276
00235070  F3 90                           pause
00235072  48 8B 01                        mov rax, qword ptr [rcx]
00235075  48 85 C0                        test rax, rax
00235078  74 DE                           je 0x140235058
0023507A  EB E4                           jmp 0x140235060
0023507C  44 8B 64 24 34                  mov r12d, dword ptr [rsp + 0x34]
00235081  49 81 C4 10 01 00 00            add r12, 0x110
00235088  49 C1 E4 05                     shl r12, 5
0023508C  4C 03 64 24 48                  add r12, qword ptr [rsp + 0x48]
00235091  45 33 ED                        xor r13d, r13d
00235094  F0 49 0F BA 2C 24 00            lock bts qword ptr [r12], 0
0023509B  0F 83 F3 FD FF FF               jae 0x140234e94
002350A1  41 FF C5                        inc r13d
002350A4  44 85 2D 01 02 D9 00            test dword ptr [rip + 0xd90201], r13d
002350AB  0F 84 F0 01 00 00               je 0x1402352a1
002350B1  F3 90                           pause
002350B3  49 8B 04 24                     mov rax, qword ptr [r12]
002350B7  48 85 C0                        test rax, rax
002350BA  74 D8                           je 0x140235094
002350BC  EB E3                           jmp 0x1402350a1
002350BE  8B 4C 24 38                     mov ecx, dword ptr [rsp + 0x38]
002350C2  48 83 C1 10                     add rcx, 0x10
002350C6  48 C1 E1 05                     shl rcx, 5
002350CA  49 03 CA                        add rcx, r10
002350CD  F0 48 0F BA 29 00               lock bts qword ptr [rcx], 0
002350D3  73 04                           jae 0x1402350d9
002350D5  F3 90                           pause
002350D7  EB 09                           jmp 0x1402350e2
002350D9  48 85 C9                        test rcx, rcx
002350DC  0F 85 99 FE FF FF               jne 0x140234f7b
002350E2  F0 48 83 65 00 00               lock and qword ptr [rbp], 0
002350E8  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
002350ED  33 ED                           xor ebp, ebp
002350EF  F0 48 0F BA 29 00               lock bts qword ptr [rcx], 0
002350F5  73 1A                           jae 0x140235111
002350F7  FF C5                           inc ebp
002350F9  85 2D AD 01 D9 00               test dword ptr [rip + 0xd901ad], ebp
002350FF  0F 84 C4 01 00 00               je 0x1402352c9
00235105  F3 90                           pause
00235107  48 8B 01                        mov rax, qword ptr [rcx]
0023510A  48 85 C0                        test rax, rax
0023510D  74 E0                           je 0x1402350ef
0023510F  EB E6                           jmp 0x1402350f7
00235111  48 8B EB                        mov rbp, rbx
00235114  45 33 E4                        xor r12d, r12d
00235117  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
0023511D  73 1C                           jae 0x14023513b
0023511F  41 FF C4                        inc r12d
00235122  44 85 25 83 01 D9 00            test dword ptr [rip + 0xd90183], r12d
00235129  0F 84 C2 01 00 00               je 0x1402352f1
0023512F  F3 90                           pause
00235131  48 8B 03                        mov rax, qword ptr [rbx]
00235134  48 85 C0                        test rax, rax
00235137  74 DE                           je 0x140235117
00235139  EB E4                           jmp 0x14023511f
0023513B  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00235140  E9 19 FE FF FF                  jmp 0x140234f5e
00235145  48 39 73 18                     cmp qword ptr [rbx + 0x18], rsi
00235149  0F 87 E4 F8 FF FF               ja 0x140234a33
0023514F  E9 B9 F8 FF FF                  jmp 0x140234a0d
00235154  48 39 73 18                     cmp qword ptr [rbx + 0x18], rsi
00235158  0F 87 74 F9 FF FF               ja 0x140234ad2
0023515E  E9 49 F9 FF FF                  jmp 0x140234aac
00235163  41 83 F8 40                     cmp r8d, 0x40
00235167  0F 85 30 FA FF FF               jne 0x140234b9d
0023516D  F0 49 83 24 24 00               lock and qword ptr [r12], 0
00235173  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
00235178  45 8B C8                        mov r9d, r8d
0023517B  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
00235183  4D 8B C4                        mov r8, r12
00235186  49 8B CE                        mov rcx, r14
00235189  E8 72 F0 FF FF                  call 0x140234200
0023518E  45 33 C0                        xor r8d, r8d
00235191  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
00235196  E9 76 F8 FF FF                  jmp 0x140234a11
0023519B  41 83 F8 40                     cmp r8d, 0x40
0023519F  0F 85 5E FA FF FF               jne 0x140234c03
002351A5  F0 48 83 65 00 00               lock and qword ptr [rbp], 0
002351AB  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
002351B3  45 8B C8                        mov r9d, r8d
002351B6  4D 8B C2                        mov r8, r10
002351B9  49 8B CE                        mov rcx, r14
002351BC  E8 3F F0 FF FF                  call 0x140234200
002351C1  45 33 C0                        xor r8d, r8d
002351C4  44 89 44 24 34                  mov dword ptr [rsp + 0x34], r8d
002351C9  E9 E2 F8 FF FF                  jmp 0x140234ab0
002351CE  45 0F B6 89 D1 BF FF FF         movzx r9d, byte ptr [r9 - 0x402f]
002351D6  4C 8D 6B 08                     lea r13, [rbx + 8]
002351DA  48 C1 E0 06                     shl rax, 6
002351DE  4C 03 D0                        add r10, rax
002351E1  41 8B C1                        mov eax, r9d
002351E4  F0 49 0F B3 02                  lock btr qword ptr [r10], rax
002351E9  F0 48 83 21 00                  lock and qword ptr [rcx], 0
002351EE  E9 1B FC FF FF                  jmp 0x140234e0e
002351F3  41 0F B6 82 D1 BF FF FF         movzx eax, byte ptr [r10 - 0x402f]
002351FB  4C 8D 63 08                     lea r12, [rbx + 8]
002351FF  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00235203  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
00235207  48 C1 E0 06                     shl rax, 6
0023520B  4C 03 C8                        add r9, rax
0023520E  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
00235212  F0 49 0F B3 01                  lock btr qword ptr [r9], rax
00235217  F0 48 83 21 00                  lock and qword ptr [rcx], 0
0023521C  E9 8E FB FF FF                  jmp 0x140234daf
00235221  8B 05 91 18 D9 00               mov eax, dword ptr [rip + 0xd91891]
00235227  A8 40                           test al, 0x40
00235229  0F 84 59 FC FF FF               je 0x140234e88
0023522F  E8 5C A2 0D 00                  call 0x14030f490
00235234  84 C0                           test al, al
00235236  0F 84 EB 00 00 00               je 0x140235327
0023523C  41 8B CD                        mov ecx, r13d
0023523F  E8 1C A2 0D 00                  call 0x14030f460
00235244  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00235249  E9 3C FC FF FF                  jmp 0x140234e8a
0023524E  8B 05 64 18 D9 00               mov eax, dword ptr [rip + 0xd91864]
00235254  A8 40                           test al, 0x40
00235256  0F 84 F3 FC FF FF               je 0x140234f4f
0023525C  E8 2F A2 0D 00                  call 0x14030f490
00235261  84 C0                           test al, al
00235263  0F 84 E6 FC FF FF               je 0x140234f4f
00235269  41 8B CC                        mov ecx, r12d
0023526C  E8 EF A1 0D 00                  call 0x14030f460
00235271  E9 DB FC FF FF                  jmp 0x140234f51
00235276  8B 05 3C 18 D9 00               mov eax, dword ptr [rip + 0xd9183c]
0023527C  A8 40                           test al, 0x40
0023527E  0F 84 EC FD FF FF               je 0x140235070
00235284  E8 07 A2 0D 00                  call 0x14030f490
00235289  84 C0                           test al, al
0023528B  0F 84 A0 00 00 00               je 0x140235331
00235291  41 8B CC                        mov ecx, r12d
00235294  E8 C7 A1 0D 00                  call 0x14030f460
00235299  48 8B CB                        mov rcx, rbx
0023529C  E9 D1 FD FF FF                  jmp 0x140235072
002352A1  8B 05 11 18 D9 00               mov eax, dword ptr [rip + 0xd91811]
002352A7  A8 40                           test al, 0x40
002352A9  0F 84 02 FE FF FF               je 0x1402350b1
002352AF  E8 DC A1 0D 00                  call 0x14030f490
002352B4  84 C0                           test al, al
002352B6  0F 84 F5 FD FF FF               je 0x1402350b1
002352BC  41 8B CD                        mov ecx, r13d
002352BF  E8 9C A1 0D 00                  call 0x14030f460
002352C4  E9 EA FD FF FF                  jmp 0x1402350b3
002352C9  8B 05 E9 17 D9 00               mov eax, dword ptr [rip + 0xd917e9]
002352CF  A8 40                           test al, 0x40
002352D1  0F 84 2E FE FF FF               je 0x140235105
002352D7  E8 B4 A1 0D 00                  call 0x14030f490
002352DC  84 C0                           test al, al
002352DE  74 59                           je 0x140235339
002352E0  8B CD                           mov ecx, ebp
002352E2  E8 79 A1 0D 00                  call 0x14030f460
002352E7  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
002352EC  E9 16 FE FF FF                  jmp 0x140235107
002352F1  8B 05 C1 17 D9 00               mov eax, dword ptr [rip + 0xd917c1]
002352F7  A8 40                           test al, 0x40
002352F9  0F 84 30 FE FF FF               je 0x14023512f
002352FF  E8 8C A1 0D 00                  call 0x14030f490
00235304  84 C0                           test al, al
00235306  0F 84 23 FE FF FF               je 0x14023512f
0023530C  41 8B CC                        mov ecx, r12d
0023530F  E8 4C A1 0D 00                  call 0x14030f460
00235314  E9 18 FE FF FF                  jmp 0x140235131
00235319  2B C1                           sub eax, ecx
0023531B  41 89 86 68 86 00 00            mov dword ptr [r14 + 0x8668], eax
00235322  E9 07 F8 FF FF                  jmp 0x140234b2e
00235327  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0023532C  E9 57 FB FF FF                  jmp 0x140234e88
00235331  48 8B CB                        mov rcx, rbx
00235334  E9 37 FD FF FF                  jmp 0x140235070
00235339  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0023533E  E9 C2 FD FF FF                  jmp 0x140235105
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00234FE8(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    unsigned int v_stack_p34;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p58;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p80;

    result = KiCheckVpBackingLongSpinWaitHypercall(a1, a2, a3, a4);
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r12)), a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00234FE8(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    uint32_t v_stack_p34;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint32_t v_stack_p58;
    uint64_t v_stack_p70;
    uint64_t v_stack_p80;

    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, Arg2, Arg3, a4);
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r12)), Arg2, Arg3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00234FE8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
