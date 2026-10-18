# DifRtlCheckRegistryKeyWrapper

- RVA: `0x0063B380`–`0x0063B4E7` (길이 `359` bytes)
- VA: `0x000000014063B380`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093E28`
- 디코드: `99`개 명령, `359/359` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0063B3B1` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063B3D9` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063B40C` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063B433` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063B44C` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063B457` → [RtlCheckRegistryKey](../../page/8C/RtlCheckRegistryKey_function_008C9010.md) (function, `0x008C9010`)
- `0x0063B484` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063B4AB` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063B4C4` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063B3EB` → RVA `0x00F048B8` (`.data`; read)
- `0x0063B3F9` → RVA `0x00F04980` (`.data`; read)
- `0x0063B405` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0063B457` → [RtlCheckRegistryKey](../../page/8C/RtlCheckRegistryKey_function_008C9010.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063B380  4C 8B DC                        mov r11, rsp
0063B383  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0063B387  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0063B38B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0063B38F  57                              push rdi
0063B390  41 56                           push r14
0063B392  41 57                           push r15
0063B394  48 83 EC 40                     sub rsp, 0x40
0063B398  33 C0                           xor eax, eax
0063B39A  0F 57 C0                        xorps xmm0, xmm0
0063B39D  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0063B3A2  44 8B F9                        mov r15d, ecx
0063B3A5  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
0063B3A9  B9 A8 00 00 00                  mov ecx, 0xa8
0063B3AE  4C 8B F2                        mov r14, rdx
0063B3B1  E8 7E A6 E5 FF                  call 0x140495a34
0063B3B6  48 8B F0                        mov rsi, rax
0063B3B9  48 85 C0                        test rax, rax
0063B3BC  0F 84 8F 00 00 00               je 0x14063b451
0063B3C2  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063B3C5  A8 18                           test al, 0x18
0063B3C7  74 0C                           je 0x14063b3d5
0063B3C9  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0063B3CE  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0063B3D3  EB 0E                           jmp 0x14063b3e3
0063B3D5  A8 04                           test al, 4
0063B3D7  74 0A                           je 0x14063b3e3
0063B3D9  E8 2A 88 E9 FF                  call 0x1404d3c08
0063B3DE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0063B3E3  40 32 ED                        xor bpl, bpl
0063B3E6  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
0063B3EB  40 38 2D C6 94 8C 00            cmp byte ptr [rip + 0x8c94c6], bpl
0063B3F2  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
0063B3F7  75 0C                           jne 0x14063b405
0063B3F9  F7 05 7D 95 8C 00 00 08 00 00   test dword ptr [rip + 0x8c957d], 0x800
0063B403  74 13                           je 0x14063b418
0063B405  48 8D 0D 74 8A 8C 00            lea rcx, [rip + 0x8c8a74]
0063B40C  E8 0F B2 BD FF                  call 0x140216620
0063B411  40 8A E8                        mov bpl, al
0063B414  84 C0                           test al, al
0063B416  74 39                           je 0x14063b451
0063B418  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0063B41C  48 8B 1F                        mov rbx, qword ptr [rdi]
0063B41F  EB 1A                           jmp 0x14063b43b
0063B421  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063B425  48 85 C0                        test rax, rax
0063B428  74 0E                           je 0x14063b438
0063B42A  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063B42E  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0063B433  E8 98 F6 07 00                  call 0x1406baad0
0063B438  48 8B 1B                        mov rbx, qword ptr [rbx]
0063B43B  48 3B DF                        cmp rbx, rdi
0063B43E  75 E1                           jne 0x14063b421
0063B440  40 84 ED                        test bpl, bpl
0063B443  74 0C                           je 0x14063b451
0063B445  48 8D 0D 34 8A 8C 00            lea rcx, [rip + 0x8c8a34]
0063B44C  E8 2F EA D0 FF                  call 0x140349e80
0063B451  49 8B D6                        mov rdx, r14
0063B454  41 8B CF                        mov ecx, r15d
0063B457  E8 B4 DB 28 00                  call 0x1408c9010
0063B45C  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
0063B460  48 85 F6                        test rsi, rsi
0063B463  74 64                           je 0x14063b4c9
0063B465  40 32 FF                        xor dil, dil
0063B468  40 38 3D 49 94 8C 00            cmp byte ptr [rip + 0x8c9449], dil
0063B46F  75 0C                           jne 0x14063b47d
0063B471  F7 05 05 95 8C 00 00 08 00 00   test dword ptr [rip + 0x8c9505], 0x800
0063B47B  74 13                           je 0x14063b490
0063B47D  48 8D 0D FC 89 8C 00            lea rcx, [rip + 0x8c89fc]
0063B484  E8 97 B1 BD FF                  call 0x140216620
0063B489  40 8A F8                        mov dil, al
0063B48C  84 C0                           test al, al
0063B48E  74 39                           je 0x14063b4c9
0063B490  48 83 C6 30                     add rsi, 0x30
0063B494  48 8B 1E                        mov rbx, qword ptr [rsi]
0063B497  EB 1A                           jmp 0x14063b4b3
0063B499  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063B49D  48 85 C0                        test rax, rax
0063B4A0  74 0E                           je 0x14063b4b0
0063B4A2  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063B4A6  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0063B4AB  E8 20 F6 07 00                  call 0x1406baad0
0063B4B0  48 8B 1B                        mov rbx, qword ptr [rbx]
0063B4B3  48 3B DE                        cmp rbx, rsi
0063B4B6  75 E1                           jne 0x14063b499
0063B4B8  40 84 FF                        test dil, dil
0063B4BB  74 0C                           je 0x14063b4c9
0063B4BD  48 8D 0D BC 89 8C 00            lea rcx, [rip + 0x8c89bc]
0063B4C4  E8 B7 E9 D0 FF                  call 0x140349e80
0063B4C9  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
0063B4CD  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0063B4D2  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0063B4D7  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0063B4DC  48 83 C4 40                     add rsp, 0x40
0063B4E0  41 5F                           pop r15
0063B4E2  41 5E                           pop r14
0063B4E4  5F                              pop rdi
0063B4E5  C3                              ret
0063B4E6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifRtlCheckRegistryKeyWrapper(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m24;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (64);
    result = 0;
    v_stack_m38 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = 0;
    result = DifGetAPIThunkContextById(168, a2, a3, a4);
    if (result == 0) goto loc_0063B451;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063B3D5;
    v_stack_m38 = v_stack_p0;
    goto loc_0063B3E3;
loc_0063B3D5:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = (unsigned int)((unsigned int)(a1));
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9213126)) != 0) goto loc_0063B405;
    if (((*(unsigned int *)(v_rip + 9213309)) & (0x800ULL)) == 0) goto loc_0063B418;
loc_0063B405:
    result = ExAcquireRundownProtection(v_rip + 9210484, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063B451;
loc_0063B418:
    goto loc_0063B43B;
loc_0063B421:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063B43B:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063B421;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9210420;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = RtlCheckRegistryKey((unsigned int)((unsigned int)((unsigned int)(a1))), a2, a3, a4);
    v_stack_m24 = (unsigned int)(result);
    if (result == 0) goto loc_0063B4C9;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9213001)) != 0) goto loc_0063B47D;
    if (((*(unsigned int *)(v_rip + 9213189)) & (0x800ULL)) == 0) goto loc_0063B490;
loc_0063B47D:
    result = ExAcquireRundownProtection(v_rip + 9210364, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063B4C9;
loc_0063B490:
    v_rsi = (result) + (48);
    goto loc_0063B4B3;
loc_0063B499:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063B4B3:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063B499;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9210300;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m24);
}
```

