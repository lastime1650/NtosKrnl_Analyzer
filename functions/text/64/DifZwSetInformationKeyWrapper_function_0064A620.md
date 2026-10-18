# DifZwSetInformationKeyWrapper

- RVA: `0x0064A620`–`0x0064A7A5` (길이 `389` bytes)
- VA: `0x000000014064A620`
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
- `0x0064A660` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0064A686` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0064A6C2` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064A6E8` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064A701` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0064A713` → [ZwSetInformationKey](../6B/ZwSetInformationKey_function_006B0630.md) (function, `0x006B0630`)
- `0x0064A73F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064A765` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064A77E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0064A696` → RVA `0x00F048B8` (`.data`; read)
- `0x0064A6AF` → RVA `0x00F04980` (`.data`; read)
- `0x0064A6BB` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0064A620  48 8B C4                        mov rax, rsp
0064A623  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0064A627  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0064A62B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0064A62F  48 89 48 08                     mov qword ptr [rax + 8], rcx
0064A633  55                              push rbp
0064A634  41 54                           push r12
0064A636  41 55                           push r13
0064A638  41 56                           push r14
0064A63A  41 57                           push r15
0064A63C  48 8B EC                        mov rbp, rsp
0064A63F  48 83 EC 50                     sub rsp, 0x50
0064A643  0F 57 C0                        xorps xmm0, xmm0
0064A646  B9 10 00 00 00                  mov ecx, 0x10
0064A64B  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0064A64F  45 8B F9                        mov r15d, r9d
0064A652  4D 8B E0                        mov r12, r8
0064A655  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0064A659  44 8B EA                        mov r13d, edx
0064A65C  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
0064A660  E8 CF B3 E4 FF                  call 0x140495a34
0064A665  48 8B F0                        mov rsi, rax
0064A668  48 85 C0                        test rax, rax
0064A66B  0F 84 95 00 00 00               je 0x14064a706
0064A671  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0064A674  A8 18                           test al, 0x18
0064A676  74 0A                           je 0x14064a682
0064A678  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0064A67C  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0064A680  EB 0D                           jmp 0x14064a68f
0064A682  A8 04                           test al, 4
0064A684  74 09                           je 0x14064a68f
0064A686  E8 7D 95 E8 FF                  call 0x1404d3c08
0064A68B  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0064A68F  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0064A693  45 32 F6                        xor r14b, r14b
0064A696  44 38 35 1B A2 8B 00            cmp byte ptr [rip + 0x8ba21b], r14b
0064A69D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0064A6A1  44 89 6D E8                     mov dword ptr [rbp - 0x18], r13d
0064A6A5  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0064A6A9  44 89 7D D8                     mov dword ptr [rbp - 0x28], r15d
0064A6AD  75 0C                           jne 0x14064a6bb
0064A6AF  F7 05 C7 A2 8B 00 00 08 00 00   test dword ptr [rip + 0x8ba2c7], 0x800
0064A6B9  74 13                           je 0x14064a6ce
0064A6BB  48 8D 0D BE 97 8B 00            lea rcx, [rip + 0x8b97be]
0064A6C2  E8 59 BF BC FF                  call 0x140216620
0064A6C7  44 8A F0                        mov r14b, al
0064A6CA  84 C0                           test al, al
0064A6CC  74 38                           je 0x14064a706
0064A6CE  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0064A6D2  48 8B 1F                        mov rbx, qword ptr [rdi]
0064A6D5  EB 19                           jmp 0x14064a6f0
0064A6D7  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064A6DB  48 85 C0                        test rax, rax
0064A6DE  74 0D                           je 0x14064a6ed
0064A6E0  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0064A6E4  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0064A6E8  E8 E3 03 07 00                  call 0x1406baad0
0064A6ED  48 8B 1B                        mov rbx, qword ptr [rbx]
0064A6F0  48 3B DF                        cmp rbx, rdi
0064A6F3  75 E2                           jne 0x14064a6d7
0064A6F5  45 84 F6                        test r14b, r14b
0064A6F8  74 0C                           je 0x14064a706
0064A6FA  48 8D 0D 7F 97 8B 00            lea rcx, [rip + 0x8b977f]
0064A701  E8 7A F7 CF FF                  call 0x140349e80
0064A706  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0064A70A  45 8B CF                        mov r9d, r15d
0064A70D  4D 8B C4                        mov r8, r12
0064A710  41 8B D5                        mov edx, r13d
0064A713  E8 18 5F 06 00                  call 0x1406b0630
0064A718  89 45 F8                        mov dword ptr [rbp - 8], eax
0064A71B  48 85 F6                        test rsi, rsi
0064A71E  74 63                           je 0x14064a783
0064A720  40 32 FF                        xor dil, dil
0064A723  40 38 3D 8E A1 8B 00            cmp byte ptr [rip + 0x8ba18e], dil
0064A72A  75 0C                           jne 0x14064a738
0064A72C  F7 05 4A A2 8B 00 00 08 00 00   test dword ptr [rip + 0x8ba24a], 0x800
0064A736  74 13                           je 0x14064a74b
0064A738  48 8D 0D 41 97 8B 00            lea rcx, [rip + 0x8b9741]
0064A73F  E8 DC BE BC FF                  call 0x140216620
0064A744  40 8A F8                        mov dil, al
0064A747  84 C0                           test al, al
0064A749  74 38                           je 0x14064a783
0064A74B  48 83 C6 30                     add rsi, 0x30
0064A74F  48 8B 1E                        mov rbx, qword ptr [rsi]
0064A752  EB 19                           jmp 0x14064a76d
0064A754  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064A758  48 85 C0                        test rax, rax
0064A75B  74 0D                           je 0x14064a76a
0064A75D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0064A761  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0064A765  E8 66 03 07 00                  call 0x1406baad0
0064A76A  48 8B 1B                        mov rbx, qword ptr [rbx]
0064A76D  48 3B DE                        cmp rbx, rsi
0064A770  75 E2                           jne 0x14064a754
0064A772  40 84 FF                        test dil, dil
0064A775  74 0C                           je 0x14064a783
0064A777  48 8D 0D 02 97 8B 00            lea rcx, [rip + 0x8b9702]
0064A77E  E8 FD F6 CF FF                  call 0x140349e80
0064A783  8B 45 F8                        mov eax, dword ptr [rbp - 8]
0064A786  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0064A78B  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0064A78F  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0064A793  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0064A797  49 8B E3                        mov rsp, r11
0064A79A  41 5F                           pop r15
0064A79C  41 5E                           pop r14
0064A79E  41 5D                           pop r13
0064A7A0  41 5C                           pop r12
0064A7A2  5D                              pop rbp
0064A7A3  C3                              ret
0064A7A4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwSetInformationKeyWrapper(__int64 a1, int a2, __int64 a3, int a4)
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
    result = DifGetAPIThunkContextById(16, a2, a3, a4);
    if (result == 0) goto loc_0064A706;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0064A682;
    v_stack_m58 = v_stack_p0;
    goto loc_0064A68F;
