# DifZwSetInformationThreadWrapper

- RVA: `0x0064AAD0`–`0x0064AC55` (길이 `389` bytes)
- VA: `0x000000014064AAD0`
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
- `0x0064AB10` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0064AB36` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0064AB72` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064AB98` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064ABB1` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0064ABC3` → [ZwSetInformationThread](../6A/ZwSetInformationThread_function_006AD270.md) (function, `0x006AD270`)
- `0x0064ABEF` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064AC15` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064AC2E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0064AB46` → RVA `0x00F048B8` (`.data`; read)
- `0x0064AB5F` → RVA `0x00F04980` (`.data`; read)
- `0x0064AB6B` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0064AAD0  48 8B C4                        mov rax, rsp
0064AAD3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0064AAD7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0064AADB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0064AADF  48 89 48 08                     mov qword ptr [rax + 8], rcx
0064AAE3  55                              push rbp
0064AAE4  41 54                           push r12
0064AAE6  41 55                           push r13
0064AAE8  41 56                           push r14
0064AAEA  41 57                           push r15
0064AAEC  48 8B EC                        mov rbp, rsp
0064AAEF  48 83 EC 50                     sub rsp, 0x50
0064AAF3  0F 57 C0                        xorps xmm0, xmm0
0064AAF6  B9 0D 00 00 00                  mov ecx, 0xd
0064AAFB  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0064AAFF  45 8B F9                        mov r15d, r9d
0064AB02  4D 8B E0                        mov r12, r8
0064AB05  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0064AB09  44 8B EA                        mov r13d, edx
0064AB0C  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
0064AB10  E8 1F AF E4 FF                  call 0x140495a34
0064AB15  48 8B F0                        mov rsi, rax
0064AB18  48 85 C0                        test rax, rax
0064AB1B  0F 84 95 00 00 00               je 0x14064abb6
0064AB21  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0064AB24  A8 18                           test al, 0x18
0064AB26  74 0A                           je 0x14064ab32
0064AB28  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0064AB2C  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0064AB30  EB 0D                           jmp 0x14064ab3f
0064AB32  A8 04                           test al, 4
0064AB34  74 09                           je 0x14064ab3f
0064AB36  E8 CD 90 E8 FF                  call 0x1404d3c08
0064AB3B  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0064AB3F  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0064AB43  45 32 F6                        xor r14b, r14b
0064AB46  44 38 35 6B 9D 8B 00            cmp byte ptr [rip + 0x8b9d6b], r14b
0064AB4D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0064AB51  44 89 6D E8                     mov dword ptr [rbp - 0x18], r13d
0064AB55  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0064AB59  44 89 7D D8                     mov dword ptr [rbp - 0x28], r15d
0064AB5D  75 0C                           jne 0x14064ab6b
0064AB5F  F7 05 17 9E 8B 00 00 08 00 00   test dword ptr [rip + 0x8b9e17], 0x800
0064AB69  74 13                           je 0x14064ab7e
0064AB6B  48 8D 0D 0E 93 8B 00            lea rcx, [rip + 0x8b930e]
0064AB72  E8 A9 BA BC FF                  call 0x140216620
0064AB77  44 8A F0                        mov r14b, al
0064AB7A  84 C0                           test al, al
0064AB7C  74 38                           je 0x14064abb6
0064AB7E  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0064AB82  48 8B 1F                        mov rbx, qword ptr [rdi]
0064AB85  EB 19                           jmp 0x14064aba0
0064AB87  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064AB8B  48 85 C0                        test rax, rax
0064AB8E  74 0D                           je 0x14064ab9d
0064AB90  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0064AB94  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0064AB98  E8 33 FF 06 00                  call 0x1406baad0
0064AB9D  48 8B 1B                        mov rbx, qword ptr [rbx]
0064ABA0  48 3B DF                        cmp rbx, rdi
0064ABA3  75 E2                           jne 0x14064ab87
0064ABA5  45 84 F6                        test r14b, r14b
0064ABA8  74 0C                           je 0x14064abb6
0064ABAA  48 8D 0D CF 92 8B 00            lea rcx, [rip + 0x8b92cf]
0064ABB1  E8 CA F2 CF FF                  call 0x140349e80
0064ABB6  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0064ABBA  45 8B CF                        mov r9d, r15d
0064ABBD  4D 8B C4                        mov r8, r12
0064ABC0  41 8B D5                        mov edx, r13d
0064ABC3  E8 A8 26 06 00                  call 0x1406ad270
0064ABC8  89 45 F8                        mov dword ptr [rbp - 8], eax
0064ABCB  48 85 F6                        test rsi, rsi
0064ABCE  74 63                           je 0x14064ac33
0064ABD0  40 32 FF                        xor dil, dil
0064ABD3  40 38 3D DE 9C 8B 00            cmp byte ptr [rip + 0x8b9cde], dil
0064ABDA  75 0C                           jne 0x14064abe8
0064ABDC  F7 05 9A 9D 8B 00 00 08 00 00   test dword ptr [rip + 0x8b9d9a], 0x800
0064ABE6  74 13                           je 0x14064abfb
0064ABE8  48 8D 0D 91 92 8B 00            lea rcx, [rip + 0x8b9291]
0064ABEF  E8 2C BA BC FF                  call 0x140216620
0064ABF4  40 8A F8                        mov dil, al
0064ABF7  84 C0                           test al, al
0064ABF9  74 38                           je 0x14064ac33
0064ABFB  48 83 C6 30                     add rsi, 0x30
0064ABFF  48 8B 1E                        mov rbx, qword ptr [rsi]
0064AC02  EB 19                           jmp 0x14064ac1d
0064AC04  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064AC08  48 85 C0                        test rax, rax
0064AC0B  74 0D                           je 0x14064ac1a
0064AC0D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0064AC11  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0064AC15  E8 B6 FE 06 00                  call 0x1406baad0
0064AC1A  48 8B 1B                        mov rbx, qword ptr [rbx]
0064AC1D  48 3B DE                        cmp rbx, rsi
0064AC20  75 E2                           jne 0x14064ac04
0064AC22  40 84 FF                        test dil, dil
0064AC25  74 0C                           je 0x14064ac33
0064AC27  48 8D 0D 52 92 8B 00            lea rcx, [rip + 0x8b9252]
0064AC2E  E8 4D F2 CF FF                  call 0x140349e80
0064AC33  8B 45 F8                        mov eax, dword ptr [rbp - 8]
0064AC36  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0064AC3B  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0064AC3F  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0064AC43  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0064AC47  49 8B E3                        mov rsp, r11
0064AC4A  41 5F                           pop r15
0064AC4C  41 5E                           pop r14
0064AC4E  41 5D                           pop r13
0064AC50  41 5C                           pop r12
0064AC52  5D                              pop rbp
0064AC53  C3                              ret
0064AC54  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwSetInformationThreadWrapper(__int64 a1, int a2, __int64 a3, int a4)
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
    result = DifGetAPIThunkContextById(13, a2, a3, a4);
    if (result == 0) goto loc_0064ABB6;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0064AB32;
    v_stack_m58 = v_stack_p0;
    goto loc_0064AB3F;
loc_0064AB32:
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
    if ((*(unsigned __int8 *)(v_rip + 9149803)) != 0) goto loc_0064AB6B;
    if (((*(unsigned int *)(v_rip + 9149975)) & (0x800ULL)) == 0) goto loc_0064AB7E;
loc_0064AB6B:
    result = ExAcquireRundownProtection(v_rip + 9147150, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0064ABB6;
loc_0064AB7E:
    goto loc_0064ABA0;
loc_0064AB87:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0064ABA0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0064AB87;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9147087;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwSetInformationThread(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_0064AC33;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9149662)) != 0) goto loc_0064ABE8;
    if (((*(unsigned int *)(v_rip + 9149850)) & (0x800ULL)) == 0) goto loc_0064ABFB;
loc_0064ABE8:
    result = ExAcquireRundownProtection(v_rip + 9147025, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_0064AC33;
loc_0064ABFB:
    v_rsi = (result) + (48);
    goto loc_0064AC1D;
loc_0064AC04:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_0064AC1D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0064AC04;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9146962;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwSetInformationThreadWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
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
    result = DifGetAPIThunkContextById(13, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0064ABB6;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0064AB32;
    v_stack_m58 = v_stack_p0;
    goto loc_0064AB3F;
loc_0064AB32:
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
    if ((*(uint8_t *)(v_rip + 0x8B9D6B)) != 0) goto loc_0064AB6B;
    if (((*(uint32_t *)(v_rip + 0x8B9E17)) & (0x800ULL)) == 0) goto loc_0064AB7E;
loc_0064AB6B:
    result = ExAcquireRundownProtection(v_rip + 9147150, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0064ABB6;
loc_0064AB7E:
    goto loc_0064ABA0;
loc_0064AB87:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0064ABA0:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0064AB87;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9147087;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = ZwSetInformationThread(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_0064AC33;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8B9CDE)) != 0) goto loc_0064ABE8;
    if (((*(uint32_t *)(v_rip + 0x8B9D9A)) & (0x800ULL)) == 0) goto loc_0064ABFB;
loc_0064ABE8:
    result = ExAcquireRundownProtection(v_rip + 9147025, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_0064AC33;
loc_0064ABFB:
    local_rsi = (result) + (48);
    goto loc_0064AC1D;
loc_0064AC04:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_0064AC1D:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0064AC04;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9146962;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0064AAD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0064AAD0[BB_0064AAD0]
  bb_0064AB21[BB_0064AB21]
  bb_0064AB28[BB_0064AB28]
  bb_0064AB32[BB_0064AB32]
  bb_0064AB36[BB_0064AB36]
  bb_0064AB3F[BB_0064AB3F]
  bb_0064AB5F[BB_0064AB5F]
  bb_0064AB6B[BB_0064AB6B]
  bb_0064AB7E[BB_0064AB7E]
  bb_0064AB87[BB_0064AB87]
  bb_0064AB90[BB_0064AB90]
  bb_0064AB9D[BB_0064AB9D]
  bb_0064ABA0[BB_0064ABA0]
  bb_0064ABA5[BB_0064ABA5]
  bb_0064ABAA[BB_0064ABAA]
  bb_0064ABB6[BB_0064ABB6]
  bb_0064ABD0[BB_0064ABD0]
  bb_0064ABDC[BB_0064ABDC]
  bb_0064ABE8[BB_0064ABE8]
  bb_0064ABFB[BB_0064ABFB]
  bb_0064AC04[BB_0064AC04]
  bb_0064AC0D[BB_0064AC0D]
  bb_0064AC1A[BB_0064AC1A]
  bb_0064AC1D[BB_0064AC1D]
  bb_0064AC22[BB_0064AC22]
  bb_0064AC27[BB_0064AC27]
  bb_0064AC33[BB_0064AC33]
  bb_0064AC54[BB_0064AC54]
  bb_0064AAD0 -->|branch| bb_0064ABB6
  bb_0064AAD0 -->|fallthrough| bb_0064AB21
  bb_0064AB21 -->|branch| bb_0064AB32
  bb_0064AB21 -->|fallthrough| bb_0064AB28
  bb_0064AB28 -->|branch| bb_0064AB3F
  bb_0064AB32 -->|branch| bb_0064AB3F
  bb_0064AB32 -->|fallthrough| bb_0064AB36
  bb_0064AB36 -->|flow| bb_0064AB3F
  bb_0064AB3F -->|branch| bb_0064AB6B
  bb_0064AB3F -->|fallthrough| bb_0064AB5F
  bb_0064AB5F -->|branch| bb_0064AB7E
  bb_0064AB5F -->|fallthrough| bb_0064AB6B
  bb_0064AB6B -->|branch| bb_0064ABB6
  bb_0064AB6B -->|fallthrough| bb_0064AB7E
  bb_0064AB7E -->|branch| bb_0064ABA0
  bb_0064AB87 -->|branch| bb_0064AB9D
  bb_0064AB87 -->|fallthrough| bb_0064AB90
  bb_0064AB90 -->|flow| bb_0064AB9D
  bb_0064AB9D -->|flow| bb_0064ABA0
  bb_0064ABA0 -->|branch| bb_0064AB87
  bb_0064ABA0 -->|fallthrough| bb_0064ABA5
  bb_0064ABA5 -->|branch| bb_0064ABB6
  bb_0064ABA5 -->|fallthrough| bb_0064ABAA
  bb_0064ABAA -->|flow| bb_0064ABB6
  bb_0064ABB6 -->|branch| bb_0064AC33
  bb_0064ABB6 -->|fallthrough| bb_0064ABD0
  bb_0064ABD0 -->|branch| bb_0064ABE8
  bb_0064ABD0 -->|fallthrough| bb_0064ABDC
  bb_0064ABDC -->|branch| bb_0064ABFB
  bb_0064ABDC -->|fallthrough| bb_0064ABE8
  bb_0064ABE8 -->|branch| bb_0064AC33
  bb_0064ABE8 -->|fallthrough| bb_0064ABFB
  bb_0064ABFB -->|branch| bb_0064AC1D
  bb_0064AC04 -->|branch| bb_0064AC1A
  bb_0064AC04 -->|fallthrough| bb_0064AC0D
  bb_0064AC0D -->|flow| bb_0064AC1A
  bb_0064AC1A -->|flow| bb_0064AC1D
  bb_0064AC1D -->|branch| bb_0064AC04
  bb_0064AC1D -->|fallthrough| bb_0064AC22
  bb_0064AC22 -->|branch| bb_0064AC33
  bb_0064AC22 -->|fallthrough| bb_0064AC27
  bb_0064AC27 -->|flow| bb_0064AC33
```
