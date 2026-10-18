# DifExDeleteLookasideListExWrapper

- RVA: `0x0061F5F0`–`0x0061F740` (길이 `336` bytes)
- VA: `0x000000014061F5F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D7BC`
- 디코드: `90`개 명령, `336/336` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0061F618` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0061F640` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0061F66E` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061F695` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061F6AE` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0061F6B6` → [ExDeleteLookasideListEx](../48/ExDeleteLookasideListEx_function_00481DD0.md) (function, `0x00481DD0`)
- `0x0061F6DF` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061F706` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061F71F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0061F652` → RVA `0x00F048B8` (`.data`; read)
- `0x0061F65B` → RVA `0x00F04980` (`.data`; read)
- `0x0061F667` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0061F5F0  48 8B C4                        mov rax, rsp
0061F5F3  48 89 58 08                     mov qword ptr [rax + 8], rbx
0061F5F7  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0061F5FB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0061F5FF  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0061F603  41 56                           push r14
0061F605  48 83 EC 30                     sub rsp, 0x30
0061F609  48 8B E9                        mov rbp, rcx
0061F60C  0F 57 C0                        xorps xmm0, xmm0
0061F60F  B9 9A 01 00 00                  mov ecx, 0x19a
0061F614  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
0061F618  E8 17 64 E7 FF                  call 0x140495a34
0061F61D  48 8B F8                        mov rdi, rax
0061F620  48 85 C0                        test rax, rax
0061F623  0F 84 8A 00 00 00               je 0x14061f6b3
0061F629  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0061F62C  A8 18                           test al, 0x18
0061F62E  74 0C                           je 0x14061f63c
0061F630  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0061F635  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0061F63A  EB 0E                           jmp 0x14061f64a
0061F63C  A8 04                           test al, 4
0061F63E  74 0A                           je 0x14061f64a
0061F640  E8 C3 45 EB FF                  call 0x1404d3c08
0061F645  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0061F64A  40 32 F6                        xor sil, sil
0061F64D  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
0061F652  40 38 35 5F 52 8E 00            cmp byte ptr [rip + 0x8e525f], sil
0061F659  75 0C                           jne 0x14061f667
0061F65B  F7 05 1B 53 8E 00 00 08 00 00   test dword ptr [rip + 0x8e531b], 0x800
0061F665  74 13                           je 0x14061f67a
0061F667  48 8D 0D 12 48 8E 00            lea rcx, [rip + 0x8e4812]
0061F66E  E8 AD 6F BF FF                  call 0x140216620
0061F673  40 8A F0                        mov sil, al
0061F676  84 C0                           test al, al
0061F678  74 39                           je 0x14061f6b3
0061F67A  4C 8D 77 20                     lea r14, [rdi + 0x20]
0061F67E  49 8B 1E                        mov rbx, qword ptr [r14]
0061F681  EB 1A                           jmp 0x14061f69d
0061F683  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061F687  48 85 C0                        test rax, rax
0061F68A  74 0E                           je 0x14061f69a
0061F68C  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061F690  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0061F695  E8 36 B4 09 00                  call 0x1406baad0
0061F69A  48 8B 1B                        mov rbx, qword ptr [rbx]
0061F69D  49 3B DE                        cmp rbx, r14
0061F6A0  75 E1                           jne 0x14061f683
0061F6A2  40 84 F6                        test sil, sil
0061F6A5  74 0C                           je 0x14061f6b3
0061F6A7  48 8D 0D D2 47 8E 00            lea rcx, [rip + 0x8e47d2]
0061F6AE  E8 CD A7 D2 FF                  call 0x140349e80
0061F6B3  48 8B CD                        mov rcx, rbp
0061F6B6  E8 15 27 E6 FF                  call 0x140481dd0
0061F6BB  48 85 FF                        test rdi, rdi
0061F6BE  74 64                           je 0x14061f724
0061F6C0  40 32 F6                        xor sil, sil
0061F6C3  40 38 35 EE 51 8E 00            cmp byte ptr [rip + 0x8e51ee], sil
0061F6CA  75 0C                           jne 0x14061f6d8
0061F6CC  F7 05 AA 52 8E 00 00 08 00 00   test dword ptr [rip + 0x8e52aa], 0x800
0061F6D6  74 13                           je 0x14061f6eb
0061F6D8  48 8D 0D A1 47 8E 00            lea rcx, [rip + 0x8e47a1]
0061F6DF  E8 3C 6F BF FF                  call 0x140216620
0061F6E4  40 8A F0                        mov sil, al
0061F6E7  84 C0                           test al, al
0061F6E9  74 39                           je 0x14061f724
0061F6EB  48 83 C7 30                     add rdi, 0x30
0061F6EF  48 8B 1F                        mov rbx, qword ptr [rdi]
0061F6F2  EB 1A                           jmp 0x14061f70e
0061F6F4  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061F6F8  48 85 C0                        test rax, rax
0061F6FB  74 0E                           je 0x14061f70b
0061F6FD  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061F701  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0061F706  E8 C5 B3 09 00                  call 0x1406baad0
0061F70B  48 8B 1B                        mov rbx, qword ptr [rbx]
0061F70E  48 3B DF                        cmp rbx, rdi
0061F711  75 E1                           jne 0x14061f6f4
0061F713  40 84 F6                        test sil, sil
0061F716  74 0C                           je 0x14061f724
0061F718  48 8D 0D 61 47 8E 00            lea rcx, [rip + 0x8e4761]
0061F71F  E8 5C A7 D2 FF                  call 0x140349e80
0061F724  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0061F729  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
0061F72E  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0061F733  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
0061F738  48 83 C4 30                     add rsp, 0x30
0061F73C  41 5E                           pop r14
0061F73E  C3                              ret
0061F73F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExDeleteLookasideListExWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(v_rsp - 24) = v_xmm0;
    result = DifGetAPIThunkContextById(410, a2, a3, a4);
    if (result == 0) goto loc_0061F6B3;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0061F63C;
    v_stack_m18 = v_stack_p0;
    goto loc_0061F64A;