loc_0064A682:
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
    if ((*(unsigned __int8 *)(v_rip + 9151003)) != 0) goto loc_0064A6BB;
    if (((*(unsigned int *)(v_rip + 9151175)) & (0x800ULL)) == 0) goto loc_0064A6CE;
loc_0064A6BB:
    result = ExAcquireRundownProtection(v_rip + 9148350, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0064A706;
loc_0064A6CE:
    goto loc_0064A6F0;
loc_0064A6D7:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0064A6F0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0064A6D7;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9148287;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwSetInformationKey(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_0064A783;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9150862)) != 0) goto loc_0064A738;
    if (((*(unsigned int *)(v_rip + 9151050)) & (0x800ULL)) == 0) goto loc_0064A74B;
loc_0064A738:
    result = ExAcquireRundownProtection(v_rip + 9148225, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_0064A783;
loc_0064A74B:
    v_rsi = (result) + (48);
    goto loc_0064A76D;
loc_0064A754:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_0064A76D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0064A754;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9148162;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwSetInformationKeyWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
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
    result = DifGetAPIThunkContextById(16, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0064A706;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0064A682;
    v_stack_m58 = v_stack_p0;
    goto loc_0064A68F;
loc_0064A682:
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
    if ((*(uint8_t *)(v_rip + 0x8BA21B)) != 0) goto loc_0064A6BB;
    if (((*(uint32_t *)(v_rip + 0x8BA2C7)) & (0x800ULL)) == 0) goto loc_0064A6CE;
loc_0064A6BB:
    result = ExAcquireRundownProtection(v_rip + 9148350, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0064A706;
loc_0064A6CE:
    goto loc_0064A6F0;
loc_0064A6D7:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0064A6F0:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0064A6D7;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9148287;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = ZwSetInformationKey(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_0064A783;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BA18E)) != 0) goto loc_0064A738;
    if (((*(uint32_t *)(v_rip + 0x8BA24A)) & (0x800ULL)) == 0) goto loc_0064A74B;
loc_0064A738:
    result = ExAcquireRundownProtection(v_rip + 9148225, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_0064A783;
loc_0064A74B:
    local_rsi = (result) + (48);
    goto loc_0064A76D;
loc_0064A754:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_0064A76D:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0064A754;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9148162;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0064A620&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0064A620[BB_0064A620]
  bb_0064A671[BB_0064A671]
  bb_0064A678[BB_0064A678]
  bb_0064A682[BB_0064A682]
  bb_0064A686[BB_0064A686]
  bb_0064A68F[BB_0064A68F]
  bb_0064A6AF[BB_0064A6AF]
  bb_0064A6BB[BB_0064A6BB]
  bb_0064A6CE[BB_0064A6CE]
  bb_0064A6D7[BB_0064A6D7]
  bb_0064A6E0[BB_0064A6E0]
  bb_0064A6ED[BB_0064A6ED]
  bb_0064A6F0[BB_0064A6F0]
  bb_0064A6F5[BB_0064A6F5]
  bb_0064A6FA[BB_0064A6FA]
  bb_0064A706[BB_0064A706]
  bb_0064A720[BB_0064A720]
  bb_0064A72C[BB_0064A72C]
  bb_0064A738[BB_0064A738]
  bb_0064A74B[BB_0064A74B]
  bb_0064A754[BB_0064A754]
  bb_0064A75D[BB_0064A75D]
  bb_0064A76A[BB_0064A76A]
  bb_0064A76D[BB_0064A76D]
  bb_0064A772[BB_0064A772]
  bb_0064A777[BB_0064A777]
  bb_0064A783[BB_0064A783]
  bb_0064A7A4[BB_0064A7A4]
  bb_0064A620 -->|branch| bb_0064A706
  bb_0064A620 -->|fallthrough| bb_0064A671
  bb_0064A671 -->|branch| bb_0064A682
  bb_0064A671 -->|fallthrough| bb_0064A678
  bb_0064A678 -->|branch| bb_0064A68F
  bb_0064A682 -->|branch| bb_0064A68F
  bb_0064A682 -->|fallthrough| bb_0064A686
  bb_0064A686 -->|flow| bb_0064A68F
  bb_0064A68F -->|branch| bb_0064A6BB
  bb_0064A68F -->|fallthrough| bb_0064A6AF
  bb_0064A6AF -->|branch| bb_0064A6CE
  bb_0064A6AF -->|fallthrough| bb_0064A6BB
  bb_0064A6BB -->|branch| bb_0064A706
  bb_0064A6BB -->|fallthrough| bb_0064A6CE
  bb_0064A6CE -->|branch| bb_0064A6F0
  bb_0064A6D7 -->|branch| bb_0064A6ED
  bb_0064A6D7 -->|fallthrough| bb_0064A6E0
  bb_0064A6E0 -->|flow| bb_0064A6ED
  bb_0064A6ED -->|flow| bb_0064A6F0
  bb_0064A6F0 -->|branch| bb_0064A6D7
  bb_0064A6F0 -->|fallthrough| bb_0064A6F5
  bb_0064A6F5 -->|branch| bb_0064A706
  bb_0064A6F5 -->|fallthrough| bb_0064A6FA
  bb_0064A6FA -->|flow| bb_0064A706
  bb_0064A706 -->|branch| bb_0064A783
  bb_0064A706 -->|fallthrough| bb_0064A720
  bb_0064A720 -->|branch| bb_0064A738
  bb_0064A720 -->|fallthrough| bb_0064A72C
  bb_0064A72C -->|branch| bb_0064A74B
  bb_0064A72C -->|fallthrough| bb_0064A738
  bb_0064A738 -->|branch| bb_0064A783
  bb_0064A738 -->|fallthrough| bb_0064A74B
  bb_0064A74B -->|branch| bb_0064A76D
  bb_0064A754 -->|branch| bb_0064A76A
  bb_0064A754 -->|fallthrough| bb_0064A75D
  bb_0064A75D -->|flow| bb_0064A76A
  bb_0064A76A -->|flow| bb_0064A76D
  bb_0064A76D -->|branch| bb_0064A754
  bb_0064A76D -->|fallthrough| bb_0064A772
  bb_0064A772 -->|branch| bb_0064A783
  bb_0064A772 -->|fallthrough| bb_0064A777
  bb_0064A777 -->|flow| bb_0064A783
```