## 5. (Beta) C Style

```c
int64_t DifRtlCheckRegistryKeyWrapper(int32_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m24;
    uint32_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (64);
    result = 0;
    v_stack_m38 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = 0;
    result = DifGetAPIThunkContextById(168, Arg2, a3, a4);
    if (result == 0) goto loc_0063B451;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063B3D5;
    v_stack_m38 = v_stack_p0;
    goto loc_0063B3E3;
loc_0063B3D5:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = (uint32_t)((uint32_t)(Arg1));
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8C94C6)) != 0) goto loc_0063B405;
    if (((*(uint32_t *)(v_rip + 0x8C957D)) & (0x800ULL)) == 0) goto loc_0063B418;
loc_0063B405:
    result = ExAcquireRundownProtection(v_rip + 9210484, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063B451;
loc_0063B418:
    goto loc_0063B43B;
loc_0063B421:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_0063B43B:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063B421;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9210420;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = RtlCheckRegistryKey((uint32_t)((uint32_t)((uint32_t)(Arg1))), Arg2, a3, a4);
    v_stack_m24 = (uint32_t)(result);
    if (result == 0) goto loc_0063B4C9;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C9449)) != 0) goto loc_0063B47D;
    if (((*(uint32_t *)(v_rip + 0x8C9505)) & (0x800ULL)) == 0) goto loc_0063B490;
loc_0063B47D:
    result = ExAcquireRundownProtection(v_rip + 9210364, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063B4C9;
loc_0063B490:
    local_rsi = (result) + (48);
    goto loc_0063B4B3;
loc_0063B499:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_0063B4B3:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063B499;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9210300;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m24);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063B380&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063B380[BB_0063B380]
  bb_0063B3C2[BB_0063B3C2]
  bb_0063B3C9[BB_0063B3C9]
  bb_0063B3D5[BB_0063B3D5]
  bb_0063B3D9[BB_0063B3D9]
  bb_0063B3E3[BB_0063B3E3]
  bb_0063B3F9[BB_0063B3F9]
  bb_0063B405[BB_0063B405]
  bb_0063B418[BB_0063B418]
  bb_0063B421[BB_0063B421]
  bb_0063B42A[BB_0063B42A]
  bb_0063B438[BB_0063B438]
  bb_0063B43B[BB_0063B43B]
  bb_0063B440[BB_0063B440]
  bb_0063B445[BB_0063B445]
  bb_0063B451[BB_0063B451]
  bb_0063B465[BB_0063B465]
  bb_0063B471[BB_0063B471]
  bb_0063B47D[BB_0063B47D]
  bb_0063B490[BB_0063B490]
  bb_0063B499[BB_0063B499]
  bb_0063B4A2[BB_0063B4A2]
  bb_0063B4B0[BB_0063B4B0]
  bb_0063B4B3[BB_0063B4B3]
  bb_0063B4B8[BB_0063B4B8]
  bb_0063B4BD[BB_0063B4BD]
  bb_0063B4C9[BB_0063B4C9]
  bb_0063B4E6[BB_0063B4E6]
  bb_0063B380 -->|branch| bb_0063B451
  bb_0063B380 -->|fallthrough| bb_0063B3C2
  bb_0063B3C2 -->|branch| bb_0063B3D5
  bb_0063B3C2 -->|fallthrough| bb_0063B3C9
  bb_0063B3C9 -->|branch| bb_0063B3E3
  bb_0063B3D5 -->|branch| bb_0063B3E3
  bb_0063B3D5 -->|fallthrough| bb_0063B3D9
  bb_0063B3D9 -->|flow| bb_0063B3E3
  bb_0063B3E3 -->|branch| bb_0063B405
  bb_0063B3E3 -->|fallthrough| bb_0063B3F9
  bb_0063B3F9 -->|branch| bb_0063B418
  bb_0063B3F9 -->|fallthrough| bb_0063B405
  bb_0063B405 -->|branch| bb_0063B451
  bb_0063B405 -->|fallthrough| bb_0063B418
  bb_0063B418 -->|branch| bb_0063B43B
  bb_0063B421 -->|branch| bb_0063B438
  bb_0063B421 -->|fallthrough| bb_0063B42A
  bb_0063B42A -->|flow| bb_0063B438
  bb_0063B438 -->|flow| bb_0063B43B
  bb_0063B43B -->|branch| bb_0063B421
  bb_0063B43B -->|fallthrough| bb_0063B440
  bb_0063B440 -->|branch| bb_0063B451
  bb_0063B440 -->|fallthrough| bb_0063B445
  bb_0063B445 -->|flow| bb_0063B451
  bb_0063B451 -->|branch| bb_0063B4C9
  bb_0063B451 -->|fallthrough| bb_0063B465
  bb_0063B465 -->|branch| bb_0063B47D
  bb_0063B465 -->|fallthrough| bb_0063B471
  bb_0063B471 -->|branch| bb_0063B490
  bb_0063B471 -->|fallthrough| bb_0063B47D
  bb_0063B47D -->|branch| bb_0063B4C9
  bb_0063B47D -->|fallthrough| bb_0063B490
  bb_0063B490 -->|branch| bb_0063B4B3
  bb_0063B499 -->|branch| bb_0063B4B0
  bb_0063B499 -->|fallthrough| bb_0063B4A2
  bb_0063B4A2 -->|flow| bb_0063B4B0
  bb_0063B4B0 -->|flow| bb_0063B4B3
  bb_0063B4B3 -->|branch| bb_0063B499
  bb_0063B4B3 -->|fallthrough| bb_0063B4B8
  bb_0063B4B8 -->|branch| bb_0063B4C9
  bb_0063B4B8 -->|fallthrough| bb_0063B4BD
  bb_0063B4BD -->|flow| bb_0063B4C9
```
