# DifZwAddBootEntryWrapper

- RVA: `0x0063D410`–`0x0063D574` (길이 `356` bytes)
- VA: `0x000000014063D410`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093E28`
- 디코드: `98`개 명령, `356/356` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0063D43E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063D466` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063D499` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063D4C0` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063D4D9` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063D4E4` → [ZwAddBootEntry](../6A/ZwAddBootEntry_function_006ADE10.md) (function, `0x006ADE10`)
- `0x0063D511` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063D538` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063D551` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063D478` → RVA `0x00F048B8` (`.data`; read)
- `0x0063D486` → RVA `0x00F04980` (`.data`; read)
- `0x0063D492` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063D410  48 8B C4                        mov rax, rsp
0063D413  48 89 58 08                     mov qword ptr [rax + 8], rbx
0063D417  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0063D41B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0063D41F  57                              push rdi
0063D420  41 56                           push r14
0063D422  41 57                           push r15
0063D424  48 83 EC 40                     sub rsp, 0x40
0063D428  0F 57 C0                        xorps xmm0, xmm0
0063D42B  4C 8B F9                        mov r15, rcx
0063D42E  B9 93 00 00 00                  mov ecx, 0x93
0063D433  4C 8B F2                        mov r14, rdx
0063D436  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0063D43A  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
0063D43E  E8 F1 85 E5 FF                  call 0x140495a34
0063D443  48 8B F0                        mov rsi, rax
0063D446  48 85 C0                        test rax, rax
0063D449  0F 84 8F 00 00 00               je 0x14063d4de
0063D44F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063D452  A8 18                           test al, 0x18
0063D454  74 0C                           je 0x14063d462
0063D456  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0063D45B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0063D460  EB 0E                           jmp 0x14063d470
0063D462  A8 04                           test al, 4
0063D464  74 0A                           je 0x14063d470
0063D466  E8 9D 67 E9 FF                  call 0x1404d3c08
0063D46B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0063D470  40 32 ED                        xor bpl, bpl
0063D473  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0063D478  40 38 2D 39 74 8C 00            cmp byte ptr [rip + 0x8c7439], bpl
0063D47F  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
0063D484  75 0C                           jne 0x14063d492
0063D486  F7 05 F0 74 8C 00 00 08 00 00   test dword ptr [rip + 0x8c74f0], 0x800
0063D490  74 13                           je 0x14063d4a5
0063D492  48 8D 0D E7 69 8C 00            lea rcx, [rip + 0x8c69e7]
0063D499  E8 82 91 BD FF                  call 0x140216620
0063D49E  40 8A E8                        mov bpl, al
0063D4A1  84 C0                           test al, al
0063D4A3  74 39                           je 0x14063d4de
0063D4A5  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0063D4A9  48 8B 1F                        mov rbx, qword ptr [rdi]
0063D4AC  EB 1A                           jmp 0x14063d4c8
0063D4AE  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063D4B2  48 85 C0                        test rax, rax
0063D4B5  74 0E                           je 0x14063d4c5
0063D4B7  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063D4BB  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0063D4C0  E8 0B D6 07 00                  call 0x1406baad0
0063D4C5  48 8B 1B                        mov rbx, qword ptr [rbx]
0063D4C8  48 3B DF                        cmp rbx, rdi
0063D4CB  75 E1                           jne 0x14063d4ae
0063D4CD  40 84 ED                        test bpl, bpl
0063D4D0  74 0C                           je 0x14063d4de
0063D4D2  48 8D 0D A7 69 8C 00            lea rcx, [rip + 0x8c69a7]
0063D4D9  E8 A2 C9 D0 FF                  call 0x140349e80
0063D4DE  49 8B D6                        mov rdx, r14
0063D4E1  49 8B CF                        mov rcx, r15
0063D4E4  E8 27 09 07 00                  call 0x1406ade10
0063D4E9  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0063D4ED  48 85 F6                        test rsi, rsi
0063D4F0  74 64                           je 0x14063d556
0063D4F2  40 32 FF                        xor dil, dil
0063D4F5  40 38 3D BC 73 8C 00            cmp byte ptr [rip + 0x8c73bc], dil
0063D4FC  75 0C                           jne 0x14063d50a
0063D4FE  F7 05 78 74 8C 00 00 08 00 00   test dword ptr [rip + 0x8c7478], 0x800
0063D508  74 13                           je 0x14063d51d
0063D50A  48 8D 0D 6F 69 8C 00            lea rcx, [rip + 0x8c696f]
0063D511  E8 0A 91 BD FF                  call 0x140216620
0063D516  40 8A F8                        mov dil, al
0063D519  84 C0                           test al, al
0063D51B  74 39                           je 0x14063d556
0063D51D  48 83 C6 30                     add rsi, 0x30
0063D521  48 8B 1E                        mov rbx, qword ptr [rsi]
0063D524  EB 1A                           jmp 0x14063d540
0063D526  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063D52A  48 85 C0                        test rax, rax
0063D52D  74 0E                           je 0x14063d53d
0063D52F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063D533  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0063D538  E8 93 D5 07 00                  call 0x1406baad0
0063D53D  48 8B 1B                        mov rbx, qword ptr [rbx]
0063D540  48 3B DE                        cmp rbx, rsi
0063D543  75 E1                           jne 0x14063d526
0063D545  40 84 FF                        test dil, dil
0063D548  74 0C                           je 0x14063d556
0063D54A  48 8D 0D 2F 69 8C 00            lea rcx, [rip + 0x8c692f]
0063D551  E8 2A C9 D0 FF                  call 0x140349e80
0063D556  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
0063D55A  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0063D55F  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0063D564  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0063D569  48 83 C4 40                     add rsp, 0x40
0063D56D  41 5F                           pop r15
0063D56F  41 5E                           pop r14
0063D571  5F                              pop rdi
0063D572  C3                              ret
0063D573  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwAddBootEntryWrapper(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
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
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    result = DifGetAPIThunkContextById(147, a2, a3, a4);
    if (result == 0) goto loc_0063D4DE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063D462;
    v_stack_m38 = v_stack_p0;
    goto loc_0063D470;
loc_0063D462:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9204793)) != 0) goto loc_0063D492;
    if (((*(unsigned int *)(v_rip + 9204976)) & (0x800ULL)) == 0) goto loc_0063D4A5;
loc_0063D492:
    result = ExAcquireRundownProtection(v_rip + 9202151, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063D4DE;
loc_0063D4A5:
    goto loc_0063D4C8;
loc_0063D4AE:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063D4C8:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063D4AE;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9202087;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwAddBootEntry(a1, a2, a3, a4);
    v_stack_m20 = (unsigned int)(result);
    if (result == 0) goto loc_0063D556;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9204668)) != 0) goto loc_0063D50A;
    if (((*(unsigned int *)(v_rip + 9204856)) & (0x800ULL)) == 0) goto loc_0063D51D;
loc_0063D50A:
    result = ExAcquireRundownProtection(v_rip + 9202031, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063D556;
loc_0063D51D:
    v_rsi = (result) + (48);
    goto loc_0063D540;
loc_0063D526:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063D540:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063D526;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9201967;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m20);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwAddBootEntryWrapper(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
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
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    result = DifGetAPIThunkContextById(147, Arg2, a3, a4);
    if (result == 0) goto loc_0063D4DE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063D462;
    v_stack_m38 = v_stack_p0;
    goto loc_0063D470;
loc_0063D462:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8C7439)) != 0) goto loc_0063D492;
    if (((*(uint32_t *)(v_rip + 0x8C74F0)) & (0x800ULL)) == 0) goto loc_0063D4A5;
loc_0063D492:
    result = ExAcquireRundownProtection(v_rip + 9202151, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063D4DE;
loc_0063D4A5:
    goto loc_0063D4C8;
loc_0063D4AE:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_0063D4C8:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063D4AE;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9202087;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = ZwAddBootEntry(Arg1, Arg2, a3, a4);
    v_stack_m20 = (uint32_t)(result);
    if (result == 0) goto loc_0063D556;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C73BC)) != 0) goto loc_0063D50A;
    if (((*(uint32_t *)(v_rip + 0x8C7478)) & (0x800ULL)) == 0) goto loc_0063D51D;
loc_0063D50A:
    result = ExAcquireRundownProtection(v_rip + 9202031, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063D556;
loc_0063D51D:
    local_rsi = (result) + (48);
    goto loc_0063D540;
loc_0063D526:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_0063D540:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063D526;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9201967;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m20);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063D410&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063D410[BB_0063D410]
  bb_0063D44F[BB_0063D44F]
  bb_0063D456[BB_0063D456]
  bb_0063D462[BB_0063D462]
  bb_0063D466[BB_0063D466]
  bb_0063D470[BB_0063D470]
  bb_0063D486[BB_0063D486]
  bb_0063D492[BB_0063D492]
  bb_0063D4A5[BB_0063D4A5]
  bb_0063D4AE[BB_0063D4AE]
  bb_0063D4B7[BB_0063D4B7]
  bb_0063D4C5[BB_0063D4C5]
  bb_0063D4C8[BB_0063D4C8]
  bb_0063D4CD[BB_0063D4CD]
  bb_0063D4D2[BB_0063D4D2]
  bb_0063D4DE[BB_0063D4DE]
  bb_0063D4F2[BB_0063D4F2]
  bb_0063D4FE[BB_0063D4FE]
  bb_0063D50A[BB_0063D50A]
  bb_0063D51D[BB_0063D51D]
  bb_0063D526[BB_0063D526]
  bb_0063D52F[BB_0063D52F]
  bb_0063D53D[BB_0063D53D]
  bb_0063D540[BB_0063D540]
  bb_0063D545[BB_0063D545]
  bb_0063D54A[BB_0063D54A]
  bb_0063D556[BB_0063D556]
  bb_0063D573[BB_0063D573]
  bb_0063D410 -->|branch| bb_0063D4DE
  bb_0063D410 -->|fallthrough| bb_0063D44F
  bb_0063D44F -->|branch| bb_0063D462
  bb_0063D44F -->|fallthrough| bb_0063D456
  bb_0063D456 -->|branch| bb_0063D470
  bb_0063D462 -->|branch| bb_0063D470
  bb_0063D462 -->|fallthrough| bb_0063D466
  bb_0063D466 -->|flow| bb_0063D470
  bb_0063D470 -->|branch| bb_0063D492
  bb_0063D470 -->|fallthrough| bb_0063D486
  bb_0063D486 -->|branch| bb_0063D4A5
  bb_0063D486 -->|fallthrough| bb_0063D492
  bb_0063D492 -->|branch| bb_0063D4DE
  bb_0063D492 -->|fallthrough| bb_0063D4A5
  bb_0063D4A5 -->|branch| bb_0063D4C8
  bb_0063D4AE -->|branch| bb_0063D4C5
  bb_0063D4AE -->|fallthrough| bb_0063D4B7
  bb_0063D4B7 -->|flow| bb_0063D4C5
  bb_0063D4C5 -->|flow| bb_0063D4C8
  bb_0063D4C8 -->|branch| bb_0063D4AE
  bb_0063D4C8 -->|fallthrough| bb_0063D4CD
  bb_0063D4CD -->|branch| bb_0063D4DE
  bb_0063D4CD -->|fallthrough| bb_0063D4D2
  bb_0063D4D2 -->|flow| bb_0063D4DE
  bb_0063D4DE -->|branch| bb_0063D556
  bb_0063D4DE -->|fallthrough| bb_0063D4F2
  bb_0063D4F2 -->|branch| bb_0063D50A
  bb_0063D4F2 -->|fallthrough| bb_0063D4FE
  bb_0063D4FE -->|branch| bb_0063D51D
  bb_0063D4FE -->|fallthrough| bb_0063D50A
  bb_0063D50A -->|branch| bb_0063D556
  bb_0063D50A -->|fallthrough| bb_0063D51D
  bb_0063D51D -->|branch| bb_0063D540
  bb_0063D526 -->|branch| bb_0063D53D
  bb_0063D526 -->|fallthrough| bb_0063D52F
  bb_0063D52F -->|flow| bb_0063D53D
  bb_0063D53D -->|flow| bb_0063D540
  bb_0063D540 -->|branch| bb_0063D526
  bb_0063D540 -->|fallthrough| bb_0063D545
  bb_0063D545 -->|branch| bb_0063D556
  bb_0063D545 -->|fallthrough| bb_0063D54A
  bb_0063D54A -->|flow| bb_0063D556
```