loc_0061F63C:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    v_rsi = 0;
    v_stack_m10 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9327199)) != 0) goto loc_0061F667;
    if (((*(unsigned int *)(v_rip + 9327387)) & (0x800ULL)) == 0) goto loc_0061F67A;
loc_0061F667:
    result = ExAcquireRundownProtection(v_rip + 9324562, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061F6B3;
loc_0061F67A:
    goto loc_0061F69D;
loc_0061F683:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061F69D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0061F683;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9324498;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExDeleteLookasideListEx(a1, a2, a3, a4);
    if (result == 0) goto loc_0061F724;
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9327086)) != 0) goto loc_0061F6D8;
    if (((*(unsigned int *)(v_rip + 9327274)) & (0x800ULL)) == 0) goto loc_0061F6EB;
loc_0061F6D8:
    result = ExAcquireRundownProtection(v_rip + 9324449, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061F724;
loc_0061F6EB:
    v_rdi = (result) + (48);
    goto loc_0061F70E;
loc_0061F6F4:
    result = *(unsigned __int64 *)(v_rdi) - 16;
    if (*(unsigned __int64 *)(v_rdi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061F70E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi))) != v_rdi) goto loc_0061F6F4;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9324385;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifExDeleteLookasideListExWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(local_rsp - 0x18) = v_xmm0;
    result = DifGetAPIThunkContextById(410, a2, a3, a4);
    if (result == 0) goto loc_0061F6B3;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0061F63C;
    v_stack_m18 = v_stack_p0;
    goto loc_0061F64A;
loc_0061F63C:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    local_rsi = 0;
    v_stack_m10 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E525F)) != 0) goto loc_0061F667;
    if (((*(uint32_t *)(v_rip + 0x8E531B)) & (0x800ULL)) == 0) goto loc_0061F67A;
loc_0061F667:
    result = ExAcquireRundownProtection(v_rip + 9324562, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0061F6B3;
loc_0061F67A:
    goto loc_0061F69D;
loc_0061F683:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0061F69D:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0061F683;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9324498;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ExDeleteLookasideListEx(Arg1, a2, a3, a4);
    if (result == 0) goto loc_0061F724;
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E51EE)) != 0) goto loc_0061F6D8;
    if (((*(uint32_t *)(v_rip + 0x8E52AA)) & (0x800ULL)) == 0) goto loc_0061F6EB;
