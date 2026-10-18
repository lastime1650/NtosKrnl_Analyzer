# DifZwSetInformationEnlistmentWrapper

- RVA: `0x0064A160`–`0x0064A2E5` (길이 `389` bytes)
- VA: `0x000000014064A160`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2B7C`
- 디코드: `112`개 명령, `389/389` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0064A1A0` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0064A1C6` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0064A202` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064A228` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064A241` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0064A253` → [ZwSetInformationEnlistment](../6B/ZwSetInformationEnlistment_function_006B05D0.md) (function, `0x006B05D0`)
- `0x0064A27F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064A2A5` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064A2BE` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0064A1D6` → RVA `0x00F048B8` (`.data`; read)
- `0x0064A1EF` → RVA `0x00F04980` (`.data`; read)
- `0x0064A1FB` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0064A160  48 8B C4                        mov rax, rsp
0064A163  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0064A167  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0064A16B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0064A16F  48 89 48 08                     mov qword ptr [rax + 8], rcx
0064A173  55                              push rbp
0064A174  41 54                           push r12
0064A176  41 55                           push r13
0064A178  41 56                           push r14
0064A17A  41 57                           push r15
0064A17C  48 8B EC                        mov rbp, rsp
0064A17F  48 83 EC 50                     sub rsp, 0x50
0064A183  0F 57 C0                        xorps xmm0, xmm0
0064A186  B9 13 00 00 00                  mov ecx, 0x13
0064A18B  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0064A18F  45 8B F9                        mov r15d, r9d
0064A192  4D 8B E0                        mov r12, r8
0064A195  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0064A199  44 8B EA                        mov r13d, edx
0064A19C  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
0064A1A0  E8 8F B8 E4 FF                  call 0x140495a34
0064A1A5  48 8B F0                        mov rsi, rax
0064A1A8  48 85 C0                        test rax, rax
0064A1AB  0F 84 95 00 00 00               je 0x14064a246
0064A1B1  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0064A1B4  A8 18                           test al, 0x18
0064A1B6  74 0A                           je 0x14064a1c2
0064A1B8  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0064A1BC  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0064A1C0  EB 0D                           jmp 0x14064a1cf
0064A1C2  A8 04                           test al, 4
0064A1C4  74 09                           je 0x14064a1cf
0064A1C6  E8 3D 9A E8 FF                  call 0x1404d3c08
0064A1CB  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0064A1CF  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0064A1D3  45 32 F6                        xor r14b, r14b
0064A1D6  44 38 35 DB A6 8B 00            cmp byte ptr [rip + 0x8ba6db], r14b
0064A1DD  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0064A1E1  44 89 6D E8                     mov dword ptr [rbp - 0x18], r13d
0064A1E5  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0064A1E9  44 89 7D D8                     mov dword ptr [rbp - 0x28], r15d
0064A1ED  75 0C                           jne 0x14064a1fb
0064A1EF  F7 05 87 A7 8B 00 00 08 00 00   test dword ptr [rip + 0x8ba787], 0x800
0064A1F9  74 13                           je 0x14064a20e
0064A1FB  48 8D 0D 7E 9C 8B 00            lea rcx, [rip + 0x8b9c7e]
0064A202  E8 19 C4 BC FF                  call 0x140216620
0064A207  44 8A F0                        mov r14b, al
0064A20A  84 C0                           test al, al
0064A20C  74 38                           je 0x14064a246
0064A20E  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0064A212  48 8B 1F                        mov rbx, qword ptr [rdi]
0064A215  EB 19                           jmp 0x14064a230
0064A217  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064A21B  48 85 C0                        test rax, rax
0064A21E  74 0D                           je 0x14064a22d
0064A220  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0064A224  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0064A228  E8 A3 08 07 00                  call 0x1406baad0
0064A22D  48 8B 1B                        mov rbx, qword ptr [rbx]
0064A230  48 3B DF                        cmp rbx, rdi
0064A233  75 E2                           jne 0x14064a217
0064A235  45 84 F6                        test r14b, r14b
0064A238  74 0C                           je 0x14064a246
0064A23A  48 8D 0D 3F 9C 8B 00            lea rcx, [rip + 0x8b9c3f]
0064A241  E8 3A FC CF FF                  call 0x140349e80
0064A246  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0064A24A  45 8B CF                        mov r9d, r15d
0064A24D  4D 8B C4                        mov r8, r12
0064A250  41 8B D5                        mov edx, r13d
0064A253  E8 78 63 06 00                  call 0x1406b05d0
0064A258  89 45 F8                        mov dword ptr [rbp - 8], eax
0064A25B  48 85 F6                        test rsi, rsi
0064A25E  74 63                           je 0x14064a2c3
0064A260  40 32 FF                        xor dil, dil
0064A263  40 38 3D 4E A6 8B 00            cmp byte ptr [rip + 0x8ba64e], dil
0064A26A  75 0C                           jne 0x14064a278
0064A26C  F7 05 0A A7 8B 00 00 08 00 00   test dword ptr [rip + 0x8ba70a], 0x800
0064A276  74 13                           je 0x14064a28b
0064A278  48 8D 0D 01 9C 8B 00            lea rcx, [rip + 0x8b9c01]
0064A27F  E8 9C C3 BC FF                  call 0x140216620
0064A284  40 8A F8                        mov dil, al
0064A287  84 C0                           test al, al
0064A289  74 38                           je 0x14064a2c3
0064A28B  48 83 C6 30                     add rsi, 0x30
0064A28F  48 8B 1E                        mov rbx, qword ptr [rsi]
0064A292  EB 19                           jmp 0x14064a2ad
0064A294  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064A298  48 85 C0                        test rax, rax
0064A29B  74 0D                           je 0x14064a2aa
0064A29D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0064A2A1  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0064A2A5  E8 26 08 07 00                  call 0x1406baad0
0064A2AA  48 8B 1B                        mov rbx, qword ptr [rbx]
0064A2AD  48 3B DE                        cmp rbx, rsi
0064A2B0  75 E2                           jne 0x14064a294
0064A2B2  40 84 FF                        test dil, dil
0064A2B5  74 0C                           je 0x14064a2c3
0064A2B7  48 8D 0D C2 9B 8B 00            lea rcx, [rip + 0x8b9bc2]
0064A2BE  E8 BD FB CF FF                  call 0x140349e80
0064A2C3  8B 45 F8                        mov eax, dword ptr [rbp - 8]
0064A2C6  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0064A2CB  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0064A2CF  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0064A2D3  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0064A2D7  49 8B E3                        mov rsp, r11
0064A2DA  41 5F                           pop r15
0064A2DC  41 5E                           pop r14
0064A2DE  41 5D                           pop r13
0064A2E0  41 5C                           pop r12
0064A2E2  5D                              pop rbp
0064A2E3  C3                              ret
0064A2E4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwSetInformationEnlistmentWrapper(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (80);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(19, a2, a3, a4);
    if (result == 0) goto loc_0064A246;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0064A1C2;
    v_stack_m58 = v_stack_p0;
    goto loc_0064A1CF;
loc_0064A1C2:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m40 = (unsigned int)((unsigned int)(a2));
    v_stack_m48 = a3;
    v_stack_m50 = (unsigned int)((unsigned int)(a4));
    if ((*(unsigned __int8 *)(v_rip + 9152219)) != 0) goto loc_0064A1FB;
    if (((*(unsigned int *)(v_rip + 9152391)) & (0x800ULL)) == 0) goto loc_0064A20E;
loc_0064A1FB:
    result = ExAcquireRundownProtection(v_rip + 9149566, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0064A246;
loc_0064A20E:
    goto loc_0064A230;
loc_0064A217:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0064A230:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0064A217;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9149503;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwSetInformationEnlistment(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_0064A2C3;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9152078)) != 0) goto loc_0064A278;
    if (((*(unsigned int *)(v_rip + 9152266)) & (0x800ULL)) == 0) goto loc_0064A28B;
loc_0064A278:
    result = ExAcquireRundownProtection(v_rip + 9149441, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_0064A2C3;
loc_0064A28B:
    v_rsi = (result) + (48);
    goto loc_0064A2AD;
loc_0064A294:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_0064A2AD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0064A294;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9149378;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwSetInformationEnlistmentWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (80);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(19, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0064A246;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0064A1C2;
    v_stack_m58 = v_stack_p0;
    goto loc_0064A1CF;
loc_0064A1C2:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m40 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m48 = Arg3;
    v_stack_m50 = (uint32_t)((uint32_t)(Arg4));
    if ((*(uint8_t *)(v_rip + 0x8BA6DB)) != 0) goto loc_0064A1FB;
    if (((*(uint32_t *)(v_rip + 0x8BA787)) & (0x800ULL)) == 0) goto loc_0064A20E;
loc_0064A1FB:
    result = ExAcquireRundownProtection(v_rip + 9149566, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0064A246;
loc_0064A20E:
    goto loc_0064A230;
loc_0064A217:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0064A230:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0064A217;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9149503;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = ZwSetInformationEnlistment(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_0064A2C3;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BA64E)) != 0) goto loc_0064A278;
    if (((*(uint32_t *)(v_rip + 0x8BA70A)) & (0x800ULL)) == 0) goto loc_0064A28B;
loc_0064A278:
    result = ExAcquireRundownProtection(v_rip + 9149441, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_0064A2C3;
loc_0064A28B:
    local_rsi = (result) + (48);
    goto loc_0064A2AD;
loc_0064A294:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_0064A2AD:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0064A294;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9149378;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0064A160&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0064A160[BB_0064A160]
  bb_0064A1B1[BB_0064A1B1]
  bb_0064A1B8[BB_0064A1B8]
  bb_0064A1C2[BB_0064A1C2]
  bb_0064A1C6[BB_0064A1C6]
  bb_0064A1CF[BB_0064A1CF]
  bb_0064A1EF[BB_0064A1EF]
  bb_0064A1FB[BB_0064A1FB]
  bb_0064A20E[BB_0064A20E]
  bb_0064A217[BB_0064A217]
  bb_0064A220[BB_0064A220]
  bb_0064A22D[BB_0064A22D]
  bb_0064A230[BB_0064A230]
  bb_0064A235[BB_0064A235]
  bb_0064A23A[BB_0064A23A]
  bb_0064A246[BB_0064A246]
  bb_0064A260[BB_0064A260]
  bb_0064A26C[BB_0064A26C]
  bb_0064A278[BB_0064A278]
  bb_0064A28B[BB_0064A28B]
  bb_0064A294[BB_0064A294]
  bb_0064A29D[BB_0064A29D]
  bb_0064A2AA[BB_0064A2AA]
  bb_0064A2AD[BB_0064A2AD]
  bb_0064A2B2[BB_0064A2B2]
  bb_0064A2B7[BB_0064A2B7]
  bb_0064A2C3[BB_0064A2C3]
  bb_0064A2E4[BB_0064A2E4]
  bb_0064A160 -->|branch| bb_0064A246
  bb_0064A160 -->|fallthrough| bb_0064A1B1
  bb_0064A1B1 -->|branch| bb_0064A1C2
  bb_0064A1B1 -->|fallthrough| bb_0064A1B8
  bb_0064A1B8 -->|branch| bb_0064A1CF
  bb_0064A1C2 -->|branch| bb_0064A1CF
  bb_0064A1C2 -->|fallthrough| bb_0064A1C6
  bb_0064A1C6 -->|flow| bb_0064A1CF
  bb_0064A1CF -->|branch| bb_0064A1FB
  bb_0064A1CF -->|fallthrough| bb_0064A1EF
  bb_0064A1EF -->|branch| bb_0064A20E
  bb_0064A1EF -->|fallthrough| bb_0064A1FB
  bb_0064A1FB -->|branch| bb_0064A246
  bb_0064A1FB -->|fallthrough| bb_0064A20E
  bb_0064A20E -->|branch| bb_0064A230
  bb_0064A217 -->|branch| bb_0064A22D
  bb_0064A217 -->|fallthrough| bb_0064A220
  bb_0064A220 -->|flow| bb_0064A22D
  bb_0064A22D -->|flow| bb_0064A230
  bb_0064A230 -->|branch| bb_0064A217
  bb_0064A230 -->|fallthrough| bb_0064A235
  bb_0064A235 -->|branch| bb_0064A246
  bb_0064A235 -->|fallthrough| bb_0064A23A
  bb_0064A23A -->|flow| bb_0064A246
  bb_0064A246 -->|branch| bb_0064A2C3
  bb_0064A246 -->|fallthrough| bb_0064A260
  bb_0064A260 -->|branch| bb_0064A278
  bb_0064A260 -->|fallthrough| bb_0064A26C
  bb_0064A26C -->|branch| bb_0064A28B
  bb_0064A26C -->|fallthrough| bb_0064A278
  bb_0064A278 -->|branch| bb_0064A2C3
  bb_0064A278 -->|fallthrough| bb_0064A28B
  bb_0064A28B -->|branch| bb_0064A2AD
  bb_0064A294 -->|branch| bb_0064A2AA
  bb_0064A294 -->|fallthrough| bb_0064A29D
  bb_0064A29D -->|flow| bb_0064A2AA
  bb_0064A2AA -->|flow| bb_0064A2AD
  bb_0064A2AD -->|branch| bb_0064A294
  bb_0064A2AD -->|fallthrough| bb_0064A2B2
  bb_0064A2B2 -->|branch| bb_0064A2C3
  bb_0064A2B2 -->|fallthrough| bb_0064A2B7
  bb_0064A2B7 -->|flow| bb_0064A2C3
```