loc_0061F6D8:
    result = ExAcquireRundownProtection(v_rip + 9324449, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0061F724;
loc_0061F6EB:
    local_rdi = (result) + (48);
    goto loc_0061F70E;
loc_0061F6F4:
    result = *(uint64_t *)(local_rdi) - 16;
    if (*(uint64_t *)(local_rdi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rdi) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0061F70E:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi))) != local_rdi) goto loc_0061F6F4;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9324385;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0061F5F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0061F5F0[BB_0061F5F0]
  bb_0061F629[BB_0061F629]
  bb_0061F630[BB_0061F630]
  bb_0061F63C[BB_0061F63C]
  bb_0061F640[BB_0061F640]
  bb_0061F64A[BB_0061F64A]
  bb_0061F65B[BB_0061F65B]
  bb_0061F667[BB_0061F667]
  bb_0061F67A[BB_0061F67A]
  bb_0061F683[BB_0061F683]
  bb_0061F68C[BB_0061F68C]
  bb_0061F69A[BB_0061F69A]
  bb_0061F69D[BB_0061F69D]
  bb_0061F6A2[BB_0061F6A2]
  bb_0061F6A7[BB_0061F6A7]
  bb_0061F6B3[BB_0061F6B3]
  bb_0061F6C0[BB_0061F6C0]
  bb_0061F6CC[BB_0061F6CC]
  bb_0061F6D8[BB_0061F6D8]
  bb_0061F6EB[BB_0061F6EB]
  bb_0061F6F4[BB_0061F6F4]
  bb_0061F6FD[BB_0061F6FD]
  bb_0061F70B[BB_0061F70B]
  bb_0061F70E[BB_0061F70E]
  bb_0061F713[BB_0061F713]
  bb_0061F718[BB_0061F718]
  bb_0061F724[BB_0061F724]
  bb_0061F73F[BB_0061F73F]
  bb_0061F5F0 -->|branch| bb_0061F6B3
  bb_0061F5F0 -->|fallthrough| bb_0061F629
  bb_0061F629 -->|branch| bb_0061F63C
  bb_0061F629 -->|fallthrough| bb_0061F630
  bb_0061F630 -->|branch| bb_0061F64A
  bb_0061F63C -->|branch| bb_0061F64A
  bb_0061F63C -->|fallthrough| bb_0061F640
  bb_0061F640 -->|flow| bb_0061F64A
  bb_0061F64A -->|branch| bb_0061F667
  bb_0061F64A -->|fallthrough| bb_0061F65B
  bb_0061F65B -->|branch| bb_0061F67A
  bb_0061F65B -->|fallthrough| bb_0061F667
  bb_0061F667 -->|branch| bb_0061F6B3
  bb_0061F667 -->|fallthrough| bb_0061F67A
  bb_0061F67A -->|branch| bb_0061F69D
  bb_0061F683 -->|branch| bb_0061F69A
  bb_0061F683 -->|fallthrough| bb_0061F68C
  bb_0061F68C -->|flow| bb_0061F69A
  bb_0061F69A -->|flow| bb_0061F69D
  bb_0061F69D -->|branch| bb_0061F683
  bb_0061F69D -->|fallthrough| bb_0061F6A2
  bb_0061F6A2 -->|branch| bb_0061F6B3
  bb_0061F6A2 -->|fallthrough| bb_0061F6A7
  bb_0061F6A7 -->|flow| bb_0061F6B3
  bb_0061F6B3 -->|branch| bb_0061F724
  bb_0061F6B3 -->|fallthrough| bb_0061F6C0
  bb_0061F6C0 -->|branch| bb_0061F6D8
  bb_0061F6C0 -->|fallthrough| bb_0061F6CC
  bb_0061F6CC -->|branch| bb_0061F6EB
  bb_0061F6CC -->|fallthrough| bb_0061F6D8
  bb_0061F6D8 -->|branch| bb_0061F724
  bb_0061F6D8 -->|fallthrough| bb_0061F6EB
  bb_0061F6EB -->|branch| bb_0061F70E
  bb_0061F6F4 -->|branch| bb_0061F70B
  bb_0061F6F4 -->|fallthrough| bb_0061F6FD
  bb_0061F6FD -->|flow| bb_0061F70B
  bb_0061F70B -->|flow| bb_0061F70E
  bb_0061F70E -->|branch| bb_0061F6F4
  bb_0061F70E -->|fallthrough| bb_0061F713
  bb_0061F713 -->|branch| bb_0061F724
  bb_0061F713 -->|fallthrough| bb_0061F718
  bb_0061F718 -->|flow| bb_0061F724
```
